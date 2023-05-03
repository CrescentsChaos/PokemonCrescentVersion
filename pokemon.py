import random
naturelist=("Hardy","Lonely","Adamant","Naughty","Brave", "Bold",'Docile','Impish','Lax','Relaxed' ,'Modest','Mild','Bashful','Rash','Quiet' ,'Calm','Gentle','Careful','Quirky','Sassy', 'Timid','Hasty','Jolly','Naive','Serious')
def stat_clac(stat,individual_value,effort_value,level,spst="None"):
	"Generates enhanced stats"
	if spst == "HP":
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+level+10)
	else:
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+5)
	return new_stat
def moveset(moves):
    moves=eval(moves)
    result=[]
    while len(result)<4:
        x=random.choice(moves)
        if x not in result:
            result.append(x)
    return result            
class Pokemon:
    def __init__(self,name="MissingNo.",primaryType="???",nickname="No",secondaryType="???",teraType="???",level=100,nature="None",happiness=255,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,ability="Unknown,Known",moves="Moves,M,N,P,U",maxiv="No",shiny="No",sprite="url",backsprite="url",item="None",gender="None",tera="???"):
        self.name=name
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
        self.spdef=spdef
        self.speed=speed
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
        self.defenseb=0
        self.spatkb=0
        self.spdefb=0
        self.speedb=0
        self.ability=ability
        self.totaliv=round(((self.hpiv+self.atkiv+self.defiv+self.spatkiv+self.spdefiv+self.speediv)/186)*100,2)
        self.totalev=(self.hpev+self.atkev+self.defev+self.spatkev+self.spdefev+self.speedev)
        self.ability=random.choice(self.ability.split(","))
        self.gender=gender
        self.gender=random.choice(self.gender.split(","))
        self.sprite=sprite
        self.backsprite="http://play.pokemonshowdown.com/sprites/ani-back/"+self.sprite.split("/")[-1]
        self.moves=moves
        self.moves=moveset(self.moves)
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
    if self.dmax==True:
        self.hp*=2
        self.maxhp*=2
    if self.name=="Shedinja":
        self.hp=self.maxhp=1
    self.maxtotal=self.maxhp+self.maxatk+self.maxdef+self.maxspatk+self.maxspdef+self.maxspeed