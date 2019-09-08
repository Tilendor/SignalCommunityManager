#~!/usr/bin/python

import getopt, os, re, sys
from json import dumps, loads
from secureconfig import SecureJson
from pydbus import SystemBus, SessionBus
from gi.repository import GLib

bus = SystemBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal')

config_file = 'config.json.enc'
config = SecureJson.from_file('key', filepath=config_file)

class HelpHandler:

    def process(self,message, source, groupID):
        if not re.search("help",message):
            return False
        signal.sendMessage("Right now, the only command is help, which you already used",None,[source])
        return True


handlers = [HelpHandler()]








def msgRcv(timestamp, source, groupID, message, attachments):
    alias_present = re.search( config.cfg["aliases"],message)

    if groupID and not alias_present:
        print("Not Addressed to me")
        return

    if not groupID and alias_present:
        signal.sendMessage("Oh!  No need to be so formal between you and me.  My name is optional in these chats, just type the commands directly.  ;)",None,[source])
        message = re.sub(config.cfg["aliases"] + "\s*","",message)

    message_handled = False

    for handler in handlers:
        message_handled = handler.process(message,source,groupID) or message_handled

    if not message_handled:
        print("no match")
        signal.sendMessage("My apologies, curse my lack of flexibility!  I didn't see a command to process.  Use the Command help and I'll tell you all about the things I can do.",None,[source])

    return


signal.onMessageReceived = msgRcv
loop.run()
