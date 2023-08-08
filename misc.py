from intro import *
@bot.command(aliases=["fr"])
async def forme(ctx,num=1):
    "Changes forms"
    db=sqlite3.connect("owned.db")
    c=db.cursor()
    num=await row(ctx,num,c)
    c.execute(f"select * from '{ctx.author.id}' where rowid={num}")
    mons=c.fetchone()
    mon=mons[0]
    if "Therian" in mon:
        mon=mon.replace("Therian ","")
        c.execute(f"""Update `{ctx.author.id}` set name="{mon}" where rowid={num}""")        
        db.commit()
    elif mon in ["Thundurus","Landorus","Tornadus","Enamorus"]:
        mon="Therian "+mon
        c.execute(f"""Update `{ctx.author.id}` set name="{mon}" where rowid={num}""")        
        db.commit()
@bot.command(aliases=["cf"])    
async def coinflip(ctx,choice,amount=100):
    "Flips a coin. Winning doubles your amount and losing deducts. Example: !coinflip heads 100"
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"select * from '{ctx.author.id}'")
    man=c.fetchone()
    if amount<=man[0]:
        choice=choice.title()
        x=random.choice(["Heads","Tails"])
        if choice==x:
            em=discord.Embed(title=f"It's {x}! You Won!",color=0x00ff00)
            em.set_thumbnail(url="https://i.gifer.com/Fw3P.gif")
            await ctx.send(embed=em)
            await addmoney(ctx,ctx.author,amount)
        if choice!=x and choice in ["Heads","Tails"]:
            em=discord.Embed(title=f"It's {x}! You Lost!",color=0xff0000)
            em.set_thumbnail(url="https://i.gifer.com/Fw3P.gif")
            await ctx.send(embed=em)
            await addmoney(ctx,ctx.author,-amount)
    else:
        ctx.reply("You don't have enough balance!")
async def moncolor(u):
    colors = {
        "Normal": "BFB97F",
        "Fighting": "D32F2E",
        "Flying": "9E87E1",
        "Poison": "AA47BC",
        "Ground": "DFB352",
        "Rock": "BDA537",
        "Bug": "98B92E",
        "Ghost": "7556A4",
        "Steel": "B4B4CC",
        "Fire": "E86513",
        "Water": "2196F3",
        "Grass": "4CB050",
        "Electric": "FECD07",
        "Psychic": "EC407A",
        "Ice": "80DEEA",
        "Fairy": "F483BB",
        "Dark": "5C4038",
        "Dragon": "673BB7"
    }

    if u in colors:
        return int(colors[u], 16)
    else:
        return int("FFFFFF", 16)

@bot.command(aliases=["dx"], description="Shows Pokémon!")
async def dex(ctx,*name):  
    "Shows the pokémon's base dex stats."
    shiny=""
    name=" ".join(name)
    name=name.title()
    if "Shiny " in name:
        name=name.replace("Shiny ","")
        shiny="Yes"
    db=sqlite3.connect("pokemondata.db")
    c=db.cursor()   
    dt=sqlite3.connect("owned.db")
    cx=dt.cursor()
    c.execute(f"select * from 'wild' where Name='{name}'")
    x=c.fetchall() 
    cx.execute(f"select * from '{ctx.author.id}' where name='{name}'")
    ch=cx.fetchall()
    text=""
    if len(ch)==0:
        text=f"<:cross:1133677258398257193> You haven't caught any {name} yet!"
    if len(ch)>0:
        text=f"<:tick:1133677303407325286> You have caught {len(ch)} {name}!"
    if len(x)!=0: 
        p=x[0]
        total=p[4]+p[5]+p[6]+p[7]+p[8]+p[9]
        sprite=p[12]
        if shiny=="Yes":
            sprite=sprite.replace("http://play.pokemonshowdown.com/sprites/ani/","http://play.pokemonshowdown.com/sprites/ani-shiny/")
        name=p[0]
        rare=p[14]
        types=await typeicon(p[1])
        clr=await moncolor(p[1])
        if p[2]!="???":
            types=f"{await typeicon(p[1])}{await typeicon(p[2])}"
            clr=await moncolor(random.choice([p[1],p[2]]))
        data=discord.Embed(title=f"{p[22]} {name}",description=f"{p[23]} Pokémon", color=clr)
        data.add_field(name="Infos:",value=f"**Types:** {types}\n**Abilities:** {p[11].replace(',','/')}\n**Rarity:** {rare}\n**Weight:** {p[13]} lbs\n**Region:** {p[16]}\n**Egg Group:** {p[18]}")
        data.add_field(name=f"Base Stats: {total}",value=f"""**HP:** {p[4]}\n**Attack:** {p[5]}\n**Defense:** {p[6]}\n**Sp. Atk:** {p[7]}\n**Sp. Def:** {p[8]}\n**Speed:** {p[9]}""")
        data.set_thumbnail(url="https://cdn.discordapp.com/attachments/1127110331408318496/1127136147156500580/1688800580902.png")
        if p[19]!="None":
            data.add_field(name="Dex Entry:",value=p[19])
        data.add_field(name="Entry:",value=text)   
        data.set_image(url=sprite) 
        await ctx.send(embed=data)
        
