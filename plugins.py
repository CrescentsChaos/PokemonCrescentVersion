import random
import discord
import sqlite3
from pokemon import *
from movelist import *
from trainers import *
from pokemon import calcst
from typematchup import *
from AI import *
from hiddenpower import *
from moves import *
megastones=("Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Ampharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite")
async def usagerecord(team):
    db=sqlite3.connect("record.db")
    c=db.cursor()
    for i in team:
        c.execute(f"select * from `pokemons` where name='{i.name}'")
        v=c.fetchone()
        if v==None:
            #insert
            c.execute(f"""INSERT INTO `pokemons` VALUES (
            "{i.name}",
            "{i.nature} 1",
            "{(i.item.replace(' ','_')).replace('[Used]','')} 1",
            "{i.ability.replace(' ','_')} 1",
            1,
            0
            )""")
            db.commit()
        else:
            #update
            natures=await convert_items_string(v[1])
            items=await convert_items_string(v[2])
            abilities=await convert_items_string(v[3])
            if "Used" in i.item:
                    i.item=i.item.replace('[Used]','')
            if i.nature in natures:
                natures[i.nature]=natures[i.nature]+1
                natures=await convert_dict_string(natures)
            elif i.nature not in natures:
                natures[i.nature]=1
                natures=await convert_dict_string(natures)
            if i.item.replace(' ','_') in items:
                items[i.item.replace(' ','_')]=items[i.item.replace(' ','_')]+1
                items=await convert_dict_string(items)
            elif i.item.replace(' ','_') not in items:
                items[i.item.replace(' ','_')]=1
                items=await convert_dict_string(items)
            if i.ability.replace(' ','_') in abilities:
                abilities[i.ability.replace(' ','_')]=abilities[i.ability.replace(' ','_')]+1
                abilities=await convert_dict_string(abilities)
            elif i.ability.replace(' ','_') not in abilities:
                abilities[i.ability.replace(' ','_')]=1
                abilities=await convert_dict_string(abilities)
            c.execute(f"""Update `pokemons` set natures="{natures}",items="{items}",abilities="{abilities}",total={v[4]+1} where name='{i.name}'""")
            db.commit()
    c.execute(f"select * from `alltime`")
    tot=c.fetchone()
    tot=tot[0]
    c.execute(f"""Update `alltime` set total={tot+1}""")
    db.commit()
async def convert_items_string(input_string):
    # Converting string to dictionary
    items_dict = {}
    
    items_list = input_string.split(',')
    for item in items_list:
        item_name, item_usage = item.split()
        items_dict[item_name] = int(item_usage)
    return {key:value for key, value in sorted(items_dict.items(),key=lambda item: item[1],reverse=True)}

async def convert_dict_string(input_dict):
    # Converting dictionary to string
    items_list = []
    for item_name, item_usage in input_dict.items():
        items_list.append(item_name + ' ' + str(item_usage))
    return ','.join(items_list)
async def sortbadge(normal_list):
    sample_list=["Boulder Badge","Cascade Badge","Thunder Badge","Rainbow Badge","Soul Badge","Marsh Badge","Volcano Badge","Earth Badge","Zephyr Badge","Hive Badge","Plain Badge","Fog Badge","Storm Badge","Mineral Badge","Glacier Badge","Rising Badge","Stone Badge","Knuckle Badge","Dynamo Badge","Heat Badge","Balance Badge","Feather Badge","Mind Badge","Rain Badge","Coal Badge","Forrest Badge","Relic Badge","Cobble Badge","Fen Badge","Mine Badge","Beacon Badge","Trio Badge","Basic Badge","Insect Badge","Bolt Badge","Quake Badge","Jet Badge","Freeze Badge","Legend Badge","Bug Badge","Cliff Badge","Rumble Badge","Plant Badge","Pixie Badge","Voltage Badge","Psi Badge","Iceberg Badge","Grass Badge","Water Badge","Fighting Badge","Fire Badge","Ghost Badge","Fairy Badge","Rock Badge","Ice Badge","Dark Badge","Dragon Badge","Cortondo Badge","Artazon Badge","Levincia Badge","Medali Badge","Cascarrafa Badge","Montenevera Badge","Glaseado Badge","Alfornada Badge","Navi Badge","Schedar Badge","Ruchbah Badge","Segin Badge","Caph Badge","Gold Knowledge Symbol","Gold Tactics Symbol","Gold Guts Symbol","Gold Luck Symbol","Gold Ability Symbol","Gold Spirits Symbol","Gold Brave Symbol","Rocket Badge","Aqua Badge","Magma Badge","Galactic Badge","Plasma Badge"]
    return sorted(normal_list, key=lambda x: sample_list.index(x))

