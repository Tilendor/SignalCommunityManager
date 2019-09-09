

class Signaler():

  def __init__(self,signal_client):
    self.signal_client = signal_client

  def reply(self,message,source,groupID):
    if not groupID:
      return self.signal_client.sendMessage(message,None,[source])
    return self.signal_client.sendGroupMessage(message,None,groupID)

  def create_group(self,name,source):
    return self.signal_client.updateGroup(None,name,[source],"")

  def add_to_group(self,groupID,number):
    name = self.signal_client.getGroupName(groupID)
    return self.signal_client.updateGroup(groupID,name,[number],"")

  def get_group_name(self,groupID):
    return self.signal_client.getGroupName(groupID)
