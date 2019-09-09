import re, random

class Say():

  def __init__(self,signaler):
    self.signaler = signaler
    self.command = 'say'
    self.summary = 'repeats back what you said'
    self.usage = "'say <something>'"
    self.description = "Simple example of repeating back text, with a little quirkiness thrown in"
    self.snark_count = random.randrange(3, 8)

  def process(self,message,source,groupID):
    if not re.search("^" + self.command, message, re.IGNORECASE):
      return False
    text = re.sub("^" + self.command + "\s*","",message,flags=re.IGNORECASE)
    self.signaler.reply(text,source,groupID)
    self.snark_count = self.snark_count - 1
    if self.snark_count <= 0:
      self.signaler.reply("Feeling amused?",source,groupID)
      self.snark_count = random.randrange(5,10)
    return True
