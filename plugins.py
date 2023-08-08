import random
import discord
import sqlite3
from pokemon import *
from movelist import *
from trainers import *
from pokemon import calcst
from AI import *
from hiddenpower import *
megastones=("Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Ampharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite")

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
    
async def row(ctx,num,c):
    c.execute(f"select *,rowid from '{ctx.author.id}'")    
    hh=c.fetchall()
    num=hh[num-1][26]            
    return num        
async def pokonvert(ctx, member, num=None):
    if num is not None:
        num = int(num)
    dt = sqlite3.connect("pokemondata.db")
    db = sqlite3.connect("owned.db")
    cx = dt.cursor()
    c = db.cursor()
    c.execute(f"SELECT * FROM '{member.id}'")
    allmon=c.fetchall()
    if num==None:
        num=len(allmon)
        num=await row(ctx,num,c)
    c.execute(f"SELECT * FROM '{member.id}' where rowid={num}")
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
    return p,allmon

async def numberify(num):
    num = str(num)
    reversed_num = num[::-1]
    chunks = [reversed_num[i:i+3] for i in range(0, len(reversed_num), 3)]
    result = ','.join(chunks)[::-1]    
    return result
    
async def gensub(num, original_dict):
    sub_dict = {}

    start = (num - 1) * 15
    end = start + 15

    keys = list(original_dict.keys())[start:end]
    values = list(original_dict.values())[start:end]

    sub_dict = dict(zip(keys, values))

    return sub_dict
async def listtodic(lst):
    dict_count = {}    
    for element in lst:
        if element in dict_count:
            dict_count[element] += 1
        else:
            dict_count[element] = 1
    return dict_count
async def itemicon(itm):
    if itm=="None":
        return "<:000:1127112083792728074>"
    elif "Used" in itm:
        return "<:000:1127112083792728074>"
    else:
        try:
            db=sqlite3.connect("pokemondata.db")
            c=db.cursor()
            c.execute(f"select * from itemshop where item=='{itm}'")
            l=c.fetchone()
            return l[4]
        except:
            return "<:000:1127112083792728074>"
async def movect(move):
    if move in typemoves.maxmovelist:
        return "<:dynamax:1104646304904257647>"
    elif move in typemoves.physicalmoves:
        return "<:physical:1127210535289634866>"
    elif move in typemoves.statusmove:
        return "<:status:1127210505275183156>"
    else:
        return "<:special:1127210563685077022>"
async def movetypeicon(x,move,field="Normal"):
    types=("Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice","Psychic")
    res="Normal"
    for i in types:
        if move in eval(f"typemoves.{i.lower()}moves"):
            res=i
    typedic={
    "Normal":"<:normal:1127146220880674878>",
    "Bug":"<:bug:1127145792654802944>",
    "Dark":"<:dark:1127147091655938068>",
    "Dragon":"<:dragon:1127147065215029298>",
    "Electric":"<:electric:1127146987423289395>",
    "Fairy":"<:fairy:1127147120160411688>",
    "Fighting":"<:fighting:1127145305066971256>",
    "Fire":"<:fire:1127146792065183784>",
    "Flying":"<:flying:1127145341385457725>",
    "Ghost":"<:ghost:1127145829505966110>",
    "Grass":"<:grass:1127146939587235910>",
    "Ground":"<:ground:1127145407613517885>",
    "Ice":"<:ice:1127147039772381305>",
    "Poison":"<:poison:1127145374457536532>",
    "Psychic":"<:psychic:1127147015760007238>",
    "Rock":"<:rock:1127145761390473306>",
    "Steel":"<:steel:1127145866868830279>",
    "Water":"<:water:1127146821635027037>"
    }
    if move=="Hidden Power":
        dmg,res=await hidp(x.hpiv,x.atkiv,x.defiv,x.spatkiv,x.spdefiv,x.speediv) 
    elif x.ability=="Normalize":
        res="Normal"
    elif x.ability=="Liquid Voice" and move in typemoves.normalmoves:
        res="Water"
    elif x.ability=="Aerilate" and move in typemoves.normalmoves:
        res="Flying"
    elif x.ability=="Galvanize" and move in typemoves.normalmoves:
        res="Electric"
    elif x.ability=="Pixilate" and move in typemoves.normalmoves:
        res="Fairy"
    elif move in ["Revelation Dance","Multi-Attack","Judgment"]:
        res=x.primaryType
        if x.teraType!="???":
            res=x.teraType
    elif move=="Tera Blast" and x.teraType!="???":
        res=x.teraType     
    elif move=="Weather Ball":
        dict={
        "Rainy":"Water",
        "Sunny":"Fire",
        "Sandstorm":"Rock",
        "Hail":"Ice",
        "Snowstorm":"Ice"}
        if field!="Normal" and field.weather in dict:
            res=dict[field.weather]
        elif field=="Normal":
            res="Normal"
    return typedic[res]
async def typeicon(type):
    typedic={
    "Normal":"<:normal:1127146220880674878>",
    "Bug":"<:bug:1127145792654802944>",
    "Dark":"<:dark:1127147091655938068>",
    "Dragon":"<:dragon:1127147065215029298>",
    "Electric":"<:electric:1127146987423289395>",
    "Fairy":"<:fairy:1127147120160411688>",
    "Fighting":"<:fighting:1127145305066971256>",
    "Fire":"<:fire:1127146792065183784>",
    "Flying":"<:flying:1127145341385457725>",
    "Ghost":"<:ghost:1127145829505966110>",
    "Grass":"<:grass:1127146939587235910>",
    "Ground":"<:ground:1127145407613517885>",
    "Ice":"<:ice:1127147039772381305>",
    "Poison":"<:poison:1127145374457536532>",
    "Psychic":"<:psychic:1127147015760007238>",
    "Rock":"<:rock:1127145761390473306>",
    "Steel":"<:steel:1127145866868830279>",
    "Water":"<:water:1127146821635027037>"
    }
    return typedic[type]
async def teraicon(type):
    teradic={
    "Normal":"<:normal1:1127150698623160430>",
    "Bug":"<:bug:1127151936366444615>",
    "Dark":"<:dark:1127152336301727784>",
    "Dragon":"<:dragon:1127152300549484544>",
    "Electric":"<:electric:1127152165333508116>",
    "Fairy":"<:fairy:1127152370854416385>",
    "Fighting":"<:fighting1:1127150829896482888>",
    "Fire":"<:fire:1127152044919226420>",
    "Flying":"<:flying1:1127150885324193812>",
    "Ghost":"<:ghost:1127151976531107860>",
    "Grass":"<:grass:1127152121846968390>",
    "Ground":"<:ground:1127151843617808485>",
    "Ice":"<:ice:1127152260686811146>",
    "Poison":"<:poison:1127151807655858227>",
    "Psychic":"<:psychic:1127152223537856584>",
    "Rock":"<:rock:1127151897355231284>",
    "Steel":"<:steel:1127152009733226558>",
    "Water":"<:water:1127152085159399475>"
    }
    return teradic[type]    
