import discord
from pokemon import *
from plugins import *
from moves import *

async def stance(ctx,x,y,turn,field,used,em):    
    if used not in typemoves.statusmove and x.ability=="Stance Change" and x.sword!=True:
        x.shield=False
        x.sword=True
        em.add_field(name=f"{x.nickname}'s Stance Change!",value="Aegislash changed to it's blade forme.")
        x.name="Blade Aegislash"
        per=x.hp/x.maxhp
        x.weight=116.84
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/aegislash-blade.gif"
        if x.shiny=="Yes":
            x.sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/aegislash-blade.gif"
        x.hp=60
        x.atk=140
        x.defense=50
        x.spatk=140
        x.spdef=50
        x.speed=60
        calcst(x)
        x.hp=x.maxhp*per
    if used in typemoves.statusmove and x.ability=="Stance Change" and x.shield!=True:
        x.shield=True
        x.sword=False
        em.add_field(name=f"{x.nickname}'s Stance Change!",value="Aegislash changed to it's shield forme.")
        x.name="Shield Aegislash"
        per=x.hp/x.maxhp
        x.hp=60
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/aegislash.gif"
        if x.shiny=="Yes":
            x.sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/aegislash.gif"
        x.atk=50
        x.defense=140
        x.spatk=50
        x.spdef=140
        x.speed=60
        calcst(x)
        x.hp=x.maxhp*per
async def preattack(ctx,x,y,tr1,tr2,used,choice2,field,turn):
    if x.yawn is not True and x.yawn=="Sleep" and x.status=="Alive" and field.terrain!="Electric":
        x.status="Sleep"
        print(f"{x.name} fell asleep!")
        x.sleependturn=turn+random.randint(2,5)
        x.yawn=False
    if x.yawn is True:
        x.yawn="Sleep"
    if x.status!="Alive" and x.ability in ["Purifying Salt","Good as Gold"]:
        x.status="Alive"    
    if y.ability=="Stench" and x.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>90:
            x.flinched=True   
    if x.item in ["King's Rock","Razor Fang"]:
        ch=random.randint(1,100)
        if ch>90 and y.ability not in ["Inner Focus"]:
            if use in typemoves.premove and x.precharge==False:
                pass
            if use in typemoves.premove and x.precharge==True:
                y.flinched=True
            else:
                y.flinched=True
async def accheck(x,y,field,em):
    used=x.use
    accuracy=100
    eff=1
    if y.evasion<40:
        y.evasion=40
    if y.evasion>160:
        y.evasion=160
    if x.accuracy<40:
        x.accuracy=40
    if x.accuracy>160:
        x.accuracy=160
    if x.use in typemoves.acc30:
        accuracy=30
    if x.use in typemoves.acc95:
        accuracy=95
    if x.use in typemoves.acc80:
        accuracy=80
    if x.use in typemoves.acc50:
        accuracy=50
    if x.use in typemoves.acc70:
        accuracy=70
    if y.ability=="Wonder Skin" and x.use in typemoves.statusmove and x.use not in typemoves.buffmove:
        eff*=0.5  
    if field.weather in ["Sunny","Sandstorm","Extreme Sunlight"] and x.use in ["Blizzard","Thunder","Hurricane"]:
        accuracy=50
    if field.weather in ["Rainy","Heavy Rain"] and x.use in ["Thunder","Hurricane"]:
        accuracy=100
    if field.weather in ["Hail","Snowstorm"] and x.use=="Blizzard":
        accuracy=100
    if x.use in typemoves.acc90:
        accuracy=90
    if x.item=="Zoom Lens" and x.speed<y.speed:
        eff*=1.2
    if x.ability=="Victory Star":
        eff*=1.1
    if x.item=="Wide Lens":
        eff*=1.1
    if y.item in ["Bright Powder","Lax Incense"]:
        eff*=0.9
    if y.ability=="Tangled Feet" and y.confused==True and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and x.use not in typemoves.abilityigmoves:
        eff*=0.5
    if x.ability=="Hustle":
        eff*=0.8
    if y.ability not in ["Air Lock","Cloud Nine"] and x.ability not in ["Air Lock","Cloud Nine"] and field.weather=="Fog":
        eff*=0.6
    if y.ability=="Snow Cloak" and x.ability not in ["Air Lock","Cloud Nine"] and field.weather in ["Snowstorm","Hail"] and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and x.use not in typemoves.abilityigmoves:
        eff*=0.75
    if y.ability=="Sand Veil" and x.ability not in ["Air Lock","Cloud Nine"] and field.weather=="Sandstorm"and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and x.use not in typemoves.abilityigmoves:
        eff*=0.75
    if x.ability in ["Compound Eyes","Illuminate"]:
        eff*=1.3
    eff*=(y.evasion/100)
    eff*=(x.accuracy/100)
    accuracy=accuracy*eff
    if y.lockon==True:
        accuracy=100    
    if x.use in typemoves.noaccuracy:
        accuracy=100
    if y.use in ["Phantom Force","Shadow Force","Sky Attack","Bounce","Dig","Fly","Dive"] and y.precharge==True and used not in typemoves.buffmove and used!="None":
        accuracy=0
        if y.use in ["Bounce","Fly","Sky Attack"] and x.use in ["Thunder","Hurricane","Sky Uppercut"]:
            accuracy=1
        if "Dig" in y.use and x.use in ["Earthquake","Magnitude"]:
            accuracy=1
            x.atk*=2
    if x.use in typemoves.premove and x.precharge==False and "Power Herb" not in x.item:
        accuracy=100    
    if x.ability=="No Guard" or y.ability=="No Guard":
        accuracy=100            
    ch=random.randint(1, 100)
    if accuracy<100 and ch>accuracy and x.recharge==False:
        x.precharge=False
        em.add_field(name=f"Move:",value=f"{x.nickname} used {x.use}!\n{y.nickname} avoided the attack!")  
        used="None"
        if x.use in ["High Jump Kick","Axe Kick"]:
            a=b=c=r=al=1
            dmg=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)
            x.hp-=dmg/2
            em.add_field(name=f"Recoil:",value=f"{x.nickname} was hurt by recoil!") 
    return used                    
