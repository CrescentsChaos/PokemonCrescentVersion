import random
from movelist import *
naturelist=("Hardy","Lonely","Adamant","Naughty","Brave", "Bold",'Docile','Impish','Lax','Relaxed' ,'Modest','Mild','Bashful','Rash','Quiet' ,'Calm','Gentle','Careful','Quirky','Sassy', 'Timid','Hasty','Jolly','Naive','Serious')
def stat_clac(stat,individual_value,effort_value,level,spst="None"):
	"Generates enhanced stats"
	if spst == "HP":
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+level+10)
	else:
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+5)
	return new_stat
def maxmovemaker(self,typem=typemoves):
    maxmove=[]
    gm="None"
    for i in self.moves:
        if i in typem.dragonmoves:
            gm="Max Wyrmwind"
            if "Duraludon" in self.name:
                gm="G-Max Depletion"
        if i in typem.normalmoves:
            gm="Max Strike"
            if self.ability=="Galvanize":
                gm="Max Lightning"
            if self.ability=="Aerilate":
                gm="Max Airstream"
            if self.ability=="Refrigerate":
                gm="Max Hailstorm"
            if self.ability=="Pixilate":
                gm="Max Starfall"
            if "Snorlax" in self.name:
                gm="G-Max Replenish"
            if "Meowth" in self.name:
                gm="G-Max Gold Rush"
            if "Eevee" in self.name:
                gm="G-Max Cuddle"
        if i in typem.steelmoves:
            gm="Max Steelspike"
            if "Copperajah" in self.name:
                gm="G-Max Steelsurge"
            if "Melmetal" in self.name:
                gm="G-Max Meltdown"
        if i in typem.fairymoves:
            gm="Max Starfall"
            if "Hatterene" in self.name:
                gm="G-Max Smite"
            if "Alcremie" in self.name:
                gm="G-Max Finale"
        if i in typem.rockmoves:
            gm="Max Rockfall"
            if "Coalossal" in self.name:
                gm="G-Max Volcalith"
        if i in typem.groundmoves:
            gm="Max Quake"
            if "Sandaconda" in self.name:
                gm="G-Max Sandblast"
        if i in typem.ghostmoves:
            gm="Max Phantasm"
            if "Gengar" in self.name:
                gm="G-Max Terror"
        if i in typem.grassmoves:
            gm="Max Overgrowth"
            if "Venusaur" in self.name:
                gm="G-Max Vine Lash"
            if "Flapple" in self.name:
                gm="G-Max Tartness"
            if "Appletun" in self.name:
                gm="G-Max Sweetness"
            if "Rillaboom" in self.name:
                gm="G-Max Drum Solo"
        if i in typem.poisonmoves:
            gm="Max Ooze"
            if "Garbodor" in self.name:
                gm="G-Max Malodor"
        if i in typem.psychicmoves:
            gm="Max Mindstorm"
            if "Orbeetle" in self.name:
                gm="G-Max Gravitas"
        if i in typem.electricmoves:
            gm="Max Lightning"
            if "Pikachu" in self.name:
                gm="G-Max Volt Crash"
            if "Toxtricity" in self.name:
                gm="G-Max Stun Shock"
        if i in typem.fightingmoves:
            gm="Max Knuckle"
            if "Machamp" in self.name:
                gm="G-Max Chi Strike"
        if i in typem.icemoves:
            gm="Max Hailstorm"
            if "Lapras" in self.name:
                gm="G-Max Resonance"
        if i in typem.statusmove:
            gm="Max Guard"
        if i in typem.watermoves:
            gm="Max Geyser"
            if "Drednaw" in self.name:
                gm="G-Max Stonesurge"
            if "Rapid" in self.name:
                gm="G-Max Rapid Flow"
            if "Inteleon" in self.name:
                gm="G-Max Hydrosnipe"
            if "Kingler" in self.name:
                gm="G-Max Foam Burst"
            if "Blastoise" in self.name:
                gm="G-Max Cannonade"
        if i in typem.bugmoves:
            gm="Max Flutterby"
            if "Butterfree" in self.name:
                gm="G-Max Befuddle"
        if i in typem.darkmoves:
            gm="Max Darkness"
            if "Grimmsnarl" in self.name:
                gm="G-Max Snooze"
            if "Single" in self.name:
                gm="G-Max One Blow"
        if i in typem.flyingmoves:
            gm="Max Airstream"
            if "Corviknight" in self.name:
                gm="G-Max Wind Rage"
        if i in typem.firemoves:
            gm="Max Flare"
            if "Charizard" in self.name:
                gm="G-Max Wildfire"
            if "Cinderace" in self.name:
                gm="G-Max Fireball"
            if "Centiskorch" in self.name:
                gm="G-Max Centiferno"
        maxmove.append(gm)
    return maxmove	
