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
   op.select_form(nr=0)
   op.form["email"] = user
   op.form["pass"] = passw
   print 'Using ' + op.form["email"] + " to login ..."
   r = op.submit()
   if 'login' in r.read(): 
      print '  ERR: Could not login. Please check your credentials'
      sys.exit()
   op.select_form(nr=1)
   rt=None
   try: 
      if 'xc_message' in op.form:
         print '   Found xc_message!'
         op.form['xc_message']=args['msg']
         rt = op.submit('view_post')
   except:
      print '  Can not find xc_message, trying out status ...'
      try:
         if 'status' in op.form:
            print '   Found status!'
            op.form['status']=args['msg']
            rt = op.submit('update')
      except:
         print 'Can neither find xc_message nor status. ERROR'
         sys.exit()

   if 'Your status has been updated' in rt.read(): print 'Your status has been updated'
   print '====='
   op.close() 
 
parser = argparse.ArgumentParser(description='Post to fb')
parser.add_argument('-m','--msg', help='message to post to the fb account', required=True)
args = vars(parser.parse_args())

for u in users:
   print u + " => " +users[u]
   postfb(u, users[u],args['msg'])

 