@bot.command(aliases=["sp"], description="Spawns Pokémon!")
async def spawn(ctx):
    "Spawns wild Pokémons. Costs 500 <:pokecoin:1134595078892044369> and gives back 250 <:pokecoin:1134595078892044369> on capture."
    dn=sqlite3.connect("playerdata.db")
    cn=dn.cursor()
    cn.execute(f"select * from '{ctx.author.id}'")
    mmm=cn.fetchone()
    money=mmm[0]
    if money>=500:
        await addmoney(ctx,ctx.author,-500)
        dx=sqlite3.connect("playerdata.db")
        ct=dx.cursor()
        ct.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{ctx.author.id}' ")
        if ct.fetchone():
            db=sqlite3.connect("pokemondata.db")
            dt=sqlite3.connect("owned.db")
            cx=dt.cursor()
            c=db.cursor()
            select=random.choices(["Common","Uncommon","Rare","Very Rare","Common Legendary","Ultra Beasts","Legendary","Mythical"],weights=[1500,500,150,50,5,10,1,3],k=1)[0]
            c.execute(f"select * from 'wild' where Rarity='{select}'")
            x=c.fetchall()
            m=random.choice(x)
            tch=random.randint(1,25)
            ach=random.randint(1,50)
            tera="???"
            extra=""
            turl=""
            shinyodd=random.randint(1,1024)
            shiny="No"
            maxiv="No"
            item="None"
            itemodd=random.randint(1,100)
            if itemodd<25:
                item=random.choice(m[17].split(","))
            if shinyodd==7:
                shiny="Yes"
            if ach==7 and select not in ("Common Legendary","Legendary","Mythical"):
                maxiv="Alpha"
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103318414795219024/20230503_195314.png"
                extra=" This pokémon seems larger than usual!"
            if tch==7:
                tera=random.choice(("Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice","Psychic"))
                if tera not in (m[1],m[2]):
                    extra=" Seems like it has a different Tera-Type!"
                    turl=f"https://play.pokemonshowdown.com/sprites/types/Tera{tera}.png"
            p=Pokemon(name=m[0],primaryType=m[1],secondaryType=m[2],level=m[3],hp=m[4],atk=m[5],defense=m[6],spatk=m[7],spdef=m[8],speed=m[9],moves=m[10], ability=m[11],sprite=m[12],gender=m[15],tera=tera,shiny=shiny,maxiv=maxiv,item=item)
            types=p.primaryType
            if p.secondaryType!="???":
                types=f"{p.primaryType}/{p.secondaryType}"
            p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
            p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)    
            wild=discord.Embed(title=f"A wild pokémon has appeared!{extra}")
            if (tch<10 and tera not in (m[1],m[2])) or "Alpha" in p.nickname:
                wild.set_thumbnail(url=f"{turl}")
            try:
                wild.set_image(url=p.sprite)
            except:
                wild.add_field(name="Network Error!",value=f"Answer: {p.name}")
            wild.set_footer(text="Guess it's full name to capture it!")
            flee=discord.Embed(title=f"The wild {p.name} fled!")
            flee.set_image(url=p.sprite)
            flee.set_footer(text="Try again later!")
            await ctx.send(embed=wild)
            while True:
                guess = await bot.wait_for('message')
                if "!sp" in guess.content and guess.author==ctx.author:
                    await ctx.send(embed=flee)
                    break
                if "hint" in guess.content:
                    ch=random.randint(1,5)
                    hint=p.name
                    if ch==4:
                        hint=p.ability
                    if ch==3:
                        hint=p.secondaryType
                    if ch==2:
                        hint=p.primaryType
                    if ch==1:
                        n=list(p.name.lower())
                        random.shuffle(n)
                        hint="".join(n)
                    await ctx.send(f" Hint: {hint}")
                if p.name.lower().split()[-1] in guess.content.lower():
                    p.moves=f"{p.moves}"
                    cx.execute(f"""CREATE TABLE IF NOT EXISTS [{guess.author.id}] (
                    Name text,
                    Nickname text,
                    Level integer,
                    hpiv integer,
                    atkiv integer,
                    defiv integer,
                    spatkiv integer,
                    spdefiv integer,
                    speediv integer,
                    hpev integer,
                    atkev integer,
                    defev integer,
                    spatkev integer,
                    spdefev integer,
                    speedev integer,
                    ability text,
                    nature text,
                    shiny text,
                    item text,
                    gender text,
                    teratype text,
                    maxiv text,
                    moves text,
                    rarity text,
                    time text,
                    totaliv integer)""")
                    clk=datetime.datetime.now()
                    catchtime=clk.strftime("%Y-%m-%d %H:%M:%S")
                    if p.shiny=="Yes" or m[14] in ["Ultra Beasts","Common Legendary","Legendary","Mythical"] or p.totaliv>80:
                        dt.commit()
                        cx.execute(f"""INSERT INTO "1084473178400755772" VALUES (
                    "{p.name}",
                    "{p.nickname}",
                    "{p.level}",
                    "{p.hpiv}",
                    "{p.atkiv}",
                    "{p.defiv}",
                    "{p.spatkiv}",
                    "{p.spdefiv}",
                    "{p.speediv}",
                    "{p.hpev}",
                    "{p.atkev}",
                    "{p.defev}",
                    "{p.spatkev}",
                    "{p.spdefev}",
                    "{p.speedev}",
                    "{p.ability}",
                    "{p.nature}",
                    "{p.shiny}",
                    "{p.item}",
                    "{p.gender}",
                    "{p.tera}",
                    "Custom",
                    "{p.moves}",
                    "{m[14]}",
                    "{catchtime}",
                    "{p.totaliv}")""")
                        dt.commit()                    
                    cx.execute(f"""INSERT INTO "{guess.author.id}" VALUES (
                    "{p.name}",
                    "{p.nickname}",
                    "{p.level}",
                    "{p.hpiv}",
                    "{p.atkiv}",
                    "{p.defiv}",
                    "{p.spatkiv}",
                    "{p.spdefiv}",
                    "{p.speediv}",
                    "{p.hpev}",
                    "{p.atkev}",
                    "{p.defev}",
                    "{p.spatkev}",
                    "{p.spdefev}",
                    "{p.speedev}",
                    "{p.ability}",
                    "{p.nature}",
                    "{p.shiny}",
                    "{p.item}",
                    "{p.gender}",
                    "{p.tera}",
                    "Custom",
                    "{p.moves}",
                    "{m[14]}",
                    "{catchtime}",
                    "{p.totaliv}")""")
                    dt.commit()
                    db.commit()
                    catch="caught"
                    if ctx.author!=guess.author:
                        catch="sniped"
                    await guess.reply(f"{guess.author.display_name} {catch} a level {p.level} {p.nickname} (IV: {p.totaliv}%)!")
                    if p.item!="None":
                        await ctx.send(f"{p.name} is holding a {p.item}!")
                    if guess.author==ctx.author:
                        await addmoney(ctx,ctx.author,250)
                    if guess.author!=ctx.author:
                        await addmoney(ctx,guess.author,-750)
                    break       
        else:
            await ctx.send("You don't have an account. Type `!start` to create an account.")     
    else:
        await ctx.send("You don't have enough money.")         
@bot.command(aliases=["cl"])            
async def claim(ctx,code):        
    if code=="tsilverw7":
        await addmoney(ctx,ctx.author,10000)
    else:
        pass
@bot.command(aliases=["bd"])            
async def badge(ctx,num=1):        
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"select * from '{ctx.author.id}'")
    dat=c.fetchone()
    print(dat)
    if dat[6]!="None":
        bdg=dat[6].split(",")
        dt=sqlite3.connect("pokemondata.db")
        ct=dt.cursor()
        tex=""
        start=(num*10)-10
        end=(num*10)
        if end>len(bdg):
            end=len(bdg)
        for i in range(start,end):
            ct.execute(f"select * from 'Trainers' where symbolname='{bdg[i]}'")
            jj=ct.fetchone()
            tex+=f"{jj[2]} {jj[1]}\n"
        bd=discord.Embed(title="Badges:",description=tex)
        await ctx.send(embed=bd)