def moveset(moves):
    moves=eval(moves)
    result=[]
    while len(result)<4:
        x=random.choice(moves)
        if x not in result:
            result.append(x)
    return result            
class Pokemon:
    def __init__(self,name="MissingNo.",primaryType="???",nickname="No",secondaryType="???",teraType="???",level=100,nature="None",happiness=255,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,ability="Unknown,Known",moves="Moves,M,N,P,U",maxiv="No",shiny="No",sprite="url",backsprite="url",item="None",gender="None",tera="???",catchdate="Unknown"):
        self.name=name
        self.status="Alive"
        self.primaryType=primaryType 
        self.secondaryType=secondaryType
        self.teraType=teraType
        self.tera=tera
        if self.tera=="???":
            self.tera=random.choice([self.primaryType,self.secondaryType])
            if self.tera=="???":
                self.tera=self.primaryType
        self.level=level
        self.nature=nature
        if self.nature=="None":
            self.nature=random.choice(naturelist)
        self.happiness=happiness
        self.hp=hp
        self.nickname=nickname
        if self.nickname=="No":
            self.nickname=self.name
        self.atk=atk
        self.defense=defense
        self.spatk=spatk
        self.shield=True
        self.sword=False
        self.spdef=spdef
        self.maxend=-1
        self.protect=False
        self.speed=speed
        self.catchdate=catchdate
        self.maxhp=hp
        self.maxatk=atk
        self.maxdef=defense
        self.maxspatk=spatk
        self.maxspdef=spdef
        self.speed=speed
        self.hpiv=hpiv
        self.atkiv=atkiv
        self.defiv=defiv
        self.spatkiv=spatkiv
        self.spdefiv=spdefiv
        self.speediv=speediv
        self.hpev=hpev
        self.atkev=atkev
        self.defev=defev
        self.spatkev=spatkev
        self.spdefev=spdefev
        self.speedev=speedev
        self.hpb=0
        self.atkb=0
        self.defb=0
        self.spatkb=0
        self.spdefb=0
        self.speedb=0
        self.atktime=0
        self.critrate=1
        self.confuseeendturn=0
        self.use="None"
        self.perishturn=0
        self.charged=False
        self.bullrush=False
        self.yawn=False
        self.flinched=False
        self.precharge=False
        self.confused=False
        self.recharge=False
        self.flashfire=False
        self.tarshot=False
        self.grav=False
        self.choiced="None"
        self.priority=False
        self.atktype="???"
        self.atkcat="???"
        self.ability=ability
        self.totaliv=round(((self.hpiv+self.atkiv+self.defiv+self.spatkiv+self.spdefiv+self.speediv)/186)*100,2)
        self.totalev=(self.hpev+self.atkev+self.defev+self.spatkev+self.spdefev+self.speedev)
        self.ability=random.choice(self.ability.split(","))
        self.gender=gender
        self.gender=random.choice(self.gender.split(","))
        self.sprite=sprite
        if self.name in ["Jellicent","Pyroar","Unfezant","Meowstic","Xatu","Wobbuffet","Ambipom","Basculegion","Beautifly","Bibarel","Blaziken","Cacturne","Camerupt","Donphan","Dustox","Floatzel","Garchomp","Heracross","Hippowdon","Houndoom","Indeedee","Kricketune","Ledian","Ludicolol","Lumineon","Luxray","Mamoswine","Medicham","Meganium","Milotic","Octillery","Oinkologne","Pachirisu","Pikachu","Politoed","Quagsire","Raticate","Relicanth","Rhydon","Rhyperior","Scizor","Scyther","Shiftry","Staraptor","Steelix","Sudowoodo","Swalot","Tangrowth","Toxicroak","Ursaring","Weavile"] and self.gender=="Female":
            self.sprite=self.sprite.replace(".gif","-f.gif")
        self.backsprite="http://play.pokemonshowdown.com/sprites/ani-back/"+self.sprite.split("/")[-1]
        self.moves=moves
        self.moves=moveset(self.moves)
        self.maxmoves=maxmovemaker(self,typemoves)
        self.maxiv=maxiv
        self.shiny=shiny
        self.item=item
        if maxiv=="Alpha":
            if "Alpha" not in self.nickname and self.nickname==self.name:
                self.nickname="Alpha "+self.nickname
        if self.shiny=="Yes":
            self.sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/"+self.sprite.split("/")[-1]
            self.backsprite="http://play.pokemonshowdown.com/sprites/ani-back-shiny/"+self.sprite.split("/")[-1]
            if "Shiny" not in self.nickname and self.nickname==self.name:
                self.nickname="Shiny "+self.nickname                
        self.dmax=False
        calcst(self)
        if self.maxiv=="Yes":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,31,31,31
        elif self.maxiv=="Alpha":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=random.randint(15,31),random.randint(15,31),random.randint(15,31),random.randint(15,31),random.randint(15,31),random.randint(15,31)
        elif self.maxiv=="No":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31)             
    def natureboost(self):
        "Boosts stats according to nature"
        if self.nature in ["Bashful","Docile","Hardy","Quirky","Serious"]:
            pass
        if self.nature in ["Adamant","Brave","Lonely","Naughty"]:
            self.maxatk+=round(self.maxatk*0.1)
        if self.nature in ["Mild","Modest","Quite","Rash"]:
            self.maxspatk+=round(self.maxspatk*0.1)
        if self.nature in ["Adamant","Careful","Impish","Jolly"]:
            self.maxspatk-=round(self.maxspatk*0.1)
        if self.nature in ["Bold","Calm","Modest","Timid"]:
            self.maxatk-=round(self.maxatk*0.1)
        if self.nature in ["Bold","Relaxed","Lax","Impish"]:
            self.maxdef+=round(self.maxdef*0.1)
        if self.nature in ["Gentle","Hasty","Lonely","Mild"]:
            self.maxdef-=round(self.maxdef*0.1)
        if self.nature in ["Calm","Careful","Gentle","Sassy"]:
            self.maxspdef+=round(self.maxspdef*0.1)
        if self.nature in ["Lax","Naive","Naughty","Rash"]:
            self.maxspdef-=round(self.maxspdef*0.1)
        if self.nature in ["Jolly","Timid","Naive","Hasty"]:
            self.maxspeed+=round(self.maxspeed*0.1)
        if self.nature in ["Brave","Quite","Sassy","Relaxed"]:
            self.maxspeed-=round(self.maxspeed*0.1)
def calcst(self):
    "Calculates Stats"
    self.maxhp = stat_clac(self.hp,self.hpiv,self.hpev,self.level,"HP")
    self.maxatk = stat_clac(self.atk,self.atkiv,self.atkev,self.level)
    self.maxdef=stat_clac(self.defense,self.defiv,self.defev,self.level)
    self.maxspatk = stat_clac(self.spatk,self.spatkiv,self.spatkev,self.level)
    self.maxspdef = stat_clac(self.spdef,self.spdefiv,self.spdefev,self.level)
    self.maxspeed=stat_clac(self.speed,self.speediv,self.speedev,self.level)
    self.natureboost()
    self.hp=self.maxhp
    if self.name=="Shedinja":
        self.hp=self.maxhp=1
    self.maxtotal=self.maxhp+self.maxatk+self.maxdef+self.maxspatk+self.maxspdef+self.maxspeed
    