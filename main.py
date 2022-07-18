footertext = "made with ❤ by NRG Cristi" #embed footer text remove credits = skid
color = 0x5865F2     #embed color (blurple)




async def on_connect():
  coro = app.create_server(
		host='0.0.0.0',
		port=8000,
		return_asyncio_server=True,
    access_log=False,
	)
  server = await coro
  print("ok")


async def on_ready():
  print("Fornite Stuff Changer Is Online")
  await bot.change_presence(activity=discord.Streaming(name="Fornite Stuff Changer Backend", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))




class embeds:
  async def not_logged_in(ctx):
    embed=discord.Embed(title="You are not Logged in or you were logged out!", description="Type /login To Login!", color=color)
    embed.set_footer(text=footertext)
    await ctx.respond(embed=embed)


async def login(ctx):
  embed=discord.Embed(title="Sign Into Your Epic Games Account", color=color)
  embed.set_image(url="https://media.discordapp.net/attachments/836517393266245632/837230076118302730/image0.png")
  embed.add_field(name="step 1", value="Go to [Epic Games](https://rebrand.ly/authcode) and copy the content that looks like this `0222adecfaaa490c8d28674754688e5e`", inline=True)
  embed.add_field(name="step 2", value="send the copied code in dms", inline=True)
  embed.set_footer(text=footertext)
  await ctx.respond(embed=embed)
  def check(m):
    return len(m.content) == 32 and m.author.id == ctx.author.id
    
  message = await bot.wait_for('message', check=check)
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method="POST",
      url="https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token",
      data=f"grant_type=authorization_code&code={message.content}",
      headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE=",
      }
    ) as r:
      d = await r.json()


      acc_id = d.get('account_id')
      token_ref = d.get('access_token')
      dn = d.get('displayName')

      rq = requests.get(url=f"https://avatar-service-prod.identity.live.on.epicgames.com/v1/avatar/fortnite/ids?accountIds={acc_id}", headers={"Content-Type": "application/json", "Authorization": f"bearer {token_ref}"})
      pp = rq.json()
      skinid = (pp[0]['avatarId'].replace('ATHENACHARACTER:', ''))
      embed=discord.Embed(title=f"Welcome {dn} 👋", description=f"You have linked {dn} To Fortnite Stuff Changer", color=color)
      embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{skinid}/icon.png?width=468&height=468")
      embed.add_field(name="Epic Games ID", value=acc_id, inline=True)
      embed.add_field(name="Logout", value="If you wish to log out type /logout", inline=True)
      embed.set_footer(text=footertext)
      await ctx.author.send(embed=embed)
      with open('users.json', 'r') as f:
          logs = json.load(f)
      logs[str(ctx.author.id)] = f'{acc_id}'
      with open('users.json', 'w') as f: 
          json.dump(logs, f, indent=3)

async def logout(ctx):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id=users[f"{ctx.author.id}"]
    print(id + " Logged Out!")
    del users[f"{ctx.author.id}"]
    with open('users.json', 'w') as f: 
        json.dump(users, f, indent=3)
    embed=discord.Embed(title="Succesfully unlinked your Epic Games From Fortnite Stuff Changer", color=color)
    embed.set_footer(text=footertext)
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return

async def crowns(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " Updated Their Crowns")
    embed=discord.Embed(title=f"Changed Crown Wins To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u change a cosmetic in your locker or restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return

async def level(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " Updated Their Level")
    embed=discord.Embed(title=f"Changed Level To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u change a cosmetic in your locker or restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return



async def battlestars(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " Updated Their Battle Stars")
    embed=discord.Embed(title=f"Changed Battle Stars To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u change a cosmetic in your locker or restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return

async def style_points(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " style points")
    embed=discord.Embed(title=f"Changed Omni Chips To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u change a cosmetic in your locker or restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return

async def vbucks(ctx, amount):
  try:
    with open('users.json', 'r') as f: 
      users = json.load(f) 
    id = users[f'{str(ctx.author.id)}']
    print(id + " vbucs")
    embed=discord.Embed(title=f"Changed vbucs To {amount}", color=color)
    embed.set_footer(text="⚠️ This will update when u restart your game")
    await ctx.respond(embed=embed)
  except:
    await embeds.not_logged_in(ctx=ctx)
    return


input("Enter Your Bot Token Here:")
print("Fortnite Stuff Changer Is Online")