async def findnum(ctx,row):
    db=sqlite3.connect("owned.db")
    c=db.cursor()
    c.execute(f"select * from '{ctx.author.id}'")
    allmon=c.fetchall()
    allmon=list(allmon)
    c.execute(f"select * from '{ctx.author.id}' where rowid={row}")
    mon=c.fetchone()
    return allmon.index(mon)+1
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
    user=None
    try:
        user=ctx.author
    except:
        user=ctx.user
    c.execute(f"select *,rowid from '{user.id}'")    
    hh=c.fetchall()
    num=hh[num-1][27]            
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
async def subl(num, original):
    start = (num - 1) * 10
    end = start + 10

    sub_list = original[start:end]

    return sub_list
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
    "Max":"<:dynamax:1104646304904257647>",
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
    entry = discord.Embed(title="Entry Effects:",color=0xffffff)
    em = None
    if x.ability=="Vessel of Ruin":
        entry.add_field(name=f"<:vessel:1138386145194037258> {x.icon} {x.nickname}'s Vessel of Ruin!",value=f"{x.nickname} weakened the Special Attack of all surrounding Pokémon!")
    elif x.ability=="Sword of Ruin":
        entry.add_field(name=f"<:sword:1138386246348046336> {x.icon} {x.nickname}'s Sword of Ruin!",value=f"{x.nickname} weakened the Defense of all surrounding Pokémon!")
    elif x.ability=="Tablets of Ruin":
        entry.add_field(name=f"<:tablets:1138386311598837761> {x.icon} {x.nickname}'s Beads of Ruin!",value=f"{x.nickname} weakened the Attack of all surrounding Pokémon!")        
    elif x.ability=="Beads of Ruin":
        entry.add_field(name=f"<:beads:1138386205713633360> {x.icon} {x.nickname}'s Beads of Ruin!",value=f"{x.nickname} weakened the Special Defense of all surrounding Pokémon!")        
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
    if x.ability=="Intimidate" and y.ability not in ["Inner Focus","Oblivious","Clear Body","Good as Gold"] and x.item not in ["Clear Amulet"]:
        if y.ability!="Guard Dog":
            await atkchange(entry,y,x,-1)
        if y.ability=="Guard Dog":
            await atkchange(entry,y,x,1)            
        if y.item=="Adrenaline Orb":       
            await speedchange(entry,y,x,2)
    elif x.ability=="Majestic Moth":
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
    elif x.ability == "Comatose":
        entry.add_field(name=f"{x.icon} {x.nickname}'s Comatose!", value=f"{x.nickname} is in a drowsy state.")
        x.status = "Drowsy"    
    elif x.ability == "Flower Gift" and field.weather in ["Sunny", "Extreme Sunlight"] and "Cherrim" in x.name and x.sprite != "https://play.pokemonshowdown.com/sprites/ani/cherrim-sunshine.gif":
        entry.add_field(name=f"{x.icon} {x.nickname}'s Flower Gift!", value=f"{x.nickname} is reacting and absorbing sunlight!")
        x.sprite = "https://play.pokemonshowdown.com/sprites/ani/cherrim-sunshine.gif"
    elif x.ability == "Illusion":
        x.name = tr1.pokemons[-1].name
        x.nickname = tr1.pokemons[-1].nickname
        x.sprite = tr1.pokemons[-1].sprite
    elif x.ability == "Pressure" and y.ability not in ["Mold Breaker", "Teravolt", "Turboblaze", "Propeller Tail"]:
        entry.add_field(name=f"{x.icon} {x.nickname}'s Pressure!", value=f"{x.nickname} is exerting its pressure!")
    elif x.ability=="Supreme Overlord" and len(tr1.pokemons)!=0:
        entry.add_field(name=f"{x.icon} {x.nickname}'s Supreme Overlord!",value=f"{x.nickname} gained strength from the fallen!")  
    elif x.ability=="Frisk" and ("None" not in y.item and "Used" not in y.item):
        entry.add_field(name=f"{x.icon} {x.nickname}'s Frisk!",value=f"{y.nickname} is holding a {y.item}!")      
    elif x.ability in ["Air Lock","Cloud Nine"] and field.weather!="Clear":       
        entry.add_field(name=f"{x.icon} {x.nickname}'s Air Lock!",value=f"{x.nickname} nullified the effects of weather!")   
    elif x.ability=="Delta Stream" and field.weather!="Strong Winds":        
        entry.add_field(name=f"{x.icon} {x.nickname}'s Delta Stream!",value=f"Mysterious strong winds are protecting Flying-type Pokémon!")  
        field.weather="Strong Winds"
    elif x.ability=="Stakeout":
        x.atk*=2
        x.spatk*=2
    elif x.ability=="Trace" and y.ability not in ["As One","Battle Bond","Commander","Disguise","Forecast","Ice Face","Imposter","Illusion","Multitype","Power of Alchemy","Protosynthesis","Stance Change","Quark Drive","RKS System","Schooling","Trace","Zen Mode","Zero to Hero"] and y.item!="Ability Shield":
        entry.add_field(name=f"{x.icon} {x.nickname}'s Trace!",value=f"{x.nickname} gained {y.ability}!")
        x.ability=y.ability
        await entryeff(ctx,x,y,tr1,tr2,field,turn)   
    elif "Quark Drive" in x.ability and field.terrain=="Electric" and ("Booster Energy" not in x.item or "Used" in x.item):    
        entry.add_field(name=f"{x.icon} {x.nickname}'s Quark Drive!",value=f"Electric Terrain activated {x.icon} {x.nickname}'s Quark Drive!")   
    elif "Protosynthesis" in x.ability and field.weather in ["Sunny","Extreme Sunlight"] and ("Booster Energy" not in x.item or "Used" in x.item):    
        entry.add_field(name=f"{x.icon} {x.nickname}'s Protosynthesis!",value=f"Harsh sunlight activated {x.icon} {x.nickname}'s Protosynthesis!")  
    elif x.ability=="Costar":
        x.atkb=y.atkb
        x.defb=y.defb
        x.spatkb=y.spatkb
        x.spdefb=y.spdefb
        x.speedb=y.speedb   
        entry.add_field(name=f"{x.icon} {x.nickname}'s Costar!",value=f"{x.nickname} copied {y.icon} {y.nickname}'s stat boosts!")         
    elif x.ability=="Imposter" and y.dmax is False and y.item not in megastones:    
        entry.add_field(name=f"{x.icon} {x.nickname}'s Imposter!",value=f"{x.nickname} transformed into {y.nickname}!")
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
        entry.add_field(name=f"{x.icon} {x.nickname}'s Sand Stream!",value=f"️{x.nickname} whipped up a sandstorm!")
        field.weather="Sandstorm" 
        field.sandturn=turn
        await sandend(field,x,y)   
    elif x.ability=="Primordial Sea" and field.weather!="Heavy Rain":  
        entry.add_field(name=f"{x.icon} {x.nickname}'s Primordial Sea!",value=f"️A heavy rain began to fall!")
        field.weather="Heavy Rain"
    elif x.ability=="Desolate Land" and field.weather!="Extreme Sunlight":  
        entry.add_field(name=f"{x.icon} {x.nickname}'s Desolate Land!",value=f"️The sunlight turned extremely harsh!")
        field.weather="Extreme Sunlight"   
    elif x.ability=="Drought" and field.weather not in ["Sunny","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.icon} {x.nickname}'s Drought!",value=f"️{x.nickname} intensified the sun's rays!")
        field.weather="Sunny"  
        field.sunturn=turn
        await sunend(field,x,y)
    elif x.ability=="Orichalcum Pulse" and field.weather not in ["Sunny","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.icon} {x.nickname}'s Orichalcum Pulse!",value=f"️{x.nickname} turned the sunlight harsh, sending its ancient pulse into a frenzy!")
        field.weather="Sunny"  
        field.sunturn=turn
        await sunend(field,x,y)
    elif x.ability=="Drizzle" and field.weather not in ["Rainy","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.icon} {x.nickname}'s Drizzle!",value=f"️{x.nickname} made it rain!")
        field.weather="Rainy"  
        field.rainturn=turn
        await rainend(field,x,y)   
    elif x.ability=="Snow Warning" and field.weather not in ["Snowstorm","Heavy Rain","Extreme Sunlight"]:
        entry.add_field(name=f"{x.icon} {x.nickname}'s Snow Warning!",value=f"️{x.nickname} whipped up a snowstorm!")
        field.weather="Snowstorm"  
        field.snowturn=turn
        await snowend(field,x,y)  
    elif x.ability=="Electric Surge":
        entry.add_field(name=f"{x.icon} {x.nickname}'s Electric Surge!",value=f"️An electric x ran across the battlefield!")
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(x,y)  
    elif x.ability=="Hadron Engine":
        entry.add_field(name=f"{x.icon} {x.nickname}'s Hadron Engine!",value=f"️{x.nickname} summoned the Electric Terrain to energize its futuristic engine!")
        field.terrain="Electric"
        field.eleturn=turn
        field.eleend(x,y)       
    elif x.ability=="Misty Surge":
        entry.add_field(name=f"{x.icon} {x.nickname}'s Misty Surge!",value=f"️Mist swirled around the battlefield!")
        field.terrain="Misty"
        field.misturn=turn
        field.misend(x,y)     
    elif x.ability=="Grassy Surge":
        entry.add_field(name=f"{x.icon} {x.nickname}'s Grassy Surge!",value=f"️Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(x,y)   
    elif x.ability=="Psychic Surge":
        entry.add_field(name=f"{x.icon} {x.nickname}'s Psychic Surge!",value=f"️The battlefield got weird!")     
        field.terrain="Psychic"        
        field.psyturn=turn
        field.psyend(x,y)      
    elif x.ability=="North Wind":        
        tr1.auroraturn=turn
        tr1.auroraend(x,y)
        tr1.auroraveil=True  
        entry.add_field(name=f"{x.icon} {x.nickname}'s North Wind!",value="Aurora Veil will reduced your team's damage taken!")
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
        await speedchange(entry,x,y,-0.5)        
    if "Stealth Rock" in tr1.hazard and x.ability not in ["Magic Guard","Levitate","Shield Dust","Mountaineer"] and x.item not in ["Heavy-Duty Boots","Air Balloon"]:
        buff=2
        if x.primaryType in ["Flying", "Bug", "Fire", "Ice"] and x.teraType=="???":
            buff*=2
        if x.secondaryType in ["Flying", "Bug", "Fire", "Ice"] and x.teraType=="???":
            buff*=2
        if x.teraType in ["Flying", "Bug", "Fire", "Ice"]:
            buff*=2
        x.hp-=(1+(x.maxhp*0.0625*buff))
        entry.add_field(name=f"Stealth Rock!",value=f"️Pointed stones dug into {x.nickname}!")
    if "Steel Spikes" in tr1.hazard and x.ability not in ["Magic Guard","Levitate","Shield Dust","Mountaineer"] and x.item not in ["Heavy-Duty Boots","Air Balloon"]:
        buff=2
        if x.primaryType in ["Fairy", "Rock", "Ice"] and x.teraType=="???":
            buff*=2
        if x.secondaryType in ["Fairy", "Rock", "Ice"] and x.teraType=="???":
            buff*=2
        if x.teraType in ["Fairy", "Rock", "Ice"]:
            buff*=2
        x.hp-=(1+(x.maxhp*0.0625*buff))
        entry.add_field(name=f"Steel Spikes!",value=f"️Pointed steel spikes dug into {x.nickname}!")        
    await prebuff(ctx,x,y,tr1,tr2,turn,field)
    if len(entry.fields)!=0:
        await ctx.send(embed=entry)    
async def maxendturn(x,turn):
    if x.dmax is True:
       x.maxend=turn+2         
async def maxtrans(ctx,x,tr1,turn):
    x.dmax=True
    tr1.canmax=False
    x.choiced=False
    tr1.sub="None"
    x.choicedmove="None"
    x.nickname+=" <:dynamax:1104646304904257647>"
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
    x.nickname+=f" {await teraicon(x.tera)}"
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
        pre.add_field(name=f"{x.icon} {x.nickname}'s Schooling!",value="Wishiwashi formed a school!")
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
    if tr1.auroraveil is True and y.ability!="Infiltrator":
        defbuff*=2
        spdefbuff*=2
    if tr1.tailwind is True:   
        speedbuff*=2      
    if tr1.reflect is True and y.ability!="Infiltrator":
        defbuff*=2
    if tr1.lightscreen is True and y.ability!="Infiltrator":
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
            pre.add_field(name=f"{x.icon} {x.nickname}'s Zen Mode!",value=f"{x.nickname} transformed!")
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
            pre.add_field(name=f"{x.icon} {x.nickname}'s {await itemicon(x.item)} {x.item}!",value=f"{x.nickname} used its Booster Energy to activate Protosynthesis!")
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
            pre.add_field(name=f"{x.icon} {x.nickname}'s {await itemicon(x.item)} {x.item}!",value=f"{x.nickname} used its Booster Energy to activate Quark Drive!")
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
    elif y.ability=="Tablets of Ruin":
        atkbuff*=0.75
    elif y.ability=="Sword of Ruin":
        defbuff*=0.75
    elif y.ability=="Beads of Ruin":
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
    if field.weather in ["Rainy","Heavy Rain"] and x.ability=="Swift Swim" and y.ability!="Cloud Nine":
        speedbuff*=2
    if field.weather in ["Sunny","Extreme Sunlight"] and x.ability in ["Chlorophyll","Big Leaves"] and y.ability!="Cloud Nine":
        speedbuff*=2
    if field.weather in ["Sandstorm"] and x.ability=="Sand Rush" and y.ability!="Cloud Nine":
        speedbuff*=2
    if field.weather in ["Hail","Snowstorm"] and x.ability=="Slush Rush" and y.ability!="Cloud Nine":
        speedbuff*=2
    if field.weather=="Snowstorm" and ("Ice" in (x.primaryType,x.secondaryType,x.teraType)) and y.ability!="Cloud Nine":
        defbuff*=1.5
    elif field.weather=="Sandstorm" and ("Rock" in (x.primaryType,x.secondaryType,x.teraType)) and y.ability!="Cloud Nine":
        spdefbuff*=1.5
    if y.ability=="Fur Coat":
        atkbuff*=0.5
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
    elif x.ability=="Ice Scales":
        spdefbuff*=2
    elif x.ability in ["Sage Power","Majestic Bird"]:
        spatkbuff*=1.5
    elif x.ability=="Gorilla Tactics":
        atkbuff*=1.5        
    elif x.ability in ["Huge Power","Pure Power"]:
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
    if len(pre.fields)!=0:
        await ctx.send(embed=pre)        
async def action(bot, ctx, tr1, tr2, x, y):
    if tr1.ai:
        new=[]
        for i in tr1.pokemons:
            new.append(i.tera)
        if "m-Z" in x.item and tr1.canz==True and x.zuse==True:
            return 5
        elif x.item not in megastones and tr1.canmax and x.tera == "Max" and x.teraType=="???" and "m-Z" not in x.item:
           x.tera=random.choice([x.primaryType,x.secondaryType])
           return 8
        elif x.item not in megastones and tr1.canmax and x.teraType == "???" and "m-Z" not in x.item and "Max" not in new:
            maxch = random.randint(1, 6)
            return 8 if maxch == 1 else 1
        elif x.item in megastones and tr1.canmega:
            return random.choices([1, 6], weights=[1, 10], k=1)[0]
        elif x.tera not in ["???","Max"] and x.tera not in (x.primaryType, x.secondaryType) and tr1.cantera==True and tr1.canmega!=True:
            return 9
        else:
            return random.choices([1, 2], weights=[10, 1], k=1)[0]
    else:
        inaction = None
        while True:
            des = "#1 💥 Fight\n#2 🔁 Switch\n#3 🚫 Forfeit\n"
            if "m-Z" in x.item and tr1.canz and x.zuse:
                des+="#5 <:zmove:1140788256577949717> Z-Move\n"
            elif tr1.canmega and not x.dmax and (x.item in megastones or "Dragon Ascent" in x.moves) and x.teraType == "???":
                des += "#6 <:megaevolve:1104646688951500850> Mega Evolve\n"
            elif not x.dmax and x.item == "Ultranecrozium-Z" and "Ultra" not in x.name:
                des += "#7 Ultra Burst\n"
            elif tr1.canmax and not x.dmax and x.item not in megastones and x.teraType == "???" and "m-Z" not in x.item:
                des += "#8 <:dynamax:1104646304904257647> Dynamax/Gigantamax\n"
            if tr1.cantera and not x.dmax and x.item not in megastones and x.teraType == "???" and "m-Z" not in x.item and x.tera!="Max":
                des += f"#9 {await teraicon(x.tera)} Terastallize\n"
            em = discord.Embed(title=f"{tr1.name}, what do you wanna do?", description=des)
            em.set_footer(text="Wait a few seconds before entering your action. Re-enter action if it's not working.")
            if tr2.ai==True:
                await ctx.send(embed=em)
                inaction = await bot.wait_for('message', check=lambda msg: msg.author == ctx.author)
            else:
                await tr1.member.send(embed=em)
                inaction = await bot.wait_for('message', check=lambda msg: isinstance(msg.channel, discord.DMChannel) and msg.author == tr1.member)
            inaction = int(inaction.content)    
            if inaction is not None:
                break
        if inaction==2:
            if y.trap==True:
                inaction=1
            elif y.ability=="Magnet Pull" and "Steel" in (x.primaryType ,x.secondaryType ,x.teraType ):
                inaction=1
        return inaction
async def spartyup(tr1,x):
    di={
    "Male":"<:male:1140875825693085757>",
    "Female":"<:female:1140875954193956944>",
    "Genderless":"<:genderless:1140875679383175250>",
    "Sleep":"<:asleep:1140745217193021511>",
    "Burned":"<:burned:1140744974514782369>",
    "Poisoned":"<:poisoned:1140745045805379604>",
    "Badly Poisoned":"<:poisoned:1140745045805379604>",
    "Frozen":"<:frozen:1140745102889857045>",
    "Paralyzed":"<:paralyzed:1140745164231544954>",
    "Alive":"<:healthy:1140746496657080420>",
    "Drowsy":"<:asleep:1140745217193021511>",
    "Frostbite":"<:frozen:1140745102889857045>",
    "Fainted":"<:fainted:1142928844421070849>"
    }
    tr1.sparty[tr1.party.index(x.icon)]=di[x.status]
    return tr1.sparty
async def score(ctx, x, y, tr1, tr2, turn, bg):
    team=" ".join(tr1.party)
    tr1.sparty=await spartyup(tr1,x)
    steam=" ".join(tr1.sparty)
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
    if x.dmax==True:
        hpbar = "<:HP:1107296292243255356>" + "<:dynamax:1141227784958652547>"* int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    elif x.status in status_mapping:
        hpbar = "<:HP:1107296292243255356>" + status_mapping[x.status] * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    elif x.status == "Alive":
        if 0.6 < (x.hp / x.maxhp) <= 1:
            hpbar = "<:HP:1107296292243255356>" + "<:GREEN:1107296335780139113>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        elif 0.3 < (x.hp / x.maxhp) <= 0.6:
            hpbar = "<:HP:1107296292243255356>" + "<:YELLOW:1107331825929556111>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        elif 0 < (x.hp / x.maxhp) <= 0.3:
            hpbar = "<:HP:1107296292243255356>" + "<:RED:1107331787480379543>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    rflct=""
    if tr1.reflect==True:
        rflct=f"\n<:reflect:1142009182095163422> Reflect"
    ls=""
    if tr1.lightscreen==True:
        rflct=f"\n<:lightscreen:1142009225741082657> Light Screen"     
    av=""          
    if tr1.auroraveil==True:
        av=f"\n<:auroraveil:1142009279705006102> Aurora Veil"
    tw=""          
    if tr1.tailwind==True:
        av=f"\n<:tailwind:1142043322064572446> Tailwind"               
    em = discord.Embed(
        title=f"{tr1.name}:",
        description=f"{team}\n{steam}",
        color=bg,
    )
    em.add_field(name="Stats:", value=f"**{x.nickname}** Lv. {x.level}\n**HP:** {round(x.hp)}/{x.maxhp} ({round((x.hp/x.maxhp)*100,2)}%)\n**ATK:** {await bufficon(x.atkb)} **DEF:** {await bufficon(x.defb)} **SPA:** {await bufficon(x.spatkb)} **SPD:** {await bufficon(x.spdefb)} **SPE:** {await bufficon(x.speedb)}{rflct}{ls}{av}{tw}")
    em.add_field(name="HP Bar:", value=f"{hpbar}{await statusicon(x.status)}")
    em.set_image(url=x.sprite)
    em.set_footer(text=f"ATK: {x.atkb} DEF: {x.defb} SPA: {x.spatkb} SPD: {x.spdefb} SPE: {x.speedb}")
    if tr1.sub!="None":
        em.set_image(url="https://play.pokemonshowdown.com/sprites/substitutes/gen5/substitute.png")
    if x.gsprite != "None":
        em.set_image(url=x.gsprite)
    await ctx.send(embed=em)
async def bufficon(s,base=0):
    if s==base:
        return "<:base:1140755497323081789>"
    elif s<base:
        return "<:low:1140755454071418910>"
    elif s>base:
        return "<:high:1140755420533772389>"
async def statusicon(s):
    di={
    "Male":"<:male:1140875825693085757>",
    "Female":"<:female:1140875954193956944>",
    "Genderless":"<:genderless:1140875679383175250>",
    "Sleep":"<:asleep:1140745217193021511>",
    "Burned":"<:burned:1140744974514782369>",
    "Poisoned":"<:poisoned:1140745045805379604>",
    "Badly Poisoned":"<:poisoned:1140745045805379604>",
    "Frozen":"<:frozen:1140745102889857045>",
    "Paralyzed":"<:paralyzed:1140745164231544954>",
    "Alive":"<:healthy:1140746496657080420>",
    "Drowsy":"<:asleep:1140745217193021511>",
    "Frostbite":"<:frozen:1140745102889857045>",
    "Fainted":"<:fainted:1142928844421070849>"
    }
    return di[s]
async def advscore(ctx, x, y, tr1, tr2, turn, field, bg):
    team=" ".join(tr1.party)
    tr1.sparty=await spartyup(tr1,x)
    steam=" ".join(tr1.sparty)
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
    if x.dmax==True:
        hpbar = "<:HP:1107296292243255356>" + "<:dynamax:1141227784958652547>"* int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    elif x.status in status_mapping:
        hpbar = "<:HP:1107296292243255356>" + status_mapping[x.status] * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    elif x.status == "Alive":
        if 0.6 < (x.hp / x.maxhp) <= 1:
            hpbar = "<:HP:1107296292243255356>" + "<:GREEN:1107296335780139113>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        if 0.3 < (x.hp / x.maxhp) <= 0.6:
            hpbar = "<:HP:1107296292243255356>" + "<:YELLOW:1107331825929556111>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        if 0 < (x.hp / x.maxhp) <= 0.3:
            hpbar = "<:HP:1107296292243255356>" + "<:RED:1107331787480379543>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    itm=x.item
    if "Used" in itm:
        itm="None"
    rflct=""
    if tr1.reflect==True:
        rflct=f"\n<:reflect:1142009182095163422> Reflect ({tr1.rfendturn-turn} turns left)"
    ls=""
    if tr1.lightscreen==True:
        rflct=f"\n<:lightscreen:1142009225741082657> Light Screen ({tr1.screenend-turn} turns left)"     
    av=""          
    if tr1.auroraveil==True:
        av=f"\n<:auroraveil:1142009279705006102> Aurora Veil ({tr1.avendturn-turn} turns left)"
    tw=""          
    if tr1.tailwind==True:
        av=f"\n<:tailwind:1142043322064572446> Tailwind ({tr1.twendturn-turn} turns left)"        
    em = discord.Embed(
        title=f"{tr1.name}:",
        description=f"{team}\n{steam}",color=bg)
    em.add_field(name="Stats:",value=f"**{x.nickname}**{await statusicon(x.gender)} Lv. {x.level}\n**HP:** {round(x.hp)}/{x.maxhp} ({round((x.hp/x.maxhp)*100,2)}%)\n**Ability:** {x.ability}\n**Held Item:** {await itemicon(x.item)} {itm}\n**ATK:** {round(x.atk)}{await bufficon(x.atkb)} **DEF:** {round(x.defense)}{await bufficon(x.defb)} **SPA:** {round(x.spatk)}{await bufficon(x.spatkb)} **SPD:** {round(x.spdef)}{await bufficon(x.spdefb)} **SPE:** {round(x.speed)}{await bufficon(x.speedb)}{rflct}{ls}{av}{tw}")
    em.add_field(name="HP Bar:",value=f"{hpbar}{await statusicon(x.status)}")
    em.set_image(url=x.sprite)
    em.set_footer(text=f"ATK: {x.atkb} DEF: {x.defb} SPA: {x.spatkb} SPD: {x.spdefb} SPE: {x.speedb}")
    if tr1.sub!="None":
        em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1139438981445062719/20230811_120335.png")
    if x.gsprite!="None":
        em.set_image(url=x.gsprite)
    if tr2.ai==False:
        await tr1.member.send(embed=em)
    if tr2.ai==True:
        await ctx.send(embed=em)
        
async def movelist(ctx,x,tr1,tr2,field):
    move=""
    if x.dmax==False and x.zuse==False:
        for i in range(len(x.moves)):
            if i!=len(x.moves)-1:
                move+=f"#{i+1} {await movetypeicon(x,x.moves[i],field)} {x.moves[i]} {await movect(x.moves[i])} PP: {x.pplist[x.moves.index(x.moves[i])]}\n"
            elif i==len(x.moves)-1:
                move+=f"#{i+1} {await movetypeicon(x,x.moves[i],field)} {x.moves[i]} {await movect(x.moves[i])} PP: {x.pplist[x.moves.index(x.moves[i])]}"
    elif x.dmax==True:
        for i in range(len(x.maxmoves)):
            if i!=len(x.maxmoves)-1:
                move+=f"#{i+1} {await movetypeicon(x,x.maxmoves[i],field)} {x.maxmoves[i]} {await movect(x.maxmoves[i])} PP: {x.pplist[x.maxmoves.index(x.maxmoves[i])]}\n"
            elif i==len(x.maxmoves)-1:
                move+=f"#{i+1} {await movetypeicon(x,x.maxmoves[i],field)} {x.maxmoves[i]} {await movect(x.maxmoves[i])} PP: {x.pplist[x.maxmoves.index(x.maxmoves[i])]}"  
    elif x.zuse==True:
        move+=f"#1 {await movetypeicon(x,x.zmove,field)} {x.zmove} {await itemicon(x.item)} PP: 1"                
    em=discord.Embed(title=f"What will {x.nickname} use?",description=move,color=0xff0000)   
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
                if x.zuse==True and tr1.canz==True:
                    x.zuse=False
                    tr1.canz=False
                    return x.zmove
                elif choice.content not in ["1","2","3","4"] and choice.author==ctx.author:
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
                if x.zuse==True and tr1.canz==True:
                    x.zuse=False
                    tr1.canz=False
                    return x.zmove
                elif choice.content not in ["1","2","3","4"]:
                    await tr1.member.send("Wrong Input.")
                elif choice.content in ["1","2","3","4"]:
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
    des=f"{x.icon} {x.nickname}'s {x.item} is reacting to {tr1.name}'s Keystone!\n{x.name} has Mega Evolved into Mega {x.name}!"
    x.nickname+=" <:megaevolve:1104646688951500850>"
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
            if x.ability=="Chlorophyll":
                x.ability=="Big Leaves"
            else:
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
            x.spdef=85
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
            x.atk=160
            x.defense=70
            x.spatk=15
            x.spdef=90
            x.speed=175
            calcst(x)
            x.hp=x.maxhp*per      
        if x.item=="Pidgeotite" and "Pidgeot" in x.name:
            x.ability="No Guard"
            x.weight=111.33
            per=x.hp/x.maxhp
            x.hp=83
            x.atk=115
            x.defense=95
            x.spatk=115
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
    if x.hp<=0 and x.ability=="Eternamax":
        x.ability="Levitate"
        x.name="Eternamax Eternatus"
        x.sprite="https://cdn.discordapp.com/attachments/1102579499989745764/1142037644470124656/image0.gif"
        x.weight=9999.99
        x.hp=255
        x.atk=115
        x.defense=250
        x.spatk=125
        x.spdef=250
        x.speed=130
        calcst(x)        
        x.hp=x.maxhp
        em=discord.Embed(title="Eternatus's Eternamax!",description="Eternamax Eternamaxed itself and regained its true form.",color=0x8fd5f7)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1106824399983751248/Dynamax.png")
        em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1142037751101915207/image0.gif")
        await ctx.send(embed=em)
    if x.hp<=0 and x.ability=="Therian Reincarnation" and x.name=="Thundurus":
        x.dmax=False
        x.name="Therian Thundurus"
        x.ability="Volt Absorb"
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/thundurus-therian.gif"
        x.weight=134.48
        x.hp=79
        x.atk=105
        x.defense=70
        x.spatk=145
        x.spdef=80
        x.speed=101
        calcst(x)        
        x.hp=x.maxhp
        em=discord.Embed(title="Thundurus's Therian Reincarnation!",description="Thundurus transformed into it's therian forme after touching its <:revealglass:1140992335593885746> Reveal Glass.",color=0x8fd5f7)
        await atkchange(em,x,x,1)
        await defchange(em,x,x,1)
        await spatkchange(em,x,x,1)
        await spdefchange(em,x,x,1)
        await speedchange(em,x,x,1)
        em.set_image(url=x.sprite)
        await ctx.send(embed=em)
    elif x.hp<=0 and x.ability=="Therian Reincarnation" and x.name=="Enamorus":
        x.dmax=False
        x.name="Therian Enamorus"
        x.ability="Overcoat"
        x.sprite="https://cdn.discordapp.com/attachments/1102535204968599592/1141004828911353967/image_search_1692107000875.gif"
        x.weight=105.8
        x.hp=74
        x.atk=115
        x.defense=110
        x.spatk=135
        x.spdef=100
        x.speed=46
        calcst(x)        
        x.hp=x.maxhp
        em=discord.Embed(title="Enamorus's Therian Reincarnation!",description="Enamorus transformed into it's therian forme after touching its <:revealglass:1140992335593885746> Reveal Glass.",color=0xe9749c)
        await atkchange(em,x,x,1)
        await defchange(em,x,x,1)
        await spatkchange(em,x,x,1)
        await spdefchange(em,x,x,1)
        await speedchange(em,x,x,1)
        em.set_image(url=x.sprite)
        await ctx.send(embed=em)        
    elif x.hp<=0 and x.ability=="Therian Reincarnation" and x.name=="Tornadus":
        x.dmax=False
        x.name="Therian Tornadus"
        x.ability="Regenerator"
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/tornadus-therian.gif"
        x.weight=138.89
        x.hp=79
        x.atk=100
        x.defense=80
        x.spatk=110
        x.spdef=90
        x.speed=121
        calcst(x)        
        x.hp=x.maxhp
        em=discord.Embed(title="Tornadus's Therian Reincarnation!",description="Tornadus transformed into it's therian forme after touching its <:revealglass:1140992335593885746> Reveal Glass.",color=0x78b867)
        await atkchange(em,x,x,1)
        await defchange(em,x,x,1)
        await spatkchange(em,x,x,1)
        await spdefchange(em,x,x,1)
        await speedchange(em,x,x,1)
        em.set_image(url=x.sprite)
        await ctx.send(embed=em)    
    elif x.hp<=0 and x.ability=="Therian Reincarnation" and x.name=="Landorus":
        x.dmax=False
        x.name="Therian Landorus"
        x.ability="Intimidate"
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/landorus-therian.gif"
        x.weight=149.91
        x.hp=89
        x.atk=145
        x.defense=90
        x.spatk=105
        x.spdef=80
        x.speed=91
        calcst(x)        
        x.hp=x.maxhp
        em=discord.Embed(title="Landorus's Therian Reincarnation!",description="Landorus transformed into it's therian forme after touching its <:revealglass:1140992335593885746> Reveal Glass.",color=0xfea458)
        await atkchange(em,x,x,1)
        await defchange(em,x,x,1)
        await spatkchange(em,x,x,1)
        await spdefchange(em,x,x,1)
        await speedchange(em,x,x,1)
        em.set_image(url=x.sprite)
        await ctx.send(embed=em)
    elif x.hp<=0 and x.ability=="Mirage Metamorphosis":
        x.dmax=False
        x.name="Hoopa Unbound"
        x.ability="Magician"
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/hoopa-unbound.gif"
        x.weight=1080.27
        x.hp=80
        x.atk=160
        x.defense=60
        x.spatk=170
        x.spdef=130
        x.speed=80
        calcst(x)        
        x.hp=x.maxhp
        em=discord.Embed(title="Hoopa's Mirage Metamorphosis!",description="Hoopa transformed into it's unbound forme after absorbing its lost power from the <:prisonbottle:1138429051929907390> Prison Bottle.",color=0xab427a)
        await atkchange(em,x,x,1)
        await defchange(em,x,x,1)
        await spatkchange(em,x,x,1)
        await spdefchange(em,x,x,1)
        await speedchange(em,x,x,1)
        em.set_image(url=x.sprite)
        await ctx.send(embed=em)
    elif x.hp<=0 and x.ability=="Distorted Resurgence":
        x.dmax=False
        x.name="Origin Giratina"
        x.ability="Levitate"
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/giratina-origin.gif"
        x.weight=1433
        x.hp=150
        x.atk=120
        x.defense=100
        x.spatk=120
        x.spdef=100
        x.speed=90
        calcst(x)        
        x.hp=x.maxhp
        em=discord.Embed(title="Giratina's Distorted Resurgence!",description="Giratina transformed into it's origin forme after falling to the abyss.",color=0xfcf491)
        await atkchange(em,x,x,1)
        await defchange(em,x,x,1)
        await spatkchange(em,x,x,1)
        await spdefchange(em,x,x,1)
        await speedchange(em,x,x,1)
        em.set_image(url=x.sprite)
        await ctx.send(embed=em)
    elif x.hp<=0:
        x.status="Fainted"
        tr1.sparty=await spartyup(tr1,x)
        if " <:megaevolve:1104646688951500850>" in x.nickname and x.name not in ["Charizard","Mewtwo"]:
            x.sprite=x.sprite.replace("-mega","")
            x.nickname=x.nickname.replace(" <:megaevolve:1104646688951500850>","")
        elif " <:megaevolve:1104646688951500850>" in x.nickname and x.name in ["Charizard","Mewtwo"]:
            x.sprite=x.sprite.replace("-megax","")
            x.sprite=x.sprite.replace("-megay","")
            x.nickname=x.nickname.replace(" <:megaevolve:1104646688951500850>","")
        em=discord.Embed(title=f"{x.nickname} fainted!")
        em.set_image(url=x.sprite)
        if y.ability in ["Moxie","Chilling Neigh"]:
            em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"Knocking Out {x.nickname} made {y.nickname} go on a rampage!")
            await atkchange(em,y,y,1)
        elif y.ability in ["Soul-Heart","Grim Neigh"]:
            em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"Knocking Out {x.nickname} made {y.nickname} go on a rampage!")
            await spatkchange(em,y,y,1)
        elif y.ability=="As One":
            if "Shadow" in y.name:
                await spatkchange(em,y,y,1)
            elif "Ice" in y.name:
                await atkchange(em,y,y,1)
        elif y.ability=="Beast Boost":
            em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"Knocking Out {x.nickname} made {y.nickname} go on a rampage!")
            m=[a,b,c,d,e]=[y.atk,y.defense,y.spatk,y.spdef,y.speed]
            if tr2.reflect==True:
                m=[y.atk,y.defense/2,y.spatk,y.spdef,y.speed]
            if tr2.lightscreen==True:
                m=[y.atk,y.defense,y.spatk,y.spdef/2,y.speed]
            pp=max(m)
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
            bb=discord.Embed(title=f"{y.icon} {y.nickname}'s Battle Bond!",description=f"{y.nickname} transformed into Ash-Greninja!")
            bb.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1125023366278029402/image0.gif")
            await ctx.send(embed=bb)
        if x.ability=="Aftermath":
            y.hp-=(y.maxhp/4)
        if y.ability in ["Looter","Predator","Scavenger"]:
            y.hp+=(y.maxhp/4)    
            if y.hp>y.maxhp:
                y.hp=y.maxhp
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
        pass
        #await ctx.send(f"{member.display_name} {await numberify(price)} <:pokecoin:1134595078892044369> added to your balance!")
    if price<0:
        price=-price
        #await ctx.send(f"{member.display_name} {await numberify(price)} <:pokecoin:1134595078892044369> was deducted from your balance!")
    await ctx.channel.send(f"{member.display_name}'s New Balance: {await numberify(money)}<:pokecoin:1134595078892044369>")
               
