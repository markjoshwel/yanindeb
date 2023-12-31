# y(et )an(other )in(teractive )de(velopment )b(log)

an exercise in styling a website while prioritising correct non-styled layout and
semantic use of html/css  
(also because we have to make one to submit for my polytechnic course)

also an exercise in creating a markdown-to-html generator for a near-future project

- [project/website structure](#projectwebsite-structure)
- [developing](#developing)
  - [workflows](#workflows)
    - [prototyping with tailwind](#prototyping-with-tailwind)
    - [updating content](#updating-content)
    - [updating templates](#updating-templates)
    - [publishing](#publishing)
- [licence](#licence)
  - [third-party open source licences](#third-party-open-source-licences)

## project/website structure

```text
.
├── public/
│   └── ...
├── public/
│   ├── font/
│   │   └──
│   ├── media/
│   │   └── ...
│   ├── style.css
│   ├── index.html
│   └── ...
├── src/
│   └── yanindeb.py
├── devbox.json
├── pyproject.toml
└── README.md
```

- [posts/](posts/)  
  where the markdown files used to generate blog pages are stored

  - \*.md  
    the markdown files used to generate blog pages, named after their respective week
    numbers

- [public/](public/)  
  where the website is stored

  - [font/](public/font/)  
    where the fonts used by the website are stored

  - [media/](public/media/)  
    where media used by the website are stored

  - [style.css](public/style.css)  
    the stylesheet used by the website

  - [style.giscus.css](public/style.giscus.css)  
    the stylesheet used by the giscus comment widget

  - [index.html](public/index.html)  
    the main page of the website, is the latest blog post

  - \*.html  
    the older blog posts of the website, named after their respective week numbers

- [src/](src/)  
   where the website tooling and tailwindcss stylesheet is stored

  - [yanindeb.py](src/yanindeb.py)  
    the tooling script used to generate blog pages from markdown files in [posts/](posts/)

## developing

yanindeb is developed using:

- [nix](https://nixos.org/) using [devbox](https://www.jetpack.io/devbox/)  
  project dependency manager

  - [bun](https://bun.sh/)  
    an alternative javascript runtime and javascript package/dependency manager

    - [tailwindcss](https://tailwindcss.com/) (`>=4.0.0`)  
      css framework for rapid prototyping (css is handwritten afterwards)

      - [prettier](https://prettier.io/))  
        html formatter

  - [python](http://python.org/) (`>=3.10`)  
    programming language for website tooling

    - [poetry](https://python-poetry.org/)  
      python dependency manager

      - [marko](https://pypi.org/project/marko/)  
        markdown parser

a prototyping environment will require tailwind to be available on your system.  
else, **having python, poetry and prettier are the minimum prerequisites** to run the
tooling script.

if you have devbox, run the following to quickly hop into a development environment:

```shell
devbox shell
```

### workflows

there are a few workflows for developing/maintaining yanindeb:

<!-- todo lol -->

#### prototyping with tailwind

1. uncomment the following or a similar line in the html file you are working on:

   ```html
   <!-- <link rel="stylesheet" href="./style.tailwind.css"> -->
   ```

2. start a tailwind watcher:

   ```shell
   bunx tailwindcss -i ./src/style.tailwind.css -o ./public/style.tailwind.css --watch
   ```

3. et voilà, you can now use tailwind utility classes. happy prototyping!

4. remember to comment out the line you uncommented in step 1, or all hell breaks loose
   definitely.  
   hit sunt dracones.

#### updating content

1. edit the markdown files in `./posts/`

2. run:

   ```shell
   poetry run yanindeb
   ```

   > [!NOTE]  
   > this will run prettier, so ensure you have it installed and available on your system!  
   > yanindeb will assume you have bun and thus bunx, but you can specify npx by using
   > `YANCMD=npx yanindeb` instead.

   heed and fix any errors raised before proceeding.

3. et voilà, you can now view the updated content in `./public/`. happy updating!

#### updating templates

edit the html file in `./src/template.html`

the following placeholders are used:

- head placeholders

  - title placeholder

    used to insert the title of the page

    ```html
    <!-- title placeholder -->
    ```

  - meta tag placeholder

    used to insert the title and description meta tags

    ```html
    <!-- meta placeholder -->
    ```

  - stylesheet override placeholder

    used to insert any overriding stylesheets, such as for defining
    a custom colour palette

    ```html
    <!-- style placeholder -->
    ```

- banner placeholder

  ```html
  <!-- banner placeholder -->
  ```

  is replaced with

  ```html
  <span>y</span>et
  <span>an</span>other
  <span>in</span>teractive
  <span>de</span>velopment
  <span>b</span>log
  ```

  (this is done seperately due to formatting issues)

- page navigation placeholder

  used to insert generated page navigation links as list elements

  ```html
  <!-- navli placeholder -->
  ```

- content placeholder

  used to insert generated content inside a `<main>` element

  ```html
  <!-- content placeholder -->
  ```

#### publishing

a continuous deployment workflow is used to publish yanindeb to Github Pages.

in the event of environmental, social, economic, or structural collapse, yanindeb (after
tooling has had its way with it) is always available in the `./public/` directory.

## licence

yanindeb’s content is dedicated to the public domain, marked by
[Creative Commons Zero v1.0 Universal Licence](https://creativecommons.org/publicdomain/zero/1.0/).

yanindeb’s codebase is free and unencumbered software released into the public domain,
marked by the [Unlicence](https://unlicense.org/).

### third-party open source licences

yanindeb uses the following third-party open source fonts:

1. [DT Nightingale by Death of Typography & Celia Yew](https://deathoftypography.com/nightingale/)

   this is a really cool font from a local (singaporean) type foundry, it’s great and if
   you’re another student taking a look around yanindeb or just someone who may want a few
   neat fonts, please check them out!

   the font is licensed under the [SIL Open Font License v1.1](public/font/nightingale.OFL-1.1).

2. BDO Grotesk by Lokal Container

   ([website](https://lokalcontainer.com/), [repository](https://github.com/Lokal-Container/BDO-Grotesk))

   the font is licensed under the [SIL Open Font License v1.1](public/font/BDOGrotesk-OFL-1.1.txt).

3. 0xProto by 0xType

   ([website](https://0xtype.dev/), [repository](https://github.com/0xType/0xProto))

   the font is licensed under the [SIL Open Font License v1.1](public/font/0xProto.OFL-1.1.txt).

4. Material Symbols by Google

   ([website](https://fonts.google.com/icons), [repository](https://github.com/google/material-design-icons))

   the font is licensed under the [Apache License 2.0](public/font/material-symbols_sharp.Apache-2.0).
