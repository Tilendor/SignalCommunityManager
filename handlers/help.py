import re

class Help():

  def __init__(self,signaler,commands):
    self.signaler = signaler
    self.command = 'help'
    self.summary = 'Lists all Commands, and detailed information on specific commands'
    self.usage = "'help'  or 'help <command>'"
    self.description = 'Publishes information on all available commands'
    self.help_text = "Here are the available commands I can handle.\n\n"
    for c in commands:
      self.help_text += "'%s' - %s\n" %(c.command, c.summary)
    self.commands = commands

  def process(self,message,source,groupID):
     if not re.search("^" + self.command, message, re.IGNORECASE):
       return False
     after_text = re.sub("^" + self.command + "\s*","",message,flags=re.IGNORECASE)
     print("After Text:%s" % (after_text))
     if not after_text:
       self.signaler.reply(self.help_text,source,None)
       return True
     for c in self.commands:
       if re.search("^" + c.command,after_text,re.IGNORECASE):
          self.signaler.reply("Command: %s\nSummary: %s\nUsage: %s\nDescription: %s" %(c.command, c.summary, c.usage, c.description),source,None)
          return True
     return False
     

