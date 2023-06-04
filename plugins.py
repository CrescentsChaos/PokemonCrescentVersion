import random
import discord
import sqlite3
from pokemon import *
from movelist import *
from trainers import *
from pokemon import calcst
megastones=["Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Ampharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite"]
async def entryeff(ctx,x,y,tr1,tr2,field,turn):
    entry=discord.Embed(title=f"Entry Effects:")
    if x.item=="Blue Orb" and "Primal" not in x.name and x.name=="Kyogre":
        em=discord.Embed(title="Primal Reversion:",description=f"{x.name}'s Primal Reversion! It reverted to its primal form!")
        x.sprite=x.sprite.replace(".gif","-primal.gif")
        x.name="Primal Kyogre"
        per=x.hp/x.maxhp
        x.ability="Primordial Sea"
        x.weight=947.99
        x.hp=100
        x.atk=150
        x.defense=90
        x.spatk=180
        x.spdef=160
        x.speed=90
        calcst(x)
        x.hp=x.maxhp*per
        em.set_image(url=x.sprite)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1108653012680982568/Blue_Orb.png")
        await ctx.send(embed=em)
    if x.item=="Red Orb" and "Primal" not in x.name and x.name=="Groudon":
        em=discord.Embed(title="Primal Reversion:",description=f"{x.name}'s Primal Reversion! It reverted to its primal form!")
        x.sprite=x.sprite.replace(".gif","-primal.gif")
        x.name="Primal Groudon"
        per=x.hp/x.maxhp
        x.ability="Desolate Land"
        x.weight=2203.96
        x.hp=100
        x.atk=180
        x.defense=160
        x.spatk=150
        x.spdef=90
        x.speed=90
        calcst(x)
        x.hp=x.maxhp*per
        em.set_image(url=x.sprite)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1109011460601954364/Red_Orb.png")
        await ctx.send(embed=em)
    #Comatose
    if x.ability=="Comatose":
        entry.add_field(name=f"{x.nickname}'s Comatose!",value=f"{x.nickname} is in a drowsy state.")
        x.status="Drowsy"
    #Flower Gift
    elif x.ability=="Flower Gift" and field.weather in ["Sunny","Desolate Land"] and "Cherrim" in x.name and x.sprite!="https://play.pokemonshowdown.com/sprites/ani/cherrim-sunshine.gif":
        entry.add_field(name=f"{x.nickname}'s Flower Gift!",value=f"{x.nickname} is reacting and absorbing sunlight!")     
        x.sprite="https://play.pokemonshowdown.com/sprites/ani/cherrim-sunshine.gif"
    elif x.ability=="Illusion":
        x.name=tr1.pokemons[-1].name
        x.nickname=tr1.pokemons[-1].nickname
        x.sprite=tr1.pokemons[-1].sprite
    elif x.ability=="Pressure" and y.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail"]:
        entry.add_field(name=f"{x.nickname}'s Pressure!",value=f"{x.nickname} is exerting its pressure!")  
    elif x.ability=="Supreme Overlord" and len(tr1.pokemons)!=0:
        entry.add_field(name=f"{x.nickname}'s Supreme Overlord!",value=f"{x.nickname} gained strength from the fallen!")  
    elif x.ability=="Frisk" and (y.item!="None" or "Used" not in y.item):
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
        x.color=y.color
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
    elif (x.ability == "Sand Stream" or (x.ability=="Forecast" and x.item=="Smooth Rock")) and field.weather not in ["Sandstorm","Primordial Sea","Desolate Land"]:
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
    elif x.ability=="Drought" and field.weather not in ["Sunny","Primordial Sea","Desolate Land"]:
        entry.add_field(name=f"{x.nickname}'s Drought!",value=f"️{x.nickname} intensified the sun's rays!")
        field.weather="Sunny"  
        field.sunturn=turn
        field.sunend(x,y)
    elif x.ability=="Orichalcum Pulse" and field.weather not in ["Sunny","Primordial Sea","Desolate Land"]:
        entry.add_field(name=f"{x.nickname}'s Orichalcum Pulse!",value=f"️{x.nickname} turned the sunlight harsh, sending its ancient pulse into a frenzy!")
        field.weather="Sunny"  
        field.sunturn=turn
        field.sunend(x,y)    
    elif x.ability=="Drizzle" and field.weather not in ["Rainy","Primordial Sea","Desolate Land"]:
        entry.add_field(name=f"{x.nickname}'s Drizzle!",value=f"️{x.nickname} made it rain!")
        field.weather="Rainy"  
        field.rainturn=turn
        field.rainend(x,y)     
    elif x.ability=="Snow Warning" and field.weather not in ["Snowstorm","Primordial Sea","Desolate Land"]:
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
        #speedchange(x,y,-0.5)        
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
    await ctx.send(embed=entry)    
