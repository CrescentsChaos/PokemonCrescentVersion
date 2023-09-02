import random
from movelist import *
from plugins import *
#freeze
async def freeze(em,x,y,ch):
    miss=100-ch
    if x.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if y.name!="Substitute" and chance>=miss and "Ice" not in (y.secondaryType,y.primaryType,y.teraType) and y.ability not in ["Ice Body","Magic Bounce","Leaf Guard","Comatose","Ice Scales","Snow Cloak","Snow Warning"] and y.status=="Alive" and x.ability!="Sheer Force" and y.hp>0:
        if y.item!="Covert Cloak" or y.ability not in ["Shield Dust"]:
            y.status="Frozen"
            em.add_field(name="Status:",value=f"{y.nickname} is frozen solid!")
    if chance>=miss and y.status=="Frozen" and y.ability in ["Synchronize"] and x.status=="Alive":
        x.status="Frozen"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} is frozen solid!")
    if chance>=miss and y.ability in ["Magic Bounce"] and x.status=="Alive" and y.status!="Frozen":
        x.status="Frozen"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} is frozen solid!")
#burn
async def burn(em,x,y,ch):
    if x.ability=="Serene Grace":
        ch*=2
    elif x.ability=="Pyromancy":
        ch*=5
    miss=100-ch
    chance=random.randint(1,100)
    if y.name!="Substitute" and chance>=miss and "Fire" not in (y.secondaryType,y.primaryType,y.teraType) and y.ability not in ["Flash Fire","Magic Bounce","Leaf Guard","Comatose","Thermal Exchange","Magma Armor","Water Veil"] and y.status=="Alive" and x.ability!="Sheer Force" and y.hp>0:
        if y.item!="Covert Cloak" or y.ability not in ["Shield Dust"]:
            y.status="Burned"
            em.add_field(name="Status:",value=f"{y.nickname} was burned.")
    if chance>=miss and y.status=="Burned" and y.ability in ["Synchronize"] and x.status=="Alive":
        x.status="Burned"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} was burned.")     
    if chance>=miss and y.ability in ["Magic Bounce"] and x.status=="Alive" and y.status!="Burned":
        x.status="Burned"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} was burned.")            
#paralyze
async def paralyze(em,x,y,ch):
    miss=100-ch
    if x.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if y.name!="Substitute" and chance>=miss and (((("Electric" not in (y.secondaryType,y.primaryType,y.teraType) and "Ground" not in (y.secondaryType,y.primaryType,y.teraType) or y.use in ["Body Slam","Force Plam","Glare","Lightning Rod","Volt Absorb","Juggernaut"] and y.ability not in ["Limber","Leaf Guard","Comatose","Magic Bounce"])) and y.status=="Alive" and x.ability!="Sheer Force") and y.hp>0):
        if y.item!="Covert Cloak" or y.ability not in ["Shield Dust"]:
            y.status="Paralyzed"
            em.add_field(name="Status:",value=f"{y.nickname} was paralyzed!")
    if chance>=miss and y.status=="Paralyzed" and y.ability in ["Synchronize"] and x.status=="Alive":
        x.status="Paralyzed"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} was paralayzed.")     
    if chance>=miss and y.ability in ["Magic Bounce"] and x.status=="Alive" and y.status!="Paralyzed":
        x.status="Paralyzed"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} was paralayzed.")       
