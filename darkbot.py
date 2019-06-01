 uksoftworld / DarkBot

Code Issues 0 Pull requests 1 Projects 0 Wiki Security Pulse Community

Branch: master 

Find fileCopy path

DarkBot/darkbot.py

 uksoftworld Update darkbot.py116e1fd on Dec 9, 2018

2 contributors

830 lines (700 sloc)  39.1 KB

RawBlameHistory

 

import discordfrom discord.ext.commands import Botfrom discord.ext import commandsfrom discord.ext.commands.cooldowns import BucketTypeimport asyncioimport platformimport colorsysimport randomimport osimport timefrom discord.voice_client import VoiceClientfrom discord import Game, Embed, Color, Status, ChannelType Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)client = Bot(description="DarkBot Bot is best", command_prefix="d!", pm_help = True)client.remove_command('help') async def status_task(): while True: await client.change_presence(game=discord.Game(name='for d!help')) await asyncio.sleep(5) await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users')) await asyncio.sleep(5) await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers')) await asyncio.sleep(5) 	@client.eventasync def on_ready(): print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users') print('--------') print('--------') print('Started Dark BOT') print('Created by Utkarsh') client.loop.create_task(status_task()) 	def is_owner(ctx): return ctx.message.author.id == "420525168381657090, 395535610548322326" def is_dark(ctx): return ctx.message.author.id == "420525168381657090" def is_shreyas(ctx): return ctx.message.author.id == "376602841625919488" def is_gameworld(ctx): return ctx.message.author.id == "402075464694366211" def is_ranger(ctx): return ctx.message.author.id == "304911836460089345" @client.command(pass_context = True)@commands.check(is_owner)async def restart(): await client.logout() @client.eventasync def on_message(message):	await client.process_commands(message) @client.eventasync def on_member_join(member): print("In our server" + member.name + " just joined") r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1)) embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b)) embed.set_author(name='Welcome message') embed.add_field(name = '__Welcome to Our Server__',value ='**Hope you will be active here. Check Our server rules and never try to break any rules. ',inline = False) embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') await client.send_message(member,embed=embed) print("Sent message to " + member.name) channel = discord.utils.get(client.get_all_channels(), server__name='DarkBot Official Server', name='darkbot-servers-join-leave-log') r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.rando
