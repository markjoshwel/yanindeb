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

from pathlib import Path
from sys import stderr

DIR_REPOSITORY_ROOT = Path(__file__).parent.parent
DIR_POSTS = DIR_REPOSITORY_ROOT / "posts"
DIR_PUBLIC = DIR_REPOSITORY_ROOT / "public"


def main():
    print("yanindeb generator", file=stderr)

    if not DIR_POSTS.exists():
        print("error: posts directory does not exist (is script in /src?)", file=stderr)
        exit(1)

    if not DIR_PUBLIC.exists():
        print(
            "error: public directory does not exist (is script in /src?)", file=stderr
        )
        exit(2)


if __name__ == "__main__":
    main()