#poison
async def poison(em,x,y,ch):
    miss=100-ch
    if x.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if y.name!="Substitute" and (chance>=miss and ("Steel" not in (y.secondaryType,y.primaryType,y.teraType) and "Poison"  not in (y.secondaryType,y.primaryType,y.teraType) or x.ability=="Corrosion") and y.ability not in ["Immunity","Magic Bounce","Leaf Guard","Comatose","Pastel Veil"] and y.status=="Alive" and x.ability!="Sheer Force") and y.hp>0:
        if y.item!="Covert Cloak" or y.ability not in ["Shield Dust"]:
            y.status="Badly Poisoned"
            em.add_field(name="Status:",value=f"{y.nickname} was badly poisoned.")
    if chance>=miss and y.status=="Badly Poisoned" and y.ability in ["Synchronize"] and x.status=="Alive":
        x.status="Badly Poisoned"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} was badly poisoned!")
    if chance>=miss and y.ability in ["Magic Bounce"] and x.status=="Alive" and y.status!="Badly Poisoned":
        x.status="Badly Poisoned"      
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} was badly poisoned!") 
#sleep
async def sleep(em,x,y,ch):
    miss=100-ch
    if x.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if y.name!="Substitute" and chance>=miss and y.ability not in ["Magic Bounce","Leaf Guard","Comatose","Vital Spirit","Insomnia"] and y.status=="Alive" and x.ability!="Sheer Force" and y.hp>0:
        if y.item!="Covert Cloak" or y.ability not in ["Shield Dust"]:
            y.status="Sleep"
            em.add_field(name="Status:",value=f"{y.nickname} fell asleep!")
            if y.ability=="Early Bird":
                y.sleepturn=random.randint(2,3)
            elif y.ability!="Early Bird":
                y.sleepturn=random.randint(2,5)
    if chance>=miss and y.status=="Sleep" and y.ability in ["Synchronize"] and x.status=="Alive":
        x.status="Sleep"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} fell asleep!")
        if x.ability=="Early Bird":
            x.sleepturn=random.randint(2,3)
        elif x.ability!="Early Bird":
            x.sleepturn=random.randint(2,5)   
    if chance>=miss and y.ability in ["Magic Bounce"] and x.status=="Alive" and y.status!="Sleep":
        x.status="Sleep"
        em.add_field(name=f"{y.icon} {y.nickname}'s {y.ability}!",value=f"{x.nickname} fell asleep!")
        if x.ability=="Early Bird":
            x.sleependturn=random.randint(2,3)
        elif x.ability!="Early Bird":
            x.sleependturn=random.randint(2,5)
#confusion
async def confuse(em,x,y,ch):
    miss=100-ch
    if x.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if y.name!="Substitute" and chance>=miss and y.confused is False and x.ability!="Sheer Force" and y.ability not in ["Own Tempo"] and y.status!="Sleep":
        em.add_field(name="Status:",value=f"{y.nickname} became confused!")
        y.confused=True
        y.confuseendturn=random.randint(2,5)            
#flinch
async def flinch(em,x,y,ch):
    miss=100-ch
    if x.ability=="Serene Grace":
        miss/=2
    chance=random.randint(1,100)
    if y.name!="Substitute" and (chance>=miss and y.ability not in ["Inner Focus"] and x.ability!="Sheer Force") and y.hp>0:
        if miss==0  and (y.item!="Covert Cloak" or y.ability not in ["Shield Dust"]):
            y.flinched=True        