async def entryeff(ctx, x, y, tr1, tr2, field, turn):
    entry = discord.Embed(title="Entry Effects:")
    em = None
    if x.item == "Blue Orb" and "Primal" not in x.name and x.name == "Kyogre":
        em = discord.Embed(title="Primal Reversion:", description=f"{x.name}'s Primal Reversion! It reverted to its primal form!")
        x.sprite = x.sprite.replace(".gif", "-primal.gif")
        x.name = "Primal Kyogre"
        per = x.hp / x.maxhp
        x.ability = "Primordial Sea"
        x.weight, x.hp, x.atk, x.defense, x.spatk, x.spdef, x.speed = 947.99, 100, 150, 90, 180, 160, 90
        calcst(x)
        x.hp = x.maxhp * per
        em.set_image(url=x.sprite)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1108653012680982568/Blue_Orb.png")    
    if x.item == "Red Orb" and "Primal" not in x.name and x.name == "Groudon":
        em = discord.Embed(title="Primal Reversion:", description=f"{x.name}'s Primal Reversion! It reverted to its primal form!")
        x.sprite = x.sprite.replace(".gif", "-primal.gif")
        x.name = "Primal Groudon"
        per = x.hp / x.maxhp
        x.ability = "Desolate Land"
        x.weight = 2203.96
        x.hp, x.atk, x.defense, x.spatk, x.spdef, x.speed = 100, 180, 160, 150, 90, 90
        calcst(x)
        x.hp = x.maxhp * per
        em.set_image(url=x.sprite)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1109011460601954364/Red_Orb.png")
    if x.ability == "Comatose":
        entry.add_field(name=f"{x.nickname}'s Comatose!", value=f"{x.nickname} is in a drowsy state.")
        x.status = "Drowsy"    
    if x.ability == "Flower Gift" and field.weather in ["Sunny", "Extreme Sunlight"] and "Cherrim" in x.name and x.sprite != "https://play.pokemonshowdown.com/sprites/ani/cherrim-sunshine.gif":
        entry.add_field(name=f"{x.nickname}'s Flower Gift!", value=f"{x.nickname} is reacting and absorbing sunlight!")
        x.sprite = "https://play.pokemonshowdown.com/sprites/ani/cherrim-sunshine.gif"
    elif x.ability == "Illusion":
        x.name = tr1.pokemons[-1].name
        x.nickname = tr1.pokemons[-1].nickname
        x.sprite = tr1.pokemons[-1].sprite
    elif x.ability == "Pressure" and y.ability not in ["Mold Breaker", "Teravolt", "Turboblaze", "Propeller Tail"]:
        entry.add_field(name=f"{x.nickname}'s Pressure!", value=f"{x.nickname} is exerting its pressure!")
    elif x.ability=="Supreme Overlord" and len(tr1.pokemons)!=0:
        entry.add_field(name=f"{x.nickname}'s Supreme Overlord!",value=f"{x.nickname} gained strength from the fallen!")  
    elif x.ability=="Frisk" and ("None" in y.item or "Used" not in y.item):
        entry.add_field(name=f"{x.nickname}'s Frisk!",value=f"{y.nickname} is holding a {y.item}!")      
    elif x.ability in ["Air Lock","Cloud Nine"] and field.weather!="Clear":       
        entry.add_field(name=f"{x.nickname}'s Air Lock!",value=f"{x.nickname} nullified the effects of weather!")   
    elif x.ability=="Delta Stream" and field.weather!="Strong Winds":        
        entry.add_field(name=f"{x.nickname}'s Delta Stream!",value=f"Mysterious strong winds are protecting Flying-type Pokémon!")  
        field.weather="Strong Winds"
    elif x.ability=="Stakeout":
        x.atk*=2
        x.spatk*=2
    elif x.ability=="Trace" and y.ability not in ["As One","Battle Bond","Commander","Disguise","Forecast","Ice Face","Imposter","Illusion","Multitype","Power of Alchemy","Protosynthesis","Stance Change","Quark Drive","RKS System","Schooling","Trace","Zen Mode","Zero to Hero"] and y.item!="Ability Shield":
        entry.add_field(name=f"{x.nickname}'s Trace!",value=f"{x.nickname} gained y.ability!") 
        await entryeff(ctx,x,y,tr1,tr2,field,turn)   
    elif "Quark Drive" in x.ability and field.terrain=="Electric" and ("Booster Energy" not in x.item or "Used" in x.item):    
        entry.add_field(name=f"{x.nickname}'s Quark Drive!",value=f"Electric Terrain activated {x.nickname}'s Quark Drive!")   
    elif "Protosynthesis" in x.ability and field.weather in ["Sunny","Extreme Sunlight"] and ("Booster Energy" not in x.item or "Used" in x.item):    
        entry.add_field(name=f"{x.nickname}'s Protosynthesis!",value=f"Harsh sunlight activated {x.nickname}'s Protosynthesis!")  
    elif x.ability=="Costar":
        x.atkb=y.atkb
        x.defb=y.defb
        x.spatkb=y.spatkb
        x.spdefb=y.spdefb
        x.speedb=y.speedb   
        entry.add_field(name=f"{x.nickname}'s Costar!",value=f"{x.nickname} copied {y.nickname}'s stat boosts!")         
    elif x.ability=="Imposter" and y.dmax is False and y.item not in megastones:    
        entry.add_field(name=f"{x.nickname}'s Imposter!",value=f"{x.nickname} transformed into {y.nickname}!")
        x.hp=round(y.maxhp*(x.hp/x.maxhp))     
        x.sprite=y.sprite
        x.maxhp=y.maxhp
        x.maxatk=y.maxatk
        x.maxdef=y.maxdef
        x.maxspatk=y.maxspatk
        x.maxspdef=y.maxspdef
        x.maxspeed=y.maxspeed    
        x.atk=y.atk
        x.defense=y.defense
        x.spatk=y.spatk
        x.spdef=y.spdef
        x.speed=y.speed    
        x.atkb=y.atkb
        x.defb=y.defb
        x.spatkb=y.spatkb
        x.spdefb=y.spdefb
        x.speedb=y.speedb
        x.moves=y.moves
        x.primaryType=y.primaryType
        x.secondaryType=y.secondaryType
        x.ability=y.ability
        x.name=x.name+f"({y.name})"
    elif (x.ability == "Sand Stream" or (x.ability=="Forecast" and x.item=="Smooth Rock")) and field.weather not in ["Sandstorm","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.nickname}'s Sand Stream!",value=f"️{x.nickname} whipped up a sandstorm!")
        field.weather="Sandstorm" 
        field.sandturn=turn
        field.sandend(x,y)        
    elif x.ability=="Primordial Sea" and field.weather!="Heavy Rain":  
        entry.add_field(name=f"{x.nickname}'s Primordial Sea!",value=f"️A heavy rain began to fall!")
        field.weather="Heavy Rain"
    elif x.ability=="Desolate Land" and field.weather!="Extreme Sunlight":  
        entry.add_field(name=f"{x.nickname}'s Desolate Land!",value=f"️The sunlight turned extremely harsh!")
        field.weather="Extreme Sunlight"   
    elif x.ability=="Drought" and field.weather not in ["Sunny","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.nickname}'s Drought!",value=f"️{x.nickname} intensified the sun's rays!")
        field.weather="Sunny"  
        field.sunturn=turn
        field.sunend(x,y)
    elif x.ability=="Orichalcum Pulse" and field.weather not in ["Sunny","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.nickname}'s Orichalcum Pulse!",value=f"️{x.nickname} turned the sunlight harsh, sending its ancient pulse into a frenzy!")
        field.weather="Sunny"  
        field.sunturn=turn
        field.sunend(x,y)    
    elif x.ability=="Drizzle" and field.weather not in ["Rainy","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.nickname}'s Drizzle!",value=f"️{x.nickname} made it rain!")
        field.weather="Rainy"  
        field.rainturn=turn
        field.rainend(x,y)     
    elif x.ability=="Snow Warning" and field.weather not in ["Snowstorm","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.nickname}'s Snow Warning!",value=f"️{x.nickname} whipped up a snowstorm!")
        field.weather="Snowstorm"  
        field.snowstormturn=turn
        field.snowstormend(x,y)   
    elif x.ability=="Electric Surge":
        entry.add_field(name=f"{x.nickname}'s Electric Surge!",value=f"️An electric x ran across the battlefield!")
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(x,y)  
    elif x.ability=="Hadron Engine":
        entry.add_field(name=f"{x.nickname}'s Hadron Engine!",value=f"️{x.nickname} summoned the Electric Terrain to energize its futuristic engine!")
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(x,y)       
    elif x.ability=="Misty Surge":
        entry.add_field(name=f"{x.nickname}'s Misty Surge!",value=f"️Mist swirled around the battlefield!")
        field.terrain="Misty"
        field.misturn=turn
        field.misend(x,y)     
    elif x.ability=="Grassy Surge":
        entry.add_field(name=f"{x.nickname}'s Grassy Surge!",value=f"️Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(x,y)   
    elif x.ability=="Psychic Surge":
        entry.add_field(name=f"{x.nickname}'s Psychic Surge!",value=f"️The battlefield got weird!")     
        field.terrain="Psychic"        
        field.psyturn=turn
        field.psyend(x,y)      
    if "Spikes" in tr1.hazard and x.ability not in ["Magic Guard","Levitate","Shield Dust"] and x.item not in ["Heavy-Duty Boots","Air Balloon"]:
        entry.add_field(name=f"Spikes!",value=f"️{x.nickname} was hurt by the Spikes!") 
        if tr1.hazard.count("Spikes")==3:
            x.hp-=(x.maxhp/4)
        if tr1.hazard.count("Spikes")==2:
            x.hp-=(x.maxhp/6)
        if tr1.hazard.count("Spikes")==1:
            x.hp-=(x.maxhp/8)        
    if "Toxic Spikes" in tr1.hazard and x.ability not in ["Magic Guard","Levitate","Shield Dust"] and x.item not in ["Heavy-Duty Boots","Air Balloon"] and "Steel" not in (x.primaryType,x.secondaryType,x.teraType) and x.status=="Alive":
        if "Poison" in (x.primaryType,x.secondaryType,x.teraType):
            tr1.hazard.remove("Toxic Spikes")
            entry.add_field(name=f"{x.nickname} is a part Poison-type!",value=f"️{x.nickname} absorbed the Toxic Spikes!") 
        else:
            if tr1.hazard.count("Toxic Spikes")==1:
                entry.add_field(name=f"Toxic Spikes!",value=f"️{x.nickname} was poisoned by toxic spikes!")
                x.status="Poisoned"
            if tr1.hazard.count("Toxic Spikes")>=2:
                entry.add_field(name=f"Toxic Spikes!",value=f"️{x.nickname} was badly poisoned by toxic spikes!")
                x.status="Badly Poisoned"                
    if "Sticky Web" in tr1.hazard and x.ability not in ["Magic Guard","Levitate","Shield Dust"] and x.item not in ["Heavy-Duty Boots","Air Balloon"]:
        entry.add_field(name=f"Sticky Web!",value=f"️{x.nickname} fell into the sticky web!")
        await speedchange(em,x,y,-0.5)        
    if "Stealth Rock" in tr1.hazard and x.ability not in ["Magic Guard","Levitate","Shield Dust","Mountaineer"] and x.item not in ["Heavy-Duty Boots","Air Balloon"]:
        buff=2
        if x.primaryType in ["Flying", "Bug", "Fire", "Ice"] and x.teraType=="None":
            buff*=2
        if x.secondaryType in ["Flying", "Bug", "Fire", "Ice"] and x.teraType=="None":
            buff*=2
        if x.teraType in ["Flying", "Bug", "Fire", "Ice"]:
            buff*=2
        if x.primaryType in ['Fighting', 'Ground', 'Steel'] and x.teraType=="None":
            buff=1
        if x.secondaryType in ['Fighting', 'Ground', 'Steel'] and x.teraType=="None":
            buff=1
        if x.teraType in ['Fighting', 'Ground', 'Steel']:
            buff=1
        x.hp-=(1+(x.maxhp*0.0625*buff))
        entry.add_field(name=f"Stealth Rock!",value=f"️Pointed stones dug into {x.nickname}!")
    await prebuff(ctx,x,y,tr1,tr2,turn,field)
    if len(entry.fields)!=0:
        await ctx.send(embed=entry)    
async def maxendturn(x,turn):
    if x.dmax is True:
       x.maxend=turn+2         
async def maxtrans(ctx,x,tr1,turn):
    x.dmax=True
    tr1.canmax=False
    em=discord.Embed(title=f"{tr1.name} dynamaxed {x.nickname}!")   
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1106824399983751248/Dynamax.png")
    if x.name in ("Charizard","Pikachu","Butterfree","Snorlax","Machamp","Gengar","Kingler","Lapras","Garbodor","Melmetal","Corviknight","Orbeetle","Drednaw","Coalossal","Copperajah","Flapple","Appletun","Sandaconda","Grimmsnarl","Hatterene","Toxtricity","Centiskorch","Alcremie","Duraludon","Single Strike Urshifu","Centiskorch","Meowth"):
        x.gsprite=x.sprite.replace(".gif","-gmax.gif")
    elif x.name=="Rapid Strike Urshifu":
        x.gsprite="https://pporg-cdn.nullcontent.net/monthly_2021_01/large.urshifu-rapid-strike-gigantamax.gif.4cb27a830aa200f328d5159491cf37d1.gif"    
    elif x.name=="Single Strike Urshifu":
        x.gsprite="https://pporg-cdn.nullcontent.net/monthly_2021_01/large.urshifu-gigantamax_002.gif.c5c2375142cfcf0d0fe6f53d8923a748.gif"       
    elif x.name=="Cinderace":
        x.gsprite="https://pporg-cdn.nullcontent.net/monthly_2021_01/large.815Cinderace-Gigantamax.png.115853e2114a6c98dd5909b7df2a9562.png"
    elif x.name=="Rillaboom":
        x.gsprite="https://cdn.discordapp.com/attachments/1102579499989745764/1120161218154475551/large.rillaboom-gigantamax.gif.8436bd055644be30e97a252e42166f26.gif"
    elif x.name=="Inteleon":
        x.gsprite="https://pporg-cdn.nullcontent.net/monthly_2021_01/large.poke_capture_0818_000_mf_g_00000000_f_r.png.61ed306f900ef5065e5cdfe4655300c1.png"
    elif x.name=="Venusaur":
        x.gsprite="https://pporg-cdn.nullcontent.net/monthly_2021_01/large.003Venusaur-Gigantamax.png.55d8fc03bb6f1a021deaf82dd16b7315.png"
    elif x.name=="Blastoise":
        x.gsprite="https://pporg-cdn.nullcontent.net/monthly_2021_01/large.009Blastoise-Gigantamax.png.d708478f1a8a467addd0944977d17bf6.png"        
    em.set_image(url=x.sprite)
    if x.gsprite!="None":
        em.set_image(url=x.gsprite)
    await maxendturn(x,turn)
    x.hp*=2
    x.maxhp*=2
    return x,em
async def teratrans(ctx,x,tr1):
    x.teraType=x.tera
    tr1.cantera=False
    x.name+="-"+x.tera
    em=discord.Embed(title="Terastallization:",description=f"{tr1.name} terastallized {x.nickname} into {x.teraType}-Type!")   
    em.set_thumbnail(url=f"https://play.pokemonshowdown.com/sprites/types/Tera{x.teraType}.png")
    em.set_image(url=x.sprite)
    if x.gsprite!="None":
        em.set_image(url=x.gsprite)
    return x,em
async def prebuff(ctx,x,y,tr1,tr2,turn,field):
    atkbuff=1
    defbuff=1
    spatkbuff=1
    spdefbuff=1
    speedbuff=1   
    pre=discord.Embed(title="Pre-move buffs:")
    if x.item=="Thick Club" and "Marowak" in x.name:
        atkbuff*=2
    if x.ability=="Schooling" and "School" not in x.name and x.hp>(x.maxhp*0.25):
        pre.add_field(name=f"{x.nickname}'s Schooling!",value="Wishiwashi formed a school!")
        x.name="School Wishiwashi"
        x.sprite="https://play.pokemonshowdown.com/sprites/ani/wishiwashi-school.gif"
        if x.shiny=="Yes":
            x.sprite="https://play.pokemonshowdown.com/sprites/ani-shiny/wishiwashi-school.gif"
        per=x.hp/x.maxhp
        x.hp=55
        x.atk=140
        x.defense=130
        x.spatk=140
        x.spdef=135
        x.speed=30
        calcst(x)
        x.hp=x.maxhp*per          
    if tr1.auroraveil is True:
        if turn==tr1.avendturn:
            tr1.auroraveil=False
            pre.add_field(name="Aurora Veil:",value="Aurora Veil wore off!")
        elif y.ability!="Infiltrator":
            defbuff*=2
            spdefbuff*=2        
    if tr1.tailwind is True:        
        if turn==tr1.twendturn:
            tr1.tailwind=False
            pre.add_field(name="Tailwind:",value="The Tailwind petered out!")
        else:
            speedbuff*=2     
    if tr1.reflect is True:
        if turn==tr1.rfendturn:
            tr1.reflect=False
            pre.add_field(name="Reflect:",value="Reflect wore off!")
        elif y.ability!="Infiltrator":
            defbuff*=2
    if tr1.lightscreen is True:
        if turn==tr1.screenend:
            tr1.lightscreen=False
            pre.add_field(name="Light Screen:",value="Light Screen wore off!")
        elif y.ability!="Infiltrator":
            spdefbuff*=2    
    if x.item=="Float Stone":
        defbuff*=0.5
        spdefbuff*=0.5
    if x.item=="Iron Ball":
        speedbuff*=0.5
    if x.item=="Wise Glasses":
        spatkbuff*=1.1            
    if x.item=="Muscle Band":
        atkbuff*=1.1
    if x.ability=="Zen Mode":
        if "Zen" not in x.name:
            pre.add_field(name=f"{x.nickname}'s Zen Mode!",value=f"{x.nickname} transformed!")
            x.name+="-Zen"
            if "Galarian" in x.name:
                x.primaryType,x.secondaryType="Ice","Fire"
                per=x.hp/x.maxhp
                x.sprite="https://play.pokemonshowdown.com/sprites/ani/darmanitan-galarzen.gif"
                x.hp=105
                x.atk=160
                x.defense=55
                x.spatk=30
                x.spdef=55
                x.speed=135
                calcst(x)
                x.hp=x.maxhp*per
            if "Galarian" not in x.name:
                x.primaryType,x.secondaryType="Fire","Psychic"
                sprite="https://play.pokemonshowdown.com/sprites/ani/darmanitan-zen.gif"
                per=x.hp/x.maxhp
                x.hp=105
                x.atk=30
                x.defense=105
                x.spatk=140
                x.spdef=105
                x.speed=55
                calcst(x)
                x.hp=x.maxhp*per   
    if x.ability=="Flower Gift" and field.weather in ["Sunny","Extreme Sunlight"]:
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/cherrim-sunshine.gif"
        speedbuff*=1.5
        atkbuff*=1.5
    if x.ability=="Illusion" and "Zoroark" not in x.name:
        atkbuff*=1.3
        spatkbuff*=1.3
    if x.ability=="Quick Feet" and x.status!="Alive":
            speedbuff*=2
    if x.ability in ["Bull Rush","Quill Rush"] and x.bullrush==True:
            speedbuff*=1.5
            atkbuff*=1.2
            x.bullrush=False
    if field.weather=="Strong Winds" and "Delta Stream" not in (x.ability,y.ability):
            pre.add_field(name="Delta Stream Faded!",value="The mysterious strong winds have dissipated!")
            field.weather="Clear"
    if y.ability=="Screen Cleaner":
        tr1.lightscreen=False
        tr1.reflect=False
        tr1.auroraveil=False   
    if x.ability=="Unburden" and (x.item=="None" or "Used" in x.item):
        speedbuff*=2
    if x.ability=="Grass Pelt" and field.terrain=="Grassy":
        defbuff*=1.5
    if x.ability=="Forecast":
        if field.weather=="Clear":
            x.primaryType="Normal"
            x.sprite="https://play.pokemonshowdown.com/sprites/ani/castform.gif"
        if field.weather=="Snowstrom":
            x.primaryType="Ice"
            x.sprite="https://play.pokemonshowdown.com/sprites/ani/castform-snowy.gif"
        if field.weather=="Rainy":
            x.primaryType="Water"
            x.sprite="https://play.pokemonshowdown.com/sprites/ani/castform-rainy.gif"
        if field.weather=="Sunny":
            x.primaryType="Fire"
            x.sprite="https://play.pokemonshowdown.com/sprites/ani/castform-sunny.gif"     
    if x.ability=="Defeatist" and x.hp<=(x.maxhp/3):
        atkbuff*=0.5
        spatkbuff*=0.5
    if "Poison" in x.status and x.ability=="Toxic Boost":
        atkbuff*=1.5
    if x.ability=="Supreme Overlord":
        atkbuff*=1+0.1*(6-len(tr1.pokemons))
        spatkbuff*=1+0.1*(6-len(tr1.pokemons))
    if field.weather in ["Sunny","Extreme Sunlight"] and x.ability=="Orichalcum Pulse":
        atkbuff*=1.34
    if field.terrain=="Electric" and x.ability=="Hadron Engine":
        spatkbuff*=1.34
    if ("Protosynthesis" in x.ability and (field.weather in ["Sunny","Extreme Sunlight"] or x.item=="Booster Energy")) or x.ability in ["Protosynthesis [Attack]","Protosynthesis [Sp. Attack]","Protosynthesis [Defense]","Protosynthesis [Sp. Defense]","Protosynthesis [Speed]"]:
        if field.weather not in ["Sunny","Extreme Sunlight"] and "[" not in x.ability:
            itemicon(x.item)
            pre.add_field(name="Booster Energy:",value=f"{x.nickname} used its Booster Energy to activate Protosynthesis!")
            x.item+="[Used]"
        m=[a,b,c,d,e]=[x.atk,x.defense,x.spatk,x.spdef,x.speed]
        if tr1.reflect==True:
            m=[x.atk,x.defense/2,x.spatk,x.spdef,x.speed]
        if tr1.lightscreen==True:
            m=[x.atk,x.defense,x.spatk,x.spdef/2,x.speed]
        z=max(m)
        if z==a or "[Attack" in x.ability:
        	atkbuff*=1.3
        	x.ability="Protosynthesis [Attack]"
        elif z==b or "[Defense" in x.ability:
        	defbuff*=1.3
        	x.ability="Protosynthesis [Defense]"
        elif z==c or "[Sp. Attack" in x.ability:
        	spatkbuff*=1.3
        	x.ability="Protosynthesis [Sp. Attack]"
        elif z==d or "[Sp. Defense" in x.ability:
        	spdefbuff*=1.3
        	x.ability="Protosynthesis [Sp. Defense]"
        elif z==e or "Speed" in x.ability:
        	speedbuff*=1.5
        	x.ability="Protosynthesis [Speed]"
    if ("Quark Drive" in x.ability and (field.terrain=="Electric" or x.item=="Booster Energy")) or x.ability in ["Quark Drive [Attack]","Quark Drive [Sp. Attack]","Quark Drive [Defense]","Quark Drive [Sp. Defense]","Quark Drive [Speed]"]:
        if field.terrain not in ["Electric"] and "[" not in x.ability:
            itemicon(x.item)
            pre.add_field(name="Booster Energy:",value=f"{x.nickname} used its Booster Energy to activate Quark Drive!")
            x.item+="[Used]"
        m=[a,b,c,d,e]=[x.atk,x.defense,x.spatk,x.spdef,x.speed]
        if tr1.reflect==True:
            m=[x.atk,x.defense/2,x.spatk,x.spdef,x.speed]
        if tr1.lightscreen==True:
            m=[x.atk,x.defense,x.spatk,x.spdef/2,x.speed]
        z=max(m)
        if z==a or "[Attack" in x.ability:
        	atkbuff*=1.3
        	x.ability="Quark Drive [Attack]"
        elif z==b or "[Defense" in x.ability:
        	defbuff*=1.3
        	x.ability="Quark Drive [Defense]"
        elif z==c or "[Sp. Attack" in x.ability:
        	spatkbuff*=1.3
        	x.ability="Quark Drive [Sp. Attack]"
        elif z==d or "[Sp. Def" in x.ability:
        	spdefbuff*=1.3
        	x.ability="Quark Drive [Sp. Defense]"
        elif z==e or "Speed" in x.ability:
        	speedbuff*=1.5
        	x.ability="Quark Drive [Speed]"
    if y.ability=="Vessel of Ruin":
        spatkbuff*=0.75
    if y.ability=="Tablets of Ruin":
        atkbuff*=0.75
    if y.ability=="Sword of Ruin":
        defbuff*=0.75
    if y.ability=="Beads of Ruin":
        spdefbuff*=0.75        	
    if x.ability=="Guts" and x.status!="Alive":
        atkbuff*=1.5
    if x.ability=="Feline Prowess":
        spatkbuff*=2
    if field.terrain=="Electric" and x.ability=="Surge Surfer":
        speedbuff*=2
    if x.status=="Paralyzed" and x.ability!="Quick Feet":
        speedbuff*=0.5
    if x.status=="Frostbite":
        spatkbuff*=0.5
    if x.status=="Burned" and x.ability!="Guts":
        atkbuff*=0.5
    if "Pikachu"in x.name and x.item=="Light Ball":
        atkbuff*=2
        spatkbuff*=2
    if x.ability=="Marvel Scale" and x.status!="Alive":
        defbuff*=1.5
    if x.ability=="Hustle":
        atkbuff*=1.5
    if x.ability=="Flare Boost" and x.status=="Burned":
        spatkbuff*=1.5
    if field.weather in ["Rainy","Heavy Rain"] and x.ability=="Swift Swim" and "Cloud Nine" not in (x.ability,y.ability):
        speedbuff*=2
    if field.weather in ["Sunny","Extreme Sunlight"] and x.ability=="Chlorophyll" and "Cloud Nine" not in (x.ability,y.ability):
        speedbuff*=2
    if field.weather in ["Sandstorm"] and x.ability=="Sand Rush" and "Cloud Nine" not in (x.ability,y.ability):
        speedbuff*=2
    if field.weather in ["Hail","Snowstorm"] and x.ability=="Slush Rush" and "Cloud Nine" not in (x.ability,y.ability):
        speedbuff*=2
    if field.weather in ["Snowstorm"] and ("Ice" in (x.primaryType,x.secondaryType,x.teraType)) and "Cloud Nine" not in (x.ability,y.ability):
        defbuff*=1.5
    if field.weather in ["Sandstorm"] and ("Rock" in (x.primaryType,x.secondaryType,x.teraType)) and "Cloud Nine" not in (x.ability,y.ability):
        spdefbuff*=1.5
    if y.ability=="Fur Coat":
        atkbuff*=0.5
    if x.ability=="Ice Scales":
        spdefbuff*=2
    if x.ability=="Sage Power":
        spatkbuff*=1.5
    if x.ability=="Gorilla Tactics":
        atkbuff*=1.5
    if x.item=="Choice Band" and x.dmax is False:
        atkbuff*=1.5
    if x.item=="Choice Specs" and x.dmax is False:
        spatkbuff*=1.5
    if x.item=="Choice Scarf" and x.dmax is False:
        speedbuff*=1.5
    if x.item=="Assault Vest":
        spdefbuff*=1.5
    if x.ability=="Typeless":
        x.primaryType=x.atktype
    if x.ability in ["Huge Power","Pure Power"]:
        atkbuff*=2
    if x.item=="Life Orb":
        atkbuff*=1.3
        spatkbuff*=1.3
    if x.item=="Eviolite":
        defbuff*=1.5
        spdefbuff*=1.5
    muldict={1:1.5,2:2,3:2.5,4:3,5:3.5,6:4,0:1,-1:0.66,-2:0.5,-3:0.4,-4:0.33,-5:0.29,-6:0.25}
    x.atk=x.maxatk*atkbuff*muldict[x.atkb]
    x.defense=x.maxdef*defbuff*muldict[x.defb]
    x.spatk=x.maxspatk*spatkbuff*muldict[x.spatkb]
    x.spdef=x.maxspdef*spdefbuff*muldict[x.spdefb]
    x.speed=x.maxspeed*speedbuff*muldict[x.speedb] 
    #await ctx.send(embed=pre)     
    
async def action(bot, ctx, tr1, tr2, x, y):
    if tr1.ai:
        if x.item not in megastones and tr1.canmax and x.teraType == "???":
            maxch = random.randint(1, 6)
            return 8 if maxch == 1 else 1
        if x.item in megastones and tr1.canmega:
            return 6
        elif x.tera != "???" and x.tera not in (x.primaryType, x.secondaryType) and tr1.cantera:
            return 9
        else:
            return random.choices([1, 2], weights=[10, 1], k=1)[0]
    else:
        inaction = None
        while True:
            des = "#1 💥 Fight\n#2 🔁 Switch\n#3 🚫 Forfeit\n"
            if tr1.canmega and not x.dmax and x.item in megastones and x.teraType == "???":
                des += "#6 <:megaevolve:1104646688951500850> Mega Evolve\n"
            if not x.dmax and x.item == "Ultranecrozium-Z" and "Ultra" not in x.name:
                des += "#7 Ultra Burst\n"
            if tr1.canmax and not x.dmax and x.item not in megastones and x.teraType == "???":
                des += "#8 <:dynamax:1104646304904257647> Dynamax/Gigantamax\n"
            if tr1.cantera and not x.dmax and x.item not in megastones and x.teraType == "???":
                des += f"#9 {await teraicon(x.tera)} Terastallize\n"
            em = discord.Embed(title=f"{tr1.name}, what do you wanna do?", description=des)
            em.set_footer(text="Wait a few seconds before entering your action. Re-enter action if it's not working.")
            if tr2.ai:
                await ctx.send(embed=em)
                inaction = await bot.wait_for('message', check=lambda msg: msg.author == ctx.author)
            else:
                await tr1.member.send(embed=em)
                inaction = await bot.wait_for('message', check=lambda msg: isinstance(msg.channel, discord.DMChannel) and msg.author == tr1.member)
            inaction = int(inaction.content)
#            except ValueError:
#                inaction = None
            if inaction is not None:
                break
        return inaction
         
async def score(ctx, x, y, tr1, tr2, turn, bg):
    hpbar = "<:HP:1107296292243255356>" + "<:GREY:1107331848360689747>" * 10 + "<:END:1107296362988580907>"
    status_mapping = {
        "Frostbite": "<:FBT:1107340620097404948>",
        "Frozen": "<:FZN:1107340597980827668>",
        "Sleep": "<:SLP:1107340641882603601>",
        "Drowsy": "<:SLP:1107340641882603601>",
        "Paralyzed": "<:YELLOW:1107331825929556111>",
        "Burned": "<:BRN:1107340533518573671>",
        "Poisoned": "<:PSN:1107340504762437723>",
        "Badly Poisoned":"<:PSN:1107340504762437723>"
    }
    if x.status in status_mapping:
        hpbar = "<:HP:1107296292243255356>" + status_mapping[x.status] * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    if x.status == "Alive":
        if 0.6 < (x.hp / x.maxhp) <= 1:
            hpbar = "<:HP:1107296292243255356>" + "<:GREEN:1107296335780139113>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        if 0.3 < (x.hp / x.maxhp) <= 0.6:
            hpbar = "<:HP:1107296292243255356>" + "<:YELLOW:1107331825929556111>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        if 0 < (x.hp / x.maxhp) <= 0.3:
            hpbar = "<:HP:1107296292243255356>" + "<:RED:1107331787480379543>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    em = discord.Embed(
        title=f"{tr1.name}:",
        description=f"**{x.nickname}** Lv. {x.level}\n**HP:** {round(x.hp)}/{x.maxhp} ({round((x.hp/x.maxhp)*100,2)}%)",
        color=bg,
    )
    em.add_field(name="HP Bar:", value=hpbar)
    em.set_image(url=x.sprite)
    if x.gsprite != "None":
        em.set_image(url=x.gsprite)
    await ctx.send(embed=em)
    
