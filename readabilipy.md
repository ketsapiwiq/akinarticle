readabilipy
```bash

  #  simple_json.py file containing the function simple_json_from_html_string().
   #     Usage:

    from readabilipy import simple_json_from_html_string

    article = simple_json_from_html_string(html_string, content_digests=False, node_indexes=False, use_readability=False)

        The function returns a dictionary with the following fields:
            title: The article title
            byline: Author information
            content: A simplified HTML representation of the article, with all article text contained in paragraph elements.
            plain_content: A "plain" version of the simplified Readability.js article HTML present in the content field. This attempts to retain only the plain text content of the article, while preserving the HTML structure.
            plain_text: A list containing plain text representations of each paragraph (<p>) or list (<ol> or <ul>) present in the simplified Readability.js article HTML in the content field. Each paragraph or list is represented as a single string. List strings look like "* item 1, * item 2, * item 3," for both ordered and unordered lists (note the trailing ,).

```