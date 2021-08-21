import discord
from discord import channel
from discord import guild
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')

#bot_is_ready
@client.event
async def on_ready():
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('MunJitso sucks'))
        print('We logged in as {0.user}'.format(client))


#===EVERYONE's COMMANDS===#

#ping&pong
@client.command()
async def ping(ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

#askme
@client.command(aliases=['ask'])
async def _8ball(ctx, *, question):
        responses = ["It is certain.",
                        "It is decidedly so.",
                        "Without a doubt.",
                        "Yes - definitely.",
                        "You may rely on it.",
                        "As I see it, yes.",
                        "Most likely.",
                        "Outlook good.",
                        "Yes.",
                        "Signs point to yes.",
                        "Reply hazy, try again.",
                        "Ask again later.",
                        "Better not tell you now.",
                        "Cannot predict now.",
                        "Concentrate and ask again.",
                        "Don't count on it.",
                        "My reply is no.",
                        "My sources say no.",
                        "Outlook not so good.",
                        "Very doubtful."]
        await ctx.send(f'Question: {question}\n Answer : {random.choice(responses)}')


#===WELCOMING===#

@client.event 
async def on_member_join(member):
        channel = client.get_channel(878202728659177502)
        await channel.send(f"Welcome To our Kingdom <:cuteface:818864333655638027> , {member.mention}!")

@client.event 
async def on_member_remove(member):
        channel = client.get_channel(878202728659177502)
        await channel.send(f"Bye Bye :((, {member.mention}!")


#===ADMIN COMMANDS===#

#clear_messages
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=10000000000000000):
        await ctx.channel.purge(limit=amount)

#kick
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} is kicked from our kingdom')

#ban
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} is banned from our kingdom')

#unban
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
                user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} has been unbanned!')
                return


client.run("ODc4MDM3Nzk3MzU1Nzk4NTg5.YR7WbA.aZE15KukYyKmwqe6ZkQeptYZUKs")