async def maxendturn(x,turn):
    if x.dmax is True:
       x.maxend=turn+3         
async def maxtrans(ctx,x,tr1,turn):
    x.dmax=True
    tr1.canmax=False
    em=discord.Embed(title=f"{tr1.name} dynamaxed {x.nickname}!")   
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1102579499989745764/1106824399983751248/Dynamax.png")
    em.set_image(url=x.sprite)
    await maxendturn(x,turn)
    x.hp*=2
    x.maxhp*=2
    return x,em
async def teratrans(ctx,x,tr1):
    x.teraType=x.tera
    tr1.cantera=False
    em=discord.Embed(title="Terastallization:",description=f"{tr1.name} terastallized {x.nickname} into {x.teraType}-Type!")   
    em.set_thumbnail(url=f"https://play.pokemonshowdown.com/sprites/types/Tera{x.teraType}.png")
    em.set_image(url=x.sprite)
    return x,em
async def prebuff(ctx,x,y,tr1,tr2,turn,field):
    atkbuff=1
    defbuff=1
    spatkbuff=1
    spdefbuff=1
    speedbuff=1   
    pre=discord.Embed(title="Pre-move buffs:")
    if turn==x.maxend:
        x.hp/=2
        x.maxhp/=2
        await ctx.send(f"{x.nickname} returned to it's normal state.")
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
    if x.ability=="Flower Gift" and field.weather in ["Sunny","Desolate Land"]:
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
    if field.weather in ["Sunny","Desolate Land"] and x.ability=="Orichalcum Pulse":
        atkbuff*=1.34
    if field.terrain=="Electric" and x.ability=="Hadron Engine":
        spatkbuff*=1.34
    if ("Protosynthesis" in x.ability and (field.weather in ["Sunny","Desolate Land"] or x.item=="Booster Energy")) or x.ability in ["Protosynthesis [Attack]","Protosynthesis [Sp. Attack]","Protosynthesis [Defense]","Protosynthesis [Sp. Defense]","Protosynthesis [Speed]"]:
        if field.weather not in ["Sunny","Desolate Land"] and "[" not in x.ability:
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
    if field.weather in ["Rainy","Primordial Sea"] and x.ability=="Swift Swim" and "Cloud Nine" not in (x.ability,y.ability):
        speedbuff*=2
    if field.weather in ["Sunny","Desolate Land"] and x.ability=="Chlorophyll" and "Cloud Nine" not in (x.ability,y.ability):
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
    
async def action(bot,ctx,tr1,tr2,x,y):      
    if tr1.ai==True:
        if x.item in megastones and tr1.canmega==True:
            return 6
        elif x.tera!="???" and x.tera not in (x.primaryType,x.secondaryType) and tr1.cantera==True:
            return 9
        else:
            return random.choices([1,2],weights=[10,1],k=1)[0]
    if tr1.ai==False:
        inaction=None
        while True:
            des="#1 💥 Fight\n#2 🔁 Switch\n#3 🚫 Forfeit\n"
            if tr1.canmega==True and x.dmax==False and x.item in megastones and x.teraType=="???":
                des+=f"#6 <:megaevolve:1104646688951500850> Mega Evolve\n"  
            if x.dmax==False and x.item=="Ultranecrozium-Z" and "Ultra" not in x.name:
                des+=f"#7 Ultra Burst\n"  
            if tr1.canmax==True and x.dmax==False and x.item not in megastones and x.teraType=="???":
                des+="#8 <:dynamax:1104646304904257647> Dynamax/Gigantamax\n"     
            if tr1.cantera==True and x.dmax==False and x.item not in megastones and x.teraType=="???":
                des+=f"#9 <:tera:1104647530119176272> Terastallize ({x.tera})\n"
            em=discord.Embed(title=f"{tr1.name}, what do you wanna do?", description=des)
            if tr2.ai==True:
                await ctx.send(embed=em)
                while True:
                    inaction=await bot.wait_for('message')
                    if inaction.author==ctx.author:
                        break
            if tr2.ai==False:
                await tr1.member.send(embed=em)
                def check(message):
                    return isinstance(message.channel,discord.DMChannel) and message.author==tr1.member
                inaction=await bot.wait_for('message',check=check)
            try:
                inaction=int(inaction.content)
            except:
                inaction=None
            if inaction!=None:
                break
        return inaction        
    
