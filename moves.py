from typematchup import *
from status import *
megastones=("Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Ampharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite")
#Silk Trap
async def silktrap(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Silk Trap!")
    x.protect=True
#Obstruct
async def obstruct(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Obstruct!")
    x.protect=True
#Max Guard
async def maxguard(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Guard!")
    x.protect=True
#Baneful Bunker
async def banefulbunker(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Baneful Bunker!")
    x.protect=True
#Spiky Shield
async def spikyshield(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Spiky Shield!")
    x.protect=True
#Protect
async def prtect(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Protect!")
    x.protect=True
#Spore
async def spore(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Spore!")
    if "Grass" not in (y.secondaryType,y.primaryType,y.teraType) and y.status=="Alive":
        await sleep(em,x,y,100)
#Eerie Impulse 
async def eerieimpulse(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Eerie Impulse!")
    await spatkchange(em,y,x,-2)
#Tickle
async def tickle(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Tickle!")
    await atkchange(em,y,x,-1)    
    await defchange(em,y,x,-1)
#Fillet Away
async def filletaway(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fillet Away!")
    if x.hp>(x.maxhp/3):
        await atkchange(em,x,x,2)
        await spatkchange(em,x,x,2)
        await speedchange(em,x,x,2)        
        x.hp-=round(x.maxhp/3)
#Metal Sound
async def metalsound(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Metal Sound!")
    await spdefchange(em,y,x,-2)    
#Fake Tears
async def faketears(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fake Tears!")
    await spdefchange(em,y,x,-2)    
#Feather Dance
async def featherdance(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Feather Dance!")
    await atkchange(em,y,x,-2)    
#Scary Face
async def scaryface(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Scary Face!")
    await speedchange(em,y,x,-2)
#Charm
async def charm(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Charm!")
    await atkchange(em,y,x,-2)
#Super Fang
async def superfang(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Super Fang!")    
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    if a!=0:
        y.hp/=2
#Ruination
async def ruination(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ruination!")    
    y.hp/=2  
#Nature's Madness
async def naturesmadness(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Nature's Madness!")    
    y.hp/=2            
#Water Spout
async def waterspout(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Water Spout!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=round(150*(x.hp/x.maxhp))
    y.hp-=await special(x,x.level,x.spatk,y.spdef,base,a,b,c,r,al,w)    
#Eruption
async def eruption(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Eruption!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=round(150*(x.hp/x.maxhp))
    y.hp-=await special(x,x.level,x.spatk,y.spdef,base,a,b,c,r,al,w)            
#Crush Grip
async def crushgrip(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Crush Grip!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=round(120*(x.hp/x.maxhp))
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)        
#Dragon Energy
async def dragonenergy(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Energy!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=round(150*(x.hp/x.maxhp))
    y.hp-=await special(x,x.level,x.spatk,y.spdef,base,a,b,c,r,al)        
#Steam Eruption
async def steameruption(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Steam Eruption!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al,w)     
    #burn    
#Fiery Dance
async def fierydance(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fiery Dance!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al,w)     
    ch=random.randint(1,2)
    if a!=0 and ch==1:
        await spatkchange(em,x,x,1)
#Tar Shot
async def tarshot(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Tar Shot!")
    await speedchange(em,y,x,-1)
    if y.tarshot is False:
        y.tarshot=True
        em.add_field(name="Effect:",value=f"{x.nickname} became weak to Fire-Type attacks!")
#Soak
async def soak(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Soak!")
    y.primaryType="Water"
    y.secondaryType="???"
    em.add_field(name="Effect:",value=f"{x.nickname} turned into {y.primaryType} type!")
#Magic Powder
async def magicpowder(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Magic Powder!")
    y.primaryType="Psychic"
    y.secondaryType="???"
    em.add_field(name="Effect:",value=f"{x.nickname} turned into {y.primaryType} type!")
#Trick-Or-Treat
async def trickortreat(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Trick-Or-Treat!")
    y.primaryType="Ghost"
    y.secondaryType="???"
    em.add_field(name="Effect:",value=f"{x.nickname} turned into {y.primaryType} type!")
#Forests Curse
async def forestscurse(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Forest's Curse!")
    y.primaryType="Grass"
    y.secondaryType="???"
    em.add_field(name="Effect:",value=f"{x.nickname} turned into {y.primaryType} type!")    
#Trick
async def trick(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Trick!")  
    if y.item=="None" or (y.ability!="Sticky Hold" and "m-Z" not in y.item and y.item not in megastones and "m-Z" not in x.item and x.item not in megastones):
        em.add_field(name="Effect:",value=f"{x.nickname} swapped its {x.item} with {y.name}'s {y.item}!")
        x.item,y.item=y.item,x.item
    else:
        em.add_field(name="Effect:",value="It failed!")
#Skill Swap
async def skillswap(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Skill Swap!")  
    if y.item!="Ability Shield":
        em.add_field(name="Effect:",value=f"{x.nickname} swapped its {x.ability} with {y.nickname}'s {y.ability}!")
    else:
        em.add_field(name="Effect:",value="It failed!")
#Recycle
async def recycle(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Recycle!")  
    if "Used" in x.item or x.item=="None":
        em.add_field(name="Effect:",value="It failed!")
    else:
        x.item=x.item.split("[")[0]
        em.add_field(name="Effect:",value=f"{x.nickname} recycled its {x.item}!")
#Spicy Extract
async def spicyextract(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Spicy Extract!")  
    await atkchange(em,y,x,2)
    await defchange(em,y,x,-2)
#Yawn
async def yawn(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Yawn!")  
    if y.yawn is False and y.status=="Alive":
        y.yawn=True
        em.add_field(name="Effect:",value=f"{y.nickname} became drowsy!")
    else:
        em.add_field(name="Effect:",value="It failed!")        
#Doodle
async def doodle(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Doodle!")  
    x.ability=y.ability 
    em.add_field(name="Effect:",value=f"{x.nickname} gained {y.ability}!")
#Aqua Ring
async def aquaring(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Aqua Ring!")  
    if x.aring is False:
        x.aring=True
    else:
        em.add_field(name="Effect:",value="It failed!")
#Wish 
async def wish(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Wish!")  
    if tr1.wishhp is False:
        tr1.wishhp=str(round(x.maxhp/2))
    else:
        em.add_field(name="Effect:",value="It failed!")
#Encore
async def encore(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Encore!")  
    if y.use!="None" and y.dmax==False and y.encore==False:
        em.add_field(name="Effect:",value=f"{x.nickname} fell for the encore!")
        y.encore=y.use
        y.encendturn=turn+random.randint(3,5)
    else:      
        em.add_field(name="Effect:",value="It failed!")  
async def hailend(tr1,mon,mon2):
	   if "Icy Rock" not in (mon.item,mon2.item):
	       tr1.hailendturn=tr1.hailturn+5
	   if "Icy Rock" in (mon.item,mon2.item):
	       tr1.hailendturn=tr1.hailturn+8  
async def snowend(tr1,mon,mon2):
	   if "Icy Rock" not in (mon.item,mon2.item):
	       tr1.snowendturn=tr1.snowturn+5
	   if "Icy Rock" in (mon.item,mon2.item):
	       tr1.snowendturn=tr1.snowturn+8  
#Snowscape
async def snowscape(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Snowscape!")    	
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Snowstorm"] and a!=0:
        em.add_field(name="Weather:",value=f"{x.nickname} started a snowstorm!")
        field.weather="Snowstorm"
        tr1.snowturn=turn
        await snowend(tr1,x,y)          	         
#Max Hailstorm
async def maxhailstorm(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Max Hailstorm!")        
    al=1
    r=await randroll()
    x.atktype="Ice"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al,w)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121422200717713529/image_search_1687438277877.png")        
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Hail"] and a!=0:
        em.add_field(name="Weather:",value=f"{x.nickname} started a hailstorm!")
        field.weather="Hail"
        tr1.hailturn=turn
        await hailend(tr1,x,y)    
        
async def sandend(tr1,mon,mon2):
	   if "Smooth Rock" not in (mon.item,mon2.item):
	       tr1.sandendturn=tr1.sandturn+5
	   if "Smooth Rock" in (mon.item,mon2.item):
	       tr1.sandendturn=tr1.sandturn+8  
#Sandstorm
async def sandstorm(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sandstorm!")   
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Sandstorm"]:        
        em.add_field(name="Weather:",value=f"{x.nickname} started a sandstorm!")
        field.weather="Sandstorm"
        tr1.sandturn=turn
        await sandend(tr1,x,y) 	                 
#Max Rockfall
async def maxrockfall(ctx,x,y,tr1,em,field,turn): 
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Rockfall!")        
    al=1
    r=await randroll()
    x.atktype="Rock"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al,w)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121421930738749441/image_search_1687438208400.jpg")        
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Sandstorm"] and a!=0:        
        em.add_field(name="Weather:",value=f"{x.nickname} started a sandstorm!")
        field.weather="Sandstorm"
        tr1.sandturn=turn
        await sandend(tr1,x,y)    
#G-Max Sandblast
async def gmaxsandblast(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Sandblast!")        
    al=1
    r=await randroll()
    x.atktype="Ground"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al,w)             
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Sandstorm"] and a!=0:        
        em.add_field(name="Weather:",value=f"{x.nickname} started a sandstorm!")
        field.weather="Sandstorm"
        tr1.sandturn=turn
        await sandend(tr1,x,y)            
async def sunend(tr1,mon,mon2):
	   if "Heat Rock" not in (mon.item,mon2.item):
	       tr1.sunendturn=tr1.sunturn+5
	   if "Heat Rock" in (mon.item,mon2.item):
	       tr1.sunendturn=tr1.sunturn+8       
#G-Max Fireball
async def gmaxfireball(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Fireball!")        
    al=1
    r=await randroll()
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al,w)       
#Sunny Day
async def sunnyday(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sunny Day!")    
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Sunny"]:
        em.add_field(name="Weather:",value=f"{x.nickname} made the sunlight harsh!")
        field.weather="Sunny"
        tr1.sunturn=turn
        await sunend(tr1,x,y)                 	       
#Max Flare
async def maxflare(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Flare!")        
    al=1
    r=await randroll()
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al,w)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121421664178163793/IMG_20230622_184856.jpg")
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Sunny"] and a!=0:
        em.add_field(name="Weather:",value=f"{x.nickname} made the sunlight harsh!")
        field.weather="Sunny"
        tr1.sunturn=turn
        await sunend(tr1,x,y)         
async def rainend(tr1,mon,mon2):
	   if "Damp Rock" not in (mon.item,mon2.item):
	       tr1.rainendturn=tr1.rainturn+5
	   if "Damp Rock" in (mon.item,mon2.item):
	       tr1.rainendturn=tr1.rainturn+8               
#G-Max Hydrosnipe
async def gmaxhydrosnipe(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Hydrosnipe!")        
    al=1
    r=await randroll()
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al,w)    	       
#G-Max Foam Burst 
async def gmaxfoamburst(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Foam Burst!")        
    al=1
    r=await randroll()
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al,w)  
    if a!=0:
        await speedchange(y,x,-1)
#Rain Dance
async def raindance(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rain Dance!")    
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Rainy"]:
        em.add_field(name="Weather:",value=f"{x.nickname} made it rain!")
        field.weather="Rainy"
        tr1.rainturn=turn
        await rainend(tr1,x,y)           
#Max Geyser
async def maxgeyser(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Geyser!")        
    al=1
    r=await randroll()
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al,w)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121421168122011668/IMG_20230622_184708.jpg")
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Rainy"] and a!=0:
        em.add_field(name="Weather:",value=f"{x.nickname} made it rain!")
        field.weather="Rainy"
        tr1.rainturn=turn
        await rainend(tr1,x,y)     
#Max Airstream
async def maxairstream(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Airstream!")        
    al=1
    r=await randroll()
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    await speedchange(em,x,x,1)    
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121420813313245254/IMG_20230622_184548.jpg")
#Max Ooze
async def maxooze(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Ooze!")        
    al=1
    r=await randroll()
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121420240891416586/IMG_20230622_184328.jpg")
    if a!=0:
        await spatkchange(em,x,x,1)        
#Max Knuckle
async def maxknuckle(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Knuckle!")        
    al=1
    r=await randroll()
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121419893653381190/image_search_1687437729972.png")            
    if a!=0:
        await atkchange(em,x,x,1)        
#Max Flutterby
async def maxflutterby(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Flutterby!")        
    al=1
    r=await randroll()
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    await spatkchange(em,y,x,-1)     
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121419636555137024/IMG_20230622_184102.jpg")   
#Max Wyrmwind
async def maxwyrmwind(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Wyrmwind!")        
    al=1
    r=await randroll()
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121419202763436032/IMG_20230622_183918.jpg")        
    if a!=0:        
        await atkchange(em,y,x,-1)
#Max Darkness
async def maxdarkness(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Darkness!")        
    al=1
    r=await randroll()
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    await spdefchange(em,y,x,-1)      
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1121418698050261002/image_search_1687437439166.png")  
#Max Strike
async def maxstrike(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Strike!")        
    al=1
    r=await randroll()
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1120557015836676297/IMG_20230620_093321.jpg")
    if a!=0:
        await speedchange(em,y,x,-1)
#Max Phantasm
async def maxphantasm(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Phantasm!")        
    al=1
    r=await randroll()
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1120558228535791648/IMG_20230620_093807.jpg")
    if a!=0:
        await defchange(em,y,x,-1)        
#Max Quake
async def maxquake(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Quake!")        
    al=1
    r=await randroll()
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1120554835356418129/IMG_20230620_092439.jpg")
    if a!=0:
        await spdefchange(em,x,x,1)
#Max Steelspike
async def maxsteelspike(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Steelspike!")        
    al=1
    r=await randroll()
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1120555927083417720/IMG_20230620_092840.jpg")
    await defchange(em,x,x,1)        
#Heal Bell
async def healbell(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Heal Bell!")
    em.add_field(name=f"Effect:",value=f"A bell chimed!")
    for i in tr1.pokemons:
        if i.ability!="Soundproof":
            if i.status!="Alive":
                em.add_field(name=f"Effect:",value=f"{i.nickname}'s status condition is cured!")
#Aromatherapy
async def aromatherapy(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aromatherapy!")
    em.add_field(name=f"Effect:",value=f"A bell chimed!")
    for i in tr1.pokemons:
        if i.ability!="Sap Sipper":
            if i.status!="Alive":
                em.add_field(name=f"Effect:",value=f"{i.nickname}'s status condition is cured!")                
#Haze
async def haze(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Haze!")
    x.evasion=0
    y.evasion=0
    x.accuracy=100
    x.atkb=1
    x.defb=1
    x.spatkb=1
    x.spdefb=1
    x.speedb=1
    y.atkb=1
    y.defb=1
    y.spatkb=1
    y.spdefb=1
    y.speedb=1
    em.add_field(name=f"Stats:",value=f"Stat boosts neutralized!")
#Pain Split    
async def painsplit(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Pain Split!")
    x.atktype="Normal"
    em.add_field(name=f"Effect:",value=f"The battlers shared their pain.")
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    if a>0:
        x.hp=y.hp=(y.hp+x.hp)/2
#Endeavor
async def endeavor(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Endeavor!")        
    x.atktype="Normal"
    ab=weakness(x,y,field)
    a=ab[0]
    if a>0 and x.hp<y.hp:
        y.hp=x.hp
#Swords Dance
async def swordsdance(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Swords Dance!")    
    await atkchange(em,x,x,2)
#Dragon Dance
async def dragondance(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Dance!")    
    await atkchange(em,x,x,1)    
    await speedchange(em,x,x,1)    
#Acid Armor
async def acidarmor(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Acid Armor!")    
    await defchange(em,x,x,2)
    
#Iron Defense
async def irondefense(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Iron Defense!")    
    await defchange(em,x,x,2)           
    
#Amnesia
async def amnesia(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Amnesia!")    
    await spdefchange(em,x,x,2)

#Cotton Guard
async def cottonguard(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Cotton Guard!")    
    await defchange(em,x,x,3)        
    
#Cosmic Powet
async def cosmicpower(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Cosmic Power!")    
    await defchange(em,x,x,1)
    await spdefchange(em,x,x,1)    
    
#Agility
async def agility(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Agility!")    
    await speedchange(em,x,x,2)
    
#Rock Polish
async def rockpolish(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rock Polish!")    
    await speedchange(em,x,x,2)    
        
#Shelter
async def shelter(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shelter!")    
    await defchange(em,x,x,2)    
#Calm Mind
async def calmmind(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Calm Mind!")    
    await spatkchange(em,x,x,1)    
    await spdefchange(em,x,x,1)     
#Quiver Dance
async def quiverdance(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Quiver Dance!")    
    await spatkchange(em,x,x,1)    
    await spdefchange(em,x,x,1)         
    await speedchange(em,x,x,1)
#Victory Dance
async def victorydance(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Victory Dance!")    
    await atkchange(em,x,x,1)    
    await defchange(em,x,x,1)         
    await speedchange(em,x,x,1)    
#Shell Smash
async def shellsmash(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shell Smash!")    
    await atkchange(em,x,x,1)
    await defchange(em,x,x,-1)
    await spatkchange(em,x,x,1)    
    await spdefchange(em,x,x,-1)         
    await speedchange(em,x,x,1)    
#Bulk Up
async def bulkup(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bulk Up!")    
    await atkchange(em,x,x,1)    
    await defchange(em,x,x,1)   
#Growth
async def growth(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Growth!")    
    await atkchange(em,x,x,1)    
    await spatkchange(em,x,x,1)       
#Curse
async def curse(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Curse!")    
    await atkchange(em,x,x,1)    
    await defchange(em,x,x,1)        
    await speedchange(em,x,x,-1)        
#Nasty Plot
async def nastyplot(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Nasty Plot!")    
    await spatkchange(em,x,x,2)    
#Tail Glow
async def tailglow(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Tail Glow!")    
    await spatkchange(em,x,x,3)        
#Charge
async def charge(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Charge!")
    await spdefchange(em,x,x,1)
    x.charged=True
#Needle Arm
async def needlearm(ctx,x,y,tr1,em,field,turn):
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
async def explosion(ctx,x,y,tr1,em,field,turn):
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
async def mistyexplosion(ctx,x,y,tr1,em,field,turn):
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
async def meteormash(ctx,x,y,tr1,em,field,turn):
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
        await atkchange(em,x,x,1)  
#Thunder Fang
async def thunderfang(ctx,x,y,tr1,em,field,turn):
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
async def icefang(ctx,x,y,tr1,em,field,turn):
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
async def psychicfangs(ctx,x,y,tr1,em,field,turn):
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
async def poisonfang(ctx,x,y,tr1,em,field,turn):
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
async def firefang(ctx,x,y,tr1,em,field,turn):
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
#Rapid Spin
async def rapidspin(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rapid Spin!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,20,a,b,c,r,al)        
    await speedchange(em,x,x,1)
    if len(tr1.hazard)>0:
        tr1.hazard=[]
#Crunch
async def crunch(ctx,x,y,tr1,em,field,turn):
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
        await defchange(em,y,x,-1)       
#Heat Crash
async def heatcrash(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Heat Crash!")          
    al=1
    r=await randroll()   
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1] 
    if x.ability=="Light Metal":
        al*=0.5
    elif x.ability=="Heavy Metal":
        al*=2
    base=(y.weight/x.weight)*100
    if base>50:
        base=40
    if 50>=base>=33.35:
        base=60
    if 33.34>=base>=25.01:
        base=80
    if 25>base>=20.01:
        base=100
    if 20>base:
        base=120
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al,w)               
#Heavy Slam
async def heavyslam(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Heavy Slam!")          
    al=1
    r=await randroll()   
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1] 
    if x.ability=="Light Metal":
        al*=0.5
    elif x.ability=="Heavy Metal":
        al*=2
    base=(y.weight/x.weight)*100
    if base>50:
        base=40
    if 50>=base>=33.35:
        base=60
    if 33.34>=base>=25.01:
        base=80
    if 25>base>=20.01:
        base=100
    if 20>base:
        base=120
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)                   
#Spirit Break
async def spiritbreak(ctx,x,y,tr1,em,field,turn):
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
        await spatkchange(em,y,x,-1)    
#False Surrender
async def falsesurrender(ctx,x,y,tr1,em,field,turn):
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
async def rocktomb(ctx,x,y,tr1,em,field,turn):
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
        await speedchange(em,y,x,-1)     
#Magnitude
async def magnitude(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    mag=random.choices([4,5,6,7,8,9,10],weights=[5,10,20,30,20,10,5],k=1)[0]
    em.add_field(name=f"Move:",value=f"{x.nickname} used Magnitude {mag}!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if field.terrain=="Grassy":
        al*=0.5
    if mag<10:
        base=10+(20*mag-4)   
    if mag==10:
        base=150
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)            
#Breaking Swipe
async def breakingswipe(ctx,x,y,tr1,em,field,turn):
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
        await atkchange(em,y,x,-1)  
#Gunk Shot
async def gunkshot(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Gunk Shot!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)          
    #poison
#Belch
async def belch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Belch!")    
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if "Berry[Used]" in x.item:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)      
#Poison Jab
async def poisonjab(ctx,x,y,tr1,em,field,turn):
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
async def poisontail(ctx,x,y,tr1,em,field,turn):
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
async def dragonhammer(ctx,x,y,tr1,em,field,turn):
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
async def zenheadbutt(ctx,x,y,tr1,em,field,turn):
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
async def ironhead(ctx,x,y,tr1,em,field,turn):
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
#Gyro Ball
async def gyroball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Gyro Ball!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=round(1+25*(y.speed/x.speed))
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)        
#Iron Tail
async def irontail(ctx,x,y,tr1,em,field,turn):
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
async def grassyglide(ctx,x,y,tr1,em,field,turn):
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
async def drumbeating(ctx,x,y,tr1,em,field,turn):
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
async def icehammer(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Hammer!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)     
    await speedchange(em,x,x,-1)
#U-turn
async def uturn(ctx,x,y,tr1,em,field,turn):
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
async def flipturn(ctx,x,y,tr1,em,field,turn):
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
async def hammerarm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hammer Arm!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)     
    await speedchange(em,x,x,-1)    
#Play Rough
async def playrough(ctx,x,y,tr1,em,field,turn):
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
        await atkchange(em,y,x,-1)  
#Thunder Wave
async def thunderwave(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder Wave!")
    y.status="Paralyzed"
    #needs work 
#Toxic
async def toxic(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Toxic!")
    y.status="Badly Poisoned"
    #needs work             
#Will-O-Wisp
async def willowisp(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Will-O-Wisp!")
    y.status="Burned"
    #needs work 
#Gigaton Hammer
async def gigatonhammer(ctx,x,y,tr1,em,field,turn):
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
async def glaciallance(ctx,x,y,tr1,em,field,turn):
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
async def superpower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Superpower!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)        
    await atkchange(em,x,x,-1)
    await defchange(em,x,x,-1)    
#High Jump Kick
async def highjumpkick(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used High Jump Kick!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)            
#Armor Cannon
async def armorcannon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Armor Cannon!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al,w)        
    if a!=0:
        await defchange(em,x,x,-1)
        await spdefchange(em,x,x,-1)    
#Headlong Rush
async def headlongrush(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Headlong Rush!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)        
    if a!=0:
        await defchange(em,x,x,-1)
        await spdefchange(em,x,x,-1)    
#Close Combat
async def closecombat(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Close Combat!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)        
    if a!=0:
        await defchange(em,x,x,-1)
        await spdefchange(em,x,x,-1)
#Avalanche
async def avalanche(ctx,x,y,tr1,em,field,turn):
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
async def iciclecrash(ctx,x,y,tr1,em,field,turn):
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
async def icespinner(ctx,x,y,tr1,em,field,turn):
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
async def orderup(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Order Up!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)  
#Shadow Sneak
async def shadowsneak(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shadow Sneak!")    
    x.atktype="Ghost"
    base=40
    if x.ability=="Technician":
        base*=1.5
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)      
#Bullet Punch
async def bulletpunch(ctx,x,y,tr1,em,field,turn):
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
async def machpunch(ctx,x,y,tr1,em,field,turn):
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
async def iceshard(ctx,x,y,tr1,em,field,turn):
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
async def aquajet(ctx,x,y,tr1,em,field,turn):
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
async def jetpunch(ctx,x,y,tr1,em,field,turn):
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
async def plasmafists(ctx,x,y,tr1,em,field,turn):
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
async def boltstrike(ctx,x,y,tr1,em,field,turn):
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
async def icepunch(ctx,x,y,tr1,em,field,turn):
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
async def firepunch(ctx,x,y,tr1,em,field,turn):
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
#Fire Lash
async def firelash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Lash!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al,w)             
    await defchange(em,y,x,-1)
#Wood Hammer
async def woodhammer(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Wood Hammer!")    
    x.atktype="Grass"
    if x.ability=="Reckless":
        al*=1.2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)             
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!") 
#Double-Edge
async def doubeedge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Double-Edge!")    
    x.atktype="Normal"
    if x.ability=="Reckless":
        al*=1.2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)             
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")         
#Brave Bird
async def bravebird(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Brave Bird!")    
    x.atktype="Flying"
    if x.ability=="Reckless":
        al*=1.2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)             
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!") 
#Head Smash
async def headsmash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Head Smash!")    
    x.atktype="Rock"
    if x.ability=="Reckless":
        al*=1.2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)             
    y.hp-=dmg
    recoil=dmg/2
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")         
#Acrobatics
async def acrobatics(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Acrobatics!")    
    x.atktype="Flying"
    if x.item=="None" or "Used" in x.item:
        al*=2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,55,a,b,c,r,al)             
    y.hp-=dmg              
#Energy Ball
async def energyball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Energy Ball!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)               
    #spdef drop
#Liquidation
async def liquidation(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Liquidation!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al,w)        
    #defdrop
#Wave Crash
async def wavecrash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Wave Crash!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    if x.ability=="Reckless":
        al*=1.2
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
#Wood Hammer
async def woodhammer(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Wood Hammer!")    
    x.atktype="Grass"
    if x.ability=="Reckless":
        al*=1.2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)             
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")        
#Volt Tackle
async def volttackle(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Volt Tackle!")    
    x.atktype="Electric"
    if x.ability=="Reckless":
        al*=1.2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)             
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")              
    #paralyze              
#Wave Crash
async def wavecrash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Wave Crash!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    if x.ability=="Reckless":
        al*=1.2
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
#Flare Blitz
async def flareblitz(ctx,x,y,tr1,em,field,turn):
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
async def thunderpunch(ctx,x,y,tr1,em,field,turn):
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
#Bolt Strike
async def boltstrike(ctx,x,y,tr1,em,field,turn):
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
#Fusion Bolt
async def fusionbolt(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fusion Bolt!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)         
#Extreme Speed
async def extremespeed(ctx,x,y,tr1,em,field,turn):
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
async def suckerpunch(ctx,x,y,tr1,em,field,turn):
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
async def outrage(ctx,x,y,tr1,em,field,turn):
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
#Return
async def returm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Return!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]       
    base=round(255*(2/5))
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)     
#Facade
async def facade(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Facade!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.status!="Alive":
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)       
#Body Press
async def bodypress(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Body Press!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.defense,y.defense,80,a,b,c,r,al)       
#Body Slam
async def bodyslam(ctx,x,y,tr1,em,field,turn):
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
async def kowtowcleave(ctx,x,y,tr1,em,field,turn):
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
async def shadowclaw(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shadow Claw!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)   
#Power Whip
async def powerwhip(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Power Whip!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)        
#Crush Claw
async def crushclaw(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Crush Claw!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)         
    #defense drop
#Spin Out
async def spinout(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Spin Out!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)         
    await speedchange(em,x,x,-2)
#Seed Bomb
async def seedbomb(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Seed Bomb!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)         
#Knock Off
async def knockoff(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Knock Off!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=65
    if "Used" not in y.item and y.item not in megastones and "m-Z" not in y.item and "None" not in y.item:
        em.add_field(name="Effect:",value=f"{x.nickname} knocked off {y.nickname}'s {y.item}!")  
        base*=2
        y.item+="[Used]"
    if x.ability=="Technician":
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)        
#Astral Barrage
async def astralbarrage(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Astral Barrage!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,130,a,b,c,r,al)           
#Last Respects
async def lastrespects(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Last Respects!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=50+(50*(6-len(tr1.pokemons))) 
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)         
#Dragon Claw    
async def dragonclaw(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Claw!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al) 
#Meteor Beam
async def meteorbeam(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Meteor Beam!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            await spatkchange(em,x,x,1)
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Rock"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} is overflowing with space power!") 
        await spatkchange(em,x,x,1)
        x.precharge=True        
#Phantom Force
async def phantomforce(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Phantom Force!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Ghost"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} vanished instantly!") 
        x.precharge=True        
#Sky Attack
async def skyattack(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sky Attack!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Flying"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,150,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} became cloaked in a harsh light!") 
        x.precharge=True                          
#Stone Edge    
async def stoneedge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Stone Edge!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)   
#Rock Slide
async def rockslide(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rock Slide!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al)         
    #flinch
#Slash
async def slash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Slash!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)       
#Cross Chop 
async def crosschop(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Cross Chop!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)       
#Cross Poison
async def crosspoison(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Cross Poison!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)       
    #poison
#Aqua Cutter
async def aquacutter(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aqua Cutter!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al,w)       
#Waterfall
async def waterfall(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Waterfall!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al,w)           
    #flinch
#Crabhammer
async def crabhammer(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Crabhammer!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al,w)        
#Night Slash
async def nightslash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Night Slash!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)       
#Psycho Cut
async def psychocut(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psycho Cut!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Psycho"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)     
#Wicked Blow
async def wickedblow(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Wicked Blow!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y,16)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)   
#Storm Throw
async def stormthrow(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Storm Throw!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y,16)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)         
#Leaf Blade
async def leafblade(ctx,x,y,tr1,em,field,turn):
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
#Flower Trick
async def flowertrick(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flower Trick!")
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y,16)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)       
#Dual Chop
async def dualchop(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dual Chop!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,40,a,b,c,r,al)       
#Dual Wingbeat
async def dualwingbeat(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dual Wingbeat!")    
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,40,a,b,c,r,al)    
#X-Scissor
async def xscissor(ctx,x,y,tr1,em,field,turn):
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
async def megahorn(ctx,x,y,tr1,em,field,turn):
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
async def drillpeck(ctx,x,y,tr1,em,field,turn):
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
async def earthquake(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Earthquake!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if field.terrain=="Grassy":
        al*=0.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)      
#High Horsepower
async def highhorsepower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used High Horsepower!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,95,a,b,c,r,al)       
#Stomping Tantrum
async def stompingtantrum(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Stomping Tantrum!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.miss==True:
        al*=2
    if x.ability=="Striker":
        al*=1.3
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)       
#Bulldoze
async def bulldoze(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bulldoze!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,65,a,b,c,r,al)      
    await speedchange(em,y,x,-1)
#Ice Beam
async def icebeam(ctx,x,y,tr1,em,field,turn):
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
#Earth Power
async def earthpower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Earth Power!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)  
    #defense drop
#Freeze-Dry
async def freezedry(ctx,x,y,tr1,em,field,turn):
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
async def extrasensory(ctx,x,y,tr1,em,field,turn):
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
#Lumina Crash
async def luminacrash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Lumina Crash!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)     
    if a!=0:
        await spdefchange(em,y,x,-2)
#Luster Purge 
async def lusterpurge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Luster Purge!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    #drop
#Mist Ball
async def mistball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Mist Ball!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    #drop    
#Psyshock
async def psyshock(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psyshock!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.defense,80,a,b,c,r,al)  
#Psystrike
async def psystrike(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psystrike!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.defense,100,a,b,c,r,al)          
#Freezing Glare
async def freezingglare(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Freezing Glare!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    #freeze
#Expanding Force
async def expandingforce(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Expanding Force!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if field.terrain=="Psychic":
        al*=1.5
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)     
#Rising Voltage
async def risingvoltage(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} Rising Voltage!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if field.terrain=="Electric":
        al*=1.5
    y.hp-=await special(x,x.level,x.spatk,y.spdef,70,a,b,c,r,al)          
#Focus Blast
async def focusblast(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Focus Blast!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)      
    #spdef drop
#Mystical Power
async def mysticalpower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Mystical power!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,70,a,b,c,r,al)      
    if a!=0:
        await spatkchange(em,x,x,1)
#Psychic   
async def psychic(ctx,x,y,tr1,em,field,turn):
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
            await spdefchange(em,y,x,-1)    
#Roost
async def roost(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Roost!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")            
#Slack Off
async def slackoff(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Slack Off!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")            
#Milk Drink
async def milkdrink(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Milk Drink!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")      
#Jungle Healing
async def junglehealing(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Jungle Healing!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")            
#Soft-Boiled
async def softboiled(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Soft-Boiled!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")           
#Heal Order
async def healorder(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Heal Order!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")         
#Hyper Beam
async def hyperbeam(ctx,x,y,tr1,em,field,turn):
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
async def prismaticlaser(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Prismatic Laser!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al)                 
#Leaf Tornado
async def leaftornado(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Leaf Tornado!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al)      
#Grass Knot
async def grassknot(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Grass Knot!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    wgt=y.weight
    if y.ability=="Light Metal":
        wgt*=0.5
    if y.ability=="Heavy Metal":
        wgt*=2
    if 0.1<=wgt<=21.8:
        base=20
    if 21.9<=wgt<=54.9:
        base=40
    if 55.1<=wgt<=110:
        base=60
    if 110.2<=wgt<=220.2:
        base=80
    if 220.4<=wgt<=440.7:
        base=100
    if wgt>=440.9:
        base=120
    y.hp-=await special(x,x.level,x.spatk,y.spdef,base,a,b,c,r,al)          
#Leaf Storm
async def leafstorm(ctx,x,y,tr1,em,field,turn):
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
        await spatkchange(em,x,x,-2)
#Oblivion Wing
async def oblivionwing(ctx,x,y,tr1,em,field,turn):
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
#G-Max Drumsolo
async def gmaxdrumsolo(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Drumsolo!")        
    al=1
    r=await randroll()
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
#Max Overgrowth
async def maxovergrowth(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Overgrowth!")        
    al=1
    r=await randroll()
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)    
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1120385791156306050/IMG_20230619_221256.jpg")
    if field.terrain!="Grassy":
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(x,y)
        em.add_field(name="Grassy Terrain",value="Grass grew to cover the battlefield!")        
#Grassy Terrain
async def grassyterrain(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Grassy Terrain!")        
    if field.terrain!="Grassy":
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(x,y)
        em.add_field(name="Grassy Terrain",value="Grass grew to cover the battlefield!")
#Max Starfall
async def maxstarfall(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Starfall!")        
    al=1
    r=await randroll()
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://archives.bulbagarden.net/media/upload/d/d9/Marnie_Grimmsnarl_Max_Starfall.png")        
    if field.terrain!="Misty":
        field.terrain="Misty"
        field.misturn=turn
        field.misend(x,y)
        em.add_field(name="Misty Terrain",value="Mist swirled around the battlefield!")        
#Misty Terrain
async def mistyterrain(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Misty Terrain!")        
    if field.terrain!="Misty":
        field.terrain="Misty"
        field.misturn=turn
        field.misend(x,y)
        em.add_field(name="Misty Terrain",value="Mist swirled around the battlefield!")        
#Max Mindstorm
async def maxmindstorm(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Mindstorm!")        
    al=1
    r=await randroll()
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1120553436409237644/IMG_20230620_091852.jpg")
    if field.terrain!="Psychic":
        field.terrain="Psychic"
        field.psyturn=turn
        field.psyend(x,y)
        em.add_field(name="Psychic Terrain",value="The battlefield got weird!")        
#Psychic Terrain
async def psychicterrain(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psychic Terrain!")        
    if field.terrain!="Psychic":
        field.terrain="Psychic"
        field.psyturn=turn
        field.psyend(x,y)
        em.add_field(name="Psychic Terrain",value="The battlefield got weird!")
#Max Lightning
async def maxlightning(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Lightning!")        
    al=1
    r=await randroll()
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,150,a,b,c,r,al)            
    em.set_image(url="https://static.wikia.nocookie.net/pokemon/images/9/9a/Max_Lightning.png/revision/latest?cb=20190819011058")             
    if field.terrain!="Electric":
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(x,y)
        em.add_field(name="Electric Terrain",value="An electric current ran across the battlefield!")
#Electric Terrain
async def electricterrain(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Electric Terrain!")
    if field.terrain!="Electric":
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(x,y)
        em.add_field(name="Electric Terrain",value="An electric current ran across the battlefield!")
#Dream Eater
async def dreameater(ctx,x,y,tr1,em,field,turn):
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
#Leech Life
async def leechlife(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Leech Life!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,70,a,b,c,r,al)          
    y.hp-=dmg
    heal=dmg/2
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        x.hp-=heal
    else:
        x.hp+=heal            
#Drain Punch
async def drainpunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Drain Punch!")    
    x.atktype="Fighting"
    base=70
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)              
    y.hp-=dmg
    heal=dmg/2
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and a!=0:
        x.hp-=heal
    else:
        x.hp+=heal 
#Giga Drain
async def gigadrain(ctx,x,y,tr1,em,field,turn):
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
async def dracometeor(ctx,x,y,tr1,em,field,turn):
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
        await spatkchange(em,x,x,-2)        
#Make It Rain
async def makeitrain(ctx,x,y,tr1,em,field,turn):
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
        await spatkchange(em,x,x,-1)        
#Recover
async def recover(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Recover!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    if x.hp==x.maxhp:
        pass
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
#Strange Steam
async def strangesteam(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Strange Steam!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)             
    #confuse   
#Psycho Boost
async def psychoboost(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psycho Boost!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,140,a,b,c,r,al)        
    if a!=0:
        spatkchange(em,x,x,-1)
#Fleur Cannon
async def fleurcannon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fleur Cannon!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,130,a,b,c,r,al)        
    await spdefchange(em,y,x,-1)
#Moonblast
async def moonblast(ctx,x,y,tr1,em,field,turn):
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
    
#Dazzling Gleam
async def dazzlinggleam(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dazzling Gleam!")    
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)             
#Aura Sphere
async def aurasphere(ctx,x,y,tr1,em,field,turn):
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
#Hurricane
async def hurricane(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hurricane!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al)    
    #confuse 
#Air Slash
async def airslash(ctx,x,y,tr1,em,field,turn):
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
async def scald(ctx,x,y,tr1,em,field,turn):
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
async def voltswitch(ctx,x,y,tr1,em,field,turn):
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
async def thunderbolt(ctx,x,y,tr1,em,field,turn):
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
async def thunder(ctx,x,y,tr1,em,field,turn):
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
async def risingvoltage(ctx,x,y,tr1,em,field,turn):
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
async def powergem(ctx,x,y,tr1,em,field,turn):
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
async def heatwave(ctx,x,y,tr1,em,field,turn):
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
async def boomburst(ctx,x,y,tr1,em,field,turn):
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
async def blizzard(ctx,x,y,tr1,em,field,turn):
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
async def sacredfire(ctx,x,y,tr1,em,field,turn):
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
#Muddy Water
async def muddywater(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Muddy Water!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al,w)      
    #accuracy drop
#Surf
async def surf(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Surf!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al,w)       
    if x.ability=="Gulp Missile" and a!=0:
        n=""
        if x.hp<=(x.maxhp/2):
            n="Pikachu"
            x.sprite="https://play.pokemonshowdown.com/sprites/ani/cramorant-gorging.gif"
        if x.hp>(x.maxhp/2):
            n="Arrokuda"
            x.sprite="https://play.pokemonshowdown.com/sprites/ani/cramorant-gulping.gif"
        x.ability+=f"-{n}"
        em.add_field(name=f"Effect:",value=f"{x.nickname} caught a {n}!")
#Hydro Pump     
async def hydropump(ctx,x,y,tr1,em,field,turn):
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
async def originpulse(ctx,x,y,tr1,em,field,turn):
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
async def scorchingsands(ctx,x,y,tr1,em,field,turn):
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
#Venoshock 
async def venoshock(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Venoshock!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Poison"
    if y.status in ["Poisoned","Badly Poisoned"]:
        al*=2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,65,a,b,c,r,al)          
#Sludge Bomb 
async def sludgebomb(ctx,x,y,tr1,em,field,turn):
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
async def darkpulse(ctx,x,y,tr1,em,field,turn):
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
#Final Gambit
async def finalgambit(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Final Gambit!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    y.hp-=x.hp
    x.hp=0
#Torch Song
async def torchsong(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Torch Song!")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al,w)      
    if a!=0:
        await spatkchange(em,x,x,1)
#Flamethrower
async def flamethrower(ctx,x,y,tr1,em,field,turn):
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
#Fusion Flare
async def fusionflare(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fusion Flate!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)       
#Fiery Wrath
async def fierywrath(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fiery Wrath!")    
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
#V-Create
async def vcreate(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used V-create!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,180,a,b,c,r,al,w)     
    if a!=0:
        await defchange(em,x,x,-1)
        await spdefchange(em,x,x,-1)
        await speedchange(em,x,x,-1)
#Searing Shot
async def searingshot(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Searing Shot!")    
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
#Fire Blast
async def fireblast(ctx,x,y,tr1,em,field,turn):
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
#Overheat
async def overheat(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Oberheat!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,130,a,b,c,r,al,w)         
    if a!=0:
        await spatkchange(em,x,x,-2)
#Blast Burn
async def blastburn(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Blast Burn!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al,w)             
    #burn
#Hydro Cannon
async def hydrocannon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hydro Cannon!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al,w)             
    #freeze
#Sparkling Aria
async def sparklingaria(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sparkling Aria!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)             
    if y.status=="Burned":
        y.status="Alive"
#Frenzy Plant
async def frenzyplant(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Frenzy Plant!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al)             
    #poison
#Lava Plume
async def lavaplume(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Lava Plume!")    
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
#Pyro Ball
async def pyroball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Pyro Ball!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al,w)     
    #burn        
#Flash Cannon
async def flashcannon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flash Cannon!")    
    if x.ability=="Mega Launcher":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Mega Launcher!",value="")
    elif x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    #spdefdrop
#Shadow Ball            
async def shadowball(ctx,x,y,tr1,em,field,turn):
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
            await spdefchange(em,y,x,-1)
#Esper Wing
async def esperwing(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Esper Wing!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)              
    if a!=0:
        await speedchange(em,x,x,1)
#Bug Buzz            
async def bugbuzz(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bug Buzz!")    
    if x.ability=="Sheer Force":
        al=1.5
        em.add_field(name=f"{x.nickname}'s Sheer Force!",value="")
    x.atktype="Bug"
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
            await spdefchange(em,y,x,-1)            
#Psych Up
async def psychup(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psych Up!") 
    x.atkb=y.atkb
    x.defb=y.defb
    x.spatkb=y.spatkb
    x.spdefb=y.spdefb
    x.speedb=y.speedb
#Perish Song    
async def perishsong(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Perish Song!") 
    if 0 in (x.perishturn,y.perishturn):
        em.add_field(name=f"Move Effect:",value=f"All Pokéx that heard the song will faint in three turns!")
    if x.perishturn==0 and x.ability!="Soundproof":
        x.perishturn=4
    if y.perishturn==0 and y.ability!="Soundproof":
        y.perishturn=4          
#Acupressure                     
async def acupressure(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Acupressure!")
    m=random.randint(1,5)
    if m==1:
        await atkchange(em,x,x,2)
    if m==2:
        await defchange(em,x,x,2)
    if m==3:
        await spatkchange(em,x,x,2)
    if m==4:
        await spdefchange(em,x,x,2)
    if m==5:
        await speedchange(em,x,x,2)
#Psycho Shift
async def psychoshift(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psycho Shift!")
    if y.status=="Alive" and x.status!="Alive":
        x.status,y,status=y.status,x.status
        em.add_field(name=f"Move Effect:",value=f"{x.nickname} shifted it's status condition to {y.name}!")
#Flail
async def flail(ctx,x,y,tr1,em,field,turn):
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
    y.hp-=physical(x,x.level,x.atk,y.defense,dmg,a,b,c,r,al)
#Reversal
async def reversal(ctx,x,y,tr1,em,field,turn):
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
        return 1.5
    if (field.weather=="Sunny") and x.atktype=="Water" and "Cloud Nine" not in (x.ability,y.ability):
        return 0.5    
    if (field.weather=="Rainy") and x.atktype=="Fire" and "Cloud Nine" not in (x.ability,y.ability):
        return 0.5      
    if field.weather in ["Sunny" ,"Extreme Sunlight"] and x.atktype=="Fire" and "Cloud Nine" not in (x.ability,y.ability):
        if "Koraidon" in x.name:
            return 2
        else:
            return 1.5        
    else:
        return 1     