from intro import *
@bot.command(aliases=["ts"])        
async def test(ctx):
    "Test command"
    await battle(ctx,ctx.author)
@bot.command(aliases=["cf"])    
async def coinflip(ctx,choice,amount=100):
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
@bot.command(aliases=["dx"], description="Shows Pokémon!")
async def dex(ctx,name,cat="No"):  
    name=name.title()
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
        text=f"You haven't caught any {name} yet!"
    if len(ch)>0:
        text=f"You have caught {len(ch)} {name}!"
    if len(x)!=0: 
        p=x[0]
        total=p[4]+p[5]+p[6]+p[7]+p[8]+p[9]
        sprite=p[12]
        name=p[0]
        rare=p[14]
        if cat.lower()=="gmax":
            name="Gigantamax "+p[0]
            sprite=sprite.split(".gif")[0]+"-gmax.gif"
        if cat.lower()=="shiny":
            rare="Almost Impossible"
            name="Shiny "+p[0]
            sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/"+sprite.split("/")[-1]
        types=p[1]
        if p[2]!="???":
            types=f"{p[1]}/{p[2]}"
        data=discord.Embed(title=f"{name}", color=0x00ff00)
        data.add_field(name="Infos",value=f"**Types:** {types}\n**Abilities:** {p[11]}\n**Rarity:** {rare}\n**Weight:** {p[13]} lbs\n**Region:** {p[16]}")
        data.add_field(name=f"Base Stats: {total}",value=f"""**HP:** {p[4]}\n**Attack:** {p[5]}\n**Defense:** {p[6]}\n**Sp. Atk:** {p[7]}\n**Sp. Def:** {p[8]}\n**Speed:** {p[9]}""")
        data.set_image(url=sprite) 
        data.set_footer(text=text)
        await ctx.send(embed=data)
        
@bot.command(aliases=["sp"], description="Spawns Pokémon!")
async def spawn(ctx):
    "Spawns wild Pokémons"
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
            tch=random.randint(1,50)
            ach=random.randint(1,100)
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
                if p.name.lower() in guess.content.lower():
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
                    time text)""")
                    clk=datetime.datetime.now()
                    catchtime=clk.strftime("%Y-%m-%d %H:%M:%S")
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
                    "{catchtime}")""")
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
        
@bot.command(aliases=["st"])            
async def start(ctx):
    dt=sqlite3.connect("playerdata.db")
    ct=dt.cursor()
    ct.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{ctx.author.id}' ")
    if ct.fetchone():
        await ctx.send("You already have an account!")
    else:
        ct.execute(f"""CREATE TABLE IF NOT EXISTS [{ctx.author.id}] (
        Balance integer,
        Squad text,
        Items text
        )""")
        ct.execute(f"""INSERT INTO "{ctx.author.id}" VALUES (
        "10000",
        "0,0,0,0,0,0",
        "[]")""")
        dt.commit()
        await ctx.send("Account created successfully.")
        db=sqlite3.connect("pokemondata.db")
        dx=sqlite3.connect("owned.db")
        c=db.cursor()
        cx=dx.cursor()
        ann=discord.Embed(title="Choose your starter:", description="Enter the fullname of the starter to claim it.")
        ann.add_field(name="Kanto",value="Venusaur\nCharizard\nBlastoise")
        ann.add_field(name="Johto",value="Meganium\nThyphlosion\nFeraligatr")
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
            if nam in "Venusaur\nCharizard\nBlastoiseMeganium\nThyphlosion\nFeraligatrSceptile\nBlaziken\nSwampertTorterra\nInfernape\nEmpoleonSerperior\nEmboar\nSamurottChesnaught\nDelphox\nGreninjaDecidueye\nIncineroar\nPrimarinaRillaboom\nCinderace\nInteleonMeowscarada\nSkeledirge\nQuaquaval":
                c.execute(f"Select * from 'wild' where name='{nam}'")
                m=c.fetchone()
                if m!=None and len(m)!=0:
                    shinyodd=random.randint(1,512)
                    shiny="No"
                    if shinyodd==7:
                        shiny="Yes"
                    p=Pokemon(name=m[0],primaryType=m[1],secondaryType=m[2],level=m[3],hp=m[4],atk=m[5],defense=m[6],spatk=m[7],spdef=m[8],speed=m[9],moves=m[10], ability=m[11],sprite=m[12],gender=m[15],shiny=shiny)
                    p.moves=f"{p.moves}"
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
                    time text)""")
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
                    "{catchtime}")""")
                    dx.commit()
                    db.commit()
                    show=discord.Embed(title=f"Congratulations {ctx.author.display_name}! You chose {p.name} as your starter!")
                    show.set_thumbnail(url=ctx.author.avatar)
                    show.set_image(url=p.sprite)
                    show.set_footer(text="Enter '!info' to see more details or '!spawn' to start catching pokémons.")
                    await ctx.send(embed=show)
                    break
        
        
