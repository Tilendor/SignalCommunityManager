#~!/usr/bin/python

import os, sys, getopt
from json import dumps, loads
from secureconfig import SecureJson

def main(argv):

   signal_phone_number = argv[0]
   aliases = argv[1:]

   config_path = 'config.json.enc'
   config = SecureJson.from_file('key')

   config.cfg['signal_phone_number'] = signal_phone_number
   config.cfg['aliases'] = aliases

   print(config)

   with open(config_path,'w+') as f:   
      SecureJson.write(config,f)
   
   new_config = SecureJson.from_file('key', filepath=config_path)
   print new_config

if __name__ == "__main__":
   main(sys.argv[1:])