async def advscore(ctx, x, y, tr1, tr2, turn, bg):
    hpbar = "<:HP:1107296292243255356>" + "<:GREY:1107331848360689747>" * 10 + "<:END:1107296362988580907>"
    status_mapping = {
        "Frostbite": "<:FBT:1107340620097404948>",
        "Frozen": "<:FZN:1107340597980827668>",
        "Sleep": "<:SLP:1107340641882603601>",
        "Drowsy": "<:SLP:1107340641882603601>",
        "Paralyzed": "<:YELLOW:1107331825929556111>",
        "Burned": "<:BRN:1107340533518573671>",
        "Poisoned": "<:PSN:1107340504762437723>",
        "Badly Poisoned":"<:PSN:1107340504762437723>"
    }
    if x.status in status_mapping:
        hpbar = "<:HP:1107296292243255356>" + status_mapping[x.status] * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    if x.status == "Alive":
        if 0.6 < (x.hp / x.maxhp) <= 1:
            hpbar = "<:HP:1107296292243255356>" + "<:GREEN:1107296335780139113>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        if 0.3 < (x.hp / x.maxhp) <= 0.6:
            hpbar = "<:HP:1107296292243255356>" + "<:YELLOW:1107331825929556111>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        if 0 < (x.hp / x.maxhp) <= 0.3:
            hpbar = "<:HP:1107296292243255356>" + "<:RED:1107331787480379543>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    em = discord.Embed(
        title=f"{tr1.name}:",
        description=f"**{x.nickname}** Lv. {x.level}\n**HP:** {round(x.hp)}/{x.maxhp} ({round((x.hp/x.maxhp)*100,2)}%)\n**Status:** {x.status}\n**Ability:** {x.ability}\n**Held Item:** {x.item}\n**Attack:** {round(x.atk)}({x.atkb}) **Defense:** {round(x.defense)}({x.defb}) **Sp. Atk:** {round(x.spatk)}({x.spatkb}) **Sp. Def:** {round(x.spdef)}({x.spdefb}) **Speed:** {round(x.speed)}({x.speedb})",color=bg)
    em.add_field(name="HP Bar:",value=hpbar)
    em.set_image(url=x.sprite)
    if x.gsprite!="None":
        em.set_image(url=x.gsprite)
    if tr2.ai==False:
        await tr1.member.send(embed=em)
    if tr2.ai==True:
        await ctx.send(embed=em)
        
