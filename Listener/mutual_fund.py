#This is the beta version of the program that analyzes mutual funds on the EDGAR data base by 
#viewing stock holdings from 13F-HR forms. 

__author__ = 'xxdpavelxx'
#6.3,6.5,6.6,6.7,11.1 python cookbook

import requests
import feedparser
from htmlParser import MyHTMLParser
import lxml
from lxml import etree, objectify
import datetime
from concurrent import futures

from io import StringIO, BytesIO
#Base URL being accessed
#url = 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&type=&dateb=&owner=exclude&start=0&count=40&output=atom'
cik_list= ['0001166559','0000019034','0000865898','0001342947'] #raw_input('Please enter a CIK number:')
#print cik
start = datetime.datetime.now()
#print start



#return sec page url
#parameter is cik number

def getLatestFiling( cik, filingType="13F-HR"):
    payload = {'CIK': cik,'action':'getcompany','type':"","dateb":"","owner":"exclude","start":"0","count":40,"output":'atom'}
    r = requests.get("http://www.sec.gov/cgi-bin/browse-edgar", params=payload)
    feed = feedparser.parse(r.text)
    for entry in feed['entries']:
        #print 'test'+entry.title
        if '13F-HR' in entry.title:
            print entry.link
            return entry.link
    print "No filing found for "+ cik +" please try a different CIK number."
    return ""

#returns link to sec filing text file
#parameter - sec page url
def getFilingTextFile(secPageUrl):
    parser = MyHTMLParser()
    r = requests.get(secPageUrl)
    parser.feed(r.text)
    return 'http://www.sec.gov'+parser.linkToTextFile

# return dictionary of holding and % of holdings
def getHoldings(linkToTextFile):
    print linkToTextFile
    r = requests.get(linkToTextFile)
    XMLer= str(r.text.replace('&', '&amp;'))
    #print XMLer
    start= XMLer.find('<informationTable')
    end= XMLer.find('</informationTable>')
    a= XMLer[start:end+19]  #string type
    #print a
    #tree = etree.parse(StringIO(a))

    lxml_form = etree.fromstring(a)
    #print type(lxml_form)

    for child in lxml_form.getiterator():
        if not hasattr(child.tag, 'find'): continue  # (1)
        i = child.tag.find('}')
        if i >= 0:
            child.tag = child.tag[i+1:]
        if 'nameOfIssuer' in child.tag:
            print child.tag, '-', child.text
        if 'value' in child.tag:
            print child.tag, '-', child.text
            print ('--------------------------------------------------------------------------------------------')

    #print #lxml.etree.XTMl(a)
    #root = etree.fromstring(r.text.replace('&', '&amp;'))
    #print root

#def printFormattedHoldings(holdings):

#bad sik= 0000002110

#cik='0001166559'
#h='http://www.sec.gov/Archives/edgar/data/1166559/000110465914039387/0001104659-14-039387-index.htm'
#with futures.ProcessPoolExecutor(4) as pool:
#    pool.map(getLatestFiling,)
for link in map(getLatestFiling, cik_list):
        #link=getLatestFiling(cik)

        if link!='':

            filingLink=getFilingTextFile(link)
            getHoldings(filingLink)


end = datetime.datetime.now()
runtime = end-start
print "total run time:",runtime
#print getFilingTextFile(h)