async def attack(ctx,bot,x,y,tr1,tr2,used,choice2,field,turn):
    c=await movecolor(used)
    em=discord.Embed(title=f"{tr1.name}:",color=c)    
    em.set_thumbnail(url=x.sprite) 
    me,they=x,y
    xhp=x.hp
    yhp=y.hp
    hit=1
    pp=1
    #Behind Substitute 
    subr=y
    if x.roost!=False:
        if x.roost=="T1":
            x.primaryType="Flying"
        if x.roost=="T2":
            x.secondaryType="Flying"
        if x.roost=="TR":
            x.teraType="Flying"
        x.roost=False
    if tr2.sub!="None" and used not in typemoves.bypass:
        yhp=tr2.sub.hp
    if used in typemoves.physicalmoves:
        x.atkcat="Physical"
    elif used not in (typemoves.statusmove+typemoves.physicalmoves):
        x.atkcat="Special"
    elif used in typemoves.statusmove:
        x.atkcat="Status"
    if y.ability=="Pressure":
        pp=2
    canatk=True
    x.use=used
    if len(x.moves)==0:
        await ctx.send(f" {x.name} has no move left!")
        used="Struggle"
    #Choice Item        
    if x.choiced is True and x.dmax is False and used!="None":
        if "Used" not in x.item and (x.choicedmove in x.moves and x.dmax is False) and x.status!="Sleep" and x.flinched==False and canatk is True:
            used=x.choicedmove
            x.use=used
        else:
            x.choicedmove="Struggle"
            used="Struggle"        
    if x.status=="Sleep":
        x.sleepturn-=1
        if x.sleepturn<=0 or x.ability in ["Insomnia","Vital Spirit"]:
            em.add_field(name="Sleep:",value=f"{x.nickname} woke up!")
            x.status="Alive"
            x.yawn=False
        else:
            em.add_field(name="Sleep:",value=f"{x.nickname} is fast asleep!") 
            x.recharge=x.precharge=False 
            if used=="Sleep Talk":
                em.add_field(name=f"Move:",value=f"{x.nickname} used Sleep Talk!")
                l=[]+x.moves
                l=list(set(l)-{"Sleep Talk"})
                used=random.choice(l)
            else:
                used="None"
    #Paralyzed        
    if x.status=="Paralyzed":
        ch=random.randint(1,100)
        if ch<=25:
            canatk=False
            used="None"
            x.precharge=False
            em.add_field(name=f"{x.nickname} is paralyzed!",value=f"{x.nickname} couldn't move because it's paralyzed!")
            x.precharge=x.recharge=False
        else:
            em.add_field(name="Paralysis:",value=f"{x.nickname} is paralyzed!")
            canatk=True      
    #Checks Freeze                
    elif y.status=="Frozen":
        if used in typemoves.firemoves:       
            em.add_field(name="Ice melted!",value=f"{y.nickname} thawed out.")
            y.status="Alive"       
    if x.status=="Frozen":
        ch=random.randint(1,10)
        if ch<=3 or used in typemoves.firemoves:
            em.add_field(name="Ice melted!",value=f"{x.nickname} thawed out.")
            x.status="Alive"
        else:
            em.add_field(name="Frozen:",value=f"{x.nickname} is frozen solid!")
            x.precharge=x.recharge=False
            used="None"                   
    #Recharging    
    if x.recharge==True:
        em.add_field(name="Rechange:",value=f"{x.nickname} is recharging.")
        x.recharge=False
        used="None"             
    if (choice2 in typemoves.buffmove or choice2=="None") and used in typemoves.protectmoves:
        em.add_field(name=f"{x.nickname} used {used}!",value="It failed.")
        used="None"
    #Consecutive Protect     
    if x.protect=="Pending" and used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct"]:
        em.add_field(name=f"{x.nickname} used {used}!",value="It failed.")
        x.protect=False
        used="None"                      
    if tr2.sub!="None" and used not in typemoves.bypass:
        yhp=tr2.sub.hp
    await preattack(ctx,x,y,tr1,tr2,used,choice2,field,turn)
    #Destiny Bond cancellation
    if used!="Destiny Bond" and "Destiny Bond" in x.moves:
        y.dbond=False
    #Disguise        
    if y.ability=="Disguise" and y.abilityused==False and used not in typemoves.statusmove+typemoves.buffmove+typemoves.zmoves+typemoves.multimove+typemoves.abilityigmoves and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and used!="None":
        em.add_field(name=f"{x.nickname} used {used}!",value=f"{y.nickname}'s {y.ability}!\n{y.nickname}'s disguise was busted!")
        y.hp-=round(y.maxhp/8)
        used="None"
        y.ability="Disguise[Used]"
        y.sprite=y.sprite.replace(".gif","-busted.gif")
    #Gigaton Hammer consecutively            
    if x.use!="None" and used=="Gigaton Hammer" and x.use=="Gigaton Hammer":
        used="None"
        em.add_field(name="Consecutive use:",value="Cannot use Gigaton Hammer consecutively!")
    #Stance Change        
    if x.ability=="Stance Change" and used!="None":
        await stance(ctx,x,y,turn,field,used,em)
    #Substitue Bypass
    if tr2.sub!="None":
        if tr2.sub.hp>0:
            y=tr2.sub
            if used in typemoves.bypass or x.ability=="Infiltrator":
                y=subr
            if used!="None" and used not in typemoves.soundmoves and used in typemoves.statusmove and (used not in typemoves.buffmove and used not in typemoves.bypass):   
                em.add_field(name=f"{x.nickname} used {used}!",value=f"It failed!")
                used="None"                        
    #Destiny Knot
    if x.item=="Destiny Knot" and y.infatuated==False and x.gender!=y.gender:
        y.infatuated=True
        em.add_field(name="Infatuation:",value=f"{y.nickname} is infatuated!")
    #Infatuation       
    if x.infatuated==True and y.ability=="Cute Charm":
        ch=random.randint(1,100)
        if ch<=25:
            canatk=False
            used="None"
            x.precharge=False
            em.add_field(name=f"{x.nickname} is infatuated!",value=f"{x.nickname} is immobilized by love!")
        else:
            em.add_field(name="Infatuation:",value=f"{x.nickname} is infatuated!")
            canatk=True
    #Checks Flinch    
    if x.flinched==True and x.dmax is False:
            x.precharge=False
            em.add_field(name="Flibch:",value=f"{x.nickname} flinched and couldn't move.")
            x.precharge=x.recharge=False
            x.flinched=False
            used="None"            
    #Confusion
    if x.confused is True:
        em.add_field(name="Confusion:",value=f" {x.name} is confused!")
        if turn>=x.confuseendturn or y.ability=="Oblivious":
            em.add_field(name="Confusion End!",value=f" {x.name} snapped out of confusion!")
            x.confused=False      
        ch=random.randint(1,100)  
        if ch>67 and x.dmax==False and x.confused==True:
            canatk=False
            used="None"
            em.add_field(name="Confused!",value=f" {x.name} hurt itx in confusion.")
            r=await randroll()
            x.hp-=await physical(x,x.level,x.atk,x.defense,base=40,a=1,r=r)
        else:
            canatk=True
    #Assist                
    if used=="Assist" and canatk==True:
        em.add_field(name=f"{x.nickname} used Assist!",value=f"It will random ally move!")
        pmoves=[]
        for i in tr1.pokemons:
            if i!=self:
                pmoves+=i.moves
                used=random.choice(pmoves)            
    #Me First        
    if used=="Me First" and canatk==True:
        if opuse!="None":
            if x.speed>y.speed:
                x.atk*=1.5
                x.spatk*=1.5
                used=choice2
                em.add_field(name=f"{x.nickname} used Me First!",value=f"It will use opponents move first!")
            else:
                em.add_field(name=f"{x.nickname} used {used}!",value=f"It failed!")    
    if x.ability=="Prankster" and "Dark" in (y.primaryType,y.secondaryType,y.teraType) and used in typemoves.statusmove:
        used="None"
        em.add_field(name="{x.nickname}'s Prankster!",value=f"{y.nickname} is immune to {x.nickname}'s Prankster due to being partially Dark-Type!")                   
    #Good as Gold        
    if y.ability=="Good as Gold" and used in typemoves.statusmove and used not in ["Stealth Rock","Haze","Toxic Spikes","Protect","Spiky Shield","Baneful Bunker","King's Shield","Silk Trap"]+typemoves.healingmoves+typemoves.buffmove:
        em.add_field(name=f"{x.nickname} used Me First!",value=f"{y.nickname}'s {y.ability} prevented {used}!")
        used="None"              
    #Encore   
    if x.encore is not False and x.dmax is False:
        if turn==x.enendturn:    
            x.encore=False
        elif x.encore in x.moves:
            used=x.encore
        else:
            used="Struggle"            
    #Safety Googles            
    if used in typemoves.powdermoves and y.item=="Safety Googles":
        em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.nickname}'s {y.item} protected it from {x.nickname}'s {used}!")
        used="None"  
    #Soundproof            
    if used in typemoves.soundmoves and y.ability=="Soundproof":
        em.add_field(name=f"{x.nickname} used {used}!",value=f"{y.nickname}'s Soundproof!")
        used="None"
    #Bulletproof        
    if used in typemoves.bulletmove and y.ability=="Bulletproof":
        em.add_field(name=f"{x.nickname} used {used}!",value=f"{y.nickname}'s Bulletproof!")
        used="None"
    #Fluffy        
    if used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
        if y.ability=="Fluffy":
            x.atk/=2
    #Priority blocker            
    if (field.terrain=="Psychic" or y.ability in ["Dazzling","Queenly Majesty","Armor Tail"]) and used in typemoves.prioritymove and x.dmax is False:
        if field.terrain!="Psychic":
            em.add_field(name=f"{x.nickname} used {used}!",value=f"{y.nickname}'s {y.ability}!\nCannot use priority moves!")
        elif field.terrain=="Psychic":
            em.add_field(name="Psychic Terrain:",value=f"Cannot use priority moves!")
        used="None"
    #Truant
    if x.ability=="Truant" and used!="Slack Off":
        if x.truant==True:
            em.add_field(name="{x.nickname}'s {x.ability}!",value=f"{x.nickname} is loafing around!")
            used="None"
            x.truant=False
        else:
            x.truant=True
    elif x.ability=="Truant" and used=="Slack Off":
        x.truant=False         
    #Assault Vest                
    if x.item=="Assault Vest" and used in typemoves.statusmove:
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"Cannot use status moves while holding an Assault Vest.")
        used="None"        
    #Protect Reset     
    if used not in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct","Silk Trap","Mad Guard"]:
        x.protect=False     
    if y.protect==True and (y.dmax is True and used not in typemoves.buffmove and used not in ["G-Max One Blow","G-Max Rapid Flow"] and used!="None"):
            em.add_field(name=f"{x.nickname} used {used}!",value=f"{y.nickname} protected itself from {x.nickname}'s {used}!")
            x.fmoveturn=0
            y.protect="Pending"
            if used in typemoves.zmoves:
                x.item+="[Used]"
                #x.moves.remove(x.use)
            used="None"
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker"]:
                used="None"     
    #Protection Moves                
    if y.dmax is False and y.protect==True and used not in typemoves.buffmove and (x.ability not in ["Infiltrator","Unseen Fist"]  and used not in ["Shadow Force","Phantom Force","Hyperspace Fury","Hyper Drill","Hyperspace Hole"] and used not in typemoves.maxmovelist and used not in typemoves.zmoves) and used!="None" :
        em.add_field(name=f"{x.nickname} used {used}!",value=f"{y.nickname} protected itself from {x.nickname}'s {used}!")
        x.fmoveturn=0
        y.protect="Pending"
        if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Max Guard"]:
            em.add_field(name=f"{x.nickname} used {used}!",value=f"It failed!")
            used="None"
            x.protect=False            
        if "Spiky Shield" in y.use and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            x.hp-=round(x.maxhp/8)
            em.add_field(name="Spiky Shield!",value=f"{x.nickname} was hurt by Spiky Shield.")
        if "Silk Trap" in y.use and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            await speedchange(em,x,y,-1)
        if "Obstruct" in y.use and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            await spatkchange(em,x,y,-1)
        if "King's Shield" in y.use and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            await atkchange(em,x,y,-1)
        if "Baneful Bunker" in y.use and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            if x.status=="Alive":
                x.status="Badly Poisoned"
                em.add_field(name="Baneful Bunker!",value=f"{x.nickname} was badly poisoned.")
    #Hit count            
    if used not in typemoves.statusmove and used!="None":
        y.atkby=x.name
        y.atktime+=1
    #Accuracy Check        
    if x.status!="Sleep" and canatk==True:
        x.use=used
        used=await accheck(x,y,field,em)         
    #Precharged Moves
    if x.precharge==True and len(x.moves)>0 and "Geomancy" not in x.moves and x.status not in ["Sleep","Frozen"] and canatk==True:
        l=list(set(x.moves).intersection(typemoves.premove))
        if len(l)!=0:
            used=l[0]            
    function_map = {
    "Shadow Ball": shadowball,
    "Charge": charge,
    "Psych Up": psychup,
    "Perish Song": perishsong,
    "Acupressure": acupressure,
    "Psycho Shift": psychoshift,
    "Flail": flail,
    "Reversal": reversal,
    "Earthquake": earthquake,
    "Psychic": psychic,
    "Stone Edge": stoneedge,
    "Order Up": orderup,
    "Spirit Break": spiritbreak,
    "False Surrender": falsesurrender,
    "Breaking Swipe": breakingswipe,
    "Glacial Lance": glaciallance,
    "Gigaton Hammer": gigatonhammer,
    "Play Rough": playrough,
    "Crunch": crunch,
    "Hydro Pump": hydropump,
    "Shadow Claw": shadowclaw,
    "Kowtow Cleave": kowtowcleave,
    "Body Slam": bodyslam,
    "Outrage": outrage,
    "Sucker Punch": suckerpunch,
    "Plasma Fists": plasmafists,
    "Mach Punch": machpunch,
    "Will-O-Wisp": willowisp,
    "Thunder Wave": thunderwave,
    "Icicle Crash": iciclecrash,
    "Close Combat": closecombat,
    "Superpower": superpower,
    "Bullet Punch": bulletpunch,
    "Extreme Speed": extremespeed,
    "Fire Fang": firefang,
    "Meteor Mash": meteormash,
    "Ice Beam": icebeam,
    "Scald": scald,
    "Recover": recover,
    "Air Slash": airslash,
    "Moonblast": moonblast,
    "Aura Sphere": aurasphere,
    "Dark Pulse": darkpulse,
    "Sludge Bomb": sludgebomb,
    "Rock Tomb": rocktomb,
    "Fire Punch": firepunch,
    "Ice Punch": icepunch,
    "Thunder Punch": thunderpunch,
    "Thunder Fang": thunderfang,
    "Poison Tail": poisontail,
    "Bug Buzz": bugbuzz,
    "Psychic Fangs": psychicfangs,
    "Poison Fang": poisonfang,
    "Bolt Strike": boltstrike,
    "Ice Fang": icefang,
    "Flare Blitz": flareblitz,
    "Misty Explosion": mistyexplosion,
    "Heal Bell": healbell,
    "Aromatherapy": aromatherapy,
    "Explosion": explosion,
    "Avalanche": avalanche,
    "Needle Arm": needlearm,
    "Leaf Blade": leafblade,
    "Drill Peck": drillpeck,
    "Poison Jab": poisonjab,
    "Freeze-Dry": freezedry,
    "Power Gem": powergem,
    "Thunderbolt": thunderbolt,
    "Toxic": toxic,
    "Milk Drink": milkdrink,
    "Slack Off": slackoff,
    "Roost": roost,
    "Heal Order": healorder,
    "Soft-Boiled": softboiled,
    "Jungle Healing": junglehealing,
    "Heat Wave": heatwave,
    "Sacred Fire": sacredfire,
    "Boomburst": boomburst,
    "Blizzard": blizzard,
    "Leaf Storm": leafstorm,
    "Make It Rain":makeitrain,
    "Extrasensory": extrasensory,
    "Draco Meteor": dracometeor,
    "Origin Pulse": originpulse,
    "Scorching Sands": scorchingsands,
    "Flamethrower": flamethrower,
    "Pain Split": painsplit,
    "Endeavor": endeavor,
    "Fire Blast": fireblast,
    "Giga Drain": gigadrain,
    "Dream Eater": dreameater,
    "Thunder": thunder,
    "Iron Head": ironhead,
    "Grassy Glide": grassyglide,
    "Drum Beating": drumbeating,
    "Ice Hammer": icehammer,
    "Earth Power": earthpower,
    "Hammer Arm": hammerarm,
    "High Jump Kick": highjumpkick,
    "Pyro Ball": pyroball,
    "Mist Ball": mistball,
    "Luster Purge": lusterpurge,
    "Venoshock": venoshock,
    "Final Gambit": finalgambit,
    "X-Scissor": xscissor,
    "Gyro Ball": gyroball,
    "Zen Headbutt": zenheadbutt,
    "Megahorn": megahorn,
    "Ice Shard": iceshard,
    "Jet Punch": jetpunch,
    "Aqua Jet": aquajet,
    "Dragon Hammer": dragonhammer,
    "Ice Spinner": icespinner,
    "Iron Tail": irontail,
    "Slash": slash,
    "Cross Chop": crosschop,
    "Aqua Cutter": aquacutter,
    "Growth": growth,
    "Acid Armor": acidarmor,
    "Iron Defense": irondefense,
    "Shelter": shelter,
    "Agility": agility,
    "Rock Polish": rockpolish,
    "Leaf Tornado": leaftornado,
    "Cotton Guard": cottonguard,
    "Psyshock": psyshock,
    "Curse": curse,
    "Haze": haze,
    "Amnesia": amnesia,
    "Acrobatics": acrobatics,
    "Cross Poison": crosspoison,
    "Wave Crash": wavecrash,
    "Wood Hammer": woodhammer,
    "Brave Bird": bravebird,
    "Bulldoze": bulldoze,
    "Cosmic Power": cosmicpower,
    "Energy Ball": energyball,
    "Psystrike": psystrike,
    "Strange Steam": strangesteam,
    "Swords Dance": swordsdance,
    "Rock Slide": rockslide,
    "Quiver Dance": quiverdance,
    "Crabhammer": crabhammer,
    "Shell Smash": shellsmash,
    "Focus Blast": focusblast,
    "Victory Dance": victorydance,
    "Calm Mind": calmmind,
    "Expanding Force": expandingforce,
    "Rising Voltage": risingvoltage,
    "Bulk Up": bulkup,
    "Freezing Glare": freezingglare,
    "Nasty Plot": nastyplot,
    "Tail Glow": tailglow,
    "Rising Voltage": risingvoltage,
    "Oblivion Wing": oblivionwing,
    "Grassy Terrain": grassyterrain,
    "Psychic Terrain": psychicterrain,
    "Misty Terrain": mistyterrain,
    "Electric Terrain": electricterrain,
    "Max Overgrowth":maxovergrowth,
    "Max Starfall":maxstarfall,
    "Max Lightning":maxlightning,
    "Max Mindstorm":maxmindstorm,
    "Max Quake":maxquake,
    "Max Steelspike":maxsteelspike,
    "Max Strike":maxstrike,
    "Max Phantasm":maxphantasm,
    "Max Darkness":maxdarkness,
    "Max Wyrmwind":maxwyrmwind,
    "Max Flutterby":maxflutterby,
    "Max Knuckle":maxknuckle,
    "Max Ooze":maxooze,
    "Max Airstream":maxairstream,
    "Max Geyser":maxgeyser,
    "Max Flare":maxflare,
    "Max Rockfall":maxrockfall,
    "Max Hailstorm":maxhailstorm,
    "Night Slash":nightslash,
    "Esper Wing":esperwing,
    "Psycho Cut":psychocut,
    "Wicked Blow":wickedblow,
    "Storm Throw":stormthrow,
    "Leech Life":leechlife,
    "Encore":encore,
    "Wish":wish,
    "Aqua Ring":aquaring,
    "Doodle":doodle,
    "Yawn":yawn,
    "Surf":surf,
    "Muddy Water":muddywater,
    "Flash Cannon":flashcannon,
    "Fleur Cannon":fleurcannon,
    "Psycho Boost":psychoboost,
    "Spicy Extract":spicyextract,
    "Recycle":recycle,
    "Skill Swap":skillswap,
    "Trick":trick,
    "Trick-Or-Treat":trickortreat,
    "Forests Curse":forestscurse,
    "Magic Powder":magicpowder,
    "Soak":soak,
    "Tar Shot":tarshot,
    "Fusion Flare":fusionflare,
    "Searing Shot":searingshot,
    "Fiery Wrath":fierywrath,
    "V-Create":vcreate,
    "Steam Eruption":steameruption,
    "Fiery Dance":fierydance,
    "Lumina Crash":luminacrash,
    "Super Fang":superfang,
    "Ruination":ruination,
    "Natures Madness":naturesmadness,
    "Charm":charm,
    "Scary Face":scaryface,
    "Eerie Impulse":eerieimpulse,
    "Metal Sound":metalsound,
    "Fake Tears":faketears,
    "Feather Dance":featherdance,
    "Fillet Away":filletaway,
    "Headlong Rush":headlongrush,
    "Armor Cannon":armorcannon,
    "Wave Crash":wavecrash,
    "Wood Hammer":woodhammer,
    "Volt Tackle":volttackle,
    "Bolt Strike":boltstrike,
    "Fusion Bolt":fusionbolt,
    "Dazzling Gleam":dazzlinggleam,
    "Lava Plume":lavaplume,
    "Hurricane":hurricane,
    "Overheat":overheat,
    "Blast Burn":blastburn,
    "Hydro Cannon":hydrocannon,
    "Frenzy Plant":frenzyplant,
    "Sparkling Aria":sparklingaria,
    "Head Smash":headsmash,
    "Last Respects":lastrespects,
    "Power Whip":powerwhip,
    "Astral Barrage":astralbarrage,
    "Knock Off":knockoff,
    "Seed Bomb":seedbomb,
    "Crush Claw":crushclaw,
    "Spin Out":spinout,
    "Meteor Beam":meteorbeam,
    "Phantom Force":phantomforce,
    "Sky Attack":skyattack,
    "Heat Crash":heatcrash,
    "Heavy Slam":heavyslam,
    "Grass Knot":grassknot,
    "Return":returm,
    "Facade":facade,
    "Body Press":bodypress,
    "Waterfall":waterfall,
    "Flower Trick":flowertrick,
    "Rapid Spin":rapidspin,
    "Dragon Dance":dragondance,
    "G-Max Fireball":gmaxfireball,
    "G-Max Drum Solo":gmaxdrumsolo,
    "G-Max Hydrosnipe":gmaxhydrosnipe,
    "G-Max Foam Burst":gmaxfoamburst,
    "G-Max Sandblast":gmaxsandblast,
    "Spore":spore,
    "Shadow Sneak":shadowsneak,
    "Drain Punch":drainpunch,
    "Sunny Day":sunnyday,
    "Rain Dance":raindance,
    "Sandstorm":sandstorm,
    "Snowscape":snowscape,
    "Gunk Shot":gunkshot,
    "Belch":belch,
    "Water Spout":waterspout,
    "Eruption":eruption,
    "Crush Grip":crushgrip,
    "Dragon Energy":dragonenergy,
    "Stomping Tantrum":stompingtantrum,
    "Magnitude":magnitude,
    "High Horsepower":highhorsepower,
    "Fire Lash":firelash,
    "Liquidation":liquidation,
    "Mystical Power":mysticalpower,
    "Torch Song":torchsong,
    "Protect":prtect,
    "Spiky Shield":spikyshield,
    "Baneful Bunker":banefulbunker,
    "Max Guard":maxguard,
    "Obstruct":obstruct,
    "Silk Trap":silktrap,
    "Double-Edge":doubleedge
}
    if used in function_map:
        await function_map[used](ctx, x, y, tr1, em, field,turn)
    elif used=="Dual Wingbeat":
        hit=0
        while True:
            hit+=1
            await dualwingbeat(ctx,x,y,tr1,em,field,turn)   
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")         
    elif used=="Dual Chop":
        hit=0
        while True:
            hit+=1
            await dualchop(ctx,x,y,tr1,em,field,turn)   
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")                  
    elif used=="Flip Turn":
        await flipturn(ctx,x,y,tr1,em,field,turn) 
        if len(tr1.pokemons)>1:
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
    elif used=="Volt Switch":
        await voltswitch(ctx,x,y,tr1,em,field,turn) 
        if len(tr1.pokemons)>1:
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
    elif used=="U-turn":
        await uturn(ctx,x,y,tr1,em,field,turn) 
        if len(tr1.pokemons)>1:
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
    elif used=="Hyper Beam":
        await hyperbeam(ctx,x,y,tr1,em,field,turn)
        x.recharge=True
    elif used=="Prismatic Laser":
        await prismaticlaser(ctx,x,y,tr1,em,field,turn)
        x.recharge=True
    else:
        if used!="None":
            em.add_field(name="Error:",value=f"{used} is missing!")        
    if y.hp>y.maxhp:
        y.hp=y.maxhp
    if x.hp>x.maxhp:
        x.hp=x.maxhp
    if y.hp<0:
        y.hp=0
    if x.hp<0:
        x.hp=0
    y.dmgtaken=yhp-y.hp
    if y.hp!=yhp and used!="None":
        x.miss=False
    if y.hp==yhp and used=="None":
        x.miss=True
        if x.item=="Blunder Policy":
            em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"Blunder Policy was used upon miss!")
            item+="[Used]"
            await speedchange(em,x,x,2)
    if yhp==y.maxhp and y.hp<=0:
        if y.item=="Focus Sash" and used not in typemoves.multimove:
            em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.nickname} hung on using Focus Sash!")
            y.hp=1
            y.item+="[Used]"
        elif y.ability in ["Sturdy","Nine Lives"] and y.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and used not in typemoves.abilityigmoves and used not in typemoves.multimove:
            em.add_field(name=f"{y.nickname}'s {y.ability}!",value=f"{y.nickname} hung on using {y.ability}!")
            y.hp=1
    if y.item=="Focus Band" and used not in typemoves.multimove and y.hp<=0:
        ch=random.randint(1,10)
        if ch==1:
            em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.nickname} hung on using Focus Band.!")
            y.hp=1
    if "Gulp Missile" in y.ability and y.hp!=yhp:
        if "-" in y.ability:
            y.sprite=y.sprite.split("-")[0]+".gif"
            em.add_field(name=f"{y.nickname}'s {y.ability}!",value=f"{y.nickname} launched something at the target!")
            if x.ability!="Magic Guard":
                x.hp-=(x.maxhp/4)
            if "Pikachu" in y.ability:
                paralyzed(y,x,100)
                y.ability="Gulp Missile"
            if "Arrocuda" in y.ability:
                defchange(x,y,-0.5)
                y.ability="Gulp Missile"            
    if len(x.moves)>=1 and x.use==x.moves[0] and len(x.pplist)>=1:
        if x.pplist[0]==1:
            pp=1
        x.pplist[0]-=pp
    elif len(x.moves)>=2 and x.use==x.moves[1] and len(x.pplist)>=2:
        if x.pplist[1]==1:
            pp=1
        x.pplist[1]-=pp
    elif len(x.moves)>=3 and x.use==x.moves[2] and len(x.pplist)>=3:
        if x.pplist[2]==1:
            pp=1
        x.pplist[2]-=pp
    elif len(x.moves)>=4 and x.use==x.moves[3] and len(x.pplist)>=4:
        if x.pplist[2]==1:
            pp=1
        x.pplist[3]-=pp
    if x.dmax is True and canatk is True:
        if len(x.maxmoves)>=1 and used==x.maxmoves[0]:
            x.pplist[0]-=pp
        if len(x.maxmoves)>=2 and used==x.maxmoves[1]:
            x.pplist[1]-=pp
        if len(x.maxmoves)>=3 and used==x.maxmoves[2]:
            x.pplist[2]-=pp
        if len(x.maxmoves)>=4 and used==x.maxmoves[3]:
            x.pplist[3]-=pp
    per=round(((yhp-y.hp)/y.maxhp)*100,2)
    sper=round(((xhp-x.hp)/x.maxhp)*100,2)
    if xhp!=x.hp and xhp-x.hp<0 and x.ability!="Parental Bond" and x==me:
        em.add_field(name="Regeneration:",value=f"{x.nickname} regained {-sper}% of its health!")
    if yhp!=y.hp and yhp-y.hp>0 and x.ability!="Parental Bond" and y==they:
        em.add_field(name="Damage:",value=f"{y.nickname} lost {per}% of its health!")
    if x.hp!=xhp and x==me and x.hp<xhp and sper>0:
        em.add_field(name="Recoil:",value=f"Total damage received {sper}%")  
    #Persim    
    if y.item=="Persim Berry" and y.confused==True and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.item} cured {y.nickname}'s confusion!")
        y.confused=False
        y.item+="[Used]"     
   #Persim   
    if x.item=="Persim Berry" and x.confused==True and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.item} cured {x.nickname}'s confusion!")
        x.confused=False
        x.item+="[Used]"        
    #Cheri        
    if x.item=="Cheri Berry" and x.status=="Paralyzed" and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.item} cured {x.nickname}'s paralysis!")
        x.status="Alive"
        x.item+="[Used]"
    #Cheri        
    if y.item=="Cheri Berry" and y.status=="Paralyzed" and y.hp>0 and y.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp*0.33)
        em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.item} cured {y.nickname}'s paralysis!")
        y.status="Alive"
        y.item+="[Used]"     
    #Rawst
    if x.item=="Rawst Berry" and x.status=="Burned" and x.hp>0 and x.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.item} cured {x.nickname}'s burn!")
        x.status="Alive"
        x.item+="[Used]"
    #Rawst
    if y.item=="Rawst Berry" and y.status=="Burned" and y.hp>0 and y.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp*0.33)
        em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.item} cured {y.nickname}'s burn!")
        y.status="Alive"
        y.item+="[Used]"        
    #Chesto 
    if x.item=="Chesto Berry" and x.status=="Sleep" and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.item} cured {x.nickname}'s sleep!")
        x.status="Alive"
        x.item+="[Used]"
   #Chesto
    if y.item=="Chesto Berry" and y.status=="Sleep" and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.item} cured {y.nickname}'s sleep!")
        y.status="Alive"
        y.item+="[Used]"
   #Aspear
    if x.item=="Aspear Berry" and x.status=="Frozen" and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.item} cured {x.nickname}'s freeze!")
        x.status="Alive"
        x.item+="[Used]"
    #Aspear
    if y.item=="Aspear Berry" and y.status=="Frozen" and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.item} cured {y.nickname}'s freeze!")
        y.status="Alive"
        y.item+="[Used]"
    #Pecha
    if x.item=="Pecha Berry" and x.status=="Badly Poisoned" and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.item} cured {x.nickname}'s poison!")
        x.status="Alive"
        x.item+="[Used]"
    #Pecha
    if y.item=="Pecha Berry" and y.status=="Badly Poisoned" and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.item} cured {y.nickname}'s poison!")
        y.status="Alive"
        y.item+="[Used]"
    #Lum
    if x.item=="Lum Berry" and x.status!="Alive"and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.item} cured {x.nickname}'s status condition!")
        x.status="Alive"
        x.item+="[Used]"        
    #Lum
    if y.item=="Lum Berry" and y.status!="Alive" and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.item} cured {y.nickname}'s status condition!")
        y.status="Alive"
        y.item+="[Used]"
    #Sitrus
    if y.hp<=y.maxhp/2 and y.hp>0:
        if y.item=="Sitrus Berry" and x.ability not in ["Unnerve","As One"]:
            if y.ability!="Ripen":
                y.hp+=round(y.maxhp/2)     
            if y.ability=="Ripen":
                y.hp+=round(y.maxhp/4)
            em.add_field(name=f"{await itemicon(y.item)} {y.nickname}'s {y.item}:",value=f"{y.nickname} restored Hp using its {y.item}!")
            y.item+="[Used]"        
    #Sitrus
    if x.hp<=x.maxhp/2 and x.hp>0:
        if x.item=="Sitrus Berry" and y.ability not in ["Unnerve","As One"]:    
            if x.ability=="Ripen":   
                x.hp+=round(x.maxhp/2)
            if x.ability!="Ripen":   
                x.hp+=round(x.maxhp/4)
            em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.nickname} restored Hp using its {x.item}!")
            x.item+="[Used]"    
    if x.hp>0:
        if x.item=="Shell Bell" and y.dmgtaken>0 and y.protect==False and x.recharge==False:
            x.hp+=(y.dmgtaken/8)
            em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"{x.nickname} restored a little HP using its Shell Bell!")            
    if y.hp>0:
        await berry(em,y,x,xhp,yhp,turn)     
        if y.hp<=(y.maxhp/2)  and yhp>(y.maxhp/2):
            if y.ability=="Berserk":
                em.add_field(name=f"{y.nickname}'s {y.ability}!",value=f"{y.nickname} went berserk!")
                await spatkchange(em,y,y,1)
            if y.ability=="Anger Shell":
                em.add_field(name=f"{y.nickname}'s {y.ability}!",value=f"{y.nickname} became extremely angry!")
                await atkchange(em,y,y,2)
                await spatkchange(em,y,y,2)
                await speedchange(em,y,y,2)
                await defchange(em,y,y,-1)
                await spdefchange(em,y,y,-1)
        if y.ability=="Stamina" and y.hp!=yhp and x.hp>0:
            await defchange(em,y,x,1)      
    if y.ability=="Innards Out" and y==they and y.hp<=0:
        em.add_field(name=f"{y.nickname}'s {y.ability}!",value=f"{y.nickname} launched a huge punch!")
        x.hp-=yhp    
    if x.item=="Throat Spray" and used in typemoves.soundmoves:
        await spatkchange(em,x,x,1)
        em.add_field(name=f"{await itemicon(x.item)} {x.nickname}'s {x.item}:",value=f"The Throat Spray raised {x.nickname}'s Special Attack!")
        x.item+="[Used]"           
    await ctx.send(embed=em)
    return x,y
    
