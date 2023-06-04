from typematchup import *
#Charge
async def charge(ctx,x,y,tr1,em,field):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Charge!")
    await spdefchange(x,x,1)
    x.charged=True
#Needle Arm
async def needlearm(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Needle Arm!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)    
    #flinch
#Explosion
async def explosion(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Explosion!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Reckless":
        al*=1.2
    if y.ability!="Damp":
        y.hp-=await physical(x,x.level,x.atk,(y.defense/2),150,a,b,c,r,al)              
    x.hp=0  
#Misty Explosion
async def mistyexplosion(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Misty Explosion!")    
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Reckless":
        al*=1.2
    if field.terrain=="Misty":
        al=1.5
    if y.ability!="Damp":
        y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)              
    x.hp=0      
#Meteor Mash
async def meteormash(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Meteor Mash!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)            
    ch=random.randint(1,10)
    if ch<2:
        await atkchange(x,x,1)  
#Thunder Fang
async def thunderfang(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder Fang!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)            
    #paralyze
#Ice Fang
async def icefang(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Fang!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)            
    #freeze    
#Psychic Fangs
async def psychicfangs(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psychic Fangs!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)            
    #screen break
#Poison Fang
async def poisonfang(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Poison Fang!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)            
    #poison
#Fire Fang
async def firefang(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Fang!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al,w)            
    #burn
#Crunch
async def crunch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Crunch!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)        
    ch=random.randint(1,10)
    if x.ability!="Sheer Force" and ch<2:
        await defchange(y,x,-1)        
#Spirit Break
async def spiritbreak(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Spirit Break!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)        
    if x.ability!="Sheer Force":
        await spatkchange(y,x,-1)    
#False Surrender
async def falsesurrender(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used False surrender!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)    
#Rock Tomb
async def rocktomb(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rock Tomb!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=60
    if x.ability=="Technician":
        base*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)    
    if a!=0 and x.ability!="Sheer Force":
        await speedchange(y,x,-1)      
#Breaking Swipe
async def breakingswipe(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Breaking Swipe!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=60
    if x.ability=="Technician":
        base*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)    
    if a!=0 and x.ability!="Sheer Force":
        await atkchange(y,x,-1)  
#Poison Jab
async def poisonjab(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Poison Jab!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)           
    #Poison 
#Poison Tail
async def poisontail(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Poison Tail!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)           
    #Poison     
#Dragon Hammer
async def dragonhammer(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Hammer!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)           
    #Flinch    
#Zen Headbutt
async def zenheadbutt(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Zen Headbutt!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)           
    #Flinch    
#Iron Head
async def ironhead(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Iron Head!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)           
    #Flinch
#Iron Tail
async def irontail(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Iron Tail!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)               
    #statdrop
#Grassy Glide
async def grassyglide(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Grassy Glide!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al) 
#Drum Beating
async def drumbeating(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Drum Beating!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)                   
    #speeddrop
#Ice Hammer
async def icehammer(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Hammer!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)     
    await speedchange(x,x,-1)
#U-turn
async def uturn(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used U-turn!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al) 
#Flip Turn
async def flipturn(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flip Turn!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al,w)           
#Hammer Arm
async def hammerarm(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hammer Arm!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)     
    await speedchange(x,x,-1)    
#Play Rough
async def playrough(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Play Rough!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)        
    ch=random.randint(1,10)
    if ch==7 and x.ability!="Sheer Force":
        await atkchange(y,x,-1)  
#Thunder Wave
async def thunderwave(ctx,x,y,tr1,em,field):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder Wave!")
    y.status="Paralyzed"
    #needs work 
#Toxic
async def toxic(ctx,x,y,tr1,em,field):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Toxic!")
    y.status="Badly Poisoned"
    #needs work             
#Will-O-Wisp
async def willowisp(ctx,x,y,tr1,em,field):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Will-O-Wisp!")
    y.status="Burned"
    #needs work 
#Gigaton Hammer
async def gigatonhammer(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Gigaton Hammer!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,160,a,b,c,r,al)        
#Glacial Lance
async def glaciallance(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Glacial Lance!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)    
#Superpower
async def superpower(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Superpower!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)        
    await atkchange(x,x,-1)
    await defchange(x,x,-1)    
#Close Combat
async def closecombat(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Close Combat!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)        
    await defchange(x,x,-1)
    await spdefchange(x,x,-1)
#Avalanche
async def avalanche(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Avalanche!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.use!="None" and y.use not in typemoves.statusmove and x.speed<y.speed:
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al)    
#Icicle Crash
async def iciclecrash(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Icicle Crash!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al)            
    #flinch
