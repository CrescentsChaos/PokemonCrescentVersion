import discord
from pokemon import *
from plugins import *
from moves import *
async def stancechange(ctx,x,y,turn,field,used,em):    
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
        print(f"  {fg(x.color)+x.name+fg.rs} fell asleep!")
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
                
async def attack(ctx,bot,x,y,tr1,tr2,used,choice2,field,turn):
    hit=1
    canatk=True
    x.use=used
    if len(x.moves)==0:
        await ctx.send(f" {x.name} has no move left!")
        used="Struggle"
    xhp=x.hp
    yhp=y.hp
    if tr2.sub!="None" and used not in typemoves.bypass:
        yhp=tr2.sub.hp
    c=await movecolor(used)
    em=discord.Embed(title=f"{tr1.name}:",color=c)    
    em.set_thumbnail(url=x.sprite)    
    await preattack(ctx,x,y,tr1,tr2,used,choice2,field,turn)
    if x.ability=="Stance Change":
        await stancechange(ctx,x,y,turn,field,used,em)
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
    if used=="Shadow Ball":
        await shadowball(ctx,x,y,tr1,em,field)  
    elif used=="Charge":
        await charge(ctx,x,y,tr1,em,field)
    elif used=="Psych Up":
        await psychup(ctx,x,y,tr1,em,field) 
    elif used=="Perish Song":
        await perishsong(ctx,x,y,tr1,em,field)  
    elif used=="Acupressure":
        await acupressure(ctx,x,y,tr1,em,field) 
    elif used=="Psycho Shift":
        await psychoshift(ctx,x,y,tr1,em,field) 
    elif used=="Flail":
        await flail(ctx,x,y,tr1,em,field)  
    elif used=="Reversal":
        await reversal(ctx,x,y,tr1,em,field)    
    elif used=="Earthquake":
        await earthquake(ctx,x,y,tr1,em,field)    
    elif used=="Psychic":
        await psychic(ctx,x,y,tr1,em,field)        
    elif used=="Stone Edge":
        await stoneedge(ctx,x,y,tr1,em,field)        
    elif used=="Dragon Claw":
        await dragonclaw(ctx,x,y,tr1,em,field)  
    elif used=="Order Up":
        await orderup(ctx,x,y,tr1,em,field)  
    elif used=="Spirit Break":
        await spiritbreak(ctx,x,y,tr1,em,field) 
    elif used=="False Surrender":
        await falsesurrender(ctx,x,y,tr1,em,field)      
    elif used=="Breaking Swipe":
        await breakingswipe(ctx,x,y,tr1,em,field)      
    elif used=="Glacial Lance":
        await glaciallance(ctx,x,y,tr1,em,field)    
    elif used=="Gigaton Hammer":
        await gigatonhammer(ctx,x,y,tr1,em,field) 
    elif used=="Play Rough":
        await playrough(ctx,x,y,tr1,em,field) 
    elif used=="Crunch":
        await crunch(ctx,x,y,tr1,em,field)  
    elif used=="Hydro Pump":
        await hydropump(ctx,x,y,tr1,em,field) 
    elif used=="Shadow Claw":
        await shadowclaw(ctx,x,y,tr1,em,field) 
    elif used=="Kowtow Cleave":
        await kowtowcleave(ctx,x,y,tr1,em,field) 
    elif used=="Body Slam":
        await bodyslam(ctx,x,y,tr1,em,field) 
    elif used=="Outrage":
        await outrage(ctx,x,y,tr1,em,field) 
    elif used=="Sucker Punch":
        await suckerpunch(ctx,x,y,tr1,em,field) 
    elif used=="Plasma Fists":
        await plasmafists(ctx,x,y,tr1,em,field) 
    elif used=="Mach Punch":
        await machpunch(ctx,x,y,tr1,em,field) 
    elif used=="Will-O-Wisp":
        await willowisp(ctx,x,y,tr1,em,field) 
    elif used=="Thunder Wave":
        await thunderwave(ctx,x,y,tr1,em,field) 
    elif used=="Icicle Crash":
        await iciclecrash(ctx,x,y,tr1,em,field) 
    elif used=="Close Combat":
        await closecombat(ctx,x,y,tr1,em,field) 
    elif used=="Superpower":
        await superpower(ctx,x,y,tr1,em,field) 
    elif used=="Bullet Punch":
        await bulletpunch(ctx,x,y,tr1,em,field) 
    elif used=="Extreme Speed":
        await extremespeed(ctx,x,y,tr1,em,field) 
    elif used=="Fire Fang":
        await firefang(ctx,x,y,tr1,em,field) 
    elif used=="Meteor Mash":
        await meteormash(ctx,x,y,tr1,em,field) 
    elif used=="Ice Beam":
        await icebeam(ctx,x,y,tr1,em,field) 
    elif used=="Scald":
        await scald(ctx,x,y,tr1,em,field) 
    elif used=="Recover":
        await recover(ctx,x,y,tr1,em,field) 
    elif used=="Air Slash":
        await airslash(ctx,x,y,tr1,em,field) 
    elif used=="Moonblast":
        await moonblast(ctx,x,y,tr1,em,field) 
    elif used=="Aura Sphere":
        await aurasphere(ctx,x,y,tr1,em,field) 
    elif used=="Dark Pulse":
        await darkpulse(ctx,x,y,tr1,em,field) 
    elif used=="Sludge Bomb":
        await sludgebomb(ctx,x,y,tr1,em,field) 
    elif used=="Rock Tomb":
        await rocktomb(ctx,x,y,tr1,em,field) 
    elif used=="Fire Punch":
        await firepunch(ctx,x,y,tr1,em,field) 
    elif used=="Ice Punch":
        await icepunch(ctx,x,y,tr1,em,field) 
    elif used=="Thunder Punch":
        await thunderpunch(ctx,x,y,tr1,em,field) 
    elif used=="Thunder Fang":
        await thunderfang(ctx,x,y,tr1,em,field) 
    elif used=="Poison Tail":
        await poisontail(ctx,x,y,tr1,em,field) 
    elif used=="Psychic Fangs":
        await psychicfangs(ctx,x,y,tr1,em,field) 
    elif used=="Poison Fang":
        await poisonfang(ctx,x,y,tr1,em,field) 
    elif used=="Bolt Strike":
        await boltstrike(ctx,x,y,tr1,em,field) 
    elif used=="Ice Fang":
        await icefang(ctx,x,y,tr1,em,field) 
    elif used=="Flare Blitz":
        await flareblitz(ctx,x,y,tr1,em,field) 
    elif used=="Misty Explosion":
        await mistyexplosion(ctx,x,y,tr1,em,field) 
    elif used=="Explosion":
        await explosion(ctx,x,y,tr1,em,field) 
    elif used=="Avalanche":
        await avalanche(ctx,x,y,tr1,em,field) 
    elif used=="Needle Arm":
        await needlearm(ctx,x,y,tr1,em,field) 
    elif used=="Leaf Blade":
        await leafblade(ctx,x,y,tr1,em,field) 
    elif used=="Drill Peck":
        await drillpeck(ctx,x,y,tr1,em,field) 
    elif used=="Poison Jab":
        await poisonjab(ctx,x,y,tr1,em,field) 
    elif used=="Freeze-Dry":
        await freezedry(ctx,x,y,tr1,em,field) 
    elif used=="Power Gem":
        await powergem(ctx,x,y,tr1,em,field) 
    elif used=="Thunderbolt":
        await thunderbolt(ctx,x,y,tr1,em,field) 
    elif used=="Toxic":
        await toxic(ctx,x,y,tr1,em,field) 
    elif used=="Milk Drink":
        await milkdrink(ctx,x,y,tr1,em,field) 
    elif used=="Slack Off":
        await slackoff(ctx,x,y,tr1,em,field) 
    elif used=="Roost":
        await roost(ctx,x,y,tr1,em,field) 
    elif used=="Heal Order":
        await healorder(ctx,x,y,tr1,em,field) 
    elif used=="Soft-Boiled":
        await softboiled(ctx,x,y,tr1,em,field) 
    elif used=="Jungle Healing":
        await junglehealing(ctx,x,y,tr1,em,field) 
    elif used=="Heat Wave":
        await heatwave(ctx,x,y,tr1,em,field) 
    elif used=="Sacred Fire":
        await sacredfire(ctx,x,y,tr1,em,field) 
    elif used=="Boomburst":
        await boomburst(ctx,x,y,tr1,em,field) 
    elif used=="Blizzard":
        await blizzard(ctx,x,y,tr1,em,field) 
    elif used=="Leaf Storm":
        await leafstorm(ctx,x,y,tr1,em,field) 
    elif used=="Make It Rain":
        await makeitrain(ctx,x,y,tr1,em,field)
    elif used=="Extrasensory":
        await extrasensory(ctx,x,y,tr1,em,field) 
    elif used=="Draco Meteor":
        await dracometeor(ctx,x,y,tr1,em,field) 
    elif used=="Origin Pulse":
        await originpulse(ctx,x,y,tr1,em,field) 
    elif used=="Scorching Sands":
        await scorchingsands(ctx,x,y,tr1,em,field) 
    elif used=="Flamethrower":
        await flamethrower(ctx,x,y,tr1,em,field) 
    elif used=="Fire Blast":
        await fireblast(ctx,x,y,tr1,em,field) 
    elif used=="Giga Drain":
        await gigadrain(ctx,x,y,tr1,em,field) 
    elif used=="Dream Eater":
        await dreameater(ctx,x,y,tr1,em,field) 
    elif used=="Thunder":
        await thunder(ctx,x,y,tr1,em,field) 
    elif used=="Iron Head":
        await ironhead(ctx,x,y,tr1,em,field) 
    elif used=="Grassy Glide":
        await grassyglide(ctx,x,y,tr1,em,field) 
    elif used=="Drum Beating":
        await drumbeating(ctx,x,y,tr1,em,field) 
    elif used=="Ice Hammer":
        await icehammer(ctx,x,y,tr1,em,field) 
    elif used=="Hammer Arm":
        await hammerarm(ctx,x,y,tr1,em,field) 
    elif used=="X-Scissor":
        await xscissor(ctx,x,y,tr1,em,field) 
    elif used=="Zen Headbutt":
        await zenheadbutt(ctx,x,y,tr1,em,field) 
    elif used=="Megahorn":
        await megahorn(ctx,x,y,tr1,em,field) 
    elif used=="Ice Shard":
        await iceshard(ctx,x,y,tr1,em,field) 
    elif used=="Jet Punch":
        await jetpunch(ctx,x,y,tr1,em,field) 
    elif used=="Aqua Jet":
        await aquajet(ctx,x,y,tr1,em,field) 
    elif used=="Dragon Hammer":
        await dragonhammer(ctx,x,y,tr1,em,field) 
    elif used=="Ice Spinner":
        await icespinner(ctx,x,y,tr1,em,field) 
    elif used=="Flip Turn":
        await flipturn(ctx,x,y,tr1,em,field) 
        if len(tr1.pokemons)>1:
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
    elif used=="Volt Switch":
        await voltswitch(ctx,x,y,tr1,em,field) 
        if len(tr1.pokemons)>1:
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
    elif used=="U-turn":
        await uturn(ctx,x,y,tr1,em,field) 
        if len(tr1.pokemons)>1:
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
    elif used=="Iron Tail":
        await irontail(ctx,x,y,tr1,em,field) 
    elif used=="Rising Voltage":
        await risingvoltage(ctx,x,y,tr1,em,field) 
    elif used=="Oblivion Wing":
        await oblivionwing(ctx,x,y,tr1,em,field)
    elif used=="Grassy Terrain":
        await grassyterrain(ctx,x,y,tr1,em,field,turn)
    elif used=="Psychic Terrain":
        await psychicterrain(ctx,x,y,tr1,em,field,turn) 
    elif used=="Misty Terrain":
        await mistyterrain(ctx,x,y,tr1,em,field,turn)
    elif used=="Electric Terrain":
        await electricterrain(ctx,x,y,tr1,em,field,turn)
    elif used=="Hyper Beam":
        await hyperbeam(ctx,x,y,tr1,em,field)
        x.recharge=True
    elif used=="Prismatic Laser":
        await prismaticlaser(ctx,x,y,tr1,em,field)
        x.recharge=True
    else:
        em.add_field(name="Error:",value=f"{used} is missing!")        
    if y.hp>y.maxhp:
        y.hp=y.maxhp
    if x.hp>x.maxhp:
        x.hp=x.maxhp
    if y.hp<0:
        y.hp=0
    if x.hp<0:
        x.hp=0
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
        