@bot.command(aliases=["st"])            
async def start(ctx):
    "Starts the game for you and creates your account."
    dt=sqlite3.connect("playerdata.db")
    ct=dt.cursor()
    ct.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{ctx.author.id}' ")
    if ct.fetchone():
        await ctx.send("You already have an account!")
    else:
        ct.execute(f"""CREATE TABLE IF NOT EXISTS [{ctx.author.id}] (
        Balance integer,
        Squad text,
        Items text,
        creationdate text,
        winstreak integer,
        highstreak integer,
        badges text
        )""")
        clk=datetime.datetime.now()
        ca=clk.strftime("%Y-%m-%d %H:%M:%S")
        ct.execute(f"""INSERT INTO "{ctx.author.id}" VALUES (
        10000,
        "0,0,0,0,0,0",
        "[]",
        "{ca}",
        0,
        0,
        "None")""")
        dt.commit()
        await ctx.send("Account created successfully.")
        db=sqlite3.connect("pokemondata.db")
        dx=sqlite3.connect("owned.db")
        c=db.cursor()
        cx=dx.cursor()
        ann=discord.Embed(title="Choose your starter:", description="Enter the fullname of the starter to claim it.")
        ann.add_field(name="Kanto",value="Venusaur\nCharizard\nBlastoise")
        ann.add_field(name="Johto",value="Meganium\nTyphlosion\nFeraligatr")
        ann.add_field(name="Hoenn",value="Sceptile\nBlaziken\nSwampert")
        ann.add_field(name="Sinnoh",value="Torterra\nInfernape\nEmpoleon")
        ann.add_field(name="Unova",value="Serperior\nEmboar\nSamurott")
        ann.add_field(name="Kalos",value="Chesnaught\nDelphox\nGreninja")
        ann.add_field(name="Alola",value="Decidueye\nIncineroar\nPrimarina")
        ann.add_field(name="Galar",value="Rillaboom\nCinderace\nInteleon")
        ann.add_field(name="Paldea",value="Meowscarada\nSkeledirge\nQuaquaval")
        ann.set_footer(text="You have to enter the full name to claim your starter.")
        await ctx.send(embed=ann)
        while True:
            guess=await bot.wait_for('message',check=lambda message: message.author==ctx.author)
            nam=guess.content.strip().title()
            if nam in "Venusaur\nCharizard\nBlastoiseMeganium\nTyphlosion\nFeraligatrSceptile\nBlaziken\nSwampertTorterra\nInfernape\nEmpoleonSerperior\nEmboar\nSamurottChesnaught\nDelphox\nGreninjaDecidueye\nIncineroar\nPrimarinaRillaboom\nCinderace\nInteleonMeowscarada\nSkeledirge\nQuaquaval":
                c.execute(f"Select * from 'wild' where name='{nam}'")
                m=c.fetchone()
                if m!=None and len(m)!=0:
                    shinyodd=random.randint(1,512)
                    shiny="No"
                    if shinyodd==7:
                        shiny="Yes"
                    p=Pokemon(name=m[0],primaryType=m[1],secondaryType=m[2],level=m[3],hp=m[4],atk=m[5],defense=m[6],spatk=m[7],spdef=m[8],speed=m[9],moves=m[10], ability=m[11],sprite=m[12],gender=m[15],shiny=shiny)
                    p.moves=f"{p.moves}"
                    p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
                    cx.execute(f"""CREATE TABLE IF NOT EXISTS [{ctx.author.id}] (
                    Name text,
                    Nickname text,
                    Level integer,
                    hpiv integer,
                    atkiv integer,
                    defiv integer,
                    spatkiv integer,
                    spdefiv integer,
                    speediv integer,
                    hpev integer,
                    atkev integer,
                    defev integer,
                    spatkev integer,
                    spdefev integer,
                    speedev integer,
                    ability text,
                    nature text,
                    shiny text,
                    item text,
                    gender text,
                    teratype text,
                    maxiv text,
                    moves text,
                    rarity text,
                    time text,
                    totaliv integer)""")
                    clk=datetime.datetime.now()
                    catchtime=clk.strftime("%Y-%m-%d %H:%M:%S")
                    cx.execute(f"""INSERT INTO "{ctx.author.id}" VALUES (
                    "{p.name}",
                    "{p.nickname}",
                    "{p.level}",
                    "{p.hpiv}",
                    "{p.atkiv}",
                    "{p.defiv}",
                    "{p.spatkiv}",
                    "{p.spdefiv}",
                    "{p.speediv}",
                    "{p.hpev}",
                    "{p.atkev}",
                    "{p.defev}",
                    "{p.spatkev}",
                    "{p.spdefev}",
                    "{p.speedev}",
                    "{p.ability}",
                    "{p.nature}",
                    "{p.shiny}",
                    "{p.item}",
                    "{p.gender}",
                    "{p.tera}",
                    "Custom",
                    "{p.moves}",
                    "{m[14]}",
                    "{catchtime}",
                    "{p.totaliv}")""")
                    dx.commit()
                    db.commit()
                    show=discord.Embed(title=f"Congratulations {ctx.author.display_name}! You chose {p.name} as your starter!")
                    show.set_thumbnail(url=ctx.author.avatar)
                    show.set_image(url=p.sprite)
                    show.set_footer(text="Enter '!info' to see more details or '!spawn' to start catching pokémons.")
                    await ctx.send(embed=show)
                    break        
@bot.command(aliases=["ml"])
async def marketlist(ctx,num=1,cost=0):
    db=sqlite3.connect("owned.db")
    c=db.cursor()
    num=await row(ctx,num,c)
    p,allmon=await pokonvert(ctx,ctx.author,num)
    p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
    p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)  
    types=await typeicon(p.primaryType)
    clr=await moncolor(p.tera)
    if p.secondaryType!="???":
        types=f"{await typeicon(p.primaryType)}{await typeicon(p.secondaryType)}"
    infos=discord.Embed(title=f"Do you want to list {p.nickname} on Pokémon Market for {await numberify(cost)} <:pokecoin:1134595078892044369>?", description=f"""**Types:** {types}\n**Tera-Type:** {await teraicon(p.tera)}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {await itemicon(p.item)} {p.item}\n**HP:** {p.maxhp} - IV: {p.hpiv}/31 - EV: {p.hpev}\n**Attack:** {p.maxatk} - IV: {p.atkiv}/31 - EV: {p.atkev}\n**Defense:** {p.maxdef} - IV: {p.defiv}/31 - EV: {p.defev}\n**Sp. Atk:** {p.maxspatk} - IV: {p.spatkiv}/31 - EV: {p.spatkev}\n**Sp. Def:** {p.maxspdef} - IV: {p.spdefiv}/31 - EV: {p.spdefev}\n**Speed:** {p.maxspeed} - IV: {p.speediv}/31 - EV: {p.speedev}\n**Total IV %:** {p.totaliv}%\n**Total EV :** {p.totalev}/508""",color=clr)
    infos.set_image(url=p.sprite)
    await ctx.send(embed=infos)
    while True:
        response=await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        if response.content.lower() in ["no","n"]:
            await ctx.send("Listing canceled.")
            break
        elif response.content.lower() in ["yes","y"]:
            code="abcdefghijklmnopqrstuvwxyz0123456789"
            gen="".join(random.choices(code,k=5))
            db=sqlite3.connect("market.db")
            dx=sqlite3.connect("owned.db")
            c=db.cursor()
            cx=dx.cursor()
            c.execute(f"""CREATE TABLE IF NOT EXISTS "market" (
                    Name text,
                    Nickname text,
                    Level integer,
                    hpiv integer,
                    atkiv integer,
                    defiv integer,
                    spatkiv integer,
                    spdefiv integer,
                    speediv integer,
                    hpev integer,
                    atkev integer,
                    defev integer,
                    spatkev integer,
                    spdefev integer,
                    speedev integer,
                    ability text,
                    nature text,
                    shiny text,
                    item text,
                    gender text,
                    teratype text,
                    maxiv text,
                    moves text,
                    rarity text,
                    time text,
                    totaliv integer,
                    price integer,
                    sellerid integer,
                    serialno text)""")
            db.commit()
            c.execute(f"""INSERT INTO "market" VALUES (
                    "{p.name}",
                    "{p.nickname}",
                    "{p.level}",
                    "{p.hpiv}",
                    "{p.atkiv}",
                    "{p.defiv}",
                    "{p.spatkiv}",
                    "{p.spdefiv}",
                    "{p.speediv}",
                    "{p.hpev}",
                    "{p.atkev}",
                    "{p.defev}",
                    "{p.spatkev}",
                    "{p.spdefev}",
                    "{p.speedev}",
                    "{p.ability}",
                    "{p.nature}",
                    "{p.shiny}",
                    "{p.item}",
                    "{p.gender}",
                    "{p.tera}",
                    "Custom",
                    "{p.moves}",
                    "Traded",
                    "Unknown",
                    "{p.totaliv}",
                    "{cost}",
                    "{ctx.author.id}",
                    "{gen}")""")
            db.commit()      
            cx.execute(f"delete from '{ctx.author.id}' where rowid={num}")  
            dx.commit()
            await ctx.send(f"{p.nickname} was listed on the Pokémon Market successfully!")
            break
        else:
            break
