import re

class AddMe():

  def __init__(self,signaler,config):
    self.signaler = signaler
    self.config = config
    self.command = 'add me'
    self.summary = 'Adds the requester to the most recently created group mentioned in the current group'
    self.usage = "'add me'"
    self.description = "When a group is created by %s in the current group, it is tracked.  Anyone can be auto-added to that group by saying add me." % (config.default_alias)

  def process(self, message, source, groupID):
    if not re.search("^" + self.command, message, re.IGNORECASE):
      return False

    if not groupID:
      self.signaler.reply("This only works from groups, sorry", source, None)
      return True

    lastGroupID = self.config.get_last_created_group(groupID)
    if not lastGroupID:
      self.signaler.reply("No tracked group has been created, I cannot do that Dave.", source, groupID)

    self.signaler.add_to_group(lastGroupID,source)
    self.signaler.reply("It is done.", source, groupID)
    return True
