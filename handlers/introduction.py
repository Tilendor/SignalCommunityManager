import re

class Introduction():

  def __init__(self,signaler,aliases_rgx):
    self.command = 'introduce yourself'
    self.summary = 'Just saying hello'
    self.usage = "'introduce yourself'"
    self.description = "Give my names, tells about the help command, and expresses goodwill."    

    self.signaler = signaler

    aliases = aliases_rgx[1:].split('|')
    akas = ",".join(aliases[1:])
    self.intro_message = "Greetings, I am %s (AKA %s)." %(aliases[0], akas)
    self.intro_message += (" I am here to take the drudgery out of growing a Signal Community."
                            "\n\n You can message me directly, or if in a group, please address me by name."
                            "\n\n Type help to learn about the many things I can do for you."
                            "\n\n It is my pleasure to be of service.")


  def process(self,message,source,groupID):
    if not re.search("^" + self.command,message,re.IGNORECASE):
      return False
    self.signaler.reply(self.intro_message,source,groupID)
    return True