@bot.command(aliases=["mi"])
async def marketinfo(ctx,code):
    dt = sqlite3.connect("pokemondata.db")
    db = sqlite3.connect("market.db")
    cx = dt.cursor()
    c = db.cursor()
    allmon = []
    c.execute(f"SELECT * FROM 'market' where serialno='{code}'")
    n = c.fetchone()
    cx.execute(f"SELECT * FROM 'wild' WHERE name=?", (n[0],))
    m = cx.fetchall()[0]
    p = Pokemon(
        name=m[0],
        nickname=n[1],
        primaryType=m[1],
        secondaryType=m[2],
        level=m[3],
        hp=m[4],
        atk=m[5],
        defense=m[6],
        spatk=m[7],
        spdef=m[8],
        speed=m[9],
        moves=n[22],
        ability=n[15],
        sprite=m[12],
        gender=n[19],
        tera=n[20],
        maxiv="Custom",
        item=n[18],
        shiny=n[17],
        nature=n[16],
        hpiv=n[3],
        atkiv=n[4],
        defiv=n[5],
        spatkiv=n[6],
        spdefiv=n[7],
        speediv=n[8],
        hpev=n[9],
        atkev=n[10],
        defev=n[11],
        spatkev=n[12],
        spdefev=n[13],
        speedev=n[14],
        catchdate=n[24],
        icon=m[22],
        weight=m[13]
    )
    known=""
    for i in p.moves:
        known+=f"{await movetypeicon(p,i)} {i} {await movect(i)}\n"
    if code!=None:
        types=await typeicon(p.primaryType)
        clr=await moncolor(p.tera)
        if p.secondaryType!="???":
            types=f"{await typeicon(p.primaryType)}{await typeicon(p.secondaryType)}"
        p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
        p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)  
        infos=discord.Embed(title=f"#{code} {p.nickname} Lv.{p.level}", description=f"""**Types:** {types}\n**Tera-Type:** {await teraicon(p.tera)}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {await itemicon(p.item)} {p.item}\n**HP:** {p.maxhp} - IV: {p.hpiv}/31 - EV: {p.hpev}\n**Attack:** {p.maxatk} - IV: {p.atkiv}/31 - EV: {p.atkev}\n**Defense:** {p.maxdef} - IV: {p.defiv}/31 - EV: {p.defev}\n**Sp. Atk:** {p.maxspatk} - IV: {p.spatkiv}/31 - EV: {p.spatkev}\n**Sp. Def:** {p.maxspdef} - IV: {p.spdefiv}/31 - EV: {p.spdefev}\n**Speed:** {p.maxspeed} - IV: {p.speediv}/31 - EV: {p.speedev}\n**Total IV %:** {p.totaliv}%\n**Total EV :** {p.totalev}/508\n**Price:** {await numberify(n[26])} <:pokecoin:1134595078892044369>""",color=clr)
        infos.set_author(name=ctx.author.display_name)
        infos.add_field(name="Moves:",value=known)
        infos.set_image(url=p.sprite)
        infos.set_thumbnail(url=ctx.author.avatar)
        await ctx.send(embed=infos)            
@bot.command(aliases=["pi"])
async def info(ctx,num=None):
    "Shows infos about your captured pokémons."
    db=sqlite3.connect("owned.db")
    c=db.cursor()
    nu=num
    if num!=None:
        num=int(num)
        nu=num
        num=await row(ctx,num,c)
    p,allmon=await pokonvert(ctx,ctx.author,num)
    known=""
    n=0
    for i in p.moves:
        n+=1
        known+=f"{await movetypeicon(p,i)} {i} {await movect(i)}\n"
    if len(allmon)!=0:
        if num==None:
            num=len(allmon)
        types=await typeicon(p.primaryType)
        clr=await moncolor(p.tera)
        if p.secondaryType!="???":
            types=f"{await typeicon(p.primaryType)}{await typeicon(p.secondaryType)}"
        p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
        p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)  
        infos=discord.Embed(title=f"#{nu} {p.nickname} Lv.{p.level}", description=f"""**Types:** {types}\n**Tera-Type:** {await teraicon(p.tera)}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {await itemicon(p.item)} {p.item}\n**HP:** {p.maxhp} - IV: {p.hpiv}/31 - EV: {p.hpev}\n**Attack:** {p.maxatk} - IV: {p.atkiv}/31 - EV: {p.atkev}\n**Defense:** {p.maxdef} - IV: {p.defiv}/31 - EV: {p.defev}\n**Sp. Atk:** {p.maxspatk} - IV: {p.spatkiv}/31 - EV: {p.spatkev}\n**Sp. Def:** {p.maxspdef} - IV: {p.spdefiv}/31 - EV: {p.spdefev}\n**Speed:** {p.maxspeed} - IV: {p.speediv}/31 - EV: {p.speedev}\n**Total IV %:** {p.totaliv}%\n**Total EV :** {p.totalev}/508""",color=clr)
        infos.set_author(name=ctx.author.display_name)
        infos.add_field(name="Moves:",value=known)
        infos.set_image(url=p.sprite)
        infos.set_thumbnail(url=ctx.author.avatar)
        infos.set_footer(text=f"Catching Date: {p.catchdate}\nDisplaying Pokémon: {nu}/{len(allmon)}")
        await ctx.send(embed=infos)
    else:
        await ctx.send("Unfortunately you don't have any Pokémon. Please catch some Pokémon using `!spawn` command.")    
@bot.command(aliases=["myl"])
async def mylistings(ctx,num=1):   
    dt=sqlite3.connect("pokemondata.db")
    ct=dt.cursor()
    db=sqlite3.connect("market.db")
    c=db.cursor()         
    c.execute(f"Select * from 'market' where sellerid={ctx.author.id}")
    n=c.fetchall()
    numbers=[]
    if len(n)!=0:
        for i in n:
            numbers.append(i)
        list_of_lists = []
        list_temp = []
        limit = 10
        # iterate through the list
        i = 0
        while i < len(numbers):
            if len(list_temp) < limit:
                list_temp.append(numbers[i])
                i += 1
            else:
                # when the limit is reached, add the sub-list to the list of lists
                list_of_lists.append(list_temp)
                list_temp = []
        # add the remaining items to the list of lists
        list_of_lists.append(list_temp)
        pages=len(list_of_lists)
        if 0<num<=len(list_of_lists):
            x=discord.Embed(title="Your listings in Pokémon Market:", description=f"There's total {len(n)} Pokémons you listed for sale.",color=0x220022)
            for i in list_of_lists[num-1]:
                c.execute(f"select * from 'market'")
                ll=c.fetchall()
                name=i[1]
                ct.execute(f"Select * from 'wild' where name='{i[0]}'")
                mon=ct.fetchone()
                icon=mon[22]
                ivp=round((i[3]+i[4]+i[5]+i[6]+i[7]+i[8])/1.86,2)
                x.add_field(name=f"#{i[28]} {icon} {name} {await teraicon(i[20])}",value=f"**Gender:** {i[19]} | **Ability:** {i[15]} | **IV:** {ivp}% | **Price:** {await numberify(i[26])} <:pokecoin:1134595078892044369>")
            x.set_footer(text=f"Showing {num} out of {len(list_of_lists)} pages.")
            await ctx.send(embed=x)