async def score(ctx,x,y,tr1,tr2,turn,bg):
    hpbar="<:HP:1107296292243255356>"+"<:GREY:1107331848360689747>"*10+"<:END:1107296362988580907>"
    if "Frostbite" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:FBT:1107340620097404948>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if "Frozen" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:FZN:1107340597980827668>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if x.status in ["Sleep","Drowsy"]:
        hpbar="<:HP:1107296292243255356>"+"<:SLP:1107340641882603601>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if "Paralyzed" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:YELLOW:1107331825929556111>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if "Burned" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:BRN:1107340533518573671>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"        
    if "Poisoned" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:PSN:1107340504762437723>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if x.status=="Alive":
        if 0.6<(x.hp/x.maxhp)<=1:
            hpbar="<:HP:1107296292243255356>"+"<:GREEN:1107296335780139113>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
        if 0.3<(x.hp/x.maxhp)<=0.6:
            hpbar="<:HP:1107296292243255356>"+"<:YELLOW:1107331825929556111>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"       
        if 0<(x.hp/x.maxhp)<=0.3:
            hpbar="<:HP:1107296292243255356>"+"<:RED:1107331787480379543>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"                 
    em=discord.Embed(title=f"{tr1.name}:", description=f"**{x.nickname}** Lv. {x.level}\n**HP:** {round(x.hp)}/{x.maxhp} ({round((x.hp/x.maxhp)*100,2)}%)",color=bg)
    em.add_field(name="HP Bar:",value=hpbar)
    em.set_thumbnail(url=tr1.sprite)
    em.set_image(url=x.sprite)
    await ctx.send(embed=em)
    
async def advscore(ctx,x,y,tr1,tr2,turn,bg):
    hpbar="<:HP:1107296292243255356>"+"<:GREY:1107331848360689747>"*10+"<:END:1107296362988580907>"
    if "Frostbite" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:FBT:1107340620097404948>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if "Frozen" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:FZN:1107340597980827668>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if x.status in ["Sleep","Drowsy"]:
        hpbar="<:HP:1107296292243255356>"+"<:SLP:1107340641882603601>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if "Paralyzed" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:YELLOW:1107331825929556111>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if "Burned" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:BRN:1107340533518573671>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if "Poisoned" in x.status:
        hpbar="<:HP:1107296292243255356>"+"<:PSN:1107340504762437723>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
    if x.status=="Alive":
        if 0.6<(x.hp/x.maxhp)<=1:
            hpbar="<:HP:1107296292243255356>"+"<:GREEN:1107296335780139113>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"
        if 0.3<(x.hp/x.maxhp)<=0.6:
            hpbar="<:HP:1107296292243255356>"+"<:YELLOW:1107331825929556111>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"       
        if 0<(x.hp/x.maxhp)<=0.3:
            hpbar="<:HP:1107296292243255356>"+"<:RED:1107331787480379543>"*int((x.hp/x.maxhp)*10)+"<:GREY:1107331848360689747>"*(10-int((x.hp/x.maxhp)*10))+"<:END:1107296362988580907>"                 
    em=discord.Embed(title=f"{tr1.name}:", description=f"**{x.nickname}** Lv. {x.level}\n**HP:** {round(x.hp)}/{x.maxhp} ({round((x.hp/x.maxhp)*100,2)}%)\n**Status:** {x.status}\n**Ability:**{x.ability}\n**Held Item:**{x.item}\n**Attack:** {round(x.atk)}({x.atkb})\n**Defense:** {round(x.defense)}({x.defb})\n**Sp. Atk:** {round(x.spatk)}({x.spatkb})\n**Sp. Def:** {round(x.spdef)}({x.spdefb})\n**Speed:** {round(x.speed)}({x.speedb})",color=bg)
    em.add_field(name="HP Bar:",value=hpbar)
    em.set_thumbnail(url=tr1.sprite)
    em.set_image(url=x.sprite)
    if tr2.ai==False:
        await tr1.member.send(embed=em)
    if tr2.ai==True:
        await ctx.send(embed=em)
        