async def movelist(ctx,x,tr1,tr2,field):
    move=""
    if x.dmax==False:
        for i in range(len(x.moves)):
            if i!=len(x.moves)-1:
                move+=f"{i+1}. {await movetypeicon(x,x.moves[i],field)} {x.moves[i]} {await movect(x.moves[i])} PP: {x.pplist[x.moves.index(x.moves[i])]}\n"
            elif i==len(x.moves)-1:
                move+=f"{i+1}. {await movetypeicon(x,x.moves[i],field)} {x.moves[i]} {await movect(x.moves[i])} PP: {x.pplist[x.moves.index(x.moves[i])]}"
    elif x.dmax==True:
        for i in range(len(x.maxmoves)):
            if i!=len(x.maxmoves)-1:
                move+=f"{i+1}. {await movetypeicon(x,x.maxmoves[i],field)} {x.maxmoves[i]} {await movect(x.maxmoves[i])} PP: {x.pplist[x.maxmoves.index(x.maxmoves[i])]}\n"
            elif i==len(x.maxmoves)-1:
                move+=f"{i+1}. {await movetypeicon(x,x.maxmoves[i],field)} {x.maxmoves[i]} {await movect(x.maxmoves[i])} PP: {x.pplist[x.maxmoves.index(x.maxmoves[i])]}"  
    em=discord.Embed(title=f"What will {x.nickname} use?:",description=move,color=0xff0000)   
    if tr2.ai==False:            
        await tr1.member.send(embed=em)
    if tr2.ai==True:
        await ctx.send(embed=em)
       
async def fchoice(ctx,bot,x,y,tr1,tr2,field):
    if tr1.ai==True:
        choice=await moveAI(x,y,tr1,tr2,field)
        return choice[0]
    if tr1.ai==False:
        await movelist(ctx,x,tr1,tr2,field)    
        if tr2.ai==True:
            while True:
                choice=await bot.wait_for('message')
                if choice.content not in ["1","2","3","4"] and choice.author==ctx.author:
                    await tr1.member.send("Wrong Input.")
                if choice.content in ["1","2","3","4"] and choice.author==ctx.author:
                    num=int(choice.content)-1
                    if "Choice" in x.item and x.choiced=="None" and x.dmax==False:
                        try:
                            choice=x.moves[num]
                            x.choiced=True
                            x.choicedmove=choice
                            return choice  
                        except:
                            await tr1.member.send("Wrong Input.")
                    if "Choice" in x.item and x.choiced!="None" and x.dmax==False:
                        try:
                            x.choiced=True
                            choice=x.moves[x.moves.index(x.choicedmove)]
                            return choice  
                        except:
                            choice="Struggle"
                            return choice       
                    if x.dmax==True:
                        try:
                             choice=x.maxmoves[num]
                             return choice 
                        except:     
                             await tr1.member.send("Wrong Input.")   
                    if "Assault Vest" in x.item:
                        try:
                            choice=x.moves[num]      
                            if choice in typemoves.statusmove:
                                await tr1.member.send("Cannot use status moves while holding Assault Vest")   
                            else:
                                return choice
                        except:
                             await tr1.member.send("Wrong Input.")   
                    if len(x.moves)==0 or len(x.maxmoves)==0:
                        return "Struggle" 
                    else:
                        try:
                            choice=x.moves[num] 
                            return choice 
                        except:  
                            await tr1.member.send("Wrong Input.") 
        if tr2.ai==False:
            def check(message):
                return isinstance(message.channel,discord.DMChannel) and message.author==tr1.member
            while True:
                choice=await bot.wait_for('message',check=check)
                if choice.content not in ["1","2","3","4"]:
                    await tr1.member.send("Wrong Input.")
                if choice.content in ["1","2","3","4"]:
                    num=int(choice.content)-1
                    if "Choice" in x.item and x.choiced=="None" and x.dmax==False:
                        try:
                            choice=x.moves[num]
                            x.choiced=choice
                            return choice  
                        except:
                            await tr1.member.send("Wrong Input.")
                    if "Choice" in x.item and x.choiced!="None" and x.dmax==False:
                        try:
                            choice=x.moves[x.moves.index(x.choiced)]
                            return choice  
                        except:
                            choice="Struggle"
                            return choice       
                    if x.dmax==True:
                        try:
                             choice=x.maxmoves[num]
                             return choice 
                        except:     
                             await tr1.member.send("Wrong Input.")   
                    if "Assault Vest" in x.item:
                        try:
                            choice=x.moves[num]      
                            if choice in typemoves.statusmove:
                                await tr1.member.send("Cannot use status moves while holding Assault Vest")   
                            else:
                                return choice
                        except:
                             await tr1.member.send("Wrong Input.")   
                    if len(x.moves)==0 or len(x.maxmoves)==0:
                        return "Struggle" 
                    else:
                        try:
                            choice=x.moves[num] 
                            return choice 
                        except:  
                            await tr1.member.send("Wrong Input.") 
                      
