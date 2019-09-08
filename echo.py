from pydbus import SystemBus, SessionBus
from gi.repository import GLib

bus = SystemBus()
#bus = SessionBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal')


def msgRcv(timestamp, source, groupID, message, attachments):
   print("msgRcv called")
   print(message)
   print('Echoing')
   signal.sendMessage('Your Face: ' + message, None, [source])
   return


signal.onMessageReceived = msgRcv
loop.run()