#Ice Spinner
async def icespinner(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Spinner!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)              
    if field.terrain!="Normal":
        field.terrain="Normal"
#Order Up 
async def orderup(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Order Up!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)  
#Bullet Punch
async def bulletpunch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bullet Punch!")    
    x.atktype="Steel"
    base=40
    if x.ability=="Technician":
        base*=1.5
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)        
#Mach Punch
async def machpunch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Mach Punch!")    
    x.atktype="Fighting"
    base=40
    if x.ability=="Technician":
        base*=1.5
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)   
#Ice Shard
async def iceshard(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Shard!")    
    x.atktype="Ice"
    base=40
    if x.ability=="Technician":
        base*=1.5
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al) 
#Aqua Jet
async def aquajet(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aqua Jet!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    base=40
    if x.ability=="Technician":
        base*=1.5
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al,w)      
#Jet Punch
async def jetpunch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Jet Punch!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    base=60
    if x.ability=="Technician":
        base*=1.5
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al,w)                     
#Plasma Fists
async def plasmafists(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Plasma Fists!")    
    x.atktype="Electric"
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al) 
#Bolt Strike
async def boltstrike(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bolt Strike!")    
    x.atktype="Electric"
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)     
    #paralyze
#Ice Punch
async def icepunch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Punch!")    
    x.atktype="Ice"
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)     
    #freeze
#Fire Punch
async def firepunch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Punch!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al,w)             
    #burn
#Flare Blitz
async def flareblitz(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flare Blitz!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    if x.ability=="Reckless":
        al*=1.2
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al,w)             
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")    
    #burn    
#Thunder Punch
async def thunderpunch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder Punch!")    
    x.atktype="Electric"
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)     
    #paralyze
#Extreme Speed
async def extremespeed(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Extreme Speed!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)       
#Sucker Punch
async def suckerpunch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sucker Punch!")    
    x.atktype="Dark"
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)     
#Outrage
async def outrage(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Outrage!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)     
    #count
#Body Slam
async def bodyslam(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Body Slam!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)     
    #paralyze
#Kowtow Cleave
async def kowtowcleave(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Kowtow Cleave!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)        
#Shadow Claw    
async def shadowclaw(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shadow Claw!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)     
#Dragon Claw    
async def dragonclaw(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Claw!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al) 
#Stone Edge    
async def stoneedge(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Stone Edge!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)     
#Leaf Blade
async def leafblade(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Leaf Blade!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)   
#X-Scissor
async def xscissor(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used X-Scissor!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al) 
#Megahorn
async def megahorn(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Megahorn!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)                 
#Drill Peck
async def drillpeck(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Drill Peck!")    
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)      
#Earthquake    
async def earthquake(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Earthquake!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)      
#Ice Beam
async def icebeam(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Beam!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)  
    #freeze
