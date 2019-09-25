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


Current roadmap

Safety/Privacy:
1. Turn off message logging on my server
2. 'distrust' - so one user can mark another as distrusted.  Someone marked as distrusted will not be able to see or join groups with individual's who distrust them using pyschobot.
3. 'restrust' - command to let a user remove the distrust flag.
4. 'leave' - Tell pyschobot to remove himself from a group.  (Need to add this to underlying infrastructure)

Group Browsing:
1. Rename 'start topic' to 'start group' 
2.  'set topic' -  Assigns a topic to a group separate from the name, to save typing (IE the Pyschology Main (9/19) chat could have the topic 'main') (Need to figure out how to keep topics unique)
3. 'list groups' - to provide a user with all open groups that they could join.
4. 'join group X' - to let a user join a group.
5. 'set welcome X' - Allows a group to have a welcome message given upon joining (Right now can only do this with adds done through PB, need to work on underlying libraries to support this for manual invites)
6. Group invitation policies.  Default is open access.  If pyschobot leaves the group its effectively closed.  Having a 'vouch' system where when someone wants to join, an announcement is made in the group and it requires a configurable number of vouches before PB will invite the user.
7. 'add motd' - Add a Message of the Day.  Something pyschobot could say at the beginning of the day.  Could track many motds and rotate through them. need 'list motd' and 'remove motd' to compliment this.

Events:
1. Big feature - Allow users to create events which get tracked by PB.  PB could announce events happening each day, send reminders, etc...  again Big Feature.

Management:
1. 'reboot' - Automate the rebooting process Bert uses to refresh a group.

Misc:
1. 'add quote' - Save a quote.
2. 'random quote' - Tells a random saved quote
3. Give pyschobot more character:
3.a Put more random behavior in the say command.
3.b Create Markov Chains from what people write to auto-generate odd comments.
3.c Rate limit 'noisy' bot behaviours to keep PB from becoming a distraction