async def movecolor(u):
    c=int("FFFFFF",16)
    if u in typemoves.normalmoves:
        c=int("BFB97F",16)
    elif u in typemoves.fightingmoves:
        c=int("D32F2E",16)
    elif u in typemoves.flyingmoves:
        c=int("9E87E1",16)
    elif u in typemoves.poisonmoves:
        c=int("AA47BC",16)
    elif u in typemoves.groundmoves:
        c=int("DFB352",16)
    elif u in typemoves.rockmoves:
        c=int("BDA537",16)
    elif u in typemoves.bugmoves:
        c=int("98B92E",16)
    elif u in typemoves.ghostmoves:
        c=int("7556A4",16)
    elif u in typemoves.steelmoves:
        c=int("B4B4CC",16)
    elif u in typemoves.firemoves:
        c=int("E86513",16)
    elif u in typemoves.watermoves:
        c=int("2196F3",16)
    elif u in typemoves.grassmoves:
        c=int("4CB050",16)
    elif u in typemoves.electricmoves:
        c=int("FECD07",16)
    elif u in typemoves.psychicmoves:
        c=int("EC407A",16)
    elif u in typemoves.icemoves:
        c=int("80DEEA",16)
    elif u in typemoves.fairymoves:
        c=int("F483BB",16)
    elif u in typemoves.darkmoves:
        c=int("5C4038",16)
    elif u in typemoves.dragonmoves:
        c=int("673BB7",16)
    return c        
        