#Freeze-Dry
async def freezedry(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Freeze-Dry!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,70,a,b,c,r,al)      
#Extrasensory
async def extrasensory(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Extrasensory!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    #flinch
#Psychic   
async def psychic(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psychic!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)  
    chance=20
    if x.ability=="Serene Grace":
        chance*=2
    if x.speed>y.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and a!=0 and x.ability!="Sheer Force":
            await spdefchange(y,x,-1)    
#Roost
async def roost(ctx,x,y,tr1,em,field):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Roost!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.maxhp/2
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")            
#Slack Off
async def slackoff(ctx,x,y,tr1,em,field):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Slack Off!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.maxhp/2
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")            
#Milk Drink
async def milkdrink(ctx,x,y,tr1,em,field):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Milk Drink!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.maxhp/2
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")      
#Jungle Healing
async def junglehealing(ctx,x,y,tr1,em,field):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Jungle Healing!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.maxhp/2
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")            
#Soft-Boiled
async def softboiled(ctx,x,y,tr1,em,field):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Soft-Boiled!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.maxhp/2
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")           
#Heal Order
async def healorder(ctx,x,y,tr1,em,field):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Heal Order!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.maxhp/2
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")         
#Hyper Beam
async def hyperbeam(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hyper Beam!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al) 
#Prismatic Laser
async def prismaticlaser(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Prismatic Laser!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al)                 
#Leaf Storm
async def leafstorm(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Leaf Storm!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,130,a,b,c,r,al)          
    if a!=0:
        await spatkchange(x,x,-2)
#Oblivion Wing
async def oblivionwing(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Oblivion Wing!")    
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)          
    y.hp-=dmg
    heal=dmg*0.75
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        x.hp-=heal
    else:
        x.hp+=heal        
#Grassy Terrain
async def grassyterrain(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Grassy Terrain!")        
    if field.terrain!="Grassy":
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(x,y)
        em.add_field(name="Grassy Terrain",value="Grass grew to cover the battlefield!")
#Misty Terrain
async def mistyterrain(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Misty Terrain!")        
    if field.terrain!="Misty":
        field.terrain="Misty"
        field.misturn=turn
        field.misend(x.y)
        em.add_field(name="Misty Terrain",value="Mist swirled around the battlefield!")        
#Psychic Terrain
async def psychicterrain(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psychic Terrain!")        
    if field.terrain!="Psychic":
        field.terrain="Psychic"
        field.psyturn=turn
        field.psyend(x,y)
        em.add_field(name="Psychic Terrain",value="The battlefield got weird!")
#Electric Terrain
async def electricterrain(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Electric Terrain!")
    if field.terrain!="Electric":
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(x,y)
        em.add_field(name="Electric Terrain",value="An electric current ran across the battlefield!")
#Dream Eater
async def dreameater(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dream Eater!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)          
    if y.status=="Sleep":
        y.hp-=dmg
        heal=dmg/2
        if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
            x.hp-=heal
        else:
            x.hp+=heal        
#Giga Drain
async def gigadrain(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Giga Drain!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)          
    y.hp-=dmg
    heal=dmg/2
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        x.hp-=heal
    else:
        x.hp+=heal
#Draco Meteor
async def dracometeor(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Draco Meteor!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,130,a,b,c,r,al)          
    if a!=0:
        await spatkchange(x,x,-2)        
#Make It Rain
async def makeitrain(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Make It Rain!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)          
    if a!=0:
        await spatkchange(x,x,-1)        
#Recover
async def recover(ctx,x,y,tr1,em,field):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Recover!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.maxhp/2
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
#Moonblast
async def moonblast(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Moonblast!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)             
    #spatk drop
#Aura Sphere
async def aurasphere(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aura Sphere!")    
    if x.ability=="Mega Launcher":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Mega Launcher!",value="")
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)        
#Air Slash
async def airslash(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Air Slash!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,75,a,b,c,r,al)    
    #flinch
#Scald
async def scald(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Scald!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al,w)    
    #burn        
#Volt Switch
async def voltswitch(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Volt Switch!")
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,70,a,b,c,r,al)              
#Thunderbolt
async def thunderbolt(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunderbolt!")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)                     
    #paralyze
#Thunder
async def thunder(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder!")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)                     
    #paralyze    
#Rising Voltage
async def risingvoltage(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rising Voltage!")
    if field.terrain=="Electric":
        al=1.5
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,70,a,b,c,r,al)                     
    #paralyze    
#Power Gem
async def powergem(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Power Gem!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)       
#Heat Wave
async def heatwave(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Heat Wave!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)    
    #burn
#Boomburst
async def boomburst(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Boomburst!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    w=await weathereff(field,x,y,em)
    y.hp-=await special(x,x.level,x.spatk,y.spdef,140,a,b,c,r,al,w)
#Blizzard
async def blizzard(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Blizzard!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al)    
    #freeze
#Sacred Fire
async def sacredfire(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sacred Fire!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al,w)    
    #burn    
#Hydro Pump     
async def hydropump(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hydro Pump!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al,w)           
#Origin Pulse
async def originpulse(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Origin Pulse!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al,w)     
#Scorching Sands
async def scorchingsands(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Scorching Sands!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)     
    #burn
#Sludge Bomb 
async def sludgebomb(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sludge Bomb!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    #poison
#Dark Pulse           
async def darkpulse(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dark Pulse!")    
    if x.ability=="Mega Launcher":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Mega Launcher!",value="")
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)         
    #flinch
#Flamethrower
async def flamethrower(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flamethrower!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al,w)     
    #burn
#Fire Blast
async def fireblast(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Blast!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al,w)     
    #burn    
#Shadow Ball            
async def shadowball(ctx,x,y,tr1,em,field):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shadow Ball!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)  
    chance=20
    if x.ability=="Serene Grace":
        chance*=2
    if x.speed>y.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and a!=0 and x.ability!="Sheer Force":
            await spdefchange(y,x,-1)
#Psych Up
async def psychup(ctx,x,y,tr1,em,field):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psych Up!") 
    x.atkb=y.atkb
    x.defb=y.defb
    x.spatkb=y.spatkb
    x.spdefb=y.spdefb
    x.speedb=y.speedb
#Perish Song    
async def perishsong(ctx,x,y,tr1,em,field):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Perish Song!") 
    if 0 in (x.perishturn,y.perishturn):
        em.add_field(name=f"Move Effect:",value=f"All Pokéx that heard the song will faint in three turns!")
    if x.perishturn==0 and x.ability!="Soundproof":
        x.perishturn=4
    if y.perishturn==0 and y.ability!="Soundproof":
        y.perishturn=4          
#Acupressure                     
async def acupressure(ctx,x,y,tr1,em,field):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Acupressure!")
    m=random.randint(1,5)
    if m==1:
        await atkchange(x,x,2)
    if m==2:
        await defchange(x,x,2)
    if m==3:
        await spatkchange(x,x,2)
    if m==4:
        await spdefchange(x,x,2)
    if m==5:
        await speedchange(x,x,2)
#Psycho Shift
async def psychoshift(ctx,x,y,tr1,em,field):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psycho Shift!")
    if y.status=="Alive" and x.status!="Alive":
        x.status,y,status=y.status,x.status
        em.add_field(name=f"Move Effect:",value=f"{x.nickname} shifted it's status condition to {y.name}!")
#Flail
async def flail(ctx,x,y,tr1,em,field):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flail!")
    mark=(64*x.hp)/x.maxhp
    dmg=0
    if 0<=mark<=1:
        dmg=200
    if 2<=mark<=5:
        dmg=150
    if 6<=mark<=12:
        dmg=100
    if 13<=mark<=21:
        dmg=80
    if 22<=mark<=42:
        dmg=40
    if 43<=mark<=64:
        dmg=20
    x.atktype="Normal"
    al=1
    r=await randroll()
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-physical(x,x.level,x.atk,y.defense,dmg,a,b,c,r,al)
#Reversal
async def reversal(ctx,x,y,tr1,em,field):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Reversal!")
    mark=(64*x.hp)/x.maxhp
    dmg=0
    if 0<=mark<=1:
        dmg=200
    if 2<=mark<=5:
        dmg=150
    if 6<=mark<=12:
        dmg=100
    if 13<=mark<=21:
        dmg=80
    if 22<=mark<=42:
        dmg=40
    if 43<=mark<=64:
        dmg=20
    x.atktype="Fighting"
    al=1
    r=await randroll()
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=physical(x,x.level,x.atk,y.defense,dmg,a,b,c,r,al)

async def physical(x,level,atk,defense,base,a=1,b=1,c=1,r=1,al=1,w=1):
    x.atkcat="Physical"
    dmg=round((((2*level + 10)/250)*(atk/ defense)*base+2)*a*b*c*r*al*w)
    return dmg
async def special(x,level,spatk,spdef,base,a=1,b=1,c=1,r=1,al=1,w=1):
    x.atkcat="Special"
    dmg=round((((2*level + 10)/250)*(spatk/spdef)*base+2)*a*b*c*r*al*w)
    return dmg
    
async def weathereff(field,x,y,em):
    if field.weather=="Extreme Sunlight" and x.atktype=="Water" and "Cloud Nine" not in (x.ability,y.ability):
        em.add_field(name="Extreme Sunlight:",value="The Water-type attack evaporated in the harsh sunlight!")
        return 0
    if field.weather=="Heavy Rain" and x.atktype=="Fire" and "Cloud Nine" not in (x.ability,y.ability):
        em.add_field(name="Heavy Rain:",value="The Fire-type attack fizzled out in the heavy rain!")
        return 0                                 
    if field.weather in ["Rainy","Heavy Rain"] and x.atktype=="Water" and "Cloud Nine" not in (x.ability,y.ability):
        print(" 🌧️ Rain boosted!")
        return 1.5
    if (field.weather=="Sunny") and x.atktype=="Water" and "Cloud Nine" not in (x.ability,y.ability):
        print(" ☀️ Sun weakened!")
        return 0.5    
    if (field.weather=="Rainy") and x.atktype=="Fire" and "Cloud Nine" not in (x.ability,y.ability):
        print(" 🌧️ Rain weakened!")
        return 0.5      
    if field.weather in ["Sunny" ,"Extreme Sunlight"] and x.atktype=="Fire" and "Cloud Nine" not in (x.ability,y.ability):
        print(" ☀️ Sun boosted!")
        if "Koraidon" in x.name:
            return 2
        else:
            return 1.5        
    else:
        return 1     