@bot.command(aliases=["pi"])
async def info(ctx,num=None):
    p,allmon=await pokonvert(ctx,ctx.author,num)
    if len(allmon)!=0:
        if num==None:
            num=len(allmon)
        types=p.primaryType
        if p.secondaryType!="???":
            types=f"{p.primaryType}/{p.secondaryType}"
        p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
        p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)  
        infos=discord.Embed(title=f"#{num} {p.nickname} Lv.{p.level}", description=f"""**Types:** {types}\n**Tera-Type:** {p.tera}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {p.item}\n**HP:** {p.maxhp} - IV: {p.hpiv}/31 - EV: {p.hpev}\n**Attack:** {p.maxatk} - IV: {p.atkiv}/31 - EV: {p.atkev}\n**Defense:** {p.maxdef} - IV: {p.defiv}/31 - EV: {p.defev}\n**Sp. Atk:** {p.maxspatk} - IV: {p.spatkiv}/31 - EV: {p.spatkev}\n**Sp. Def:** {p.maxspdef} - IV: {p.spdefiv}/31 - EV: {p.spdefev}\n**Speed:** {p.maxspeed} - IV: {p.speediv}/31 - EV: {p.speedev}\n**Total IV %:** {p.totaliv}%\n**Total EV :** {p.totalev}/508""",color=0x00ff00)
        infos.set_author(name=ctx.author.display_name)
        infos.set_image(url=p.sprite)
        infos.set_thumbnail(url=ctx.author.avatar)
        infos.set_footer(text=f"Catching Date: {p.catchdate}\nDisplaying Pokémon: {num}/{len(allmon)}")
        await ctx.send(embed=infos)
    else:
        await ctx.send("Unfortunately you don't have any Pokémon. Please catch some Pokémon using `!spawn` command.")         
@bot.command(aliases=["pp"])     
async def pokemons(ctx,num=1,name="None"):
    db=sqlite3.connect(f"owned.db")
    c=db.cursor()  
    if name=="None":
        c.execute(f"Select * from '{ctx.author.id}'")
    if name!="None" and name.title()=="Shiny":
        c.execute(f"Select * from '{ctx.author.id}' where shiny='Yes'")
    if name!="None" and name in ["Common","Uncommon","Rare","Very Rare","Common Legendary","Legendary","Mythical"]:
        c.execute(f"Select * from '{ctx.author.id}' where rarity='{name.title()}'")
    if name!="None" and name not in ["Common","Uncommon","Rare","Very Rare","Common Legendary","Legendary","Mythical","Shiny"]:
        name=name.title()
        c.execute(f"Select * from '{ctx.author.id}' where name='{name}'")
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
                ivp=round((i[3]+i[4]+i[5]+i[6]+i[7]+i[8])/1.86,2)
                x.add_field(name=f"#{k} {name}",value=f"**Gender:** {i[19]} | **Ability:** {i[15]} | **IV:** {ivp}%")
            x.set_footer(text=f"Showing {num} out of {len(list_of_lists)} pages.")
            await ctx.send(embed=x)
    else:
        await ctx.send("Unfortunately you don't have any Pokémon. Please catch some Pokémon using `!spawn` command.")        