async def winner(ctx,tr1,tr2):
    if tr2.ai==False:
        await usagerecord(tr2.fullteam)
    if tr1.ai==False:
        db=sqlite3.connect("record.db")
        c=db.cursor()
        await usagerecord(tr1.fullteam)
        for i in tr1.fullteam:
            c.execute(f"select * from `pokemons` where name='{i.name}'")
            v=c.fetchone()
            c.execute(f"""Update `pokemons` set wins={v[5]+1} where name='{i.name}'""")
            db.commit()
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
    await ctx.send(embed=em)        
        
#Effects    
async def effects(ctx,x,y,tr1,field,turn):
    if 0 in x.pplist:
        if x.dmax is False and x.use in x.moves:
            x.lostmoves.append(x.moves[x.pplist.index(0)])
            x.moves.remove(x.moves[x.pplist.index(0)])
            x.pplist.remove(0) 
        elif x.dmax is True and x.use in x.maxmoves:
            x.moves.remove(x.moves[x.pplist.index(0)])
            x.maxmoves.remove(x.maxmoves[x.pplist.index(0)])
            x.pplist.remove(0) 
         
    em=discord.Embed(title="Effects:")
    x.flinched=False
    x.canfakeout=False
    if turn==x.taunturn:
        x.taunted=False
    if turn==x.encendturn:
        x.encore=False
    if field.trickroom is True:
        if turn==field.troomendturn:
            field.trickroom=False
            em.add_field(name=f"Trick Room:",value="The dimensions returned to normal!")         
    if tr1.auroraveil is True:
        if turn==tr1.avendturn:
            tr1.auroraveil=False
            em.add_field(name=f"Aurora Veil:",value="The Aurora Veil wore off!") 
    if tr1.tailwind is True:        
        if turn==tr1.twendturn:
            tr1.tailwind=False
            em.add_field(name="Tailwind:",value="The Tailwind petered out!")
    if tr1.reflect is True:
        if turn==tr1.rfendturn:
            tr1.reflect=False
            em.add_field(name=f"Reflect:",value="The Reflect wore off!")
    if tr1.lightscreen is True:
        if turn==tr1.screenend:
            tr1.lightscreen=False
            em.add_field(name=f"Light Screen:",value="The Light Screen wore off!")
    if field.terrain=="Misty":
        if turn>=field.misendturn:
            em.add_field(name="Terrain:",value="The battlefield turned normal.")
            field.terrain="Normal"
    elif field.terrain=="Psychic":
        if turn>=field.psyendturn:
            em.add_field(name="Terrain:",value="The battlefield turned normal.")
            field.terrain="Normal"
    elif field.terrain=="Electric":
        if turn>=field.eleendturn:
            em.add_field(name="Terrain:",value="The battlefield turned normal.")
            field.terrain="Normal"
    elif field.terrain=="Grassy":
        if turn>=field.grassendturn:
            em.add_field(name="Terrain:",value="The battlefield turned normal.")
            field.terrain="Normal"
    if field.weather=="Snowstorm":
        if turn>=field.snowendturn:
            em.add_field(name="Weather:",value="The snowstorm stopped.")
            field.weather="Cloudy"            
    elif field.weather=="Hail":
        if turn>=field.hailendturn:
            em.add_field(name="Weather:",value="The hail stopped.")
            field.weather="Cloudy"
    elif field.weather=="Sandstorm":
        if turn>=field.sandendturn:
            em.add_field(name="Weather:",value="The sandstorm subsided.")
            field.weather="Clear"
    elif field.weather=="Sunny":
        if turn>=field.sunendturn:
            em.add_field(name="Weather:",value="The harsh sunlight faded.")
            field.weather="Clear"
    elif field.weather=="Rainy":
        if turn>=field.rainendturn:
            em.add_field(name="Weather:",value="The rain stopped.")
            field.weather="Cloudy"        
    elif field.weather=="Heavy Rain" and "Primordial Sea" not in (x.ability,y.ability) and "Marine" not in field.location:
        field.weather="Clear"
        em.add_field(name="Weather:",value="The heavy rainfall stopped.")
    elif field.weather=="Extreme Sunlight" and "Desolate Land" not in (x.ability,y.ability) and "Terra" not in field.location:
        field.weather="Clear"
        em.add_field(name="Weather:",value="The extreme sunlight fade away.")          
    #Dynamax Reset
    if x.dmax==True and turn==x.maxend:
        x.dmax=False
        x.gsprite="None"
        x.hp=round(x.hp/2)
        x.maxhp=round(x.maxhp/2)
        em.add_field(name="Dynamax End:",value=f"{x.name} returned to it's normal state!")
        x.nickname=x.nickname.replace(" <:dynamax:1104646304904257647>","")
        if "gmax" in x.sprite:
            x.sprite=x.sprite.replace("-gmax.gif",".gif")
    if x.fmove==True:
        x.fmoveturn-=1
        if x.fmoveturn==0:
            x.fmove=False
            await confuse(em,x,x,100)            
    #Perish            
    if x.perishturn!=0:
        x.perishturn-=1
        em.add_field(name="Perish Count:",value=f"{x.icon} {x.nickname}'s perish count fell to {x.perishturn}!")
        if x.perishturn==0:
            x.hp=0
            em.add_field(name="Perish End:",value=f"{x.nickname} perished away!")    
    #Flame Orb            
    if x.item=="Flame Orb" and x.status=="Alive" and x.hp>0:
        x.status="Burned"
        em.add_field(name=f"{x.icon} {x.nickname}'s {await itemicon(x.item)} {x.item}!",value=f"{x.nickname} was burned by its {x.item}!")
    #Toxic Orb        
    elif x.item=="Toxic Orb" and x.status=="Alive" and x.hp>0:
        x.status="Badly Poisoned"
        em.add_field(name=f"{x.icon} {x.nickname}'s {await itemicon(x.item)} {x.item}!",value=f"{x.nickname} was badly poisoned by its {x.item}!")          
    #BAD DREAMS
    if y.ability=="Bad Dreams" and x.status=="Sleep" and x.hp>0:
        x.hp-=round(x.maxhp/8)
        em.add_field(name="{y.icon} {y.nickname}'s Bad Dreams!",value=f"{x.nickname} is tormented.")
    #LEECH SEED
    if x.seeded==True and x.hp>0 and y.hp>0:
        em.add_field(name="Leeach Seed:",value=f"The opposing {x.icon} {x.nickname}'s health is sapped by leech seed!")
        x.hp-=round(x.maxhp/16)
        if y.hp<=(y.maxhp-y.maxhp/16):
            y.hp+=round(y.maxhp/16)    
    #HAIL DAMAGE
    if field.weather=="Hail" and x.ability not in ["Snow Cloak","Ice Body","Overcoat","Slush Rush"] and x.item!="Safety Googles" and x.hp>0:     
        if x.primaryType!="Ice" and x.secondaryType!="Ice" and x.teraType!="Ice" and x.ability!="Magic Guard":
            x.hp-=round(x.maxhp/16)
            em.add_field(name="<:hail:1141090300501176511> Hail:",value=f"{x.nickname} is pelted by the hail!")      
    #SAND DAMAGE
    elif field.weather =="Sandstorm" and x.ability not in ["Sand Veil","Sand Force","Overcoat","Sand Rush"] and x.item!="Safety Googles" and x.hp>0:
        if x.primaryType not in ["Rock","Ground","Steel"] and x.secondaryType not in ["Rock","Ground","Steel"] and x.teraType not in ["Rock","Ground","Steel"] and x.ability!="Magic Guard":
            x.hp-=(1+round(x.maxhp/16))
            em.add_field(name="<:sandstorm:1141088700047048744> Sandstorm:",value=f"{x.nickname} is buffeted by the sandstorm!")
    if x.gravendturn==turn:
        x.grav=False
    if x.vlendturn==turn:
        x.vldmg=False
    if x.cntendturn==turn:
        x.cntdmg=False
    if x.cnendturn==turn:
        x.cndmg=False
    if x.wfendturn==turn:
        x.wfdmg=False
    if x.magmaendturn==turn:
        x.magmadmg=False
    #Badly Poisoned            
    if x.status=="Badly Poisoned" and x.ability not in ["Magic Guard","Poison Heal","Toxic Boost","Immunity"] and x.hp>0:
        x.hp-=(1+(x.maxhp*x.toxicCounter/16))
        x.toxicCounter+=1
        em.add_field(name="<:poisoned:1140745045805379604> Badly Poisoned:",value=f"{x.name} was hurt by fatal poison!")
    #Burned        
    if x.status=="Burned" and x.ability!="Magic Guard" and x.hp>0:
        em.add_field(name="<:burned:1140744974514782369> Burn:",value=f"{x.name} was hurt by burn!")
        x.hp-=x.maxhp/16
    #poisoned
    if x.status=="Poisoned" and x.ability!="Magic Guard" and x.hp>0:
        em.add_field(name="<:poisoned:1140745045805379604> Poisoned:",value=f"{x.name} was hurt by poison!")
        x.hp-=x.maxhp/8   
    #Infestation end       
    if x.infestation==turn or (x.infestation!=False and "Infestation" not in y.moves):
        x.infestation=False
        em.add_field(name="Infestation:",value=f"{x.nickname} is freed from the infestation.")        
    #Sand Tomb free        
    if x.sandtomb==turn or (x.sandtomb!=False and "Sand Tomb" not in y.moves):
        x.sandtomb=False
        em.add_field(name="Sand Tomb:",value=f"{x.nickname} is freed from the sand tomb.")
    #Whirlpool free       
    if x.whirlpool==turn or (x.whirlpool!=False and "Whirlpool" not in y.moves):
        x.whirlpool=False
        em.add_field(name="Whirlpool:",value=f"{x.nickname} is freed from the whirlpool.")
    #Fire spin free        
    if x.firespin==turn or (x.firespin!=False and "Fire Spin" not in y.moves):
        x.firespin=False
        em.add_field(name="Fire Spin:",value=f"{x.nickname} is freed from the vortex of fire.")        
    #Speed Boost        
    if x.ability=="Speed Boost" and x.hp>0:
        await speedchange(em,x,y,1)        
    #Trap damage        
    if x.wfdmg==True and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="G-Max Wildfire:",value=f"{x.nickname} is hurt by G-Max Wildlife’s flames!")
        x.hp-=(x.maxhp/6)
    if tr1.vcdmg==True and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="G-Max Volcalith:",value=f"{x.nickname} is hurt by the rocks thrown out by G-Max Volcalith!")
        x.hp-=(x.maxhp/6)         
    if x.vldmg==True and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="G-Max Vine Lash:",value=f"{x.nickname} is hurt by G-Max Vine Lash’s ferocious beating!")
        x.hp-=(x.maxhp/6)
    if x.cntdmg==True and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="G-Max Centiferno:",value=f"{x.nickname} is hurt by G-Max Centiferno’s vortex!")
        x.hp-=(x.maxhp/6) 
    if x.cndmg==True and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="G-Max Cannonade:",value=f"{x.nickname} is hurt by G-Max Cannonade’s vortex!")
        x.hp-=(x.maxhp/6)
    if x.magmadmg==True and x.hp>0 and "Magma Storm" in y.moves and x.ability!="Magic Guard":
        em.add_field(name="Magma Storm:",value=f"{x.nickname} was hurt by Magma Storm!")
        if y.item!="Binding Band":
            x.hp-=(x.maxhp/8)
        if y.item=="Binding Band":
            x.hp-=(x.maxhp/6)                
    if x.infestation!=0 and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="Infestation:",value=f"{x.nickname} is hurt by the infestation!")
        x.hp-=(x.maxhp/16)   
    if x.sandtomb!=0 and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="Sand Tomb:",value=f"{x.nickname} is hurt by the sand tomb!")
        x.hp-=(x.maxhp/16)   
    if x.whirlpool!=0 and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="Whirlpool:",value=f"{x.nickname} is hurt by the whirlpool!")
        x.hp-=(x.maxhp/16)   
    if x.firespin!=0 and x.hp>0 and x.ability!="Magic Guard":
        em.add_field(name="Fire Spin:",value=f"{x.nickname} is hurt by the vortex of fire!")
        x.hp-=(x.maxhp/16)        
    #Leftovers       
    if x.hp>0 and x.hp<x.maxhp and x.item=="Leftovers":
        em.add_field(name=f"{x.icon} {x.nickname}'s {await itemicon(x.item)} {x.item}!",value=f"{x.nickname} restored a little HP using its Leftovers.")
        x.hp+=round(x.maxhp/16) 
        if x.hp>x.maxhp:
            x.hp=x.maxhp
    #Ice Body
    if x.hp>0 and x.hp<x.maxhp and field.weather in ["Snowstorm","Hail"] and x.ability=="Ice Body":
        em.add_field(name=f"<:snowstorm:1141089242731266180> {x.icon} {x.nickname}'s Ice Body!",value=f"{x.nickname} restored a little HP using its Ice Body.")
        x.hp+=round(x.maxhp/8)    
        if x.hp>x.maxhp:
            x.hp=x.maxhp     
    #Poison Heal
    if x.hp>0 and x.hp<x.maxhp and x.ability=="Poison Heal" and "Poisoned" in x.status:
        em.add_field(name=f"{x.icon} {x.nickname}'s Poison Heal!",value=f"{x.nickname} restored a little HP using its Poison Heal.")
        x.hp+=round(x.maxhp/8)       
        if x.hp>x.maxhp:
            x.hp=x.maxhp 
    #Black Sludge
    if x.hp>0 and x.hp<x.maxhp and x.item=="Black Sludge":
        if "Poison" in (x.primaryType,x.secondaryType,x.teraType):
            em.add_field(name=f"{x.icon} {x.nickname}'s {await itemicon(x.item)} {x.item}!",value=f"{x.nickname} restored a little HP using its Black Sludge.")
            x.hp+=round(x.maxhp/16)   
            if x.hp>x.maxhp:
                x.hp=x.maxhp   
        else:  
            em.add_field(name=f"{x.icon} {x.nickname}'s {await itemicon(x.item)} {x.item}!",value=f"{x.nickname} lost a little HP using its Black Sludge.")
            x.hp-=round(x.maxhp/16)
    #Aqua Ring        
    if x.hp>0 and x.hp<x.maxhp and x.aring is True:
        em.add_field(name="Aqua Ring:",value=f"{x.nickname} restored a little HP using its Aqua Ring.")
        if x.item=="Big Root":
            x.hp+=round((x.maxhp/16)*1.3)
            if x.hp>x.maxhp:
                x.hp=x.maxhp
        else:
            x.hp+=round(x.maxhp/16)      
            if x.hp>x.maxhp:
                x.hp=x.maxhp    
    #Grassy Terrain            
    if x.hp>0 and field.terrain =="Grassy" and x.hp<x.maxhp and (x.ability not in ["Levitate"] and "Flying" not in (x.primaryType,x.secondaryType,x.teraType) or x.grav is True):
        em.add_field(name="<:grassy:1141090982788603985> Grassy Terrain:",value=f"{x.icon} {x.nickname}'s HP was restored.")
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

