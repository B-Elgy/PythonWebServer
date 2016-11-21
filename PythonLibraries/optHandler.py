__all__=["Scanner"]
class OptScanner:
	__all__=["__init__","scan"]
	def __init__(self, firstFlag=True, flagsNeedArgs=True):
		self.flags=list()
		self.args=list()
		self.opts=dict()
		self.firstFlag=firstFlag
		self.flagsNeedArgs=flagsNeedArgs

	def scan(self,argv):
		#Modes: 1-Extended Option 2-Normal Option 3-Normal Option Already Filled
		mode=None
		for k in argv:
			if(k[0]=="-"):
				#Flag
				if(mode==2 and not self.flagsNeedArgs):
					#No Argument For Flag, None Required
					self.args.append("")
				if(mode==2 and self.flagsNeedArgs):
					#No Argument For Flag, Required
					assert False, "ERROR: Arguments Required For All Options"
				self.flags.append(k)
				if(k[1]=="-"):
					#Extended Option Flag
					self.args.append(list())
					mode=1
				else:
					#Normal Flag
					mode=2
			else:
				#Argument
				if(mode==1):
					#Extended Option Argument
					self.args[len(self.flags)-1].append(k)
				elif(mode==2):
					#Normal Option Argument
					self.args.append(k)
					mode=3
				elif(mode==3):
					#ERROR: Normal Option Argument Already Filled
					assert False, "ERROR: Normal Option Argument Already Filled, As Option " + str(len(self.flags)) + " You Put " + str(k) +\
					"Normal Options Can Only Have One Argument"
				elif(mode==None and self.firstFlag):
					#ERROR: First Input Must Be Flag (Unless Specified By First Flag Parameter (firstFlag) In Constructor)
					assert False, "ERROR: First Argument Must Be A Flag"
				else:
					#ERROR: Unknown Error Occured
					assert False, "ERROR: Unknown Error Occured While Scanning Options"
			
		if(len(self.flags)!=len(self.args) and self.flagsNeedArgs):
			#ERROR: Different Number Of Flags And Arguments, All Flags Must Have Arguments (Unless Specified By Flags Need Arguments
			#Parameter (flagsNeedArgs) In Constructor)
			assert False, "ERROR: Different Number Of Flags And Arguments"
		if(len(self.flags)!=len(self.args) and not self.flagsNeedArgs):
			#Unequal, Args not required
			self.args.append("")

		for i in range(len(self.flags)):
			self.opts[self.flags[i]]=self.args[i]

	def __clear__(self): #For Testing Purposes Only
		self.args=list()
		self.flags=list()
		self.opts=dict()

	def __settings__(self, firstFlag=True, flagsNeedArgs=True): #For Testing Purposes Only
		self.firstFlag=firstFlag
		self.flagsNeedArgs=flagsNeedArgs




					

