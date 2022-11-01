"""**************************************************************
* TO DO LIST                                                    *
*	1) handle scheduling via cron                               *
*		-may need to handle schedling in bot code               *
*	2) send 1 of 2 stored strings                               *
*		-string sent depends on day of week                     *
*	3) accept command line argument to change name of event?    *
*		-define .env file to store passed argument              *
*			-to change title of event, either edit after posted *
*			 or update .env file                                *
**************************************************************"""

import discord
import os
import sys
import random
from dotenv import load_dotenv

CHANNEL = 834460054736338956
message = "/shrug"

load_dotenv()

client = discord.Bot()
token = os.getenv('TOKEN')

@client.event
async def on_ready():
	print("Logged in as a bot {0.user}".format(client))
	message_channel = client.get_channel(CHANNEL)
	await message_channel.send(message)
	exit_msg = "sent " + str(message) + " to " + str(message_channel)
	sys.exit(exit_msg)	

client.run(token)