@bot.command(aliases=["mr"])     
async def market(ctx,num=1,*name):
    dt=sqlite3.connect("pokemondata.db")
    ct=dt.cursor()
    db=sqlite3.connect("market.db")
    c=db.cursor()         
    if name==():
        c.execute(f"Select * from 'market' order by totaliv DESC")
    if name!=():
        name=" ".join(name)
        name=name.title()
    if name!=() and name=="Shiny":
        c.execute(f"Select * from 'market' where shiny='Yes' order by totaliv DESC")
    elif name!=() and name!="Shiny":
        c.execute(f"Select * from 'market' where name='{name}' order by totaliv DESC")
    n=c.fetchall()
    numbers=[]
    if len(n)!=0:
        for i in n:
            numbers.append(i)
        list_of_lists = []
        list_temp = []
        limit = 10
        # iterate through the list
        i = 0
        while i < len(numbers):
            if len(list_temp) < limit:
                list_temp.append(numbers[i])
                i += 1
            else:
                # when the limit is reached, add the sub-list to the list of lists
                list_of_lists.append(list_temp)
                list_temp = []
        # add the remaining items to the list of lists
        list_of_lists.append(list_temp)
        pages=len(list_of_lists)
        if 0<num<=len(list_of_lists):
            x=discord.Embed(title="Pokémon Market:", description=f"There's total {len(n)} Pokémons for sale.",color=0x220022)
            for i in list_of_lists[num-1]:
                c.execute(f"select * from 'market'")
                ll=c.fetchall()
                name=i[1]
                ct.execute(f"Select * from 'wild' where name='{i[0]}'")
                mon=ct.fetchone()
                icon=mon[22]
                ivp=round((i[3]+i[4]+i[5]+i[6]+i[7]+i[8])/1.86,2)
                x.add_field(name=f"**ID:** {i[28]} | {icon} {name} {await teraicon(i[20])}",value=f"**Ability:** {i[15]} | **IV:** {ivp}%\n**Price:** {await numberify(i[26])} <:pokecoin:1134595078892044369>")
            x.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1134736129250300045/image_search_1690612550924.jpg")
            x.set_footer(text=f"Showing {num} out of {len(list_of_lists)} pages.")
            await ctx.send(embed=x)
@bot.command()     
async def wipepc(ctx):
    await ctx.send("Do you really wanna wipe your pc?\n⚠️ You will lose all your pokémons!")
    response = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if response.content.lower() in ["yes"]:
        db=sqlite3.connect("owned.db")
        c=db.cursor()
        c.execute(f"DROP table IF EXISTS '{ctx.author.id}'")
        db.commit()
    else:
        pass     
@bot.command()     
async def wipeacc(ctx):
    await ctx.send("Do you really wanna wipe your account?\n⚠️ You will lose all your items and pokécoins!")
    response = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if response.content.lower() in ["yes"]:
        db=sqlite3.connect("playerdata.db")
        c=db.cursor()
        c.execute(f"DROP table IF EXISTS '{ctx.author.id}'")
        db.commit()
    else:
        pass                
@bot.command(aliases=["pp"])     
async def pokemons(ctx,num=1,*name):
    "Shows all the captured pokémons."
    dt=sqlite3.connect("pokemondata.db")
    ct=dt.cursor()
    db=sqlite3.connect("owned.db")
    c=db.cursor()  
    if name!=():
        name=" ".join(name)
        name=name.title()
    elif name==():
        c.execute(f"Select * from '{ctx.author.id}'")
    if name!=() and name=="Shiny":
        c.execute(f"Select * from '{ctx.author.id}' where shiny='Yes'")
    elif name!=() and name=="Alpha":
        c.execute(f"Select * from '{ctx.author.id}' where nickname like '%<:alpha:1127167307198758923>%' order by totaliv DESC")
    elif name!=() and name=="Item":
        c.execute(f"Select * from '{ctx.author.id}' where item!='None'")
    elif name!=() and name=="Speediv":
        c.execute(f"Select * from '{ctx.author.id}' order by speediv DESC")
    elif name!=() and name=="Spdefiv":
        c.execute(f"Select * from '{ctx.author.id}' order by spdefiv DESC")
    elif name!=() and name=="Spatkiv":
        c.execute(f"Select * from '{ctx.author.id}' order by spatkiv DESC")
    elif name!=() and name=="Defiv":
        c.execute(f"Select * from '{ctx.author.id}' order by defiv DESC")
    elif name!=() and name=="Hpiv":
        c.execute(f"Select * from '{ctx.author.id}' order by hpiv DESC")
    elif name!=() and name=="Atkiv":
        c.execute(f"Select * from '{ctx.author.id}' order by atkiv DESC")
    elif name!=() and name in ["Iv","IV","iv"]:
        c.execute(f"Select * from '{ctx.author.id}' order by totaliv DESC")        
    elif name!=() and name in ["Common","Uncommon","Rare","Very Rare","Common Legendary","Legendary","Mythical","Ultra Beasts"]:
        c.execute(f"Select * from '{ctx.author.id}' where rarity='{name.title()}' order by totaliv DESC")
    elif name!=() and name not in ["Common","Uncommon","Rare","Very Rare","Common Legendary","Legendary","Mythical","Shiny","Ultra Beasts"]:
        c.execute(f"Select * from '{ctx.author.id}' where name like '%{name}' or name like '{name}%' order by totaliv DESC")
    n=c.fetchall()
    numbers=[]
    if len(n)!=0:
        for i in n:
            numbers.append(i)
        list_of_lists = []
        list_temp = []
        limit = 10
        # iterate through the list
        i = 0
        while i < len(numbers):
            if len(list_temp) < limit:
                list_temp.append(numbers[i])
                i += 1
            else:
                # when the limit is reached, add the sub-list to the list of lists
                list_of_lists.append(list_temp)
                list_temp = []
        # add the remaining items to the list of lists
        list_of_lists.append(list_temp)
        pages=len(list_of_lists)
        if 0<num<=len(list_of_lists):
            x=discord.Embed(title="Pokémon PC", description=f"You've caught {len(n)} total Pokémons.",color=0x220022)
            x.set_author(name=ctx.author.display_name)
            x.set_thumbnail(url=ctx.author.avatar)
            for i in list_of_lists[num-1]:
                c.execute(f"select * from '{ctx.author.id}'")
                ll=c.fetchall()
                k=(ll.index(i))+1
                name=i[1]
                ct.execute(f"Select * from 'wild' where name='{i[0]}'")
                mon=ct.fetchone()
                icon=mon[22]
                ivp=round((i[3]+i[4]+i[5]+i[6]+i[7]+i[8])/1.86,2)
                x.add_field(name=f"#{k} {icon} {name} {await teraicon(i[20])}",value=f"**Gender:** {i[19]} | **Ability:** {i[15]} | **IV:** {ivp}%")
            x.set_footer(text=f"Showing {num} out of {len(list_of_lists)} pages.")
            await ctx.send(embed=x)
    else:
        await ctx.send("Unfortunately you don't have any Pokémon. Please catch some Pokémon using `!spawn` command.")        
        
