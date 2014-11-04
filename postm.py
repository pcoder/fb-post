import mechanize
import argparse
import sys 
import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("config.ini")
users = dict(Config.items('users'))

def postfb(user, passw, msg):
   url = "https://m.facebook.com"
   op = mechanize.Browser()
   op.set_handle_robots(False)
   op.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)')]
   print 'Opening url ' + url
   op.open(url)
   op.forms()
   op.select_form(nr=0)
   op.form["email"] = user
   op.form["pass"] = passw
   print 'Using ' + op.form["email"] + " to login ..."
   r = op.submit()
   if 'login' in r.read(): 
      print '  ERR: Could not login. Please check your credentials'
      sys.exit()
   op.select_form(nr=1)
   op.form['xc_message']=args['msg']
   rt = op.submit('view_post')
   if 'Your status has been updated' in rt.read(): print 'Your status has been updated'
   print '====='
  
 
parser = argparse.ArgumentParser(description='Post to fb')
parser.add_argument('-m','--msg', help='message to post to the fb account', required=True)
args = vars(parser.parse_args())

for u in users:
   print u + " => " +users[u]
   postfb(u, users[u],args['msg'])

 