async def movelist(ctx,x,tr1,tr2):
    move=""
    if x.dmax==False:
        for i in range(len(x.moves)):
            move+=f"{i+1}. {x.moves[i]}\n"
    elif x.dmax==True:
        for i in range(len(x.maxmoves)):
            move+=f"{i+1}. {x.maxmoves[i]}\n"  
    em=discord.Embed(title=f"What will {x.nickname} use?:",description=move,color=0xff0000)   
    if tr2.ai==False:            
        await tr1.member.send(embed=em)
    if tr2.ai==True:
        await ctx.send(embed=em)
       
async def fchoice(ctx,bot,x,y,tr1,tr2,field):
    if tr1.ai==True:
        return random.choice(x.moves)
    if tr1.ai==False:
        await movelist(ctx,x,tr1,tr2)    
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
        if x.item=="Gyaradosite":
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
        if x.item=="Venusaurite":
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
        if x.item=="Charizardite X":
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
        if x.item=="Charizardite Y":
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
        if x.item=="Blastoisinite":
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
        if x.item=="Beedrillite":
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
        if x.item=="Pidgeotite":
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
        if x.item=="Alakazite":
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
        if x.item=="Slowbronite":
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
        if x.item=="Gengarite":
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
        if x.item=="Kangaskhanite":
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
        if x.item=="Pinsirite":
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
        if x.item=="Aerodactylite":
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
        if x.item=="Mewtwonite X":
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
        if x.item=="Mewtwonite Y":
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
        dt=discord.Embed(title=f"{x.nickname} fainted!")
        dt.set_image(url=x.sprite)
        if y.ability=="Battle Bond" and "Ash" not in y.name:
            per=y.hp/y.maxhp
            y.weight=88.18
            y.sprite="http://play.pokemonshowdown.com/sprites/ani/greninja-ash.gif"
            y.hp=72
            y.atk=145
            y.defense=67
            y.spatk=153
            y.spdef=71
            y.speed=132
            calcst(y)
            y.hp=y.maxhp*per
        tr1.faintedmon.append(x)
        tr1.pokemons.remove(x)
        if len(tr1.pokemons)==0:
            await ctx.send(embed=dt)
        if len(tr1.pokemons)!=0 and len(tr2.pokemons)!=0:
            await ctx.send(embed=dt)
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
            if x.hp<=0:
                await faint(ctx,bot,x,y,tr1,tr2,field,turn)                
    return x                      
        
async def winner(ctx,tr1,tr2):
    winner=None
    if len(tr1.pokemons)==0:
        winner=tr2
    elif len(tr2.pokemons)==0:
        winner=tr1
    em=discord.Embed(title=f"{winner.name} won the battle!")
    em.set_image(url=tr1.sprite)
    await ctx.send(embed=em)
    
async def effects(ctx,x,y,tr1,turn):
    pass