@bot.command(aliases=["rl"])            
async def release(ctx,num=1,force="No"):
    "Releases one of your selected pokémon."
    db=sqlite3.connect("owned.db")
    c=db.cursor()
    num=await row(ctx,num,c)
    c.execute(f"Select * from '{ctx.author.id}' where rowid={num}")
    r=c.fetchone()
    if force in ["y","yes"]:
       c.execute(f"delete from '{ctx.author.id}' where rowid={num}")
       db.commit()
       price=await pricetag(r)
       await addmoney(ctx,ctx.author,price)
       await ctx.send(f"{r[0]} was released!")
    elif force=="No":
        await ctx.send(f"Do you want to release {r[0]}?")
        while True:
            guess = await bot.wait_for('message')
            if "!" in guess.content:
                break
            elif guess.content.lower() in ["n","no"] and guess.author==ctx.author:
                await ctx.send(f"{r[0]} was't released!")
                break
            elif guess.content.lower() in ["y","yes"]and guess.author==ctx.author:
                c.execute(f"delete from '{ctx.author.id}' where rowid={num}")
                db.commit()
                price=await pricetag(r)
                await addmoney(ctx,ctx.author,price)
                await ctx.send(f"{r[0]} was released!")
                break
                
@bot.command(aliases=["mv"])
async def moves(ctx,num=1):
    "Shows all the available and learned moves of that particular pokémon."
    dt=sqlite3.connect("pokemondata.db")
    db=sqlite3.connect("owned.db")
    cx=dt.cursor()
    c=db.cursor()       
    num=await row(ctx,num,c)
    p,allmon=await pokonvert(ctx,ctx.author,num)
    c.execute(f"Select * from '{ctx.author.id}' where rowid={num}")
    mon=c.fetchone()
    move=eval(mon[22])
    cx.execute(f"Select * from 'wild' where name='{mon[0]}'")
    spc=cx.fetchone()
    canlearn=list(set(eval(spc[10])+["Tera Blast"])-set(move))
    known=""
    can=""
    n=0
    for i in move:
        n+=1
        known+=f"{await movetypeicon(p,i)} {i} {await movect(i)}\n"
    for i in canlearn:
        can+=f"{i}\n"
    now=discord.Embed(title=f"{mon[0]}'s Moveset:",color=0xff0000)
    now.add_field(name="Current Moveset:",value=known)
    now.add_field(name="Available Moves:",value=can)
    now.set_footer(text="!learn num 'move name' to update moveset.")
    now.set_image(url=spc[12])
    await ctx.send(embed=now)
@bot.command(aliases=["nn"])
async def nickname(ctx,num=1,select="None"):
    if select!="None":
        dt=sqlite3.connect("pokemondata.db")
        db=sqlite3.connect("owned.db")
        cx=dt.cursor()
        c=db.cursor()
        num=await row(ctx,num,c)       
        c.execute(f"select * from `{ctx.author.id}` where rowid={num}")
        mon=c.fetchone()
        if "<:traded:1127340280966828042>" in mon[1]:
            select=select+" <:traded:1127340280966828042>"
        if "<:shiny:1127157664665837598>" in mon[1]:
            select=select+" <:shiny:1127157664665837598>"
        elif "<:alpha:1127167307198758923>" in mon[1]:
            select=select+" <:alpha:1127167307198758923>"
        elif "<:hatched:1134745434506666085>" in mon[1]:
            select=select+" <:hatched:1134745434506666085>"            
        c.execute(f"""Update `{ctx.author.id}` set nickname="{select}" where rowid={num}""") 
        db.commit()
        await ctx.send(f"Nickname updated!")
@bot.command(aliases=["lr"])
async def learn(ctx,num=1,*select):
    "Teaches your pokémon a certain move."
    if select!="None":
        select=(" ".join(select)).strip()
        select=select.title()
        dt=sqlite3.connect("pokemondata.db")
        db=sqlite3.connect("owned.db")
        cx=dt.cursor()
        c=db.cursor()
        num=await row(ctx,num,c)        
        p,allmon=await pokonvert(ctx,ctx.author,num) 
        c.execute(f"Select * from '{ctx.author.id}' where rowid={num} ")
        mon=c.fetchone()
        move=eval(mon[22])
        cx.execute(f"Select * from 'wild' where name='{mon[0]}'")
        spc=cx.fetchone()
        canlearn=eval(spc[10])+["Tera Blast"]
        known=""
        n=0
        for i in move:
            n+=1
            known+=f"{await movetypeicon(p,i)} {i} ({n}) {await movect(i)}\n"    
        now=discord.Embed(title=f"{mon[0]}'s Moveset:", description=f"Select a move to replace with {select}!",color=0xff0000)
        now.add_field(name="New Move:",value=f"{await movetypeicon(p,select)} {select} {await movect(select)}")
        now.add_field(name="Current Moveset:",value=known)
        now.set_footer(text="Enter the 'number' of the move you want to replace!")
        if select in canlearn and select not in move:
            await ctx.send(embed=now)
            while True:
                response = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                if response.author==ctx.author and "!" in response.content:
                    break
                if response.author==ctx.author and 0<int(response.content)<=4:
                    rep=move[int(response.content)-1]
                    move[int(response.content)-1]=select
                    move=f"{move}".replace('"',"'")
                    c.execute(f"""Update `{ctx.author.id}` set moves="{move}" where rowid={num}""")
                    db.commit()
                    db.close()
                    await ctx.send(f"{rep} was replaced by {select}!")
                    break
        else:
            await ctx.send(f"{mon[0]} cannot learn {select} or you misspelled it.")          
                  
@bot.command(aliases=["ev"])
async def evtrain(ctx,num=1,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0):
    "EV trains your pokémon for free!"
    evlist=[hpev,atkev,defev,spatkev,spdefev,speedev]
    total=hpev+atkev+defev+spatkev+spdefev+speedev
    if max(evlist)<=252 and len(evlist)==6 and total<=508:
        db=sqlite3.connect("owned.db")
        c=db.cursor()
        num=await row(ctx,num,c)
        c.execute(f"""Update `{ctx.author.id}` set 
        hpev="{hpev}",
        atkev="{atkev}",
        defev="{defev}",
        spatkev="{spatkev}",
        spdefev="{spdefev}",
        speedev="{speedev}"
        where rowid={num}""")
        db.commit()
        await ctx.send("EV training complete.")
    else:
        await ctx.send("Invalid input.") 
        
@bot.command(aliases=["it"])      
async def items(ctx,*item):
    "Shows you an item."
    item=" ".join(item)
    item=item.title()
    db=sqlite3.connect("pokemondata.db")    
    c=db.cursor()   
    c.execute(f"select * from 'itemshop' where item='{item}'")
    item=c.fetchone()
    show=discord.Embed(title=f"{item[0]}", description=f"**Price:** {await numberify(item[1])} <:pokecoin:1134595078892044369>")
    if item[3]!="None":
        show.add_field(name="Description:",value=item[3])
    show.set_thumbnail(url=item[2])
    show.set_footer(text="Use `!buy 'item name' to buy the item.")
    await ctx.send(embed=show)
    
