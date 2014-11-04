import mechanize
import argparse
import sys 

parser = argparse.ArgumentParser(description='Post to fb')
parser.add_argument('-u','--user', help='username or email of fb account', required=True)
parser.add_argument('-p','--pass', help='password of the fb account', required=True)
parser.add_argument('-m','--msg', help='message to post to the fb account', required=True)
args = vars(parser.parse_args())

url = "https://m.facebook.com"
op = mechanize.Browser()
op.set_handle_robots(False)
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)')]
print 'Opening url ' + url
op.open(url)
op.forms()
op.select_form(nr=0)
op.form["email"] = args['user']
op.form["pass"] = args['pass']
print 'Using ' + op.form["email"] + " to login ..."
r = op.submit()
if 'login' in r.read(): 
   print 'Could not login. Please check your credentials'
   sys.exit()
op.select_form(nr=1)
op.form['xc_message']=args['msg']
rt = op.submit('view_post')
if 'Your status has been updated' in rt.read(): print 'Your status has been updated'