async def weather(ctx,field,bg):
    em=discord.Embed(title="Weather Update!",color=bg)
    if field.weather =="Extreme Sunlight":
        em.add_field(name="Weather:",value=f"The sunlight is extremely harsh.")
    if field.weather =="Heavy Rain":
        em.add_field(name="Weather:",value=f"Heavy rain continues to fall.")
    if field.weather =="Snowstorm":
        em.add_field(name="Weather:",value=f"Snow continues to fall.")
    if field.weather =="Rainy":
        em.add_field(name="Weather:",value=f"Rain continues to fall.")
    if field.weather =="Sandstorm":
        em.add_field(name="Weather:",value=f"The sandstorm is raging!")
    if field.weather=="Hail":
        em.add_field(name="Weather:",value=f"Hail continues to fall.")
    if field.weather=="Sunny":
        em.add_field(name="Weather:",value=f"The sunlight is strong.")
    if field.weather not in ["Normal","Cloudy","Clear"]:
        await ctx.send(embed=em)
        
async def switch(ctx,bot,x,y,tr1,tr2,field,turn):
    if x.ability in ["Protean","Libero"]:
        if "Kecleon" in x.name:
            x.primaryType,x.secondaryType="Normal","Ghost"
        if "Meowscarada" in x.name:
            x.primaryType,x.secondaryType="Grass","Dark"
        if "Cinderace" in x.name:
            x.primaryType="Fire"
        if "Greninja" in x.name:
            x.primaryType,x.secondaryType="Water","Dark"
    if "Disguise" in x.ability:
        x.ability="Disguise"
        x.sprite="sprites/Mimikyu.png"
    if "Quark Drive" in x.ability:
        x.ability="Quark Drive"
    if "Protosynthesis" in x.ability:
        x.ability="Protosynthesis"
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
        pklist+=f"#{n} {i.name} {i.hp}/{i.maxhp}\n"
    em=discord.Embed(title="Choose your pokémon!",description=pklist)
    if tr1.ai==True:
        while new=="" or new==x:
            new=random.choice(tr1.pokemons)
        await withdraweff(ctx,x,tr1,y)
        em=discord.Embed(title=f"{tr1.name} sent out {new.nickname}!")
        em.set_thumbnail(url=tr1.sprite)
        em.set_image(url=new.sprite) 
        await ctx.send(embed=em)
        await entryeff(ctx,new,y,tr1,tr2,field,turn)
        return new
    elif tr2.ai==True and tr1.ai==False:
        while new=="" or new==x:
            await ctx.send(embed=em)  
            num=await bot.wait_for('message')
            if num.author==ctx.author:
                num=int(num.content)
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
async def withdraweff(ctx,x,tr1,y):
    em=discord.Embed(title="Withdraw Effect:")
    if x.ability=="Zero to Hero" and "Hero" not in x.name and x.hp>0 and x.dmax==False:
        em.add_field(name=f"{x.name}'s Zero to Hero!",value=f"{x.name} underwent a heroic transformation!")
        x.name="Hero Palafin"
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/palafin-hero.gif"
        per=x.hp/x.maxhp
        x.color=20
        x.weight=214.73
        x.hp=100
        x.atk=160
        x.defense=97
        x.spatk=106
        x.spdef=87
        x.speed=100
        calcst(x)
        x.hp=x.maxhp*per
    if x.ability=="Illusion":
        x.name=trainer.pokemons[len(trainer.pokemons)-1].name
        x.sprite=trainer.pokemons[len(trainer.pokemons)-1].sprite      
    if x.ability=="Natural Cure" and (x.status!="Alive" and x.status!="Fainted"):
        em.add_field(name=f"{x.name}'s Natural Cure!",value=f"{x.name}'s status condition was cured!")
        x.status="Alive"
    if x.ability=="Regenerator" and 0<x.hp<x.maxhp and x.status!="Fainted":
        em.add_field(name=f"{x.name}'s Regenerator!",value=f"{x.name} regenerated a bit of it's health!")
        if x.hp<=(x.maxhp/3):
            x.hp+=round(x.maxhp/3)
        elif x.hp>(x.maxhp/3):
            x.hp=x.maxhp    
async def teambuild(team):
    new=[]
    while len(new)!=6:
        mon=random.choice(team)
        if mon not in new:
            new.append(mon)
    return new            
