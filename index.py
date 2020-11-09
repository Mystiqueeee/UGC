import discord
from discord.ext import commands, tasks
from random import choice
from discord import DMChannel


client = commands.Bot(command_prefix = "ugc")

status = ['At Unfaithful Gamers Community | ugc', 'ugchelp', 'With Admins | ugc']
queue = []

 
class ClientData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None
 
        self.reaction_role = None
        self.reaction_message = None
 
clientdata = ClientData()
@client.event
async def on_ready():
    change_status.start()
    print("Now Serving UGC!")
 
 
@client.command()
@commands.has_guild_permissions(ban_members=True)
async def ann(ctx, reason=None):

    channel = await client.fetch_channel('755234152672133130')

    embed = discord.Embed(title=f"**Announcement**", description=f"Attention @everyone!", color=0xea7938)
    embed.add_field(name='Description', value=reason)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/760038282078847037/775217195444862996/kingfisher-logonfgg.png')
    embed.set_footer(text=f"Made By THISURAvX#9069", icon_url="https://cdn.discordapp.com/attachments/760038282078847037/775217195444862996/kingfisher-logonfgg.png")
    await channel.send(embed=embed)



@client.command()
@commands.has_guild_permissions(ban_members=True)
async def elecp(ctx, reason=None):

   # channel = await client.fetch_channel('755234152672133130')

    # embed.add_field(name='Description', value=reason)
    #embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/760038282078847037/775217195444862996/kingfisher-logonfgg.png')
    #embed.set_footer(text=f"Made By THISURAvX#9069", icon_url="https://cdn.discordapp.com/attachments/760038282078847037/775217195444862996/kingfisher-logonfgg.png")
    #await channel.send(embed=embed)
    embed = discord.Embed(title=f"None Of the Participants have fulfilled the requirements", color=0xea7938)
    await ctx.send(embed=embed)


@client.command()
@commands.has_guild_permissions(ban_members=True)
async def dm(ctx,user:discord.User,*,reason=None):

    user = await client.fetch_user(user.id)

    embed = discord.Embed(color=0xea7938)
    embed = discord.Embed(title=f"DM sent to {user.name}")
    await ctx.send(embed=embed)

    await DMChannel.send(user, reason)
    
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))
 
client.run ("Nzc1MjE1MzQ3OTI1NTE2MzQ4.X6jFjQ.sZhOzMj7Ha1_oj9RkIY68_sAJIM")