async def megatrans(ctx,x,y,tr1,tr2,field,turn):
    des=f"{x.nickname}'s {x.item} is reacting to {tr1.name}'s Keystone!\n{x.name} has Mega Evolved into Mega {x.name}!"
    if x.name not in ["Mewtwo","Charizard"]:
        x.sprite=x.sprite.replace(".gif","-mega.gif")
    if "Rayquaza" in x.name:
        des=f"{tr1.nams}'s fervent wish has reached {x.name}!\n{prevname} Mega evolved into Mega {x.name}!"
    em=discord.Embed(title="Mega Evolution:",description=des) 
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1108284098641940521/Mega.png")
    tr1.canmega=False
    if True:
        if x.item=="Gyaradosite" and "Gyarados" in x.name:
            x.secondaryType="Dark"
            x.ability="Mold Breaker"
            per=x.hp/x.maxhp
            x.weight=672.41
            x.hp=95
            x.atk=155
            x.defense=109
            x.spatk=70
            x.spdef=130
            x.speed=81
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Venusaurite" and "Venusaur" in x.name:
            x.ability="Thick Fat"
            x.weight=342.82
            per=x.hp/x.maxhp
            x.hp=80
            x.atk=100
            x.defense=123
            x.spatk=122
            x.spdef=120
            x.speed=80
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Charizardite X" and "Charizard" in x.name:
            x.ability="Tough Claws"
            x.secondaryType="Dragon"
            x.weight=243.61
            x.sprite=x.sprite.replace(".gif","-megax.gif")
            per=x.hp/x.maxhp
            x.hp=78
            x.atk=130
            x.defense=111
            x.spatk=130
            x.spdef=130
            x.speed=100
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Charizardite Y" and "Charizard" in x.name:
            x.ability="Drought"
            x.weight=221.56
            per=x.hp/x.maxhp
            x.sprite=x.sprite.replace(".gif","-megay.gif")
            x.hp=78
            x.atk=104
            x.defense=78
            x.spatk=159
            x.spdef=115
            x.speed=100
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Blastoisinite" and "Blastoise" in x.name:
            x.ability="Mega Launcher"
            x.weight=222.89
            per=x.hp/x.maxhp
            x.hp=79
            x.atk=103
            x.defense=120
            x.spatk=135
            x.spdef=115
            x.speed=78
            calcst(x)
            x.hp=x.maxhp*per    
        if x.item=="Beedrillite" and "Beedrill" in x.name:
            x.ability="Adaptability"
            x.weight=89.29
            per=x.hp/x.maxhp
            x.hp=65
            x.atk=150
            x.defense=40
            x.spatk=15
            x.spdef=80
            x.speed=145
            calcst(x)
            x.hp=x.maxhp*per      
        if x.item=="Pidgeotite" and "Pidgeot" in x.name:
            x.ability="No Guard"
            x.weight=111.33
            per=x.hp/x.maxhp
            x.hp=83
            x.atk=80
            x.defense=80
            x.spatk=135
            x.spdef=80
            x.speed=121
            calcst(x)
            x.hp=x.maxhp*per     
        if x.item=="Alakazite" and "Alakazam" in x.name:
            x.ability="Trace"
            x.weight=105.82
            per=x.hp/x.maxhp
            x.hp=55
            x.atk=50
            x.defense=65
            x.spatk=175
            x.spdef=105
            x.speed=150
            calcst(x)
            x.hp=x.maxhp*per  
        if x.item=="Slowbronite" and "Slowbro" in x.name:
            x.ability="Regenerator"
            x.weight=264.55
            per=x.hp/x.maxhp
            x.hp=95
            x.atk=75
            x.defense=180
            x.spatk=130
            x.spdef=80
            x.speed=30
            calcst(x)
            x.hp=x.maxhp*per 
        if x.item=="Gengarite" and "Gengar" in x.name:
            x.ability="Shadow Tag"
            x.weight=89.29
            per=x.hp/x.maxhp
            x.hp=60
            x.atk=65
            x.defense=80
            x.spatk=170
            x.spdef=95
            x.speed=130
            calcst(x)
            x.hp=x.maxhp*per       
        if x.item=="Kangaskhanite" and "Kangaskhan" in x.name:
            x.ability="Parental Bond"
            x.weight=220.46
            per=x.hp/x.maxhp
            x.hp=105
            x.atk=125
            x.defense=100
            x.spatk=60
            x.spdef=100
            x.speed=100
            calcst(x)
            x.hp=x.maxhp*per       
        if x.item=="Pinsirite" and "Pinsir" in x.name:
            x.ability="Aerilate"
            x.secondaryType="Flying"
            x.weight=130.07
            per=x.hp/x.maxhp
            x.hp=65
            x.atk=155
            x.defense=130
            x.spatk=65
            x.spdef=90
            x.speed=105
            calcst(x)
            x.hp=x.maxhp*per         
        if x.item=="Aerodactylite" and "Aerodactyl" in x.name:
            x.ability="Tough Claws"
            x.weight=174.17
            per=x.hp/x.maxhp
            x.hp=80
            x.atk=135
            x.defense=85
            x.spatk=70
            x.spdef=95
            x.speed=150
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Mewtwonite X" and "Mewtwo" in x.name:
            x.ability="Steadfast"
            x.secondaryType="Fighting"
            x.weight=279.99
            x.sprite=x.sprite.replace(".gif","-megax.gif")
            per=x.hp/x.maxhp
            x.hp=106
            x.atk=190
            x.defense=100
            x.spatk=154
            x.spdef=100
            x.speed=130
            calcst(x)
            x.hp=x.maxhp*per    
        if x.item=="Mewtwonite Y" and "Mewtwo" in x.name:
            x.ability="Insomnia"
            x.sprite=x.sprite.replace(".gif","-megay.gif")
            x.weight=72.75
            per=x.hp/x.maxhp
            x.hp=106
            x.atk=150
            x.defense=70
            x.spatk=194
            x.spdef=120
            x.speed=140
            calcst(x)
            x.hp=x.maxhp*per     
        if x.item=="Ampharosite":
            x.ability=random.choice(["Thick Fat","Mold Breaker"])
            x.secondaryType="Dragon"
            x.weight=135.58
            per=x.hp/x.maxhp
            x.hp=90
            x.atk=95
            x.defense=105
            x.spatk=165
            x.spdef=110
            x.speed=45
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Steelixite":
            x.ability="Heatproof"
            x.weight=1631.42
            per=x.hp/x.maxhp
            x.hp=75
            x.atk=125
            x.defense=230
            x.spatk=55
            x.spdef=95
            x.speed=30
            calcst(x)
            x.hp=x.maxhp*per   
        if x.item=="Scizorite":
            x.ability="Technician"
            x.weight=275.58
            per=x.hp/x.maxhp
            x.hp=70
            x.atk=150
            x.defense=140
            x.spatk=65
            x.spdef=100
            x.speed=75
            calcst(x)
            x.hp=x.maxhp*per  
        if x.item=="Heracronite":
            x.ability="Skill Link"
            x.weight=137.79
            per=x.hp/x.maxhp
            x.hp=80
            x.atk=185
            x.defense=115
            x.spatk=40
            x.spdef=105
            x.speed=75
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Houndoominite":
            x.ability=random.choice(["Solar Power","Dark Aura"])
            x.weight=109.13
            per=x.hp/x.maxhp
            x.hp=75
            x.atk=110
            x.defense=90
            x.spatk=140
            x.spdef=90
            x.speed=115
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Tyranitarite":
            x.ability="Sand Stream"
            x.weight=562.18
            per=x.hp/x.maxhp
            x.hp=100
            x.atk=164
            x.defense=150
            x.spatk=95
            x.spdef=120
            x.speed=71
            calcst(x)
            x.hp=x.maxhp*per    
        if x.item=="Sceptilite":
            x.ability="Technician"
            x.secondaryType="Dragon"
            x.weight=121.7
            per=x.hp/x.maxhp
            x.hp=70
            x.atk=135
            x.defense=75
            x.spatk=110
            x.spdef=85
            x.speed=145
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Blazikenite":
            x.ability="Speed Boost"
            x.weight=114.64
            per=x.hp/x.maxhp
            x.hp=80
            x.atk=160
            x.defense=80
            x.spatk=130
            x.spdef=80
            x.speed=100
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Swampertite":
            x.ability="Swift Swim"
            x.weight=224.87
            per=x.hp/x.maxhp
            x.hp=100
            x.atk=150
            x.defense=110
            x.spatk=95
            x.spdef=110
            x.speed=70
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Gardevoirite":
            x.ability="Pixilate"
            x.weight=106.7
            per=x.hp/x.maxhp
            x.hp=68
            x.atk=85
            x.defense=65
            x.spatk=165
            x.spdef=135
            x.speed=100
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Sablenite":
            x.ability="Magic Bounce"
            x.weight=354.94
            per=x.hp/x.maxhp
            x.hp=50
            x.atk=85
            x.defense=125
            x.spatk=85
            x.spdef=115
            x.speed=20
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Mawilite":
            x.ability="Huge Power"
            x.weight=51.81
            per=x.hp/x.maxhp
            x.hp=50
            x.atk=105
            x.defense=125
            x.spatk=55
            x.spdef=95
            x.speed=50
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Aggronite":
            x.ability="Filter"
            x.secondaryType="None"
            x.weight=870.83
            per=x.hp/x.maxhp
            x.hp=70
            x.atk=140
            x.defense=230
            x.spatk=60
            x.spdef=80
            x.speed=50
            calcst(x)
            x.hp=x.maxhp*per    
        if x.item=="Medichamite":
            x.ability="Pure Power"
            x.weight=69.45
            per=x.hp/x.maxhp
            x.hp=60
            x.atk=100
            x.defense=85
            x.spatk=80
            x.spdef=85
            x.speed=100
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Manectite":
            x.ability="Intimidate"
            x.weight=97
            per=x.hp/x.maxhp
            x.hp=70
            x.atk=75
            x.defense=80
            x.spatk=135
            x.spdef=80
            x.speed=135
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Sharpedonite":
            x.ability="Strong Jaw"
            x.weight=287.26
            per=x.hp/x.maxhp
            x.hp=70
            x.atk=140
            x.defense=70
            x.spatk=110
            x.spdef=65
            x.speed=105
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Camerupite":
            x.ability="Sheer Force"
            x.weight=706.58
            per=x.hp/x.maxhp
            x.hp=90
            x.atk=100
            x.defense=110
            x.spatk=145
            x.spdef=115
            x.speed=20
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Altarianite":
            x.ability="Pixilate"
            x.secondaryType="Fairy"
            x.weight=45.42
            per=x.hp/x.maxhp
            x.hp=85
            x.atk=110
            x.defense=110
            x.spatk=110
            x.spdef=105
            x.speed=80
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Banettite":
            x.ability="Prankster"
            x.secondaryType="Normal"
            x.weight=28.66
            per=x.hp/x.maxhp
            x.hp=64
            x.atk=165
            x.defense=75
            x.spatk=93
            x.spdef=83
            x.speed=75
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Absolite":
            x.ability=random.choice(["Magic Bounce","Sharpness"])
            x.secondaryType="Fairy"
            x.weight=108.03
            per=x.hp/x.maxhp
            x.hp=65
            x.atk=150
            x.defense=60
            x.spatk=115
            x.spdef=60
            x.speed=115
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Glalitite":
            x.ability="Refrigerate"
            x.weight=772.06
            per=x.hp/x.maxhp
            x.hp=80
            x.atk=135
            x.defense=80
            x.spatk=105
            x.spdef=80
            x.speed=100
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Salamencite":
            x.ability="Aerilate"
            x.weight=248.24
            per=x.hp/x.maxhp
            x.hp=95
            x.atk=145
            x.defense=130
            x.spatk=120
            x.spdef=90
            x.speed=120
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Metagrossite":
            x.ability="Tough Claws"
            x.weight=2078.74
            per=x.hp/x.maxhp
            x.hp=80
            x.atk=145
            x.defense=150
            x.spatk=105
            x.spdef=110
            x.speed=110
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Latiasite":
            per=x.hp/x.maxhp
            x.weight=114.64
            x.hp=80
            x.atk=100
            x.defense=120
            x.spatk=140
            x.spdef=150
            x.speed=110
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Latiosite":
            per=x.hp/x.maxhp
            x.weight=154.32
            x.hp=80
            x.atk=139
            x.defense=100
            x.spatk=160
            x.spdef=120
            x.speed=110
            calcst(x)
            x.hp=x.maxhp*per
        if "Dragon Ascent" in x.moves:
            x.ability="Delta Stream"
            per=x.hp/x.maxhp
            x.weight=864.21
            x.hp=105
            x.atk=180
            x.defense=100
            x.spatk=180
            x.spdef=100
            x.speed=115
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Garchompite":
            x.ability="Sand Force"
            x.weight=209.44
            per=x.hp/x.maxhp
            x.hp=108
            x.atk=170
            x.defense=105
            x.spatk=120
            x.spdef=95
            x.speed=102
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Lucarionite":
            x.ability="Adaptability"
            x.weight=126.77
            per=x.hp/x.maxhp
            x.hp=70
            x.atk=145
            x.defense=88
            x.spatk=140
            x.spdef=70
            x.speed=112
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Abomasite":
            x.ability="Slush Rush"
            x.weight=407.86
            per=x.hp/x.maxhp
            x.hp=90
            x.atk=132
            x.defense=105
            x.spatk=132
            x.spdef=105
            x.speed=60
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Lopunnite":
            x.ability="Scrappy"
            per=x.hp/x.maxhp
            x.weight=62.9
            x.hp=80
            x.atk=139
            x.defense=100
            x.spatk=160
            x.spdef=120
            x.speed=110
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Galladite":
            x.ability="Sharpness"
            x.weight=124.34
            per=x.hp/x.maxhp
            x.hp=68
            x.atk=165
            x.defense=95
            x.spatk=65
            x.spdef=115
            x.speed=110
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Audinite":
            x.ability="Regenerator"
            x.secondaryType="Fairy"
            color="yellow"
            x.weight=70.55
            per=x.hp/x.maxhp
            x.hp=103
            x.atk=60
            x.defense=126
            x.spatk=80
            x.spdef=126
            x.speed=50
            calcst(x)
            x.hp=x.maxhp*per
        if x.item=="Diancite":
            x.ability="Magic Bounce"
            x.weight=61.29
            per=x.hp/x.maxhp
            x.hp=50
            x.atk=160
            x.defense=110
            x.spatk=160
            x.spdef=110
            x.speed=110
            calcst(x)
            x.hp=x.maxhp*per      
        em.set_image(url=x.sprite)            
        await entryeff(ctx,x,y,tr1,tr2,field,turn)
    return x,em                                           

async def faint(ctx,bot,x,y,tr1,tr2,field,turn):
    if x.hp<=0:
        em=discord.Embed(title=f"{x.nickname} fainted!")
        em.set_image(url=x.sprite)
        if y.ability in ["Moxie","Chilling Neigh"]:
            await atkchange(em,y,y,1)
        elif y.ability in ["Soul-Heart","Grim Neigh"]:
            await spatkchange(em,y,y,1)
        elif y.ability=="As One":
            if "Shadow" in y.name:
                await spatkchange(em,y,y,1)
            elif "Ice" in y.name:
                await atkchange(em,y,y,1)
        elif y.ability=="Beast Boost":
            m=[a,b,c,d,e]=[y.atk,y.defense,y.spatk,y.spdef,y.speed]
            if tr2.reflect==True:
                m=[y.atk,y.defense/2,y.spatk,y.spdef,y.speed]
            if tr2.lightscreen==True:
                m=[y.atk,y.defense,y.spatk,y.spdef/2,y.speed]
            pp=mapp(m)
            if pp==a:
            	await atkchange(em,y,y,1)
            elif pp==b:
            	await defchange(em,y,y,1)
            elif pp==c:
        	    await spatkchange(em,y,y,1)
            elif pp==d:
        	    await spdefchange(em,y,y,1)
            elif pp==e:
            	await speedchange(em,y,y,1)
        elif y.ability=="Battle Bond" and "Ash" not in y.name:
            per=y.hp/y.maxhp
            y.weight=88.18
            y.sprite="http://play.pokemonshowdown.com/sprites/ani/greninja-ash.gif"
            y.name="Ash Greninja"
            y.hp=72
            y.atk=145
            y.defense=67
            y.spatk=153
            y.spdef=71
            y.speed=132
            calcst(y)
            y.hp=y.maxhp*per
            bb=discord.Embed(title=f"{y.nickname}'s Battle Bond!",description=f"{y.nickname} transformed into Ash-Greninja!")
            bb.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1125023366278029402/image0.gif")
            await ctx.send(embed=bb)
        if x.ability=="Aftermath":
            y.hp-=(y.maxhp/4)    
        tr1.faintedmon.append(x)
        tr1.pokemons.remove(x)
        if len(tr1.pokemons)==0:
            await ctx.send(embed=em)
        if len(tr1.pokemons)!=0 and len(tr2.pokemons)!=0:
            await ctx.send(embed=em)
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
            if x.hp<=0:
                await faint(ctx,bot,x,y,tr1,tr2,field,turn)                
    return x                      
async def addmoney(ctx,member,price):
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"select * from '{member.id}'")
    m=c.fetchone()
    money=m[0]+price
    try:
        if price<0 and member.id!=1084473178400755772:
            c.execute(f"select * from '1084473178400755772'")
            mow=c.fetchone()
            moey=mow[0]-price
            c.execute(f"update '1084473178400755772' set balance={moey}")
            db.commit()
    except:
        pass           
    c.execute(f"update '{member.id}' set balance={money}")
    db.commit()
    if price>0:
        await ctx.send(f"{member.display_name} {await numberify(price)} <:pokecoin:1134595078892044369> added to your balance!")
    if price<0:
        price=-price
        await ctx.send(f"{member.display_name} {await numberify(price)} <:pokecoin:1134595078892044369> was deducted from your balance!")
    await ctx.send(f"{member.display_name}'s New Balance: {await numberify(money)}<:pokecoin:1134595078892044369>")
               