async def gamemonvert(m):
    dt=sqlite3.connect("pokemondata.db")
    cx=dt.cursor()
    print(m[0])
    cx.execute(f"select * from 'wild' where name='{m[0]}' ")
    n=cx.fetchall()[0]
    moves=m[14]
    ability=m[8]
    if ability=="None":
        ability=n[11]
    if moves=="A,B,C,D":
        moves=n[10]
    p=Pokemon(name=m[0],hpev=m[2],atkev=m[3],defev=m[4],spatkev=m[5],spdefev=m[6],speedev=m[7],ability=ability,nature=m[9],shiny=m[10],item=m[11],gender=m[12],tera=m[13],moves=moves,maxiv="Yes",primaryType=n[1],secondaryType=n[2],level=n[3],hp=n[4],atk=n[5],defense=n[6],spatk=n[7],spdef=n[8],speed=n[9],sprite=n[12])
    return p            
async def gameteam(ctx,num=0):
    players=["Gym Leader Brock","Gym Leader Misty","Gym Leader Lt.Surge","Gym Leader Erika","Gym Leader Sabrina","Gym Leader Blaine","Gym Leader Blue","Gym Leader Allister","Elite Four Agatha","Elite Four Aaron","Elite Four Acerola","Sinnoh Champion Cynthia","Hoenn Champion Steven","Pokemon Trainer Alain","Unova Champion Alder","Salon Maiden Anabel","Rocket Admin Archer","Rocket Admin Ariana","Aqua Leader Archie","Pokemon Trainer Barry","Gym Leader Bede","Gym Leader Bea","Boss Trainer Benga","Elite Four Bertha","Pyramid King Brandon","Gym Leader Brassius","Gym Leader Brawly","Gym Leader Brycen","Gym Leader Bugsy","Gym Leader Burgh","Gym Leader Byron","Elite Four Caitlin","Gym Leader Candice","Pokemon Trainer Cheren","Gym Leader Chuck","Gym Leader Clair","Gym Leader Clay","Gym Leader Clemont","Plasma Admin Colress""Plasma Admin Colress","Pokemon Trainer Conway","Magma Admin Courtney","Gym Leader Crasher Wake","Galactic Leader Cyrus","Battle Arcade Dahlia","Castle Velvet Darach","Kalos Champion Diantha","Elite Four Drake","Elite Four Drasna","Gym Leader Drayden","Pokemon Trainer Drew","Gym Leader Elesa","Subway Boss Emmet","Battle Chatelaine Evelyn","Aether Foundation Faba","Gym Leader Falkner","Gym Leader Fantina","Gym Leader Flannery","Elite Four Flint","Gym Leader Gardenia","Researcher Gary Oak","Paldea Champion Geeta","Plasma Leader Ghetsis","Rocket Boss Giovanni","Elite Four Glacia","Pokemon Trainer Gladion","Gym Leader Gordie","Gym Leader Grant","Arena Tycoon Greta","Elite Four Grimsley","Gym Leader Grusha","Skull Leader Guzma","Elite Four Hala","Island Kahuna Hapu","Elite Four Hassel","Pokemon Trainer Hop"]
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
    tr1=Trainer(name,mons,"Unknown",sprite=sprite,ai=True)
    return tr1
async def trsprite(name):
    spritelist={
    "Pokemon Trainer Hop","https://cdn.discordapp.com/attachments/1102579499989745764/1112283056359866469/Hop.png",
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
    "Rocket Admin Ariana":"https://cdn.discordapp.com/attachments/1102579499989745764/1109860318064160859/20230521_210826.png",
    "Pokemon Trainer Barry":"https://media.tenor.com/M0jtKgsWg-4AAAAi/barry-dance.gif",
    "Gym Leader Bea":"https://cdn.discordapp.com/attachments/1102579499989745764/1111029602874294355/Bea.png",
    "Gym Leader Bede":"https://cdn.discordapp.com/attachments/1102579499989745764/1111030432801243176/Bede.png",
    "Boss Trainer Benga":"https://cdn.discordapp.com/attachments/1102579499989745764/1111031362300952747/Benga.png",
    "Elite Four Bertha":"https://cdn.discordapp.com/attachments/1102579499989745764/1111037750297243848/Bertha.png"
    }
    sprite=spritelist[name]
    return sprite      