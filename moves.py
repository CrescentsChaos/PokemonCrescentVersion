from typematchup import *
from status import *
megastones=("Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Ampharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite")
#Corrosive Gas
async def corrosivegas(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Corrosive Gas!")    
    em.add_field(name="Effect:",value=f"{x.nickname}'s corrosive gas melted {y.nickname}'s {await itemicon(y.item)} {y.item}!") 
    y.item+="[Used]"
#Trop Kick
async def tropkick(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Trop Kick!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)     
    if a!=0:
        await atkchange(em,y,x,-1)
#Smelling Salts
async def smellingsalts(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Smelling Salts!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.status=="Paralyzed":
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)        
    if y.status=="Paralyzed" and a!=0:
        y.status="Alive"     
#Spirit Shackle
async def spiritshackle(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Spirit Shackle!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)             
    if a!=0 and y.item!="Covert Cloak":
        await flinch(em,x,y,20)
        x.trap=True
#Thunderous Kick
async def thunderouskick(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunderous Kick!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al) 
    ch=random.randint(1,100)
    chance=20
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance and a!=0:
        await defchange(em,y,x,-1)
#Defog
async def defog(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Defog!")
    if len(tr1.hazard)!=0:
        tr1.hazard=[]
        em.add_field(name="Effect:",value=f"{x.nickname} blew away all the hazard!")
    if field.terrain!="Normal":
        field.terrain="Normal"
        em.add_field(name="Effect:",value=f"{x.nickname} blew away the terrain effects!")
#Venom Drench
async def venomdrench(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Venom Drench!")
    if "Poisoned" in x.status:
        await atkchange(em,y,x,-1)
        await spatkchange(em,y,x,-1)
        await speedchange(em,y,x,-1)
#Destiny Bond
async def destinybond(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Destiny Bond!")
    if y.dbond==True:
        em.add_field(name="Effect:",value="It failed!")
    if y.dbond!=True:
        y.dbond=True 
        em.add_field(name="Effect:",value=f"{x.nickname} is hoping to take its attacker down with it!")
#Mirror Coat
async def mirrorcoat(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Mirror Coat!")
    if y.atkcat=="Special" and "Dark" not in (y.primaryType,y.secondaryType,y.teraType):
        y.hp-=x.dmgtaken*2
    else:
        em.add_field(name="Effect:",value="It failed.")
#Counter
async def counter(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Counter!")
    if y.atkcat=="Physical" and "Ghost" not in (y.primaryType,y.secondaryType,y.teraType):
        y.hp-=x.dmgtaken*2
    else:
        em.add_field(name="Effect:",value="It failed.")
#Sheer Cold
async def sheercold(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sheer Cold!")
    x.atktype=="Ice"
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    if a!=0:
        y.hp-=y.hp
        em.add_field(name="Effect:",value="It's a one-hit KO!")
#Fissure
async def fissure(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fissure!")
    x.atktype=="Ground"
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    if a!=0:
        y.hp-=y.hp
        em.add_field(name="Effect:",value="It's a one-hit KO!")
#Horn Drill
async def horndrill(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Horn Drill!")
    x.atktype=="Normal"
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    if a!=0:
        y.hp-=y.hp
        em.add_field(name="Effect:",value="It's a one-hit KO!")
#Guillotine
async def guillotine(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Guillotine!")
    x.atktype=="Normal"
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    if a!=0:
        y.hp-=y.hp
        em.add_field(name="Effect:",value="It's a one-hit KO!")        
#Trick Room
async def trickroom(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Trick Room!")
    if field.trickroom is False:
        field.trickroom=True
        field.troomturn=turn
        field.troomend(x,y)
        em.add_field(name="Trick Room:",value=f"{x.nickname} twisted the dimensions!")
    elif field.trickroom is True:
        field.trickroom=False
        field.troomendturn=-1
        em.add_field(name="Trick Room:",value=f"{x.nickname} twisted the dimensions!")
#Taunt
async def taunt(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Taunt!")
    if y.taunted=="False":
        y.taunturn=turn+random.choice(2,5)
        y.taunted=True
#Confuse Ray
async def confuseray(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Confuse Ray!")        
    await confuse(em,x,y,100)
#Sweet Kiss
async def sweetkiss(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sweet Kiss!")        
    await confuse(em,x,y,100)    
#Lovely Kiss
async def lovelykiss(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Lovely Kiss!")        
    await sleep(em,x,y,100)        
#Tailwind
async def tailwind(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Tailwind!")
    if tr1.tailwind is True:
        em.add_field(name="Tailwind:",value="Nothing happened!")
    if tr1.tailwind is False:
        tr1.tailturn=turn
        tr1.twend(x,y)
        tr1.tailwind=True  
        em.add_field(name="Tailwind:",value="The Tailwind blew from behind your team.")
#Aurora Veil
async def auroraveil(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aurora Veil!")
    if tr1.auroraveil is True or field.weather not in ["Hail","Snowstorm"]:
        em.add_field(name=f"Aurora Veil:",value="Nothing happened!")
    if tr1.auroraveil is False and field.weather in ["Hail","Snowstorm"]:
        tr1.auroraturn=turn
        tr1.auroraend(x,y)
        tr1.auroraveil=True  
        em.add_field(name=f"Aurora Veil:",value="Aurora Veil will reduced your team's damage taken!")
#Reflect
async def reflect(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Reflect!")
    if tr1.reflect is True:
        em.add_field(name=f"Reflect:",value="Nothing happened!")
    elif tr1.reflect is False:
        tr1.reflecturn=turn
        tr1.reflectend(x,y)
        tr1.reflect=True  
        em.add_field(name=f"Reflect:",value="Reflect raised your team's Defense!")
#Light Screen
async def lightscreen(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Light Screen!")
    if tr1.lightscreen is True:
        em.add_field(name=f"Light Screen:",value="Nothing happened!")
    elif tr1.lightscreen is False:
        tr1.lightscreen=True
        em.add_field(name=f"Light Screen:",value="Light Screen raised your team's Special Defense!")
        tr1.lsturn=turn
        tr1.lightscreenend(x,y)
#Toxic Spikes
async def toxicspikes(ctx,x,y,tr1,tr2,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Toxic Spikes!")
    if tr2.hazard.count("Toxic Spikes")==3:
        em.add_field(name=f"Toxic Spikes:",value="Nothing happened!")
    elif tr2.hazard.count("Toxic Spikes")<3 and y.ability!="Magic Bounce":
        tr2.hazard.append("Toxic Spikes")
        em.add_field(name=f"Toxic Spikes:",value="Poison spikes were scattered all around the opposing team!")
    elif tr1.hazard.count("Toxic Spikes")<3 and y.ability=="Magic Bounce":
        tr1.hazard.append("Toxic Spikes")
        em.add_field(name="Toxic Spikes:",value="Poison spikes were scattered all around the ally team!")
#Spikes
async def spikes(ctx,x,y,tr1,tr2,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Spikes!")
    if tr2.hazard.count("Spikes")==3:
        em.add_field(name=f"Spikes:",value="Nothing happened!")
    elif tr2.hazard.count("Spikes")<3 and y.ability!="Magic Bounce":
        tr2.hazard.append("Spikes")
        em.add_field(name=f"Spikes:",value="Spikes were scattered all around the opposing team!")
    elif tr1.hazard.count("Spikes")<3 and y.ability=="Magic Bounce":
        tr1.hazard.append("Spikes")
        em.add_field(name=f"Spikes:",value="Spikes were scattered all around the ally team!")
#Sticky Web
async def stickyweb(ctx,x,y,tr1,tr2,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sticky Web!")
    if "Sticky Web" in tr2.hazard:
        em.add_field(name=f"Sticky Web:",value="Nothing happened!")
    elif "Sticky Web" not in tr2.hazard and y.ability!="Magic Bounce":
        tr2.hazard.append("Sticky Web")
        em.add_field(name=f"Sticky Web:",value="A sticky web spreads out in the ground around the opposing team!")
    elif "Sticky Web" not in tr1.hazard and y.ability=="Magic Bounce":
        tr1.hazard.append("Sticky Web")
        em.add_field(name=f"Sticky Web:",value="A sticky web spreads out in the ground around the ally team!")
#Stealth Rock
async def stealthrock(ctx,x,y,tr1,tr2,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Stealth Rock!")
    if "Stealth Rock" in tr2.hazard:
        em.add_field(name=f"Stealth Rock:",value="Nothing happened!")
    elif "Stealth Rock" not in tr2.hazard and y.ability!="Magic Bounce":
        tr2.hazard.append("Stealth Rock")
        em.add_field(name=f"Stealth Rock:",value="Pointed stones float in the air around the opposing team!")
    elif "Stealth Rock" not in tr1.hazard and y.ability=="Magic Bounce":
        tr1.hazard.append("Stealth Rock")
        em.add_field(name=f"Stealth Rock:",value="Pointed stones float in the air around the ally team!")
#Shed Tail
async def shedtail(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shed Tail!")
    if x.hp<(x.maxhp/2) or tr1.sub!="None":
        em.add_field(name="Substitute:",value=f"It failed!")
    elif x.hp>(x.maxhp/2) and tr1.sub=="None":
        em.add_field(name="Substitute:",value=f"{x.nickname} created a substitute!")
        x.hp-=x.maxhp/2
        tr1.sub=Pokemon(name="Substitute",moves='["A","B","C","D"]',primaryType=x.primaryType,secondaryType=x.secondaryType)
        tr1.sub.hp=x.maxhp/2
        tr1.sub.atk=x.atk
        tr1.sub.defense=x.defense
        tr1.sub.spdef=x.spdef
        tr1.sub.spatk=x.spatk
        tr1.sub.speed=x.speed
#Substitute
async def substitute(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Substitute!")
    if x.hp<(x.maxhp/4) or tr1.sub!="None":
        em.add_field(name="Substitute:",value=f"It failed!")
    elif x.hp>(x.maxhp/4) and tr1.sub=="None": 
        em.add_field(name="Substitute:",value=f"{x.nickname} created a substitute!")
        x.hp-=x.maxhp/4
        tr1.sub=Pokemon(name="Substitute",moves='["A","B","C","D"]',primaryType=x.primaryType,secondaryType=x.secondaryType)
        tr1.sub.hp=x.maxhp/4
        tr1.sub.atk=x.atk
        tr1.sub.defense=x.defense
        tr1.sub.spdef=x.spdef
        tr1.sub.spatk=x.spatk
        tr1.sub.speed=x.speed        
#Silk Trap
async def silktrap(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Silk Trap!")
    if x.protect=="Pending":
        x.protect=False
    elif x.protect==False:
        x.protect=True
#Obstruct
async def obstruct(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Obstruct!")
    if x.protect=="Pending":
        x.protect=False
    elif x.protect==False:
        x.protect=True
#Max Guard
async def maxguard(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Max Guard!")
    if x.protect=="Pending":
        x.protect=False
    elif x.protect==False:
        x.protect=True
#Baneful Bunker
async def banefulbunker(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Baneful Bunker!")
    if x.protect=="Pending":
        x.protect=False
    elif x.protect==False:
        x.protect=True
async def spikyshield(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Spiky Shield!")
    if x.protect=="Pending":
        x.protect=False
    elif x.protect==False:
        x.protect=True
#Protect
async def prtect(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Protect!")
    if x.protect=="Pending":
        x.protect=False
    elif x.protect==False:
        x.protect=True
#Sleep Powder
async def sleeppowder(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sleep Powder!")
    if "Grass" not in (y.secondaryType,y.primaryType,y.teraType) and y.status=="Alive":
        await sleep(em,x,y,100)  
          
#Stun Spore
async def stunspore(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Stun Spore!")
    if "Grass" not in (y.secondaryType,y.primaryType,y.teraType) and y.status=="Alive" and y.item!="Covert Cloak":
        await paralyze(em,x,y,100)  
        
#Spore
async def spore(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Spore!")
    if "Grass" not in (y.secondaryType,y.primaryType,y.teraType):
        await sleep(em,x,y,100)
#Dark Void
async def darkvoid(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dark Void!")
    await sleep(em,x,y,100)   
    em.set_image(url=random.choice(["https://cdn.discordapp.com/attachments/1102579499989745764/1144902039038595142/image_search_1693036302851.gif","https://cdn.discordapp.com/attachments/1102579499989745764/1144902055853559808/image_search_1693036306217.gif"]))
#Hypnosis
async def hypnosis(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hypnosis!")
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
#Struggle
async def struggle(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Struggle!")    
    al=1
    r=await randroll()
    c=await isCrit(em,tr1,x,y)
    a=1
    b=1
    y.hp-=await special(x,x.level,x.spatk,y.spdef,50,a,b,c,r,al)
    x.hp-=(x.maxhp/8)
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143457218960818176/image0.gif")
#Steam Eruption
async def steameruption(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Steam Eruption!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al,w)     
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,30)
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
        em.add_field(name="Effect:",value=f"{y.nickname} became weak to Fire-Type attacks!")
#Soak
async def soak(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Soak!")
    y.primaryType="Water"
    y.secondaryType="???"
    em.add_field(name="Effect:",value=f"{y.nickname} turned into {y.primaryType} type!")
#Magic Powder
async def magicpowder(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Magic Powder!")
    y.primaryType="Psychic"
    y.secondaryType="???"
    em.add_field(name="Effect:",value=f"{y.nickname} turned into {y.primaryType} type!")
#Trick-Or-Treat
async def trickortreat(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Trick-Or-Treat!")
    y.primaryType="Ghost"
    y.secondaryType="???"
    em.add_field(name="Effect:",value=f"{y.nickname} turned into {y.primaryType} type!")
#Forests Curse
async def forestscurse(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used Forest's Curse!")
    y.primaryType="Grass"
    y.secondaryType="???"
    em.add_field(name="Effect:",value=f"{y.nickname} turned into {y.primaryType} type!")    
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
        x.ability,y.ability=y.ability,x.ability
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
        em.add_field(name="Effect:",value=f"{y.nickname} fell for the encore!")
        y.encore=y.use
        y.encendturn=turn+random.randint(3,5)
    else:      
        em.add_field(name="Effect:",value="It failed!")  
 
#Snowscape
async def snowscape(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Snowscape!")    	
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Snowstorm"] and a!=0:
        em.add_field(name="Weather:",value=f"{x.nickname} started a snowstorm!")
        field.weather="Snowstorm"
        field.snowturn=turn
        await snowend(field,x,y)          	        
#Chilly Reception
async def chillyreception(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Chilly Reception!")    	
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Snowstorm"] and a!=0:
        em.add_field(name="Weather:",value=f"{x.nickname} started a snowstorm!")
        field.weather="Snowstorm"
        field.snowturn=turn
        await snowend(field,x,y)        
#G-Max Resonance 
async def gmaxresonance(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name="Move:",value=f"{x.nickname} used G-Max Resonance!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143338239671930921/IMG_20230822_061618.jpg")    
    if tr1.auroraveil is False:
        tr1.auroraturn=turn
        tr1.auroraend(x,y)
        tr1.auroraveil=True  
        em.add_field(name=f"Aurora Veil:",value="Aurora Veil will reduced your team's damage taken!")        
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
        field.hailturn=turn
        await hailend(field,x,y)    
        

#Sandstorm
async def sandstorm(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sandstorm!")   
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Sandstorm"]:        
        em.add_field(name="Weather:",value=f"{x.nickname} started a sandstorm!")
        field.weather="Sandstorm"
        field.sandturn=turn
        await sandend(field,x,y) 	    
#Splintered Stormshards
async def splinteredstormshards(ctx,x,y,tr1,em,field,turn): 
    em.add_field(name=f"Move:",value=f"{x.nickname} used Splintered Stormshards!")        
    al=1
    r=await randroll()
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,190,a,b,c,r,al)       
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1141622970322800701/image_search_1692254516038.png")    
    if field.terrain!="Normal":
        field.terrain="Normal"       
        em.add_field(name="Terrain:",value="The battlefield turned normal.")
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
        field.sandturn=turn
        await sandend(field,x,y)    
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
        field.sandturn=turn
        await sandend(field,x,y)            
     
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
        y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,160,a,b,c,r,al,w)       
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143327832257331311/tumblr_78af84bcebb2a33be38dca44ba196c02_906c857b_540.gif")        
#Sunny Day
async def sunnyday(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sunny Day!")    
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Sunny"]:
        em.add_field(name="Weather:",value=f"{x.nickname} made the sunlight harsh!")
        field.weather="Sunny"
        field.sunturn=turn
        await sunend(field,x,y)  
#Hydro Vortex
async def hydrovortex(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hydro Vortex!")        
    al=1
    r=await randroll()
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al,w)        
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1140805397427519538/image_search_1692059587928.png")       
#Continental Crush
async def continentalcrush(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Continental Crush!")        
    al=1
    r=await randroll()
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)       
#Tectonic Rage
async def tectonicrage(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Tectonic Rage!")        
    al=1
    r=await randroll()
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)        
#Corkscrew Crash
async def corkscrewcrash(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Corkscrew Crash!")        
    al=1
    r=await randroll()
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)                     
#Oceanic Operetta
async def operetta(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Oceanic Operetta!")        
    al=1
    r=await randroll()
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,195,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,195,a,b,c,r,al,w)        #Inferno Overdrive
async def infernooverdrive(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Inferno Overdrive!")        
    al=1
    r=await randroll()
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al,w)       
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1140804259361869947/image_search_1692059302205.png")
#G-Max Centiferno
async def gmaxcentiferno(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Centiferno!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1147085975302963251/image_search_1693556959209.jpg")    
    if y.cntdmg is False and "Fire" not in (y.primaryType,y.secondaryType,y.teraType) and y.hp>0:
        y.cntdmg=True
        em.add_field(name="Effect:",value=f"{y.nickname} was trapped by vortex of fire!")
        x.cntendturn=turn+4        
#G-Max Wildfire
async def gmaxwildfire(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Wildfire!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142811058994696352/image0.gif")    
    if y.wfdmg is False and "Fire" not in (y.primaryType,y.secondaryType,y.teraType) and y.hp>0:
        y.wfdmg=True
        em.add_field(name="Effect:",value=f"{y.nickname} was surrounded by fire!")
        x.wfendturn=turn+4    
#G-Max Cannonade 
async def gmaxcannonade(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Cannonade!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142807584055763024/image0.gif")    
    if y.cndmg is False and "Water" not in (y.primaryType,y.secondaryType,y.teraType) and y.hp>0:
        y.cndmg=True
        em.add_field(name="Effect:",value=f"{y.nickname} got caught in the vortex of water!")
        x.cnendturn=turn+4
#G-Max Vine Lash
async def gmaxvinelash(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Vine Lash!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142807732651569225/image0.gif")    
    if y.vldmg is False and "Grass" not in (y.primaryType,y.secondaryType,y.teraType) and y.hp>0:
        y.vldmg=True
        em.add_field(name="Effect:",value=f"{y.nickname} got trapped with vines!!")
        x.vlendturn=turn+4        
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
        field.sunturn=turn
        await sunend(field,x,y)         
              
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
        y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al,w)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,160,a,b,c,r,al,w)    	       
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143328737069371572/image0.gif")            
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143330873337450546/G-Max_Foam_Burst_VIII.png")
#Rain Dance
async def raindance(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rain Dance!")    
    if field.weather not in ["Extreme Sunlight","Heavy Rain","Strong Wind","Rainy"]:
        em.add_field(name="Weather:",value=f"{x.nickname} made it rain!")
        field.weather="Rainy"
        field.rainturn=turn
        await rainend(field,x,y)           
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
        field.rainturn=turn
        await rainend(field,x,y)     
#G-Max Stonesurge
async def gmaxstonesurge(ctx,x,y,tr1,tr2,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Stonesurge!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1147086204710420551/image_search_1693557047820.png")
    if "Stealth Rock" in tr2.hazard:
        em.add_field(name=f"Stealth Rock:",value="Nothing happened!")
    elif "Stealth Rock" not in tr2.hazard and y.ability!="Magic Bounce":
        tr2.hazard.append("Stealth Rock")
        em.add_field(name=f"Stealth Rock:",value="Pointed stones float in the air around the opposing team!")
    elif "Stealth Rock" not in tr1.hazard and y.ability=="Magic Bounce":
        tr1.hazard.append("Stealth Rock")
        em.add_field(name=f"Stealth Rock:",value="Pointed stones float in the air around the ally team!")   
#Supersonic Skystrike
async def supersonicskystrike(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Supersonic Skystrike!")        
    al=1
    r=await randroll()
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)                    
#All-Out Pummeling 
async def alloutpummeling(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used All-Out Pummeling!")        
    al=1
    r=await randroll()
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)           
#Let's Snuggle Forever
async def letssnuggleforever(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Let's Snuggle Forever!")        
    al=1
    r=await randroll()
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,190,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,190,a,b,c,r,al)           
#Twinkle Tackle
async def twinkletackle(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Twinkle Tackle!")        
    al=1
    r=await randroll()
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,195,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,195,a,b,c,r,al)           
#Devastating Drake
async def devastatingdrake(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Devastating Drake!")        
    al=1
    r=await randroll()
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)           
#Subzero Slammer
async def subzeroslammer(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Subzero Slammer!")        
    al=1
    r=await randroll()
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)           
#Acid Downpour
async def aciddownpour(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Acid Downpour!")        
    al=1
    r=await randroll()
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)           
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
#G-Max Malodor
async def gmaxmalodor(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Malodor!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143341765684908082/IMG_20230822_063015.jpg")
    if a!=0 and y.item!="Covert Cloak":
        await poison(em,x,y,100)    
#Shell Side Arm
async def shellsidearm(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shell Side Arm!")        
    al=1
    r=await randroll()
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,90,a,b,c,r,al)            
    if a!=0 and y.item!="Covert Cloak":
        await poison(em,x,y,20)                        
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
#G-Max Chi Strike
async def gmaxchistrike(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Chi Strike!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143334665328005210/IMG_20230822_060241.jpg")
    if a!=0:
        x.critrate*=2      
        em.add_field(name="Effect:",value="Crit rate was increased!")
#Savage Spin-Out
async def savagespinout(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Savage Spin-Out!")        
    al=1
    r=await randroll()
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1145135506519232624/image0.gif")         
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
#G-Max Befuddle 
async def gmaxbefuddle(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Befuddle!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143332197265330338/G-Max_Befuddle_VIII.png")    
    if y.status=="Alive" and y.item!="Covert Cloak":
        m=random.randint(1,3)
        if m==1:
            await poison(em,x,y,100)
        elif m==2:
            await sleep(em,x,y,100)
        elif m==3:
            await paralyze(em,x,y,100)
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
#G-Max Snooze
async def gmaxsnooze(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Snooze!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143107569703985266/image_search_1692608454113.png")         
    if y.yawn=="False" and y.status=="Alive":
        y.yawn=True
        em.add_field(name="Effect:",value=f"{y.nickname} became drowsy!")
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
#Black Hole Eclipse
async def blackholeeclipse(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Black Hole Eclipse!")        
    al=1
    r=await randroll()
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142426191874244638/image_search_1692445953464.png")      
#G-Max Gold Rush
async def gmaxgoldrush(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Gold Rush!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143333537102172210/IMG_20230822_055905.jpg")
    if a!=0:
        await confuse(em,x,y,100)    
#G-Max Cuddle
async def gmaxcuddle(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Cuddle!")        
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
    if a!=0 and y.item!="Covert Cloak":
        y.infatuated=True
        em.add_field(name="Effect:",value=f"{y.nickname} is infatuated!")
#G-Max Replenish
async def gmaxreplenish(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Replenish!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143340239239250040/IMG_20230822_062244.jpg")
    if a!=0 and "Berry[Used]" in x.item:
        ch=random.randint(1,2)
        if ch==1:
            x.item=x.item.replace("[Used]","")
            em.add_field(name="Effect:",value=f"{x.nickname}'s {x.item} was replenished!")
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
#G-Max Terror
async def gmaxterror(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Terror!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143336183313735681/IMG_20230822_060822.jpg")
    if a!=0 and x.trap==False:
        x.trap=True
        em.add_field(name="Effect:",value=f"{x.nickname} trapped {y.nickname}!")
#Shattered Psyche
async def shatteredpsyche(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shattered Psyche!")        
    al=1
    r=await randroll()
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)           
#Breakneck Blitz
async def breakneckblitz(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Breakneck Blitz!")        
    al=1
    r=await randroll()
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)           
#Sinister Arrow Raid
async def arrowraid(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sinister Arrow Raid!")        
    al=1
    r=await randroll()
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,180,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,180,a,b,c,r,al)           
#Pulverizing Pancake
async def pancake(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Pulverizing Pancake!")        
    al=1
    r=await randroll()
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,210,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,210,a,b,c,r,al)           
#Light that burns the sky
async def skyburn(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Light That Burns The Sky!")        
    al=1
    r=await randroll()
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)           
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
#Never-ending Nightmare
async def neverendingnightmare(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Never-ending Nightmare!")        
    al=1
    r=await randroll()
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143112548858728448/image0.gif")        
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
#G-Max Meltdown
async def gmaxmeltdown(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Meltdown!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143342497788072066/IMG_20230822_063337.jpg")
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
#Swagger
async def swagger(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Swagger!")    
    await atkchange(em,y,x,2)       
    await confuse(em,x,y,100)     
#Belly drum
async def bellydrum(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Belly Drum!")    
    if x.hp>(x.maxhp/2):
        await atkchange(em,x,x,6)
        x.hp-=round(x.maxhp/2)
        em.add_field(name="Effect:",value=f"{x.nickname} cuts its own HP and maximized its Attack.")
    else:
        em.add_field(name="Effect:",value="It failed.")
#Dragon Dance
async def dragondance(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Dance!")    
    await atkchange(em,x,x,1)    
    await speedchange(em,x,x,1)    
#Acid Armor
async def acidarmor(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Acid Armor!")    
    await defchange(em,x,x,2)
#Barrier
async def barrier(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Barrier!")    
    await defchange(em,x,x,2)          
#Iron Defense
async def irondefense(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Iron Defense!")    
    await defchange(em,x,x,2)           
#Defend Order
async def defendorder(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Defend Order!")    
    await defchange(em,x,x,1)
    await spdefchange(em,x,x,1)       
#Amnesia
async def amnesia(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Amnesia!")    
    await spdefchange(em,x,x,2)

#Cotton Guard
async def cottonguard(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Cotton Guard!")    
    await defchange(em,x,x,3)        
    
#Cosmic Power
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
    await atkchange(em,x,x,2)
    await defchange(em,x,x,-1)
    await spatkchange(em,x,x,2)    
    await spdefchange(em,x,x,-1)         
    await speedchange(em,x,x,2)    
#Bulk Up
async def bulkup(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bulk Up!")    
    await atkchange(em,x,x,1)    
    await defchange(em,x,x,1)
#Hone Claws
async def honeclaws(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hone Claws!")    
    await atkchange(em,x,x,1)    
    x.accuracy+=10
    em.add_field(name="Accuracy Increase:",value=f"{x.icon} {x.nickname}'s accuracy rose!")
#Autotomize 
async def autotomize(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Autotomize!")         
    x.weight*=0.5
    await speedchange(em,x,x,2)
#Captivate
async def captivate(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Captivate!")     
    await spatkchange(em,y,x,-2)
#Coil
async def coil(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Coil!")    
    await atkchange(em,x,x,1)    
    await defchange(em,x,x,1)    
    x.accuracy+=10
    em.add_field(name="Accuracy Increase:",value=f"{x.icon} {x.nickname}'s accuracy rose!")  
#Mimic
async def mimic(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Mimic!")     
    if y.use!="None" and y.dmax==False and y.use not in x.moves:
        x.moves[x.moves.index("Mimic")]=y.use
        em.add_field(name="Effect:",value=f"{x.nickname} learned {y.use}!")
#Growth
async def growth(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Growth!")    
    await atkchange(em,x,x,1)    
    await spatkchange(em,x,x,1)       
#Curse
async def curse(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Curse!")    
    if "Ghost" not in (x.primaryType,x.secondaryType,x.teraType):
        await atkchange(em,x,x,1)    
        await defchange(em,x,x,1)        
        await speedchange(em,x,x,-1)      
    else:
        if y.cursed!=True:
            x.hp-=x.maxhp/2
            y.cursed=True
            em.add_field(name="Curse:",value=f"{x.nickname} cut its own HP and put a curse on {y.nickname}!")
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
        al*=1.33
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)    
    await flinch(em,x,y,30)
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
#Steel Wing 
async def steelwing(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Steel Wing!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)            
    ch=random.randint(1,10)
    if ch<3:
        await defchange(em,x,x,1)          
#Thunder Fang
async def thunderfang(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder Fang!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)            
    if y.item!="Covert Cloak":
        await flinch(em,x,y,10)
        await paralyze(em,x,y,10)
#Ice Fang
async def icefang(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Fang!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)            
    if y.item!="Covert Cloak":
        await freeze(em,x,y,10)
        await flinch(em,x,y,10)
#Psychic Fangs
async def psychicfangs(ctx,x,y,tr1,tr2,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psychic Fangs!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)            
    if tr2.reflect:
        tr2.reflect=False
        em.add_field(name="Reflect:",value=f"{x.nickname} broke through opposing Reflect!")
    if tr2.lightscreen:
        tr2.lightscreen=False
        em.add_field(name="Light Screen:",value=f"{x.nickname} broke through opposing Light Screen!")     
#Glaive Rush
async def glaiverush(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Glaive Rush!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)     
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
#Poison Fang
async def poisonfang(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Poison Fang!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)            
    await poison(em,x,y,50)
#Fire Fang
async def firefang(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Fang!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al,w)            
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,10)
        await flinch(em,x,y,10)
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
    if x.seeded==True:
        x.seeded=False
        em.add_field(name="Effect:",value=f"{x.icon} {x.nickname} got rid of Leech Seed!")   
    if len(tr1.hazard)>0:
        tr1.hazard=[]
        em.add_field(name="Effect:",value=f"{x.icon} {x.nickname} removed hazards from its side!")
#Tidy Up
async def tidyup(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Tidy Up!")    
    await atkchange(em,x,x,1)
    await speedchange(em,x,x,1)
    if x.seeded==True:
        x.seeded=False
        em.add_field(name="Effect:",value=f"{x.icon} {x.nickname} got rid of Leech Seed!")   
    if len(tr1.hazard)>0:
        tr1.hazard=[]
        em.add_field(name="Effect:",value=f"{x.icon} {x.nickname} removed hazards from its side!")        
#Mortal Spin
async def mortalspin(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Mortal Spin!")    
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,30,a,b,c,r,al)        
    await poison(em,x,y,100)
    if x.seeded==True:
        x.seeded=False
        em.add_field(name="Effect:",value=f"{x.icon} {x.nickname} got rid of Leech Seed!")   
    if len(tr1.hazard)>0:
        tr1.hazard=[]
        em.add_field(name="Effect:",value=f"{x.icon} {x.nickname} removed hazards from its side!")        
#Crunch
async def crunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Crunch!")    
    if x.ability=="Strong Jaw":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Strong Jaw!",value="")
    if x.ability=="Sheer Force":
        al*=1.33
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
        al*=1.33
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
        al*=1.33
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
#Scale Shot
async def scaleshot(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Scale Shot!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,25,a,b,c,r,al)   
#Rock Blast
async def rockblast(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rock Blast!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,25,a,b,c,r,al)             
#Bullet Seed
async def bulletseed(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bullet Seed!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,25,a,b,c,r,al)                  
#Icicle Spear
async def iciclespear(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Icicle Spear!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,25,a,b,c,r,al)       
#Pin Missile
async def pinmissile(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Pin Missile!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,25,a,b,c,r,al)       
#Dragon Tail
async def dragontail(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Tail!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)      
#Breaking Swipe
async def breakingswipe(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Breaking Swipe!")    
    if x.ability=="Sheer Force":
        al*=1.33
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
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)          
    await poison(em,x,y,30)
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
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)           
    await poison(em,x,y,30)
#Dire Claw
async def direclaw(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dire Claw!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)        
    if x.ability!="Sheer Force" and y.item!="Covert Cloak":
        ll=random.randint(1,3)
        if ll==1 and x.status=="Alive":
            await poison(em,x,y,50)
        elif ll==2 and x.status=="Alive":
            await sleep(em,x,y,50)
        elif ll==3 and x.status=="Alive": 
            await paralyze(em,x,y,50)       
#Poison Tail
async def poisontail(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Poison Tail!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)           
    if a!=0  and y.item!="Covert Cloak":
        await poison(em,x,y,10)
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
    await flinch(em,x,y,10) 
#Dragon Rush
async def dragonrush(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Rush!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)           
    await flinch(em,x,y,20)     
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142742725658153050/image0.gif")
#Zen Headbutt
async def zenheadbutt(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Zen Headbutt!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)           
    await flinch(em,x,y,20) 
#Smart Strike
async def smartstrike(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Smart Strike!")
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)               
#Iron Head
async def ironhead(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Iron Head!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)           
    await flinch(em,x,y,30)
#Anchor Shot
async def anchorshot(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Anchor Shot!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)               
    if x.trap==False:
        x.trap=True
        em.add_field(name="Effect:",value=f"{x.nickname} trapped {y.nickname}!")
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
#Roar of Time
async def roaroftime(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Roar of Time!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)         
    em.set_image(url="https://cdn.discordapp.com/attachments/1102535204968599592/1142051009657569381/image0.gif") 
#Spacial Rend
async def spacialrend(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Special Rend!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al)      
    em.set_image(url="https://cdn.discordapp.com/attachments/1102535204968599592/1142051591986348032/image_search_1692356705077.gif")
#Eternabeam
async def eternabeam(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Eternabeam!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al)    
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142052934037807164/image0.gif")
#Dynamax Cannon
async def dynamaxcannon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dynamax Cannon!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.dmax==True or y.name=="Eternamax Eternatus":
        al*=2
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al)          
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142053199751172146/image0.gif")
#Behemoth Blade
async def behemothblade(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Behemoth Blade!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.dmax==True or y.name=="Eternamax Eternatus":
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)           
    em.set_image(url="https://64.media.tumblr.com/efd98a2ab2a90ce6e859606ae59524e8/b92fa84e4708d62d-10/s1280x1920/7663fab1ebd0a86caa8ad35263d3c0412276496f.gifv")
#Behemoth Bash
async def behemothbash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Behemoth Bash!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.dmax==True or y.name=="Eternamax Eternatus":
        al*=2
    y.hp-=await physical(x,x.level,x.defense,y.defense,100,a,b,c,r,al)       
    if a!=0:
        x.recharge=True
    em.set_image(url="https://64.media.tumblr.com/7950439127c135330af2c9b20ffd0e17/69ebd355e221ee89-40/s1280x1920/081a8fedce985d7922ea04ee42436886739c6634.gif")    
#Iron Tail
async def irontail(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Iron Tail!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)               
    ch=random.randint(1,100)
    chance=30
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await defchange(em,y,x,-1)
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
    await speedchange(em,y,x,-1)
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
#Parting Shot
async def partingshot(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Parting Shot!")     
    await atkchange(em,y,x,-1)
    await spatkchange(em,y,x,-1)
#Water Shuriken
async def watershuriken(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Water Shuriken!")    
    x.atktype="Dragon"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=15
    if x.ability=="Technician":
        al*=1.5
    elif x.name=="Ash Greninja":
        base=25
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al,w)       
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
    if a!=0:
        await speedchange(em,x,x,-1)    
#Play Rough
async def playrough(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Play Rough!")    
    if x.ability=="Sheer Force":
        al*=1.33
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
    await paralyze(em,x,y,100)  
#Toxic
async def toxic(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Toxic!")
    await poison(em,x,y,100)    
#Toxic Thread
async def toxicthread(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Toxic Thread!")
    await poison(em,x,y,100)      
    await speedchange(em,y,x,-1)       
#Will-O-Wisp
async def willowisp(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Will-O-Wisp!")
    await burn(em,x,y,100)   
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
#Blood Moon
async def bloodmoon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Blood Moon!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)    
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1147059667613270046/image_search_1693550721846.jpg")
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1144898496495882310/image0.gif")
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
    if a!=0:
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
#Axe Kick
async def axekick(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Axe Kick!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)                
    await confuse(em,x,y,30)
#Blaze Kick
async def blazekick(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Blaze Kick!")    
    x.atktype="Fire"
    if x.ability=="Striker":
        al*=1.3
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al,w)    
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
#Sky Uppercut
async def skyuppercut(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sky Uppercut!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)             
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
#Collison Course
async def collisioncourse(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Collision Course!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if a>=2:
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)        
#Electro Drift
async def electrodrift(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Electro Drift!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if a>=2:
        al*=1.5
    y.hp-=await physical(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al)    
#Dragon Ascent
async def dragonascent(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Ascent!")    
    x.atktype="Flying"
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
        al*=1.33
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al)            
    if x.ability!="Sheer Force":
        await flinch(em,x,y,30) 
#Avalanche 
async def avalanche(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Avalanche!")    
    if x.speed<y.speed and (y.use not in typemoves.statusmove and y.use!="None"):
        al*=2
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)                    
#Zing Zap
async def zingzap(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Zing Zap!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)                
    if x.ability!="Sheer Force":
        await flinch(em,x,y,30)    
#Mountain Gale
async def mountaingale(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Mountain Gale!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)            
    if x.ability!="Sheer Force":
        await flinch(em,x,y,30)    
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
#Triple Axel
async def tripleaxel(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Triple Axel!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Striker":
        al*=1.3
    hit=0
    ch=random.randint(1,100)
    if ch<90:
        y.hp-=await physical(x,x.level,x.atk,y.defense,20,a,b,c,r,al)                  
        hit+=1    
        ch=random.randint(1,100)
        if ch<90:
            y.hp-=await physical(x,x.level,x.atk,y.defense,40,a,b,c,r,al)    
            hit+=1    
            ch=random.randint(1,100)
            if ch<90:
                y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)   
                hit+=1
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")               
    else:        
        em.add_field(name="Effect:",value=f"{y.nickname} avoided the attack!")   
#Triple Kick
async def triplekick(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Triple Kick!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Striker":
        al*=1.3
    hit=0
    ch=random.randint(1,100)
    if ch<90:
        y.hp-=await physical(x,x.level,x.atk,y.defense,20,a,b,c,r,al)                  
        hit+=1    
        ch=random.randint(1,100)
        if ch<90:
            y.hp-=await physical(x,x.level,x.atk,y.defense,40,a,b,c,r,al)    
            hit+=1    
            ch=random.randint(1,100)
            if ch<90:
                y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)   
                hit+=1
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")               
    else:        
        em.add_field(name="Effect:",value=f"{y.nickname} avoided the attack!")           
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
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)       
#Fake Out
async def fakeout(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fake Out!")    
    if x.canfakeout==True and x.ability!="Parental Bond[Used]":
        x.atktype="Normal"
        base=40
        if x.ability=="Technician":
            base*=1.5
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)     
        x.canfakeout=False
        if a!=0 and y.item!="Covert Cloak":
            await flinch(em,x,y,100)
    else:
        em.add_field(name="Effect:",value="It failed.")   
#Upper Hand
async def upperhand(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Upper Hand!")    
    if x.canfakeout==True and x.ability!="Parental Bond[Used]":
        x.atktype="Fighting"
        base=40
        if x.ability=="Technician":
            base*=1.5
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)     
        x.canfakeout=False
        if a!=0 and y.item!="Covert Cloak":
            await flinch(em,x,y,100)
    else:
        em.add_field(name="Effect:",value="It failed.")
#First Impression
async def firstimpression(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used First Impression!")    
    if x.canfakeout==True and x.ability!="Parental Bond[Used]":
        x.atktype="Bug"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)     
        x.canfakeout=False
    else:
        em.add_field(name="Effect:",value="It failed.")           
#Quick Attack
async def quickattack(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Quick Attack!")    
    x.atktype="Normal"
    base=40
    if x.ability=="Technician":
        base*=1.5
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al) 
#Feint
async def feint(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Feint!")    
    x.atktype="Normal"
    base=50
    if x.ability=="Technician":
        base*=1.5
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)               
#Shadow Punch
async def shadowpunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shadow Punch!")    
    x.atktype="Ghost"
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al) 
#Poltergeist
async def poltergeist(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Poltergeist!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.item!="None" and "Used" not in y.item:
        y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)     
        em.add_field(name="Effect:",value=f"{y.nickname} is about to be attacked by its {y.item}.")     
    else:
        em.add_field(name="Effect:",value="It failed.") 
#Rage fist
async def ragefist(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rage Fist!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=50+(50*x.atktime)
    if base>300:
        base=300
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)         
#Vaccum Wave
async def vaccumwave(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Vaccum Wave!")    
    x.atktype="Fighting"
    if x.ability=="Technician":
        al*=1.5
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,40,a,b,c,r,al)     
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
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)   
#Power-Up Punch
async def poweruppunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Power-up Punch!")    
    x.atktype="Fighting"
    base=40
    if x.ability=="Technician":
        base*=1.5
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)      
    if a!=0:
        await atkchange(em,x,x,1)
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
        al*=1.33
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
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
        al*=1.33
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)     
    if a!=0  and y.item!="Covert Cloak":
        await paralyze(em,x,y,20)
#Ice Punch
async def icepunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Punch!")    
    x.atktype="Ice"
    if x.ability=="Sheer Force":
        al*=1.33
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)     
    if y.item!="Covert Cloak":
        await freeze(em,x,y,10)
#Fire Punch
async def firepunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Punch!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    if x.ability=="Sheer Force":
        al*=1.33
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al,w)             
    if y.item!="Covert Cloak":
        await burn(em,x,y,10)
#Fire Lash
async def firelash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Lash!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    if x.ability=="Sheer Force":
        al*=1.33
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
    if dmg>y.hp:
        dmg=y.hp         
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!") 
#Double-Edge
async def doubleedge(ctx,x,y,tr1,em,field,turn):
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
    if dmg>y.hp:
        dmg=y.hp         
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")        
#Beak Blast
async def beakblast(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Beak Blast!")    
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)            
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
    if dmg>y.hp:
        dmg=y.hp         
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!") 
#Submission
async def submission(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Submission!")    
    x.atktype="Fighting"
    if x.ability=="Reckless":
        al*=1.2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)    
    if dmg>y.hp:
        dmg=y.hp         
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head" and a!=0:
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")         
#Wild Charge
async def wildcharge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Wild Charge!")    
    x.atktype="Electric"
    if x.ability=="Reckless":
        al*=1.2
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)             
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    recoil=dmg/4
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
    if dmg>y.hp:
        dmg=y.hp
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
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg              
#Energy Ball
async def energyball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Energy Ball!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)               
    ch=random.randint(1,100)
    chance=10
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await spdefchange(em,y,x,-1)
#Seed Flare
async def seedflare(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Seed Flare!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)               
    ch=random.randint(1,100)
    chance=40
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await spdefchange(em,y,x,-2)        
#Fishious Rend
async def fishiousrend(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fishious Rend!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Strong Jaw":
        al*=1.5
    if x.speed>y.speed:
        al*=2
    dmg=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al,w)        
#Aqua Tail
async def aquatail(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aqua Tail!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al,w)    
#Aqua Fang
async def aquafang(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aqua Fang!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Strong Jaw":
        al*=1.5
    dmg=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al,w)
#Bolt Beak
async def boltbeak(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bolt Beak!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.speed>y.speed:
        al*=2
    dmg=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al)               
#Shadow Bone
async def shadowbone(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shadow Bone!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al)        
    ch=random.randint(1,100)
    chance=20
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await defchange(em,y,x,-1)    
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
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al,w)        
    ch=random.randint(1,100)
    chance=20
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await defchange(em,y,x,-1)
#Razor Shell
async def razorshell(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Razor Shell!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    if x.ability=="Sharpness":
        al*=1.5
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al,w)        
    ch=random.randint(1,100)
    chance=50
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await defchange(em,y,x,-1)        
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
    if dmg>y.hp:
        dmg=y.hp         
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
    if dmg>y.hp:
        dmg=y.hp         
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
    if dmg>y.hp:
        dmg=y.hp         
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")     
    if a!=0  and y.item!="Covert Cloak":         
        await paralyze(em,x,y,10)
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
    if dmg>y.hp:
        dmg=y.hp         
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
        al*=1.33
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al,w)             
    if dmg>y.hp:
        dmg=y.hp         
    y.hp-=dmg
    recoil=dmg/3
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")    
    if a!=0 and y.item!="Covert Cloak":        
        await burn(em,x,y,10)
#Thunder Punch
async def thunderpunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder Punch!")    
    x.atktype="Electric"
    if x.ability=="Sheer Force":
        al*=1.33
    elif x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)     
    if a!=0 and y.item!="Covert Cloak":
        await paralyze(em,x,y,10)
#Force Palm
async def forcepalm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Force Palm!")    
    x.atktype="Fighting"
    if x.ability=="Sheer Force":
        al*=1.33
    elif x.ability=="Technician":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)     
    if a!=0 and x.ability!="Sheer Force" and y.item!="Covert Cloak":
        await paralyze(em,x,y,30)
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
#Electroweb
async def electroweb(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Electroweb!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,65,a,b,c,r,al)            
    if a!=0:
        await speedchange(em,y,x,-1) 
#Overdrive
async def overdrive(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Overdrive!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)
#Discharge
async def discharge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Discharge!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)           
    if a!=0 and y.item!="Covert Cloak":
        await paralyze(em,x,y,30)
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
#Thunderclap 
async def thunderclap(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder Clap!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)     
#Sucker Punch
async def suckerpunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sucker Punch!")    
    x.atktype="Dark"
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
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
#Strength
async def strength(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Strength!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)      
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
    if a!=0 and y.item!="Covert Cloak":
        await paralyze(em,x,y,30)
#Raging Bull
async def ragingbull(ctx,x,y,tr1,tr2,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Raging Bull!")    
    x.atktype="Normal"
    if x.name=="Paldean Tauros":
        x.atktype="Fighting"
    elif "Blaze Breed" in x.name:
        x.atktype="Fire"
    elif "Aqua Breed" in x.name:
        x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al,w)    
    if tr2.reflect:
        tr2.reflect=False
        em.add_field(name="Reflect:",value=f"{x.nickname} broke through opposing Reflect!")
    if tr2.lightscreen:
        tr2.lightscreen=False
        em.add_field(name="Light Screen:",value=f"{x.nickname} broke through opposing Light Screen!")
#Brick Break
async def brickbreak(ctx,x,y,tr1,tr2,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Brick Break!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al)   
    if tr2.reflect:
        tr2.reflect=False
        em.add_field(name="Reflect:",value=f"{x.nickname} broke through opposing Reflect!")
    if tr2.lightscreen:
        tr2.lightscreen=False
        em.add_field(name="Light Screen:",value=f"{x.nickname} broke through opposing Light Screen!")       
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
#Petal Blizzard
async def petalblizzard(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Petal Blizzard!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)            
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
    ch=random.randint(1,100)
    chance=50
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await defchange(em,y,x,-1)
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1144896357161775166/image0.gif")
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
#Raging Fury
async def ragingfury(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Raging Fury!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al,w)     
    if x.fmove==False:
        x.fmove=True
        x.fmoveturn+=3    
#Thrash
async def thrash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thrash!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)     
    if x.fmove==False:
        x.fmove=True
        x.fmoveturn+=3    
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
    if x.fmove==False:
        x.fmove=True
        x.fmoveturn+=3
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
#Geomancy
async def geomancy(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Geomancy!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
            await spatkchange(em,x,x,2)
            await spdefchange(em,x,x,2)
            await speedchange(em,x,x,2)
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} is absorbing power.") 
        await spatkchange(em,x,x,2)
        await spdefchange(em,x,x,2)
        await speedchange(em,x,x,2)
        x.precharge=True    
#Meteor Beam
async def meteorbeam(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Meteor Beam!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
            await spatkchange(em,x,x,1)
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
#Shadow Force
async def shadowforce(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shadow Force!")    
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
        y.hp-=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} vanished instantly!") 
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
#Skull Bash
async def skullbash(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Skull Bash!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
            await defchange(em,x,x,1)
        al=1
        r=await randroll() 
        x.atktype="Normal"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} lowered it's head.") 
        await defchange(em,x,x,1)
        x.precharge=True          
#Dig
async def dig(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dig!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Ground"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} burrowed its way under the ground!") 
        x.precharge=True          
#Bounce
async def bounce(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bounce!")    
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
        y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al)   
        x.precharge=False
        if y.item!="Covert Cloak":
            await paralyze(em,x,y,30)
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} sprang up!") 
        x.precharge=True          
#Fly
async def fly(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fly!")    
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
        y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} flew up high!") 
        x.precharge=True          
#Razor Wind
async def razorwind(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Razor Wind!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Flying"
        c=await isCrit(em,tr1,x,y,2)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,160,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} whipped up a whirlwind!") 
        x.precharge=True             
#Solar Beam
async def solarbeam(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Solar Beam!")    
    if x.item=="Power Herb" or x.precharge is True or field.weather in ["Sunny","Extreme Sunlight"] or x.ability in ["Chloroplast","Big Leaves"]:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Grass"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} is absorbing sunlight!") 
        x.precharge=True    
#Solar Blade
async def solarblade(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Solar Blade!")    
    if x.item=="Power Herb" or x.precharge is True or field.weather in ["Sunny","Extreme Sunlight"] or x.ability in ["Chloroplast","Big Leaves"]:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Grass"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,125,a,b,c,r,al)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} is absorbing sunlight!") 
        x.precharge=True                     
#Ice Burn
async def iceburn(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ice Burn!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Ice"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await special(x,x.level,x.spatk,y.spdef,140,a,b,c,r,al)   
        em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1144917504154665001/image_search_1693039988996.gif")
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} became cloaked in a freezing air!") 
        x.precharge=True                     
#Freeze Shock
async def freezeshock(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Freeze Shock!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Ice"
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,140,a,b,c,r,al)   
        x.precharge=False
        em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1144917233592717333/image_search_1693039901528.png")
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} became cloaked in a freezing light!") 
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
#Stone Axe
async def stoneaxe(ctx,x,y,tr1,tr2,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Stone Axe!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Sharpness":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,65,a,b,c,r,al)       
    if "Stealth Rock" in tr2.hazard:
        em.add_field(name=f"Stealth Rock:",value="Nothing happened!")
    elif "Stealth Rock" not in tr2.hazard and y.ability!="Magic Bounce":
        tr2.hazard.append("Stealth Rock")
        em.add_field(name=f"Stealth Rock:",value="Pointed stones float in the air around the opposing team!")
    elif "Stealth Rock" not in tr1.hazard and y.ability=="Magic Bounce":
        tr1.hazard.append("Stealth Rock")
        em.add_field(name=f"Stealth Rock:",value="Pointed stones float in the air around the ally team!")  
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
    await flinch(em,x,y,30)
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
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)       
    await poison(em,x,y,10)
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
#Surging Strikes
async def surgingstikes(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Surging Strikes!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y,16)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,25,a,b,c,r,al,w)               
#Waterfall
async def waterfall(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Waterfall!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,85,a,b,c,r,al,w)           
    await flinch(em,x,y,20)
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
#Foul Play
async def foulplay(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Foul Play!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,y.atk,y.defense,80,a,b,c,r,al)    
#Throat Chop
async def throatchop(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Throat Chop!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)     
#Aura Wheel
async def aurawheel(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aura Wheel!")    
    x.atktype="Electric"
    if "hangry" in x.sprite:
        x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,110,a,b,c,r,al)     
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
#Assurance 
async def assurance(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Assurance!")    
    if x.ability=="Technician":
        al*=1.5
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.speed<y.speed:
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)    
#Payback 
async def payback(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Payback!")    
    if x.ability=="Technician":
        al*=1.5
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.speed<y.speed:
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,50,a,b,c,r,al)     
#Ceasless Edge
async def ceaselessedge(ctx,x,y,tr1,tr2,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ceasless Edge!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)           
    if tr2.hazard.count("Spikes")==3:
        em.add_field(name=f"Spikes:",value="Nothing happened!")
    elif tr2.hazard.count("Spikes")<3 and y.ability!="Magic Bounce":
        tr2.hazard.append("Spikes")
        em.add_field(name=f"Spikes:",value="Spikes were scattered all around the opposing team!")
    elif tr1.hazard.count("Spikes")<3 and y.ability=="Magic Bounce":
        tr1.hazard.append("Spikes")
        em.add_field(name=f"Spikes:",value="Spikes were scattered all around the ally team!")
#G-Max Steelsurge
async def gmaxsteelsurge(ctx,x,y,tr1,tr2,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Steelsurge!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143343581101310093/IMG_20230822_063835.jpg")
    if "Steel Spikes" in tr2.hazard:
        em.add_field(name=f"Steel Spikes:",value="Nothing happened!")
    elif "Steel Spikes" not in tr2.hazard and y.ability!="Magic Bounce":
        tr2.hazard.append("Steel Spikes")
        em.add_field(name=f"Steel Spikes:",value="Sharp-pointed pieces of steel started floating around your opposing Pokémon!")
    elif "Steel Spikes" not in tr1.hazard and y.ability=="Magic Bounce":
        tr1.hazard.append("Steel Spikes")
        em.add_field(name=f"Steel Spikes:",value="Sharp-pointed pieces of steel started floating around your ally Pokémon!")        
#Psycho Cut
async def psychocut(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Psycho Cut!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Psychic"
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
#Draco Barrage
async def dracobarrage(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Draco Barrage!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if a==0:
        a=1
    if x.atk>=x.spatk:
        y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al) 
    elif x.spatk>x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)   
    if y.hp<0:
        y.hp=0
    x.hp-=round((y.maxhp-y.hp)*0.33)
#Sacred Sword
async def sacredsword(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sacred Sword!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.maxdef,90,a,b,c,r,al)     
#Secret Sword
async def secretsword(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Secret Sword!")    
    if x.ability=="Sharpness":
        al*=1.5
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y,defense,85,a,b,c,r,al)       
#Darkest Lariat
async def darkestlariat(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Darkest Lariat!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.maxdef,85,a,b,c,r,al)       
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
#Trailblaze
async def trailblaze(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Trailblaze!")    
    if x.ability=="Technician":
        al*=1.5
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,50,a,b,c,r,al)     
    if a!=0:
        await speedchange(em,x,x,1)
#Razor Leaf
async def razorleaf(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Razor Leaf!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)       
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
#Triple Dive
async def tripledive(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Triple Dive!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,30,a,b,c,r,al,w)       
#Double Iron Bash
async def ironbash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Double Iron Bash!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)      
    await flinch(em,x,y,30)
#Dragon Darts
async def dragondarts(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Darts!")    
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,50,a,b,c,r,al)     
#Gear Grind
async def geargrind(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Gear Grind!")    
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await physical(x,x.level,x.atk,y.defense,50,a,b,c,r,al)          
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
#Lunge
async def lunge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Lunge!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)                     
    await atkchange(em,y,x,-1)
#Pounce
async def pounce(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Pounce!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)                     
    await speedchange(em,y,x,-1)    
#Skitter Smack
async def skittersmack(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Skitter Smack!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,70,a,b,c,r,al)                     
    await spatkchange(em,y,x,-1)    
#Fell Stinger
async def fellstinger(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fell Stinger!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,30,a,b,c,r,al)                     
    if y.hp<=0:
        await atkchange(em,x,x,2)    
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
#Blazing Torque
async def blazingtorque(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Blazing Torque!")    
    x.atktype="Fire"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)   
#Combat Torque
async def combattorque(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Combat Torque!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)        
#Noxious Torque
async def noxioustorque(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Noxious Torque!")    
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)       
#Magical Torque
async def magicaltorque(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Magical Torque!")    
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)       
#Wicked Torque
async def wickedtorque(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Wicked Torque!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)       
#Lands Wrath
async def landswrath(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Land's Wrath!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)    
#Thousand Arrows
async def thousandarrows(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thousand Arrows!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if a==0:
        a=1
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al)    
#Drill Run
async def drillrun(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Drill Run!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)          
#Precipice Blades
async def precipiceblades(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Precipice Blades!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)      
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
        al*=1.33
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)  
    await freeze(em,x,y,10)
#Frost Breath
async def frostbreath(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Frost Breath!")    
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y,16)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await special(x,x.level,x.spatk,y.spdef,65,a,b,c,r,al)        
#Icy Wind
async def icywind(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Icy Wind!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await special(x,x.level,x.spatk,y.spdef,55,a,b,c,r,al)    
    if x.ability!="Sheer Force":
        await speedchange(em,y,x,-1)
#Glaciate
async def glaciate(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Glaciate!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]
    y.hp-=await special(x,x.level,x.spatk,y.spdef,65,a,b,c,r,al)    
    if x.ability!="Sheer Force":
        await speedchange(em,y,x,-1)        
#Earth Power
async def earthpower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Earth Power!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,100)
    chance=10
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await spdefchange(em,y,x,-1)
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
        al*=1.33
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    await flinch(em,x,y,10)
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
        al*=1.33
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
        al*=1.33
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
#Glare
async def glare(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Glare!")        
    await paralyze(em,x,y,100)        
#Freezing Glare
async def freezingglare(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Freezing Glare!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    await freeze(em,x,y,10)
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
        al*=1.33
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)      
    ch=random.randint(1,100)
    chance=30
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await spdefchange(em,y,x,-1) 
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
        al*=1.33
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)  
    ch=random.randint(1,100)
    chance=10
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await spdefchange(em,y,x,-1) 
#Roost
async def roost(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Roost!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
        if x.teraType=="Flying":
            x.roost="TR"
            x.teraType="None"
        if x.primaryType=="Flying":
            x.roost="T1"
            x.primaryType="None"
        elif x.secondaryType=="Flying":
            x.roost="T2"
            x.secondaryType="None"
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
        if x.teraType=="Flying":
            x.roost="TR"
            x.teraType="None"
        if x.primaryType=="Flying":
            x.roost="T1"
            x.primaryType="None"
        elif x.secondaryType=="Flying":
            x.roost="T2"
            x.secondaryType="None"          
#Slack Off
async def slackoff(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Slack Off!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")            
#Milk Drink
async def milkdrink(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Milk Drink!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")      
#Jungle Healing
async def junglehealing(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Jungle Healing!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")            
#Soft-Boiled
async def softboiled(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Soft-Boiled!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")           
#Heal Order
async def healorder(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Heal Order!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")   
#Revelation Dance
async def revelationdance(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hyper Beam!")    
    x.atktype=x.primaryType
    if x.teraType!="???":
        x.atktype=x.teraType
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)               
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
    if a!=0:
        x.recharge=True
#Tri Attack
async def triattack(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Tri Attack!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)     
    ch=random.randint(1,100)
    if x.ability=="Serene Grace":
        ch/=2
    if ch<30 and y.item!="Covert Cloak":
        m=random.randint(1,3)
        if m==1:
            await burn(em,x,y,100)
        elif m==2:
            await freeze(em,x,y,100)
        elif m==3:
            await paralyze(em,x,y,100)
#Hyper Voice
async def hypervoice(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hyper Voice!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    w=await weathereff(field,x,y,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)     
#Tera Blast
async def terablast(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Tera Blast!")    
    x.atktype="Normal"
    if x.teraType!="???":
        x.atktype=x.teraType
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al,w)     
#Hidden Power
async def hiddenpower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hidden Power!")    
    base,x.atktype=await hidp(x.hpiv,x.atkiv,x.defiv,x.spatkiv,x.spdefiv,x.speediv)
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,base,a,b,c,r,al,w)     
#Judgment 
async def judgment(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Judgment!")    
    x.atktype=x.primaryType
    if x.teraType!="???":
        x.atktype=x.teraType
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    w=await weathereff(field,x,y,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)     
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1144901105579462656/image0.gif")
#Multi-Attack
async def multiattack(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Multi-Attack!")    
    x.atktype=x.primaryType
    if x.teraType!="???":
        x.atktype=x.teraType
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    w=await weathereff(field,x,y,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al,w)     
#Giga Impact
async def gigaimpact(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Giga Impact!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,150,a,b,c,r,al) 
    if a!=0:
        x.recharge=True
#Meteor Assault
async def meteorassault(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Meteor Assault!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,160,a,b,c,r,al) 
    if a!=0 and y.item!="Covert Cloak":
        x.recharge=True        
        await paralyze(em,x,y,40)
#Head Charge
async def headcharge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Head Charge!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Reckless":
        al*=1.2
    dmg=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al)         
    if dmg>y.hp:
        dmg=y.hp         
    y.hp-=dmg
    recoil=dmg/4
    if x.ability!="Rock Head":
        x.hp-=recoil
        em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil.!")     
    ch=random.randint(1,100)
    if x.ability=="Serene Grace":
        ch/=2
    if ch<20 and x.ability!="Sheer Force" and a!=0:
        await defchange(em,y,x,-1)
#Hyper Drill
async def hyperdrill(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hyper Drill!")    
    x.atktype="Normal"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)         
#Rock Wrecker
async def rockwrecker(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rock Wrecker!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)     
    if a!=0:
        x.recharge=True
#Aqua Step
async def aquastep(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aqua Step!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al,w)     
    if a!=0:
        await speedchange(em,x,x,1)
#Flame Charge
async def flamecharge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flame Charge!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,50,a,b,c,r,al,w)     
    if a!=0:
        await speedchange(em,x,x,1)        
#Weather Ball 
async def weatherball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Weather Ball!")    
    x.atktype="Normal"
    if field.weather=="Rainy":
        x.atktype="Water"
        al*=1.5
    elif field.weather=="Sunny":
        x.atktype="Fire"
        al*=1.5
    elif field.weather=="Sandstorm":
        x.atktype="Rock"
        al*=1.5
    elif field.weather in ["Hail","Snowstorm"]:
        x.atktype="Ice"
        al*=1.5
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.ability=="Technician":
        al*=1.5
    y.hp-=await special(x,x.level,x.spatk,y.spdef,50,a,b,c,r,al,w)    
#Bitter Blade
async def bitterblade(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bitter Blade!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    if x.ability=="Sharpness":
        al=1.5
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al,w)              
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    heal=dmg/2
    if x.item=="Big Root":
        heal*=1.3
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and a!=0:
        x.hp-=heal
    else:
        x.hp+=heal     
#Horn Leech
async def hornleech(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Horn Leech!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,75,a,b,c,r,al,w)              
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    heal=dmg/2
    if x.item=="Big Root":
        heal*=1.3
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and a!=0:
        x.hp-=heal
    else:
        x.hp+=heal             
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
    if a!=0:
        x.recharge=True
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
#Low Kick
async def lowkick(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Low Kick!")    
    x.atktype="Fighting"
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
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)              
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
    if dmg>y.hp:
        dmg=y.hp
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
        y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,160,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143327715232055336/image_search_1692660813022.gif")        
#Bloom Doom
async def bloomdoom(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bloom Doom!")        
    al=1
    r=await randroll()
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)    
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142420716990500964/image0.gif")        
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
#Genesis Supernova
async def genesissupernova(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Genesis Supernova!")        
    al=1
    r=await randroll()
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,185,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,185,a,b,c,r,al)            
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1140799716637016196/image0.gif")
    if field.terrain!="Psychic":
        field.terrain="Psychic"
        field.psyturn=turn
        field.psyend(x,y)
        em.add_field(name="Psychic Terrain",value="The battlefield got weird!")         
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
#G-Max Volt Crash
async def gmaxvoltcrash(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Volt Crash!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143332709792501820/IMG_20230822_055551.jpg")    
    paralyze(em,x,y,100)
#G-Max Stun Shock 
async def gmaxstunshock(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used G-Max Stun Shock!")        
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
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1147085420102955109/image0.gif")     
    ch=random.randint(1,2)         
    if ch==1 and y.item!="Covert Cloak":
        await paralyze(em,x,y,100) 
    if ch==2 and y.item!="Covert Cloak":
        await poison(em,x,y,100)
#Extreme Evoboost
async def evoboost(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Extreme Evoboost!")      
    await atkchange(em,x,x,2) 
    await defchange(em,x,x,2) 
    await spatkchange(em,x,x,2) 
    await spdefchange(em,x,x,2) 
    await speedchange(em,x,x,2)          
#Gigavolt Havoc
async def gigavolthavoc(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Gigavolt Havoc!")        
    al=1
    r=await randroll()
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,200,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,200,a,b,c,r,al)  
#Stoked Soarksurfer
async def sparksurf(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Stoked Sparksurfer!")        
    al=1
    r=await randroll()
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,175,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,175,a,b,c,r,al)                   
    if a!=0 and y.item!="Covert Cloak":         
        await paralyze(em,x,y,100)
#Guardian of Alola
async def guardianofalola(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Guardian of Alola!")    
    if y.hp==1:
        y.hp=0
    else:
        y.hp-=(y.hp*0.75)
#Catastropika
async def catastropika(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used Catastropika!")        
    al=1
    r=await randroll()
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if x.spatk>=x.atk:
        y.hp-=await special(x,x.level,x.spatk,y.spdef,210,a,b,c,r,al)
    elif x.spatk<x.atk:
        y.hp-=await special(x,x.level,x.atk,y.defense,210,a,b,c,r,al)      
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
#10,000,000 Volt Thunderbolt
async def tenmillionvolt(ctx,x,y,tr1,em,field,turn):  
    em.add_field(name=f"Move:",value=f"{x.nickname} used 10,000,000 Volt Thunderbolt!")
    al=1
    r=await randroll()
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.atk,y.defense,195,a,b,c,r,al)            
    em.set_image(url="https://media.tenor.com/ITqaLZeafGgAAAAd/10million-volt-thunderbolt.gif")           
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
        if dmg>y.hp:
            dmg=y.hp
        y.hp-=dmg
        heal=dmg/2
    if x.item=="Big Root":
        heal*=1.3
        if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
            x.hp-=heal
        else:
            x.hp+=heal       
#Strength Sap
async def strengthsap(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Strength Sap!")        
    if y.ability not in ["Clear Body","Big Pecks","White Smoke","Full Metal Body","Flower Veil"]:
        if y.atkb>-6:
            prev=x.atk
            await atkchange(em,y,x-1)
            x.hp+=prev
            if x.hp>=x.maxhp:
                x.hp=x.maxhp
        else:        
            em.add_field(name="Effect:",value="It failed!")                
#Leech Seed
async def leechseed(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Leech Seed!")        
    if "Grass" not in (y.primaryType,y.secondaryType,y.teraType) and y.ability!="Magic Bounce" and y.seeded is False:
        y.seeded=True
        em.add_field(name="Status:",value=f"{y.nickname} was seeded!")
    elif "Grass" not in (x.primaryType,x.secondaryType,x.teraType) and y.ability=="Magic Bounce" and x.seeded is False:
        x.seeded=True
        em.add_field(name=f"{y.nickname}'s {y.ability}!",value=f"{x.nickname} was seeded!")      
#Attack Order
async def attackorder(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Attack Order!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)                 
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
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    heal=dmg/2
    if x.item=="Big Root":
        heal*=1.3
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        x.hp-=heal
    else:
        x.hp+=heal            
#Dizzy Punch
async def dizzypunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dizzy Punch!")    
    x.atktype="Normal"
    base=70
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)     
    await confuse(em,x,y,20)    
#Dynamic Punch
async def dynamicpunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dynamic Punch!")    
    x.atktype="Fighting"
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,100,a,b,c,r,al)     
    await confuse(em,x,y,100)
#Drain Punch
async def drainpunch(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Drain Punch!")    
    x.atktype="Fighting"
    base=70
    if x.ability=="Iron Fist":
        al=1.3
        em.add_field(name=f"{x.icon} {x.nickname}'s Iron Fist!",value="")
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)              
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    heal=dmg/2
    if x.item=="Big Root":
        heal*=1.3
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"] and a!=0:
        x.hp-=heal
    else:
        x.hp+=heal 
#Petal Dance 
async def petaldance(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Petal Dance!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)         
    if x.fmove==False:
        x.fmove=True
        x.fmoveturn+=3
#Matcha Gotcha
async def matchagotcha(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Matcha Gotcha!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)          
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,20)
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    heal=dmg/2
    if x.item=="Big Root":
        heal*=1.3
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
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
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    heal=dmg/2
    if x.item=="Big Root":
        heal*=1.3
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        x.hp-=heal
    else:
        x.hp+=heal        
#Parabolic Charge
async def paraboliccharge(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Parabolic Charge!")    
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,75,a,b,c,r,al)          
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    heal=dmg/2
    if x.item=="Big Root":
        heal*=1.3
    if y.ability=="Liquid Ooze" and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        x.hp-=heal
    else:
        x.hp+=heal
#Draining Kiss
async def drainingkiss(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Draining Kiss!")    
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,50,a,b,c,r,al)          
    if dmg>y.hp:
        dmg=y.hp
    y.hp-=dmg
    heal=dmg*0.75
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
#Synthesis
async def synthesis(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Synthesis!")   
    if field.weather in ["Sunny","Extreme Sunlight"]:
        x.hp+=(x.maxhp*(2/3))
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    elif field.weather in ["Sandstorm","Hail","Rainy","Snowstorm"]:
        x.hp+=(x.maxhp/4)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp+=(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!") 
    if x.hp>x.maxhp:
        x.hp=x.maxhp 
        
#Morning Sun
async def morningsun(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Morning Sun!")   
    if field.weather in ["Sunny","Extreme Sunlight"]:
        x.hp+=(x.maxhp*(2/3))
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    elif field.weather in ["Sandstorm","Hail","Rainy","Snowstorm"]:
        x.hp+=(x.maxhp/4)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp+=(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!") 
    if x.hp>x.maxhp:
        x.hp=x.maxhp            
#Moonlight
async def moonlight(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Moonlight!")   
    if field.weather in ["Sunny","Extreme Sunlight"]:
        x.hp+=(x.maxhp*(2/3))
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    elif field.weather in ["Sandstorm","Hail","Rainy","Snowstorm"]:
        x.hp+=(x.maxhp/4)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp+=(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!") 
    if x.hp>x.maxhp:
        x.hp=x.maxhp             
#Shore Up
async def shoreup(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shore Up!")   
    if field.weather in ["Sunny","Extreme Sunlight"]:
        x.hp+=(x.maxhp/4)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    elif field.weather in ["Sandstorm","Hail","Rainy","Snowstorm"]:
        x.hp+=(x.maxhp*(2/3))
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp+=(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!") 
    if x.hp>x.maxhp:
        x.hp=x.maxhp         
#Jungle Healing
async def junglehealing(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Jungle Healing!")           
    if x.status!="Alive":
        x.status="Alive"
        em.add_field(name="Effect:",value=f"{x.nickname}'s status condition cured!")    
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")   
#Lunar Blessing
async def lunarblessing(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Lunar Blessing!")           
    if x.status!="Alive":
        x.status="Alive"
        em.add_field(name="Effect:",value=f"{x.nickname}'s status condition cured!")    
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")                
#Recover
async def recover(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Recover!")           
    if x.hp>=(x.maxhp/2):
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
    else:
        x.hp=x.hp+(x.maxhp/2)
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
#Rest
async def rest(ctx,x,y,tr1,em,field,turn):     
    em.add_field(name=f"Move:",value=f"{x.nickname} used Rest!")                
    if x.hp!=x.maxhp and x.status!="Sleep":
        x.hp=x.maxhp
        em.add_field(name="Heal:",value=f"{x.nickname} regained some of its health!")
        x.status="Sleep"
        x.sleepturn=2
    
#Strange Steam
async def strangesteam(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Strange Steam!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)             
    await confuse(em,x,y,20) 
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
        al*=1.33
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
        al*=1.33
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)             
    ch=random.randint(1,100)
    chance=10
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await spatkchange(em,y,x,-1)
#Light of Ruin
async def lightofruin(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Light of Ruin!")    
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,140,a,b,c,r,al)           
    y.hp-=(y.maxhp/2)
#Mind Blown
async def mindblown(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Mind Blown!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,140,a,b,c,r,al,w)           
    y.hp-=(y.maxhp/2)    
#Chloroblast
async def chloroblast(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Chloroblast!")    
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)           
    y.hp-=(y.maxhp/2)    
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
#Seismic Toss
async def seismictoss(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Seismic Toss!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if a!=0:
        y.hp-=x.level
#Night Shade
async def nightshade(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Night Shade!")    
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if a!=0:
        y.hp-=x.level        
#Aura Sphere
async def aurasphere(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aura Sphere!")    
    if x.ability=="Mega Launcher":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Mega Launcher!",value="")
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
        al*=1.33
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al)    
    await confuse(em,x,y,30)
#Air Slash
async def airslash(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Air Slash!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,75,a,b,c,r,al)    
    await flinch(em,x,y,30)
#Aeroblast
async def aeroblast(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aeroblast!")
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y,2)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al)       
#Bleakwind Storm
async def bleakwindstorm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bleakwind Storm!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,95,a,b,c,r,al)    
    await flinch(em,x,y,30)    
#Wildbolt Storm
async def wildboltstorm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Wildbolt Storm!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,95,a,b,c,r,al)    
    if a!=0 and y.item!="Covert Cloak":
        await paralyze(em,x,y,30)      
#Springtide Storm
async def springtidestorm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Springtide Storm!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fairy"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,95,a,b,c,r,al)     
#Sandsear Storm
async def sandsearstorm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sandsear Storm!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,95,a,b,c,r,al)      
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,30)       
#Scald
async def scald(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Scald!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al,w)    
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,30)     
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
#Electro Ball
async def electroball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Electro Ball!")
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=30*(1+(x.speed/y.speed))
    y.hp-=await special(x,x.level,x.spatk,y.spdef,base,a,b,c,r,al)        
#Zap Cannon
async def zapcannon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Zap Cannon!")
    if x.ability in ["Sheer Force","Mega Launcher"]:
        al=1.33
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al)                     
    if a!=0 and y.item!="Covert Cloak":
        await paralyze(em,x,y,100)    
#Inferno
async def inferno(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Inferno!")
    if x.ability in ["Sheer Force"]:
        al=1.33
    x.atktype="Fire"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    w=await weathereff(field,x,y,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,150,a,b,c,r,al,w)                     
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,100)            
#Thunder Cage
async def thundercage(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder Cage!")
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)         
    em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1143460359789871225/image0.gif")
    if a!=0 and x.trap==False:
        x.trap=True
        em.add_field(name="Effect:",value=f"{x.nickname} trapped {y.nickname}!")
#Thunderbolt
async def thunderbolt(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunderbolt!")
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)                     
    if a!=0 and y.item!="Covert Cloak":
        await paralyze(em,x,y,10)
#Nuzzle
async def nuzzle(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Nuzzle!")
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,20,a,b,c,r,al)                     
    if a!=0 and y.item!="Covert Cloak":
        await paralyze(em,x,y,100)    
#Thunder
async def thunder(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Thunder!")
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Electric"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)                     
    if a!=0 and y.item!="Covert Cloak":
        await paralyze(em,x,y,30)
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
    
#Diamond Storm
async def diamondstorm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Diamond Storm!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al)    
    ch=random.randint(1,100)
    if x.ability=="Serene Grace":
        ch/=2
    if ch<50:
        await spdefchange(em,y,x,-1)
#Ancient Power
async def ancientpower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Ancient Power!")    
    x.atktype="Rock"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,60,a,b,c,r,al)      
    ch=random.randint(1,100)
    chance=10
    if x.ability=="Serene Grace":
        chance/=2
    if x.ability!="Sheer Force" and ch<=chance:
        await atkchange(em,x,x,1)
        await defchange(em,x,x,1)
        await spatkchange(em,x,x,1)
        await spdefchange(em,x,x,1)
        await speedchange(em,x,x,1)
#Heat Wave
async def heatwave(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Heat Wave!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)    
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,10)
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
#Air Cutter
async def aircutter(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Air Cutter!")    
    if x.ability in ["Sharpness","Technician"]:
        al=1.5
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,60,a,b,c,r,al)  
#Aerial Ace
async def aerialace(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Aerial Ace!")    
    if x.ability in ["Sharpness","Technician"]:
        al=1.5
    x.atktype="Flying"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,60,a,b,c,r,al)           
#Blizzard
async def blizzard(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Blizzard!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Ice"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al)    
    await freeze(em,x,y,10)
#Sacred Fire
async def sacredfire(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sacred Fire!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,110,a,b,c,r,al,w)    
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,50)  
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
#Chilling Water
async def chillingwater(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Chilling Water!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,50,a,b,c,r,al,w)     
    if a!=0 or w!=0:
        await atkchange(em,y,x,-1)
#Dive
async def dive(ctx,x,y,tr1,em,field,turn):
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dive!")    
    if x.item=="Power Herb" or x.precharge is True:
        if x.item=="Power Herb":
            x.item+="[Used]"  
            em.add_field(name=f"Item:",value=f"{x.nickname} became fully charged due to its Power Herb.")  
        al=1
        r=await randroll() 
        x.atktype="Water"
        w=await weathereff(field,x,y,em)
        c=await isCrit(em,tr1,x,y)
        ab=await weakness(ctx,x,y,field,em)
        a=ab[0]
        b=ab[1]   
        y.hp-=await physical(x,x.level,x.atk,y.defense,90,a,b,c,r,al,w)   
        x.precharge=False
    else:
        em.add_field(name="Effect:",value=f"{x.nickname} hid underwater!") 
        x.precharge=True
        if x.ability=="Gulp Missile" and a!=0:
            n=""
            if x.hp<=(x.maxhp/2):
                n="Pikachu"
                x.sprite=x.sprite.replace("cramorant","cramorant-gorging")
            if x.hp>(x.maxhp/2):
                n="Arrokuda"
                x.sprite=x.sprite.replace("cramorant","cramorant-gulping")
            x.ability+=f"-{n}"
            em.add_field(name=f"Effect:",value=f"{x.nickname} caught a {n}!")          
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
            x.sprite=x.sprite.replace("cramorant","cramorant-gorging")
        if x.hp>(x.maxhp/2):
            n="Arrokuda"
            x.sprite=x.sprite.replace("cramorant","cramorant-gulping")
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
#Snipe Shot
async def snipeshot(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Snipe Shot!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y,4)
    ab=await weakness(ctx,x,y,field,em)
    if x.ability=="Mega Launcher":
        al*=1.5
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,70,a,b,c,r,al,w)               
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
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,30)
#Venoshock 
async def venoshock(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Venoshock!")    
    if x.ability=="Sheer Force":
        al*=1.33
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
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    await poison(em,x,y,30)
#Sludge Wave
async def sludgewave(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sludge Wave!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,95,a,b,c,r,al)      
    await poison(em,x,y,10)    
#Acid Spray
async def acidspray(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Acid Spray!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,40,a,b,c,r,al)      
    if x.ability!="Sheer Force" and a!=0:
        await spdefchange(em,y,x,-2)
#Dragon Pulse           
async def dragonpulse(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dragon Pulse!")    
    if x.ability=="Mega Launcher":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Mega Launcher!",value="")
    x.atktype="Dragon"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,85,a,b,c,r,al)   
#Dark Hole
async def darkhole(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dark Hole!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al)    
    if x.ability!="Sheer Force":    
        await sleep(em,x,y,40)
#Snarl 
async def snarl(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Snarl!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,65,a,b,c,r,al)    
    if x.ability!="Sheer Force":
        await spatkchange(em,y,x,-1)
#Dark Pulse           
async def darkpulse(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Dark Pulse!")    
    if x.ability=="Mega Launcher":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Mega Launcher!",value="")
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)         
    await flinch(em,x,y,20)
#Night Daze
async def nightdaze(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Night Daze!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al)         
    if x.ability!="Sheer Force":
        y.accuracy-=10
#Final Gambit
async def finalgambit(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Final Gambit!")    
    x.atktype="Fighting"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    if a!=0:
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
#Fire Spin
async def firespin(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Spin!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,35,a,b,c,r,al,w)          
    if y.firespin==False:
        y.firespin=turn+random.randint(2,5)
        em.add_field(name="Effect:",value=f"{y.nickname} was trapped in a vortex of fire.")
#Whirlpool
async def whirlpool(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Whirlpool!")    
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,35,a,b,c,r,al,w)          
    if y.whirlpool==False:
        y.whirlpool=turn+random.randint(2,5)
        em.add_field(name="Effect:",value=f"{y.nickname} was trapped in a whirlpool.")        
#Sand Tomb
async def sandtomb(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Sand Tomb!")    
    x.atktype="Ground"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,35,a,b,c,r,al)          
    if y.sandtomb==False:
        y.sandtomb=turn+random.randint(2,5)
        em.add_field(name="Effect:",value=f"{y.nickname} was trapped in a sand tomb.")
#Infestation
async def infestation(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Infestation!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,35,a,b,c,r,al)          
    if y.infestation==False:
        y.infestation=turn+random.randint(2,5)
        em.add_field(name="Effect:",value=f"{y.nickname} is being infested.")        
#Flamethrower
async def flamethrower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flamethrower!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al,w)     
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,10)
#Burning Jealousy
async def burningjealousy(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Burning Jealousy!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,70,a,b,c,r,al,w)         
    if a!=0 and x.ability!="Sheer Force" and (y.atkb>1 or y.defb>1 or y.spatkb>1 or y.spdefb>1 or y.speedb>1) and y.item!="Covert Cloak":
        await burn(em,x,y,100)
#Fusion Flare
async def fusionflare(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fusion Flare!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w) 
#Blue Flare
async def blueflare(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Blue Flare!")    
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fiery Wrath!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,130,a,b,c,r,al,w)
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,20)   
#Fiery Wrath
async def fierywrath(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fiery Wrath!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)       
    await flinch(em,x,y,20)
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
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)     
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,30)      
#Fire Blast
async def fireblast(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Fire Blast!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al,w)     
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,10) 
#Magma storm
async def magmastorm(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Magma Storm!")    
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,100,a,b,c,r,al,w)      
    if y.magmadmg is False:
        y.magmadmg=True
        x.magmaendturn=turn+random.choice(2,5)
        if x.item=="Binding Band":
            x.magmaendturn=turn+5
#Overheat
async def overheat(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Overheat!")    
    if x.ability=="Sheer Force":
        al*=1.33
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
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al,w)             
    if a!=0 and y.item!="Covert Cloak":
        x.recharge=True
        await burn(em,x,y,50)
#Hydro Cannon
async def hydrocannon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hydro Cannon!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Water"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al,w)             
    if a!=0 and y.item!="Covert Cloak":
        x.recharge=True
        await freeze(em,x,y,30)
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
        al*=1.33
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,160,a,b,c,r,al)             
    if a!=0 and y.item!="Covert Cloak":
        x.recharge=True
        await poison(em,x,y,50)
    
#Lava Plume
async def lavaplume(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Lava Plume!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al,w)     
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,30)     
#Pyro Ball
async def pyroball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Pyro Ball!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Fire"
    w=await weathereff(field,x,y,em)
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,120,a,b,c,r,al,w)     
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,10)     
    if x.name=="Cinderace":
        em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142743351947448380/cinderace-pyro-ball.gif")
#Flash Cannon
async def flashcannon(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Flash Cannon!")    
    if x.ability=="Mega Launcher":
        al=1.5
        em.add_field(name=f"{x.icon} {x.nickname}'s Mega Launcher!",value="")
    elif x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Steel"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    #spdefdrop
#Stored Power
async def storedpower(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Stored Power!")    
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=20*(1+x.atkb,x.defb,x.spatkb,x.spdefb,x.speedb)
    y.hp-=await special(x,x.level,x.spatk,y.spdef,base,a,b,c,r,al) 
#Hex
async def hex(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Hex!")
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.status!="Alive":
        al*=2
    y.hp-=await special(x,x.level,x.spatk,y.spdef,65,a,b,c,r,al)
#Infernal Parade
async def infernalparade(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Infernal Parade!")
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.status!="Alive":
        al*=2
    y.hp-=await special(x,x.level,x.spatk,y.spdef,65,a,b,c,r,al)        
    if a!=0 and y.item!="Covert Cloak":
        await burn(em,x,y,30)  
#Barb Barrage
async def barbbarrage(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Barb Barrage!")
    x.atktype="Poison"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    if y.status in ["Poisoned","Badly Poisoned"]:
        al*=2
    y.hp-=await physical(x,x.level,x.atk,y.defense,65,a,b,c,r,al)        
    if a!=0 and y.item!="Covert Cloak":
        await poison(em,x,y,30)          
#Power Trip
async def powertrip(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Power Trip!")    
    x.atktype="Dark"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    base=20*(1+x.atkb,x.defb,x.spatkb,x.spdefb,x.speedb)
    y.hp-=await physical(x,x.level,x.atk,y.defense,base,a,b,c,r,al)          
#Shadow Ball            
async def shadowball(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Shadow Ball!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Ghost"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)  
    chance=20
    if x.ability=="Serene Grace":
        chance/=2
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
        al*=1.33
    x.atktype="Psychic"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)              
    if a!=0:
        await speedchange(em,x,x,1)
#Pollen Puff   
async def pollenpuff(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Pollen Puff!")    
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    dmg=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)      
    if dmg>y.hp:
        dmg=y.hp
    x.hp+=dmg/3
    y.hp-=dmg    
#Signal Beam
async def signalbeam(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Signal Beam!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,75,a,b,c,r,al)    
    if x.ability!="Sheer Force":
        await comfuse(em,x,y,10)
#Bug Buzz            
async def bugbuzz(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Bug Buzz!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Bug"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,90,a,b,c,r,al)  
    chance=20
    if x.ability=="Serene Grace":
        chance/=2
    if x.speed>y.speed:
        ch=random.randint(1,100)            
        if ch>(100-chance) and a!=0 and x.ability!="Sheer Force":
            await spdefchange(em,y,x,-1)       
#Apple Acid
async def appleacid(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Apple Acid!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await special(x,x.level,x.spatk,y.spdef,80,a,b,c,r,al)  
    if x.ability!="Sheer Force" and a!=0:
        await spdefchange(em,y,x,-1)
#Grav Apple
async def gravapple(ctx,x,y,tr1,em,field,turn):
    al=1
    r=await randroll()
    em.add_field(name=f"Move:",value=f"{x.nickname} used Grav Apple!")    
    if x.ability=="Sheer Force":
        al*=1.33
    x.atktype="Grass"
    c=await isCrit(em,tr1,x,y)
    ab=await weakness(ctx,x,y,field,em)
    a=ab[0]
    b=ab[1]   
    y.hp-=await physical(x,x.level,x.atk,y.defense,80,a,b,c,r,al)  
    if x.ability!="Sheer Force" and a!=0:
        await defchange(em,y,x,-1)                    
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
        em.add_field(name=f"Move Effect:",value=f"All Pokémon that heard the song will faint in three turns!")
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
    y.hp-=await physical(x,x.level,x.atk,y.defense,dmg,a,b,c,r,al)
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
    y.hp-=await physical(x,x.level,x.atk,y.defense,dmg,a,b,c,r,al) 
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