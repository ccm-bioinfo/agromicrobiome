# Agromicrobiome's documentation

### Setup

1. Install **Python 3.12** on an **Ubuntu 22.04** machine to make your
development environment consistent with the one used by the GitHub Action that
builds the webpage.
2. Clone this repository.
3. Install pip dependencies:

    ```text
    pip install -r requirements.txt
    ```

### Creating new pages

1. Create a Markdown file in the `source/` directory. For example:
    ```text
    touch source/mypage.md
    ```
2. Fill it with contents. It supports [MyST Markdown](https://mystmd.org/guide/quickstart-myst-markdown),
   a superset of standard Markdown. The header will be used as the title of your
   page. For example:
    ```markdown
    ### This is my page

    Here I can write my **bold**, *italics*, and <u>underlined</u> text.
    ```
3. Add your page to the index. To do that, append the name of the file (relative
   to the `source/` directory) in the `source/index.rst` file. For example:
    ```rst
    Main title
    ==========
    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       mypage.md
       anotherpage.md
    ```

### Previewing your edits

1. Build the webpage from root directory:
    ```text
    sphinx-build source/ build/html
    ```
2. Serve the webpage locally:
    ```text
    python3 -m http.server -d build/html/ 12345
    ```
3. Browse the webpage at http://0.0.0.0:12345/.

### Publishing your edits

1. Add your files to git index:
    ```text
    git add .
    ```
2. Create a commit with a descriptive commit message:
    ```text
    git commit -m 'feat: create mypage.md'
    ```
3. Push your changes to main branch.
    ```text
    git push
    ```
4. Wait until the webpage is built. You can browse its progress [here](https://github.com/ccm-bioinfo/agromicrobiome/actions).
5. Once built, your changes will be reflected in the repository's GitHub page:
   https://ccm-bioinfo.github.io/agromicrobiome
