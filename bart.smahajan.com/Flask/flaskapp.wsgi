#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/bart.smahajan.com/Flask/")
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
from Flask import app as application