async def partyup(tr1,new):
    if new.icon not in tr1.party:
        tr1.party[tr1.party.index("<:ball:1127196564948009052>")]=new.icon
    return tr1.party                
async def switch(ctx,bot,x,y,tr1,tr2,field,turn):
    if x.dmax==True:
        x.gsprite=x.sprite
        x.nickname=x.nickname.replace(" <:dynamax:1104646304904257647>","")
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
    if tr1.sub!="None" and "Shed Tail" not in x.moves:
        tr1.sub="None"
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
        tr1.party=await partyup(tr1,new)       
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
                        tr1.party=await partyup(tr1,new)      
                        return new
                    if x not in tr1.pokemons:
                        new=tr1.pokemons[num]                          
                        await entryeff(ctx,new,y,tr1,tr2,field,turn)
                        em=discord.Embed(title=f"{tr1.name} sent out {new.nickname}!")
                        em.set_thumbnail(url=tr1.sprite)
                        em.set_image(url=new.sprite)
                        await ctx.send(embed=em)
                        tr1.party=await partyup(tr1,new)      
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
                        tr1.party=await partyup(tr1,new)      
                        return new
                    if x not in tr1.pokemons:
                        new=tr1.pokemons[num]                          
                        await entryeff(ctx,new,y,tr1,tr2,field,turn)
                        em=discord.Embed(title=f"{tr1.name} sent out {new.nickname}!")
                        em.set_thumbnail(url=tr1.sprite)
                        em.set_image(url=new.sprite)
                        await ctx.send(embed=em)
                        tr1.party=await partyup(tr1,new)      
                        return new
