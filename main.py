from misc import *

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
    infos=discord.Embed(title=f"#{num} {p.nickname} Lv.{p.level}", description=f"""**Types:** {types}\n**Tera-Type:** {p.tera}\n**Ability:** {p.ability}\n**Nature:** {p.nature}\n**Gender:** {p.gender}\n**Held Item:** {p.item}\n**HP:** {p.hp} - IV: {p.hpiv}/31 - EV: {p.hpev}\n**Attack:** {p.maxatk} - IV: {p.atkiv}/31 - EV: {p.atkev}\n**Defense:** {p.maxdef} - IV: {p.defiv}/31 - EV: {p.defev}\n**Sp. Atk:** {p.maxspatk} - IV: {p.spatkiv}/31 - EV: {p.spatkev}\n**Sp. Def:** {p.maxspdef} - IV: {p.spdefiv}/31 - EV: {p.spdefev}\n**Speed:** {p.maxspeed} - IV: {p.speediv}/31 - EV: {p.speedev}\n**Total IV %:** {p.totaliv}%\n**Total EV :** {p.totalev}/508""")
    infos.set_thumbnail(url=ctx.author.avatar)
    infos.set_image(url=p.sprite)
    await ctx.author.send(embed=infos)
@bot.command(aliases=["hp"])   
async def hpbar(ctx,hp=100,maxhp=100):
    em=discord.Embed(title="Pikachu",description="<:HP:1107296292243255356>"+"<:GREEN:1107296335780139113>"*int((hp/maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((hp/maxhp)*10))+"<:END:1107296362988580907>") 
    await ctx.send(embed=em)
@bot.command(aliases=["tm"])   
async def team(ctx,a=1,b=2,c=3,d=4,e=5,f=6):
    tm=[a,b,c,d,e,f] 
    mx=max(tm)
    team=f"{tm}"
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    dt=sqlite3.connect("owned.db")
    ct=dt.cursor()
    ct.execute(f"select * from '{ctx.author.id}'")
    m=ct.fetchall()
    if mx>len(m):
        await ctx.send("Some pokémons don't exist.")
    elif len(tm)==6:
        c.execute(f"""update '{ctx.author.id}' set squad="{team}" """)
        db.commit()
        await ctx.send("Team update successful!")

@bot.command(aliases=["pr"])       
async def profile(ctx):
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"select * from '{ctx.author.id}'")
    det=c.fetchone()
    data=discord.Embed(title=f"{ctx.author.display_name}'s Profile:", description=f"**Balance:** {det[0]} ¥")
    try:
        team=await teamconvert(ctx,ctx.author,ctx.author.id)
        tm=""
        n=0
        for i in team:
            n+=1
            tm+=f"#{n} {i.name}\n"
        data.add_field(name="Current Team:",value=tm)
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
    field=Field()
    p1team=await teamconvert(ctx,p1,p1.id)
    if isinstance(p2, int):
        tr2=await gameteam(ctx,p2)
    else:
        p2team=await teamconvert(ctx,p2,p2.id)
        tr2=Trainer(p2.display_name,p2team,"Earth",sprite=p2.avatar,member=p2)
    tr1=Trainer(p1.display_name,p1team,"Earth",sprite=p1.avatar,member=p1)
    intro=discord.Embed(title=f"{tr1.name} vs {tr2.name}")
    intro.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1103853991760248924/VS.png")
    intro.add_field(name="Task:",value="Choose your lead pokémon! Check your DM!")
    intro.set_footer(text=f"Location: {field.location} | Weather: {field.weather} | Terrain: {field.terrain}")
    await ctx.send(embed=intro)
    p2team=tr2.pokemons
    p1leadoptions=""
    p2leadoptions=""
    n1=0
    n2=0
    for i in p1team:
        n1+=1
        p1leadoptions+=f"#{n1} {i.name}\n"
    for i in p2team:
        n2+=1
        p2leadoptions+=f"#{n2} {i.name}\n"
    p1leadem=discord.Embed(title="Choose your lead pokémon!", description=p1leadoptions) 
    p1leadem.set_footer(text="Enter the number until you get the confirmation messaage!")
    if tr2.ai==False:
        p2leadem=discord.Embed(title="Choose your lead pokémon!", description=p2leadoptions)
        p2leadem.set_footer(text="Enter the number until you get the confirmation messaage!")
    x,y=None,None
    def xcheck(message):
        return isinstance(message.channel,discord.DMChannel) and message.author==p1
    if tr2.ai==False:
        def ycheck(message):
            return isinstance(message.channel,discord.DMChannel) and message.author==p2                
    while True:
        if x==None and tr2.ai==True:
            await ctx.send(embed=p1leadem) 
            while True:
                xnum=await bot.wait_for('message')
                if xnum.author==ctx.author:
                    x=tr1.pokemons[int(xnum.content)-1]
                    break
        if x==None and tr2.ai==False:
            await p2.send(f"{tr1.name} is choosing their lead pokémon. Please wait patiently!")
            await p1.send(embed=p1leadem) 
            xnum=await bot.wait_for('message',check=xcheck)
            x=tr1.pokemons[int(xnum.content)-1]
            if x!=None:
                await p1.send(f"You chose {x.name} as your lead pokémon.")
        if x!=None and tr2.ai==True:
             y=random.choice(tr2.pokemons)     
        if x!=None and tr2.ai==False:
            await p1.send(f"{tr2.name} is choosing their lead pokémon. Please wait patiently!")
            await p2.send(embed=p2leadem)
            ynum=await bot.wait_for('message',check=ycheck)   
            y=tr2.pokemons[int(ynum.content)-1]   
            if x!=None:
                await p2.send(f"You chose {y.name} as your lead pokémon. Now go back to the server!")
        if None not in (x,y):
            break       
        
    turn=0        
    if x.speed>=y.speed:
        await entryeff(ctx,x,y,tr1,tr2,field,turn)
        await entryeff(ctx,y,x,tr2,tr1,field,turn)        
    if y.speed>x.speed:
        await entryeff(ctx,y,x,tr2,tr1,field,turn)      
        await entryeff(ctx,x,y,tr1,tr2,field,turn) 
    lead1=discord.Embed(title=f"{tr1.name}: Go, {x.nickname}!",description=f"{tr1.name} sents out **{x.name}**!")
    lead1.set_image(url=x.sprite)   
    lead1.set_thumbnail(url=tr1.sprite)
    lead2=discord.Embed(title=f"{tr2.name}: Go, {y.nickname}!", description=f"{tr2.name} sents out **{y.name}**!")
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
        bg=int("FFFFFF",16)
        if field.terrain in ["Normal"]:
            bg=int("E5E7E2",16)
        if field.weather in ["Clear","None"]:
            bg=int("E5E7E2",16)
        if field.weather=="Cloudy": 
            bg=int("E5E7E2",16)
        if field.terrain=="Misty":
            bg=int("FEB8B7",16)
        if field.terrain=="Psychic":
            bg=int("BD61E6",16)
        if field.terrain=="Electric":
            bg=int("D5CD73",16)
        if field.terrain=="Grassy":
            bg=int("9CF7BD",16)
        if field.weather=="Strong Winds":
            bg=int("90FFF0",16)
        if field.weather=="Extreme Sunlight":
            bg=int("FF5E20",16)
        if field.weather=="Heavy Rain":
            bg=int("0790FF",16)
        if field.weather in ["Hail","Snowstorm"]:
            if field.weather=="Snowstorm":
                bg=int("CCECFF",16)
            if field.weather=="Hail":
                bg=int("7EC8FF",16)
        if field.weather=="Rainy":
            bg=int("32C7FF",16)
        if field.weather=="Sunny":
            bg=int("FAFF6C",16)
        if field.weather=="Sandstorm":
            bg=int("CCAF5E",16)
        turnem=discord.Embed(title=f"Turn: {turn}", description=f"**Location:** {field.location}\n**Weather:** {field.weather}\n**Terrain:** {field.terrain}\n",color=bg)
        await ctx.send(embed=turnem)
        if x.protect==True:
            x.protect=False
        if y.protect==True:
            y.protect=False
        action1=None
        action2=None
        while action1==None or action2==None:
            if action1 not in [1,2]:
                action1=await action(bot,ctx,tr1,tr2,x,y)
            if action2 not in [1,2]:
                action2=await action(bot,ctx,tr2,tr1,y,x)     
        if action1==3 and action2!=3:
            break
        if action2==3 and action1!=3:
            break 
        em1=""
        em2=""
        if tr2.ai==False:
            await tr1.member.send("Please wait...")
            await tr2.member.send("Please wait...")
        if action1==8:
            x,em1=await maxtrans(ctx,x,tr1,turn)
            action1=1
        if action1==7:
            action1=1
        if action1==6:
            x,em1=await megatrans(ctx,x,y,tr1,tr2,field,turn)
            action1=1
        if action1==9:
            x,em1=await teratrans(ctx,x,tr1)
            action1=1
        if action2==8:
            y,em2=await maxtrans(ctx,y,tr2,turn)
            action2=1
        if action2==7:
            action2=1
        if action2==6:
            y,em2=await megatrans(ctx,y,x,tr2,tr1,field,turn)
            action2=1
        if action2==9:
            y,em2=await teratrans(ctx,y,tr2)
            action2=1
        if action1==2 and len(tr1.pokemons)==1:
            action1=1
        if action2==2 and len(tr2.pokemons)==1:
            action2=1
        if em1!="":
            await ctx.send(embed=em1)     
        if em2!="":
            await ctx.send(embed=em2)
        if action1==1 and action2==1:
            if tr2.ai==True:
                await advscore(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
            if tr2.ai==False:
                await score(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
                await advscore(ctx,x,y,tr1,tr2,turn,bg)
                await advscore(ctx,y,x,tr2,tr1,turn,bg)
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
                if yPriority>80:
                    yPriority=True
            if x.ability=="Quick Draw":
                xPriority=random.randint(1,100)
                if xPriority>20:
                    xPriority=True
            if x.item=="Quick Claw":
                xPriority=random.randint(1,100)
                if xPriority>82:
                    xPriority=True
            if y.item=="Quick Claw":
                yPriority=random.randint(1,100)
                if yPriority>82:
                    yPriority=True
            if y.item=="Quick Claw" and y.ability=="Quick Draw":
                yPriority=random.randint(1,100)
                if yPriority>64:
                    yPriority=True
            if x.item=="Quick Claw" and x.ability=="Quick Draw":
                xPriority=random.randint(1,100)
                if xPriority>64:
                    xPriority=True
            if (choice1 in typemoves.prioritymove and choice2 not in typemoves.prioritymove) or x.priority is True or (x.ability=="Prankster" and choice1 in typemoves.statusmove and "Dark" not in (y.primaryType,y.secondaryType)) or (choice1 in typemoves.firemoves and x.ability=="Blazing Soul") or (choice1 in typemoves.flyingmoves and x.ability=="Gale Wings") or (field.terrain=="Grassy" and choice1=="Grassy Glide") or (x.ability=="Triage" and choice1 in typemoves.healingmoves) or (choice2 in typemoves.negprioritymove) or (xPriority==True) or (choice2 in typemoves.statusmove and y.ability=="Mycelium Might") or y.item=="Lagging Tail":
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
                    y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2, choice1,field,turn)
                    await effects (ctx,x,y,tr1,turn)
                    await effects(ctx,y,x,tr2,turn)
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
            elif (choice2 in typemoves.prioritymove and choice1 not in typemoves.prioritymove) or x.priority is True or (x.ability=="Prankster" and choice2 in typemoves.statusmove and "Dark" not in (x.primaryType,x.secondaryType)) or (choice2 in typemoves.firemoves and y.ability=="Blazing Soul") or (choice2 in typemoves.flyingmoves and y.ability=="Gale Wings") or (field.terrain=="Grassy" and choice2=="Grassy Glide") or (y.ability=="Triage" and choice2 in typemoves.healingmoves) or (choice1 in typemoves.negprioritymove) or (yPriority==True) or (choice1 in typemoves.statusmove and x.ability=="Mycelium Might") or x.item=="Lagging Tail":
                await weather(ctx,field,bg)   
                y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2, choice1,field,turn)
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
                    await effects(ctx,y,x,tr2,turn)
                    await effects (ctx,x,y,tr1,turn)
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
                    await effects(ctx,y,x,tr2,turn)
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
                    y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2, choice1,field,turn)
                    await effects (ctx,x,y,tr1,turn)
                    await effects(ctx,y,x,tr2,turn)
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
                    await effects (ctx,x,y,tr1,turn)
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
                    y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2, choice1,field,turn)
                    await effects (ctx,x,y,tr1,turn)
                    await effects(ctx,y,x,tr2,turn)
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
                    await effects (ctx,x,y,tr1,turn)
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
                y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2, choice1,field,turn)
                await prebuff(ctx,x,y,tr1,tr2,turn,field)
                await prebuff(ctx,y,x,tr2,tr1,turn,field)
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break
                elif x.hp>0:                    
                    x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
                    await effects(ctx,y,x,tr2,turn)
                    await effects (ctx,x,y,tr1,turn)
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
                    await effects(ctx,y,x,tr2,turn)
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
                y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2, choice1,field,turn)
                await prebuff(ctx,x,y,tr1,tr2,turn,field)
                await prebuff(ctx,y,x,tr2,tr1,turn,field)
                if y.hp<=0:
                    y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                    if len(tr2.pokemons)==0:
                        await winner(ctx,tr1,tr2)
                        break
                elif x.hp>0:                    
                    x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
                    await effects(ctx,y,x,tr2,turn)
                    await effects (ctx,x,y,tr1,turn)
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
                    await effects(ctx,y,x,tr2,turn)
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
                await advscore(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
            if tr2.ai==False:
                await score(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
                await advscore(ctx,x,y,tr1,tr2,turn,bg)
                await advscore(ctx,y,x,tr2,tr1,turn,bg)
            choice2=await fchoice(ctx,bot,y,x,tr2,tr1,field)
            await weather(ctx,field,bg)
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
            y,x=await attack(ctx,bot,y,x,tr2,tr1,choice2, choice1,field,turn)
            await effects (ctx,x,y,tr1,turn)
            await effects(ctx,y,x,tr2,turn)
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
            y.protect=False
#tr1 ATTACKS AND tr2 SWITCHES                
        elif action1==1 and action2==2:
            choice2="None"
            if tr2.ai==True:
                await advscore(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
            if tr2.ai==False:
                await score(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
                await advscore(ctx,x,y,tr1,tr2,turn,bg)
                await advscore(ctx,y,x,tr2,tr1,turn,bg)
            choice1=await fchoice(ctx,bot,x,y,tr1,tr2,field)
            await weather(ctx,field,bg)
            y=await switch(ctx,bot,y,x,tr2,tr1,field,turn)
            x,y=await attack(ctx,bot,x,y,tr1,tr2,choice1,choice2,field,turn)
            if x.hp<=0:
                x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                   await winner(ctx,tr2,tr1)
                   break
            await effects (ctx,x,y,tr1,turn)
            await effects(ctx,y,x,tr2,turn)
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
            x.protect=False
#IF BOTH SWITCHES                
        elif action1==2 and action2==2:
            if tr2.ai==True:
                await advscore(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
            if tr2.ai==False:
                await score(ctx,x,y,tr1,tr2,turn,bg)
                await score(ctx,y,x,tr2,tr1,turn,bg)
                await advscore(ctx,x,y,tr1,tr2,turn,bg)
                await advscore(ctx,y,x,tr2,tr1,turn,bg)
            await weather(ctx,field,bg)
            if x.speed>=y.speed:
                x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)  
                y=await switch(ctx,bot,y,x,tr2,tr1,field,turn)
            if y.speed>x.speed:
                y=await switch(ctx,bot,y,x,tr2,tr1,field,turn)
                x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)  
            await effects(ctx,y,x,tr2,turn)
            if y.hp<=0:
                y=await faint(ctx,bot,y,x,tr2,tr1,field,turn)
                if len(tr2.pokemons)==0:
                    await winner(ctx,tr1,tr2)
                    break
            await effects (ctx,x,y,tr1,turn)          
            if x.hp<=0:
                x=await faint(ctx,bot,x,y,tr1,tr2,field,turn)
                if len(tr1.pokemons)==0:
                   await winner(ctx,tr2,tr1)
                   break            
keep_alive()
bot.run(token)    