async def winner(ctx,tr1,tr2):
    db=sqlite3.connect("playerdata.db")
    c=db.cursor()
    c.execute(f"select * from '{ctx.author.id}'")
    pl=c.fetchone()
    winner=tr1
    em=discord.Embed(title=f"{winner.name} won the battle!")
    em.set_image(url=tr1.sprite)
    
    if tr1.name!=ctx.author.display_name:
        c.execute(f"""Update `{ctx.author.id}` set winstreak=0""")
        db.commit()
    elif tr1.name==ctx.author.display_name:
        am=0
        streak=pl[4]+1
        c.execute(f"""Update `{ctx.author.id}` set winstreak={streak}""")
        db.commit()
        dt=sqlite3.connect("pokemondata.db")
        ct=dt.cursor()
        nm=tr2.name.split("> ")[-1]
        ct.execute(f"select * from 'Trainers' where name='{nm}'")
        bdg=ct.fetchone()
        if bdg!=None:
            if pl[6]=="None":
                c.execute(f"""Update `{ctx.author.id}`set badges='{bdg[1]}'""")
                em.add_field(name="1st badge obtained!",value=f"{bdg[2]} Congratulations! You received a {bdg[1]} from {tr2.name}.")
                db.commit()
            elif pl[6]!="None":
                if bdg[1] not in pl[6]:
                    new=pl[6]+","+bdg[1]
                    c.execute(f"""Update `{ctx.author.id}`set badges='{new}'""")
                    em.add_field(name="New badge obtained!",value=f"{bdg[2]} Congratulations! You received a {bdg[1]} from {tr2.name}.")
                    db.commit()
        if pl[5]<streak:
            c.execute(f"""Update `{ctx.author.id}` set highstreak={streak}""")
            db.commit()
        await ctx.send(embed=em)
        if "Pokemon Trainer" in tr2.name:
            am=1000
        elif "Gym Leader" in tr2.name:
            am=2000
        elif "Elite Four" in tr2.name:
            am=5000
        elif "Champion" in tr2.name:
            am=10000
        else:
             am=1000
        await addmoney(ctx,ctx.author,am)
        
#Effects    
async def effects(ctx,x,y,tr1,field,turn):
    em=discord.Embed(title="Effects:")
    #Dynamax Reset
    if x.dmax==True and turn==x.maxend:
        x.dmax=False
        x.gsprite="None"
        x.hp=round(x.hp/2)
        x.maxhp=round(x.maxhp/2)
        em.add_field(name="Dynamax End:",value=f"{x.name} returned to it's normal state!")
        if "gmax" in x.sprite:
            x.sprite=x.sprite.replace("-gmax.gif",".gif")
    if 0 in x.pplist:
        if x.dmax is False and x.use in x.moves:
            x.lostmoves.append(x.moves[x.pplist.index(0)])
            x.moves.remove(x.moves[x.pplist.index(0)])
        if x.dmax is True and x.use in x.maxmoves:
            x.moves.remove(x.moves[x.pplist.index(0)])
            x.maxmoves.remove(x.maxmoves[x.pplist.index(0)])
        x.pplist.remove(0)                 
    #Badly Poisoned            
    if x.status=="Badly Poisoned" and x.ability not in ["Magic Guard","Poison Heal","Toxic Boost","Immunity"] and x.hp>0:
        x.hp-=(1+(x.maxhp*x.toxicCounter/16))
        x.toxicCounter+=1
        em.add_field(name="Badly Poisoned:",value=f"{x.name} was hurt by fatal poison!")
    #Burned        
    if x.status=="Burned" and x.ability!="Magic Guard" and x.hp>0:
        em.add_field(name="Burn:",value=f"{x.name} was hurt by burn!")
        x.hp-=x.maxhp/16
    #Leftovers       
    if x.hp>0 and x.hp<x.maxhp and x.item=="Leftovers":
        em.add_field(name="Leftovers:",value=f"{x.nickname} restored a little HP using its Leftovers.")
        x.hp+=round(x.maxhp/16) 
    #Ice Body
    if x.hp>0 and x.hp<x.maxhp and field.weather in ["Snowstorm","Hail"] and x.ability=="Ice Body":
        em.add_field(name=f"{x.nickname}'s Ice Body!",value=f"{x.nickname} restored a little HP using its Ice Body.")
        x.hp+=round(x.maxhp/8)         
    #Poison Heal
    if x.hp>0 and x.hp<x.maxhp and x.ability=="Poison Heal" and "Poisoned" in x.status:
        em.add_field(name=f"{x.nickname}'s Poison Heal!",value=f"{x.nickname} restored a little HP using its Poison Heal.")
        x.hp+=round(x.maxhp/8)        
    #Black Sludge
    if x.hp>0 and x.hp<x.maxhp and x.item=="Black Sludge":
        if "Poison" in (x.primaryType,x.secondaryType,x.teraType):
            em.add_field(name="Black Sludge:",value=f"{x.nickname} restored a little HP using its Black Sludge.")
            x.hp+=round(x.maxhp/16)      
        else:  
            em.add_field(name="Black Sludge:",value=f"{x.nickname} lost a little HP using its Black Sludge.")
            x.hp-=round(x.maxhp/16)
    #Aqua Ring        
    if x.hp>0 and x.hp<x.maxhp and x.aring is True:
        em.add_field(name="Aqua Ring:",value=f"{x.nickname} restored a little HP using its Aqua Ring.")
        if x.item=="Big Root":
            x.hp+=round((x.maxhp/16)*1.3)
        else:
            x.hp+=round(x.maxhp/16)          
    #Grassy Terrain            
    if x.hp>0 and field.terrain =="Grassy" and x.hp<x.maxhp and (x.ability not in ["Levitate"] and "Flying" not in (x.primaryType,x.secondaryType,x.teraType) or x.grav is True):
        em.add_field(name="Grassy Terrain:",value=f"{x.nickname}'s HP was restored.")
        x.hp+=round(x.maxhp/16)
        if x.hp>x.maxhp:
            x.hp=x.maxhp
    if x.hp<0:
        x.hp=0
    if len(em.fields)!=0:
        await ctx.send(embed=em)
#Weather    
async def weather(ctx, field, bg):
    weather_messages = {
        "Extreme Sunlight": "The sunlight is extremely harsh.",
        "Heavy Rain": "Heavy rain continues to fall.",
        "Snowstorm": "Snow continues to fall.",
        "Rainy": "Rain continues to fall.",
        "Sandstorm": "The sandstorm is raging!",
        "Hail": "Hail continues to fall.",
        "Sunny": "The sunlight is strong."
    }
    
    em = discord.Embed(title="Weather Update!", color=bg)
    if field.weather in weather_messages:
        em.add_field(name="Weather:", value=weather_messages[field.weather])
    elif field.weather not in ["Normal", "Cloudy", "Clear"]:
        await ctx.send(embed=em)

        
async def switch(ctx,bot,x,y,tr1,tr2,field,turn):
    if x.dmax==True:
        x.hp/=2
        x.maxhp/=2
        x.dmax=False
    if x.ability in ["Protean", "Libero"]:
        type_assignments = {
        "Kecleon": ("Normal", "Ghost"),
        "Meowscarada": ("Grass", "Dark"),
        "Cinderace": ("Fire", "???"),
        "Greninja": ("Water", "Dark")
    }

        if x.name in type_assignments:
            x.primaryType, x.secondaryType=type_assignments[x.name]
    if "Disguise" in x.ability:
        x.ability = "Disguise"
        x.sprite = "http://play.pokemonshowdown.com/sprites/ani/mimikyu.gif"

    if "Quark Drive" in x.ability:
        x.ability = "Quark Drive"

    if "Protosynthesis" in x.ability:
        x.ability = "Protosynthesis"

    if "Ditto" in x.name:
        x.ability="Imposter"
        x.name="Ditto"
        x.sprite="sprites/Ditto.png"
    x.atkb=x.defb=x.spatkb=x.spdefb=x.speedb=0
    x.atk=x.maxatk
    x.speed=x.maxspeed
    x.spatk=x.maxspatk
    x.spdef=x.maxspdef
    x.defense=x.maxdef
    new=""
    n=0
    pklist=""
    for i in tr1.pokemons:
        n+=1
        pklist+=f"#{n} {i.icon} {i.name} {i.hp}/{i.maxhp}\n"
    em=discord.Embed(title="Choose your pokémon!",description=pklist)
    if tr1.ai:
        new = ""
        while not new or new == x:
            new = random.choice(tr1.pokemons)
    
        await withdraweff(ctx, x, tr1, y)
    
        em = discord.Embed(title=f"{tr1.name} sent out {new.nickname}!")
        em.set_thumbnail(url=tr1.sprite)
        em.set_image(url=new.sprite)
    
        await ctx.send(embed=em)
        await entryeff(ctx, new, y, tr1, tr2, field, turn)
    
        return new

    elif tr2.ai == True and tr1.ai == False:
        while new == "" or new == x:
            await ctx.send(embed=em)  
            def check(message):
                return message.author == ctx.author
            num = await bot.wait_for('message', check=check)
            num = int(num.content) if num.content.isdigit() else 0        
            if True:
                if 0<num<7:
                    num=num-1
                    new=x
                    if x in tr1.pokemons:
                        cnum=tr1.pokemons.index(x)
                        if cnum==num:
                            await tr1.member.send(f"{x.name} is already in battle!")
                        if cnum!=num:
                            new=tr1.pokemons[num]
                            await withdraweff(ctx,x,tr1,y)
                        await entryeff(ctx,new,y,tr1,tr2,field,turn)
                        em=discord.Embed(title=f"{tr1.name} sent out {new.nickname}!")
                        em.set_thumbnail(url=tr1.sprite)
                        em.set_image(url=new.sprite)
                        await ctx.send(embed=em)
                        return new
                    if x not in tr1.pokemons:
                        new=tr1.pokemons[num]                          
                        await entryeff(ctx,new,y,tr1,tr2,field,turn)
                        em=discord.Embed(title=f"{tr1.name} sent out {new.nickname}!")
                        em.set_thumbnail(url=tr1.sprite)
                        em.set_image(url=new.sprite)
                        await ctx.send(embed=em)
                        return new
    elif tr2.ai==False and tr1.ai==False:
        while new=="" or new==x:
            await tr1.member.send(embed=em)  
            def check(message):
                return isinstance(message.channel,discord.DMChannel) and message.author==tr1.member
            num=await bot.wait_for('message',check=check)
            if True:
                num=int(num.content)
                if 0<num<7:
                    num=num-1
                    new=x
                    if x in tr1.pokemons:
                        cnum=tr1.pokemons.index(x)
                        if cnum==num:
                            await tr1.member.send(f"{x.name} is already in battle!")
                        if cnum!=num:
                            new=tr1.pokemons[num]
                            await withdraweff(ctx,x,tr1,y)
                        await entryeff(ctx,new,y,tr1,tr2,field,turn)
                        em=discord.Embed(title=f"{tr1.name} sent out {new.nickname}!")
                        em.set_thumbnail(url=tr1.sprite)
                        em.set_image(url=new.sprite)
                        await ctx.send(embed=em)
                        return new
                    if x not in tr1.pokemons:
                        new=tr1.pokemons[num]                          
                        await entryeff(ctx,new,y,tr1,tr2,field,turn)
                        em=discord.Embed(title=f"{tr1.name} sent out {new.nickname}!")
                        em.set_thumbnail(url=tr1.sprite)
                        em.set_image(url=new.sprite)
                        await ctx.send(embed=em)
                        return new
async def withdraweff(ctx, x, tr1, y):
    em = discord.Embed(title="Withdraw Effect:")
    
    if x.ability == "Zero to Hero" and "Hero" not in x.name and x.hp > 0 and not x.dmax:
        em.add_field(name=f"{x.name}'s Zero to Hero!", value=f"{x.name} underwent a heroic transformation!")
        x.name = "Hero Palafin"
        x.sprite = "http://play.pokemonshowdown.com/sprites/ani/palafin-hero.gif"
        per = x.hp / x.maxhp
        x.weight = 214.73
        x.hp = 100
        x.atk = 160
        x.defense = 97
        x.spatk = 106
        x.spdef = 87
        x.speed = 100
        calcst(x)
        x.hp = x.maxhp * per
    
    if x.ability == "Illusion":
        last_pokemon = tr1.pokemons[len(tr1.pokemons) - 1]
        x.name = last_pokemon.name
        x.sprite = last_pokemon.sprite
    
    if x.ability == "Natural Cure" and x.status != "Alive" and x.status != "Fainted":
        em.add_field(name=f"{x.name}'s Natural Cure!", value=f"{x.name}'s status condition was cured!")
        x.status = "Alive"
    
    if x.ability == "Regenerator" and 0 < x.hp < x.maxhp and x.status != "Fainted":
        em.add_field(name=f"{x.name}'s Regenerator!", value=f"{x.name} regenerated a bit of its health!")
        if x.hp <= (x.maxhp / 3):
            x.hp += round(x.maxhp / 3)
        elif x.hp > (x.maxhp / 3):
            x.hp = x.maxhp