@bot.command(aliases=["br"])    
async def breed(ctx,mon1=1,mon2=2):
    "Breed two compatible pokémons. Costs 5,000 <:pokecoin:1134595078892044369>."
    db=sqlite3.connect("owned.db")
    c=db.cursor()
    num1=await row(ctx,mon1,c)
    num2=await row(ctx,mon2,c)
    mon1=await pokonvert(ctx,ctx.author,num1)
    mon2=await pokonvert(ctx,ctx.author,num2)
    mon1=mon1[0]
    mon2=mon2[0]
    eg1=await egggroup(ctx,mon1.name)
    eg2=await egggroup(ctx,mon2.name)
    canbreed=await common(eg1.split(","),eg2.split(","))
    dn=sqlite3.connect("playerdata.db")
    cn=dn.cursor()
    cn.execute(f"select * from '{ctx.author.id}'")
    mmm=cn.fetchone()
    money=mmm[0]
    if (mon1.gender!=mon2.gender and "Undiscovered" not in (eg1,eg2) and canbreed==True) or ("Ditto" in (mon2.name,mon1.name) and "Undiscovered" not in (eg1,eg2)) and money>=5000:
        dt=sqlite3.connect("pokemondata.db")
        ct=dt.cursor()
        name=""
        if mon1.gender=="Female":
            name=mon1.name
        elif mon2.gender=="Female":
            name=mon2.name
        elif mon1.name=="Ditto":
            name=mon2.name
        elif mon2.name=="Ditto":
            name=mon1.name
        ct.execute(f"Select * from 'wild' where name='{name}' ")
        m=ct.fetchone()
        hpiv=max([mon1.hpiv,mon2.hpiv])
        atkiv=max([mon1.atkiv,mon2.atkiv])
        defiv=max([mon1.defiv,mon2.defiv])
        spatkiv=max([mon1.spatkiv,mon2.spatkiv])
        spdefiv=max([mon1.spdefiv,mon2.spdefiv])
        speediv=max([mon1.speediv,mon2.speediv])
        shinyodd=random.randint(1,256)
        shiny="No"
        if shinyodd==7:
            shiny="Yes"
        p=Pokemon(name=m[0],primaryType=m[1],secondaryType=m[2],level=m[3],hp=m[4],atk=m[5],defense=m[6],spatk=m[7],spdef=m[8],speed=m[9],moves=m[10], ability=m[11],sprite=m[12],gender=m[15],maxiv="Custom",shiny=shiny,hpiv=hpiv,atkiv=atkiv,defiv=defiv,spatkiv=spatkiv,spdefiv=spdefiv,speediv=speediv)
        p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
        p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)  
        bred=discord.Embed(title="Proceed breeding?", description=f"Sacrifice {mon1.name} and {mon2.name} to breed a better pokémon!\nPrice: 5,000 <:pokecoin:1134595078892044369>")
        types=p.primaryType
        if p.secondaryType!="???":
            types=f"{p.primaryType}/{p.secondaryType}"
        bred.add_field(name=f"Newborn {p.name}", value=f"""**Types:** {types}\n**Tera-Type:** {p.tera}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {p.item}\n**HP:** {p.maxhp} - IV: {p.hpiv}/31 - EV: {p.hpev}\n**Attack:** {p.maxatk} - IV: {p.atkiv}/31 - EV: {p.atkev}\n**Defense:** {p.maxdef} - IV: {p.defiv}/31 - EV: {p.defev}\n**Sp. Atk:** {p.maxspatk} - IV: {p.spatkiv}/31 - EV: {p.spatkev}\n**Sp. Def:** {p.maxspdef} - IV: {p.spdefiv}/31 - EV: {p.spdefev}\n**Speed:** {p.maxspeed} - IV: {p.speediv}/31 - EV: {p.speedev}\n**Total IV %:** {p.totaliv}%\n**Total EV :** {p.totalev}/508""")
        bred.set_image(url=p.sprite)
        await ctx.send(embed=bred)
        while True:
            ans=await bot.wait_for('message',check=lambda message: message.author==ctx.author)
            if "!" in ans.content or ans.content.lower() in ["n","no"]:
                await ctx.send("Breeding cancelled!")
                break
            if ans.content.lower() in ["y","yes"]:
                c.execute(f"Select *,rowid from '{ctx.author.id}'")
                r=c.fetchall()
                num=[num1,num2]
                num.sort()
                c.execute(f"delete from '{ctx.author.id}' where rowid={num[1]}")
                db.commit()
                c.execute(f"delete from '{ctx.author.id}' where rowid={num[0]}")
                db.commit()
                clk=datetime.datetime.now()
                catchtime=clk.strftime("%Y-%m-%d %H:%M:%S")
                if "<:hatched:1134745434506666085>" not in p.nickname:
                    p.nickname=p.nickname+" <:hatched:1134745434506666085>"
                c.execute(f"""INSERT INTO "{ctx.author.id}" VALUES (
                "{p.name}",
                "{p.nickname}",
                "{p.level}",
                "{p.hpiv}",
                "{p.atkiv}",
                "{p.defiv}",
                "{p.spatkiv}",
                "{p.spdefiv}",
                "{p.speediv}",
                "{p.hpev}",
                "{p.atkev}",
                "{p.defev}",
                "{p.spatkev}",
                "{p.spdefev}",
                "{p.speedev}",
                "{p.ability}",
                "{p.nature}",
                "{p.shiny}",
                "{p.item}",
                "{p.gender}",
                "{p.tera}",
                "Custom",
                "{p.moves}",
                "{m[14]}",
                "{catchtime}",
                "{p.totaliv}")""")
                db.commit()
                await addmoney(ctx,ctx.author,-5000)
                await ctx.send("Breeding successful!")
                break
    else:
        await ctx.send(f" You can't breed a {mon1.gender} {mon1.name} with a {mon2.gender} {mon2.name} or You don't have sufficient balance!")
    

    


@bot.command(aliases=["dr"])
async def drop(ctx,num=1):
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"Select * from '{ctx.author.id}'")
    items=c.fetchone()
    items=eval(items[2])
    dt=sqlite3.connect("owned.db")
    ct=dt.cursor()
    num=await row(ctx,num,ct)
    ct.execute(f"select item from '{ctx.author.id}' where rowid={num}")
    item=ct.fetchone()
    item=item[0]
    if item!="None":
        items.append(item)
        items=f"{items}"
        c.execute(f"""update '{ctx.author.id}' set Items="{items}" """)
        db.commit()
        ct.execute(f"update '{ctx.author.id}' set item='None' where rowid={num}")
        dt.commit()
        await ctx.send(f"{item} was sent to your inventory!")
    if item=="None":
        await ctx.send(f"It's not holding any item!")
        
@bot.command()
async def buy(ctx,*item):
    item=" ".join(item)
    item=item.title()
    db=sqlite3.connect("pokemondata.db")
    c=db.cursor()
    c.execute(f"select * from 'itemshop' where item='{item}'")
    item=c.fetchone()
    dt=sqlite3.connect("playerdata.db")
    ct=dt.cursor()
    ct.execute(f"select * from '{ctx.author.id}'")
    b=ct.fetchone()
    balance=b[0]
    if item[1]>balance:
        await ctx.reply("You don't have enough balance!")
    if item[1]<balance:
        em=discord.Embed(title=f"Would you like to buy {item[0]}?",description=f"**Price:** {await numberify(item[1])} <:pokecoin:1134595078892044369>\n**Balance after purchase:** {balance-item[1]} <:pokecoin:1134595078892044369>")
        em.set_thumbnail(url=item[2])
        await ctx.send(embed=em)
        while True:
            response=await bot.wait_for('message')
            ct.execute(f"select * from '{ctx.author.id}'")
            b=ct.fetchone()
            balance=b[0]
            if response.content.lower() in ["n","no","!"] and response.author==ctx.author and item[1]>balance:
                await ctx.reply("You canceled the purchase!")
                break
            if response.content.lower() in ["y","yes"] and response.author==ctx.author and item[1]<balance:
                await addmoney(ctx,ctx.author,-item[1])
                items=eval(b[2])
                items.append(item[0])
                ct.execute(f"""update '{ctx.author.id}' set Items="{items}" """)
                dt.commit()
                await ctx.send(f"You purchased a {item[0]}!")
                break
