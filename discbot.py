import discord
import random
import praw

from discord.ext import commands

reddit = praw.Reddit( client_id = "YpYLSzRiSbqRXw",
                      client_secret = "QnpKbCAcCdbNVvGPW33BWTHRqK4",
                      user_agent = "discord")

client = commands.Bot(command_prefix = ".b ")

@client.event
async def on_ready():
    print("online")

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.Member,*,reason = None):
    await user.kick(reason = reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.Member,*,reason = None):
    await user.ban(reason = reason)

@client.command()
async def hello(ctx):
    res1 = ["Yo","Hey There","Hi"]
    await ctx.send(random.choice(res1))
    
@client.command()
async def no(ctx):
    p1 = ["https://imgur.com/rVInx0u"]
    await ctx.send(random.choice(p1))

@client.command()
async def sface(ctx):
    p2 = ["https://imgur.com/2U38tMr","https://imgur.com/ONEE1tG","https://imgur.com/LcYZFfv","https://imgur.com/JJxy9JV","https://imgur.com/THoHESk" ]
    await ctx.send(random.choice(p2))

@client.command()
async def mango(ctx):
    mangoes = ["https://imgur.com/Vl90XgN","https://imgur.com/tXMt28B","https://imgur.com/lJlYJZg"]
    await ctx.send(random.choice(mangoes))

@client.command()
async def dice(ctx):
    player1 = random.randint(1,6)
    player2 = random.randint(1,6)
    
    if player1 == player2:
        await ctx.send("Draw :( \n Player 1 rolled : " + str(player1) + "\n Player 2 rolled : " + str(player2))
    elif player1 > player2:
        await ctx.send("Player 1 wins! \n Player 1 rolled : " + str(player1) + "\n Player 2 rolled : " + str(player2))
    else:
        await ctx.send("Player 2 wins! \n Player 1 rolled : " + str(player1) + "\n Player 2 rolled : " + str(player2))

@client.command()
async def rps(ctx,*,decission):
    
    plist = ["Rock","Paper","Scissor"]

    
    player2 = random.choice(plist)

    if decission in ["Paper","paper","p"]:
        decission = "Paper"
    elif decission in["Rock","rock","r"]:    
        decission = "Rock"          
    elif decission in["Scissor","scissor","s"]:
        decission = "Scissor"
        
    player1 = decission

    if player1 == player2:
        await ctx.send("It's a Draw! \n I chose " + player2)
    
    elif player1 == "Rock" and player1 != player2:
        if player2 == plist[1]:
            await ctx.send("You lost! \n I chose " + player2)
        if player2 == plist[2]:
            await ctx.send("You won! \n I chose " + player2)

    elif player1 == "Paper" and player1 != player2:
        if player2 == plist[0]:
            await ctx.send("You won! \n I chose " + player2)
        if player2 == plist[2]:
            await ctx.send("You lost! \n I chose " + player2)

    elif player1 == "Scissor" and player1 != player2:
        if player2 == plist[1]:
            await ctx.send("You won! \n I chose " + player2)
        if player2 == plist[0]:
            await ctx.send("You lost! \n I chose " + player2)

    else:
        await ctx.send("Something went wrong! \n place the right choice after the command.")

@client.command()
async def meme(ctx):
    submission = reddit.subreddit("memes").random()
    await ctx.send(submission.url)
    
client.run("NzM1MDk1NTQ3NDI1NDU2MTI5.XxbRJQ.iz1oWQybJsT9InUtwqZQ6xjhGak") 


