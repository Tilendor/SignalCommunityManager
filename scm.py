#~!/usr/bin/python

import getopt, os, re, sys
from json import dumps, loads
from secureconfig import SecureJson
from pydbus import SystemBus, SessionBus
from gi.repository import GLib

from configuration import Configuration
from signaler import Signaler
from handlers.add_me import AddMe
from handlers.introduction import Introduction
from handlers.help import Help
from handlers.say import Say
from handlers.create_group import CreateGroup

bus = SystemBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal')

config = Configuration()

signaler = Signaler(signal)

handlers = [CreateGroup(signaler, config), 
            AddMe(signaler, config),
            Introduction(signaler,config.aliases_rgx), 
            Say(signaler)]

help = Help(signaler,handlers)
handlers.append(help)


def msgRcv(timestamp, source, groupID, message, attachments):
    alias_present = re.search( config.aliases_rgx ,message,re.IGNORECASE)

    if groupID and not config.group_exists(groupID):
      name = signaler.get_group_name(groupID)
      config.new_group(groupID,name)

    if groupID and not alias_present:
        print("Not Addressed to me")
        return

    if not groupID and alias_present:
        signal.sendMessage("Oh!  No need to be so formal between you and me.  My name is optional in a direct message, just type the commands directly.  ;)",None,[source])
    message = re.sub(config.aliases_rgx + "\s*","",message, flags=re.IGNORECASE)

    message_handled = False

    for handler in handlers:
        message_handled = handler.process(message,source,groupID) or message_handled

    if not message_handled:
        print("no match")
        signal.sendMessage("My apologies, curse my lack of flexibility!  I didn't see a command to process in '%s'.  Use the Command help and I'll tell you all about the things I can do." % (message) ,None,[source])

    return


signal.onMessageReceived = msgRcv
loop.run()
