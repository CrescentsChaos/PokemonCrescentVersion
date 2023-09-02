from misc import *
@bot.command(aliases=["td"])
async def trade(ctx,member:discord.Member):
    tr1="None"
    tr2="None"
    while (tr1=="None" and tr2=="None"):
        await ctx.send(f"{ctx.author.mention} what you wanna trade? (pokemon/money/free)")
        response=await bot.wait_for('message',check=lambda message:message.author==ctx.author)
        if response.content.lower() in ["p","poke","pokemon","pk"]:
            tr1="Pokemon"
        elif response.content.lower() in ["c","cash","money","dollar","mn"]:
            tr1="Money" 
        elif response.content.lower() in ["fr","free","gift"]:
            tr1="Free"                        
        elif response.content.lower() in ["cn","cancel","end","en"]:
            tr1="Cancel"            
        await ctx.send(f"{member.mention} what you wanna trade? (pokemon/money/free)")     
        res1=await bot.wait_for('message',check=lambda message:message.author==member)
        if res1.content.lower() in ["p","poke","pokemon","pk"]:
            tr2="Pokemon"
        elif res1.content.lower() in ["c","cash","money","dollar","mn"]:
            tr2="Money" 
        elif res1.content.lower() in ["fr","free","gift"]:
            tr2="Free"                        
        elif res1.content.lower() in ["cn","cancel","end","en"]:
            tr2="Cancel"       
    if "Cancel" in (tr1,tr2):
        await ctx.send("Trade cancelled.")
    elif tr1=="Money" and tr2=="Free":
        db=sqlite3.connect("playerdata.db")
        c=db.cursor()
        c.execute(f"select * from '{ctx.author.id}'")
        m=c.fetchone()
        money=m[0]
        while True:
            await ctx.send(f"{ctx.author.mention} how much money you wanna give?")
            response=await bot.wait_for('message',check=lambda message:message.author==ctx.author)
            try:
                if int(response.content)<=money:
                    new=int(response.content)
                    await addmoney(ctx,member,new)
                    await addmoney(ctx,ctx.author,-new)
                    break
            except:
                await ctx.send(f"{ctx.author.mention},you don't have enough money!")
                break
    elif tr2=="Money" and tr1=="Free":
        db=sqlite3.connect("playerdata.db")
        c=db.cursor()
        c.execute(f"select * from '{member.id}'")
        m=c.fetchone()
        money=m[0]
        while True:
            await ctx.send(f"{member.mention} how much money you wanna give?")
            response=await bot.wait_for('message',check=lambda message:message.author==member)
            try:
                if int(response.content)<=money:
                    new=int(response.content)
                    await addmoney(ctx,ctx.author,new)
                    await addmoney(ctx,member,-new)
                    break
            except:
                await ctx.send(f"{member.mention},you don't have enough money!")
                break                    
    elif tr1=="Pokemon" and tr2=="Free":
        await ctx.send(f"{ctx.author.mention} which pokemon you wanna trade for free?")
        while True:
            response=await bot.wait_for('message',check=lambda message:message.author==ctx.author)
            db=sqlite3.connect("owned.db")
            c=db.cursor()
            c.execute(f"select * from '{ctx.author.id}'")
            monlist=c.fetchall()
            if int(response.content)<=len(monlist):
                num=int(response.content)
                nm=await row(ctx,num,c)
                p,allmon=await pokonvert(ctx,ctx.author,num)
                types=await typeicon(p.primaryType)
                clr=await moncolor(p.tera)
                p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
                if p.secondaryType!="???":
                    types=f"{await typeicon(p.primaryType)}{await typeicon(p.secondaryType)}"
                infos=discord.Embed(title=f"{p.icon} {p.nickname} Lv.{p.level} will be traded to {member.mention}!",description=f"""**Types:** {types}{await teraicon(p.tera)}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {p.item}\n**Total IV %:** {p.totaliv}%""",color=clr)
                infos.set_image(url=p.sprite)
                await ctx.send(embed=infos)
                while True:
                    response=await bot.wait_for('message',check=lambda message:message.author==ctx.author)
                    if (response.content).lower() in ["yes","y","confirm","cm"]:
                        clk=datetime.datetime.now()
                        catchtime=clk.strftime("%Y-%m-%d %H:%M:%S")
                        if "<:traded:1127340280966828042>" not in p.nickname:
                            p.nickname=p.nickname+" <:traded:1127340280966828042>"
                        c.execute(f"""INSERT INTO "{member.id}" VALUES (
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
                    "{catchtime}")""")
                        db.commit()
                        c.execute(f"delete from '{ctx.author.id}' where rowid={nm}")
                        db.commit()
                        await ctx.send("Traded successfully.")   
                    else:
                        break
            else:              
                break          
    elif tr2=="Pokemon" and tr1=="Free":
        await ctx.send(f"{member.mention} which pokemon you wanna trade for free?")
        while True:
            response=await bot.wait_for('message',check=lambda message:message.author==member)
            db=sqlite3.connect("owned.db")
            c=db.cursor()
            c.execute(f"select * from '{member.id}'")
            monlist=c.fetchall()
            if int(response.content)<=len(monlist):
                num=int(response.content)
                nm=await row(ctx,num,c)
                p,allmon=await pokonvert(ctx,ctx.author,num)
                types=await typeicon(p.primaryType)
                clr=await moncolor(p.tera)
                p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
                if p.secondaryType!="???":
                    types=f"{await typeicon(p.primaryType)}{await typeicon(p.secondaryType)}"
                infos=discord.Embed(title=f"{p.icon} {p.nickname} Lv.{p.level} will be traded to {member.mention}!",description=f"""**Types:** {types}{await teraicon(p.tera)}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {p.item}\n**Total IV %:** {p.totaliv}%""",color=clr)
                infos.set_image(url=p.sprite)
                await ctx.send(embed=infos)
                while True:
                    response=await bot.wait_for('message',check=lambda message:message.author==member)
                    if (response.content).lower() in ["yes","y","confirm","cm"]:
                        clk=datetime.datetime.now()
                        catchtime=clk.strftime("%Y-%m-%d %H:%M:%S")
                        if "<:traded:1127340280966828042>" not in p.nickname:
                            p.nickname=p.nickname+" <:traded:1127340280966828042>"
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
                    "Traded",
                    "{catchtime}")""")
                        db.commit()
                        c.execute(f"delete from '{member.id}' where rowid={nm}")
                        db.commit()
                        await ctx.send("Traded successfully.")   
                    else:
                        break               
            else:              
                break                          
    elif tr2=="Money" and tr1=="Pokemon":
        db=sqlite3.connect("playerdata.db")
        c=db.cursor()
        c.execute(f"select * from '{member.id}'")
        m=c.fetchone()
        money=m[0]
        while True:
            await ctx.send(f"{member.mention} how much money you wanna give?")
            response=await bot.wait_for('message',check=lambda message:message.author==member)
            if int(response.content)<=money:
                new=int(response.content)
                break
            else:
                break
        await ctx.send(f"{ctx.author.mention} which pokemon you wanna trade for {new}<:pokecoin:1134595078892044369>?")
        while True:
            response=await bot.wait_for('message',check=lambda message:message.author==ctx.author)
            db=sqlite3.connect("owned.db")
            c=db.cursor()
            c.execute(f"select * from '{ctx.author.id}'")
            monlist=c.fetchall()
            if int(response.content)<=len(monlist):
                num=int(response.content)
                nm=await row(ctx,num,c)
                p,allmon=await pokonvert(ctx,ctx.author,num)
                types=await typeicon(p.primaryType)
                clr=await moncolor(p.tera)
                p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
                if p.secondaryType!="???":
                    types=f"{await typeicon(p.primaryType)}{await typeicon(p.secondaryType)}"
                infos=discord.Embed(title=f"{p.icon} {p.nickname} Lv.{p.level} will be traded to {member.mention} for {new}<:pokecoin:1134595078892044369>. {ctx.author.mention},Do you confirm?",description=f"""**Types:** {types}{await teraicon(p.tera)}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {p.item}\n**Total IV %:** {p.totaliv}%""",color=clr)
                infos.set_image(url=p.sprite)
                await ctx.send(embed=infos)   
                p1=""    
                p2=""
                while True:
                    response=await bot.wait_for('message',check=lambda message:message.author==ctx.author)
                    if (response.content).lower() in ["yes","y","confirm","cm"]:
                        p1="Confirmed"
                        break
                    else:
                        break
                if p1=="Confirmed":
                    while True:
                        await ctx.send(f"{member.mention} do you want to confirm the trade?")
                        response=await bot.wait_for('message',check=lambda message:message.author==member)
                        if (response.content).lower() in ["yes","y","confirm","cm"]:
                            p2="Confirmed"
                            clk=datetime.datetime.now()
                            catchtime=clk.strftime("%Y-%m-%d %H:%M:%S")
                            if "<:traded:1127340280966828042>" not in p.nickname:
                                p.nickname=p.nickname+" <:traded:1127340280966828042>"
                            c.execute(f"""INSERT INTO "{member.id}" VALUES (
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
                    "{catchtime}")""")
                            db.commit()
                            c.execute(f"delete from '{ctx.author.id}' where rowid={nm}")
                            db.commit()
                            await addmoney(ctx,ctx.author,new)
                            await addmoney(ctx,member,-new)
                            await ctx.send("Traded successfully.")
                            break
                        else:
                            break
    else:
        await ctx.send("Trade cancelled.")
    
@bot.command(aliases=["bt"])
async def battle(ctx,member:discord.Member):
    await ctx.send(f"{member.mention} do you want to battle?")
    while True:
        response=await bot.wait_for('message',check=lambda message:message.author==member)
        if response.content.lower() in ["y","yes"]:
            await ctx.send(f"Battle starting between {ctx.author.display_name} and {member.display_name}!")
            await multiplayer(ctx,ctx.author,member)
            break
        else:
            break
@bot.command(aliases=["gm"])
async def game(ctx,num=0):
    await multiplayer(ctx,ctx.author,num)
@bot.command()
async def view(ctx,num=1):
    team=await teamconvert(ctx,ctx.author,ctx.author.id)
    p=team[num-1]
    types=p.primaryType
    if p.secondaryType!="???":
        types=f"{p.primaryType}/{p.secondaryType}"
    p.totaliv=round(((p.hpiv+p.atkiv+p.defiv+p.spatkiv+p.spdefiv+p.speediv)/186)*100,2)
    p.totalev=(p.hpev+p.atkev+p.defev+p.spatkev+p.spdefev+p.speedev)  
    infos=discord.Embed(title=f"#{num} {p.nickname} Lv.{p.level}",description=f"""**Types:** {types}\n**Tera-Type:** {p.tera}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {p.item}\n**HP:** {p.hp} - IV: {p.hpiv}/31 - EV: {p.hpev}\n**Attack:** {p.maxatk} - IV: {p.atkiv}/31 - EV: {p.atkev}\n**Defense:** {p.maxdef} - IV: {p.defiv}/31 - EV: {p.defev}\n**Sp. Atk:** {p.maxspatk} - IV: {p.spatkiv}/31 - EV: {p.spatkev}\n**Sp. Def:** {p.maxspdef} - IV: {p.spdefiv}/31 - EV: {p.spdefev}\n**Speed:** {p.maxspeed} - IV: {p.speediv}/31 - EV: {p.speedev}\n**Total IV %:** {p.totaliv}%\n**Total EV :** {p.totalev}/508""")
    infos.set_thumbnail(url=ctx.author.avatar)
    infos.set_image(url=p.sprite)
    await ctx.author.send(embed=infos)
@bot.command(aliases=["hp"])   
async def hpbar(ctx,hp=100,maxhp=100):
    em=discord.Embed(title="Pikachu",description="<:HP:1107296292243255356>"+"<:GREEN:1107296335780139113>"*int((hp/maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((hp/maxhp)*10))+"<:END:1107296362988580907>") 
    await ctx.send(embed=em)
@bot.command(aliases=["afv"])   
async def addfav(ctx,num):
    new=int(num)
    dt=sqlite3.connect("owned.db")
    ct=dt.cursor()
    num=await row(ctx,new,ct)
    ct.execute(f"select * from '{ctx.author.id}' where rowid={num}")
    v=ct.fetchone()
    if "<:favorite:1144122202942357534>" not in v[1]:
        ct.execute(f"""update '{ctx.author.id}' set nickname="{v[1]+' <:favorite:1144122202942357534>'}" where rowid={num}""")
        dt.commit()
        await ctx.send("Favorite added.")
@bot.command(aliases=["tm"])   
async def team(ctx,a=1,b=2,c=3,d=4,e=5,f=6):
    db=sqlite3.connect("playerdata.db")
    cx=db.cursor()
    dt=sqlite3.connect("owned.db")
    ct=dt.cursor()
    tm=[a,b,c,d,e,f] 
    new=[]
    for i in tm:
        n=await row(ctx,i,ct)
        new.append(n)
    mx=max(new)
    team=f"{new}"
    if len(tm)==6:
        cx.execute(f"""update '{ctx.author.id}' set squad="{new}" """)
        db.commit()
        await ctx.send("Team updated successful!")
@bot.command(aliases=["pr"])       
async def profile(ctx):
    db=sqlite3.connect("playerdata.db")
    dt=sqlite3.connect("owned.db")
    c=db.cursor()
    ct=dt.cursor()
    c.execute(f"select * from '{ctx.author.id}'")
    ct.execute(f"select * from '{ctx.author.id}'")
    det=c.fetchone()
    allmon=ct.fetchall()
    ct.execute(f"select * from '{ctx.author.id}' where shiny='Yes'")
    shinies=ct.fetchall()
    dy=(datetime.datetime.today()-datetime.datetime.strptime(det[3],"%Y-%m-%d %H:%M:%S")).days
    ttl=""
    if ctx.author.id==1084473178400755772:
        ttl="<:owner:1133682173413699714>"
    data=discord.Embed(title=f"{ctx.author.display_name}{ttl}'s Profile:",description=f"**<:pokecoin:1134595078892044369> Balance:** {await numberify(det[0])}\n**<:ball:1127196564948009052> Pokémons Caught:** {len(allmon)}\n**<:shiny:1127157664665837598> Shinies Caught:** {len(shinies)}\n**<:currentwin:1140763688668766249> Winstreak:** {det[4]}\n**<:winstreak:1140763720683880478> Highest Winstreak:** {det[5]}")
    data.set_footer(text=f"Creation Date: {det[3]} ({dy} days ago)")
    sq=eval(det[1])
    try:
        team=await teamconvert(ctx,ctx.author,ctx.author.id)
        ll=0
        for i in team:
            ll+=1
            data.add_field(name=f"#{await findnum(ctx,sq[ll-1])} {i.icon} {i.nickname} {await teraicon(i.tera)}",value=f"**Ability:** {i.ability}\n**Item:** {await itemicon(i.item)} {i.item}")
    except:
        data.add_field(name="Current Team:",value="Not available")
    data.set_thumbnail(url=ctx.author.avatar)
    await ctx.send(embed=data)
             
     
async def teamconvert(ctx,p,id):
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"select squad from '{id}'")
    lt=c.fetchone()
    lt=eval(lt[0])
    team=[]
    for i in lt:
        m=await pokonvert(ctx,p,i)
        m=m[0]
        team.append(m)
    return team
    
async def multiplayer(ctx,p1,p2):
    field = Field()
    p1team = await teamconvert(ctx,p1,p1.id)
    if isinstance(p2,int):
        tr2 = await gameteam(ctx,p2)
    else:
        p2team = await teamconvert(ctx,p2,p2.id)
        tr2 = Trainer(p2.display_name,p2team,"Earth",sprite=p2.avatar,member=p2)    
    tr1 = Trainer(p1.display_name,p1team,"Earth",sprite=p1.avatar,member=p1)   
    intro = discord.Embed(title=f"{tr1.name} vs {tr2.name}")
    intro.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1103853991760248924/VS.png")
    if tr2.ai==False:
        intro.add_field(name="Task:",value="Choose your lead pokémon! Check your DM!")
    intro.set_image(url=tr2.sprite)
    intro.set_footer(text=f"Location: {field.location} | Weather: {field.weather} | Terrain: {field.terrain}")
    await ctx.send(embed=intro)
    p2team=tr2.pokemons
    p1leadoptions=""
    p2leadoptions=""
    n1=0
    n2=0
    for i in p1team:
        n1+=1
        p1leadoptions+=f"#{n1} {i.icon} {i.name}\n"
    for i in p2team:
        n2+=1
        p2leadoptions+=f"#{n2} {i.icon} {i.name}\n"
    p1leadem=discord.Embed(title="Choose your lead pokémon!",description=p1leadoptions) 
    p1leadem.set_footer(text="Enter the number until you get the confirmation messaage!")
    if tr2.ai==False:
        p2leadem=discord.Embed(title="Choose your lead pokémon!",description=p2leadoptions)
        p2leadem.set_footer(text="Enter the number until you get the confirmation messaage!")
    x,y = None,None

    def xcheck(message):
        return isinstance(message.channel,discord.DMChannel) and message.author == p1

    if tr2.ai == False:
        def ycheck(message):
            return isinstance(message.channel,discord.DMChannel) and message.author == p2

    while True:
        if x == None and tr2.ai == True:
            await ctx.send(embed=p1leadem) 
            while True:
                xnum = await bot.wait_for('message')
                if xnum.author == ctx.author:
                    x = tr1.pokemons[int(xnum.content)-1]
                    break
        if x == None and tr2.ai == False:
            await p2.send(f"{tr1.name} is choosing their lead pokémon. Please wait patiently!")
            await p1.send(embed=p1leadem) 
            xnum = await bot.wait_for('message',check=xcheck)
            x = tr1.pokemons[int(xnum.content)-1]
            if x != None:
                await p1.send(f"You chose {x.name} as your lead pokémon.")

        if x != None and tr2.ai == True:
            y = random.choice(tr2.pokemons)      
        if x != None and tr2.ai == False:
            await p1.send(f"{tr2.name} is choosing their lead pokémon. Please wait patiently!")
            await p2.send(embed=p2leadem)
            ynum = await bot.wait_for('message',check=ycheck)   
            y = tr2.pokemons[int(ynum.content)-1]   
            if x != None:
                await p2.send(f"You chose {y.name} as your lead pokémon. Now go back to the server!")

        if None not in (x,y):
            tr1.party=await partyup(tr1,x)
            tr2.party=await partyup(tr2,y)  
            break       
    turn=0        
    if x.speed>=y.speed:
        await entryeff(ctx,x,y,tr1,tr2,field,turn)
        await entryeff(ctx,y,x,tr2,tr1,field,turn)        
    if y.speed>x.speed:
        await entryeff(ctx,y,x,tr2,tr1,field,turn)      
        await entryeff(ctx,x,y,tr1,tr2,field,turn) 
    lead1=discord.Embed(title=f"{tr1.name}: Go,{x.nickname}!",description=f"{tr1.name} sents out **{x.name}**!")
    lead1.set_image(url=x.sprite)   
    lead1.set_thumbnail(url=tr1.sprite)
    lead2=discord.Embed(title=f"{tr2.name}: Go,{y.nickname}!",description=f"{tr2.name} sents out **{y.name}**!")
    lead2.set_image(url=y.sprite)
    lead2.set_thumbnail(url=tr2.sprite)     
    if x.speed>=y.speed:
        await ctx.send(embed=lead1)
        await ctx.send(embed=lead2)
    if y.speed>x.speed:
        await ctx.send(embed=lead2)
        await ctx.send(embed=lead1)    
    while True:
        turn+=1
        bg = int("FFFFFF",16)
        color_map = {
    "Normal": "E5E7E2",
    "Clear": "E5E7E2",
    "None": "E5E7E2",
    "Cloudy": "E5E7E2",
    "Misty": "FEB8B7",
    "Psychic": "BD61E6",
    "Electric": "D5CD73",
    "Grassy": "9CF7BD",
    "Strong Winds": "90FFF0",
    "Extreme Sunlight": "FF5E20",
    "Heavy Rain": "0790FF",
    "Hail": "7EC8FF",
    "Snowstorm": "CCECFF",
    "Rainy": "32C7FF",
    "Sunny": "FAFF6C",
    "Sandstorm": "CCAF5E"
}
        if field.weather in color_map:
            bg = int(color_map[field.weather],16)
        if field.terrain in color_map and field.terrain!="Normal":
            bg = int(color_map[field.terrain],16)
        wt="Clear"
        ts="Normal"
        trm=""
        if field.weather=="Sunny":
            wt=f"<:sunny:1141089317150793798> Sunny ({field.sunendturn-turn+1} turns left)"
        elif field.weather=="Rainy":
            wt=f"<:rainy:1141087852436922378> Rainy ({field.rainendturn-turn+1} turns left)"
        elif field.weather=="Sandstorm":
            wt=f"<:sandstorm:1141088700047048744> Sandstorm ({field.sandendturn-turn+1} turns left)"
        elif field.weather=="Snowstorm":
            wt=f"<:snowstorm:1141089242731266180> Snowstorm ({field.snowendturn-turn+1} turns left)"
        elif field.weather=="Hail":
            wt=f"<:hail:1141090300501176511> Hail ({field.hailendturn-turn+1} turns left)"   
        elif field.weather=="Heavy Rain":
            wt=f"<:heavyrain:1141093451765665823> Heavy Rain"               
        elif field.weather=="Extreme Sunlight":
            wt=f"<:extremesunlight:1141093481276776490> Extreme Sunlight"            
        elif field.weather=="Strong Winds":
            wt=f"<:strongwind:1141093937273114704> Strong Winds"
        elif field.weather in ["Clear","Cloudy","Normal"]:
            wt=f"<:clear:1141211018974994462> Clear"      
        if field.terrain=="Grassy":
            ts=f"<:grassy:1141090982788603985> Grassy ({field.grassendturn-turn+1} turns left)"
        elif field.terrain=="Electric":
            ts=f"<:electric:1141092625038970922> Electric ({field.eleendturn-turn+1} turns left)"
        elif field.terrain=="Psychic":
            ts=f"<:psychic:1141091324376911923> Psychic ({field.psyendturn-turn+1} turns left)"
        elif field.terrain=="Misty":
            ts=f"<:misty:1141091967162384404> Misty ({field.misendturn-turn+1} turns left)"
        elif field.terrain in ["Clear","Cloudy","Normal"]:
            ts=f"<:clear:1141211018974994462> Normal"   
        if field.trickroom==True:
            trm=f"**Dimension:** <:trickroom:1142045158200840313> Trick Room ({field.troomendturn-turn+1} turns left)"
        turnem=discord.Embed(title=f"Turn: {turn}",description=f"**Location:** {field.location}\n**Weather:** {wt}\n**Terrain:** {ts}\n{trm}",color=bg)
        await ctx.send(embed=turnem)
        if x.protect==True and x.use in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct","Silk Trap"]:
            x.protect = "Pending"
        elif x.protect==True and x.use=="Max Guard":
            x.protect=False
        if y.protect==True and y.use in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct","Silk Trap"]:
            y.protect = "Pending"
        elif y.protect==True and y.use=="Max Guard":
            y.protect=False
        action1 = None
        action2 = None
        await prebuff(ctx,x,y,tr1,tr2,turn,field)
        await prebuff(ctx,y,x,tr2,tr1,turn,field)
        if tr2.ai:
            await score(ctx,y,x,tr2,tr1,turn,bg)
            await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
        elif tr2.ai is False:
            await score(ctx,x,y,tr1,tr2,turn,bg)
            await score(ctx,y,x,tr2,tr1,turn,bg)
            await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
            await advscore(ctx,y,x,tr2,tr1,turn,field,bg)
        while action1 is None or action2 is None:
            if action1 not in [1,2]:
                action1 = await action(bot,ctx,tr1,tr2,x,y)
            if action2 not in [1,2]:
                action2 = await action(bot,ctx,tr2,tr1,y,x)
        if action1 == 3 and action2 != 3:
            await winner(ctx,tr2,tr1)
            break
        if action2 == 3 and action1 != 3:
            await winner(ctx,tr1,tr2)
            break
        em1 = ""
        em2 = ""
        if tr2.ai == False:
            await tr1.member.send("Please wait...")
            await tr2.member.send("Please wait...")
        if action1 in [7,8]:
            if action1 == 8:
                x,em1 = await maxtrans(ctx,x,tr1,turn)
            action1 = 1

        elif action1 == 6:
            x,em1 = await megatrans(ctx,x,y,tr1,tr2,field,turn)
            action1 = 1
        elif action1==5:
            x.zuse=True
            action1=1
        elif action1 == 9:
            x,em1 = await teratrans(ctx,x,tr1)
            action1 = 1

        if action2 in [7,8]:
            if action2 == 8:
                y,em2 = await maxtrans(ctx,y,tr2,turn)
            action2 = 1

        elif action2 == 6:
            y,em2 = await megatrans(ctx,y,x,tr2,tr1,field,turn)
            action2 = 1
        elif action2==5:
            y.zuse=True
            action2=1
        elif action2 == 9:
            y,em2 = await teratrans(ctx,y,tr2)
            action2 = 1

        if action1 == 2 and len(tr1.pokemons) == 1:
            action1 = 1

        if action2 == 2 and len(tr2.pokemons) == 1:
            action2 = 1

        if em1:
            await ctx.send(embed=em1)
        if em2:
            await ctx.send(embed=em2)

        if action1==1 and action2==1:
            if tr2.ai==True:
                await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
            if tr2.ai==False:
                await score(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
                await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
                await advscore(ctx,y,x,tr2,tr1,turn,field,bg)
            choice1="None"
            choice2="None"
            choice1=await fchoice(ctx,bot,x,y,tr1,tr2,field)
            if choice1!="None" and tr2.ai==False:
                await tr1.member.send(f"{x.nickname} will use {choice1}!")
            choice2=await fchoice(ctx,bot,y,x,tr2,tr1,field)
            if choice2!="None" and tr2.ai==False:
                await tr2.member.send(f"{y.nickname} will use {choice2}!")
            xPriority=0
            yPriority=0
            if y.ability=="Quick Draw":
                yPriority=random.randint(1,100)
                if yPriority<20:
                    y.priority=True
            if x.ability=="Quick Draw":
                xPriority=random.randint(1,100)
                if xPriority<20:
                    x.priority=True
            if x.item=="Quick Claw":
                xPriority=random.randint(1,100)
                if xPriority<18:
                    x.priority=True
            if y.item=="Quick Claw":
                yPriority=random.randint(1,100)
                if yPriority<18:
                    y.priority=True
            if y.item=="Quick Claw" and y.ability=="Quick Draw":
                yPriority=random.randint(1,100)
                if yPriority<36:
                    y.priority=True
            if x.item=="Quick Claw" and x.ability=="Quick Draw":
                xPriority=random.randint(1,100)
                if xPriority<36:
                    x.priority=True
            if (
    choice1 in typemoves.prioritymove
    or x.priority==True
    or (x.ability == "Prankster" and choice1 in typemoves.statusmove and "Dark" not in (y.primaryType,y.secondaryType))
    or (choice1 in typemoves.firemoves and x.ability == "Blazing Soul")
    or (choice1 in typemoves.flyingmoves and x.ability == "Gale Wings")
    or (field.terrain == "Grassy" and choice1 == "Grassy Glide")
    or (x.ability == "Triage" and choice1 in typemoves.healingmoves)
    or choice2 in typemoves.negprioritymove
    or (choice2 in typemoves.statusmove and y.ability == "Mycelium Might")
    or y.item == "Lagging Tail"
):
                if x.priority==True and x.item=="Quick Claw":
                    qc=discord.Embed(title=f"{x.nickname}'s Quick Claw!",description=f"{x.nickname} can act faster than normal,thanks to its Quick Claw")
                    await ctx.send(embed=qc)
                await weather(ctx,field,bg)   
                x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
                await prebuff(ctx,x,y,tr1,tr2,turn,field)
                await prebuff(ctx,y,x,tr2,tr1,turn,field)
                if x.hp<=0:
                    x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        await winner(ctx,tr2,tr1)
                        break
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break 
                elif y.hp>0:                     
                    y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2,choice1,field,turn)
                    await effects (ctx,x,y,tr1,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    await prebuff(ctx,x,y,tr1,tr2,turn,field)
                    await prebuff(ctx,y,x,tr2,tr1,turn,field)   
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break 
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    await effects(ctx,x,y,tr1,turn)
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break
                x.priority=False       
            elif (
    choice2 in typemoves.prioritymove
    or y.priority==True
    or (y.ability == "Prankster" and choice2 in typemoves.statusmove and "Dark" not in (x.primaryType,x.secondaryType))
    or (choice2 in typemoves.firemoves and y.ability == "Blazing Soul")
    or (choice2 in typemoves.flyingmoves and y.ability == "Gale Wings")
    or (field.terrain == "Grassy" and choice2 == "Grassy Glide")
    or (y.ability == "Triage" and choice2 in typemoves.healingmoves)
    or choice1 in typemoves.negprioritymove
    or (choice1 in typemoves.statusmove and x.ability == "Mycelium Might")
    or x.item == "Lagging Tail"
):
                if y.priority==True and y.item=="Quick Claw":
                    qc=discord.Embed(title=f"{y.nickname}'s Quick Claw!",description=f"{y.nickname} can act faster than normal,thanks to its Quick Claw")
                    await ctx.send(embed=qc)
                await weather(ctx,field,bg)   
                y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2,choice1,field,turn)
                await prebuff(ctx,y,x,tr2,tr1,turn,field)
                await prebuff(ctx,x,y,tr1,tr2,turn,field)
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break 
                if x.hp<=0:
                    x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        await winner(ctx,tr2,tr1)
                        break      
                elif x.hp>0:                     
                    x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    await effects (ctx,x,y,tr1,field,turn)
                    await prebuff(ctx,y,x,tr2,tr1,turn,field)  
                    await prebuff(ctx,x,y,tr1,tr2,turn,field)
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break 
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break 
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break
                    if len(tr1.pokemons)==0:
                        await winner(ctx,tr2,tr1)
                        break
                y.priority=False        
                
            elif x.speed>=y.speed and field.trickroom==False:
                await weather(ctx,field,bg)        
                x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)                         
                await prebuff(ctx,x,y,tr1,tr2,turn,field)
                await prebuff(ctx,y,x,tr2,tr1,turn,field)
                if x.hp<=0:
                    x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        await winner(ctx,tr2,tr1)
                        break       
                elif y.hp>0:                    
                    y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2,choice1,field,turn)
                    await effects (ctx,x,y,tr1,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    await prebuff(ctx,x,y,tr1,tr2,turn,field)
                    await prebuff(ctx,y,x,tr2,tr1,turn,field)
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break       
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    await effects (ctx,x,y,tr1,field,turn)
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break      
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break   
            elif x.speed<y.speed and field.trickroom==True:
                await weather(ctx,field,bg)
                x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
                await prebuff(ctx,x,y,tr1,tr2,turn,field)
                await prebuff(ctx,y,x,tr2,tr1,turn,field)
                if x.hp<=0:
                    x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                    if len(tr1.pokemons)==0:
                        await winner(ctx,tr2,tr1)
                        break   
                elif y.hp>0:                     
                    y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2,choice1,field,turn)
                    await effects (ctx,x,y,tr1,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    await prebuff(ctx,x,y,tr1,tr2,turn,field)
                    await prebuff(ctx,y,x,tr2,tr1,turn,field)
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break   
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    await effects (ctx,x,y,tr1,field,turn)
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break   
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break
                        
            elif y.speed>x.speed and field.trickroom==False:
                await weather(ctx,field,bg)
                y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2,choice1,field,turn)
                await prebuff(ctx,x,y,tr1,tr2,turn,field)
                await prebuff(ctx,y,x,tr2,tr1,turn,field)
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break
                elif x.hp>0:                    
                    x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    await effects (ctx,x,y,tr1,field,turn)
                    await prebuff(ctx,x,y,tr1,tr2,turn,field)
                    await prebuff(ctx,y,x,tr2,tr1,turn,field)
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break   
                if x.hp<=0:
                    x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break
                    if len(tr1.pokemons)==0:
                        await winner(ctx,tr2,tr1)
                        break   

            elif y.speed<=x.speed and field.trickroom==True:
                await weather(ctx,field,bg)
                y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2,choice1,field,turn)
                await prebuff(ctx,x,y,tr1,tr2,turn,field)
                await prebuff(ctx,y,x,tr2,tr1,turn,field)
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break
                elif x.hp>0:                    
                    x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    await effects (ctx,x,y,tr1,field,turn)
                    await prebuff(ctx,x,y,tr1,tr2,turn,field)
                    await prebuff(ctx,y,x,tr2,tr1,turn,field)
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break
                    if x.hp<=0:
                        x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                        if len(tr1.pokemons)==0:
                            await winner(ctx,tr2,tr1)
                            break
                if x.hp<=0:
                    x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                    await effects(ctx,y,x,tr2,field,turn)
                    if y.hp<=0:
                        y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                        if len(tr2.pokemons)==0:
                            await winner(ctx,tr1,tr2)
                            break
                    if len(tr1.pokemons)==0:
                        await winner(ctx,tr2,tr1)
                        break
        elif action1==2 and action2==1:
            choice1="None"
            if tr2.ai==True:
                await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
            if tr2.ai==False:
                await score(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
                await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
                await advscore(ctx,y,x,tr2,tr1,turn,field,bg)
            choice2=await fchoice(ctx,bot,y,x,tr2,tr1,field)
            await weather(ctx,field,bg)
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
            y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2,choice1,field,turn)
            await effects (ctx,x,y,tr1,field,turn)
            await effects(ctx,y,x,tr2,field,turn)
            if y.hp<=0:
                y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    await winner(ctx,tr1,tr2)
                    break
            if x.hp<=0:
                x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                   await winner(ctx,tr2,tr1)
                   break
            
#tr1 ATTACKS AND tr2 SWITCHES                
        elif action1==1 and action2==2:
            choice2="None"
            if tr2.ai==True:
                await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
            if tr2.ai==False:
                await score(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
                await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
                await advscore(ctx,y,x,tr2,tr1,turn,field,bg)
            choice1=await fchoice(ctx,bot,x,y,tr1,tr2,field)
            await weather(ctx,field,bg)
            y=await switch(ctx,bot,y,x,tr2,tr1,field,turn)
            x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
            if x.hp<=0:
                x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                   await winner(ctx,tr2,tr1)
                   break
            await effects (ctx,x,y,tr1,field,turn)
            await effects(ctx,y,x,tr2,field,turn)
            await prebuff(ctx,x,y,tr1,tr2,turn,field)
            await prebuff(ctx,y,x,tr2,tr1,turn,field)
            if x.hp<=0:
                x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                   await winner(ctx,tr2,tr1)
                   break
            if y.hp<=0:
                y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    await winner(ctx,tr1,tr2)
                    break
            
#IF BOTH SWITCHES                
        elif action1==2 and action2==2:
            if tr2.ai==True:
                await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
            if tr2.ai==False:
                await score(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
                await advscore(ctx,x,y,tr1,tr2,turn,field,bg)
                await advscore(ctx,y,x,tr2,tr1,turn,field,bg)
            await weather(ctx,field,bg)
            if x.speed>=y.speed:
                x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)  
                y=await switch(ctx,bot,y,x,tr2,tr1,field,turn)
            if y.speed>x.speed:
                y=await switch(ctx,bot,y,x,tr2,tr1,field,turn)
                x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)  
            await effects(ctx,y,x,tr2,field,turn)
            if y.hp<=0:
                y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    await winner(ctx,tr1,tr2)
                    break
            await effects (ctx,x,y,tr1,field,turn)          
            if x.hp<=0:
                x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                   await winner(ctx,tr2,tr1)
                   break            
keep_alive()
bot.run(token)    