async def withdraweff(ctx, x, tr1, y):
    em = discord.Embed(title="Withdraw Effect:")
    if x.ability == "Zero to Hero" and "Hero" not in x.name and x.hp > 0 and not x.dmax:
        em.add_field(name=f"{x.icon} {x.name}'s Zero to Hero!", value=f"{x.name} underwent a heroic transformation!")
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
        em.add_field(name=f"{x.icon} {x.name}'s Natural Cure!", value=f"{x.name}'s status condition was cured!")
        x.status = "Alive"
    
    if x.ability == "Regenerator" and 0 < x.hp < x.maxhp and x.status != "Fainted":
        em.add_field(name=f"{x.icon} {x.name}'s Regenerator!", value=f"{x.name} regenerated a bit of its health!")
        if x.hp<x.maxhp:
            x.hp += round(x.maxhp/3)
            if x.hp>x.maxhp:
                x.hp = x.maxhp
    if len(em.fields)!=0:
        await ctx.send(embed=em)                    

async def teambuild(team):
    new=[]
    if len(team)>6:
        while len(new)!=5:
            mon=random.choice(team)
            if mon not in new and mon!=team[5]:
                new.append(mon)
        new.append(team[5])        
        return new         
    else:
        return team   
async def gamemonvert(tr,m):
    dt = sqlite3.connect("pokemondata.db")
    cx = dt.cursor()
    print(m[0])
    xxx = m[0]
    ability = m[8]
    newname=m[1]
    if xxx==newname:
        newname=xxx
    if m[0] == "Zacian" and m[11] == "Rusted Sword":
        xxx= "Crowned Zacian"
    elif m[0] == "Zamazenta" and m[11] == "Rusted Shield":
        xxx=newname= "Crowned Zamazenta"
    elif m[0] == "Palkia" and m[11] == "Lustrous Globe":
        xxx= "Origin Palkia"   
    elif m[0] == "Dialga" and m[11] == "Adamant Crystal":
        xxx= "Origin Dialga"     
    elif m[0] == "Giratina" and m[11] == "Griseous Core":
        xxx="Origin Giratina"
        ability="Levitate"
    cx.execute(f"SELECT * FROM 'wild' WHERE name='{xxx}'")
    n = cx.fetchall()[0]
    itm="None"
    moves = m[14]
    ter=m[13]
    if ter!="???" and "," in ter:
        ter=random.choice(ter.split(","))
    if ability == "None":
        ability = n[11]
    if moves == "A,B,C,D":
        moves = n[10]
    if m[1]==None:
        newname=m[0]
    if m[11]!="None":
        itm=random.choice(m[11].split(","))
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
        ability=random.choice(ability.split(",")),
        nature=random.choice(m[9].split(",")),
        shiny=m[10],
        item=itm,
        gender=m[12],
        tera=ter,
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
    players=("World Champion Ash","Professor Oak","Researcher Gary Oak","Team Rocket James","Team Rocket Jessie","Pokemon Breeder Brock","Gym Leader Brock","Tomboyish Mermaid Misty","Gym Leader Misty","Gym Leader Lt.Surge","Gym Leader Erika","Gym Leader Janine","Gym Leader Sabrina","Gym Leader Blaine","Gym Leader Blue","Elite Four Lorelei","Champion Lorelei(Rain)","Champion Lorelei(Hail)","Elite Four Bruno","Elite Four Agatha","Kanto Champion Lance","Pokemon Trainer Green","Pokemon Trainer Trace","Kanto Champion Red","Rocket Boss Giovanni","Pokemon Trainer Silver","Gym Leader Falkner","Gym Leader Bugsy","Gym Leader Morty","Gym Leader Chuck","Gym Leader Jasmine","Gym Leader Pryce","Gym Leader Clair","Elite Four Will","Elite Four Koga","Elite Four Karen","Rocket Admin Archer","Rocket Admin Ariana","Pokemon Trainer Harrison","Pokemon Trainer May","Gym Leader Roxanne","Gym Leader Brawly","Gym Leader Wattson","Gym Leader Flannery","Gym Leader Norman","Gym Leader Winona","Gym Leader Tate","Gym Leader Liza","Gym Leader Juan","Elite Four Sidney","Elite Four Phoebe","Elite Four Glacia","Elite Four Drake","Hoenn Champion Steven","Hoenn Champion Wallace","Aqua Leader Archie","Magma Admin Courtney","Magma Leader Maxie","Factory Head Noland","Arena Tycoon Greta","Dome Ace Tucker","Palace Maven Spenser","Pike Queen Lucy","Salon Maiden Anabel","Pyramid King Brandon","Pokemon Trainer Paul","Pokemon Trainer Barry","Pokemon Trainer Conway","Gym Leader Roark","Gym Leader Gardenia","Gym Leader Maylene","Gym Leader Crasher Wake","Gym Leader Fantina","Gym Leader Byron","Gym Leader Candice","Gym Leader Volkner","Elite Four Aaron","Elite Four Bertha","Elite Four Flint","Elite Four Lucian","Sinnoh Champion Cynthia","Pokemon Trainer Tobias","Galactic Commander Mars","Galactic Commander Jupiter","Galactic Commander Saturn","Galactic Leader Cyrus","Pokemon Trainer Riley","Pokemon Trainer Cheryl","Pokemon Trainer Marley","Pokemon Trainer Mira","Pokemon Trainer Buck","Factory Head Thorton","Battle Arcade Dahlia","Castle Velvet Darach","Hall Matron Argenta","Tower Tycoon Palmer","Pokemon Trainer Trip","Pokemon Trainer Cameron","Pokemon Trainer Stephan","Gym Leader Cilan","Gym Leader Cress","Gym Leader Chili","Pokemon Trainer Cheren","Pokemon Trainer Bianca","Gym Leader Lenora","Gym Leader Roxie","Gym Leader Burgh","Gym Leader Elesa","Gym Leader Clay","Gym Leader Skyla","Gym Leader Brycen","Gym Leader Marlon","Gym Leader Drayden","Gym Leader Marlon","Elite Four Marshal","Elite Four Shauntal","Elite Four Grimsley","Elite Four Caitlin","Unova Champion Alder","Unova Champion Iris","Pokemon Trainer Hugh","Plasma Admin Colress","Natural Harmonia Gropius","Plasma Leader Ghetsis","Boss Trainer Benga","Subway Boss Ingo","Subway Boss Emmet","Pokemon Trainer Sawyer","Pokemon Trainer Trevor","Pokemon Trainer Tierno","Pokemon Trainer Shauna","Gym Leader Viola","Gym Leader Grant","Gym Leader Korrina","Gym Leader Ramos","Gym Leader Clemont","Gym Leader Valerie","Gym Leader Olympia","Gym Leader Wulfric","Elite Four Siebold","Elite Four Wikstrom","Elite Four Malva","Elite Four Drasna","Pokemon Trainer Alain","Kalos Champion Diantha","Flare Boss Lysandre","Pokemon Trainer Gladion","Trial Captain Kiawe","Trial Captain Lana","Trial Captain Lillie","Trial Captain Mallow","Island Kahuna Ilima","Trial Captain Nanu","Elite Four Hala","Elite Four Olivia","Elite Four Molayne","Professor Kukui","Skull Admin Plumeria","Skull Leader Guzma","Aether Foundation Faba","Aether President Lusamine","Gym Leader Milo","Gym Leader Nessa","Gym Leader Kabu","Gym Leader Bede","Gym Leader Bea","Gym Leader Allister","Gym Leader Opal","Gym Leader Gordie","Gym Leader Marnie","Gym Leader Piers","Gym Leader Raihan","Pokemon Trainer Hop","Galar Champion Peony","Galar Champion Leon","Chairman Rose","Galar Champion Mustard","Instructor Jacq","Instructor Miriam","Instructor Tyme","Instructor Dendra","Gym Leader Katy","Gym Leader Brassius","Gym Leader Iono","Gym Leader Kofu","Gym Leader Ryme","Gym Leader Tulip","Gym Leader Grusha","Team Star Giacomo","Team Star Mela","Team Star Atticus","Team Star Ortega","Team Star Eri","Star Leader Penny","Elite Four Rika","Elite Four Poppy","Elite Four Larry","Elite Four Hassel","Paldea Champion Geeta","Paldea Champion Nemona","Professor Sada","Professor Turo","Elite Four Acerola","Pokemon Trainer Drew","Battle Chatelaine Evelyn","Island Kahuna Hapu","Fusion Creator Darwin","Elite Four Kahili","Coordinator Kenny","Gym Leader Klara","Aqua Admin Matt","Battle Chatelaine Nita","Pokemon Wielder Volo","Nurse Joy","Evil Trainer Crescent","Cipher Head Evice")
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
    name=await checkname(name)
    for i in mons:
        p=await gamemonvert(name,i)
        if p.name=="Pikachu":
            if name=="Kanto Champion Red":
                p.sprite="https://play.pokemonshowdown.com/sprites/ani/pikachu-starter.gif"
            elif name=="World Champion Ash":
                p.sprite=f"https://play.pokemonshowdown.com/sprites/ani/pikachu{random.choice(['-partner','','-alola','-hoenn','-kalos','-sinnoh','-unova','-original'])}.gif"
        team.append(p)
    mons=await teambuild(team)
    tr1=Trainer(name,mons,"Unknown",sprite=sprite,ai=True)
    return tr1    
