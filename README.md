#Wordbrutepress
Wordpress Brute Force Multithreading with standard and xml-rpc login method written in python.
<pre>	
Coded By :      Claudio Viviani
                http://www.homelab.it
                http://adf.ly/1F1MNw (Full HomelabIT Archive Exploit)
                http://ffhd.homelab.it (Free Fuzzy Hashes Database)
                
                info@homelab.it
                homelabit@protonmail.ch

                https://www.facebook.com/homelabit
                https://twitter.com/homelabit
                https://plus.google.com/+HomelabIt1/
                https://www.youtube.com/channel/UCqqmSdMqf_exicCe_DjlBww
</pre>
#Features:
<pre>
1) Multithreading
2) xml-rpc brute force mode
3) http and https protocols support
4) Random User Agent
</pre>
#Usage:
<pre>
Standard login request:

python wordbrutepress.py -S -t http[s]://target.com[:port] -u username -w wordlist [--timeout in sec]

Xml-rpc login request:

python wordbrutepress.py -X -t http[s]://target.com[:port] -u username -w wordlist [--timeout in sec]
</pre>
#CHANGELOG
<pre>
 2015-04-12 v2.0
 1) Add new feature: xml-rpc brute force mode
 2) Fix minor bugs

 2015-04-11 v1.1
 1) optparse (Deprecated since version 2.7) replaced by argparse
 2) Fix connection bugs
</pre>
