"""
yanindeb: y(et )an(other )in(teractive )de(velopment )b(log)
------------------------------------------------------------
by mark <mark@joshwel.co>

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

from os import environ
from pathlib import Path
from subprocess import run
from sys import stderr
from typing import Final, NamedTuple

import marko

# constants
DIR_REPOSITORY_ROOT: Final[Path] = Path(__file__).parent.parent
DIR_POSTS: Final[Path] = DIR_REPOSITORY_ROOT.joinpath("posts/")
DIR_PUBLIC: Final[Path] = DIR_REPOSITORY_ROOT.joinpath("public/")
PLACEHOLDER_TITLE: Final[str] = "<!-- title placeholder -->"
PLACEHOLDER_META: Final[str] = "<!-- meta placeholder -->"
PLACEHOLDER_STYLE: Final[str] = "<!-- style placeholder -->"
PLACEHOLDER_NAVLI: Final[str] = "<!-- navli placeholder -->"
PLACEHOLDER_BANNER: Final[str] = "<!-- banner placeholder -->"
PLACEHOLDER_CONTENT: Final[str] = "<!-- content placeholder -->"
NAVLI_TEMPLATE: Final[
    str
] = """<li>
  <a href="{href}">
  <b>{title}</b><br>
  {description}
  </a>
</li>"""
BANNER: Final[
    str
] = """<h1>
    <span>y</span>et
    <span>an</span>other
    <span>in</span>teractive
    <span>de</span>velopment
    <span>b</span>log
   </h1>"""

# replace maps
#   POSTMARKO_REPLACE_MAP: replaces h1-h6 with h2-h6
#   because the markdown files are written with h1 as the title
POSTMARKO_REPLACE_MAP: Final[dict[str, str]] = {
    "<h6>": "<h6>",  # clamp at h6
    "<h5>": "<h6>",
    "<h4>": "<h5>",
    "<h3>": "<h4>",
    "<h2>": "<h3>",
    "<h1>": "<h2>",
    "</h6>": "</h6>",
    "</h5>": "</h6>",
    "</h4>": "</h5>",
    "</h3>": "</h4>",
    "</h2>": "</h3>",
    "</h1>": "</h2>",
}

CLEANUP_REPLACE_MAP: Final[dict[str, str]] = {
    "</meta>": "",
    "<meta/>": "",
    "<meta />": "",
}


class YanindebPost(NamedTuple):
    number: int
    title: str
    content: str


def yanindeb_inject(html: str, post_number: int) -> str:
    """injects semantic tags into marko-generated html"""

    section = 0
    new_html: str = "<header>"
    window: str = ""

    for char in html:
        new_html += char
        window += char

        if window.endswith("</h2>"):
            section += 1
            new_html += (
                f'<p>Week {post_number:>02}</p> </header> <section id="s{section}">'
            )
            window = ""

        elif any(
            hr_type := [
                window.endswith("<hr>"),
                window.endswith("<hr/>"),
                window.endswith("<hr />"),
            ]
        ):
            hr_length: int = 4
            match hr_type:
                case [True, False, False]:
                    hr_length = 4
                case [False, True, False]:
                    hr_length = 5
                case [False, False, True]:
                    hr_length = 6

            section += 1
            new_html = (
                new_html[:-hr_length]
                + ("</section> " if section > 1 else "")
                + f'<section id="s{section}">'
            )
            window = ""

        else:
            continue

        # unreachable if no match
        window = ""

    return new_html + ("</section>" if "<section" in new_html else "")


def apply_replace(text: str, replace_map: dict[str, str]) -> str:
    """utlity function to applies replace_map to text"""

    for key, value in replace_map.items():
        text = text.replace(key, value)

    return text


def main() -> None:
    """command-line entry function"""

    # pre-run checks
    print("yanindeb generator", file=stderr)

    if not DIR_POSTS.exists():
        print(
            "error: posts directory does not exist (is script in /src?)",
            file=stderr,
        )
        exit(1)

    if not DIR_PUBLIC.exists():
        print(
            "error: public directory does not exist (is script in /src?)",
            file=stderr,
        )
        exit(2)

    # (dark) gather targets
    targets: list[YanindebPost] = []
    print(f"info: scanning {DIR_POSTS}", file=stderr)

    for post_file in DIR_POSTS.iterdir():
        post_filename = post_file.stem.split("-")[0]

        if not post_file.suffix == ".md":
            print(f"      skipping {post_filename} (not a markdown file)", file=stderr)
            continue

        match post_filename.split(maxsplit=1):
            # usual post filename format: '<number> <qualified title>.md'

            case [left, right]:
                if left.isdigit():  # first part of filename is a number; this is a post
                    targets.append(
                        YanindebPost(
                            number=int(left),
                            title=right.strip(),
                            content=post_file.read_text(),
                        )
                    )

                    print(
                        f"      targetting {targets[-1].number} - '{targets[-1].title}'",
                        file=stderr,
                    )

    if len(targets) == 0:
        print("warn: nothing to do. (no posts found)", file=stderr)
        exit(0)

    targets.sort(key=lambda post: post.number, reverse=True)

    # open template
    post_template = DIR_REPOSITORY_ROOT.joinpath("src/template.html").read_text(
        encoding="utf-8"
    )

    # preprocess posts to generate navigation
    navli: list[str] = []
    for n, post in enumerate(targets):
        navli.append(
            NAVLI_TEMPLATE.format(
                href="/" if (n == 0) else f"/{post.number}",
                title=f"Week {post.number:>02}",
                description=post.title,
            )
        )

    # process posts
    for n, post in enumerate(targets):
        post_specific_replace_map: dict[str, str] = {
            PLACEHOLDER_TITLE: f"Week {post.number:>02}",
            PLACEHOLDER_META: (
                f'<meta name="title" content="Week {post.number:>02}">\n'
                f'<meta name="description" content="{post.title}">'
            ),
            # TODO
            # PLACEHOLDER_STYLE: "TODO",
            PLACEHOLDER_NAVLI: "".join(navli),
            PLACEHOLDER_CONTENT: yanindeb_inject(
                html=apply_replace(marko.convert(post.content), POSTMARKO_REPLACE_MAP),
                post_number=post.number,
            ),
        }

        # create post html from template
        post_html: str = apply_replace(post_template, post_specific_replace_map)

        # restore banner (can't be done so previously due to bs4 formatting rules)
        post_html = post_html.replace(PLACEHOLDER_BANNER, BANNER)
        post_html = apply_replace(post_html, CLEANUP_REPLACE_MAP)

        DIR_PUBLIC.joinpath(
            "index.html" if (n == 0) else f"{post.number}.html"
        ).write_text(
            post_html,
            encoding="utf-8",
        )

        # format
        # post_html = bs4.BeautifulSoup(post_html, "html.parser").prettify(
        #     # formatter=formatter
        # )
        format_args: list[str] = [
            environ.get("YANCMD", "bunx"),
            "prettier",
            "--write",
            "public",
        ]
        print(f"info: running format command '{' '.join(format_args)}'")
        run(
            args=format_args,
            cwd=DIR_REPOSITORY_ROOT,
        )


if __name__ == "__main__":
    main()
