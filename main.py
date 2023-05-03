from intro import *
@bot.command(aliases=["ts"])        
async def test(ctx):
    "Test command"
    await battle(ctx,ctx.author)
@bot.command(aliases=["dx"], description="Shows Pokémon!")
async def dex(ctx,name,cat="No"):  
    name=name.title()
    db=sqlite3.connect("pokemondata.db")
    c=db.cursor()   
    dt=sqlite3.connect("playerdata.db")
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
    db=sqlite3.connect("pokemondata.db")
    dt=sqlite3.connect("playerdata.db")
    cx=dt.cursor()
    c=db.cursor()
    select=random.choices(["Common","Uncommon","Rare","Very Rare","Common Legendary","Legendary","Mythical"],weights=[500,190,70,50,10,3,1],k=1)[0]
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
            if tera=="Psychic":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076287830048820/Psychic_Tera.png"
            if tera=="Ice":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076210961023176/Ice_Tera.png"
            if tera=="Bug":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103075280286928977/Bug_Tera.png"
            if tera=="Normal":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076242779033621/Normal_Tera.png"
            if tera=="Ghost":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076146045780029/Ghost_Tera.png"
            if tera=="Dark":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103075420561232012/Dark_Tera.png"
            if tera=="Poison":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076263649886238/Poison_Tera.png"
            if tera=="Steel":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076336458801244/Steel_Tera.png"
            if tera=="Dragon":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103075563830251681/Dragon_Tera.png"
            if tera=="Fairy":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103075789353779250/Fairy_Tera.png"
            if tera=="Fighting":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103075834341888111/Fighting_Tera.png"
            if tera=="Flying":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103075897306779668/Flying_Tera.png"
            if tera=="Ground":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076191293952111/Ground_Tera.png"
            if tera=="Electric":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103075609116164217/Electric_Tera.png"
            if tera=="Grass":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076168170733719/Grass_Tera.png"
            if tera=="Water":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076350341951498/Water_Tera.png"
            if tera=="Rock":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103076317685088358/Rock_Tera.png"
            if tera=="Fire":
                turl="https://cdn.discordapp.com/attachments/1102579499989745764/1103075867854372905/Fire_Tera.png"
        
    p=Pokemon(name=m[0],primaryType=m[1],secondaryType=m[2],level=m[3],hp=m[4],atk=m[5],defense=m[6],spatk=m[7],spdef=m[8],speed=m[9],moves=m[10], ability=m[11],sprite=m[12],gender=m[15],tera=tera,shiny=shiny,maxiv=maxiv)
    types=p.primaryType
    if p.secondaryType!="???":
        types=f"{p.primaryType}/{p.secondaryType}"
    p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
    p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)    
    wild=discord.Embed(title=f"A wild pokémon has appeared!{extra}")
    if (tch<10 and tera not in (m[1],m[2])) or "Alpha" in p.nickname:
        wild.set_thumbnail(url=f"{turl}")
    wild.set_image(url=p.sprite)
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
            rarity text)""")
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
            "{m[14]}")""")
            dt.commit()
            db.commit()
            catch="caught"
            if ctx.author!=guess.author:
                catch="sniped"
            await guess.reply(f"{guess.author.display_name} {catch} a level {p.level} {p.nickname}!")
            break       
             
@bot.command(aliases=["pi"])
async def info(ctx,num=None):
    p,allmon=await pokonvert(ctx,num)
    if num==None:
        num=len(allmon)
    types=p.primaryType
    if p.secondaryType!="???":
        types=f"{p.primaryType}/{p.secondaryType}"
    p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
    p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)  
    infos=discord.Embed(title=f"Level {p.level} {p.nickname}", description=f"""**Types:** {types}\n**Tera-Type:** {p.tera}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {p.item}\n**HP:** {p.maxhp} - IV: {p.hpiv}/31 - EV: {p.hpev}\n**Attack:** {p.maxatk} - IV: {p.atkiv}/31 - EV: {p.atkev}\n**Defense:** {p.maxdef} - IV: {p.defiv}/31 - EV: {p.defev}\n**Sp. Atk:** {p.maxspatk} - IV: {p.spatkiv}/31 - EV: {p.spatkev}\n**Sp. Def:** {p.maxspdef} - IV: {p.spdefiv}/31 - EV: {p.spdefev}\n**Speed:** {p.maxspeed} - IV: {p.speediv}/31 - EV: {p.speedev}\n**Total IV %:** {p.totaliv}%\n**Total EV :** {p.totalev}/508""",color=0x00ff00)
    infos.set_author(name=ctx.author.display_name)
    infos.set_image(url=p.sprite)
    infos.set_thumbnail(url=ctx.author.avatar)
    infos.set_footer(text=f"ID: {ctx.author.id}\nDisplaying Pokémon: {num}/{len(allmon)}")
    await ctx.send(embed=infos)
@bot.command(aliases=["pp"])     
async def pokemons(ctx,num=1):
    db=sqlite3.connect(f"playerdata.db")
    c=db.cursor()  
    try:
        c.execute(f"Select * from '{ctx.author.id}'")
    except:
        pass
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
            n=10*(num-1)
            for i in list_of_lists[num-1]:
                n+=1
                name=i[1]
                ivp=round((i[3]+i[4]+i[5]+i[6]+i[7]+i[8])/1.86,2)
                if i[17]=="Yes":
                    name="Shiny "+i[1]
                x.add_field(name=f"#{n} {name}",value=f"**Ability:** {i[15]} || **IV:** {ivp}%")
            x.set_footer(text=f"Showing {num} out of {len(list_of_lists)} pages.")
            await ctx.send(embed=x)
    else:
        await ctx.send("Unfortunately you don't have any Pokémon. Please catch some Pokémon using `!spawn` command.")        
@bot.command(aliases=["rl"])            
async def release(ctx,num=1,force="No"):
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    try:
        c.execute(f"Select * from '{ctx.author.id}' where rowid={num}")
    except:
        pass
    r=c.fetchone()
    if force in ["y","yes"]:
       c.execute(f"delete from '{ctx.author.id}' where rowid={num}")
       db.commit()
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
                await ctx.send(f"{r[0]} was released!")
                break
                
async def pokonvert(ctx,num=None):
    if num!=None:
        num=int(num)
    dt=sqlite3.connect("pokemondata.db")
    db=sqlite3.connect("playerdata.db")
    cx=dt.cursor()
    c=db.cursor()
    c.execute(f"select * from '{ctx.author.id}'")
    allmon=c.fetchall()
    if num==None:
        num=len(allmon)
    if len(allmon)<num:
        await ctx.send("Invalid Pokémon.")
    if len(allmon)>=num:
        n=allmon[num-1]
        cx.execute(f"select * from 'wild' where name='{n[0]}' ")
        m=cx.fetchall()[0]
        p=Pokemon(name=m[0],nickname=n[1],primaryType=m[1],secondaryType=m[2],level=m[3],hp=m[4],atk=m[5],defense=m[6],spatk=m[7],spdef=m[8],speed=m[9],moves=n[22], ability=n[15],sprite=m[12],gender=n[19],tera=n[20],maxiv="Custom",item=n[18],shiny=n[17],nature=n[16],hpiv=n[3],atkiv=n[4],defiv=n[5],spatkiv=n[6],spdefiv=n[7],speediv=n[8],hpev=n[9],atkev=n[10],defev=n[11],spatkev=n[12],spdefev=n[13],speedev=n[14])
    return p,allmon
                   
keep_alive()
bot.run(token)       
    