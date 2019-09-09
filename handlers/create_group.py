import re

class CreateGroup():

  def __init__(self,signaler,config):
    self.signaler = signaler
    self.config = config
    self.command = 'start topic'
    self.summary = 'Creates a new joinable group with the given topic'
    self.usage = "'start topic <name>'"
    self.description = "Creates a group with the given name and automatically adds the user.  If used in a group, others in that group can also join the new one."
 

  def process(self,message,source,groupID):
    if not re.search("^" + self.command, message, re.IGNORECASE):
      return False
    name = re.sub("^" + self.command + "\s*","",message,flags=re.IGNORECASE)
    
    newGroupID = self.signaler.create_group(name,source)
    self.config.new_group(newGroupID,name)

    create_message = "Group %s created!" % (name)
    if groupID:
       self.config.set_last_created_group(groupID,newGroupID)
       create_message += " Others can join by typing '%s add me'" % (self.config.default_alias)
    
    self.signaler.reply(create_message,source,groupID)
    return True
    
