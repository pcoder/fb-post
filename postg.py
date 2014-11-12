import mechanize
import argparse
import sys 
import ConfigParser
import re

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
users = dict(Config.items('users'))
#groups = list(Config.items('groups'))
#url = "https://m.facebook.com"
#op = mechanize.Browser()
#op.set_handle_robots(False)
#op.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)')]

def postfb(user, passw, msg):
   url = "https://m.facebook.com"
   op = mechanize.Browser()
   op.set_handle_robots(False)
   op.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)')]
   print 'Opening url ' + url
   op.open(url)
   op.select_form(nr=0)
   op.form["email"] = user
   op.form["pass"] = passw
   print 'Using ' + op.form["email"] + " to login ..."
   r = op.submit()
   if 'login' in r.read(): 
      print '  ERR: Could not login. Please check your credentials'
      sys.exit()
   groups = None
   with open('groups.ini') as f:
      groups = f.read().splitlines()
   for g in groups:
      postGroup(op, g, msg)

#   links = list(op.links())
#   groupsl = None
#   l = op.links(text_regex=re.compile("Groups"))
#   lstl = list(l)
#   groupsl = lstl[0]
#   # follow the groups link
#   rl = op.follow_link(groupsl)

   # we are in the groups page; get the link of the specified page
   #nl = list(op.links(text_regex=re.compile("Group1")))
   #res_t = op.follow_link(nl[0]) 
   #op.select_form(nr=1)
   #op.form['xc_message']="Hi, Welcome to Group1"
   #rt = op.submit('view_post')
   #print 'Your status has been updated'
   #print '====='
   op.close() 

def postGroup(op, group, msg):
   print 'Posting to ' + group
   op.open(group)
   op.select_form(nr=1)
   op.form['xc_message']=msg
   rt = op.submit('view_post')
   print group + ' status has been updated'
   print '====='
 
parser = argparse.ArgumentParser(description='Post to fb')
parser.add_argument('-m','--msg', help='message to post to the fb account', required=True)
args = vars(parser.parse_args())

for u in users:
   print u + " => " +users[u]
   postfb(u, users[u],args['msg'])

 
