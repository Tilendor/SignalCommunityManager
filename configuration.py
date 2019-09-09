import os, re, sys
from json import dumps, loads
from secureconfig import SecureJson


class Configuration():

  def __init__(self):
    self.config_file_name = 'config.json.enc'
    self.config_file_path = '.'
    self.encryption_key_name = 'key'
    self.secure_json = SecureJson.from_file(self.encryption_key_name,filepath=self.config_file_name)

    self.signal_phone_number = self.secure_json.cfg['signal_phone_number']
    self.aliases_rgx = self.secure_json.cfg['aliases']
    self.default_alias = self.aliases_rgx[2:].replace(")","").split('|')[0]


  @staticmethod
  def strGid(bgroupID):
    return ",".join(map(str,bgroupID))
  
  @staticmethod
  def byteGid(sgroupID):
    return map(int,sgroupID.split(','))

  def save(self):
    with open(self.config_file_name, 'w+') as f:
      SecureJson.write(self.secure_json,f)

  def group_exists(self,groupID):
    str_group_id = self.strGid(groupID) 
    return str_group_id in self.secure_json.cfg['groups']

  def new_group(self,groupID, name):
    str_group_id = self.strGid(groupID)
    self.secure_json.cfg['groups'][str_group_id] = {'groupID': groupID, 'topic': name}
    self.save()

  def set_group_topic(self, groupID, topic):
    str_group_id = self.strGid(groupID)
    group = self.secure_json.cfg['groups'][str_group_id]
    if not group:
      return
    group['topic'] = topic
    self.save()

  def set_last_created_group(self,groupID,newGroupID):
    str_group_id = self.strGid(groupID)
    group = self.secure_json.cfg['groups'][str_group_id]
    if not group:
      return
    group['last_created_group'] = newGroupID
    self.save()

  def get_last_created_group(self,groupID):
    str_group_id = self.strGid(groupID)
    group = self.secure_json.cfg['groups'][str_group_id]
    if not group:
      return None
    return group['last_created_group']




