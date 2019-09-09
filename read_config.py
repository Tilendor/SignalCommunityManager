#~!/usr/bin/python

import os, sys, getopt
from json import dumps, loads
from secureconfig import SecureJson


new_config = SecureJson.from_file('key', filepath="config.json.enc")
print new_config