async def trsprite(name):
    spritelist={
    "Instructor Dendra":"https://play.pokemonshowdown.com/sprites/trainers/dendra.png",
    "Instructor Tyme":"https://play.pokemonshowdown.com/sprites/trainers/tyme.png",
    "Instructor Jacq":"https://play.pokemonshowdown.com/sprites/trainers/jacq.png",
    "Instructor Miriam":"https://play.pokemonshowdown.com/sprites/trainers/miriam.png",
    "Pokemon Trainer Hugh":"https://play.pokemonshowdown.com/sprites/trainers/hugh.png",
    "Cipher Head Evice":"https://cdn.discordapp.com/attachments/1102579499989745764/1143884401780990012/20230823_182800.png",
    "Pokemon Trainer Harrison":"https://cdn.discordapp.com/attachments/1102579499989745764/1143763951184785408/20230823_102906.png",
    "Gym Leader Chili":"https://play.pokemonshowdown.com/sprites/trainers/chili.png",
    "Gym Leader Cress":"https://play.pokemonshowdown.com/sprites/trainers/cress.png",
    "Pokemon Trainer Bianca":"https://play.pokemonshowdown.com/sprites/trainers/bianca.png",
    "Pokemon Trainer Stephan":"https://cdn.discordapp.com/attachments/1102579499989745764/1143754567297806517/20230823_095207.png",
    "Pokemon Trainer Trip":"https://cdn.discordapp.com/attachments/1102579499989745764/1143597556773949520/20230822_232813.png",
    "Pokemon Trainer Cameron":"https://cdn.discordapp.com/attachments/1102579499989745764/1143595948983988294/20230822_232150.png",
    "Pokemon Trainer Silver":"https://cdn.discordapp.com/attachments/1102579499989745764/1143486243842314340/20230822_160554.png",
    "Pokemon Trainer Trace":"https://cdn.discordapp.com/attachments/1102579499989745764/1143485651145203762/20230822_160305.png",
    "Pokemon Trainer Green":"https://cdn.discordapp.com/attachments/1102579499989745764/1143485660976660570/20230822_160335.png",
    "Pokemon Trainer Shauna":"https://play.pokemonshowdown.com/sprites/trainers/shauna.png",
    "Pokemon Trainer Tierno":"https://play.pokemonshowdown.com/sprites/trainers/tierno.png",
    "Pokemon Trainer Trevor":"https://play.pokemonshowdown.com/sprites/trainers/trevor.png",
    "Pokemon Trainer Sawyer":"https://cdn.discordapp.com/attachments/1102579499989745764/1143377840205733928/20230822_085457.png",
    "Nurse Joy":"https://cdn.discordapp.com/attachments/1102579499989745764/1142455980181954590/20230819_195155.png",
    "Gym Leader Valerie":"https://play.pokemonshowdown.com/sprites/trainers/valerie.png",
    "Gym Leader Cilan":"https://play.pokemonshowdown.com/sprites/trainers/cilan.png",
    "Gym Leader Viola":"https://play.pokemonshowdown.com/sprites/trainers/viola.png",
    "Team Star Eri":"https://play.pokemonshowdown.com/sprites/trainers/eri.png",
    "Team Star Mela":"https://play.pokemonshowdown.com/sprites/trainers/mela.png",
    "Team Star Giacomo":"https://play.pokemonshowdown.com/sprites/trainers/giacomo.png",
    "Team Star Atticus":"https://play.pokemonshowdown.com/sprites/trainers/atticus.png",
    "Hall Matron Argenta":"https://cdn.discordapp.com/attachments/1102579499989745764/1140512276017840168/KatePlatinum.gif",
    "Gym Leader Wulfric":"https://cdn.discordapp.com/attachments/1102579499989745764/1140300033028259910/image_search_1691939087769.png",
    "Elite Four Will":"https://cdn.discordapp.com/attachments/1102579499989745764/1138413461248950403/Spr_HGSS_Will.png",
    "Pokemon Wielder Volo":"https://play.pokemonshowdown.com/sprites/trainers/volo.png",
    "Gym Leader Volkner":"https://cdn.discordapp.com/attachments/1102579499989745764/1138361906139242527/Spr_B2W2_Volkner.png",
    "Gym Leader Tulip":"https://cdn.discordapp.com/attachments/1102579499989745764/1137992736453177365/20230807_121640.png",
    "Elite Four Sidney":"https://play.pokemonshowdown.com/sprites/trainers/sidney.png",
    "World Champion Ash":random.choice(["https://play.pokemonshowdown.com/sprites/trainers/ash-alola.png","https://play.pokemonshowdown.com/sprites/trainers/ash-capbackward.png","https://play.pokemonshowdown.com/sprites/trainers/ash-hoenn.png","https://play.pokemonshowdown.com/sprites/trainers/ash-johto.png","https://play.pokemonshowdown.com/sprites/trainers/ash-kalos.png","https://play.pokemonshowdown.com/sprites/trainers/ash-sinnoh.png","https://play.pokemonshowdown.com/sprites/trainers/ash-unova.png","https://play.pokemonshowdown.com/sprites/trainers/ash.png"]),
    "Elite Four Shauntal":"https://cdn.discordapp.com/attachments/1102579499989745764/1136917784996089906/Spr_B2W2_Shauntal.png",
    "Pokemon Trainer Tobias":"https://cdn.discordapp.com/attachments/1102579499989745764/1136904651510394943/1691129578488.png",
    "Professor Turo":"https://play.pokemonshowdown.com/sprites/trainers/turo.png",
    "Professor Sada":"https://play.pokemonshowdown.com/sprites/trainers/sada.png",
    "Dome Ace Tucker":"https://cdn.discordapp.com/attachments/1102579499989745764/1136899891789045780/Spr_E_Tucker.png",
    "Palace Maven Spenser":"https://cdn.discordapp.com/attachments/1102579499989745764/1136898826507137104/Spr_E_Spenser.png",
    "Gym Leader Janine":"https://cdn.discordapp.com/attachments/1102579499989745764/1140291026578321478/JanineHGSSSprite.gif",
    "Gym Leader Skyla":"https://cdn.discordapp.com/attachments/1102579499989745764/1136898405508063252/Spr_B2W2_Skyla.png",
    "Galactic Commander Saturn":"https://cdn.discordapp.com/attachments/1102579499989745764/1136897817684754494/Spr_DP_Saturn.png",
    "Factory Head Thorton":"https://cdn.discordapp.com/attachments/1102579499989745764/1140296434642604112/NejikiPlatinum.gif",
    "Hoenn Champion Wallace":"https://cdn.discordapp.com/attachments/1102579499989745764/1140288579105460224/WallaceB2W2sprite.gif",
    "Gym Leader Tate":"https://cdn.discordapp.com/attachments/1102579499989745764/1136897295825240104/Spr_B2W2_Tate.png",
    "Gym Leader Winona":"https://cdn.discordapp.com/attachments/1102579499989745764/1136615608037941360/image_search_1691060615276.png",
    "Gym Leader Wattson":"https://cdn.discordapp.com/attachments/1102579499989745764/1136615607631106078/image_search_1691060604914.png",
    "Elite Four Siebold":"https://play.pokemonshowdown.com/sprites/trainers/siebold.png",
    "Elite Four Wikstrom":"https://cdn.discordapp.com/attachments/1102579499989745764/1136901309019205662/image_search_1691128774978.png",
    "Pokemon Trainer Cheryl":"https://cdn.discordapp.com/attachments/1102579499989745764/1126801413515780146/Cheryl.png",
    "Pokemon Trainer Buck":"https://cdn.discordapp.com/attachments/1102579499989745764/1126801176525029396/Buck.png",
    "Gym Leader Ryme":"https://play.pokemonshowdown.com/sprites/trainers/ryme.png",
    "Gym Leader Roxie":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580957487194/Roxie.png",
    "Gym Leader Roxanne":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580739379200/Roxanne.png",
    "Chairman Rose":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580470935562/Rose.png",
    "Gym Leader Roark":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580257038336/Roark.png",
    "Pokemon Trainer Riley":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792580030541964/Riley.png",
    "Elite Four Rika":"https://play.pokemonshowdown.com/sprites/trainers/rika.png",
    "Kanto Champion Red":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792579544006806/Red.png",
    "Gym Leader Ramos":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792579309121536/Ramos.png",
    "Gym Leader Raihan":"https://cdn.discordapp.com/attachments/1102579499989745764/1126792579057455124/Raihan.png",
    "Gym Leader Pryce":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767579650871366/Pryce.png",
    "Elite Four Poppy":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767579415982110/Poppy.png",
    "Skull Admin Plumeria":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767579172716614/Plumeria.png",
    "Gym Leader Piers":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767578904285254/Piers.png",
    "Elite Four Phoebe":"https://play.pokemonshowdown.com/sprites/trainers/phoebe-gen6.png",
    "Galar Champion Peony":"https://play.pokemonshowdown.com/sprites/trainers/peony.png",
    "Star Leader Penny":"https://play.pokemonshowdown.com/sprites/trainers/penny.png",
    "Pokemon Trainer Paul":"https://cdn.discordapp.com/attachments/1102579499989745764/1126767577742458930/Paul.png",
    "Tower Tycoon Palmer":"https://cdn.discordapp.com/attachments/1102579499989745764/1140296432981639168/PalmerPlatinum.gif",
    "Team Star Ortega":"https://play.pokemonshowdown.com/sprites/trainers/ortega.png",
    "Gym Leader Opal":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759237054382100/Opal.png",
    "Gym Leader Olympia":"https://play.pokemonshowdown.com/sprites/trainers/olympia.png",
    "Elite Four Olivia":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759236274237510/Olivia.png",
    "Professor Oak":"https://play.pokemonshowdown.com/sprites/trainers/oak.png",
    "Gym Leader Norman":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759235586371644/Norman.png",
    "Factory Head Noland":"https://play.pokemonshowdown.com/sprites/trainers/noland.png",
    "Battle Chatelaine Nita":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759235032715334/Nita.png",
    "Gym Leader Nessa":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759234751709254/Nessa.png",
    "Paldea Champion Nemona":"https://play.pokemonshowdown.com/sprites/trainers/nemona-v.png",
    "Trial Captain Nanu":"https://cdn.discordapp.com/attachments/1102579499989745764/1126759234122563654/Nanu.png",
    "Natural Harmonia Gropius":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712947134177370/N.png",
    "Galar Champion Mustard":"https://play.pokemonshowdown.com/sprites/trainers/mustard-master.png",
    "Gym Leader Morty":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712946685394964/Morty.png",
    "Elite Four Molayne":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712946479865886/Molayne.png",
    "Pokemon Trainer Mira":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712946203045898/Mira.png",
    "Pokemon Trainer Mina":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712945942994965/Mina.png",
    "Gym Leader Milo":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712945636814919/Milo.png",
    "Gym Leader Maylene":"https://cdn.discordapp.com/attachments/1102579499989745764/1126712944982503524/Maylene.png",
    "Fusion Creator Darwin":"https://play.pokemonshowdown.com/sprites/trainers/unknown.png",
    "Pokemon Trainer May":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587242423992350/May.png",
    "Magma Leader Maxie":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587242084237423/Maxie.png",
    "Aqua Admin Matt":"https://play.pokemonshowdown.com/sprites/trainers/matt.png",
    "Elite Four Marshal":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587241442512916/Marshal.png",
    "Galactic Commander Mars":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587241077620796/Mars.png",
    "Gym Leader Marnie":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587240830140496/Marnie.png",
    "Gym Leader Marlon":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587240557514792/Marlon.png",
    "Pokemon Trainer Marley":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587240200994847/Marley.png",
    "Elite Four Malva":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587239886426205/Malva.png",
    "Trial Captain Mallow":"https://cdn.discordapp.com/attachments/1102579499989745764/1120587239634780170/Mallow.png",
    "Flare Boss Lysandre":"https://play.pokemonshowdown.com/sprites/trainers/lysandre.png",
    "Aether President Lusamine":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578905494003773/Lusamine.png",
    "Pike Queen Lucy":"https://play.pokemonshowdown.com/sprites/trainers/lucy.png",
    "Elite Four Lucian":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578905003274261/Lucian.png",
    "Champion Lorelei(Hail)":"https://cdn.discordapp.com/attachments/1102579499989745764/1138762073552195594/1691572419426.png",
    "Champion Lorelei(Rain)":"https://cdn.discordapp.com/attachments/1102579499989745764/1138762073552195594/1691572419426.png",
    "Elite Four Lorelei":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578904743223387/Lorelei.png",
    "Gym Leader Liza":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578904478986280/Liza.png",
    "Trial Captain Lillie":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578904252489798/Lillie.png",
    "Galar Champion Leon":"https://play.pokemonshowdown.com/sprites/trainers/leon.png",
    "Gym Leader Lenora":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578903749177436/Lenora.png",
    "Elite Four Larry":"https://cdn.discordapp.com/attachments/1102579499989745764/1120578903463960647/Larry.png",
    "Kanto Champion Lance":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571178516492379/Lance.png",
    "Trial Captain Lana":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571178222887003/Lana.png",
    "Professor Kukui":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571178013180055/Kukui.png",
    "Gym Leader Korrina":"https://cdn.discordapp.com/attachments/1102579499989745764/1120571177732153495/Korrina.png",
    "Elite Four Koga":"https://cdn.discordapp.com/attachments/1102579499989745764/1140291025651372154/KogaHGSS.gif",
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
    "Unova Champion Iris":"https://cdn.discordapp.com/attachments/1102579499989745764/1140295347105714298/Champion_Iris.gif",
    "Gym Leader Iono":"https://cdn.discordapp.com/attachments/1102579499989745764/1115999803806072852/Iono.png",
    "Elite Four Bruno":random.choice(["https://cdn.discordapp.com/attachments/1102579499989745764/1115998773781475368/Bruno.png","https://cdn.discordapp.com/attachments/1102579499989745764/1140293031187206195/BrunoHGSS.gif"]),
    "Pokemon Trainer Hop":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283056359866469/Hop.png",
    "Pokemon Trainer Hau":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283056133382204/Hau.png",
    "Elite Four Hassel":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283055927865435/Hassel.png",
    "Island Kahuna Hapu":"https://cdn.discordapp.com/attachments/1102579499989745764/1112283055705554994/Hapu.png",
    "Elite Four Hala":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258206861889566/Hala.png",
    "Skull Leader Guzma":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258206614438008/Guzma.png",
    "Gym Leader Grusha":"https://play.pokemonshowdown.com/sprites/trainers/grusha.png",
    "Elite Four Grimsley":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258205993668628/Grimsley.png",
    "Arena Tycoon Greta":"https://cdn.discordapp.com/attachments/1102579499989745764/1112258205628776528/Greta.png",
    "Gym Leader Grant":"https://play.pokemonshowdown.com/sprites/trainers/grant.png",
    "Gym Leader Gordie":"https://play.pokemonshowdown.com/sprites/trainers/gordie.png",
    "Pokemon Trainer Gladion":"https://cdn.discordapp.com/attachments/1102579499989745764/1112020338079973416/Gladion.png",
    "Elite Four Glacia":"https://play.pokemonshowdown.com/sprites/trainers/glacia.png",
    "Rocket Boss Giovanni":"https://cdn.discordapp.com/attachments/1102579499989745764/1140297675254796348/GiovanniHGSS.gif",
    "Plasma Leader Ghetsis":random.choice(["https://play.pokemonshowdown.com/sprites/trainers/ghetsis.png","https://play.pokemonshowdown.com/sprites/trainers/ghetsis-gen5bw.png"]),
    "Paldea Champion Geeta":"https://play.pokemonshowdown.com/sprites/trainers/geeta.png",
    "Researcher Gary Oak":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226698514492/Gary2.png",
    "Gym Leader Gardenia":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226476208159/Gardenia.png",
    "Elite Four Flint":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226245517382/Flint.png",
    "Gym Leader Flannery":"https://cdn.discordapp.com/attachments/1102579499989745764/1111943226027425904/Flannery.png",
    "Gym Leader Fantina":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897876314996816/Fantina.png",
    "Gym Leader Falkner":"https://cdn.discordapp.com/attachments/1102579499989745764/1140291027006136340/FalknerHGSSSprite.gif",
    "Aether Foundation Faba":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897875903942706/Faba.png",
    "Battle Chatelaine Evelyn":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897875702628362/Evelyn.png",
    "Subway Boss Emmet":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897875484520468/Emmet.png",
    "Gym Leader Elesa":"https://cdn.discordapp.com/attachments/1102579499989745764/1111897704201736202/Elesa1.png",
    "Pokemon Trainer Drew":"https://cdn.discordapp.com/attachments/1102579499989745764/1111163495371771934/Drew.png",
    "Gym Leader Drayden":"https://cdn.discordapp.com/attachments/1102579499989745764/1140295347848093776/DraydenBWsprite.gif",
    "Elite Four Drasna":"https://cdn.discordapp.com/attachments/1102579499989745764/1111163494876860476/Drasna.png",
    "Elite Four Drake":"https://cdn.discordapp.com/attachments/1102579499989745764/1111163494662942791/Drake.png",
    "Kalos Champion Diantha":"https://play.pokemonshowdown.com/sprites/trainers/diantha.png",
    "Castle Velvet Darach":"https://cdn.discordapp.com/attachments/1102579499989745764/1140296433464004698/KochraneCattleyaPlatinum.gif",
    "Battle Arcade Dahlia":"https://cdn.discordapp.com/attachments/1102579499989745764/1140296433858256977/Dahlia.gif",
    "Galactic Leader Cyrus":"https://cdn.discordapp.com/attachments/1102579499989745764/1140297304201506906/CyrusPlatinum.gif",
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
    "Elite Four Caitlin":"https://cdn.discordapp.com/attachments/1102579499989745764/1140296434256707695/Caitlin.gif",
    "Gym Leader Byron":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114704451010661/Byron.png",
    "Gym Leader Burgh":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114704144834662/Burgh.png",
    "Gym Leader Bugsy":"https://cdn.discordapp.com/attachments/1102579499989745764/1140292531888869449/BugsyHGSSSprite.gif",
    "Gym Leader Brycen":"https://cdn.discordapp.com/attachments/1102579499989745764/1111114703641522226/Brycen.png",
    "Gym Leader Brawly":"https://cdn.discordapp.com/attachments/1102579499989745764/1111112061213216788/Brawly.png",
    "Gym Leader Brassius":"https://cdn.discordapp.com/attachments/1102579499989745764/1111112060919632012/Brassius.png",
    "Pyramid King Brandon":"https://cdn.discordapp.com/attachments/1102579499989745764/1111112060684738601/Brandon.png",
    "Aqua Leader Archie":"https://cdn.discordapp.com/attachments/1102579499989745764/1109681004983107714/Archie.png",
    "Sinnoh Champion Cynthia":random.choice(["https://cdn.discordapp.com/attachments/1102579499989745764/1140294182708195328/CynthiaPlatinum.gif","https://cdn.discordapp.com/attachments/1102579499989745764/1140294183165378670/Champion_Cynthia.gif"]),
    "Gym Leader Brock":"https://cdn.discordapp.com/attachments/1102579499989745764/1140289187719950386/Brock_gameHGSS.gif",
    "Pokemon Breeder Brock":"https://cdn.discordapp.com/attachments/1102579499989745764/1140289187719950386/Brock_gameHGSS.gif",
    "Gym Leader Misty":"https://cdn.discordapp.com/attachments/1102579499989745764/1140289438115696690/MistyHGSS.gif",
    "Tomboyish Mermaid Misty":"https://cdn.discordapp.com/attachments/1102579499989745764/1140289438115696690/MistyHGSS.gif",
    "Gym Leader Lt.Surge":"https://cdn.discordapp.com/attachments/1102579499989745764/1140289772473036902/Lt._SurgeHGSS.gif",
    "Gym Leader Erika":"https://cdn.discordapp.com/attachments/1102579499989745764/1140289772837949611/ErikaHGSS.gif",
    "Gym Leader Sabrina":"https://cdn.discordapp.com/attachments/1102579499989745764/1140291025223565322/SabrinaHGSS.gif",
    "Gym Leader Blaine":"https://cdn.discordapp.com/attachments/1102579499989745764/1140291026142118009/BlaineHGSS.gif",
    "Gym Leader Blue":"https://cdn.discordapp.com/attachments/1102579499989745764/1140292117814579401/BlueHGSS.gif",
    "Hoenn Champion Steven":"https://cdn.discordapp.com/attachments/1102579499989745764/1140288579571036210/StevenB2W2sprite.gif",
    "Elite Four Aaron":"https://cdn.discordapp.com/attachments/1102579499989745764/1109598046653788231/Aaron.png",
    "Elite Four Acerola":"https://cdn.discordapp.com/attachments/1102579499989745764/1109598930997620938/Acerola.png",
    "Elite Four Agatha":"https://cdn.discordapp.com/attachments/1102579499989745764/1109599848900083863/Agatha.png",
    "Pokemon Trainer Alain":"https://play.pokemonshowdown.com/sprites/trainers/alain.png",
    "Unova Champion Alder":"https://cdn.discordapp.com/attachments/1102579499989745764/1140295347441250427/AlderBWsprite.gif",
    "Gym Leader Allister":"https://cdn.discordapp.com/attachments/1102579499989745764/1109611947713892362/Allister.png",
    "Salon Maiden Anabel":random.choice(["https://cdn.discordapp.com/attachments/1102579499989745764/1109681004442046505/Anabel.png","https://play.pokemonshowdown.com/sprites/trainers/anabel.png"]),
    "Rocket Admin Archer":"https://cdn.discordapp.com/attachments/1102579499989745764/1109681004727246958/Archer.png",
    "Rocket Admin Ariana":"https://cdn.discordapp.com/attachments/1102579499989745764/1136897549467394078/Spr_HGSS_Ariana.png",
    "Pokemon Trainer Barry":"https://media.tenor.com/M0jtKgsWg-4AAAAi/barry-dance.gif",
    "Gym Leader Bea":"https://cdn.discordapp.com/attachments/1102579499989745764/1111029602874294355/Bea.png",
    "Gym Leader Bede":random.choice(["https://play.pokemonshowdown.com/sprites/trainers/bede.png","https://play.pokemonshowdown.com/sprites/trainers/bede-leader.png"]),
    "Boss Trainer Benga":"https://cdn.discordapp.com/attachments/1102579499989745764/1111031362300952747/Benga.png",
    "Elite Four Bertha":"https://cdn.discordapp.com/attachments/1102579499989745764/1111037750297243848/Bertha.png"
    }
    if name in spritelist:
        sprite=spritelist[name]
    else:
        sprite="https://play.pokemonshowdown.com/sprites/trainers/unknown.png"
    return sprite      