class Trainer:
	def __init__(self,name="Billy",pokemons=[],region="Kanto",hazard=None,ai=False,lightscreen=False,reflect=False,auroraveil=False,faintedmon=[],tailwind=False,wishhp=False,vcdmg=False,vcturn=False,vcendturn=False,canmega=True,canmax=True,cantera=True,mon="None",future=0,ftmul=0,sub="None",winner=False,doom=0,item=[],sprite="Trainers/unknown.png",id=0,member="None"):
		self.name=name
		self.ai=ai
		self.winner=winner
		self.pokemons=pokemons
		self.cantera=cantera
		self.canmax=canmax
		self.member=member
		self.id=id
		self.future=future
		self.doom=doom
		self.sprite=sprite
		self.ftmul=ftmul
		self.sub=sub
		self.faintedmon=faintedmon
		self.lightscreen=lightscreen
		self.reflect=reflect		
		self.mon=mon
		self.canmega=canmega
		self.tailwind=tailwind
		self.auroraveil=auroraveil
		self.region=region
		self.reflecturn=0
		self.wishhp=wishhp
		self.tailturn=0
		self.auroraturn=0
		self.lsturn=0
		self.vcdmg=vcdmg
		self.vcturn=vcturn
		self.vcendturn=vcendturn
		self.screenend=self.lsturn+6
		self.twendturn=self.tailturn+4
		self.rfendturn=self.reflecturn+6
		self.avendturn=self.auroraturn+6
		self.item=item
		if self.item==[]:
		    self.item=["Full Restore","Full Restore","Full Restore"]
		if hazard is None:
		    self.hazard=[]
		else:
		    self.hazard=hazard   
	def lightscreenend(self,mon,mon2):
	       if "Light Clay" not in (mon.item,mon2.item):
	           self.screenend=self.lsturn+6
	       if "Light Clay" in (mon.item,mon2.item):
	           self.screenend=self.lsturn+9
	       return self.screenend
	       
	def reflectend(self,mon,mon2):
	       if "Light Clay" not in (mon.item,mon2.item):
	           self.rfendturn=self.reflecturn+6
	       if "Light Clay" in (mon.item,mon2.item):
	           self.rfendturn=self.reflecturn+9
	       return self.rfendturn
	       
	def auroraend(self,mon,mon2):
	       if "Light Clay" not in (mon.item,mon2.item):
	           self.avendturn=self.auroraturn+6
	       if "Light Clay" in (mon.item,mon2.item):
	           self.avendturn=self.auroraturn+9
	       return self.avendturn
	def twend(self,mon,mon2):
	    self.twendturn=self.tailturn+4
	    return self.twendturn         