@bot.command(aliases=["rl"])            
async def release(ctx,num=1,force="No"):
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
    dt=sqlite3.connect("pokemondata.db")
    db=sqlite3.connect("owned.db")
    cx=dt.cursor()
    c=db.cursor()       
    num=await row(ctx,num,c)
    c.execute(f"Select * from '{ctx.author.id}' where rowid={num} ")
    mon=c.fetchone()
    move=eval(mon[22])
    cx.execute(f"Select * from 'wild' where name='{mon[0]}'")
    spc=cx.fetchone()
    canlearn=eval(spc[10])
    known=""
    can=""
    n=0
    for i in move:
        n+=1
        known+=f"#{n} {i}\n"
    for i in canlearn:
        can+=f"{i}\n"
    now=discord.Embed(title=f"{mon[0]}'s Moveset:",color=0xff0000)
    now.add_field(name="Current Moveset:",value=known)
    now.add_field(name="Available Moves:",value=can)
    now.set_footer(text="!learn num 'move name' to update moveset.")
    now.set_image(url=spc[12])
    await ctx.send(embed=now)
        
@bot.command(aliases=["lr"])
async def learn(ctx,num=1,select=None):
    if select!="None":
        select=select.title()
        dt=sqlite3.connect("pokemondata.db")
        db=sqlite3.connect("owned.db")
        cx=dt.cursor()
        c=db.cursor()
        num=await row(ctx,num,c)         
        c.execute(f"Select * from '{ctx.author.id}' where rowid={num} ")
        mon=c.fetchone()
        move=eval(mon[22])
        cx.execute(f"Select * from 'wild' where name='{mon[0]}'")
        spc=cx.fetchone()
        canlearn=eval(spc[10])
        known=""
        n=0
        for i in move:
            n+=1
            known+=f"#{n} {i}\n"    
        now=discord.Embed(title=f"{mon[0]}'s Moveset:", description=f"Select a move to replace with {select}!",color=0xff0000)
        now.add_field(name="Current Moveset",value=known)
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
async def items(ctx,item):
    item=item.title()
    db=sqlite3.connect("pokemondata.db")    
    c=db.cursor()   
    c.execute(f"select * from 'itemshop' where item='{item}'")
    item=c.fetchone()
    show=discord.Embed(title=f"{item[0]}", description=f"**Price:** {item[1]} ¥")
    if item[3]!="None":
        show.add_field(name="Description:",value=item[3])
    show.set_thumbnail(url=item[2])
    show.set_footer(text="Use `!buy 'item name' to buy the item.")
    await ctx.send(embed=show)
    