@bot.command()    
async def bag(ctx,num=1):             
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"Select * from '{ctx.author.id}'")
    items=c.fetchone()
    items=eval(items[2])
    items.sort()
    newdic=await listtodic(items)
    sub=await gensub(num,newdic)
    tot=round(len(newdic)//15)+1
    bag=discord.Embed(title=f"{ctx.author.display_name}'s Backpack:",description=f"Total item: {len(items)}")
    txt=""
    if len(items)!=0:
        for k,v in sub.items():
            txt+=f"{await itemicon(k)} {k} ×{v}\n"
        bag.add_field(name="Item List:",value=txt)
    else:
        bag.add_field(name="Item List:",value="Your backpack is empty!")     
    bag.set_footer(text=f"Showing {num} out of {tot} pages")
    bag.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1134073215803723827/image_search_1690454504333.png")       
    await ctx.send(embed=bag)
        
@bot.command()    
async def giveitem(ctx,num=1,*it):
    it=" ".join(it)
    it=it.title()
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"Select * from '{ctx.author.id}'")
    items=c.fetchone()
    items=eval(items[2])
    dt=sqlite3.connect("owned.db")
    ct=dt.cursor()
    num=await row(ctx,num,ct)
    ct.execute(f"select item from '{ctx.author.id}' where rowid={num}")
    item=ct.fetchone()
    item=item[0]
    if item!="None":
        items.append(item)
        items=f"{items}"
        c.execute(f"""update '{ctx.author.id}' set Items="{items}" """)
        db.commit()
        ct.execute(f"update '{ctx.author.id}' set item='None'")
        dt.commit()
        items=eval(items)
        await ctx.send(f"{item} was sent to your inventory!")
    if it in items:
        ct.execute(f"update '{ctx.author.id}' set item='{it}' where rowid={num}")
        dt.commit()
        items.remove(it)
        items=f"{items}"
        c.execute(f"""update '{ctx.author.id}' set Items="{items}" """)
        db.commit()
        ct.execute(f"select * from '{ctx.author.id}' where rowid={num}")
        x=ct.fetchone()
        await ctx.send(f"{x[0]} is now holding a {it}!")
async def egggroup(ctx,name):
    db=sqlite3.connect("pokemondata.db")          
    c=db.cursor() 
    c.execute(f"Select * from 'wild' where name='{name}'")
    n=c.fetchone()
    return n[18]
async def common(l1,l2):
    for i in l1:
        if i in l2:
            return True
    return False            
    
@bot.command(aliases=["ti"])
async def trainerinfo(ctx,num=0):
    tr1=await gameteam(ctx,num)
    db=sqlite3.connect("pokemondata.db")
    c=db.cursor()
    mm=tr1.name.split("> ")[-1]
    c.execute(f"select * from 'Trainers' where name='{mm}'")
    dat=c.fetchone()
    n=0
    txt=""
    if dat!=None:
        if dat[1]!="None":
            txt=f"\n**Badge:**\n{dat[2]} {dat[1]}"
    info=discord.Embed(title=f"{tr1.name}'s Team:",description=f"This is a team sample. You can't rely on it entirely. But you can get an idea about who you are dealing with.{txt}")
    info.set_thumbnail(url=tr1.sprite)
    for i in tr1.pokemons:
        n+=1
        info.add_field(name=f"#{n} {i.icon} {i.nickname} {await teraicon(i.tera)}",value=f"**Ability:** {i.ability}\n**Item:** {await itemicon(i.item)} {i.item}\n{await movetypeicon(i,i.moves[0])} {i.moves[0]} {await movect(i.moves[0])}\n{await movetypeicon(i,i.moves[1])} {i.moves[1]} {await movect(i.moves[1])}\n{await movetypeicon(i,i.moves[2])} {i.moves[2]} {await movect(i.moves[2])}\n{await movetypeicon(i,i.moves[3])} {i.moves[3]} {await movect(i.moves[3])}")
    await ctx.send(embed=info)        

@bot.command(aliases=["cm"])
async def commands(ctx,c="None"):
    c=c.lower()
    if c=="none":
        em=discord.Embed(title="Command List:",description="**Start:** `!commands start` or `!cm start`\n**Spawn:** `!commands spawn` or `!cm spawn`\n**Information:** `!commands info` or `!cm info`\n**Pokémon List:** `!commands pokemons` or `!cm pokemons`\n**Team Building:** `!commands team` or `!cm team`")
    elif c=="team":
        em=discord.Embed(title="Team Building:",description="**Command:** `!team` or `!tm`\nYou have 6 arguments in this command. If you simply use `!tm` it will build your team using 1st six pokémons of your list. You can customize your team like `!tm 3 6 5 87 167 540` those numbers are the #num of the pokémons you caught. You can only take 6 pokémons in your party. This party will be used in battles.")
    elif c=="pokemons":
        em=discord.Embed(title="Pokémon List:",description="**Command:** `!pokemons` or `!pp`\nAfter using the command without any argument it will show your 1st 10 pokémons. If you have enough pokémons you can choose page numbers as well.For example: `!pp 2` . You can also search specific pokémon species. For example `!pp 1 Charizard` . It will  show how many Charizards you got. You can also find shiny in your list by doing `!pp 1 Shiny`. Basically the number indicates the page number. You can use it to locate efficiently.")
    elif c=="start":
        em=discord.Embed(title="Start:",description="**Command:** `!start` or `!st`\nAfter using the command you'll be given a list of starters from Gen I-IX. You can choose your favorite starter by writing it's name. You'll also get 10,000<:pokecoin:1134595078892044369> starting cash.\n**Example:** msg1:`!st` msg2: Charizard")
    elif c=="info":
        em=discord.Embed(title="Information:",description="**Command:** `!info` or `!pi` or `!info pokémonnumber` or `!pi pokémonnumber`\nAfter using this command you you'll get to see all the necessary infos about your pokémon. If you don't enter any pokémon number it will show you your latest caught pokémon.\n**Example:** `!pi 1` will show you #1 pokémon from your pokémon list. and `!pi` will show your last pokémon")     
    elif c=="spawn":
        em=discord.Embed(title="Spawn:",description="**Command:** `!spawn` or `!sp`\nAfter using this command a pokémon will spawn.You can catch it by simply writing it's name in your next text. Spawning costs 500<:pokecoin:1134595078892044369> and returns you back 250<:pokecoin:1134595078892044369> if you capture it successfully. If other people snipe your spawn they will catch the pokémon but lose 750<:pokecoin:1134595078892044369>.You can find various kind of pokémons based on rarity.You can find *Alpha* and *Shiny* pokémons. You can also find pokémon with different *Tera-Type*. Endless possibilities.")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1124598531504742440/image_search_1688195566002.webp")  
    await ctx.send(embed=em)          
    