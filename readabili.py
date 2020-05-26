
#  simple_json.py file containing the function simple_json_from_html_string().
#     Usage:
import os
import json
from ReadabiliPy.readabilipy import simple_json_from_html_string
path = 'data/articles/bafe/'

with open('data/articles/readable_bafe.jsonl', 'w+') as jsonl:
    for file in os.listdir(path):
        if(file.endswith('.html') and not file.endswith('.pdf.html')):
            with open(path+file, 'r') as html_file:
                try:
                    html = html_file.read()
                except UnicodeDecodeError:
                    try:
                        print("Trying to open ", file, " in latin-1")
                        # html = open(path+file, 'r', encoding='ISO-8859-1').read()
                        html = open(path+file, 'r', encoding='latin-1').read()
                        article = simple_json_from_html_string(
                            html, use_readability=True)
                    except:
                        print("Bug, abandoning this one")
                        pass
                try:
                    article = simple_json_from_html_string(
                        html, use_readability=True)
                # article = simple_json_from_html_string(html_file.read(), use_readability=True)
                    print("Writing ", article['title'])
                except KeyboardInterrupt:
                    sys.exit()
                    pass
                except:
                    print("Bug, abandoning this one")
                    pass
                jsonl.write(json.dumps(article))
                jsonl.write("\n")
