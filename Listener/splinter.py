__author__ = 'xxdpavelxx'

from splinter.browser import Browser
b = browser()
url = "http://sociopages.com/twitter"
b.visit(url)
b.fill('q','ufc')

#6.3,6.5,6.6,6.7,11.1 python cookbook