@bot.command(aliases=["br"])    
async def breed(ctx,mon1,mon2):
    num1=mon1
    num2=mon2
    mon1=await pokonvert(ctx,ctx.author,mon1)
    mon2=await pokonvert(ctx,ctx.author,mon2)
    mon1=mon1[0]
    mon2=mon2[0]
    dn=sqlite3.connect("playerdata.db")
    cn=dn.cursor()
    cn.execute(f"select * from '{ctx.author.id}'")
    mmm=cn.fetchone()
    money=mmm[0]
    if (mon1.gender!=mon2.gender and "Genderless" not in (mon1.gender,mon2.gender) and mon1.name in mon2.name) or "Ditto" in (mon2.name,mon1.name) and money>=10000:
        dt=sqlite3.connect("pokemondata.db")
        db=sqlite3.connect("owned.db")
        ct=dt.cursor()
        c=db.cursor()
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
        bred=discord.Embed(title="Proceed breeding?", description=f"Sacrifice {mon1.name} and {mon2.name} to breed a better pokémon!")
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
                num1=await row(ctx,int(num1),c)
                num2=await row(ctx,int(num2),c)
                num=[num1,num2]
                num.sort()
                c.execute(f"delete from '{ctx.author.id}' where rowid={num[1]}")
                db.commit()
                c.execute(f"delete from '{ctx.author.id}' where rowid={num[0]}")
                db.commit()
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
                "{len(r)+1}")""")
                db.commit()
                await addmoney(ctx,ctx.author,-10000)
                await ctx.send("Breeding successful!")
                break
    else:
        await ctx.send(f" You can't breed a {mon1.gender} {mon1.name} with a {mon2.gender} {mon2.name} or You don't have sufficient balance!")
    
async def pokonvert(ctx,member,num=None):
    if num!=None:
        num=int(num)
    dt=sqlite3.connect("pokemondata.db")
    db=sqlite3.connect("owned.db")
    cx=dt.cursor()
    c=db.cursor()
    allmon=[]
    c.execute(f"select * from '{member.id}'")
    allmon=c.fetchall()
    if num==None:
        num=len(allmon)
    if len(allmon)<num:
        await ctx.send("Invalid Pokémon.")
    if len(allmon)>=num:
        n=allmon[num-1]
        cx.execute(f"select * from 'wild' where name='{n[0]}' ")
        m=cx.fetchall()[0]
        p=Pokemon(name=m[0],nickname=n[1],primaryType=m[1],secondaryType=m[2],level=m[3],hp=m[4],atk=m[5],defense=m[6],spatk=m[7],spdef=m[8],speed=m[9],moves=n[22], ability=n[15],sprite=m[12],gender=n[19],tera=n[20],maxiv="Custom",item=n[18],shiny=n[17],nature=n[16],hpiv=n[3],atkiv=n[4],defiv=n[5],spatkiv=n[6],spdefiv=n[7],speediv=n[8],hpev=n[9],atkev=n[10],defev=n[11],spatkev=n[12],spdefev=n[13],speedev=n[14],catchdate=n[24])
    try:        
        return p,allmon
    except:
        return "None",allmon
    
async def row(ctx,num,c):
    c.execute(f"select *,rowid from '{ctx.author.id}'")    
    hh=c.fetchall()
    num=hh[num-1][25]            
    return num        
async def pricetag(r):
    price=0
    iv=round((r[3]+r[4]+r[5]+r[6]+r[7]+r[8])/186,2)
    if r[23]=="Common":
        price=random.randint(100,200)
    elif r[23]=="Uncommon":
        price=random.randint(300,400)
    elif r[23]=="Rare":
        price=random.randint(500,700)
    elif r[23]=="Very Rare":
        price=random.randint(1000,1500)
    elif r[23]=="Common Legendary":
        price=random.randint(5000,7500)
    elif r[23]=="Legendary":
        price=random.randint(15000,20000)
    elif r[23]=="Mythical":
        price=random.randint(30000,50000)
    price=int(price+price*iv)   
    return price          
    
async def addmoney(ctx,member,price):
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"select * from '{member.id}'")
    m=c.fetchone()
    money=m[0]+price
    c.execute(f"update '{member.id}' set balance={money}")
    db.commit()
    if price>0:
        await ctx.send(f"¥ {price} added to your balance!")
    if price<0:
        price=-price
        await ctx.send(f"¥ {price} was deducted from your balance!")
        
@bot.command()
async def itemdiscard(ctx,num=1):
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
async def buy(ctx,item):
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
        em=discord.Embed(title=f"Would you like to buy {item[0]}?",description=f"**Price:** {item[1]} ¥\n**Balance after purchase:** {balance-item[1]} ¥")
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
async def giveitem(ctx,num=1,it="None"):
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
    if it.title() in items:
        ct.execute(f"update '{ctx.author.id}' set item='{it}' where rowid={num}")
        dt.commit()
        items.remove(it)
        items=f"{items}"
        c.execute(f"""update '{ctx.author.id}' set Items="{items}" """)
        db.commit()
        ct.execute(f"select * from '{ctx.author.id}' where rowid={num}")
        x=ct.fetchone()
        await ctx.send(f"{x[0]} is now holding a {it}!")
        
        
    
    