async def teambuild(team):
    new=[]
    while len(new)!=6:
        mon=random.choice(team)
        if mon not in new:
            new.append(mon)
    return new            
async def gamemonvert(m):
    dt = sqlite3.connect("pokemondata.db")
    cx = dt.cursor()
    print(m[0])
    xxx = m[0]
    
    if m[0] == "Zacian" and m[11] == "Rusted Sword":
        xxx = "Crowned Zacian"
    elif m[0] == "Zamazenta" and m[11] == "Rusted Shield":
        xxx = "Crowned Zamazenta"
    
    cx.execute(f"SELECT * FROM 'wild' WHERE name='{xxx}'")
    n = cx.fetchall()[0]
    newname=m[1]
    itm="None"
    moves = m[14]
    ability = m[8]
    if ability == "None":
        ability = n[11]
    
    if moves == "A,B,C,D":
        moves = n[10]
    if m[1]==None:
        newname=m[0]
    if m[11]!="None":
        itm=m[11].split(",")[0]
    elif m[11]=="None":
        itm=n[24]
        if itm is None:
            itm="None"
        else:
            itm=random.choice(n[24].split(","))
    p = Pokemon(
        name=m[0],
        nickname=newname,
        hpev=m[2],
        atkev=m[3],
        defev=m[4],
        spatkev=m[5],
        spdefev=m[6],
        speedev=m[7],
        ability=ability.split(",")[0],
        nature=m[9].split(",")[0],
        shiny=m[10],
        item=itm,
        gender=m[12],
        tera=m[13],
        moves=moves,
        maxiv="Yes",
        primaryType=n[1],
        secondaryType=n[2],
        level=n[3],
        hp=n[4],
        atk=n[5],
        defense=n[6],
        spatk=n[7],
        spdef=n[8],
        speed=n[9],
        sprite=n[12],
        icon=n[22]
    )
    
    return p
async def checkname(name):
    if "Gym Leader" in name:
        name="<:gym:1134404587432980611> "+name
    elif "Elite Four" in name:
        name="<:e4:1134407225222377474> "+name
    elif "Galactic" in name:
        name="<:galactic:1134373093457022996> "+name        
    elif "Rocket" in name:
        name="<:rocket:1134396195394039968> "+name        
    elif "Aqua" in name:
        name="<:aqua:1134377659342798849> "+name        
    elif "Magma" in name:
        name="<:magma:1134377889287110681> "+name        
    elif "Plasma" in name:
        name="<:plasma:1134394632004968448> "+name        
    return name
async def gameteam(ctx,num=0):
    players=("World Champion Ash","Professor Oak","Researcher Gary Oak","Team Rocket James","Team Rocket Jessie","Gym Leader Brock","Gym Leader Misty","Gym Leader Lt.Surge","Gym Leader Erika","Gym Leader Janine","Gym Leader Sabrina","Gym Leader Blaine","Gym Leader Blue","Elite Four Lorelei","Elite Four Bruno","Elite Four Agatha","Kanto Champion Lance","Kanto Champion Red","Rocket Boss Giovanni","Gym Leader Falkner","Gym Leader Bugsy","Gym Leader Morty","Gym Leader Chuck","Gym Leader Jasmine","Gym Leader Pryce","Gym Leader Clair","Elite Four Will","Elite Four Koga","Elite Four Karen","Rocket Admin Archer","Rocket Admin Ariana","Pokemon Trainer May","Gym Leader Roxanne","Gym Leader Brawly","Gym Leader Wattson","Gym Leader Flannery","Gym Leader Norman","Gym Leader Winona","Gym Leader Tate","Gym Leader Liza","Gym Leader Juan","Elite Four Sidney","Elite Four Phoebe","Elite Four Glacia","Elite Four Drake","Hoenn Champion Steven","Hoenn Champion Wallace","Aqua Leader Archie","Magma Admin Courtney","Magma Leader Maxie","Factory Head Noland","Arena Tycoon Greta","Dome Ace Tucker","Palace Maven Spenser","Pike Queen Lucy","Salon Maiden Anabel","Pyramid King Brandon","Pokemon Trainer Paul","Pokemon Trainer Barry","Pokemon Trainer Conway","Gym Leader Roark","Gym Leader Gardenia","Gym Leader Maylene","Gym Leader Crasher Wake","Gym Leader Fantina","Gym Leader Byron","Gym Leader Candice","Gym Leader Volkner","Elite Four Aaron","Elite Four Bertha","Elite Four Flint","Elite Four Lucian","Sinnoh Champion Cynthia","Pokemon Trainer Tobias","Galactic Commander Mars","Galactic Commander Jupiter","Galactic Commander Saturn","Galactic Leader Cyrus","Pokemon Trainer Riley","Pokemon Trainer Cheryl","Pokemon Trainer Marley","Pokemon Trainer Mira","Pokemon Trainer Buck","Factory Head Thorton","Battle Arcade Dahlia","Castle Velvet Darach","Tower Tycoon Palmer","Gym Leader Cilan","Pokemon Trainer Cheren","Gym Leader Lenora","Gym Leader Roxie","Gym Leader Burgh","Gym Leader Elesa","Gym Leader Clay","Gym Leader Skyla","Gym Leader Brycen","Gym Leader Marlon","Gym Leader Drayden","Gym Leader Marlon","Elite Four Marshal","Elite Four Shauntal","Elite Four Grimsley","Elite Four Caitlin","Unova Champion Alder","Unova Champion Iris","Plasma Admin Colress","Natural Harmonia Gropius","Plasma Leader Ghetsis","Boss Trainer Benga","Subway Boss Ingo","Subway Boss Emmet","Gym Leader Viola","Gym Leader Grant","Gym Leader Korrina","Gym Leader Ramos","Gym Leader Clemont","Gym Leader Valerie","Gym Leader Olympia","Gym Leader Wulfric","Elite Four Siebold","Elite Four Wikstrom","Elite Four Malva","Elite Four Drasna","Pokemon Trainer Alain","Kalos Champion Diantha","Flare Boss Lysandre","Pokemon Trainer Gladion","Trial Captain Kiawe","Trial Captain Lana","Trial Captain Lillie","Trial Captain Mallow","Island Kahuna Ilima","Trial Captain Nanu","Elite Four Hala","Elite Four Olivia","Elite Four Molayne","Professor Kukui","Skull Admin Plumeria","Skull Leader Guzma","Aether Foundation Faba","Aether President Lusamine","Gym Leader Milo","Gym Leader Nessa","Gym Leader Kabu","Gym Leader Bede","Gym Leader Bea","Gym Leader Allister","Gym Leader Opal","Gym Leader Gordie","Gym Leader Marnie","Gym Leader Piers","Gym Leader Raihan","Pokemon Trainer Hop","Galar Champion Peony","Galar Champion Leon","Chairman Rose","Galar Champion Mustard","Gym Leader Katy","Gym Leader Brassius","Gym Leader Iono","Gym Leader Kofu","Gym Leader Ryme","Gym Leader Tulip","Gym Leader Grusha","Team Star Giacomo","Team Star Mela","Team Star Atticus","Team Star Ortega","Team Star Eri","Star Leader Penny","Elite Four Rika","Elite Four Poppy","Elite Four Larry","Elite Four Hassel","Paldea Champion Geeta","Paldea Champion Nemona","Professor Sada","Professor Turo","Elite Four Acerola","Pokemon Trainer Drew","Battle Chatelaine Evelyn","Island Kahuna Hapu","Fusion Creator Darwin","Elite Four Kahili","Coordinator Kenny","Gym Leader Klara","Aqua Admin Matt","Battle Chatelaine Nita","Pokemon Wielder Volo")
    if num==0:
        name=random.choice(players)  
    else:
        num=num-1
        name=players[num]
    sprite=await trsprite(name)
    db=sqlite3.connect("pokemondata.db")
    c=db.cursor()
    c.execute(f"select * from '{name}'")
    mons=c.fetchall()
    team=[]
    for i in mons:
        p=await gamemonvert(i)
        team.append(p)
    mons=await teambuild(team)
    name=await checkname(name)
    tr1=Trainer(name,mons,"Unknown",sprite=sprite,ai=True)
    return tr1    