#Berry            
async def berry(em,y,x,xhp,yhp,turn):
    if y.hp<=(y.maxhp/4)  and yhp>(y.maxhp/4):
      if y.item=="Lansat Berry" and x.ability not in ["Unnerve","As One"]:
          if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
              y.hp+=(y.maxhp/3)
          em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s critical hit ratio!")
          n=4
          if y.ability=="Ripen":
              n=8
          y.critrate*=n
          y.item+="[Used]"
      if y.item=="Ganlon Berry" and x.ability not in ["Unnerve","As One"]:
          if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
              y.hp+=(y.maxhp/3)
          em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Special Defense!")
          n=1
          if y.ability=="Ripen":
              n=2
          await defchange(em,y,x,n)
          y.item+="[Used]"
      if y.item=="Apicot Berry" and x.ability not in ["Unnerve","As One"]:
          if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
              y.hp+=(y.maxhp/3)
          em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Special Defense!")
          n=1
          if y.ability=="Ripen":
              n=2
          await spdefchange(em,y,x,n)
          y.item+="[Used]"
    if y.item=="Maranga Berry" and y.atkcat=="Special" and x.hp!=xhp:
          if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
              y.hp+=(y.maxhp/3)
          em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Special Defense!")
          n=1
          if y.ability=="Ripen":
              n=2
          await spdefchange(em,y,x,n)
          y.item+="[Used]"
    if x.use not in typemoves.statusmove:
        if y.item=="Jaboca Berry" and y.atkcat=="Physical" and x.hp!=xhp:
            if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                y.hp+=(y.maxhp/3)
            em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} damaged {x.nickname}!")
            x.hp-=round(x.maxhp/8)
            y.item+="[Used]"
        if y.item=="Rowap Berry" and y.atkcat=="Special" and x.hp!=xhp:
            if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                y.hp+=(y.maxhp/3)
            em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} damaged {x.nickname}!")
            x.hp-=(y.maxhp/8)
            y.item+="[Used]"
        if y.item=="Kee Berry" and x.ability not in ["Unnerve","As One"]:
            if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                y.hp+=(y.maxhp/3)
            em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Defense!")
            n=1
            if y.ability=="Ripen":
                n=2
            await defchange(em,y,x,n)
            y.item+="[Used]"
    if (y.hp<=(y.maxhp/4)  and yhp>(y.maxhp/4)) or (y.ability=="Gluttony" and y.hp<=(y.maxhp/2) and yhp>(y.maxhp/2)):
        if y.item=="Liechi Berry" and x.ability not in ["Unnerve","As One"]:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Attack!")
              n=1
              if y.ability=="Ripen":
                  n=2
              await atkchange(em,y,x,n)
              y.item+="[Used]"
        if y.item=="Petaya Berry" and x.ability not in ["Unnerve","As One"]:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Special Attack!")
              n=1
              if y.ability=="Ripen":
                  n=2
              await spatkchange(em,y,x,n)
              y.item+="[Used]"
        if y.item=="Salac Berry" and x.ability not in ["Unnerve","As One"]:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Speed!")
              n=1
              if y.ability=="Ripen":
                  n=2
              await speedchange(em,y,x,n)
              y.item+="[Used]"
        if y.item=="Custap Berry" and y.speed<x.speed:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              y.priority=True
              y.item+="[Used]"
        if y.item=="Starf Berry" and x.ability not in ["Unnerve","As One"]:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              ss=random.randint(1,5)
              n=1
              if y.ability=="Ripen":
                  n=2
              if ss==1:
                  em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Attack!")
                  await atkchange(em,y,x,n)
              if ss==2:
                  em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Special Attack!")
                  await spatkchange(em,y,x,n)
              if ss==3:
                  em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Defense!")
                  await defchange(em,y,x,n)
              if ss==4:
                  em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Special Defense!")
                  await spdefchange(em,y,x,n)
              if ss==5:
                  em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.nickname}'s Speed!")
                  await speedchange(em,y,x,n)
              y.item+="[Used]"
        if y.item in ["Aguav Berry","Figy Berry","Ipapa Berry","Mago Berry","Wiki Berry"]:
                y.hp+=round(y.maxhp/3)
                em.add_field(name=f"{y.icon} {y.nickname}'s {await itemicon(y.item)} {y.item}!",value=f"{y.nickname} consumed it's {y.item} and restored some HP!")
                if y.item=="Wiki Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Adamant","Jolly","Careful","Impish"]:
                        pass
                        #confuse(y,y,turn,100)
                if y.item=="Ipapa Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Lonely","Mild","Gentle","Hasty"]:
                        pass
                        #confuse(y,y,turn,100)
                if y.item=="Aguav Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Naughty","Naive","Rash","Lax"]:
                        pass
                        #confuse(y,y,turn,100)
                if y.item=="Mago Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Brave","Quiet","Sassy","Relaxed"]:
                        pass
                        #confuse(y,y,turn,100)
                if y.item=="Figy Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Modest","Timid","Calm","Bold"]:
                        pass
                        #confuse(y,y,turn,100)
                y.item+="[Used]"                                                      