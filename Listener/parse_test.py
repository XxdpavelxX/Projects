__author__ = 'xxdpavelxx'
from HTMLParser import HTMLParser
import requests
import re

# create a subclass and override the handler methods

list1 = []
def handle_starttag(self, tag, attrs):
    #print "Encountered a start tag:", tag
    if tag=='a':
        match = re.findall(r'u[\D]{22}[0-9]+/[0-9]+/[0-9]+-[0-9]+-[0-9]+.txt[\D]',attrs)
        #print match
        for attr in attrs:
            list1.append(attr)
            print list1

            #print attrs
            #print "     attr:", attr
#def handle_endtag(self, tag):
    #print "Encountered an end tag :", tag
def handle_data(self, data):
    if (data=='Complete submission text file'):
        print "Encountered some data  :", data


# instantiate the parser and fed it some HTML
#parser = MyHTMLParser()
r = requests.get("http://www.sec.gov/Archives/edgar/data/1166559/000104746907006532/0001047469-07-006532-index.htm")
#parser.feed(r.text)
print handle_starttag()