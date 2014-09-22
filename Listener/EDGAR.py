import urllib2

#url = "http://example.com"

#openerDirective1 = ...
#openerDirective2 = ...

#opener = urllib2.build_opener(openerDirective1, openerDirective2)

#urllib2.install_opener(opener)

#website = urllib2.urlopen(url)


authDirective = urllib2.HTTPBasicAuthHandler()
realm = "Webmail"
url = "http://example.com/webmail/"
username = "leethaxxer"
password = "letmein"
authDirective.add_password(realm, url, username, password)

opener = urllib2.build_opener(authDirective)
urllib2.install_opener(opener)