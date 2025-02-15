# This has to be an integer. Read more [here](https://core.telegram.org/api/obtaining_api_id) | No quotes
api_id: 

# Long 32 characters hash identifier. Read more [here](https://core.telegram.org/api/obtaining_api_id) | With quotes
api_hash: '' 

# Session name. Only one session (with a unique session name) can run at a time | With quotes
session_name: 'forwardgram' 

# Discord Bot Token. Go create a bot on discord. | No quotes
discord_bot_token: ''

# Discord Channels | No quotes
discord_1_channel: ************************
discord_2_channel: ************************
discord_3_channel: ************************
discord_4_channel: ************************

# The channel names that you'd like to forward messages from. Just add input telegram channel names here.
# The user running the client must have these channels present on it's dialogs. 
input_channel_names:
  - 'channel_send'

# The output channel names that the messages will be forwarded to.
# The user running the client must have a write access to those channels, and have the channels present on theirs dialogs.
output_channel_names: 
  - 'channel_recieve'

# The channel IDs that you'd like to forward messages from. Just get channel id from channels you put as input_channel_names above (You can get a channel ID by forwarding any message from it to @userinfobot , and removing the -100 from the start ) 
input_channel_ids:
  - 1644472394

# The output channel IDs that the messages will be forwarded to. Just get channel id from channels you put as output_channel_names above (You can get a channel ID by forwarding any message from it to @userinfobot , and removing the -100 from the start )
output_channel_ids: 
  - 1621993740

# Do not touch this: 
input_channel_ids: []
