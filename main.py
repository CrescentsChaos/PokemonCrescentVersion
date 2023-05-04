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
    dx=sqlite3.connect("playerdata.db")
    ct=dx.cursor()
    ct.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{ctx.author.id}' ")
    if ct.fetchone():
        db=sqlite3.connect("pokemondata.db")
        dt=sqlite3.connect("owned.db")
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
                rarity text,
                code integer)""")
                hh=cx.fetchall()
                code=len(hh)+1
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
                "{code}")""")
                dt.commit()
                db.commit()
                catch="caught"
                if ctx.author!=guess.author:
                    catch="sniped"
                await guess.reply(f"{guess.author.display_name} {catch} a level {p.level} {p.nickname}!")
                break       
    else:
        await ctx.send("You don't have an account. Type `!start` to create an account.")     
        
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
        Squad text
        )""")
        ct.execute(f"""INSERT INTO "{ctx.author.id}" VALUES (
        "0",
        "0,0,0,0,0,0")""")
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
            c.execute(f"Select * from 'wild' where name='{nam}'")
            m=c.fetchone()
            if "!" in guess.content:
                break
            elif len(m)!=0:
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
                code integer)""")
                hh=cx.fetchall()
                code=len(hh)+1
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
                "{code}")""")
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
    p,allmon=await pokonvert(ctx,num)
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
        infos.set_footer(text=f"ID: {ctx.author.id}\nDisplaying Pokémon: {num}/{len(allmon)}")
        await ctx.send(embed=infos)
    else:
        await ctx.send("Unfortunately you don't have any Pokémon. Please catch some Pokémon using `!spawn` command.")         
@bot.command(aliases=["pp"])     
async def pokemons(ctx,num=1,name="None"):
    db=sqlite3.connect(f"owned.db")
    c=db.cursor()  
    if name=="None":
        c.execute(f"Select * from '{ctx.author.id}'")
    if name!="None":
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
                if i[17]=="Yes":
                    name="Shiny "+i[1]
                x.add_field(name=f"#{k} {name}",value=f"**Gender:** {i[19]} | **Ability:** {i[15]} | **IV:** {ivp}%")
            x.set_footer(text=f"Showing {num} out of {len(list_of_lists)} pages.")
            await ctx.send(embed=x)
    else:
        await ctx.send("Unfortunately you don't have any Pokémon. Please catch some Pokémon using `!spawn` command.")        
@bot.command(aliases=["rl"])            
async def release(ctx,num=1,force="No"):
    db=sqlite3.connect("owned.db")
    c=db.cursor()
    c.execute(f"Select *,rowid from '{ctx.author.id}'")
    r=c.fetchall()
    num=r[num-1][25]
    if force in ["y","yes"]:
       c.execute(f"delete from '{ctx.author.id}' where rowid={num}")
       db.commit()
       await ctx.send(f"{r[num-1][0]} was released!")
    elif force=="No":
        await ctx.send(f"Do you want to release {r[0][0]}?")
        while True:
            guess = await bot.wait_for('message')
            if "!" in guess.content:
                break
            elif guess.content.lower() in ["n","no"] and guess.author==ctx.author:
                await ctx.send(f"{r[0][0]} was't released!")
                break
            elif guess.content.lower() in ["y","yes"]and guess.author==ctx.author:
                c.execute(f"delete from '{ctx.author.id}' where rowid={num}")
                db.commit()
                await ctx.send(f"{r[0][0]} was released!")
                break
                
@bot.command(aliases=["mv"])
async def moves(ctx,num=1):
    dt=sqlite3.connect("pokemondata.db")
    db=sqlite3.connect("owned.db")
    cx=dt.cursor()
    c=db.cursor()           
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
async def evtrain(ctx,num,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0):
    evlist=[hpev,atkev,defev,spatkev,spdefev,speedev]
    total=hpev+atkev+defev+spatkev+spdefev+speedev
    if max(evlist)<=252 and len(evlist)==6 and total<=508:
        db=sqlite3.connect("owned.db")
        c=db.cursor()
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
    show=discord.Embed(title=f"{item[0]}", description=f"Price: {item[1]} ¥")
    show.set_thumbnail(url=item[2])
    show.set_footer(text="Use `!buy 'item name' to buy the item.")
    await ctx.send(embed=show)
    
@bot.command(aliases=["br"])    
async def breed(ctx,mon1,mon2):
    num1=mon1
    num2=mon2
    mon1=await pokonvert(ctx,mon1)
    mon2=await pokonvert(ctx,mon2)
    mon1=mon1[0]
    mon2=mon2[0]
    if mon1.gender!=mon2.gender and "Genderless" not in (mon1.gender,mon2.gender) and mon1.name in mon2.name:
        dt=sqlite3.connect("pokemondata.db")
        db=sqlite3.connect("owned.db")
        ct=dt.cursor()
        c=db.cursor()
        name=""
        if mon1.gender=="Female":
            name=mon1.name
        if mon2.gender=="Female":
            name=mon2.name
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
                num1=r[int(num1)-1][24]
                num2=r[int(num2)-1][24]
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
                await ctx.send("Breeding successful!")
                break
    else:
        await ctx.send(f" You can't breed a {mon1.gender} {mon1.name} with a {mon2.gender} {mon2.name}!")
    
async def pokonvert(ctx,num=None):
    if num!=None:
        num=int(num)
    dt=sqlite3.connect("pokemondata.db")
    db=sqlite3.connect("owned.db")
    cx=dt.cursor()
    c=db.cursor()
    allmon=[]
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
    