async def trsprite(name):
    spritelist={
    "Gym Leader Tulip":"https://cdn.discordapp.com/attachments/1102579499989745764/1137992736453177365/20230807_121640.png",
    "Elite Four Sidney":"https://cdn.discordapp.com/attachments/1102579499989745764/1137428029459681350/Spr_RS_Sidney.png",
    "World Champion Ash":"https://cdn.discordapp.com/attachments/1102579499989745764/1137425204969230346/20230805_224131.png",
    "Elite Four Shauntal":"https://cdn.discordapp.com/attachments/1102579499989745764/1136917784996089906/Spr_B2W2_Shauntal.png",
    "Pokemon Trainer Tobias":"https://cdn.discordapp.com/attachments/1102579499989745764/1136904651510394943/1691129578488.png",
    "Professor Turo":"https://cdn.discordapp.com/attachments/1102579499989745764/1136902377216167996/1691129034584.png",
    "Professor Sada":"https://cdn.discordapp.com/attachments/1102579499989745764/1136902376972877965/1691128954401.png",
    "Dome Ace Tucker":"https://cdn.discordapp.com/attachments/1102579499989745764/1136899891789045780/Spr_E_Tucker.png",
    "Palace Maven Spenser":"https://cdn.discordapp.com/attachments/1102579499989745764/1136898826507137104/Spr_E_Spenser.png",
    "Gym Leader Janine":"https://cdn.discordapp.com/attachments/1102579499989745764/1136898405768122378/Spr_HGSS_Janine.png",
    "Gym Leader Skyla":"https://cdn.discordapp.com/attachments/1102579499989745764/1136898405508063252/Spr_B2W2_Skyla.png",
    "Galactic Commander Saturn":"https://cdn.discordapp.com/attachments/1102579499989745764/1136897817684754494/Spr_DP_Saturn.png",
    "Factory Head Thorton":"https://cdn.discordapp.com/attachments/1102579499989745764/1136896591094087800/Spr_Pt_Thorton.png",
    "Hoenn Champion Wallace":"https://cdn.discordapp.com/attachments/1102579499989745764/1136896963388907601/Spr_B2W2_Wallace.png",
    "Gym Leader Tate":"https://cdn.discordapp.com/attachments/1102579499989745764/1136897295825240104/Spr_B2W2_Tate.png",
    "Gym Leader Winona":"https://cdn.discordapp.com/attachments/1102579499989745764/1136615608037941360/image_search_1691060615276.png",
    "Gym Leader Wattson":"https://cdn.discordapp.com/attachments/1102579499989745764/1136615607631106078/image_search_1691060604914.png",
    "Elite Four Siebold":"https://cdn.discordapp.com/attachments/1102579499989745764/1136901308750766160/image_search_1691128765143.png",
    "Elite Four Wikstrom":"https://cdn.discordapp.com/attachments/1102579499989745764/1136901309019205662/image_search_1691128774978.png",
    "Pokemon Trainer Cheryl":"https://cdn.discordapp.com/attachments/1102579499989745764/1126801413515780146/Cheryl.png",
    "Pokemon Trainer Buck":"https://cdn.discordapp.com/attachments/1102579499989745764/1126801176525029396/Buck.png",
    "Gym Leader Ryme":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792581196550246/Ryme.png",
    "Gym Leader Roxie":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580957487194/Roxie.png",
    "Gym Leader Roxanne":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580739379200/Roxanne.png",
    "Chairman Rose":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580470935562/Rose.png",
    "Gym Leader Roark":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580257038336/Roark.png",
    "Pokemon Trainer Riley":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580030541964/Riley.png",
    "Elite Four Rika":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792579757903942/Rika.png",
    "Kanto Champion Red":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792579544006806/Red.png",
    "Gym Leader Ramos":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792579309121536/Ramos.png",
    "Gym Leader Raihan":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792579057455124/Raihan.png",
    "Gym Leader Pryce":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767579650871366/Pryce.png",
    "Elite Four Poppy":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767579415982110/Poppy.png",
    "Skull Admin Plumeria":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767579172716614/Plumeria.png",
    "Gym Leader Piers":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767578904285254/Piers.png",
    "Elite Four Phoebe":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767578640040007/Phoebe.png",
    "Galar Champion Peony":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767578359025687/Peony.png",
    "Star Leader Penny":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767577981530172/Penny.png",
    "Pokemon Trainer Paul":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767577742458930/Paul.png",
    "Tower Tycoon Palmer":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767577482408026/Palmer.png",
    "Team Star Ortega":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767577184616458/Ortega.png",
    "Gym Leader Opal":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759237054382100/Opal.png",
    "Gym Leader Olympia":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759236517498890/Olympia.png",
    "Elite Four Olivia":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759236274237510/Olivia.png",
    "Professor Oak":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759235980627978/oak.png",
    "Gym Leader Norman":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759235586371644/Norman.png",
    "Factory Head Noland":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759235309551646/Noland.png",
    "Battle Chatelaine Nita":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759235032715334/Nita.png",
    "Gym Leader Nessa":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759234751709254/Nessa.png",
    "Paldea Champion Nemona":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759234474872872/Nemona.png",
    "Trial Captain Nanu":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759234122563654/Nanu.png",
    "Natural Harmonia Gropius":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712947134177370/N.png",
    "Galar Champion Mustard":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712946920271974/Mustard.png",
    "Gym Leader Morty":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712946685394964/Morty.png",
    "Elite Four Molayne":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712946479865886/Molayne.png",
    "Pokemon Trainer Mira":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712946203045898/Mira.png",
    "Pokemon Trainer Mina":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712945942994965/Mina.png",
    "Gym Leader Milo":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712945636814919/Milo.png",
    "Gym Leader Maylene":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712944982503524/Maylene.png",
    "Fusion Creator Darwin":"https://play.pokemonshowdown.com/sprites/trainers/unknown.png",
    "Pokemon Trainer May":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587242423992350/May.png",
    "Magma Leader Maxie":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587242084237423/Maxie.png",
    "Aqua Admin Matt":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587241761292288/Matt.png",
    "Elite Four Marshal":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587241442512916/Marshal.png",
    "Galactic Commander Mars":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587241077620796/Mars.png",
    "Gym Leader Marnie":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587240830140496/Marnie.png",
    "Gym Leader Marlon":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587240557514792/Marlon.png",
    "Pokemon Trainer Marley":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587240200994847/Marley.png",
    "Elite Four Malva":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587239886426205/Malva.png",
    "Trial Captain Mallow":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587239634780170/Mallow.png",
    "Flare Boss Lysandre":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578905703723088/Lysandre.png",
    "Aether President Lusamine":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578905494003773/Lusamine.png",
    "Pike Queen Lucy":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578905275912323/Lucy.png",
    "Elite Four Lucian":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578905003274261/Lucian.png",
    "Elite Four Lorelei":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578904743223387/Lorelei.png",
    "Gym Leader Liza":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578904478986280/Liza.png",
    "Trial Captain Lillie":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578904252489798/Lillie.png",
    "Galar Champion Leon":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578903984066600/Leon.png",
    "Gym Leader Lenora":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578903749177436/Lenora.png",
    "Elite Four Larry":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578903463960647/Larry.png",
    "Kanto Champion Lance":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571178516492379/Lance.png",
    "Trial Captain Lana":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571178222887003/Lana.png",
    "Professor Kukui":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571178013180055/Kukui.png",
    "Gym Leader Korrina":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571177732153495/Korrina.png",
    "Elite Four Koga":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571177509863515/Koga.png",
    "Gym Leader Kofu":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571177212063805/Kofu.png",
    "Gym Leader Klara":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571176998150244/Klara.png",
    "Trial Captain Kiawe":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571176771666030/Kiawe.png",
    "Coordinator Kenny":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571176532586598/Kenny.png",
    "Gym Leader Katy":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571176322867210/Katy.png",
    "Island Kahuna Ilima":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283056624119858/Ilima.png",
    "Subway Boss Ingo":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283056850608228/Ingo.png",
    "Elite Four Karen":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999806100357140/Karen.png",
    "Gym Leader Kabu":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999805869666314/Kabu.png",
    "Elite Four Kahili":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999805601239110/Kahili.png",
    "Galactic Commander Jupiter":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999805349576834/Jupiter.png",
    "Team Rocket Jessie":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999804837875752/Jessie.png",
    "Gym Leader Juan":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999805076942962/Juan.png",
    "Gym Leader Jasmine":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999804535881758/Jasmine.png",
    "Team Rocket James":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999804280025169/James.png",
    "Unova Champion Iris":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999804045152266/Iris.png",
    "Gym Leader Iono":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999803806072852/Iono.png",
    "Elite Four Bruno":"https://cdn.discordapp.com/attachments/1102579499989745764/1115998773781475368/Bruno.png",
    "Pokemon Trainer Hop":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283056359866469/Hop.png",
    "Pokemon Trainer Hau":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283056133382204/Hau.png",
    "Elite Four Hassel":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283055927865435/Hassel.png",
    "Island Kahuna Hapu":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283055705554994/Hapu.png",
    "Elite Four Hala":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258206861889566/Hala.png",
    "Skull Leader Guzma":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258206614438008/Guzma.png",
    "Gym Leader Grusha":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258206362783774/Grusha.png",
    "Elite Four Grimsley":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258205993668628/Grimsley.png",
    "Arena Tycoon Greta":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258205628776528/Greta.png",
    "Gym Leader Grant":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258205276459028/Grant.png",
    "Gym Leader Gordie":"https://cdn.discordapp.com/attachments/1102579499989745764/1112020338579095592/Gordie.png",
    "Pokemon Trainer Gladion":"https://cdn.discordapp.com/attachments/1102579499989745764/1112020338079973416/Gladion.png",
    "Elite Four Glacia":"https://cdn.discordapp.com/attachments/1102579499989745764/1112020337840881794/Glacia.png",
    "Rocket Boss Giovanni":"https://cdn.discordapp.com/attachments/1102579499989745764/1112020337572462642/Giovanni.png",
    "Plasma Leader Ghetsis":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943227134713876/Ghetsis.png",
    "Paldea Champion Geeta":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226937577512/Geeta.png",
    "Researcher Gary Oak":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226698514492/Gary2.png",
    "Gym Leader Gardenia":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226476208159/Gardenia.png",
    "Elite Four Flint":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226245517382/Flint.png",
    "Gym Leader Flannery":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226027425904/Flannery.png",
    "Gym Leader Fantina":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897876314996816/Fantina.png",
    "Gym Leader Falkner":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897876105277460/Falkner.png",
    "Aether Foundation Faba":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897875903942706/Faba.png",
    "Battle Chatelaine Evelyn":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897875702628362/Evelyn.png",
    "Subway Boss Emmet":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897875484520468/Emmet.png",
    "Gym Leader Elesa":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897704201736202/Elesa1.png",
    "Pokemon Trainer Drew":"https://cdn.discordapp.com/attachments/1102579499989745764/1111163495371771934/Drew.png",
    "Gym Leader Drayden":"https://cdn.discordapp.com/attachments/1102579499989745764/1111163495136899152/Drayden.png",
    "Elite Four Drasna":"https://cdn.discordapp.com/attachments/1102579499989745764/1111163494876860476/Drasna.png",
    "Elite Four Drake":"https://cdn.discordapp.com/attachments/1102579499989745764/1111163494662942791/Drake.png",
    "Kalos Champion Diantha":"https://cdn.discordapp.com/attachments/1102579499989745764/1111163494465818625/Diantha.png",
    "Castle Velvet Darach":"https://cdn.discordapp.com/attachments/1102579499989745764/1111144175568699523/Darach.png",
    "Battle Arcade Dahlia":"https://cdn.discordapp.com/attachments/1102579499989745764/1111144175237353523/Dahlia.png",
    "Galactic Leader Cyrus":"https://cdn.discordapp.com/attachments/1102579499989745764/1111144175023439912/Cyrus.png",
    "Gym Leader Crasher Wake":"https://cdn.discordapp.com/attachments/1102579499989745764/1111144174755000380/Crasher_Wake.png",
    "Magma Admin Courtney":"https://cdn.discordapp.com/attachments/1102579499989745764/1111144174503350334/Courtney.png",
    "Pokemon Trainer Conway":"https://cdn.discordapp.com/attachments/1102579499989745764/1111144174289436672/Conway.png",
    "Plasma Admin Colress":"https://cdn.discordapp.com/attachments/1102579499989745764/1111127415071199272/Colress.png",
    "Gym Leader Clemont":"https://cdn.discordapp.com/attachments/1102579499989745764/1111127414836314162/Clemont.png",
    "Gym Leader Clay":"https://cdn.discordapp.com/attachments/1102579499989745764/1111127414546903040/Clay.png",
    "Gym Leader Clair":"https://cdn.discordapp.com/attachments/1102579499989745764/1111127414240727092/Clair.png",
    "Gym Leader Chuck":"https://cdn.discordapp.com/attachments/1102579499989745764/1111127413951316037/Chuck.png",
    "Pokemon Trainer Cheren":"https://cdn.discordapp.com/attachments/1102579499989745764/1111127413481558167/Cheren.png",
    "Gym Leader Candice":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114704904003685/Candice.png",
    "Elite Four Caitlin":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114704656535572/Caitlin.png",
    "Gym Leader Byron":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114704451010661/Byron.png",
    "Gym Leader Burgh":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114704144834662/Burgh.png",
    "Gym Leader Bugsy":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114703922532453/Bugsy.png",
    "Gym Leader Brycen":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114703641522226/Brycen.png",
    "Gym Leader Brawly":"https://cdn.discordapp.com/attachments/1102579499989745764/1111112061213216788/Brawly.png",
    "Gym Leader Brassius":"https://cdn.discordapp.com/attachments/1102579499989745764/1111112060919632012/Brassius.png",
    "Pyramid King Brandon":"https://cdn.discordapp.com/attachments/1102579499989745764/1111112060684738601/Brandon.png",
    "Aqua Leader Archie":"https://cdn.discordapp.com/attachments/1102579499989745764/1109681004983107714/Archie.png",
    "Sinnoh Champion Cynthia":"https://cdn.discordapp.com/attachments/1102579499989745764/1109109244420165662/Cynthia.png",
    "Gym Leader Brock":"https://cdn.discordapp.com/attachments/1102579499989745764/1109341253000241203/Brock.png",
    "Gym Leader Misty":"https://cdn.discordapp.com/attachments/1102579499989745764/1109466211990917120/Misty.png",
    "Gym Leader Lt.Surge":"https://cdn.discordapp.com/attachments/1102579499989745764/1109477458245324810/Surge.png",
    "Gym Leader Erika":"https://cdn.discordapp.com/attachments/1102579499989745764/1109477743596412928/Erika.png",
    "Gym Leader Sabrina":"https://cdn.discordapp.com/attachments/1102579499989745764/1109477743881617591/Sabrina.png",
    "Gym Leader Blaine":"https://cdn.discordapp.com/attachments/1102579499989745764/1109477744129101895/Blaine.png",
    "Gym Leader Blue":"https://cdn.discordapp.com/attachments/1102579499989745764/1109477744435273788/Blue.png",
    "Hoenn Champion Steven":"https://cdn.discordapp.com/attachments/1102579499989745764/1109597883084312596/Steven.png",
    "Elite Four Aaron":"https://cdn.discordapp.com/attachments/1102579499989745764/1109598046653788231/Aaron.png",
    "Elite Four Acerola":"https://cdn.discordapp.com/attachments/1102579499989745764/1109598930997620938/Acerola.png",
    "Elite Four Agatha":"https://cdn.discordapp.com/attachments/1102579499989745764/1109599848900083863/Agatha.png",
    "Pokemon Trainer Alain":"https://cdn.discordapp.com/attachments/1102579499989745764/1109611947156045845/Alain.png",
    "Unova Champion Alder":"https://cdn.discordapp.com/attachments/1102579499989745764/1109611947449655356/Alder.png",
    "Gym Leader Allister":"https://cdn.discordapp.com/attachments/1102579499989745764/1109611947713892362/Allister.png",
    "Salon Maiden Anabel":"https://cdn.discordapp.com/attachments/1102579499989745764/1109681004442046505/Anabel.png",
    "Rocket Admin Archer":"https://cdn.discordapp.com/attachments/1102579499989745764/1109681004727246958/Archer.png",
    "Rocket Admin Ariana":"https://cdn.discordapp.com/attachments/1102579499989745764/1136897549467394078/Spr_HGSS_Ariana.png",
    "Pokemon Trainer Barry":"https://media.tenor.com/M0jtKgsWg-4AAAAi/barry-dance.gif",
    "Gym Leader Bea":"https://cdn.discordapp.com/attachments/1102579499989745764/1111029602874294355/Bea.png",
    "Gym Leader Bede":"https://cdn.discordapp.com/attachments/1102579499989745764/1111030432801243176/Bede.png",
    "Boss Trainer Benga":"https://cdn.discordapp.com/attachments/1102579499989745764/1111031362300952747/Benga.png",
    "Elite Four Bertha":"https://cdn.discordapp.com/attachments/1102579499989745764/1111037750297243848/Bertha.png"
    }
    if name in spritelist:
        sprite=spritelist[name]
    else:
        sprite="https://play.pokemonshowdown.com/sprites/trainers/unknown.png"
    return sprite      