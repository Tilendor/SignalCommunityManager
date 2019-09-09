# SignalCommunityManager
A chat bot to manage a community built on top of signal

Depends upon the Signal CLI at https://github.com/AsamK/signal-cli this needs to be running and successfully publishing to the dbus to function.

Built on Python 2.7

Need to list libraries required

First step is to register your settings in an encrypted config file:

python register.py <phoneNumber, ie  +18011234567> <default alias> [additional aliases]
  
The default alias is what users should type to signal the bot.
You can have the bot listen to several aliases, list them space separated after the first
Right now the alias cannot contain a space

Next you can run the program:

python scm.py
