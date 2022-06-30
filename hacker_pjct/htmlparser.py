from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : ", tag)

    def handle_endtag(self, tag):
        print("End : ", tag)

    def handle_data(self, data):
        print("-> ", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>HTML Parser - I</title></head>'
            '<body data-modal-target class=1><h1>HackerRank</h1><br /></body></html>')

