#py:python_OS_win_linux_shell_cmd
__doc__ = """
Cybele by AS for www.adelinosaldanha.site ✦

# This Python script is licensed under the GNU General Public License, version 2.
# See the LICENSE file for more details: https://www.gnu.org/licenses/gpl-2.0.en.html
"""
integrty = '0x21fab1a'
version = '0.5 βeta'
_title_ = 'Cybele'
_pcnode_ = ['LAPTOP','DESKTOP']
_spchar_ = '⚝〉“”—❛❜↺心'
_active_ = '01.08.2024'
_revise_ = '30.04.2025'
_author_ = 'Adelino Saldanha'
_auth1r_ = _author_.split()[0]
_cyext_ = " extention"
_pyver_ = '3.13.2'
_cybid_ = False

try:
	import random
	import sys,os
	import math,re
	import datetime
	import time
	import platform
	from platform import python_version
	from time import gmtime, strftime, sleep
	from datetime import date, datetime, time, timedelta
	from math import degrees as deg, radians as rad
	from math import floor, ceil, pi, atan, tan, sin, asin, cos, acos

except ImportError as err:
	match = re.search(r"'(.*?)'", str(err))
	if match:
		module_name = match.group(1)
		modname = str(err) + "\n   I cannot execute properly. Exiting. \n   Try in Console: pip install " + module_name
	else:
		modname = str(err) + "\n   I cannot execute properly. Exiting."
	print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
	exit()

node_name = platform.node()
if node_name:
	sysos = platform.system()
	sysver = sys.hexversion
	if platform.node().lower() in [node.lower() for node in _pcnode_]:
		addcomm = []
		extvars = []
		try:
			import cybext
			import urllib.request
			_cybid_ = True
			_cyext_ = _cyext_.replace(_cyext_[0:4],_cyext_[0:4].upper())
			addcomm = cybext.addcommands()
			extvars = cybext.extinternal_vars()
		except ImportError:
			_cybid_ = False

#-----------------------------------------------------------
chkcyb = "Ngtnmahkbsxw Fhwbybvtmbhg Wxmxvmxw.\n    Kxlixvmbgz max tnmahk'l vhgmkbunmbhgl bl yngwtfxgmte mh max ikbgvbiexl hy hixg-lhnkvx wxoxehifxgm.\n    Xqbmbgz."
year_months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
aboutyou = "B'f t wbghltnk bg t mxva tzx, unm B'f lmbee xqxvnmbgz fr vhwx yetpexller."
days_till_today = date.today() - date(year=int(_active_[6:]), month=int(_active_[3:5]), day=int(_active_[0:2]))
iknow_pun = {"i know": "you know","you know": "i know"}
cybchk = int(str(ord("\x0f")) + str(ord("\x1c")));chkauth = sum(ord(char) for char in _author_)
month_name = date.today().strftime('%B');next_year = str(date.today().year + 1);weekdaydate = date.today().weekday()
_poigps_=[39.4487,-8.0376,0,0,0];shift=int(_poigps_[0]+6);gamescore=[-1,0,0];actions_for_today=[];action_for_digi=[]

#-----------------------------------------------------------
website = {
	"home": "https://www.adelinosaldanha.site",
	"mystory": "https://www.adelinosaldanha.site/mystory",
	"may4th" : "https://dub.sh/1vgai8g",
	"tvshow": "https://www.adelinosaldanha.site/tvshows",
	"thamix": "https://www.adelinosaldanha.site/thamix",
	"deserted": "https://www.adelinosaldanha.site/deserted",
	"trails": "https://www.adelinosaldanha.site/trails",
	"cybele": "https://kernelx64.trinket.io/sites/cybele",
	"trakt": "https://simkl.com/4378279/tv/watching/",
	"solar": "https://kernelx64.trinket.io/sites/solarsystem",
	"symbad": "https://simbad.cds.unistra.fr/simbad/sim-id?output.format=ASCII&Ident="
}
webshare = {
  "tvshow": "Maxkx bl vnkkxgmer gh latkbgz bgyhkftmbhg.",
  "movies": "Maxkx bl vnkkxgmer gh latkbgz bgyhkftmbhg.",
  "art of sight": "ammil://ppp.twxebghltewtgat.lbmx/wot"
}
presence_online = {
	"online": "Visit www.adelinosaldanha.site/mystory to view all my online presence services."
}

#-----------------------------------------------------------
as_quotes = [
	"... to keep you busy.",
	"The time i like to waist is not wasted time, never was and never gonna be.",
	"Nature don't need our protetion just our absence.",
	"In order to instigate revolutionary change we must transform human conscienence.",
	"Nature does not make mistakes.",
	"If Nature isn't kept healthy, humans won't survive. Simple as that and let's face'it, nature is already scruded. The question is whether it is possible for us to have a future.",
	"Extreme weather events, rising sea levels, and the loss of biodiversity are already devastating communities around the world. We are witnessing the consequences of our inaction in real-time.",
	"Who needs Hugh Hefner others and alike's when you've got free, low-res internet gratification? #PlayboyPastItsPrime",
	"We dream of mansions, yet find true contentment in tiny houses. We strive for the space, and we all endup to a six-foot plot. Perhaps it’s time to reconsider what truly matters.",
	"Next time you find yourself feeling curious, embrace it. Let it lead you on a journey of discovery, self-reflection, and growth. You might be surprised at where it takes you. Don't blame me if ...",
	"Um Portugal sem aldeias é um país que perde a alma, um mapa demográfico em branco e compromete o futuro, perdendo a memória e as raízes que o geraram e o fortalecem. Creio que muitos não perceberam que aldeias sem gente são o fim de um tempo que não volta. Morrem as aldeias e morre uma parte do que somos. As nossas aldeias são um tesouro a ser, preservado, e valorizado.",
	"From shale villages to abandoned places, including picturesque houses and pure nature, from the interior to the coast there are destinations here that are true 'treasures' and, quite simply. That's why I've always preferred places of this scope and not mass, trendy destinations and alike's, because after all, even the little things define us.",
	"I am sorry if you don't like my honesty, but to be fair i dont give a fuck.",
	"Somethings just cannot be fixed. Sometimes wore mented to not. Somethings lost are lost forever. No matter how hard we fight, How much it hurts.",
	"In memory of the 90s, that beloved era, a special time for many.",
	"Oh! Just bite me, like the Terminator: I can be old but i'm not obsolete."
]
#-----------------------------------------------------------
kolor = {
    'WHITE': '\033[1;37m','YELLOW': '\033[1;33m','GREEN': '\033[1;32m','BLUE': '\033[1;34m','CYAN': '\033[1;36m',
    'RED': '\033[1;31m','MAGENTA': '\033[1;35m','BLACK': '\033[1;30m','DARK_WHITE': '\033[0;37m','DARK_YELLOW': '\033[0;33m',
    'DARK_GREEN': '\033[0;32m','DARK_BLUE': '\033[0;34m','DARK_CYAN': '\033[0;36m','DARK_RED': '\033[0;31m',
	'DARK_MAGENTA': '\033[0;35m','DARK_BLACK': '\033[0;30m','OFF': '\033[0;0m'
}
#--------------------------
art_world = [
	[32,32,32,32,32,32,32,32,32,32,32,32,95,44,45,45,39,44,32,32,32,95,46,95,46,45,45,46,95,95,95,95,95,32],
	[32,32,32,32,32,46,45,45,46,45,45,39,59,95,39,45,46,39,44,32,39,59,95,32,32,32,32,32,32,95,46,44,45,32],
	[32,32,32,32,46,39,45,45,39,46,32,32,95,46,39,32,32,32,32,123,96,39,45,59,95,32,46,45,46,62,46,39,32,32],
	[32,32,32,32,32,32,32,32,32,32,39,45,58,95,32,32,32,32,32,32,41,32,32,47,32,96,39,32,39,61,46,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,41,32,62,32,32,32,32,32,123,95,47,44,32,32,32,32,32,47,126,41,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,124,47,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,96,94,32,46,32]
]
art_cybele = [
	[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,95,95,95,46,32,32,32,32,32,32,32,32,32,32,32,32,46,95,95,32],
	[32,32,32,95,95,95,32,32,95,95,95,46,95,95,46,92,95,32,124,95,95,32,32,32,32,95,95,95,95,32,32,124,32,32,124,32,32,32,32,95,95,95,95,32],
	[95,47,32,95,95,95,92,60,32,32,32,124,32,32,124,32,124,32,95,95,32,92,32,95,47,32,95,95,32,92,32,124,32,32,124,32,32,95,47,32,95,95,32,92],
	[92,32,32,92,95,95,95,32,92,95,95,95,32,32,124,32,124,32,92,95,92,32,92,92,32,32,95,95,95,47,32,124,32,32,124,95,95,92,32,32,95,95,95,47],
	[32,92,95,95,95,32,32,62,47,32,95,95,95,95,124,32,124,95,95,95,32,32,47,32,92,95,95,95,32,32,62,124,95,95,95,95,47,32,92,95,95,95,32,62],
	[32,32,32,32,32,92,47,32,92,47,32,32,32,32,32,32,32,32,32,32,92,47,32,32,32,32,32,32,92,47,32,32,32,32,32,32,32]
]
art_py = ["\n          \033[1;34m.XXXXX.\033[m         ","         \033[1;34mXX XXXXXX\033[m        ",
	"         \033[1;34m''""XXXXX\033[m        ","   \033[1;34m.XXXXXXXXXXXXXX\033[m \033[1;33mXXXX.\033[m  ",
	"  \033[1;34m.XXXXXXXXXXXXXXX\033[m \033[1;33mXXXXX.\033[m ","  \033[1;34m'XXXXX\033[m \033[1;33mxxxxxxxxxxXXXXX'\033[m ",
	"   \033[1;34m'XXXX\033[m \033[1;33mXXXXXXXXXXXXXX'\033[m  ","         \033[1;33mXXXXX....\033[m        ",
	"         \033[1;33mYXXXXX XY\033[m        ","          \033[1;33m'YXXXY'\033[m         \n"
]
art_kx64 = [98,121,32,107,101,114,110,101,108,120,54,52]
art_byas = [98,121,32,65,83]
#------------------------------------------------------------
csugestions = []; chkdict = []
#------------------------------------------------------------
core = {
	"greatings":	["good morning","good evening","good afternoon","good night","hi good morning","hello good morning","hi good evening",
					"hello good evening","hi good afternoon","hello good afternoon","hi good night","hello good night","hi there","hello there",
					"greatings","greatings good morning","greatings good afternoon","greatings good night","greatings good evening"],
	"negative_word": ["not","never","none","nothing","nobody","nowhere","neither","difficult","impossible","incorrect","wrong","bad","terrible","dont","dont't"],
	"badword":	["arse","arsehead","arsehole","ass","ass hole","asshole","bastard","bitch","bloody","bollocks","brotherfucker","bugger",
				"bullshit","child-fucker","cock","cocksucker","crap","cunt","dammit","damn","damned","damn it","dick","dick-head","dickhead",
				"dumb-ass","dumbass","dyke","father-fucker","fatherfucker","frigger","fuck","fucker","fucking","goddammit","goddamn","goddamned",
				"godsdamn","holyshit","horseshit","in shit","jack-ass","jackarse","jackass","wept","kike","mother fucker","mother-fucker",
				"motherfucker","nigga","nigra","pigfucker","piss","prick","pussy","shit","shit ass","shite","sibling fucker","sisterfuck",
				"sisterfucker","slut","son of a bitch","son of a whore","spastic","sweet jesus","fag","cum","blowjob",
				"retard","retarded","whore","wtf","fool","bull","loser","fuckface","ass-wipe","goat","goat banger","faggot","blockhead","jinx"],
	"spring":	["march","april","may"],
	"summer":	["june","july","august"],
	"autumn":	["september","october","november"],
	"winter":	["december","january","february"],
	"seasons":	["spring", "summer", "autumn", "winter"],
	"primary moon phase":	["new moon","first quarter","full moon","last quarter"],
	"secondary moon phase":	["waxing crescent","waxing gibbous","waning gibbous","waning crescent"],
	"day of the week":	["monday","tuesday","wednesday","thursday","friday","saturday","sunday"],
	"months":	["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"],
	"year event":	["christmas","new year","new yearseve","birthday","my birthday"],
	"planet":	["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus" , "neptune"],
	"day period":	["morning","afternoon","night","evening"],
	"orbital regime":	["geo","igo","ego","nso","gto","meo","gho","leo","hao","mgo","heo","lmo","ufo","eso"],
	"time unit":	["second","seconds","minutes","minute","hour","hours","day","days"],
	"messure factor": ["feets","miles","yards","m3","gallons","fahrenheit"],
	"exitmsg":	['It was a pleasure.','Until next time!.','Until we meet again!','Looking forward.','Have a good one.','Take care.',
				'Catch you later!','Peace Out.','Farewell.'],
	"intromsg":	["Welcome.","Greeatings.","Entertain.","Glad you're here!","Delighted to have you!","Fantastic to see you!",
				"Awesome you're here!","Stoked you're here!","Pleasure to have you!","Delighted to welcome you!","Is a privilege to host you!"],
	"cthemes":	["I know about","Let's explore the together about","Based on my offline knowledge","You can ask me about",
				"If you are curious you can ask'me about","I can anwser questions about","I can share knowledge about",
				"I can provide you answers about","I can tell you about","I have knowledge about"],
	"out":	["exit","quit",":x",":q","x:","q:"],
	"question_words":	["who", "what", "where", "when", "why", "can", "whose", "which"], #"how"],
	"askard_command":	["list askard","view askard","show askard","achk askard","scan askard"],
	"working_hard":	["Cybele is taking a break right now. Please wait a moment and try again later."],
	"yodaw":	["Hmm. Nothing to transform, there is.","Empty, the input is.","Words, there are none.","Silence, I hear.",
				"Lost, the input is.","A void, it seems.","Speak, nothing does.","Unspoken, it remains.","Gone, all the words are."],
	"coded":	["py","python","python art"]
}
#-------------------------------------------------------------
chkdict.append(sum(sum(ord(char) for char in word) for value in core.values() for word in value))
#-------------------------------------------------------------
messages = {
	"activity_msg":	["We're serving up one year's worth of seasonal shenanigans, daily!","One year of seasons, squeezed into a single day. Time travel? Sort of.",
					"Daily dose of a year's worth of seasonal quirks.","Seasons? We've got a year of 'em, packed into each day!",
					"Ever wanted to experience a whole year of seasons in a day? We're showing one year per day.","Once a day. It's like a time machine, but with more leaves and snow.",
					"This program shows one year of seasonal activities... daily.","Please refrain from asking us to explain the space-time continuum."],

	"badword_msg":	["Whoa there, sailor! Watch your language!" , "Beep! Beep! Profanity detected!",
					"Language, please! We're trying to keep this PG-rated." , "Your mom would be disappointed.",
					"Is that really necessary? We can express ourselves without the colorful vocabulary.",
					 "I'm pretty sure that word isn't in the thesaurus under 'elegant'.",
					"You're speaking a language I don't understand... and I'm pretty sure I don't want to.",
					"I believe we call that 'adulting' and it's not going well." ,
					"Did you just channel your inner pirate? Because 'argh' is a perfectly acceptable alternative.",
					"I'm calling the language police. You're under arrest!",
					"Wow, that was deep. Really made me think about the complexities of the universe.",
					"I'm so glad you decided to share your inner poet with us.",
					"I'm learning so much about the English language today. Thanks!",
					"Your vocabulary is as vast as your knowledge of grammar.",
					"I'm impressed by your ability to convey such profound thoughts with such limited vocabulary."],

	"birthday_msg":	["I'm so glad you remembered! Thank you.","Woohoo! Thank you so much for the birthday wishes!",
					"I'm feeling the birthday love! Thanks!","You're the best! Thanks for the birthday greeting.",
					"Another year older, another year wiser...or so they say. Thanks for the birthday wishes!"
					"Well, this is my official aging announcement. Thanks for celebrating with me!",
					"Thank you. It really means alot coming from you, beside the important is -You Rememberered!",
					"Age is just a number, right? Thanks for helping me celebrate!",
					"Hey, thanks for the birthday wishes! I'm so glad we're friends.",
					"Your birthday wishes made my day brighter! Thanks!",
					"It means a lot coming from you. Thanks for the birthday greeting!"],

	"birthday_short":	["I'm so glad.","You remembered!","Ohh so sweet...","You're the best!","Hey, thanks.","It means a lot.",
						"I'm impressed.","Interesting!","You make'me dream!","I'm so ancious...","Woohoo! Thank you.",
						"I feel your love!","I'm feeling the love","My day geted brighter!","Your wishes made'me...",
						"Another year wiser!","Another year older.","So they say...","Coming from you...","Age is just a number."],

	"creative matter":	["Interesting! %s definitely has a vibe of %s." , "You're right, '%s' does have a strong %s feel to it.",
						"That's a great point! The word '%s' certainly evokes %s imagery." , "I can see why you think that. '%s' does seem like a very %s word.",
						"The word %s belongs to the %s based on my general knowledge." , "The word '%s' gives me a distinct %s impression.",
						"I associate '%s' with a %s atmosphere." , "The connotation of '%s' is definitely %s." , "'%s' has a strong %s undertone.",
						"I would describe '%s' as undeniably %s." , "The word '%s' carries a %s essence." , "'%s' evokes a %s mood in me.",
						"I find '%s' to be quintessentially %s." , "The word '%s' is synonymous with %s." , "The feeling I get from '%s' is %s.",
						"I would categorize '%s' as a %s word." , "'%s' has a clear %s quality." , "The word '%s' is undeniably %s in nature.",
						"I'm drawn to the %s aspect of '%s'." , "The word '%s' has a strong %s connotation." , "I associate '%s' with a %s sense of being.",
						"The word '%s' is full of %s energy." , "I perceive '%s' as having a %s aura." , "The word '%s' is a perfect example of %s.",
						"I would characterize '%s' as deeply %s." , "The word '%s' has a %s flavor." , "I find '%s' to be very %s-like.",
						"The word '%s' is reminiscent of %s." , "I associate '%s' with a %s experience." , "The word '%s' has a %s impact on me.",
						"I would describe '%s' as %s-inspired." , "The word '%s' is a %s concept." , "I find '%s' to be a very %s term.",
						"The word '%s' is full of %s possibilities." , "I perceive '%s' as a %s phenomenon." , "The word '%s' is a %s expression.",
						"I would characterize '%s' as a %s idea." , "The word '%s' is a %s concept." , "I find '%s' to be a very %s term.",
						"The word '%s' is full of %s possibilities." , "I perceive '%s' as a %s phenomenon." , "The word '%s' is a %s expression."],

	"earlier_nyear":	["You're a little early, but thanks for the optimism!", "New Year's cheer eariler!? I like your style!",
					"Hold that thought! We've got a few time to go.", "Woah there, partner! Let's not get ahead of ourselves.",
					"Is it December already? Time flies when you're having fun!", "You're officially the most prepared person I know.",
					"Happy New Year to you too! But... Are we there allready?", "You've got great timing for the future!"],

	"enjoying": ["Currently enjoying ", "Enjoying at the moment " ,"Right now, I'm loving ","In the middle of enjoying ","Just enjoying some ",
                "Having a great time with ","Really digging ", "is really hitting the spot right now.", "Currently immersed in ", "I am presently enjoying ",
                "At this moment, I am enjoying ", "I am taking pleasure in ","I am finding great enjoyment in ","This very moment, I'm enjoying ", "In this instant, I'm relishing "],

    "endterm":	["For now" , "In the meantime" , "For the time being" , "Temporarily" , "Until further notice" , "Presently" , "Currently" , "As of now" , "At this point" , "For the moment"],

	"game_messages":	["Whoa, hold your horses!" , "Can you slow down? My brain's overheating!" , "This is mind-boggling!" , "No way, José!" ,
						"I'm having a meltdown!" , "You're on fire!" , "My jaw dropped." , "Are you kidding me?" , "I think i have a bug...",
						"Dude, what just happened?" , "This is crazy town!" , "I'm not even mad, I'm impressed.", "You're out of this world!",
						"I'm speechless." , "This is blowing my mind." , "I'm having a moment." , "That's next level." , "My brain just exploded.",
						"You are so fast i didn't not have time to process!" , "Aliens, maybe?" , "Did I just witness magic?", "Pinch me, I must be dreaming!",
						"This is a rollercoaster of emotions." , "My inner child is freaking out." , "This is beyond science." , "My reality is questioned."],

	"gamereset":	["Is this Groundhog Day or something?" , "I'm starting to feel like a broken record." , "Attempt number... who knows?",
					"This is getting ridiculous." , "I'm beginning to question my life choices." , "I'm officially a professional at failing at this.",
					"If at first you don't succeed, try, try again... and again... and again..." , "I'm pretty sure I've mastered the art of failure by now.",
					"I'm beginning to question my life choices." , "This is like trying to herd cats, but less cute." , "I'm starting to think this is a conspiracy."],

	"gamereset_msg":	["Let's start over." , "New game, new chance." , "Back to zero." , "Fresh start." , "Let's do this again.",
						"Okay, let's see who can pull ahead now!" , "Alright, here we go again!" , "New score, new possibilities!",
						"Let's shake things up!" , "It's anyone's game now." , "Let's see who can dominate this round.",
						"Time to turn the tables."],

	"magic_anwser":	["Haha, you're asking for some magic, aren't you? Just type the %s directy...\n",
					"Way so many formalities! Just type directly the %s and see the magic happen!.\n",
					"While I can't pull a real rabbit out of a hat i can tell you about %s if you type directly.\n",
					"I can't pull a planet out of thin air!, I can definitely help you in %s if you type directly.\n",
					"Think of me as a magical library full of %s knowledge, waiting to be unleashed! Type directly!.\n"],

	"newyear_msg":	["Cheers to a new beginning!","Wishing you a fantastic year ahead.","Let's make " + next_year + " unforgettable!",
					"Grateful for another year with you. Happy New Year!", "You're the best part of my year. Can't wait to make more memories with you.",
					"Here's to a year filled with love, laughter, and endless possibilities.", "Looking forward to another year of adventures with you. Happy New Year!",
					"Thank you for being a part of my life. Happy New Year!", "Embrace the unknown and create your own magic. Happy New Year!",
					"I'm not sure what the new year holds, but I'm hoping it includes less Monday mornings. Happy New Year!",
					"I resolved to eat more chocolate this year. Anyone want to join me? Happy New Year!",
					"Let's make a pact to only make good decisions this year... or at least try. Happy New Year!",
					"I'm ready to hit the reset button and start fresh. Happy New Year!", "I'm not sure what's ahead, but I'm bringing snacks. Happy New Year!",
					"New year, new you. Let's make it count!", "Believe in yourself and great things will happen. Happy New Year!",
					"Let's turn our dreams into reality. Happy New Year!", "It's a new chapter. Write a good one.","Here's to a brighter future!"],

	"notchristmas":	["Wow, you're really getting a head start on the holiday season!","I'm still recovering... Maybe you can lend me your time machine?",
					"Merry Christmas to you too! Just kidding, it's "+month_name+"!.","Thanks for the early holiday cheer.",
					"I'll try to save it for later.","Is this a new kind of time travel?","I'm definitely not ready for snow and eggnog yet.",
					"Let's stick to ice cream and sunshine, okay?","You must be on the naughty list for starting Christmas so early.",
					"Don't worry, I'll keep your secret.","Hold your reindeer! It's still too hot for jingle bells.",
					"Let's enjoy this beautiful "+month_name+" weather first."],

	"notvalentines": ["It's so sweet of you to think ahead! Can't wait to celebrate Valentine's Day with you.",
					"Aww, that's so thoughtful! I'm looking forward to our Valentine's Day together.",
					"You're such a romantic! I'll be thinking of you on Valentine's Day.",
					"That's a great reminder! I'm excited to celebrate with you.",
					"You're always one step ahead! Thanks for the early Valentine's Day wishes."],

	"valentinesmsg": ["Happy Valentine's Day! You're the apple of my eye.","Sending you lots of love and warm hugs this Valentine's Day.",
					"Thinking of you on this special day. You're the sweetest.","You make my heart skip a beat. Happy Valentine's Day!",
					"Roses are red, violets are blue, you're the one for me, through and through.","Sending you a virtual hug and a kiss. Happy Valentine's Day!",
					"You brighten my world. Happy Valentine's Day, my love.","I'm so lucky to have you in my life. Happy Valentine's Day!",
					"Here's to many more Valentine's Days together.","You're the missing piece to my puzzle. Happy Valentine's Day!"],

	"notplanet":	["Alien technology detected. Trying to locate %s planet...\n","You've discovered a new planet %s! Congratulations, explorer!\n",
					"Planet %s not found. Did you mean 'Planet Hoth'?\n","Error 404: Planet %s not found. Please try searching for %s again.\n",
					"That planet sounds like a great sci-fi novel, %s!\n","Well, the %s cristal ball gonna show the planet's name i presume...\n",
					"%s is not a planet name from our solar system.\n","I must be in another galaxy cos %s is not a planet name arround here!\n"],

	"notgood_lino":	["You've really messed this up, %s","%s, that was a stupid thing to do.","%s, you're an idiot.",
					"%s, I'm disappointed in your decision.","That wasn't very clever, %s","%s, that's so bad, it's almost good.",
					"You're not exactly Einstein, are you %s?"],

	"not_right":	["Something is not right about this situation." , "There's something amiss; something is not right.",
					"I have a feeling something is not right here." , "Something just doesn't seem right to me.",
					"Something's off.","There's something fishy going on." , "This doesn't add up.","I sense something's wrong.",
					"This situation is suspicious." , "This is not sitting right with me.", "There's an undercurrent of unease.",
					"Something feels out of place." , "This doesn't feel right.", "I have a bad feeling about this.",
					"There's a discrepancy here." , "An anomaly exists within this situation.", "This matter is shrouded in irregularity.",
					"A sense of impropriety pervades the atmosphere."],

	"nostar_message":	["Lost in space? Give me a star to aim for!","Stargazing without a star? That's like fishing without a hook!",
					"Where's the star, dude? I need something to shine on!","You want me to find a needle in a haystack, but without the haystack?",
					"I'm not a magical genie. You gotta give me a star to rub!","My crystal ball is cloudy without a star name. Try again!",
					"Are you trying to summon a random space rock? Be more specific!","You expect me to channel my inner astrologer with nothing but empty space?",
					"I'm not a cosmic detective. Give me a clue!","I'm not a mind reader, you know!"],

	"math_msg":	["What! e,m or h brain's on fire? Use ice, cream or sleep!","If it's allready hard use e,m or h, Math Quiz!?, gonna be Einscharged!.",
				"e,m or h, not e=mc2 and allready is a problem? Use magic, coffee or nap!","Life's tough? Choose chill, grill or spill!",
				"Need a vacation allready? Visit Mars, Jupiter or Venus!","Feeling overwhelmed by e,m or h? Try yoga, nap or laugh!",
				"Stressed about e,m or h choice? Blame aliens, cats or dreams!"],

	"trouble_msg": ["We've got a situation here." , "This is not good." , "We've hit a snag." , "Hoston we have a problem.",
					"We hit a problemo." , "I think we've got a problem." , "We're in trouble." , "Mayday, mayday!" , "All hands on deck!"],

	"trouble_short":	["Ah-oh.","Uh-oh.","Oops.","Yikes.","Oh dear.","Crikey!","Darn it.","Holy!","Whoa!","Ouch!","Gulp!","Blimey!",
						"Darn!","Shoot!","Crud!","Oh no!","Goodness gracious!","Heavens to Betsy!","Good grief!","Well, I'll be!",
						"I can't believe it!","Oh fudge!","Great Scott!","Dude!","Man!","Aw, crap!","No way!","Are you kidding me?",
						"Seriously?","Oh boy!","Sweet mercy!"],

	"things_done":	["Consider it done!", "Sure thing!", "You got it!", "Already on it!", "Of course!", "Mind reader here!",
					"It's taken care of.", "Crystal ball working overtime!", "Telepathy - it's a real thing!", "You don't need to ask me.",
					"Absolutely.", "You betcha!", "No problem.", "Absolutely!", "Roger that.", "For sure.", "Definitely.", "On it.",
					"Working on it.", "I'm on it.", "Got it coveRED.", "In progress.", "Taking care of it.", "No sweat!", "Happy to help.",
					"Count on it.", "Done and done.", "You bet!", "Affirmative.", "Gotcha.", "Easy peasy.", "Check.", "Will do.",
					"Happy to oblige.", "No worries.", "As you wish.", "By all means.", "It's a deal.", "I'll take care of it.",
					"You've got it.", "Consider it handled.", "I'm on the case.", "Don't mention it.", "With pleasure.", "Gladly.",
					"Absolutely!", "No doubt about it.", "You can count on me.", "I'm all over it.", "No problem at all.",
					"I'm on it like a duck on water.", "I'm on it like a shot.", "I'm on it like white on rice.",
					"I'm on it like a cheetah on a gazelle.", "I'm on it like a hawk on a mouse." , "I'm on it like a shark on a seal.",
					"I'm on it like a spider on a fly." , "I'm on it like a tiger on its prey."],

	"older_messages":	["From the ages of times" , "The older's have spocken" , "Lo, these many years" , "Hark! A tale is told",
						"Based on my ancient knowledge..." , "In the wisdom of old times..." , "Drawing on ages past...",
						"From time immemorial..." , "According to the ancients..." , "As passed down thought the generations...",
						"In days of yore","Verily, I say unto thee" , "Forsooth, it is written" , "Whence came this knowledge?",
						"Aye, by the gods", "Thus spake the oracle" , "The ancients decreed" , "It is decreed by fate" ,
						"The elders have warned" , "By the power vested in me" , "Hearken to my words" , "Let it be known", "Time immemorial",
						"Ancient wisdom" , "Timeless truth" , "Bygone era" , "Primeval force" , "Cosmic order" , "Eternal law",
						"The elders proclaimed" , "The sages dictated" , "The oracles foretold" , "The seers envisioned",
						"The ancient laws stipulated" , "The time-honored customs demanded" , "The revered traditions prescribed",
						"The sacRED texts commanded" , "The cosmic order decreed" , "The divine will ordained" , "The hidden forces dictated",
						"Primeval knowledge" , "Age-old adage" , "Everlasting principle", "Primal understanding" , "Eternal verity",
						"Enduring legacy" , "Perennial concept" , "Inherent truth" , "Fundamental axiom" , "Bedrock belief",
						"Historical precedent" , "Ancestral lore" , "Legendary wisdom" , "Bygone era wisdom", "Antiquated knowledge",
						"The elders proclaimed" , "The sages dictated" , "The oracles foretold" , "The seers envisioned",
						"The ancient laws stipulated" , "The time-honored customs demanded" , "The revered traditions prescribed",
						"The sacred texts commanded" , "The cosmic order decreed" , "The divine will ordained" , "The hidden forces dictated"],

	"year_event_msg":	["That in my knowledge is a year event. Perhaps you might want to know the number the days till %s...\n",
						"%s is a unique event in the year. Have you considered know the number the days till then...\n",
						"In my knowledge is a year event. I wonder if you know how many days left to %s...\n",
						"In other words we may say it's a once year event. Do you know how many days are still %s.\n",
						"Did you consider know how many days are still that unique event that it %s?\n",]
}
#-------------------------------------------------------------------------------------
chkdict.append(sum(sum(ord(char) for char in word) for value in messages.values() for word in value))
#-------------------------------------------------------------------------------------
weather_season_condiction = {
	"winter":	["Coldest days","Short days","Long nights","Snow","Ice","Rainy days","Frost","Cold","Bare trees","Chilly winds","Cloudy sky","Freezing rain","Strong cold Wind"],
	"spring":	["Warming temperatures","Longer days","Melting snow","Flower blooming","New life emerging","Gradually warming","Sky partly cloudy","Cloudy to sunny","Moderated wind","Summer is coming"],
	"summer":	["Hot days","Longest days","Shortest nights","Sunny skies","GREEN landscapes","Light breezes","Sunny day","High temperatures","Autumn approaching","Spring as gone"],
	"autumn":	["Cooling temperatures","Falling leaves","Harvest season","Crisp air","Occasional drizzle","Crisp evenings","Changing colors","Sky partly cloudy","Wind increasings","Winter approaching"]
}
#------------------------------------------------------------
topics = ["astronomy glossary","planets","planet orbit","orbits acronyms","asteroids","constelations","information about stars","distance of planets and from the sun",
		"periodic table elements","visualize the periodic table","where is the ISS","people in space","climate dictionary","old tech objects and terms",
		"the world capitals","seasons of the year","play capitals","math game","constellations and elements game","manage the askards database","linux command",
		"phonetic alphabet","morse code encoding/decoding","how many days till","moon phases","yoda say","today activity","art python",
		"astronomy questions","difference from <date>","age calc <from date>","Show you the meaning of some words or terms"]

#------------------------------------------------------------
factors = [["feets", 0.3048],["miles", 1.609344],["yards", 0.9144],["m3", 0.001],["gallons", 3.78541178],["fahrenheit", 33.8],["au", 149.6e6]]

#------------------------------------------------------------
countries = {
	"afghanistan": {"capital": "kabul", "population": 42647492 },"albania": {"capital": "tirana", "population": 2791765 },
	"algeria": {"capital": "algiers", "population": 46814308 },"andorra": {"capital": "andorra la vella", "population": 81938 },
	"angola": {"capital": "luanda", "population": 37885849 },"antigua and barbuda": {"capital": "saint john’s", "population": 93772 },
	"argentina": {"capital": "buenos aires", "population": 45696159 },"armenia": {"capital": "yerevan", "population": 2973840 },
	"australia": {"capital": "canberra", "population": 26713205 },"austria": {"capital": "vienna", "population": 9120813 },
	"azerbaijan": {"capital": "baku", "population": 10336577 },"the bahamas": {"capital": "nassau", "population": 401283 },
	"bahrain": {"capital": "manama", "population": 1607049 },"bangladesh": {"capital": "dhaka", "population": 173562364 },
	"barbados": {"capital": "bridgetown", "population": 282467 },"belarus": {"capital": "minsk", "population": 9056696 },
	"belgium": {"capital": "brussels", "population": 11738763 },"belize": {"capital": "belmopan", "population": 417072 },
	"benin": {"capital": "porto-novo", "population": 14462724 },"bhutan": {"capital": "thimphu", "population": 791524 },
	"bolivia": {"capital": "la paz, sucre", "population": 12413315 },"bosnia and herzegovina": {"capital": "sarajevo", "population": 3164253 },
	"botswana": {"capital": "gaborone", "population": 2521139 },"brazil": {"capital": "brasilia", "population": 211998573 },
	"brunei": {"capital": "bandar seri begawan", "population": 462721 },"bulgaria": {"capital": "sofia", "population": 6757689 },
	"burkina faso": {"capital": "ouagadougou", "population": 23548781 },"burundi": {"capital": "bujumbura", "population": 14047786 },
	"cambodia": {"capital": "phnom penh", "population": 17638801 },"cameroon": {"capital": "yaounde", "population": 29123744 },
	"canada": {"capital": "ottawa", "population": 39742430 },"cape verde": {"capital": "praia", "population": 524877 },
	"central african republic": {"capital": "bangui", "population": 5330690 },"chad": {"capital": "n’djamena", "population": 20299123 },
	"chile": {"capital": "santiago", "population": 19764771 },"china": {"capital": "beijing", "population": 1419321278 },
	"colombia": {"capital": "bogota", "population": 52886363 },"comoros": {"capital": "moroni", "population": 866628 },
	"republic of the congo": {"capital": "brazzaville", "population": 6332961 },"democratic republic of the congo": {"capital": "kinshasa", "population": 109276265 },
	"costa rica": {"capital": "san jose", "population": 5129910 },"cote d’ivoire": {"capital": "yamoussoukro", "population": 31934230 },
	"croatia": {"capital": "zagreb", "population": 3875325 },"cuba": {"capital": "havana", "population": 10979783 },
	"cyprus": {"capital": "nicosia", "population": 1358282 },"czech republic": {"capital": "prague", "population": 10735859 },
	"denmark": {"capital": "copenhagen", "population": 5977412 },"djibouti": {"capital": "djibouti", "population": 1168722 },
	"dominica": {"capital": "roseau", "population": 66205 },"dominican republic": {"capital": "santo domingo", "population": 11427557 },
	"east timor": {"capital": "dili", "population": 1400638 },"ecuador": {"capital": "quito", "population": 18135478 },
	"egypt": {"capital": "cairo", "population": 116538258 },"el salvador": {"capital": "san salvador", "population": 6338193 },
	"equatorial guinea": {"capital": "malabo", "population": 1892516 },"eritrea": {"capital": "asmara", "population": 3535603 },
	"estonia": {"capital": "tallinn", "population": 1360546 },"ethiopia": {"capital": "addis ababa", "population": 132059767 },
	"fiji": {"capital": "suva", "population": 928784 },"finland": {"capital": "helsinki", "population": 5617310 },
	"france": {"capital": "paris", "population": 66548530 },"gabon": {"capital": "libreville", "population": 2538952 },
	"the gambia": {"capital": "banjul", "population": 2759988 },"georgia": {"capital": "tbilisi", "population": 3807670 },
	"germany": {"capital": "berlin", "population": 84552242 },"ghana": {"capital": "accra", "population": 34427414 },
	"greece": {"capital": "athens", "population": 10047817 },"grenada": {"capital": "saint george’s", "population": 117207 },
	"guatemala": {"capital": "guatemala city", "population": 18406359 },"guinea": {"capital": "conakry", "population": 14754785 },
	"guinea-bissau": {"capital": "bissau", "population": 2201352 },"guyana": {"capital": "georgetown", "population": 831087 },
	"haiti": {"capital": "port-au-prince", "population": 11772557 },"honduras": {"capital": "tegucigalpa", "population": 10825703 },
	"hungary": {"capital": "budapest", "population": 9676135 },"iceland": {"capital": "reykjavik", "population": 393396 },
	"india": {"capital": "new delhi", "population": 1450935791 },"indonesia": {"capital": "jakarta", "population": 283487931 },
	"iran": {"capital": "tehran", "population": 91567738 },"iraq": {"capital": "baghdad", "population": 46042015 },
	"ireland": {"capital": "dublin", "population": 5255017 },"israel": {"capital": "jerusalem", "population": 9387021 },
	"italy": {"capital": "rome", "population": 59342867 },"jamaica": {"capital": "kingston", "population": 2839175 },
	"japan": {"capital": "tokyo", "population": 123753041 },"jordan": {"capital": "amman", "population": 11552876 },
	"kazakhstan": {"capital": "astana", "population": 20592571 },"kenya": {"capital": "nairobi", "population": 56432944 },
	"kiribati": {"capital": "tarawa atoll", "population": 134518 },"north korea": {"capital": "pyongyang", "population": 26498823 },
	"south korea": {"capital": "seoul", "population": 51717590 },"kosovo": {"capital": "pristina", "population": 0 },
	"kuwait": {"capital": "kuwait city", "population": 4934507 },"kyrgyzstan": {"capital": "bishkek", "population": 7186009 },
	"laos": {"capital": "vientiane", "population": 7769819 },"latvia": {"capital": "riga", "population": 1871871 },
	"lebanon": {"capital": "beirut", "population": 5805962 },"lesotho": {"capital": "maseru", "population": 2337423 },
	"liberia": {"capital": "monrovia", "population": 5612817 },"libya": {"capital": "tripoli", "population": 7381023 },
	"liechtenstein": {"capital": "vaduz", "population": 39870 },"lithuania": {"capital": "vilnius", "population": 2859110 },
	"luxembourg": {"capital": "luxembourg", "population": 673036 },"macedonia": {"capital": "skopje", "population": 1823009 },
	"madagascar": {"capital": "antananarivo", "population": 31964956 },"malawi": {"capital": "lilongwe", "population": 21655286 },
	"malaysia": {"capital": "kuala lumpur", "population": 35557673 },"maldives": {"capital": "male", "population": 527799 },
	"mali": {"capital": "bamako", "population": 24478595 },"malta": {"capital": "valletta", "population": 539607 },
	"marshall islands": {"capital": "majuro", "population": 37548 },"mauritania": {"capital": "nouakchott", "population": 5169395 },
	"mauritius": {"capital": "port louis", "population": 1271169 },"mexico": {"capital": "mexico city", "population": 130861007 },
	"federated states of micronesia": {"capital": "palikir", "population": 526923 },"moldova": {"capital": "chisinau", "population": 3034961 },
	"monaco": {"capital": "monaco", "population": 38631 },"mongolia": {"capital": "ulaanbaatar", "population": 3475540 },
	"montenegro": {"capital": "podgorica", "population": 638479 },"morocco": {"capital": "rabat", "population": 38081173 },
	"mozambique": {"capital": "maputo", "population": 34631766 },"myanmar": {"capital": "naypyidaw", "population": 54500091 },
	"namibia": {"capital": "windhoek", "population": 3030131 },"nauru": {"capital": "yaren district", "population": 11947 },
	"nepal": {"capital": "kathmandu", "population": 29651054 },"netherlands": {"capital": "amsterdam", "population": 18228742 },
	"new zealand": {"capital": "wellington", "population": 5213944 },"nicaragua": {"capital": "managua", "population": 6916140 },
	"niger": {"capital": "niamey", "population": 27032412 },"nigeria": {"capital": "abuja", "population": 232679478 },
	"norway": {"capital": "oslo", "population": 5576660 },"oman": {"capital": "muscat", "population": 5281538 },
	"pakistan": {"capital": "islamabad", "population": 251269164 },"palau": {"capital": "melekeok", "population": 17695 },
	"panama": {"capital": "panama city", "population": 4515577 },"papua new guinea": {"capital": "port moresby", "population": 10576502 },
	"paraguay": {"capital": "asuncion", "population": 6929153 },"peru": {"capital": "lima", "population": 34217848 },
	"philippines": {"capital": "manila", "population": 115843670 },"poland": {"capital": "warsaw", "population": 38539201 },
	"portugal": {"capital": "lisbon", "population": 10425292 },"qatar": {"capital": "doha", "population": 3048423 },
	"romania": {"capital": "bucharest", "population": 19015088 },"russia": {"capital": "moscow", "population": 144820423 },
	"rwanda": {"capital": "kigali", "population": 14256567 },"saint kitts and nevis": {"capital": "basseterre", "population": 46843 },
	"saint lucia": {"capital": " castries", "population": 179744 },"saint vincent and the grenadines": {"capital": "kingstown", "population": 100616 },
	"samoa": {"capital": "apia", "population": 218019 },"san marino": {"capital": "san marino", "population": 33581 },
	"sao tome and principe": {"capital": "sao tome", "population": 235536 },"saudi arabia": {"capital": "riyadh", "population": 33962757 },
	"senegal": {"capital": "dakar", "population": 18501984 },"serbia": {"capital": "belgrade", "population": 6736216 },
	"seychelles": {"capital": "victoria", "population": 130418 },"sierra leone": {"capital": "freetown", "population": 8642022 },
	"singapore": {"capital": "singapore", "population": 5832387 },"slovakia": {"capital": "bratislava", "population": 5506760 },
	"slovenia": {"capital": "ljubljana", "population": 2118697 },"solomon islands": {"capital": "honiara", "population": 819198 },
	"somalia": {"capital": "mogadishu", "population": 19009151 },"south africa": {"capital": "pretoria, cape town, bloemfontein", "population": 64007187 },
	"south sudan": {"capital": "juba", "population": 11943408 },"spain": {"capital": "madrid", "population": 47910526 },
	"sri lanka": {"capital": "colombo, sri jayewardenepura kotte", "population": 23103565 },"sudan": {"capital": "khartoum", "population": 50448963 },
	"suriname": {"capital": "paramaribo", "population": 634431 },"eswatini": {"capital": "mbabane", "population": 1242822 },
	"sweden": {"capital": "stockholm", "population": 10606999 },"switzerland": {"capital": "bern", "population": 8921981 },
	"syria": {"capital": "damascus", "population": 24672760 },"taiwan": {"capital": "taipei", "population": 23213962 },
	"tajikistan": {"capital": "dushanbe", "population": 10590927 },"tanzania": {"capital": "dodoma", "population": 68560157 },
	"thailand": {"capital": "bangkok", "population": 71668011 },"togo": {"capital": "lome", "population": 9515236 },
	"tonga": {"capital": "nuku’alofa", "population": 104175 },"trinidad and tobago": {"capital": "port-of-spain", "population": 1507782 },
	"tunisia": {"capital": "tunis", "population": 12277109 },"turkey": {"capital": "ankara", "population": 87473805 },
	"turkmenistan": {"capital": "ashgabat", "population": 7494498 },"tuvalu": {"capital": "funafuti", "population": 9646 },
	"uganda": {"capital": "kampala", "population": 50015092 },"ukraine": {"capital": "kyiv", "population": 37860221 },
	"united arab emirates": {"capital": "abu dhabi", "population": 11027129 },"united kingdom": {"capital": "london", "population": 69138192 },
	"united states of america": {"capital": "washington d.c.", "population": 345426571 },"uruguay": {"capital": "montevideo", "population": 3386588 },
	"uzbekistan": {"capital": "tashkent", "population": 36361859 },"vanuatu": {"capital": "port-vila", "population": 327777 },
	"vatican city": {"capital": "vatican city", "population": 1000 },"venezuela": {"capital": "caracas", "population": 28405543 },
	"vietnam": {"capital": "hanoi", "population": 100987686 },"yemen": {"capital": "sanaa", "population": 40583164 },
	"zambia": {"capital": "lusaka", "population": 21314956 },"zimbabwe": {"capital": "harare", "population": 16634373 }
}
#----------------------------------------------------
core['country'] = list(countries.keys())
core['capital'] = [country["capital"] for country in countries.values()]
chkdict.append(sum(sum(ord(char) for char in word) for value in countries.values() for word in value))

#----------------------------------------------------
stars_dict = {
	"Acamar": ["HR 897","Eri"],"Achernar": ["HR 472","Eri"],"Achird": ["HR 219","Cas"],"Acrab": ["HR 5984","Sco"],
	"Acrux": ["HR 4730","Cru"],"Acubens": ["HR 3572","Cnc"],"Adhafera": ["HR 4031","Leo"],"Adhara": ["HR 2618","CMa"],
	"Adhil": ["HR 390","And"],"Ain": ["HR 1409","Tau"],"Ainalrami": ["HR 7116","Sgr"],"Aladfar": ["HR 7298","Lyr"],
	"Albaldah": ["HR 7264","Sgr"],"Albali": ["HR 7950","Aqr"],"Albireo": ["HR 7417","Cyg"],"Alchiba": ["HR 4623","Crv"],
	"Alcor": ["HR 5062","UMa"],"Alcyone": ["HR 1165","Tau"],"Aldebaran": ["HR 1457","Tau"],"Alderamin": ["HR 8162","Cep"],
	"Aldhanab": ["HR 8353","Gru"],"Aldhibah": ["HR 6396","Dra"],"Aldulfin": ["HR 7852","Del"],"Alfirk": ["HR 8238","Cep"],
	"Algedi": ["HR 7754","Cap"],"Algenib":["HR 39","Peg"],"Algieba": ["HR 4057","Leo"],"Algol": ["HR 936","Per"],
	"Algorab":["HR 4757","Crv"],"Alhena":["HR 2421","Gem"],"Alioth":["HR 4905","UMa"],"Aljanah":["HR 7949","Cyg"],
	"Alkaid": ["HR 5191","UMa"],"Alkalurops":["HR 5733","Boo"],"Alkaphrah": ["HR 3594","UMa"],"Alkarab": ["HR 8905", "Peg"],
    "Alkes": ["HR 4287", "Crt"],"Almaaz": ["HR 1605", "Aur"],"Almach": ["HR 603", "And"],"Alnair": ["HR 8425", "Gru"],
	"Alnasl": ["HR 6746", "Sgr"],"Alnilam": ["HR 1903", "Ori"],"Alnitak": ["HR 1948", "Ori"],"Alniyat": ["HR 6084", "Sco"],
    "Alphard": ["HR 3748", "Hya"],"Alphecca": ["HR 5793", "CrB"],"Alpheratz": ["HR 15", "And"],"Alpherg": ["HR 437", "Psc"],
    "Alrakis": ["HR 6370", "Dra"],"Alrescha": ["HR 596", "Psc"],"Alruba": ["HR 6618", "Dra"],"Alsafi": ["HR 7462", "Dra"],
    "Alsciaukat": ["HR 3275", "Lyn"],"Alsephina": ["HR 3485", "Vel"],"Alshain": ["HR 7602", "Aql"],"Alshat": ["HR 7773", "Cap"],
    "Altair": ["HR 7557", "Aql"],"Altais": ["HR 7310", "Dra"],"Alterf": ["HR 3773", "Leo"],"Aludra": ["HR 2827", "CMa"],
    "Alula Australis": ["HR 4375", "UMa"],"Alula Borealis": ["HR 4377", "UMa"],"Alya": ["HR 7141", "Ser"],
    "Alzirr": ["HR 2484", "Gem"],"Ancha": ["HR 8499", "Aqr"],"Angetenar": ["HR 850", "Eri"],"Ankaa": ["HR 99", "Phe"],
    "Anser": ["HR 7405", "Vul"],"Antares": ["HR 6134", "Sco"],"Arcturus": ["HR 5340", "Boo"],"Arkab Posterior": ["HR 7343", "Sgr"],
    "Arkab Prior": ["HR 7337", "Sgr"],"Arneb": ["HR 1865", "Lep"],"Ascella": ["HR 7194", "Sgr"],"Asellus Australis": ["HR 3461", "Cnc"],
    "Asellus Borealis": ["HR 3449", "Cnc"],"Ashlesha": ["HR 3482", "Hya"],"Aspidiske": ["HR 3699", "Car"],"Asterope": ["HR 1151", "Tau"],
    "Athebyne": ["HR 6132", "Dra"],"Atik": ["HR 1131", "Per"],"Atlas": ["HR 1178", "Tau"],"Atria": ["HR 6217", "TrA"],
    "Avior": ["HR 3307", "Car"],"Azelfafage": ["HR 8301", "Cyg"],"Azha": ["HR 874", "Eri"],"Azmidi": ["HR 3045", "Pup"],
    "Barnard's Star": ["GJ 699", "Oph"],"Baten Kaitos": ["HR 539", "Cet"],"Beemim": ["HR 1393", "Eri"],"Beid": ["HR 1298", "Eri"],
    "Bellatrix": ["HR 1790", "Ori"],"Betelgeuse": ["HR 2061", "Ori"],"Bharani": ["HR 838", "Ari"],"Biham": ["HR 8450", "Peg"],
    "Botein": ["HR 951", "Ari"],"Brachium": ["HR 5603", "Lib"],"Bunda": ["HR 8264", "Aqr"],"Canopus": ["HR 2326", "Car"],
    "Capella": ["HR 1708", "Aur"],"Caph": ["HR 21", "Cas"],"Castor": ["HR 2891", "Gem"],"Castula": ["HR 265", "Cas"],
    "Cebalrai": ["HR 6603", "Oph"],"Celaeno": ["HR 1140", "Tau"],"Cervantes": ["HR 6585", "Ara"],"Chalawan": ["HR 4277", "UMa"],
    "Chamukuy": ["HR 1412", "Tau"],"Chara": ["HR 4785", "CVn"],"Chertan": ["HR 4359", "Leo"],"Copernicus": ["HR 3522", "Cnc"],
    "Cor Caroli": ["HR 4915", "CVn"],"Cujam": ["HR 6117", "Her"],"Cursa": ["HR 1666", "Eri"],"Dabih": ["HR 7776", "Cap"],
    "Dalim": ["HR 963", "For"],"Deneb Algedi": ["HR 8322", "Cap"],"Deneb": ["HR 7924", "Cyg"],"Denebola": ["HR 4534", "Leo"],
    "Diadem": ["HR 4968", "Com"],"Diphda": ["HR 188", "Cet"],"Dschubba": ["HR 5953", "Sco"],"Dubhe": ["HR 4301", "UMa"],
    "Dziban": ["HR 6636", "Dra"],"Edasich": ["HR 5744", "Dra"],"Electra": ["HR 1142", "Tau"],"Elgafar": ["HR 5409", "Vir"],
    "Elkurud": ["HR 2177", "Col"],"Elnath": ["HR 1791", "Tau"],"Eltanin": ["HR 6705", "Dra"],"Enif": ["HR 8308", "Peg"],
    "Errai": ["HR 8974", "Cep"],"Fafnir": ["HR 6945", "Dra"],"Fang": ["HR 5944", "Sco"],"Fawaris": ["HR 7528", "Cyg"],
    "Felis": ["HR 3923", "Hya"],"Fomalhaut": ["HR 8728", "PsA"],"Fulu": ["HR 153", "Cas"],"Fumalsamakah": ["HR 8773", "Psc"],
    "Furud": ["HR 2282", "CMa"],"Fuyue": ["HR 6630", "Sco"],"Gacrux": ["HR 4763", "Cru"],"Giausar": ["HR 4434", "Dra"],
    "Gienah": ["HR 4662", "Crv"],"Ginan": ["HR 4700", "Cru"],"Gomeisa": ["HR 2845", "CMi"],"Grumium": ["HR 6688", "Dra"],
    "Hadar": ["HR 5267", "Cen"],"Haedus": ["HR 1641", "Aur"], "Hamal": ["HR 617", "Ari"],"Hassaleh": ["HR 1577", "Aur"],
    "Hatysa": ["HR 1899", "Ori"],"Helvetios": ["HR 8729", "Peg"],"Heze": ["HR 5107", "Vir"],"Homam": ["HR 8634", "Peg"],
    "Iklil": ["HR 5928", "Sco"],"Intercrus": ["HR 3743", "UMa"],"Izar": ["HR 5506", "Boo"],"Jabbah": ["HR 6027", "Sco"],
    "Jishui": ["HR 2930", "Gem"],"Kaffaljidhma": ["HR 804", "Cet"],"Kang": ["HR 5315", "Vir"],"Kaus Australis": ["HR 6879", "Sgr"],
    "Kaus Borealis": ["HR 6913", "Sgr"],"Kaus Media": ["HR 6859", "Sgr"],"Keid": ["HR 1325", "Eri"],"Khambalia": ["HR 5359", "Vir"],
    "Kitalpha": ["HR 8131", "Equ"],"Kochab": ["HR 5563", "UMi"],"Kornephoros": ["HR 6148", "Her"],"Kraz": ["HR 4786", "Crv"],
    "Kurhah": ["HR 8417", "Cep"],"Larawag": ["HR 6241", "Sco"],"Lesath": ["HR 6508", "Sco"],"Libertas": ["HR 7595", "Aql"],
    "Lich": ["PSR B1257+12", "Vir"],"Lilii Borea": ["HR 824", "Ari"],"Maasym": ["HR 6526", "Her"],"Mahasim": ["HR 2095", "Aur"],
    "Maia": ["HR 1149", "Tau"],"Marfik": ["HR 6149", "Oph"],"Markab": ["HR 8781", "Peg"],"Markeb": ["HR 3734", "Vel"],
    "Marsic": ["HR 6008", "Her"],"Matar": ["HR 8650", "Peg"],"Mebsuta": ["HR 2473", "Gem"],"Megrez": ["HR 4660", "UMa"],
    "Meissa": ["HR 1879", "Ori"],"Mekbuda": ["HR 2650", "Gem"],"Meleph": ["HR 3429", "Cnc"],"Menkalinan": ["HR 2088", "Aur"],
    "Menkar": ["HR 911", "Cet"],"Menkent": ["HR 5288", "Cen"],"Menkib": ["HR 1228", "Per"],"Merak": ["HR 4295", "UMa"],
    "Merga": ["HR 5533", "Boo"],"Meridiana": ["HR 7254", "CrA"],"Merope": ["HR 1156", "Tau"],"Mesarthim": ["HR 546", "Ari"],
    "Miaplacidus": ["HR 3685", "Car"],"Mimosa": ["HR 4853", "Cru"],"Minchir": ["HR 3418", "Hya"],"Minelauva": ["HR 4910", "Vir"],
    "Mintaka": ["HR 1852", "Ori"],"Mira": ["HR 681", "Cet"],"Mirach": ["HR 337", "And"],"Miram": ["HR 834", "Per"],
    "Mirfak": ["HR 1017", "Per"],"Mirzam": ["HR 2294", "CMa"],"Misam": ["HR 941", "Per"],"Mizar": ["HR 5054", "UMa"],
    "Mothallah": ["HR 544", "Tri"],"Muliphein": ["HR 2657", "CMa"],"Muphrid": ["HR 5235", "Boo"],"Muscida": ["HR 3323", "UMa"],
    "Musica": ["HR 8030", "Del"],"Nahn": ["HR 3627", "Cnc"],"Naos": ["HR 3165", "Pup"],"Nashira": ["HR 8278", "Cap"],
    "Nekkar": ["HR 5602", "Boo"],"Nembus": ["HR 464", "And"],"Nihal": ["HR 1829", "Lep"],"Nunki": ["HR 7121", "Sgr"],
    "North Star": ["HR 424", "UMi"],"Nusakan": ["HR 5747", "CrB"],"Ogma": ["HD 149026", "Her"],"Okab": ["HR 7235", "Aql"],"Peacock": ["HR 7790", "Pav"],
    "Phact": ["HR 1956", "Col"],"Phecda": ["HR 4554", "UMa"],"Pherkad": ["HR 5735", "UMi"],"Piautos": ["HR 3268", "Cnc"],
    "Pipirima": ["HR 6252", "Sco"],"Pleione": ["HR 1180", "Tau"],"Polaris Australis": ["HR 7228", "Oct"],
    "Polaris": ["HR 424", "UMi"],"Polis": ["HR 6812", "Sgr"],"Pollux": ["HR 2990", "Gem"],"Porrima": ["HR 4825", "Vir"],
    "Praecipua": ["HR 4247", "LMi"],"Prima Hyadum": ["HR 1346", "Tau"],"Procyon": ["HR 2943", "CMi"],"Propus": ["HR 2216", "Gem"],
    "Proxima Centauri": ["GJ 551", "Cen"],"Ran": ["HR 1084", "Eri"],"Rasalas": ["HR 3905", "Leo"],"Rasalgethi": ["HR 6406", "Her"],
    "Rasalhague": ["HR 6556", "Oph"],"Rastaban": ["HR 6536", "Dra"],"Regulus": ["HR 3982", "Leo"],"Revati": ["HR 361", "Psc"],
    "Rigel": ["HR 1713", "Ori"],"Rigil Kentaurus": ["HR 5459", "Cen"],"Rotanev": ["HR 7882", "Del"],"Ruchbah": ["HR 403", "Cas"],
    "Rukbat": ["HR 7348", "Sgr"],"Sabik": ["HR 6378", "Oph"],"Saclateni": ["HR 1612", "Aur"],"Sadachbia": ["HR 8518", "Aqr"],
    "Sadalbari": ["HR 8684", "Peg"],"Sadalmelik": ["HR 8414", "Aqr"],"Sadalsuud": ["HR 8232", "Aqr"],"Sadr": ["HR 7796", "Cyg"],
    "Saiph": ["HR 2004", "Ori"],"Salm": ["HR 8880", "Peg"],"Sargas": ["HR 6553", "Sco"],"Sarin": ["HR 6410", "Her"],
    "Sceptrum": ["HR 1481", "Eri"],"Scheat": ["HR 8775", "Peg"],"Schedar": ["HR 168", "Cas"],"Secunda Hyadum": ["HR 1373", "Tau"],
    "Segin": ["HR 0542", "Cas"],"Seginus": ["HR 5435", "Boo"],"Sham": ["HR 7479", "Sge"],"Shaula": ["HR 6527", "Sco"],
	"Sheliak": ["HR 7106", "Lyr"],"Sheratan": ["HR 553", "Ari"],"Sirius": ["HR 2491", "CMa"],"Situla": ["HR 8610", "Aqr"],
	"Skat": ["HR 8709", "Aqr"],"Spica": ["HR 5056", "Vir"],"Sualocin": ["HR 7906", "Del"],"Subra": ["HR 3852", "Leo2"],
    "Suhail": ["HR 3634", "Vel"],"Sulafat": ["HR 7178", "Lyr"],"Syrma": ["HR 5338", "Vir"],"Tabit": ["HR 1543", "Ori"],
    "Taiyangshou": ["HR 4518", "UMa"],"Taiyi": ["HR 4916", "Dra"],"Talitha": ["HR 3569", "UMa"],"Tania Australis": ["HR 4069", "UMa"],
    "Tania Borealis": ["HR 4033", "UMa"],"Tarazed": ["HR 7525", "Aql"],"Tarf": ["HR 3249", "Cnc"],"Taygeta": ["HR 1145", "Tau"],
    "Tegmine": ["HR 3208", "Cnc"],"Tejat": ["HR 2286", "Gem"],"Terebellum": ["HR 7597", "Sgr"],"Theemin": ["HR 1464", "Eri"],
	"Thuban": ["HR 5291", "Dra"],"Tiaki": ["HR 8636", "Gru"],"Tianguan": ["HR 1910", "Tau"],"Tianyi": ["HR 4863", "Dra"],
    "Titawin": ["HR 458", "And"],"Tonatiuh": ["HR 4609", "Cam"],"Torcular": ["HR 510", "Psc"],"Tureis": ["HR 3185", "Pup"],
    "Ukdah": ["HR 3845", "Hya"],"Unukalhai": ["HR 5854", "Ser"],"Unurgunite": ["HR 2646", "CMa"],"Vega": ["HR 7001", "Lyr"],
    "Veritate": ["HR 8930", "And"],"Vindemiatrix": ["HR 4932", "Vir"],"Wasat": ["HR 2777", "Gem"],"Wazn": ["HR 2040", "Col"],
    "Wezen": ["HR 2693", "CMa"],"Wurren": ["HR 338", "Phe"],"Xamidimura": ["HR 6247", "Sco"],"Xuange": ["HR 5351", "Boo"],
    "Yed Posterior": ["HR 6075", "Oph"],"Yed Prior": ["HR 6056", "Oph"],"Yildun": ["HR 6789", "UMi"],"Zaniah": ["HR 4689", "Vir"],
    "Zaurak": ["HR 1231", "Eri"],"Zavijava": ["HR 4540", "Vir"],"Zhang": ["HR 3903", "Hya"],"Zibal": ["HR 984", "Eri"],
    "Zosma": ["HR 4357", "Leo"],"Zubenelgenubi": ["HR 5531", "Lib"],"Zubenelhakrabi": ["HR 5787", "Lib"],"Zubeneschamali": ["HR 5685", "Lib"],
}
#--------------------------------------------------------------
core["star name"] = [key.lower() for key in stars_dict.keys()]
chkdict.append(sum(sum(ord(char) for char in word) for value in stars_dict.values() for word in value))

#--------------------------------------------------------------
astronomy_glossary = {
	"a-type star": "In the Harvard spectral classification system, a class of main-sequence star having spectra dominated by Balmer absorption lines of hydrogen. Stars of spectral class A are typically BLUE-white or white in color, measure between 1.4 and 2.1 times the mass of the Sun, and have surface temperatures of 7,600–10,000 kelvin.",
	"absolute magnitude": "A scale for measuring the actual brightness of a celestial object without accounting for the distance of the object. Absolute magnitude measures how bright an object would appear if it were exactly 10 parsecs (about 33 light-years) away from Earth. On this scale, the Sun has an absolute magnitude of +4.8 while it has an apparent magnitude of -26.7 because it is so close.",
	"absolute zero": "The temperature at which the motion of all atoms and molecules stops and no heat is given off. Absolute zero is reached at 0 degrees Kelvin or -273.16 degrees Celsius.",
	"absorption line": "When light passes through a gas, certain colors are absorbed, creating dark lines within the otherwise continuous spectrum. These unique patterns of dark lines correspond to specific elements, allowing scientists to determine the composition of distant stars and celestial bodies.",
	"ablation": "A process by where the atmosphere melts away and removes the surface material of an incoming meteorite.",
	"accretion": "The process by where dust and gas accumulated into larger bodies such as stars and planets.",
	"accretion disk": "A disk of gas that accumulates around a center of gravitational attraction, such as a white dwarf, neutron star, or black hole. As the gas spirals in, it becomes hot and emits light or even X-radiation.",
	"achondrite": "A stone meteorite that contains no chondrules.",
	"active galactic nuclei": "At the heart of some galaxies lies an incREDibly bright, compact region powered by a supermassive black hole. This cosmic monster feeds on surrounding matter, creating a swirling disk that heats up to extreme temperatures and releases vast amounts of energy. The most luminous examples of these galactic powerhouses are known as quasars.",
	"agn": "A compact region in the center of a galaxy displaying a much higher than normal luminosity over some part of the electromagnetic spectrum with characteristics indicating that the luminosity is not produced by stars. A galaxy hosting an AGN is called an active galaxy.",
	"albedo": "The reflective property of a non-luminous object. A perfect mirror would have an albedo of 100% while a black hole would have an albedo of 0%.",
	"albedo feature": "A dark or light marking on the surface of an object that may or may not be a geological or topographical feature.",
	"altitude": "The angular distance of an object above the horizon.",
	"ammonia": "Ammonia is a molecule made up of one nitrogen atom bonded to three hydrogen atoms. It's a common substance found throughout the universe, existing as a gas or frozen ice depending on the temperature of its environment.",
	"amplitude": "The size of a wave from the top of a wave crest to its midpoint.",
	"angstrom": "An angstrom is a tiny unit of measurement equal to one ten-billionth of a meter. It's so small that it's often used to measure things at the atomic level, like the size of atoms or the wavelength of light. An angstrom is equal to one tenth of one nanometer.",
	"angular resolution": "Angular resolution is the specific angle by which two points can be separated and still be seen as distinct.",
	"antimatter": "Matter consisting of particles with charges opposite that of ordinary matter. In antimatter, protons have a negative charge while electrons have a positive charge.",
	"antipodal point": "A point that is on the direct opposite side of a planet.",
	"apastron": "The point of greatest separation of two stars, such as in a binary star system.",
	"aperture": "The size of the opening through which light passes in an optical instrument such as a camera or telescope.",
	"aphelion": "The point in the orbit of a planet or other celestial body where it is farthest from the Sun.",
	"apogee": "The point in the orbit of the Moon or other satellite where it is farthest from the Earth.",
	"apparent magnitude": "The apparent brightness of an object in the sky as it appears to an observer on Earth. Bright objects have a low apparent magnitude while dim objects will have a higher apparent magnitude.",
	"astronomical dust": "Is composed of tiny particles, ranging from the size of a few molecules to a few millimeters. These particles are typically made up of silicate grains (similar to sand) and polycyclic aromatic hydrocarbons (PAHs), which resemble soot. This cosmic dust is found in abundance throughout the universe, from within comets and asteroids to the vast spaces between stars. It plays a crucial role in various astronomical processes, such as star formation and the evolution of galaxies.",
	"asterism": "Any prominent star pattern that isn’t a whole constellation, such as the Northern Cross or the Big Dipper.",
	"asteroid": "A small planetary body in orbit around the Sun, larger than a meteoroid but smaller than a planet. Most asteroids can be found in a belt between the orbits of Mars and Jupiter. The orbits of some asteroids take them close to the Sun, which also takes them across the paths of the planets.",
	"asteroid belt": "collection of rocky objects situated between the orbits of Mars and Jupiter. These airless remnants failed to coalesce into a larger planet during the solar system's formation, approximately 4.6 billion years ago.",
	"astrochemistry": "The branch of science that explores the chemical interactions between dust and gas interspersed between the stars.",
	"astronomical unit": "A unit of measure equal to the average distance between the Earth and the Sun, approximately 93 million miles.",
	"astronomical filter": "(Filter) Is a specialized tool used by astronomers to selectively block specific wavelengths of light while allowing others to pass through. This enables them to study celestial objects in particular colors or to reduce the intensity of bright light sources. Similar to sunglasses that filter out harmful UV rays, astronomical filters help astronomers focus on specific details or features of celestial bodies.",
	"atmosphere": "A layer of gases surrounding a planet, moon, or star. The Earth's atmosphere is 120 miles thick and is composed mainly of nitrogen, oxygen, carbon dioxide, and a few other trace gases.",
	"atom": "An atom is the fundamental building block of matter. It's composed of a central nucleus containing protons (positively charged) and neutrons (neutral), surrounded by negatively charged electrons. The number of protons determines the type of element the atom represents.",
	"atomic nucleus": "The positively charged core of an atom consisting of protons and (except for hydrogen) neutrons, and around which electrons orbit.",
	"au": "Astronomical Unit, The average distance from Earth to the Sun, slightly less than 93 million miles (150 million kilometers).",
	"aurora": "A glow in a planet's ionosphere caused by the interaction between the planet's magnetic field and charged particles from the Sun. This phenomenon is known as the Aurora Borealis in the Earth's northern hemisphere and the Aurora Australis in the Earth's Southern Hemisphere.",
	"aurora australis": "Also known as the southern lights, this is an atmospheric phenomenon that displays a diffuse glow in the sky in the southern hemisphere. It is caused by charged particles from the Sun as they interact with the Earth's magnetic field. Known as the Aurora Borealis in the northern hemisphere.",
	"aurora borealis": "Also known as the northern lights, this is an atmospheric phenomenon that displays a diffuse glow in the sky in the northern hemisphere. It is caused by charged particles from the Sun as they interact with the Earth's magnetic field. Known as the Aurora Australis in the southern hemisphere.",
	"averted vision": "Viewing an object by looking slightly to its side. This technique can help you detect faint objects that are invisible when you stare directly at them.",
	"axis": "Also known as the poles, this is an imaginary line through the center of rotation of an object.",
	"azimuth": "The angular distance of an object around or parallel to the horizon from a predefined zero point.",
	"bar": "A unit of measure of atmospheric pressure. One bar is equal to 0.987 atmospheres, 1.02 kg/cm2, 100 kilopascal, and 14.5 lbs/square inch.",
	"barlow lens": "A lens that’s placed into the focusing tube to effectively double or triple a telescope’s focal length and, in turn, the magnification of any eyepiece used with it.",
	"big bang": "The theory that suggests that the universe was formed from a single point in space during a cataclysmic explosion about 13.7 billion years ago. This is the current accepted theory for the origin of the universe and is supported by measurements of background radiation and the observed expansion of space.",
	"binary": "A system of two stars that revolve around a common center of gravity.",
	"binary stars": "or (Binary Star System) A system of two stars orbiting around a common center of mass that are bound together by their mutual gravitational attraction.",
	"binary star system": "or (Binary Stars) Two stars orbiting around a common center of mass that are bound together by their mutual gravitational attraction.",
	"black body": "A blackbody is an idealized object that completely absorbs all light that hits it. It then re-emits this energy as heat, creating a unique pattern of light called a blackbody spectrum. Scientists use blackbody models to understand the behavior of hot, dense objects like stars and planets.",
	"blackbody spectrum": "or Blackbody radiation is the light emitted by any heated object. The color and intensity of this light directly correlate to the object's temperature. Hotter objects glow brighter and appear BLUEr, while cooler objects are dimmer and redder. By analyzing the blackbody spectrum, scientists can precisely determine an object's temperature.",
	"black hole": "The collapsed core of a massive star. Stars that are very massive will collapse under their own gravity when their fuel is exhausted. The collapse continues until all matter is crushed out of existence into what is known as a singularity. The gravitational pull is so strong that not even light can escape.",
	"black moon": "A term used to describe an extra new that occurs in a season. It usually refers to the third new moon in a season with four new moons. The term is sometimes used to describe a second new moon in a single month.",
	"blazar": "Essentially, blazars are a specific type of quasar seen from a particular angle, while quasars are a broader category of extremely luminous galaxies. Both are powered by supermassive black holes.",
	"BLUE dwarf": "These hot, massive, luminous stars burn through their fuel quickly. Since their lifetimes are short, they do not move very far from where they were born.",
	"BLUE moon": "A term used to describe an extra full that occurs in a season. It usually refers to the third full moon in a season with four full moons. Note that a BLUE moon does not actually appear BLUE in color. It is merely a coinsidence in timing caused by the fact that the lunar month is slightly shorter than a calendar month. More recently, the term has also been used to describe a second full moon in a single month.",
	"BLUEshift": "A shift in the lines of an object's spectrum toward the BLUE end. BLUEshift indicates that an object is moving toward the observer. The larger the BLUEshift, the faster the object is moving.",
	"bolide2": "A term used to describe an exceptionally bright meteor. Bolides typically will produce a sonic boom.",
	"brown dwarf": "A celestial object too small to be considered a star. Unlike stars, it lacks the mass needed to sustain nuclear fusion in its core, which is the process that powers stars and gives them their light. As a result, brown dwarfs gradually cool down over time. They are significantly smaller than the Sun, with a maximum mass about 8% that of our star.",
	"bulge central": "The spherical structure at the center of a spiral galaxy that is made up primarily of old stars, gas, and dust. The Milky Way’s bulge is roughly 15,000 light-years across.",
	"caldera": "A type of volcanic crater that is extremely large, usually formed by the collapse of a volcanic cone or by a violent volcanic explosion. Crater Lake is one example of a caldera on Earth.",
	"catena": "A series or chain of craters.",
	"carbon dioxide": "Carbon dioxide is a molecule made up of one carbon atom bonded to two oxygen atoms. It's a common substance found throughout the universe, existing as a gas or solid ice (dry ice) depending on the temperature.",
	"cavus": "A hollow, irregular depression.",
	"celestial coordinates": "A grid system for locating things in the sky. It’s anchored to the celestial poles (directly above Earth’s north and south poles) and the celestial equator (directly above Earth’s equator). Declination and right ascension are the celestial equivalents of latitude and longitude.",
	"celestial equator": "An imaginary line that divides the celestial sphere into a northern and southern hemisphere.",
	"celestial poles": "The North and South poles of the celestial sphere.",
	"celestial sphere": "An imaginary sphere around the Earth on which the stars and planets appear to be positioned.",
	"centaurs": "Centaurs are small icy bodies that have been ejected from the Kuiper Belt. They orbit the Sun between Jupiter and Neptune, crossing the paths of the giant planets.",
	"cepheid variable": "This is a variable star whose light pulsates in a regular cycle. The period of fluctuation is linked to the brightness of the star. Brighter Cepheids will have a longer period.",
	"chaos": "A distinctive area of broken terrain.",
	"chasma": "Another name used to describe a canyon.",
	"chemical evolution": "Is the gradual transformation of simple elements into the complex molecules needed for life. This process took place over immense periods of time and involved a series of chemical reactions. For example, the creation of heavier elements like helium from hydrogen within stars is an early step in this grand process.",
	"chondrite": "A meteorite that contains chondrules.",
	"chondrule": "Small, glassy spheres commonly found in meteorites.",
	"chromosphere": "The part of the Sun's atmosphere just above the surface.",
	"circumpolar": "Denotes an object near a celestial pole that never dips below the horizon as Earth rotates and thus does not rise or set.Denotes an object near a celestial pole that never dips below the horizon as Earth rotates and thus does not rise or set.",
	"circumpolar star": "A star that never sets but always stays above the horizon. This depends on the location of the observer. The further South you go the fewer stars will be circumpolar. Polaris, the North Star, is circumpolar in most of the northern hemisphere.",
	"circumstellar": "The habitable zone is the area around a star where conditions are suitable for liquid water to exist on a planet's surface. Planets closer to the star's edge of this zone would be warm enough to potentially have water in liquid form, while those on the outer edge would be cool enough to prevent water from boiling away but not so cold that it freezes entirely.",
	"circumstellar disk": "A torus or ring-shaped accumulation of gas, dust, or other debris in orbit around a star in different phases of its life cycle.",
	"coma": "An area of dust or gas surrounding the nucleus of a comet.",
	"comet": "A gigantic ball of ice and rock that orbit the Sun in a highly eccentric orbit. Some comets have an orbit that brings them close to the Sun where they form a long tail of gas and dust as they are heated by the Sun's rays.",
	"conjunction": "An event that occurs when two or more celestial objects appear close close together in the sky.",
	"constellation": "A grouping of stars that make an imaginary picture in the sky.",
	"comet": "Comets are icy bodies, often described as 'dirty snowballs', traveling through space. Their orbits around the Sun can be either one-time flybys or recurring paths like Halley's Comet. As they approach the Sun, they heat up and release gases, creating a dramatic, glowing tail.",
	"compound telescope": "A telescope with a mirror in the back and a lens in the front. The most popular designs are the Schmidt-Cassegrain telescope (SCT) and the Maksutov-Cassegrain telescope (commonly called a “Mak”).",
	"collimation": "Aligning the optical elements of a telescope so that they all point in the proper direction. Most reflectors and compound telescopes require occasional collimation in order to produce the best possible images.",
	"colliding galaxies": "(Interacting Galaxies) When galaxies pass close enough, their mutual gravitational pull can dramatically distort each other’s structures, creating elongated streams of stars. This violent interaction often sparks intense star formation and can ultimately lead to the complete merger of the two galaxies.",
	"constellation": "A geometric pattern of bright stars that appears grouped in the sky. Ancient observers named many constellations after gods, heroes, animals, and mythological beings.",
	"collecting area": "(mirror) The area of a telescope’s primary light-collecting mirror. A telescope’s light-gathering power rises withan increase in its collecting area.",
	"corona": "The outer part of the Sun's atmosphere. The corona is visible from Earth during a total solar eclipse. It is the bright glow seen in most solar eclipse photos.",
	"coronagraph": "An instrument designed to block out the direct light from a star so that surrounding objects which would otherwise be hidden in the star's glare can be observed.",
	"cosmic ray": "Atomic nuclei (mostly protons) that are observed to strike the Earth's atmosphere with extremely high amounts of energy.",
	"cosmic string": "A tube-like configuration of energy that is believed to have existed in the early universe. A cosmic string would have a thickness smaller than a trillionth of an inch but its length would extend from one end of the visible universe to the other.",
	"cosmochemistry": "is the scientific study of the chemical composition of celestial objects and the chemical processes occurring within them. It explores the universe's chemical makeup and how these substances change over time.",
	"cosmogony": "The study of celestial systems, including the Solar System, stars, galaxies, and galactic clusters.",
	"cosmology": "A branch of science that deals with studying the origin, structure, and nature of the universe.",
	"cosmological principle": "The universe is fundamentally uniform on a large scale. This means that no matter where you look in the cosmos, it appears the same. Just as the ocean looks similar from any boat, the universe looks similar from any vantage point. Extensive observations of matter and energy support this idea of a cosmic sameness.",
	"crater": "A bowl-shaped depression formed by the impact of an asteroid or meteoroid. Also the depression around the opening of a volcano.",
	"culmination": "The moment when a celestial object crosses the meridian and is thus at its highest above the horizon.",
	"dark adaptation": "The eyes’ transition to night vision, in order to see faint objects. Dark adaptation is rapid during the first 5 or 10 minutes after you leave a well-lit room, but full adaptation requires at least a half hour — and it can be ruined by a momentary glance at a bright light.",
	"dark ernegy": "Dark energy is the mysterious force counteracting gravity, causing the universe to expand at an accelerating rate.",
	"dark matter": "A term used to describe matter in the universe that cannot be seen, but can be detected by its gravitational effects on other bodies.",
	"debris disk": "A ring-shaped circumstellar disk of dust and debris in orbit around a star. Debris disks can be created as the next phase in planetary system development following the protoplanetary disk phase. They can also be formed by collisions between planetesimals.",
	"declination": "The angular distance of an object in the sky from the celestial equator.",
	"density": "The amount of matter contained within a given volume. Density is measured in grams per cubic centimeter (or kilograms per liter). The density of water is 1.0, iron is 7.9, and lead is 11.3.",
	"disk": "The surface of the Sun or other celestial body projected against the sky.",
	"digital image": "In essence, astronomical digital images are highly specialized versions of general digital images, tailored to the unique challenges and requirements of studying the cosmos. They demand greater precision, sensitivity, and data processing capabilities to extract valuable scientific information.",
	"diffraction grating": "is a component of a spectroscope. It's the part that actually splits the light into its component wavelengths.",
	"dispersion": "Property of light where different colors (wavelengths) bend at different angles when passing through a medium like glass or water. This bending, or refraction, causes white light to split into its constituent colors, as seen in a rainbow or when light passes through a prism. Shorter wavelengths (BLUE and violet) bend more than longer wavelengths (red and orange).",
	"debris disc": " It's a disk-shaped region around a star primarily composed of dust, with very little gas compared to protoplanetary disks. It's often compared to our solar system's Kuiper Belt.",
	"double asteroid": "Two asteroids that revolve around each other and are held together by the gravity between them. Also called a binary asteroid.",
	"doppler effect": "The apparent change in wavelength of sound or light emitted by an object in relation to an observer's position. An object approaching the observer will have a shorter wavelength (BLUE) while an object moving away will have a longer (RED) wavelength. The Doppler effect can be used to estimate an object's speed and direction.",
	"double star": "A grouping of two stars. This grouping can be apparent, where the stars seem close together, or physical, such as a binary system.",
	"dust": "(Astronomical dust) Is composed of tiny particles, ranging from the size of a few molecules to a few millimeters. These particles are typically made up of silicate grains (similar to sand) and polycyclic aromatic hydrocarbons (PAHs), which resemble soot. This cosmic dust is found in abundance throughout the universe, from within comets and asteroids to the vast spaces between stars. It plays a crucial role in various astronomical processes, such as star formation and the evolution of galaxies.",
	"dwarf galaxy": "A relatively small galaxy. The Large and Small Magellanic Clouds, visible in the Southern Hemisphere, are two dwarf irregular galaxies that are neighbors of the Milky Way.",
	"dwarf planet": "A celestial body orbiting the Sun that is massive enough to be rounded by its own gravity but has not cleared its neighboring region of planetesimals and is not a satellite. It has to have sufficient mass to overcome rigid body forces and achieve hydrostatic equilibrium. Pluto is considered to be a dwarf planet.",
	"eccentricity": "The measure of how an object's orbit differs from a perfect circle. Eccentricity defines the shape of an object's orbit.",
	"eclipse": "The total or partial blocking of one celestial body by another.",
	"eclipsing binary": "A binary system where one object passes in front of the other, cutting off some or all of its light.",
	"ecliptic": "An imaginary line in the sky traced by the Sun as it moves in its yearly path through the sky.",
	"ejecta": "Material from beneath the surface of a body such as a moon or planet that is ejected by an impact such as a meteor and distributed around the surface. Ejecta usually appear as a lighter color than the surrounding surface.",
	"electron": "A negatively charge elementary particle that typically resides outside the nucleus of an atom but is bound to it by electromagnetic forces. An electron’s mass is tiny: 1,836 electrons equals the mass of one proton",
	"electromagnetic radiation": "Another term for light. Light waves created by fluctuations of electric and magnetic fields in space.",
	"electromagnetic spectrum": "The full range of frequencies, from radio waves to gamma waves, that characterizes light.",
	"element": "Is a pure substance composed entirely of one type of atom. The defining characteristic of an element is its atomic number, which represents the number of protons in its nucleus. Elements exhibit unique chemical properties and there are approximately 90 naturally occurring elements on Earth.",
	"elementary particles": "Particles smaller than atoms that are the basic building blocks of the universe. The most prominent examples are photons, electrons, and quarks.",
	"elongation": "The angular distance the Moon or a planet is from the Sun. The inner planets of Mercury and Venus are best seen when at maximum elongation, and thus are highest above the horizon before sunrise or after sunset.",
	"emr": "EMR typically refers to Electromagnetic Radiation, a form of energy that travels through space in waves. It encompasses a wide range of wavelengths, from radio waves to gamma rays, including visible light.",
	"emission line": "Is a bright line in a spectrum caused by the emission of light at specific wavelengths. Each element produces a unique set of emission lines, acting like a fingerprint that allows scientists to identify the elements present in a celestial object.",
	"ellipse": "An ellipse is an oval shape. Johannes Kepler discovered that the orbits of the planets were elliptical in shape rather than circular.",
	"elliptical galaxy": "A galaxy whose structure shaped like an ellipse and is smooth and lacks complex structures such as spiral arms.",
	"elongation": "The angular distance of a planetary body from the Sun as seen from Earth. A planet at greatest eastern elongation is seen at its highest point above the horizon in the evening sky and a planet at greatest western elongation will be seen at its highest point above the horizon in the morning sky.",
	"ephemeris": "A table of data arranged by date. Ephemeris tables are typically to list the positions of the Sun, Moon, planets and other solar system objects.",
	"equinox": "The two points at which the Sun crosses the celestial equator in its yearly path in the sky. The equinoxes occur on or near March 21 and September 22. The equinoxes signal the start of the Spring and Autumn seasons.",
	"era of reionization": "(EOR) The early universe was shrouded in a dense fog of gas that blocked most of the light. This made it extremely difficult to observe the first galaxies. Scientists are still trying to understand what caused this fog to clear, allowing light to travel freely through space as it does today.",
	"earthshine": "Sunlight reflected by Earth that makes the otherwise dark part of the Moon glow faintly. It’s especially obvious during the Moon’s thin crescent phases.",
	"escape velocity": "The speed required for an object to escape the gravitational pull of a planet or other body.",
	"eor": "(Era of Reionization) The early universe was shrouded in a dense fog of gas that blocked most of the light. This made it extremely difficult to observe the first galaxies. Scientists are still trying to understand what caused this fog to clear, allowing light to travel freely through space as it does today.",
	"esa": "The European Space Agency (ESA) is an international collaboration of fifteen European countries dedicated to space exploration. With Canada as a partner, ESA designs, develops, and launches satellites. The agency also supports European astronomers in utilizing the Hubble Space Telescope through the Space Telescope-European Coordinating Facility (ST-ECF).",
	"event horizon": "The invisible boundary around a black hole past which nothing can escape the gravitational pull - not even light.",
	"evolved star": "A star that is near the end of its life cycle where most of its fuel has been used up. At this point the star begins to loose mass in the form of stellar wind.",
	"extinction": "The apparent dimming of star or planet when low on the horizon due to absorption by the Earth's atmosphere.",
	"extragalactic": "A term that means outside of or beyond our own galaxy.",
	"extraterrestrial": "A term used to describe anything that does not originate on Earth.",
	"excited state": "A greater-than-minimum energy state of any atom that is achieved when at least one of its electrons resides at a greater-than-normal distance from its parent nucleus.",
	"exposure": "Is the process of capturing light on a sensitive material like photographic film or a digital sensor. The resulting image is also referred to as an exposure. To capture faint, distant objects in space, long exposure times are necessary to gather enough light.",
	"exoplanet": "A planet that orbits a star other than the Sun.",
	"eyepiece": "The lens at the viewing end of a telescope. The eyepiece is responsible for enlarging the image captured by the instrument. Eyepieces are available in different powers, yielding differing amounts of magnification.",
	"f/number": "(Focal Ratio) A lens or mirror’s focal length divided by its aperture. For instance, a telescope with an 80-mm-wide lens and a 400-mm focal length has a focal ratio of f/5.",
	"faculae": "Bright patches that are visible on the Sun's surface, or photosphere.",
	"field of view": "The circle of sky that you see when you look through a telescope or binoculars. Generally, the lower the magnification, the wider the field of view.",
	"filament": "A strand of cool gas suspended over the photosphere by magnetic fields, which appears dark as seen against the disk of the Sun.",
	"filter": "Is a specialized tool used by astronomers to selectively block specific wavelengths of light while allowing others to pass through. This enables them to study celestial objects in particular colors or to reduce the intensity of bright light sources. Similar to sunglasses that filter out harmful UV rays, astronomical filters help astronomers focus on specific details or features of celestial bodies.",
	"finder": "A small, wide-field telescope attached to a larger telescope. The finder is used to help point the larger telescope to the desired viewing location.",
	"fireball": "An extremely bright meteor. Also known as bolides, fireballs can be several times brighter than the full Moon. Some can even be accompanied by a sonic boom.",
	"fission": "A nuclear process that releases energy when heavyweight atomic nuclei break down into lighter nuclei. Fission is the basis of the atomic bomb.",
	"flare star": "A faint RED star that appears to change in brightness due to explosions on its surface.",
	"focal length": "The distance (usually expressed in millimeters) from a mirror or lens to the image that it forms. In most telescopes the focal length is roughly equal to the length of the tube. Some telescopes use extra lenses and/or mirrors to create a long effective focal length in a short tube.",
	"focal ratio": "(f/number) A lens or mirror’s focal length divided by its aperture. For instance, a telescope with an 80-mm-wide lens and a 400-mm focal length has a focal ratio of f/5.",
	"fusion": "A nuclear process that releases energy when light atomic nuclei combine to form heavier nuclei. Fusion is the energy source for stars like our sun.",
	"g-type star": "A G-type star is a main-sequence star, like our Sun, that produces energy by fusing hydrogen into helium. They are often called 'YELLOW dwarfs', though their color can range from white to slightly YELLOW. These stars are relatively stable and have lifespans long enough for planets to develop and potentially support life.",
	"galactic halo": "The name given to the spherical region surrounding the center, or nucleus of a galaxy.",
	"galactic nucleus": "A tight concentration of stars and gas found at the innermost regions of a galaxy. Astronomers now believe that massive black holes may exist in the center of many galaxies.",
	"galact center": "The central hub or nucleus of a galaxy. The Milky Way’s galactic center is about 28,000 light-years from Earth",
	"galaxy": "A large grouping of stars. Galaxies are found in a variety of sizes and shapes. Our own Milky Way galaxy is spiral in shape and contains several billion stars. Some galaxies are so distant the their light takes millions of years to reach the Earth.",
	"galaxy cluster": "A collection of dozens to thousands of galaxies bound together by gravity.",
	"galaxy evolution": "The study of the birth of galaxies and how they change and develop over time.",
	"galaxy superclusters": "Are immense cosmic structures containing tens of thousands of galaxies spread across hundreds of millions of light-years. They represent the largest known organized structures in the universe.",
	"galilean moons": "The name given to Jupiter's four largest moons, Io, Europa, Callisto, and Ganymede. They were discovered independently by Galileo Galilei and Simon Marius.",
	"gamma-ray": "The highest energy, shortest wavelength form of electromagnetic radiation.",
	"gas giant": "Are massive planets primarily composed of hydrogen and helium. Unlike Earth-like planets with solid surfaces, these planets have thick, swirling atmospheres surrounding a small, dense core. They can be significantly larger than Jupiter and orbit much closer to their stars than any planet in our solar system.",
	"geosynchronous orbit": "An orbit in which a satellite's orbital velocity is matched to the rotational velocity of the planet. A spacecraft in geosynchronous orbit appears to hang motionless above one position of a planet's surface.",
	"giant molecular cloud": "(GMC) Massive clouds of gas in interstellar space composed primarily of hydrogen molecules. These clouds have enough mass to produce thousands of stars and are frequently the sites of new star formation.",
	"gibbous": "When the Moon or other body appears more than half, but not fully, illuminated (from gibbus, Latin for “hump”).",
	"globular cluster": "A tight, spherical grouping of hundreds of thousands of stars. Globular clusters are composed of older stars, and are usually found around the central regions of a galaxy.",
	"goddard space flight center": "(GSFC) in GREENbelt, Maryland, is a hub for space exploration and research. It oversees operations of telescopes like Hubble, receiving and processing data. This data is then sent to the Space Telescope Science Institute for image creation. In addition to data management, Goddard is at the forefront of space technology development and scientific discovery.",
	"granulation": "A pattern of small cells that can be seen on the surface of the Sun. They are caused by the convective motions of the hot gases inside the Sun.",
	"gravitational clustering": "Is the process by which massive structures in the universe, like galaxies and galaxy clusters, form. Over time, the force of gravity pulls together smaller clumps of matter, causing them to grow and merge into larger structures. This ongoing process is believed to be responsible for the cosmic web of galaxies we observe today.",
	"gravitational lens": "A concentration of matter such as a galaxy or cluster of galaxies that bends light rays from a background object. Gravitational lensing results in duplicate images of distant objects.",
	"gravitational waves": "Gravitational waves are tiny ripples in the fabric of spacetime caused by extremely violent cosmic events like colliding black holes or exploding stars. These waves carry information about their origins and offer clues about gravity.",
	"gravity": "A mutual physical force of nature that causes two bodies to attract each other.",
	"GREENhouse effect": "An increase in temperature caused when incoming solar radiation is passed but outgoing thermal radiation is blocked by the atmosphere. Carbon dioxide and water vapor are two of the major gases responsible for this effect.",
	"gsfc": "Goddard Space Flight Center in GREENbelt, Maryland, is a hub for space exploration and research. It oversees operations of telescopes like Hubble, receiving and processing data. This data is then sent to the Space Telescope Science Institute for image creation. In addition to data management, Goddard is at the forefront of space technology development and scientific discovery.",
	"habitable zone": "Is the area around a star where conditions are suitable for liquid water to exist on a planet's surface. Planets closer to the star's edge of this zone would be warm enough to potentially have water in liquid form, while those on the outer edge would be cool enough to prevent water from boiling away but not so cold that it freezes entirely.",
	"heliopause": "The point in space at which the solar wind meets the interstellar medium or solar wind from other stars.",
	"heliosphere": "The space within the boundary of the heliopause containing the Sun and the Solar System.",
	"hot jupiter": "A planet that is physically similar to Jupiter, orbiting close to its host star with an orbital period of less than 10 days.",
	"hubble constant": "A number that expresses the rate at which the universe expands with time. (v = H0 * d) appears to be between 60 and 75 kilometers per second per megaparsec",
	"hubble law": "The law of physics (v = H0 * d) that states that the farther a galaxy is from us, the faster it is moving away from us.",
	"hubble's law": "The law of physics (v = H0 * d) that states that the farther a galaxy is from us, the faster it is moving away from us.",
	"hubble space telescope": "(HST) A space telescope capturing visible, ultraviolet, and near-infraRED light from celestial bodies using an 8-foot primary mirror. It orbits Earth every 96 minutes, powered by solar energy.",
	"hst": "(Hubble Space Telescope) A space telescope capturing visible, ultraviolet, and near-infraRED light from celestial bodies using an 8-foot primary mirror. It orbits Earth every 96 minutes, powered by solar energy.",
	"hydrogen": "An element consisting of one electron and one proton. Hydrogen is the lightest of the elements and is the building block of the universe. Stars form from massive clouds of hydrogen gas.",
	"hydrostatic equilibrium": "A state that occurs when compression due to gravity is balanced by a pressure gradient which creates a pressure gradient force in the opposite direction. Hydrostatic equilibrium is responsible for keeping stars from imploding and for giving planets their spherical shape.",
	"hypergalaxy": "A system consisting of a spiral galaxy surrounded by several dwarf white galaxies, often ellipticals. Our galaxy and the Andromeda galaxy are examples of hypergalaxies.",
	"ice": "A term used to describe water or a number of gases such as methane or ammonia when in a solid state.",
	"ice giant": "Giant planets are primarily composed of hydrogen and helium gas, enveloping a core of rock and heavy metals. Uranus and Neptune, categorized as ice giants, differ by containing significant amounts of oxygen, carbon, nitrogen, and sulfur.",
	"inclination": "A measure of the tilt of a planet's orbital plane in relation to that of the Earth.",
	"infrared radiation": "(IR) Radiation that has longer wavelengths and lower frequencies and energies than visible light.",
	"infrared light": "InfraRED light is a type of invisible radiation with less energy than visible light. Similar to how our ears can't detect low-pitched sounds, our eyes can't perceive this lower-energy light. However, we can feel it as heat, especially from warm-blooded creatures.",
	"infrared telescope": "An instrument that collects the infrared radiation emitted by celestial objects. There are several Earth and space-based infrared observatories.",
	"inferior conjunction": "A conjunction of an inferior planet that occurs when the planet is lined up directly between the Earth and the Sun.",
	"inferior planet": "A planet that orbits between the Earth and the Sun. Mercury and Venus are the only two inferior planets in our solar system.",
	"international astronomical union": "(IAU) An international organization that unites national astronomical societies from around the world and acts as the internationally recognized authority for assigning designations to celestial bodies and their surface features.",
	"interacting galaxies": "Colliding Galaxies) When galaxies pass close enough, their mutual gravitational pull can dramatically distort each other’s structures, creating elongated streams of stars. This violent interaction often sparks intense star formation and can ultimately lead to the complete merger of the two galaxies.",
	"interplanetary magnetic field": "The magnetic field carried along with the solar wind.",
	"interstellar dust": "Tiny solid particles suspended in the vastness of space between stars, known as interstellar dust, scatter and redden visible starlight. While effectively blocking ultraviolet radiation, these particles allow longer infrared wavelengths to pass through.",
	"interstellar medium": "The gas and dust that exists in open space between the stars.",
	"invisible radiation": "Radiation that the eye cannot detect, such as gamma rays, radio waves, ultraviolet light, and X-rays.",
	"ion": "An atom with one or more electrons removed (or added), giving the atom a positive (or negative) charge.",
	"ionization": "The process by which ions are produced, typically by collisions with other atoms or electrons, or by absorption of electromagnetic radiation.",
	"ionosphere": "A region of charged particles in a planet's upper atmosphere. In Earth's atmosphere, the ionosphere begins at an altitude of about 25 miles and extends outward about 250.",
	"iron meteorite": "A meteorite that is composed mainly of iron mixed with smaller amounts of nickel.",
	"irregular galaxy": "A galaxy with no spiral structure and no symmetric shape. Irregular galaxies are usually filamentary or very clumpy in shape.",
	"irregular satellite": "A satellite that orbits a planet far away with an orbit that is eccentric and inclined. They also tend to have retrograde orbits. Irregular satellites are believed to have been captuRED by the planet's gravity rather than being formed along with the planet.",
	"jansky": "A unit used in radio astronomy to indicate the flux density (the rate of flow of radio waves) of electromagnetic radiation received from outer space. A typical radio source has a spectral flux density of roughly 1 Jy. The jansky was named to honor Karl Gothe Jansky who developed radio astronomy in 1932.",
	"jets": "A narrow stream of gas or particles ejected from an accretion disk surrounding a star or black hole.",
	"kelvin": "A temperature scale used in sciences such as astronomy to measure extremely cold temperatures. The Kelvin temperature scale is just like the Celsius scale except that the freezing point of water, zero degrees Celsius, is equal to 273 degrees Kelvin. Absolute zero, the coldest known temperature, is reached at 0 degrees Kelvin or -273.16 degrees Celsius.",
	"keplers first law": "A planet orbits the Sun in an ellipse with the Sun at one focus.",
	"keplers second law": "A ray directed from the Sun to a planet sweeps out equal areas in equal times.",
	"keplers third law": "The square of the period of a planet's orbit is proportional to the cube of that planet's semi major axis; the constant of proportionality is the same for all planets.",
	"kilonova": "A cataclysmic explosion occurs when two neutron stars or a neutron star and a black hole collide. Scientists believe these mergers are also the source of short-lived gamma-ray bursts.",
	"kiloparsec": "A distance equal to 1000 parsecs.",
	"kirkwood gaps": "Regions in the main belt of asteroids where few or no asteroids are found. They were named after the scientist who first noticed them.",
	"kuiper belt": "(Object) A large ring of icy, primitive objects beyond the orbit of Neptune. Kuiper Belt objects are believed to be remnants of the original material that formed the Solar System. Some astronomers believe Pluto and Charon are Kuiper Belt objects.",
	"L2 orbit": "Situated directly opposite the Earth from the Sun, L2 is the second Lagrange point. There are a total of five such points where the gravitational influence of two celestial bodies creates stable positions for a third, smaller object to orbit without drifting away.",
	"lagrange point": "French mathematician and astronomer Joseph Louis Lagrange showed that three bodies could lie at the apexes of an equilateral triangle which rotates in its plane. If one of the bodies is sufficiently massive compared with the other two, then the triangular configuration is apparently stable. Such bodies are sometimes referred to as Trojans. The leading apex of the triangle is known as the leading Lagrange point or L4; the trailing apex is the trailing Lagrange point or L5.",
	"lenticular galaxy": "A disk-shaped galaxy that contains no conspicuous structure within the disk. Lenticular galaxies tend to look more like elliptical galaxies than spiral galaxies.",
	"libration": "An effect caused by the apparent wobble of the Moon as it orbits the Earth. The Moon always keeps the same side toward the Earth, but due to libration, 59% of the Moon's surface can be seen over a period of time.",
	"light curve": "A graph showing the brightness of an object over time.",
	"light year": "An astronomical unit of measure equal to the distance light travels in a year, approximately 5.8 trillion miles.",
	"limb": "The outer edge or border of a planet or other celestial body.",
	"local group": "A small group of about two dozen galaxies of which our own Milky Way galaxy is a member.",
	"luminosity": "The amount of light emitted by a star.",
	"lunar Eclipse": "A phenomenon that occurs when the Moon passes into the shadow of the Earth. A partial lunar eclipse occurs when the Moon passes into the penumbra, or partial shadow. In a total lunar eclipse, the Moon passes into the Earth's umbra, or total shadow.",
	"lunar month": "The average time between successive new or full moons. A lunar month is equal to 29 days 12 hours 44 minutes. Also called a synodic month.",
	"lunation": "The interval of a complete lunar cycle, between one new Moon and the next. A lunation is equal to 29 days, 12 hours, and 44 minutes.",
	"m dwarf": "(RED Dwarf Star) An M dwarf is a small, cool star, the most common type in the universe. It's much smaller and dimmer than our Sun, often fully convective, and potentially hosts Earth-sized planets in its habitable zone.",
	"magellanic clouds": "Two small, irregular galaxies found just outside our own Milky Way galaxy. The Magellanic Clouds are visible in the skies of the southern hemisphere.",
	"magnetic field": "A condition found in the region around a magnet or an electric current, characterized by the existence of a detectable magnetic force at every point in the region and by the existence of magnetic poles.",
	"magnetic pole": "Either of two limited regions in a magnet at which the magnet's field is most intense.",
	"magnetosphere": "The area around a planet most affected by its magnetic field. The boundary of this field is set by the solar wind.",
	"magnitude": "The degree of brightness of a star or other object in the sky according to a scale on which the brightest star has a magnitude -1.4 and the faintest visible star has magnitude 6. Sometimes referred to as apparent magnitude. In this scale, each number is 2.5 times the brightness of the previous number. Thus a star with a magnitude of 1 is 100 times brighter than on with a visual magnitude of 6.",
	"magnification": "The amount that a telescope enlarges its subject. It’s equal to the telescope’s focal length divided by the eyepiece’s focal length.",
	"main asteroid belt": "collection of rocky objects situated between the orbits of Mars and Jupiter. These airless remnants failed to coalesce into a larger planet during the solar system's formation, approximately 4.6 billion years ago.",
	"main belt": "The area between Mars and Jupiter where most of the asteroids in our solar system are found.",
	"main sequence star": "Is a typical star that generates energy by fusing hydrogen into helium within its core. This stable phase constitutes the majority of a star's lifespan and is represented by a diagonal band on the Hertzsprung-Russell diagram.",
	"major planet": "A name used to describe any planet that is considerably larger and more massive than the Earth, and contains large quantities of hydrogen and helium. Jupiter and Neptune are examples of major planets.",
	"mare": "A term used to describe a large, circular plain. The word mare means 'sea'. On the Moon, the maria are the smooth, dark-colored areas.",
	"mass": "A measure of the total amount of material in a body, defined either by the inertial properties of the body or by its gravitational influence on other bodies.",
	"matter": "A word used to describe anything that contains mass.",
	"megaparsec": "Equals one million parsecs (3.26 million light-years) and is the unit of distance commonly used to measure the distance between galaxies.",
	"meridian": "An imaginary circle drawn through the North and South poles of the celestial equator.",
	"messier object": "An entry in a catalog of 103 star clusters, nebulas, and galaxies compiled by French comet hunter Charles Messier (mess-YAY) between 1758 and 1782. The modern-day Messier catalog contains 109 objects.",
	"metal": "(in Astronomy) A term used by astronomers to describe all elements except hydrogen and helium, as in the universe is composed of hydrogen, helium and traces of metals. This astronomical definition is quite different from the traditional chemistry definition of a metal.",
	"meteor": "A small particle of rock or dust that burns away in the Earth's atmosphere. Meteors are also referred to as shooting stars.",
	"meteor shower": "An event where a large number of meteors enter the Earth's atmosphere from the same direction in space at nearly the same time. Most meteor showers take place when the Earth passes through the debris left behind by a comet.",
	"meteorite": "An object, usually a chunk or metal or rock, that survives entry through the atmosphere to reach the Earth's surface. Meteors become meteorites if they reach the ground.",
	"meteoroid": "A small, rocky object in orbit around the Sun, smaller than an asteroid.",
	"methane": "Simple molecule composed of one carbon atom bonded to four hydrogen atoms. On Earth, it exists as a colorless, odorless gas that is the primary component of natural gas. However, in the frigid, airless environment of space, methane solidifies into a white substance that can vaporize when exposed to sunlight.",
	"micron": "Is a unit of measurement equaling one-millionth of a meter. This is equivalent to 0.000001 meters or 10^-6 meters. To put it in perspective, a micron is ten times larger than a nanometer.",
	"micrometer": "Is a unit of measurement equaling one-millionth of a meter. This is equivalent to 0.000001 meters or 10^-6 meters. To put it in perspective, a micron is ten times larger than a nanometer.",
	"microwaves": "Type of invisible light energy. They occupy a range on the electromagnetic spectrum between infrared and radio waves, with wavelengths spanning from one millimeter to one meter.",
	"millibar": "A measure of atmospheric pressure equal to 1/1000 of a bar. Standard sea-level pressure on Earth is about 1013 millibars.",
	"milky way": "Our home (Galaxy), the Milky Way, is a vast, spiral-shaped collection of over 100 billion stars. Stretching across an immense 100,000 light-years, it's a cosmic island where Earth resides.",
	"minor planet": "A term used since the 19th century to describe objects, such as asteroids, that are in orbit around the Sun but are not planets or comets. In 2006, the International Astronomical Union reclassified minor planets as either dwarf planets or small solar system bodies.",
	"molecular cloud": "An interstellar cloud of molecular hydrogen containing trace amounts of other molecules such as carbon monoxide and ammonia.",
	"muon": "These are “cousins” of electrons but with a much shorter lifespan. Unlike electrons which exist indefinitely, muons have an extremely brief existence, lasting only about 2.2 millionths of a second before they decay.",
	"nancy grace roman space telescope": "The Nancy Grace Roman Space Telescope is a NASA infrared observatory with a 2.4-meter mirror designed to study dark energy, exoplanets, and the infrared universe. Its wide field of view will enable it to survey vast cosmic regions and discover numerous exoplanets.",
	"nadir": "A term used to describe a point directly underneath an object or body.",
	"nanometer": "A nanometer is an extremely small unit of measurement, equal to one billionth of a meter. To put it into perspective (0.000000001 meters), it's one-thousandth of a micron.",
	"nebula": "A cloud of dust and gas in space, usually illuminated by one or more stars. Nebulae represent the raw material the stars are made of.",
	"neutrino": "A fundamental particle produced by the nuclear reactions in stars. Neutrinos are very hard to detect because the vast majority of them pass completely through the Earth without interacting.",
	"neutron": "Is a fundamental particle without an electric charge. Slightly heavier than a proton, it resides within the nucleus of every atom except hydrogen.",
	"neutron star": "A compressed core of an exploded star made up almost entirely of neutrons. Neutron stars have a strong gravitational field and some emit pulses of energy along their axis. These are known as pulsars.",
	"newton first law of motion": "A body continues in its state of constant velocity (which may be zero) unless it is acted upon by an external force.",
	"newton second law of motion": "For an unbalanced force acting on a body, the acceleration produced is proportional to the force impressed; the constant of proportionality is the inertial mass of the body.",
	"newton third law of motion": "In a system where no external forces are present, every action force is always opposed by an equal and opposite reaction.",
	"nova": "A star that flares up to several times its original brightness for some time before returning to its original state.",
	"nuclear fusion": "The nuclear process whereby several small nuclei are combined to make a larger one whose mass is slightly smaller than the sum of the small ones. Nuclear fusion is the reaction that fuels the Sun, where hydrogen nuclei are fused to form helium.",
	"observable universe": "The portion of the entire universe that can be seen from Earth.",
	"observatory": "Specialized facility designed for observing and studying celestial or terrestrial phenomena. It's equipped with instruments like telescopes, which gather and analyze light or other forms of radiation to provide data about distant objects or atmospheric conditions.",
	"obliquity": "The angle between a body's equatorial plane and orbital plane.",
	"oblateness": "A measure of flattening at the poles of a planet or other celestial body.",
	"occultation": "(Secondary Eclipse) An event that occurs when one celestial body conceals or obscures another. For example, a solar eclipse is an occultation of the Sun by the Moon.",
	"oort cloud": "A theoretical shell of comets that is believed to exist at the outermost regions of our solar system. The Oort cloud was named after the Dutch astronomer who first proposed it.",
	"one-dimensional spectrum": "A one-dimensional spectrum graphically displays how a property varies across a single factor, like wavelength or energy. It's essentially a line chart showing changes in value along a line.",
	"open cluster": "A collection of young stars that formed together. They may or may not be still bound by gravity. Some of the youngest open clusters are still embedded in the gas and dust from which they formed.",
	"opposition": "The position of a planet when it is exactly opposite the Sun in the sky as seen from Earth. A planet at opposition is at its closest approach to the Earth and is best suitable for observing.",
	"opacity": "Is the measure of how much a material blocks light. It's the opposite of transparency. A high opacity means little light passes through, while low opacity allows more light to penetrate.",
	"orbit": "The path of a celestial body as it moves through space.",
	"parallax": "The apparent change in position of two objects viewed from different locations.",
	"parsec": "A large distance often used in astronomy. A parsec is equal to 3.26 light-years.",
	"patera": "A shallow crater with a complex, scalloped edge.",
	"penumbra": "The area of partial illumination surrounding the darkest part of a shadow caused by an eclipse.",
	"perigee": "The point in the orbit of the Moon or other satellite at which it is closest to the Earth.",
	"perihelion": "The point in the orbit of a planet or other body where it is closest to the Sun.",
	"perturb": "To cause a planet or satellite to deviate from a theoretically regular orbital motion.",
	"phase": "The apparent change in shape of the Moon and inferior planets as seen from Earth as they move in their orbits.",
	"phase curve": "Depicts how an object's brightness changes as its orientation to a light source and observer varies. It's essential for studying celestial bodies' properties, such as surface composition and atmospheric conditions.",
	"photon": "A particle of light composed of a minute quantity of electromagnetic energy.",
	"photosphere": "The bright visible surface of the Sun.",
	"photodissociation": "Is the process where molecules break apart into smaller fragments due to absorbing energy from light. This energy, often from ultraviolet radiation, overcomes the chemical bonds holding the molecule together.",
	"photometry": "Is the science of measuring light, specifically how bright it appears to the human eye. It involves quantifying the amount of light emitted, transmitted, or received by an object.",
	"parhelion": "or sundog. Atmospheric optical phenomenon that consists of a bright spot to one or both sides of the Sun. Two sun dogs often flank the Sun within a 22° halo.",
	"parallax": "The visible displacement of an object in the foreground when observed from different angles. This phenomenon is evident in the apparent movement of the Moon against the backdrop of stars as viewed from various points on Earth. Astronomers exploit this principle to measure the distance to nearby stars by tracking their minute positional shifts caused by Earth's orbital motion.",
	"planemo": "A large planet or planetary body that does not orbit a star. Planemos instead wander cold and alone through the cosmos. It is believed that most planemos once orbited their mother star but were ejected from the star system by gravitational interaction with another massive object.",
	"planet": "A celestial body orbiting a star or stellar remnant that is massive enough to be rounded by its own gravity, is not massive enough to cause thermonuclear fusion, and has cleared its neighboring region of planetesimals.",
	"planetary nebula": "A shell of gas surrounding a small, white star. The gas is usually illuminated by the star, producing a variety of colors and shapes.",
	"planetesimal": "A solid object that is believed to exist in protoplanetary disks and in debris disks. Planetesimals are formed from small dust grains that collide and stick together and are the building blocks that eventually form planets in new planetary systems.",
	"planck curve": "A Planck curve illustrates the amount of energy emitted by a perfect black body at different wavelengths. The curve's shape and peak position depend on the object's temperature.",
	"planisphere": "A device that can be adjusted to show the appearance of the night sky for any time and date on a round star map. Planispheres can be used to identify stars and constellations but not the planets, whose positions are always changing.",
	"planum": "A high plain or plateau.",
	"plasma": "A form of ionized gas in which the temperature is too high for atoms to exist in their natural state. Plasma is composed of free electrons and free atomic nuclei.",
	"precession": "The apparent shift of the celestial poles caused by a gradual wobble of the Earth's axis.",
	"prominence": "An explosion of hot gas that erupts from the Sun's surface. Solar prominences are usually associated with sunspot activity and can cause interference with communications on Earth due to their electromagnetic effects on the atmosphere.",
	"prograde orbit": "In reference to a satellite, a prograde orbit means that the satellite orbits the planet in the same direction as the planet's rotation. A planet is said to have a prograde orbit if the direction of its orbit is the same as that of the majority of other planets in the system.",
	"proper motion": "The apparent angular motion across the sky of an object relative to the Solar System.",
	"proton": "A positively charged elementary particle that resides in the nucleus of every atom.",
	"protoplanet": "Is a large celestial body formed within a protoplanetary disk that is in the process of becoming a planet. It's essentially a planetary embryo that grows through the accumulation of smaller objects.",
	"protoplanetary disk": "A rotating circumstellar disk of dense gas surrounding a young newly formed star. It is thought that planets are eventually formed from the gas and dust within the protoplanetary disk.",
	"protostar": "Dense regions of molecular clouds where stars are forming.",
	"population iii stars": "Population III stars are the universe's first stars, formed from pristine gas without any heavier elements. These massive, short-lived giants enriched the cosmos with elements heavier than hydrogen and helium, laying the groundwork for subsequent star generations.",
	"pulsar": "A spinning neutron star that emits energy along its gravitational axis. This energy is received as pulses as the star rotates.",
	"quadrature": "A point in the orbit of a superior planet where it appears at right angles to the Sun as seem from Earth.",
	"quasar": "An unusually bright object found in the remote areas of the universe. Quasars release incredible amounts of energy and are among the oldest and farthest objects in the known universe. They may be the nuclei of ancient, active galaxies.",
	"quadrant": "A quadrant is one of the four equal parts created by intersecting a plane with two perpendicular lines. The most common example is in a two-dimensional Cartesian coordinate system, where the x-axis and y-axis divide the plane into four quadrants. Each quadrant is labeled with a roman numeral (I, II, III, and IV) and has specific sign conventions for its coordinates.",
	"quasi-stellar object": "Sometimes also called quasi-stellar source, this is a star-like object with a large REDshift that gives off a strong source of radio waves. They are highly luminous and presumed to be extragalactic.",
	"radial velocity": "The movement of an object either towards or away from a stationary observer.",
	"radiant": "A point in the sky from which meteors in a meteor shower seem to originate.",
	"radiation": "Energy radiated from an object in the form of waves or particles.",
	"radiation belt": "Regions of charged particles in a magnetosphere.",
	"radio galaxy": "A galaxy that gives off large amounts of energy in the form of radio waves.",
	"reionization": "Is the cosmic event when the universe's neutral hydrogen gas was transformed back into ionized plasma by the intense radiation from the first stars and galaxies, ending the cosmic 'dark ages.'",
	"RED dwarf star": "(M dwarf) Is a small, cool star, the most common type in the universe. It's much smaller and dimmer than our Sun, often fully convective, and potentially hosts Earth-sized planets in its habitable zone.",
	"RED giant": "A stage in the evolution of a star when the fuel begins to exhaust and the star expands to about fifty times its normal size. The temperature cools, which gives the star a reddish appearance.",
	"REDshift": "A shift in the lines of an object's spectrum toward the RED end. REDshift indicates that an object is moving away from the observer. The larger the REDshift, the faster the object is moving.",
	"regular satellite": "A satellite that orbits close to a planet in a nearly circular, equatorial orbit. Regular satellites are believed to have been formed at the same time as the planet, unlike irregular satellites which are believed to have been captured by the planet's gravity.",
	"relativity": "Relativity is a physics theory (E = mc2) which expresses a relationship between mass (m), energy (E), and the speed of light (c). Explaining how space and time are linked, influenced by gravity and speed. It consists of special relativity (for constant motion) and general relativity (incorporating gravity).",
	"resolving power": "Is a measure of an instrument's ability to distinguish between closely spaced objects.",
	"resonance": "A state in which an orbiting object is subject to periodic gravitational perturbations by another.",
	"retrograde": "Motion in the opposite direction of normal. Most solar system bodies orbit and rotate counterclockwise, but those moving clockwise exhibit retrograde motion. This can also describe a planet's apparent backward movement due to Earth's orbital position.",
	"retrograde motion": "The phenomenon where a celestial body appears to slow down, stop, them move in the opposite direction. This motion is caused when the Earth overtakes the body in its orbit.",
	"retrograde orbit": "The orbit of a satellite where the satellite travels in a direction opposite to that direction of the planet's rotation.",
	"right ascension": "The amount of time that passes between the rising of Aries and another celestial object. Right ascension is one unit of measure for locating an object in the sky.",
	"ring galaxy": "A galaxy that has a ring-like appearance. The ring usually contains luminous BLUE stars. Ring galaxies are believed to have been formed by collisions with other galaxies.",
	"ring system": "A disk or ring orbiting an astronomical object that is composed of solid material such as dust and moonlets, and is a common component of satellite systems around giant planets.",
	"roche limit": "The smallest distance from a planet or other body at which purely gravitational forces can hold together a satellite or secondary body of the same mean density as the primary. At a lesser distance the tidal forces of the primary would break up the secondary.",
	"roman space telescope": "Is a NASA observatory (is a near-infraRED telescope with a 2.4-meter (7.8-foot) primary mirror) designed to study dark energy, exoplanets, and infraRED astrophysics. It will have a much wider field of view than Hubble, allowing it to observe vast areas of the sky and potentially discover thousands of new exoplanets.",
	"rotation": "The spin of a body about its axis.",
	"saber beads": "Broken arc of illuminations seen at the limb of very young or old lunar crescents. The visual similarity to the moments before and after a total solar eclipse was first noted by American astronomer Stephen Saber.",
	"saros series": "Also known as a saros cycle, a period of 223 synodic months that can be used to predict solar and lunar eclipses. The saros cycle is equal to 6,585.3 days (18 years 11 days 8 hours).",
	"satellite": "A natural or artificial body in orbit around a planet.",
	"scarp": "A line of cliffs produced erosion or by the action of faults.",
	"secondary eclipse": "(Occultation) A secondary eclipse occurs when a planet passes behind its host star, blocking the planet's emitted light. This event allows scientists to study the planet's atmosphere and temperature by measuring the decrease in overall brightness.",
	"seyfert galaxy": "A type of spiral galaxy which has a small, compact nucleus that is much brighter than the rest of the galaxy. The nucleus exhibits variable light intensity and radio emission suggesting that a black hole may be devouring material at the galaxy's center.",
	"shell star": "A type of star which is believed to be surrounded by a thin envelope of gas, which is often indicated by bright emission lines in its spectrum.",
	"shock wave": "A powerful pressure wave that travels faster than the speed of sound. It's created by sudden, violent disturbances like explosions or supersonic objects. Unlike sound waves, shock waves cause abrupt changes in pressure, temperature, and density.",
	"shepherd satellite": "A satellite that constrains the extent of a planetary ring through gravitational forces. Also known as a shepherd moon.",
	"sidereal": "Of, relating to, or concerned with the stars. Sidereal rotation is that measured with respect to the stars rather than with respect to the Sun or the primary of a satellite.",
	"sidereal month": "The average period of revolution of the Moon around the Earth in reference to a fixed star, equal to 27 days, 7 hours, 43 minutes in units of mean solar time.",
	"sidereal period": "The period of revolution of a planet around the Sun or a satellite around its primary.",
	"singularity": "The center of a black hole, where the curvature of space time is maximal. At the singularity, the gravitational tides diverge. Theoretically, no solid object can survive hitting the singularity.",
	"snow line": "The snow line is the lowest elevation where snow persists year-round. It varies by location and is influenced by factors like latitude, altitude, and climate.",
	"small solar system body": "A term defined in 2006 by the International Astronomical Union to describe objects in the Solar System that are neither planets or dwarf planets. These include most of the asteroids, comets, and other small bodies in the Solar System.",
	"solar system": "The eight planets orbiting the Sun, along with dwarf planets, asteroids, comets, and dust. Our cosmic neighborhood...",
	"solar cycle": "The approximately 11-year quasi-periodic variation in frequency or number of solar active events.",
	"solar eclipse": "A phenomenon that occurs when the Earth passes into the shadow of the Moon. A total solar eclipse occurs when the Moon is close enough to completely block the Sun's light. An annular solar eclipse occurs when the Moon is farther away and is not able to completely block the light. This results in a ring of light around the Moon.",
	"solar flare": "A bright eruption of hot gas in the Sun's photosphere. Solar prominences are usually only detectable by specialized instruments but can be visible during a total solar eclipse.",
	"solar mass": "A solar mass is a unit of measurement used in astronomy to describe the mass of stars and other celestial bodies. It's equal to the mass of our Sun, approximately 2 x 10^30 kilograms.",
	"solar nebula": "The cloud of dust and gas out of which the Solar System was believed to have formed about 5 billion years ago.",
	"solar wind": "A flow of charged particles that travels from the Sun out into the Solar System.",
	"solstice": "The time of the year when the Sun appears furthest north or south of the celestial equator. The solstices mark the beginning of the Summer and Winter seasons.",
	"space-time": "The four-dimensional coordinate system (three dimensions of space and one of time) in which physical events are located. Is a unified concept combining space and time into a single framework. It forms the foundation of Einstein's relativity theory, describing how gravity influences the shape of spacetime itself.",
	"spectrometer": "The instrument connected to a telescope that separates the light signals into different frequencies, producing a spectrum.",
	"spectroscopy": "The technique of observing the spectra of visible light from an object to determine its composition, temperature, density, and speed.",
	"spectroscope": "Is an instrument that separates light into its individual colors or wavelengths. It typically uses a diffraction grating, which is a surface with closely spaced lines that disperses light into a spectrum.",
	"spectra": "Spectra are patterns of light, sound, or other energy distributed according to wavelength or frequency. They reveal information about the composition and properties of objects, from stars to molecules.",
	"spectral line": "In a spectrum, an emission (bright) or absorption (dark) at a specific frequency or wavelength.",
	"spectrum": "The range of colors that make up visible white light. A spectrum is produced when visible light passes through a prism.",
	"spectroscopy": "Analyzes the interaction between matter and electromagnetic radiation. It studies the absorption or emission of light to determine the composition and properties of substances.",
	"spectroscopic observations": "Spectroscopic observations analyze light by splitting it into its component wavelengths. This reveals information about an object's composition, temperature, motion, and other properties.",
	"spicules": "Grass-like patterns of gas seen in the atmosphere of the Sun.",
	"spiral galaxy": "A galaxy that contains a prominent central bulge and luminous arms of gas, dust, and young stars that wind out from the central nucleus in a spiral formation. Our galaxy, the Milky Way, is a spiral galaxy.",
	"star": "A giant ball of hot gas that creates and emits its own radiation through nuclear fusion.",
	"starburst galaxy": "Is a cosmic factory rapidly producing stars. Its gas is consumed at a much faster rate than in normal galaxies, leading to intense star formation activity and a short lifespan.",
	"star cluster": "A large grouping of stars, from a few dozen to a few hundred thousand, that are bound together by their mutual gravitational attraction.",
	"steady state theory": "The theory that suggests the universe is expanding but exists in a constant, unchanging state in the large scale. The theory states that new matter is being continually being created to fill the gaps left by expansion. This theory has been abandoned by most astronomers in favor of the big bang theory.",
	"stellar evolution": "(Stellar Lifecycle) Traces a star's life from birth in a nebula to its eventual death, influenced by its mass. Stars spend most of their lives fusing hydrogen into helium, eventually expanding and cooling before collapsing into a remnant like a white dwarf, neutron star, or black hole.",
	"stellar lifecycle": "(Stellar Evolution) Traces a star's life from birth in a nebula to its eventual death, influenced by its mass. Stars spend most of their lives fusing hydrogen into helium, eventually expanding and cooling before collapsing into a remnant like a white dwarf, neutron star, or black hole.",
	"stellar wind": "The ejection of gas from the surface of a star. Many different types of stars, including our Sun, have stellar winds. The stellar wind of our Sun is also known as the Solar wind. A star's stellar wind is strongest near the end of its life when it has consumed most of its fuel.",
	"stone meteorite": "A meteorite that resembles a terrestrial rock and is composed of similar materials.",
	"stony iron": "A meteorite that contains regions resembling both a stone meteorite and an iron meteorite.",
	"super-earth": "An exoplanet with a mass greater than Earth's but smaller than ice giants like Neptune. They are often rocky or gaseous and hold potential for hosting life, making them a focus of exoplanet research.",
	"sundog": "or parhelion. Atmospheric optical phenomenon that consists of a bright spot to one or both sides of the Sun. Two sun dogs often flank the Sun within a 22° halo.",
	"sunspot": "Areas of the Sun's surface that are cooler than surrounding areas. The usually appear black on visible light photographs of the Sun. Sunspots are usually associated disturbances in the Sun's electromagnetic field.",
	"snr": "(Supernova Remnant) An expanding shell of gas ejected at high speeds by a supernova explosion. Supernova remnants are often visible as diffuse gaseous nebulae usually with a shell-like structure. Many resemble 'bubbles' in space.",
	"supergiant": "The stage in a star's evolution where the core contracts and the star swells to about five hundreds times its original size. The star's temperature drops, giving it a RED color.",
	"supermoon": "A term used to describe a full moon that occurs during the Moon's closest approach to the Earth. During a supermoon, the Moon may appear slightly larger and brighter than normal.",
	"superior conjunction": "A conjunction that occurs when a planet passes behind the Sun and is on the opposite side of the Sun from the Earth.",
	"superior planet": "A planet that exists outside the orbit of the Earth. All of the planets in our solar system are superior except for Mercury and Venus. These two planets are inferior planets.",
	"superclusters": "Are immense cosmic structures containing tens of thousands of galaxies spread across hundreds of millions of light-years. They represent the largest known organized structures in the universe.",
	"supernova": "A supernova is a cataclysmic explosion caused when a star exhausts its fuel and ends its life. Supernovae are the most powerful forces in the universe. All of the heavy elements were created in supernova explosions.",
	"supernova remnant": "(SNR) An expanding shell of gas ejected at high speeds by a supernova explosion. Supernova remnants are often visible as diffuse gaseous nebulae usually with a shell-like structure. Many resemble 'bubbles' in space.",
	"super puff planet": "Are a very unusual type of exoplanet with extremely low mass and density. They are gas giants with a very low-density atmosphere and a radius larger than Neptune's.",
	"synchronous rotation": "A period of rotation of a satellite about its axis that is the same as the period of its orbit around its primary. This causes the satellite to always keep the same face to the primary. Our Moon is in synchronous rotation around the Earth.",
	"synodic month": "The period of time it takes the Moon to make one complete revolution around the Earth. A Synodic month is equal to 29.53 days and is measured as the time between a lunar phase and the return of that same phase.",
	"synodic period": "The interval between points of opposition of a superior planet.",
	"tektite": "A small, glassy material formed by the impact of a large body, usually a meteor or asteroid. Tektites are commonly found at the sites of meteor craters.",
	"telescope": "An instrument that uses lenses and sometimes mirrors to collect large amounts of light from distant objects and enable direct observation and photography. A Telescope can also include any instrument designed to observe distant objects by their emissions of invisible radiation such as x-rays or radio waves.",
	"terminator": "The boundary between the light side and the dark side of a planet or other body.",
	"terrestrial": "A term used to describe anything originating on the planet Earth.",
	"terrestrial planet": "A name given to a planet composed mainly of rock and iron, similar to that of Earth.",
	"terrestrial planets": "Rocky worlds like Earth, composed primarily of silicate minerals and metals. They are typically smaller and denser than gas giants, with solid surfaces and often have atmospheres. Our solar system's inner planets are terrestrial.",
	"the european space agency": "(ESA) is an international collaboration of fifteen European countries dedicated to space exploration. With Canada as a partner, ESA designs, develops, and launches satellites. The agency also supports European astronomers in utilizing the Hubble Space Telescope through the Space Telescope-European Coordinating Facility (ST-ECF).",
	"tidal force": "The differential gravitational pull exerted on any extended body within the gravitational field of another body.",
	"tidal heating": "Frictional heating of a satellite's interior due to flexure caused by the gravitational pull of its parent planet and/or other neighboring satellites.",
	"transit": "The passage of a celestial body across an observer's meridian; also the passage of a celestial body across the disk of a larger one.",
	"transit method": "The transit method detects exoplanets by measuring the tiny decrease in a star's brightness as a planet passes in front of it. This technique allows for determining a planet's size and orbital period.",
	"trans-neptunian object": "(TNO) Any one of a number of celestial objects that orbit the Sun at a distance beyond the orbit of the planet Neptune.",
	"t-tauri star": "Is a young, pre-main sequence star still contracting and heating up. They exhibit variable brightness and strong magnetic activity, often surrounded by gas and dust disks where planets can form.",
	"ultraviolet": "Electromagnetic radiation at wavelengths shorter than the violet end of visible light. The atmosphere of the Earth effectively blocks the transmission of most ultraviolet light, which can be deadly to many forms of life.",
	"umbra": "The area of total darkness in the shadow caused by an eclipse.",
	"universe": "The universe encompasses all space, time, matter, and energy. It includes everything from subatomic particles to vast galaxies, and its origins and ultimate fate remain subjects of scientific exploration.",
	"ut": "(Universal Time) Also known as GREENwich Mean Time, this is local time on the GREENwich meridian. Universal time is used by astronomers as a standard measure of time.",
	"universal time": "(UT) Also known as GREENwich Mean Time, this is local time on the GREENwich meridian. Universal time is used by astronomers as a standard measure of time.",
	"van allen belts": "Radiation zones of charged particles that surround the Earth. The shape of the Van Allen belts is determined by the Earth's magnetic field.",
	"variable star": "A star that fluctuates in brightness. These include eclipsing binaries.",
	"visible light": "Wavelengths of electromagnetic radiation that are visible to the human eye.",
	"virgo cluster": "A gigantic cluster of over 2000 galaxies that is located mainly within the constellation of Virgo. This cluster is located about 60 million light-years from Earth.",
	"visual magnitude": "A scale used by astronomers to measure the brightness of a star or other celestial object. Visual magnitude measures only the visible light from the object. On this scale, bright objects have a lower number than dim objects.",
	"volcanism": "Volcanism is the process where molten rock (magma) erupts from Earth's interior to its surface. It shapes landscapes, influences climate, and provides insights into our planet's internal dynamics.",
	"wave": "A vibration, a disturbance that transfers energy through a medium without net movement of particles. It's characterized by oscillations and can be classified as mechanical (requires medium) or electromagnetic (propagates through space).",
	"wavelength": "The distance between consecutive crests of a wave. This serves as a unit of measure of electromagnetic radiation.",
	"webb telescope": "The Webb Telescope is a powerful infrared observatory designed to explore the early universe, study exoplanets, and investigate star formation. It's the successor to Hubble, offering unprecedented detail and sensitivity.",
	"white dwarf": "A very small, white star formed when an average sized star uses up its fuel supply and collapses. This process often produces a planetary nebula, with the white dwarf star at its center.",
	"wolf-rayet star": "A Wolf-Rayet star is a massive, dying star shedding its outer layers at a rapid rate. Characterized by strong emission lines of helium, nitrogen, carbon, or oxygen, they represent a brief, final stage in the life of extremely large stars.",
	"x-ray": "Electromagnetic radiation of a very short wavelength and very high-energy. X-rays have shorter wavelengths than ultraviolet light but longer wavelengths than cosmic rays.",
	"x-ray astronomy": "The field of astronomy that studies celestial objects by the x-rays they emit.",
	"x-ray star": "A bright celestial object that gives off x-rays as a major portion of its radiation.",
	"YELLOW dwarf": "(G-type star) An ordinary star such as the Sun at a stable point in its evolution.",
	"zenith": "A point directly overhead from an observer.",
	"zodiac": "An imaginary belt across the sky in which the Sun, moon, and all of the planets can always be found.",
	"zodiacal Light": "A faint cone of light that can sometimes be seen above the horizon after sunset or before sunrise. Zodiacal light is caused by sunlight reflecting off small particles of material in the plane of the Solar System."
}
#----------------------------------------------------
core["astronomy glossary"] = list(astronomy_glossary.keys())
chkdict.append(sum(sum(ord(char) for char in word) for value in astronomy_glossary.values() for word in value))

#----------------------------------------------------
orbit_regime = {
	"geo": "Geostationary Orbit           \n i < 25°, 35586 km < hp < 35986 km, 35586 km < ha < 35986 km",
	"igo": "Inclined Geosynchronous Orbit \n 37948 km < a < 46380 km, e < 0.25, 25° < i < 180°",
	"ego": "Extended Geostationary Orbit  \n 37948 km < a < 46380 km, e < 0.25, i < 25°",
	"nso": "Navigation Satellites Orbit   \n 50° < i < 70°, 18100 km < hp < 24300 km, 18100 km < ha < 24300 km",
	"gto": "GEO Transfer Orbit            \n i < 90°, hp < 2000 km, 31570 km < ha < 40002 km",
	"meo": "Medium Earth Orbit            \n 2000 km < hp < 31570 km, 2000 km < ha < 31570 km",
	"gho": "GEO-superGEO Crossing Orbits  \n 31570 km < hp < 40002 km, ha > 40002 km",
	"leo": "Low Earth Orbit               \n hp < 2000 km, ha < 2000 km",
	"hao": "High Altitude Earth Orbit     \n hp > 40002 km, ha > 40002 km",
	"mgo": "MEO-GEO Crossing Orbits       \n 2000 km < hp < 31570 km, 31570 km < ha < 40002 km",
	"heo": "Highly Eccentric Earth Orbit  \n hp < 31570 km, ha > 40002 km",
	"lmo": "LEO-MEO Crossing Orbits       \n hp < 2000 km, 2000 km < ha < 31570 km",
	"sso": "Sun-synchronous orbit         \n i = 98°, hp < 600 km, < ha < 800 km",
}
#----------------------------------------------------
chkdict.append(sum(sum(ord(char) for char in word) for value in orbit_regime.values() for word in value))

#----------------------------------------------------
planet_data = {
	"mercury": {"orbital_period": 0.24,"semi_major_axis": 0.39,"orbital_eccentricity": 0.21,"orbital_inclination": 7.00,
	"rotation_period": 58.65,"axial_tilt": 0.03,"mass": 3.3011e23,
	"atmosphere": "Virtually no atmosphere. Trace amounts of hydrogen, helium, and oxygen.",
	"moons": "No moons.","rings": "No rings.","temperature": "167°C (333°F) day, -180°C (-292°F) night"
	},
	"venus": {"orbital_period": 0.62,"semi_major_axis": 0.72,"orbital_eccentricity": 0.007,"orbital_inclination": 3.39,
	"rotation_period": 243.02,"axial_tilt": 177.36,"mass": 4.8675e24,
	"atmosphere": "Primarily carbon dioxide (96.5%), with nitrogen, argon, and trace amounts of other gases.",
	"moons": "No moons.","rings": "No rings.","temperature": "462°C (864°F)"
	},
	"earth": {"orbital_period": 1.00,"semi_major_axis": 1.00,"orbital_eccentricity": 0.017,"orbital_inclination": 0.00,
	"rotation_period": 24.00,"axial_tilt": 23.44,"mass": 5.9722e24,
	"atmosphere": "Primarily nitrogen (78%) and oxygen (21%), with argon and trace gases.",
	"moons": "One moon: Moon","rings": "No rings.","temperature": "15°C (59°F)"
	},
  	"mars": {"orbital_period": 1.88,"semi_major_axis": 1.52,"orbital_eccentricity": 0.093,"orbital_inclination": 1.85,
	"rotation_period": 01.03,"axial_tilt": 25.19,"mass": 6.4171e23,
	"atmosphere": "Primarily carbon dioxide (95%), with nitrogen, argon, and trace amounts of oxygen and water vapor.",
	"moons": "Two moons: Phobos and Deimos.","rings": "No rings.","temperature": "-63°C (-81°F)"
	},
  	"jupiter": {"orbital_period": 11.86,"semi_major_axis": 5.20,"orbital_eccentricity": 0.048,"orbital_inclination": 1.31,
	"rotation_period": 0.41,"axial_tilt": 3.13,"mass": 1.8981e27,
	"atmosphere": "Primarily hydrogen and helium, with methane, ammonia, and trace amounts of other gases.",
	"moons": "Over 80 moons, with the four largest being Io, Europa, Ganymede, and Callisto.",
	"rings": "Prominent ring system composed mainly of ice particles.","temperature": "-145°C (-229°F)"
	},
  	"saturn": {"orbital_period": 29.46,"semi_major_axis": 9.54,"orbital_eccentricity": 0.056,"orbital_inclination": 2.49,
	"rotation_period": 0.43,"axial_tilt": 26.73,"mass": 5.6834e26,
	"atmosphere": "Primarily hydrogen and helium, with methane and ammonia.",
	"moons": "Over 80 moons, with the largest being Titan.",
	"rings": "Extensive and complex ring system composed mostly of ice particles.","temperature": "-185°C (-299°F)"
	},
  	"uranus": {"orbital_period": 84.01,"semi_major_axis": 19.18,"orbital_eccentricity": 0.046,"orbital_inclination": 0.77,
	"rotation_period": -0.72,"axial_tilt": 97.77,"mass": 8.6810e25,
	"atmosphere": "Primarily hydrogen and helium, with methane giving it its BLUE color.",
	"moons": "Over 27 moons, with the largest being Titania and Oberon.",
	"rings": "Faint ring system composed of dark particles.","temperature": "-195°C (-319°F)"
	},
  	"neptune": {"orbital_period": 164.81,"semi_major_axis": 30.06,"orbital_eccentricity": 0.009,"orbital_inclination": 1.77,
	"rotation_period": 0.67,"axial_tilt": 28.32,"mass": 1.0243e26,
	"atmosphere": "Primarily hydrogen and helium, with methane and ammonia.",
	"moons": "Over 14 moons, with the largest being Triton.",
	"rings": "Faint ring system composed of ice particles.","temperature": "-200°C (-328°F)"
	},
	"pluto": {"orbital_period": 248.09,"semi_major_axis": 39.48,"orbital_eccentricity": 0.2488,"orbital_inclination": 17.14,
	"rotation_period": -6.387,"axial_tilt": 122.53,"mass": 1.30900e22,
	"atmosphere": "Thin atmosphere composed primarily of nitrogen, with methane and carbon monoxide.",
	"moons": "Five moons: Charon, Styx, Nix, Kerberos, and Hydra.","rings": "No rings.","temperature": "-228°C (-378°F)"
	}
}
#----------------------------------------------------
chkdict.append(sum(sum(ord(char) for char in word) for value in planet_data.values() for word in value))

#----------------------------------------------------
constellations_dict = {
	"andromeda": "Princess of Ethiopia","antlia": "Air pump","apus": "Bird of Paradise","aquarius": "Water bearer",
	"aquila": "Eagle","ara": "Altar","aries": "Ram","auriga": "Charioteer","bootes": "Herdsman",
	"caelum": "Graving tool","camelopardalis": "Giraffe","cancer": "Crab","canes venatici": "Hunting dogs",
	"canis major": "Big dog","canis minor": "Little dog","capricornus": "Sea goat","carina": "Keel of Argonauts' ship",
	"cassiopeia": "Queen of Ethiopia","centaurus": "Centaur","cepheus": "King of Ethiopia","cetus": "Sea monster (whale)",
	"chamaeleon": "Chameleon","circinus": "Compasses","columba": "Dove","coma berenices": "Berenice's hair",
	"corona australis": "Southern crown","corona borealis": "Northern crown","corvus": "Crow","crater": "Cup",
	"crux": "Cross (southern)","cygnus": "Swan","delphinus": "Porpoise","dorado": "Swordfish","draco": "Dragon",
	"equuleus": "Little horse","eridanus": "River","fornax": "Furnace","gemini": "Twins","grus": "Crane",
	"hercules": "Hercules, son of Zeus","horologium": "Clock","hydra": "Sea serpent","hydrus": "Water snake","indus": "Indian",
	"lacerta": "Lizard","leo": "Lion","leo Minor": "Little lion","lepus": "Hare","libra": "Balance","lupus": "Wolf",
	"lynx": "Lynx","lyra": "Lyre or harp","mensa": "Table mountain","microscopium": "Microscope","monoceros": "Unicorn",
	"musca": "Fly","norma": "Carpenter's Level","octans": "Octant","ophiuchus": "Holder of serpent","orion": "Orion, the hunter",
	"pavo": "Peacock","pegasus": "Pegasus, the winged horse","perseus": "Perseus, hero who saved Andromeda",
	"phoenix": "Phoenix","pictor": "Easel","pisces": "Fishes","piscis austrinus": "Southern fish","puppis": "Stern of the Argonauts' ship",
	"pyxis": "Compass on the Argonauts' ship","reticulum": "Net","sagitta": "Arrow","sagittarius": "Archer","scorpius": "Scorpion",
	"sculptor": "Sculptor's tools","scutum": "Shield","serpens": "Serpent","sextans": "Sextant","taurus": "Bull",
	"telescopium": "Telescope","triangulum": "Triangle","triangulum australe": "Southern triangle","tucana": "Toucan",
	"ursa major": "Big bear","ursa minor": "Little bear","vela": "Sail of the Argonauts' ship","virgo": "Virgin",
	"volans": "Flying fish","vulpecula": "Fox"
}
#----------------------------------------------------
core["constelattion"] = list(constellations_dict.keys())
chkdict.append(sum(sum(ord(char) for char in word) for value in constellations_dict.values() for word in value))

#---------------------------------------------------------
constellations_abbr = {
	"And": "Andromeda","Ant": "Antlia","Apus": "Apodis","Aqr": "Aquarius","Aql": "Aquila",
	"Ara": "Arae","Ari": "Aries","Aur": "Auriga","Boo": "Bootes","Cae": "Caelum","Cam": "Camelopardalis",
	"Cnr": "Cancer","CVn": "Canes Venatici","CMa": "Canis Major","CMi": "Canis Minor","Cap": "Capricornus","Car": "Carina",
	"Cas": "Cassiopeia","Cen": "Centaurus","Cep": "Cepheus","Cet": "Cetus","Cha": "Chamaeleon","Cir": "Circinus",
	"Col": "Columba","Com": "Coma Berenices","CrA": "Corona Australis","CrB": "Corona Borealis","Crv": "Corvus",
	"Crt": "Crater","Cru": "Crux","Cyh": "Cygnus","Del": "Delphinus","Dor": "Dorado","Dra": "Draco",
	"Equ": "Equuleus","Eri": "Eridanus","For": "Fornax","Gem": "Gemini","Gru": "Grus","Her": "Hercules",
	"Hor": "Horologium","Hya": "Hydra","Hyi": "Hydrus","Ind": "Indus","Lac": "Lacerta","Leo": "Leonis",
	"LMi": "Leo Minor","Lep": "Lepus","Lib": "Libra","Lup": "Lupus","Lyn": "Lynx","Lyr": "Lyra",
	"Men": "Mensa","Mic": "Microscopium","Mon": "Monoceros","Mus": "Musca","Nor": "Norma","Oct": "Octans",
	"Oph": "Ophiuchus","Ori": "Orion","Pav": "Pavo","Peg": "Pegasus","Per": "Perseus","Phe": "Phoenix",
	"Pic": "Pictor","Psc": "Pisces","PsA": "Piscis Austrinus","Pup": "Puppis","Pyx": "Pyxis","Ret": "Reticulum",
	"Sge": "Sagitta","Sgr": "Sagittarius","Sco": "Scorpius","Scl": "Sculptor","Sct": "Scutum","Ser": "Serpens",
	"Sex": "Sextans","Tau": "Taurus","Tel": "Telescopium","Tri": "Triangulum","TrA": "Triangulum Australe","Tuc": "Tucana",
	"UMa": "Ursa Major","UMi": "Ursa Minor","Vel": "Vela","Vir": "Virgo","Vol": "Volans","Vul": "Vulpecula"
}
#---------------------------------------------------------
chkdict.append(sum(sum(ord(char) for char in word) for value in constellations_abbr.values() for word in value))

#---------------------------------------------------------
asteroids_list = {
	"65 cybele": {"type": "minor planet", "dimensions":237.26, "description": "65 Cybele is one of the largest asteroids in the Solar System. Its located in the outer asteroid belt. It is thought to be a emnant primordial body."},
	"ceres": {"type": "dwarf planet", "dimensions":939.4, "description": "Largest asteroid, potential water ice"},
    "vesta": {"type": "asteroid", "dimensions":525.4, "description": "Brightest asteroid visible to the naked eye. Second-largest, differentiated structure"},
    "pallas": {"type": "asteroid", "dimensions":545, "description": "Third-largest, unusual orbit"},
    "bennu": {"type": "dangerous asteroid", "dimentions":0.492, "description": "Carbon-rich, explored by OSIRIS-REx"},
    "ryugu": {"type": "asteroid", "dimensions":0.9, "description": "Carbon-rich, explored by Hayabusa2"},
    "itokawa": {"type": "asteroid", "dimensions":0.33, "description": "Small, S-type, explored by Hayabusa"},
    "eros": {"type": "asteroid", "dimensions":16.84, "description": "Near-Earth asteroid, extensively studied"},
    "gaspra": {"type": "asteroid", "dimensions":12.2, "description": "First asteroid imaged close-up"},
    "ida": {"type": "asteroid", "dimensions":32, "description": "Has a moon (Dactyl)"},
    "juno": {"type": "asteroid", "dimensions":246.596, "description": "One of the largest main-belt asteroids"},
    "hebe": {"type": "asteroid", "dimensions":185.18, "description": "One of the most massive asteroids"},
    "iris": {"type": "asteroid", "dimensions":199.83, "description": "One of the brightest asteroids"},
    "flora": {"type": "asteroid", "dimensions":147.491, "description": "Largest asteroid in the Flora family"},
    "metis": {"type": "asteroid", "dimensions":190, "description": "Innermost asteroid in the asteroid belt"},
    "hygiea": {"type": "asteroid", "dimensions":407.12, "description": "Fourth-largest asteroid"},
    "interamnia": {"type": "asteroid", "dimensions":306.313, "description": "One of the most massive asteroids"},
    "europa": {"type": "asteroid", "dimensions":303.918, "description": "Large asteroid with high albedo"},
	"apophis": {"type": "dangerous asteroid", "dimensions": 0.37, "description": "Potentially hazardous asteroid, close Earth approach in 2029"},
    "1950 da": {"type": "asteroid", "dimensions": 1.1, "description": "Potentially hazardous asteroid, high risk of Earth impact in 2880"},
	"psyche": {"type": "metal-rich asteroid", "dimensions": 220, "description": "Potentially iron-nickel core of a protoplanet"},
	#-----------------------------------------------------------------
	"thetis": {"type": "main-belt asteroid", "dimensions": 84.899, "description": "A typical main-belt asteroid"},
	"melpomene": {"type": "main-belt asteroid", "dimensions": 139.594, "description": "A typical main-belt asteroid"},
	"fortuna": {"type": "main-belt asteroid", "dimensions": 200, "description": "A large main-belt asteroid"},
	"massalia": {"type": "main-belt asteroid", "dimensions": 135.680, "description": "A typical main-belt asteroid"},
	"lutetia": {"type": "main-belt asteroid", "dimensions": 95.76, "description": "A large main-belt asteroid"},
	"kalliope": {"type": "main-belt asteroid", "dimensions": 167.536, "description": "A large main-belt asteroid"},
	"thalia": {"type": "main-belt asteroid", "dimensions": 107.53, "description": "A typical main-belt asteroid"},
	"themis": {"type": "main-belt asteroid", "dimensions": 198, "description": "A large main-belt asteroid"},
	"phocaea": {"type": "main-belt asteroid", "dimensions": 61.054, "description": "A smaller main-belt asteroid"},
	"proserpina": {"type": "main-belt asteroid", "dimensions": 94.80, "description": "A typical main-belt asteroid"},
	"euterpe": {"type": "main-belt asteroid", "dimensions": 96, "description": "A typical main-belt asteroid"},
	"bellona": {"type": "main-belt asteroid", "dimensions": 120.90, "description": "A typical main-belt asteroid"},
	"amphitrite": {"type": "main-belt asteroid", "dimensions": 189.559, "description": "A large main-belt asteroid"},
	"urania": {"type": "main-belt asteroid", "dimensions": 92.787, "description": "A typical main-belt asteroid"},
	"euphrosyne": {"type": "main-belt asteroid", "dimensions": 267.080, "description": "A very large main-belt asteroid"},
	"pomona": {"type": "main-belt asteroid", "dimensions": 80.76, "description": "A typical main-belt asteroid"},
	"1950 da": {"type": "dangerous asteroid", "dimensions": 1.1, "description": "This asteroid has a relatively high probability of impact in the distant future, making it a subject of ongoing study."},
	"4179 toutatis": {"type": "dangerous asteroid", "dimensions": 5.2, "description": "This asteroid is quite large and has had close approaches to Earth in the past, making it a potential concern."},
	"2007 tu24": {"type": "dangerous asteroid", "dimensions": 250, "description": "This asteroid made a relatively close approach to Earth in 2007, highlighting the need for continued monitoring of near-Earth objects."},
	"99942 apophis": {"type": "dangerous asteroid", "dimensions": 250, "description": "This asteroid was once considered a significant threat but subsequent observations have reduced the risk. It's still monitored closely."},
	"2010 al30": {"type": "dangerous asteroid", "dimensions": 15, "description": "This asteroid made a very close approach to Earth in 2010, emphasizing the need for early detection of these objects."},
	"2011 md": {"type": "dangerous asteroid", "dimensions": 7, "description": "This small asteroid made an exceptionally close Earth flyby in 2011, highlighting the potential for unexpected encounters."},
	"2014 rc": {"type": "dangerous asteroid", "dimensions": 22, "description": "This small asteroid passed extremely close to Earth in 2014, underscoring the difficulty in detecting all near-Earth objects."},
	"Unidentified PHA": {"type": "dangerous asteroid", "dimensions": 0, "description": "There are likely many other potentially hazardous asteroids yet to be discovered or fully characterized."}
}
#----------------------------------------------------
core["asteroid"] = list(asteroids_list.keys())

#----------------------------------------------------
climate_dictionary = {
	"adaptation":	"/ædæpˈteɪʃn/ noun: adjusting to the impacts of climate change, like extreme weather, rising sea levels, and more.",
	"BLUE economy":	"/ˈbluː ɪˈkɒnəmi/ noun: Sustainable use of ocean resources for economic benefit and healthy marine ecosystems.",
	"carbon removal":	"/ˈkɑːbən rɪˈmuːvl/ noun: Carbon removal is basically cleaning up the air by taking out GREENhouse gases, especially carbon dioxide, that contribute to climate change. It can involve planting trees, improving soil, or even using technology to capture carbon directly from the air.",
	"carbon capture":	"/ˈkɑːbən kæptʃə(r)/ noun: Carbon capture, in the context of climate change, is basically snaring the carbon dioxide (CO2) from factories and power plants before it goes into the air.  This trapped CO2 can then be stored underground.",
	"carbon footprint":	"/ˈkɑːbən ˈfʊtprɪnt/ noun: carbon footprint is a measure of the GREENhouse gases, like carbon dioxide, released by your activities. The more you emit, the bigger your footprint and impact on climate change.",
	"carbon markets":	"/ˈkɑːbən mɑːkɪts/ noun: Carbon markets are like marketplaces for pollution.  Companies can buy and sell permits to release GREENhouse gases, creating an incentive to reduce emissions.",
	"carbon sink":	"/ˈkɑːbən sɪŋk/ noun: A carbon sink is basically a giant air filter, like a forest, that sucks in carbon dioxide from the atmosphere and helps fight climate change.",
	"circular economy":	"/ˈsɜːkjələ(r) ɪˈkɒnəmi/  noun: odels that aim to reduce waste, pollution, and resource use, while promoting nature's renewal. In short, it's about keeping things in use for longer and minimizing what we throw away.",
	"climate crisis":	"/ˈklaɪmət kraɪsɪs/ noun: Refers to the urgent danger caused by climate change. It emphasizes the seriousness of the situation and the need for immediate action.",
	"climate finance":	"/ˈklaɪmət ˈfaɪnæns/ noun: Is the money used to fight climate change. This includes funds for both REDucing emissions (mitigation) and adapting to climate impacts (adaptation).  In short, it's the cash to tackle climate change.",
	"climate justice":	"/ˈklaɪmət ˈdʒʌstɪs/ noun: Is about fairness in dealing with climate change.  It considers two main things: Richer countries caused more climate problems and should help poorer countries that are suffering more. We should take action now to protect future generations who will inherit the climate we create.",
	"climate overshoot":	"/ˈklaɪmət ˌəʊvəˈʃuːt/  noun: Refers to a temporary period when global warming surpasses a certain target, like 1.5°C, before going back down due to mitigation efforts",
	"climate security":		"/ˈklaɪmət sɪˈkjʊərəti/ noun: Refers to the dangers that climate change brings to peace and stability, and how to manage those risks.",
	"cop":	"COP stands for 'Conference of the Parties'.  It's basically a big meeting  of countries that are trying to address climate change together.",
	"decarbonization":	"/ˌdiːˌkɑːbənaɪˈzeɪʃn/ noun: In a nutshell, is reducing the amount of GREENhouse gases, especially carbon dioxide, released into the atmosphere. It's like weaning our activities off of carbon to fight climate change.",
	"feedback loop":	"/ˈfiːdbæk luːp/ noun: Is a self-perpetuating cycle where a change in climate triggers further changes that either amplify (positive) or dampen (negative) the initial effect. Imagine a domino effect, but for climate!",
	"global warming":	"/ˌɡləʊbl ˈwɔːmɪŋ/ noun: Is Earth's atmosphere and oceans heating up due to increased GREENhouse gases trapping more heat.  In short, it's Earth getting warmer from certain gases acting like a blanket.",
	"climate change":	"/ˈklaɪmət tʃeɪndʒ/ noun: Climate change refers to long-term shifts in weather patterns, caused mainly by human activities that release GREENhouse gases and warm the Earth's atmosphere.",
	"GREEN jobs":	"/ɡriːn dʒɒb/ noun: Are jobs that fight climate change by protecting the environment. This can involve making renewable energy or recycling materials.",
	"GREENhouse":	"/ˌɡriːn.haʊs/ noum: Refers to gases that trap heat from the sun in the Earth's atmosphere, causing it to warm. This is a different meaning from the building used for growing plants.",
	"gas emissions":	"/ɡæs ɪˈmɪʃns/ noun: refers to the release of gases, like carbon dioxide, that trap heat in the atmosphere, causing global warming.  These are called GREENhouse gases.",
	"GREENwashing":	"/ˈɡriːnwɒʃɪŋ/ noun: Is when a company makes their products or practices seem more environmentally friendly than they really are [1]. It's a way to mislead consumers about their true impact on climate change.",
	"indigenous knowledge":	"/ɪnˈdɪdʒənəs ˈnɒlɪdʒ/ noun: Knowledge passed down through generations by indigenous peoples. Deep understanding of the natural world and its changes. Helps communities live in balance with the environment. Valuable resource for understanding and adapting to climate change",
	"ipcc":	"IPCC stands for the Intergovernmental Panel on Climate Change. In short, it's the leading international body for the assessment of climate change.  They evaluate the science and provide recommendations to policymakers.",
	"just transition":	"/dʒʌst trænˈzɪʃn/ noun: Is about moving to a sustainable economy  fairly for everyone. This means creating new jobs ('decent work') and retraining workers in industries affected by climate action.  Basically, it's about making the shift to a GREENer world without leaving people behind.",
	"loss and damage":	"/lɒs ənd ˈdæmɪdʒ/ noun: Refers to the negative effects that happen even if we try to reduce emissions (mitigation) and prepare for change (adaptation).  These are often harms to developing countries that are especially vulnerable.!",
	"long-term strategies":	"/ˌlɒŋ ˈtɜːm ˈstrætədʒis/ noun: Are basically roadmaps for achieving two main goals: Limiting global warming: This means keeping the average temperature increase well below 2°C compared to pre-industrial levels.  Adapting to climate impacts: This involves preparing for the unavoidable changes caused by warming, like rising sea levels and extreme weather. These strategies are designed to be a long-term vision that guides shorter-term actions towards a sustainable future.",
	"mitigation":	"/mɪtɪˈɡeɪʃn/ noun: Means reducing GREENhouse gas emissions to slow down warming.  This can involve using less energy, switching to renewable sources, or planting trees.",
	"nationally determined contributions":	"/ˈnæʃnəli dɪˈtɜːmɪnd ˌkɒntrɪˈbjuːʃns/ noun: In a nutshell, Nationally Determined Contributions (NDCs) are countries' individual climate action plans. They outline how each country will reduce GREENhouse gas emissions and adapt to the effects of climate change. These plans are updated every five years.",
	"national adaptation plans":	"/ˈnæʃnəl ˌædæpˈteɪʃn plæns/ noun: (NAPs) are basically roadmaps countries create to deal with climate change impacts. They involve figuring out what the country's vulnerabilities are and then making a plan to become more resilient.",
	"nature-based solutions":	"/ˈneɪtʃə(r) beɪst səˈluːʃns/ noun: Nature-based solutions are using nature's power to fight climate change. This involves protecting, restoring, and managing ecosystems to store carbon and boost resilience.  Think of it as giving nature a helping hand to combat climate change.",
	"net zero":	"/ˌnet ˈzɪərəʊ/ noun: Net zero, in the context of climate change, is like having a giant emissions scale. You're trying to get the emissions side (bad) to balance out with the removal side (good). This means reducing emissions as much as possible and removing any remaining ones from the atmosphere.",
	"paris agreement":	"pærɪs əˈɡriːmənt/ noun: The Paris Agreement is an international treaty aiming to limit global warming to well below 2°C, ideally 1.5°C, by reducing emissions and supporting developing countries ",
	"reforestation":	"/ˌriːfɒrɪˈsteɪʃn/ noun: Is bringing back trees to areas that once had forests but lost them recently. This can happen due to wildfires, human actions, or natural causes.",
	"afforestation":	"/əˌfɒrɪˈsteɪʃn/ noun: Refers to the planting of new forests, which is the opposite of deforestation and would help combat climate change.",
	"redd+":	"Is a program that aims to fight climate change by protecting forests in developing countries. It stands for reducing Emissions from Deforestation and Forest Degradation.",
	"regenerative agriculture":	"/rɪˈdʒenərətɪv ˈæɡrɪkʌltʃə(r)/ noun: Is a farming approach that improves soil health, which in turn helps fight climate change by: - Increasing the amount of carbon captured by the soil, reducing water use- Preventing land degradation, - Promoting biodiversity. It's essentially a win-win for both people and the planet!",
	"renewable energy":	"/rɪˈnjuːəbl ˈenədʒi/ noun: Is energy that comes from natural sources that are constantly refilled, like sunshine, wind, and moving water. This is in contrast to fossil fuels that run out and pollute the environment.",
	"resilience":	"/rɪˈzɪliəns/ noun: The concept is closely related to adaptation. In the context of climate change, resilience refers to the ability of communities and ecosystems to bounce back from climate impacts and even thrive in the face of a changing climate.",
	"rewilding":	"/ˌriːˈwaɪldɪŋ/ noun: Is basically giving nature a helping hand to heal itself. It involves restoring damaged ecosystems by letting nature take the lead, but with a nudge from us in the form of reintroducing missing species or removing human-made obstacles. This helps fight climate change by boosting natural processes that suck carbon dioxide out of the air.",
	"tipping point":	"/ˈtɪpɪŋ pɔɪnt/ noun: Refers to a critical threshold beyond which a natural system undergoes a large and often irreversible change.  These changes can be triggered by human activity, such as GREENhouse gas emissions, and can have significant consequences for the planet and its inhabitants.! - The concept of tipping points is a serious concern for scientists and policymakers alike.  Understanding these potential thresholds is crucial for mitigating climate change and preventing the worst-case scenarios.",
	"unfccc":	"The UNFCCC is an international treaty to fight climate change adopted by almost all countries in 1992. ",
	"weather vs climate":	"/ˈweðə(r)/ noun  /ˈˈklaɪmət/ noun: Weather refers to the short-term conditions of the atmosphere, like temperature, humidity, precipitation, cloudiness, wind, and visibility, at a particular time and place. Climate, on the other hand, refers to the average weather patterns of a specific region over a long period of time, typically 30 years or more. It's like the overall mood of a place, while weather is the day-to-day ups and downs."
}
#----------------------------------------------------
core["climate dictionary term"] = list(climate_dictionary.keys())
core["climate dictionary"] = list(climate_dictionary.values())
chkdict.append(sum(sum(ord(char) for char in word) for value in climate_dictionary.values() for word in value))

#----------------------------------------------------
oldtech_terms = {
	"a/s/l": "Age/sex/location?",
	"aol dialup": "Dial-up Internet access is a form of Internet access that uses the facilities of the public switched telephone network (PSTN) to establish a connection to Internet service provider (ISP) by dialing a telephone number on a conventional telephone.",
	"aim": "AIM was an instant messaging and presence computer program created by AOL, which used the proprietary OSCAR instant messaging protocol and the TOC protocol.",
	"anonymous": "Normally used to log in to an FTP server (See FTP), to indicate that the user is not registered with a service. The password to be provided must be your own email address.",
	"apple pippin": "The Pippin was a video game system introduced by Apple in 1996. It had a strange sort of licensing triangle in existence where it was also being licensed and sold by two other companies at the time.",
	"archie": "Tool that allows you to search for files and information on FTP servers. Archie is given the name of the file (or part of it) that he wants to find and he provides the name (address) of the servers where he can find it.",
	"arpanet": "(Advanced Research Projects Agency Network): The precursor to the internet.",
	"article": "An existing text on Usenet/News.",
	"ansi": "American National Standards Institute: A private non-profit organization that develops and promotes standards in the United States.",
	"ansi codes": "ANSI escape sequences: A set of control characters and commands embedded in text that control formatting, such as color, font style, and cursor positioning.",
	"ascii": "Standard for encoding characters using binary numbers, used on different computers. Defines the encoding of characters with codes from 0 to 127.",
	"batch": "A method of executing a series of computer programs successively without human interaction.",
	"baud": "Amount of information that is provided between two computers interconnected by a modem. Measure Unit",
	"baud rate": "The <baud> rate is the rate at which information is transferred in a communication channel. Baud rate is commonly used when discussing electronics that use serial communication. In the serial port context, '9600 baud' means that the serial port is capable of transferring a maximum of 9600 bits per second.",
	"bandwidth": "Bandwidth. Term that designates the amount of information that can be transmitted per unit of time, in a given means of communication (wire, radio wave, optical fiber, etc.). Typically measured in bits per second, kilobits per second, megabits per second, kilobytes per second, megabytes per second, etc.",
	"backbone": "Highest-level structure in a network composed of multiple subnets.",
	"beeper": "A beeper, also known as a pager, is a wireless telecommunications device that receives and displays alphanumeric or voice messages",
	"bleeper": "A bleeper, also known as a beeper or pager, is a wireless telecommunications device that receives and displays alphanumeric or voice messages",
	"bios": "It is the machine's basic memory. Contains primary instructions for the correct operation of the machine.  BIOS that stores the information that your PC has a keyboard, HD, memory for example.",
	"bitnet": "Global network accessible via the Internet, but distinct from it, with educational characteristics.",
	"btw": "Acronym for English 'By the Way' (Already now / By the way, etc.). Used in electronic mail texts, news articles, etc.",
	"bbs": "Bulletin Board System. Were originally more like intranet systems than Internet ones, allowing a whole bunch of computers to connect to a system using a terminal program. They had message boards, they allowed people to share files with relative ease, and sometimes they even had chat programs — but the rise of dial-up Internet in the mid part of the decade basically killed the market for them.",
	"boot up": "Process of starting the computer by loading the operating system (from floppy disk in MS-DOS)",
	"bug": "Software error or malfunction",
	"cassete": "Cassette tapes were a popular audio recording and playback format in the 1990s. They consisted of a plastic case containing a magnetic tape that stored sound. To listen to music, you would insert the cassette into a cassette player. Popular brands : Basf, Tdk, Maxwell, Sony.",
	"cd": "In the 1990s, the abbreviation 'CD' had two distinct meanings: MS-DOS, 'CD' stood for 'Change Directory.' It was a command used to navigate through the file system by switching to a different folder or directory and 'CD' referred to a Compact Disc. This was a revolutionary digital optical disc format for storing and playing audio, and later, data.",
	"command line": "Text-based interface for interacting with the computer by typing commands",
	"chain letter": "A letter that is received by someone and sent to several people and so on until it becomes excessively widespread. Normally its text encourages the dissemination of the letter by other people.",
	"chain mail": "See <chain letter>.",
	"crash": "System failure causing the computer to freeze or shut down unexpectedly",
	"cell phone": "Cell phones in the 90s were vastly different from the modern smartphones we use today, (XX Century). They were often referred to as 'brick phones' due to their size and weight. ",
	"cello": "Cello is an early, discontinued graphical web browser for Windows 3.1; it was developed by Thomas R. Bruce. It was released as shareware in 1993. While other browsers ran on various Unix machines, Cello was the first web browser for Microsoft Windows, using the winsock system to access the Internet. In addition to the basic Windows, Cello worked on Windows NT 3.5 and with small modifications on OS/2.",
	"cert": "Computer Emergency Response Team. Organization created in 1988 by Darpa, aiming to address security issues in networks, particularly the Internet.",
	"crt": "Display device with Cathode Ray Tube technology (precursor to LCD monitor)",
	"cyberspace": "Cyber space is usually referred to as the set of interconnected computer networks and all the activity there. It is a kind of virtual planet, where people (the information society) interact virtually, by electronic means. Term invented by William Gibson in his novel Neuromancer. Later name given to the Internet.",
	"com port": "The serial connection standard that allowed computers to communicate with peripherals like modems, printers, and other devices.",
	"con": "Connecting your computer to a remote computer.",
	"copy": "MS-DOS copying file process from <path source> <path destiny>",
	"crosspost": "Crosspost... The act of sending an article (or part) already published (or to be published at the same time) in another group to a news group.",
	"cypherpunk": "Despite the fact that it has the word 'punk' in it, a cypherpunk was actually someone who who advocated the widespread use of strong cryptography (writing in code) as a way of protecting your privacy. Julian Assange has been a major voice in the cypherpunk movement since it began in the 80s.",
	"daemon": "Program that runs (that was launched) on a computer and is (always) ready to receive instructions/requests from other programs to execute a certain action.",
	"defaults": "It is said to be the configuration normally used by a device or program.",
	"database": "Software for storing and managing structured data (e.g., dBASE)",
	"debug": "The process of identifying and removing errors from computer programs.",
	"defragging": "Reorganizing the data on your computer in order to get it to work faster.",
	"denial of servide": "D O S - Attack that consists of overloading a server with an excessive amount of service requests.",
	"dial-in": "Designation of a type of connection or an act of connecting to the Internet, in this case by establishing a call (telephone - Dial) to a computer, through, for example, a modem. See: <dial-up>.",
	"dial-up": "A method of connecting to the internet using a modem and a phone line.",
	"digerati": "It's like 'gliterrati' (which is a combination of gliterr and literati to denote the intellectual elite) except applied to technology.",
	"digital camera": "In 1990s, the world saw the advent of digital photography and companies. Once prohibitively expensive, became accessible due to competition and technological advancements. However, the rise of smartphones overshadowed both film and digital cameras,",
	"digital dictionary": "Knowing the meaning of the words in seconds fascinates everyone. But in the 90s, if you don’t know the meaning of a word you had to look it up in the big thick book called dictionary. It was released in 1991, and offered alphabetic and taxonomic access to English definitions.",
	"dir": "Dir stands for directory. In computing, it refers to two main things: A Directory, DIR command: DIR is also a built-in command in MS-DOS, Windows, and some other operating systems. Is used to list the contents of a directory.",
	"discman": "The Discman was the name given to the very first portable CD player released. The device was designed to play compact discs in a portable format, just like Walkman. It quickly became popular and inspired a generation of people to switch from cassette tapes to CDs. This device was incredibly popular.",
	"dma": "(Direct Memory Access): A technique for transferring data between a device and system memory without CPU intervention.",
	"dos": "Back before Windows as we know it today, Mac OS, and perhaps to a lesser degree Linux had become the standard home computer operating systems, most of us dealt with DOS (MS-DOS) at one point or another. See <denial of service>",
	"dos shell": "DOS Shell is a file manager, debuted in MS-DOS and IBM PC DOS v4.0 (June 1988). It was discontinued in MS-DOS v6.0, but remained part of the 'Supplemental Disk' until v6.22 (the last independent retail version of MS-DOS). It was, however, retained in PC DOS through PC DOS 2000.",
	"dot matrix printer": "Impact printer using pins and ink ribbon (precursor to laser/inkjet printers)",
	"dot-com": "The word that people used for an Internet company before the tech bubble burst and we switched to 'startup.'",
	"doom": "One of the most famous games distributed in shareware on the Internet. Its creators (3 young people) quickly became millionaires! :-) It has several levels, sound effects, is 3-dimensional and allows several players to play simultaneously, each on their own computer. A true classic in the genre (shots and explosions).",
	"download": "Download a file. The act of transferring the file from a remote computer to your own computer, using any communications protocol.",
	"edu": "Suffix present in various addresses on the Internet and designating teaching/educational institutions (edu=educational).",
	"electronic diary": "An electronic diary from the 90s was essentially a small, handheld device designed to store personal information digitally. It was a precursor to modern smartphones and PDAs. Some models had included additional features like calculators, games, and voice recording.",
	"elme": "An email program/reader for Unix environments (although versions can also be found for other operating systems). Based on menus with choice of options by letters and cursor keys.",
	"ega": "(Enhanced Graphics Adapter): A graphics standard for IBM PC compatible computers, offering improved color and resolution over CGA.",
	"emoticon": "see smiley.",
	"ethernet": "One of the possible architectures in local networks. Ethernet networks typically use coaxial cables that connect multiple computers. Each of them accesses the network in competition with the others, and there are rules/conventions that allow designating which computer should transmit information at a given moment. The information can be transmitted in 'Broadcast' mode, that is, to all other computers on the network and not just to one.",
	"eudora": "A very complete email program/reader, available on several platforms, including Macintosh and PC (Windows). Recommended.",
	"exite": "One of the most popular search engines on the web. Excite was a metasearch engine, which means that it aggregated and sorted through results provided by other search engines. It was eventually required by AskJeeves, which is now known as Ask.com",
	"fax": "Short for facsimile. Method of transmitting documents electronically over a telephone line. The document is scanned and sent over the phone line, and then reproduced at the receiving end.",
	"fqdn": "Fully Qualified Domain Name. Complete domain name, everything to the right of the @ symbol in an email address, without omitting any part (generally includes the name of the country, institution and at least one computer).",
	"flame": "Untimely and often provocative response to a news article or mail. A set of flames and counter-flames is called a 'flame-war'. Normally in this type of discussion, it is difficult to reach any conclusion...",
	"flame war": "See <flame>.",
	"floppy 3.1/2": "A floppy diskette is a type of disk storage composed of a thin and flexible disk of a magnetic storage medium in a square or nearly square",
	"floppy 5.1/4": "A floppy diskette is a type of disk storage composed of a thin and flexible disk of a magnetic storage medium in a square or nearly square",
	"floppy disk": "Removable magnetic storage medium using flexible disks (precursor to USB flash drive)",
	"floppy": "Casual term for a floppy disk",
	"follow up": "Reply to a news article with another news article, maintaining the same topic of discussion. discussion forum - In English, newsgroup. In a discussion forum, that is, a news group, people write (publicly) about the topic indicated by the name of the group.",
	"fidonet": "An early computer network system using BBSes for communication. Let's say that it is a type of Internet that is quite limited in terms of interaction, diffusion, speed and heterogeneity, when compared to the real Internet, but, of course, it has its own identity.",
	"finger": "Program to obtain information about a specific person who has an electronic address on the Internet. The email address of that person is indicated and it searches for and returns information relating to that person, after checking the computer where that person has their mailbox.",
	"firmware": "Software that is embedded in hardware and difficult to change.",
	"freeware": "Software distributed free of charge but according to some general principles such as the impossibility of changing any part for subsequent distribution, impossibility of sale, etc.",
	"ftp": "File Transfer Protocol. Designates the main file transfer protocol used on the Internet, or a program that uses this protocol.",
	"ftp server": "FTP server. Computer that has software files accessible through programs that use the file transfer protocol, FTP.",
	"full ip": "Full connection to the Internet, through a dedicated line, or other permanent means of communication. Therefore, all Internet services are available on the computer that has this type of connection.",
	"fyi": "For Your Information. Document(s) similar to the RFC, containing general information on topics relating to TCP/IP protocols or the Internet.",
	"game": "Simple text-based adventures or early graphical games with limited capabilities.",
	"game boy": "The Game Boy is a handheld game console developed by Nintendo, launched in the Japanese home market on April 21, 1989, followed by North America and Europe later that year. Another market hit and revolution.",
	"gaming consoles": "Atari, Nintendo, Sega, controllers, cartridges, etc.",
	"glitch": "Temporary or minor error in the system",
	"gif": "Graphic Interchange Format. Format for image files, widely used since the time it was popularized by Compuserve.",
	"gnu": "GNU's not Unix. Non-profit organization/Association that aims to promote (and does promote!) the development of software of all types (operating systems, compilers, etc.) comparable to Unix... but free! :-)",
	"gopher": "A distributed document-sharing protocol and system. Allows you to search for information in existing databases around the world, whether or not you use your own keyword search tools.",
	"gov": "Suffix for electronic addresses belonging to North American government organizations. Presently is worldwide.",
	"hard disk": "Rigid storage device with higher capacity than floppies (precursor to SSD)",
	"hierarchy": "Directory hierarchy is the set of directories in a given file system, which encompasses the root and all subdirectories. Newsgroups are also divided into a hierarchy, starting at the top levels (beginning of the group name: soc, comp, sci, rec, misc, etc.) and sub-divided into several themes, within each top designation. For example, there are several soc.culture groups, including soc.culture.brazilian. Generally, groups that starting with the ISO code of a country (e.g. pt) are only distributed nationally within that country (e.g. pt.geral, etc.)",
	"home page": "Base page of the WWW of an institution or individual. The base page is a kind of starting point for searching for information regarding that person or institution.",
	"host": "Central computer. Also called server or no' sometimes.",
	"howto": "Document(s) in electronic format, which accompany Linux (public domain version of Unix) and which constitute a type of manual, where you can look for information on almost all Linux installation, administration and updating tasks.",
	"how-to": "Document(s) in electronic format, which accompany Linux (public domain version of Unix) and which constitute a type of manual, where you can look for information on almost all Linux installation, administration and updating tasks.",
	"http": "Hypertext Transport Protocol. It is the protocol that defines how two programs/servers must interact, in order to transfer commands or information related to the WWW between them.",
	"hotbot": "It was the first search engine that allowed users to search within search results. By 1998, it was clear this wasn't working out for them and they were bought out by Lycos.",
	"imho": "In My Humble Opinion. In my humble opinion (NMMO). Acronym used when someone wants to express an opinion and likes to remain modest! :-) information super-highway - See information super-highway.",
	"internet": "With a lowercase i, Internet designates a network of networks only, and not specifically the Internet.",
	"internic": "An American Organization that assigns unique IP numbers to anyone who requests it and is also the manager of the root (top of the hierarchy) of the global DNS.",
	"information highway": "The information superhighway is a late-20th-century phrase that aspirationally referred to the increasingly mainstream availability of digital communication systems (and ultimately, the Internet and its World Wide Web).",
	"isp": "(Internet Service Provider): A company that provides internet access.",
	"icq":	"An online chat program and messaging system. From the ham radio term “CQ,” or “seek you.”",
	"information superhighway": "Basically, the Internet, back when we were really, really excited about it.",
	"ip": "It is the address that a machine has when connecting to the Internet. Each time the user connects, they obtain a new IP address.",
	"ip adress": "It is the address that a machine has when connecting to the Internet. Each time the user connects, they obtain a new IP address.",
	"irc": "Internet relay chat. IRCs were a staple of early Internet communication.",
	"irq": "(Interrupt Request): A signal from a hardware device to the CPU requesting attention.",
	"iso": "International Standards Organization. International organization for setting standards.",
	"kermit": "A communications program/protocol that allows, among others, the transfer of files between two machines.",
	"lan": "Local Area Network. Local network. It is a network with 2 or a few dozen computers that does not extend beyond the physical limits of any building. Typically used in companies for local interconnection of their computers. There are several technologies that allow the creation of a local network, the most important of which are Ethernet and Token-Ring.",
	"lan party": "A LAN party is an event to bring people together with their computers, to which they connect them on a local area network (LAN), generally with the aim of playing multiplayer computer games and more. Having its origins in northern Europe, where they are common, and its tradition dates back more than 20 years.",
	"latency": "Time that a unit of information takes to travel through a given means of communication. It can, for example, be said that the latency time of a VSAT satellite is 300 ms, which means that a character sent from one point takes 300 ms to reach another, passing through the satellite.",
	"leased-line": "Leased line. Most of the lines that connect the various Internet machines are leased lines available permanently. With a leased line, two computers are permanently connected. leased line - see leased-line.",
	"link": "On the WWW, a highlighted word indicates the existence of a link, which is a type of pointer to another source of information. By choosing this link, you obtain the information page that it designated, which may, in turn, also have several links. Today I am known as hyperlink/hyperlink. Unix/Linux term.",
	"linux": "Name derived from the name of the author of the core of this operating system, Linus Torvalds. Linux is nowadays an operating system with all the characteristics of Unix, with an enviable implementation and in constant evolution... and it is in the public domain. It is normally distributed in different 'releases' which are nothing more than a (recompilable) core accompanied by programs, utilities, tools, documentation, etc.",
	"lycos": "Lycos was launched in 1994, a time when the average user was just being introduced to the internet. Who doesn't their remember the 'Go get it!' commercials featuring the black lab being sent in search of Claudia Schiffer? Now there's a bit of classic 90s nostalgia.",
	"lynx": "A program (browser) to browse the WWW. Lynx was designed to be used in text terminals, so only the textual information can be viewed, with the remainder (images, sounds, etc.) available for recording on your computer's disk for later viewing/listening.",
	"man": "Metropolitan Area Network. Computer network extending up to a few tens of kilometers, normally interconnecting a few hundred computers in a given region.",
	"mail bomb": "It is the technique of flooding a computer with electronic messages.",
	"multi-frequency": "Designation for a telephone line capable of carrying electrical signals at different frequencies. These are the lines that allow you to have a telephone where dialing is done using tones and not impulses.",
	"midi": "Musical instrument digital interface. Anyone who played video or computer games in the '90s should be familiar with the unique sound of MIDI files.",
	"mil": "Suffix for electronic addresses belonging to North American military organizations.",
	"mime": "Multipurpose Internet Mail Extensions. Set of rules defined to allow the sending of electronic mail (text) with other documents (graphics, sounds, etc.) attached.",
	"modem": "Device for dial-up internet connection (precursor to cable/DSL/fiber optic modems). MODulator DEModulator.",
	"mosaic": "The first program (browser) for the WWW designed by NCSA (USA). With it, the WWW gained a huge boost as it was the first tool that allowed viewing WWW information and using it in a graphic and attractive way.",
	"mud": "Multi User Dungeon. A game for multiple users, normally present on any server on the Internet. It is a kind of Virtual World where various users can meet and interact. Normally, everything is written verbatim (no pretty images or flashy sounds).",
	"msdos": "Stands for Microsoft Disk Operating System, a popular operating system for IBM PC compatible computers in the 1980s",
	"net": "Network (of computers, in this context). Term applied and used as an internet identifier or (www).",
	"netiquette": "Set of rules and advice for good use of the Internet, in order to avoid mistakes made by beginners when interacting with other (more experienced) users. Netiquette is very much based on simple and elementary common sense.",
	"netscape": "A program (browser) for the WWW. Successor to Mosaic and developed by the same team of programmers, Netscape evolves faster and is the most used WWW browser, due to its speed, caching, internal visualization of various file formats, support for a more advanced page description language. evolved, etc.",
	"newbie": "Noob. Derogatory designation given by veterans to those who have recently discovered it.",
	"news": "Abbreviation for Usenet News, news are discussion groups, organized by themes (more than 10,000!), most of them with international distribution, and there may be some distributed in just one country or institution. In these public groups, anyone can read articles and write their own articles. Some groups are moderated, meaning that a human designated for this purpose reads the articles before they are published, to verify their compliance with the group's theme. However, the vast majority of groups are not moderated.",
	"newsgroup": "A news group, forum or discussion group.",
	"newsgroups": "A news group, forum or discussion group.",
	"ncsa": "National Center for Supercomputing Applications.",
	"napster": "Napster was a groundbreaking peer-to-peer (P2P) file-sharing application that disrupted the music industry in the late 1990s. It allowed users to share MP3 audio files directly with each other, creating a vast digital library accessible to millions.",
	"netizen": "Literally, a citizen of the net, back when we thought of it as a whole different, exotic country.",
	"nnrp": "Network News Reading Protocol. Protocol that allows a news reader program to obtain information (articles, groups, etc.) from a news server.",
	"nntp": "Network News Transport Protocol. Protocol for transferring Usenet newsgroups and control messages.",
	"norton commander": "A file manager that offered a dual-pane interface, making it efficient for navigating and managing files.",
	"offline": "not available on or performed using the internet or other computer network. | not available (as for communication) especially by way of the the Internet",
	"pda": "PDAs were handheld devices that combined features like address books, calendars, calculators, and sometimes even basic games. (Palm, Casio, Psion)'s",
	"palmtop": "A palmtop is a 'computer small and light enough to be held in your hand.' Sound familiar? Back in the '90s the palmtop PC, with its tiny keyboard and adorable little smart pen, was the best way to show people around you that you were a BOSS. Then, the iPhone arrived.",
	"path": "The path command specifies the location where MSDOS should look when it executes a command.",
	"pager": "A pager, also known as a beeper or bleeper, is a wireless telecommunications device that receives and displays alphanumeric or voice messages.",
	"pager's": "A pager, also known as a beeper or bleeper, is a wireless telecommunications device that receives and displays alphanumeric or voice messages",
	"palmtop": "Palmtop refers to a small, handheld computer that can fit in the palm of your hand. It's an older term used to describe early mobile computing devices. Think of it as a precursor to today's smartphones, but with much more limited capabilities.",
	"pgp": "Pretty Good Privacy. Program for encoding text messages, invented by Philip Zimmerman. A message sent in this way is unbreakable and only the recipient can decode it, giving a key that only he knows.",
	"pine": "An email program/reader for Unix environments (although versions for other operating systems can also be found). Based on menus with choice of options by letters and cursor keys. Users say that it is simpler than elm... It also supports the MIME message format (text messages with other types of attached files).",
	"ping": "Small utility used to see if a given connection is active and how long it takes for a message to go from one point of the connection to another. Ping sends packets (generally 64 bytes) to a peer, which responds by sending another equivalent packet.",
	"phreaking": "This just means hacking the telephone system, which isn't as exciting as it sounds.",
	"poloroid": "Polaroid is a brand synonymous with instant photography. These cameras produce physical prints immediately after taking a picture. Known for their square format and distinctive white borders.",
	"post": "Designates a news article, sometimes. Making a post means writing and submitting an article to a news group.",
	"ppp": "Point to Point Protocol. PPP implements the TCP/IP protocol (the Internet protocol(s)) on a telephone line, so that through it a personal computer can connect to the Internet and take advantage of all existing services and applications. It is a standard, subsequent to SLIP and more complete.",
	"protocol": "A protocol is to computers what a language (language) is to humans. To be able to transfer information between two computers, two computers must use the same protocol (or have a third party that understands both protocols and carries out the translation). public domain - Public Domain.",
	"public domain": "Something that is in the public domain (software, for example) is something that you can copy, cut, paste, burn, distribute, enjoy and generally use without paying anything! :-) Normally due credit should be given to the author(s) of that something.",
	"publify": "Another vaguely sexual sounding word that simply means 'to publish online.'",
	"pulse": "Impulse. A telephone line is pulsed if not multifrequency, that is, typing signals are sent by a series of small pulses, separated by spaces. Typing (and call establishment) on these types of lines is slower.",
	"phreaking": "It is the improper use of telephone lines, landlines or cell phones.",
	"problem solver": "one who solves problems.",
	"readme": "Read me. file that must be read before starting to use or install a specific program, system, computer, etc. It generally contains information that can save time for the user who wants to do something (and that something has an accessible README file).",
	"reboot": "Before 'restart' you used to use 'reboot' to describe the arduous process of putting your computer to sleep and waking it up again to get it to work properly.",
	"rfc": "Request For Comments. Documents that define standards and protocols for the Internet and where technical-level discussions are held to define new protocols.",
	"rtfm": "Read The Fucking Manual. Read the '#$%' manual. Term used to indicate to someone that they should read the manual, as they are probably asking questions that are clearly answered there.",
	"scanners": "Scanners are programs that look for open TCP ports through which an invasion can be carried out. So that the scan is not noticed by the victim, some scanners test a computer's ports for many days, at random times.",
	"screensaver": "Nowadays, computers just go to sleep to save battery, so gone are the days when you got to pick a nice ocean view or rainforest as your special monitor.",
	"shareware": "Software that is distributed freely, as long as its original format is maintained, without modifications, and due credit is given to its author. Typically, it was designed to be tested over a short period of time (test/evaluation period) and, if used, the user has a moral obligation to send payment to its author (in the order of a few - a few - tens of dollars ).",
	"site": "An Internet 'site' is one of the existing nodes/computers. For example, an FTP site is a computer that offers the FTP service (identical to FTP server).",
	"slip": "Serial Line Internet Protocol. SLIP implements the TCP/IP protocol (the Internet protocol(s)) on a telephone line, so that through it a personal computer can connect to the Internet and take advantage of all existing services and applications. It was the first protocol defined for the use of TCP/IP on telephone lines.",
	"smiley": "They are small sets of ASCII characters that aim to convey an emotion or state of mind. They should be viewed from the side, with the sheet at 90 degrees... The best known are: :-) or :) :-( or :( ;-) or ;)",
	"smtp": "Simple Mail Transport Protocol. Protocol used between programs that transfer electronic mail from one computer to another.",
	"smurf": "The attacker sends a sequence of Ping requests and floods the computer.",
	"sniffing": "Analyzes network traffic. In the hands of hackers, it steals passwords (pwd's) and confidential information.",
	"sockets": "The name of the Unix interface (originally, but also existing on other platforms) that implements the TCP/IP protocols. An interface is a set of possible calls to libraries that contain routines implementing certain objectives, in this case, TCP/IP communication.",
	"soup": "Simple Offline Usenet Protocol. 'Standard' (or program) that defines what a compressed package of electronic letters and news articles should look like, to be read offline, by any text editor program that understands that format.",
	"spam": "Publishing the same news article to multiple discussion groups, often resulting in wasted disk space and bandwidth on transmission media.",
	"spreadsheet": "Software for data analysis and creating spreadsheets (e.g., Lotus 1-2-3, Excel)",
	"spoofing": "The act of disguising a communication as coming from another source.",
	"surf": "On the Internet it means wandering around, looking for information, especially on the WWW. You can also say surfing, for the more radical! :-)",
	"sysadmin": "System Administrator. The person responsible for a system.",
	"system v": "A (commercial) version of the Unix operating system.",
	"talk": "Program that allows two users (there are versions that allow more users) to 'dialogue textually' directly over the Internet.",
	"tape": "Cassettes and tapes were a popular for recordings and playbacks formats in the 1990s. They consisted of a plastic case containing a magnetic tape that stored video/sound or just sound. To play those tapes, you would insert in the cassette player or VCR and press play.",
	"tamagotchi": "Is a brand of handheld digital pets that was created in Japan. It was released by Bandai on November 23, 1996 in Japan and in the United States on May 1, 1997, quickly becoming one of the biggest toy fads of the late 1990s and the early 2000s.",
	"telnet": "A network protocol used for accessing remote computer systems.",
	"thread": "Within a discussion group, there are typically several threads. A thread represents a specific subject discussed there and is composed of one or more articles.",
	"tim berners lee": "The man, at the time a researcher at CERN, who defined/invented the HTTP protocol and gave rise to the WWW.",
	"tone": "As opposed to <pulse>, tonality. On the tone telephone line (multifrequency), dialing a number results in the sending of signals at different frequencies (different sounds). Dialing a number (call establishment) on this type of line is faster than on a pulse line.",
	"trojan horse": "It's a kind of virus (you program it to do whatever you want). Much more powerful than a common virus whose sole function is to destroy computers, that is, it is a disguised program that performs some task.",
	"trumpet": "Trumpet is the name given to programs that implement and use TCP/IP in a Windows environment, made by Peter Tattam. The most important is the Trumpet Winsock. Firm name.",
	"uart": "Universal Asynchronous Receiver Transmitter. Integrated circuit responsible for communications through a serial port on a computer.",
	"udp": "User Datagram Protocol. One of the protocols in the Internet protocol suite (commonly called TCP/IP). It corresponds to level 4 of the OSI model, as it is a transport protocol, without connection. In UDP, a message is sent to the destination, without there being a logical connection made between the source and the destination (similar to a telephone connection between two points). The message packet(s) can then pass through several Internet nodes until it reaches its destination. Less viable than TCP (another transport protocol, but with a connection), but very useful when the loss of one packet or another is not important and you want speed in transmission and avoiding the overload of several established logical connections.",
	"url": "Uniform Resource Locator. Universal Resource Locator. Method of specifying a given resource on the Internet, whether obtained by FTP, News, Gopher, Mail, HTTP, etc. It aims to standardize the way of designating the location of a certain type of information on the Internet. Example: http://www.insa-lyon.fr - request, via HTTP, from the INSA Lyon home page (WWW). usenet - Set of discussion groups, articles and computers that transfer them. The Internet includes Usenet, but Usenet can be carried by computers outside the Internet.",
	"uucp": "Unix to Unix Copy. An (old but still used) method for transmitting mail and Usenet articles between computers. Originally designed to transmit between Unix computers, it is now also possible to use it on other types of computers. uudecode - Program to decode a text file and transform it into the corresponding binary. Together with uuencode, it allows you to transfer binaries (therefore, any software) through a simple text file.",
	"usenet": "A distributed discussion system based on the concept of newsgroups.",
	"utility software": "Programs for specific tasks like file management, disk formatting, or system maintenance",
	"v.32": "One of the standards established for modems and which defines data transmission at a speed of 14400 bps.",
	"v.32bis": "One of the standards established for modems and which defines data transmission at a speed of 14400 bps.",
	"v.34": "One of the standards established for modems and which defines data transmission at a speed of 28800 bps.",
	"v.fast": "A pseudo-standard defined by modem manufacturers to allow data transmission at a speed of 28800 bps. Obsolete with the arrival of standard V.34.",
	"video store": "Was a physical retail store where people could rent movies and video games. They typically had a vast collection of VHS tapes, and later, DVDs. Customers would browse the shelves, select their desired media, and pay a rental fee. Popular names from the 90's: Blockbuster, Hollywood Video, Video Warehouse.",
	"vsat": "Very Small Aperture Terminal. A VSAT antenna allows data transmission (sending and receiving) to another VSAT antenna, using a part of the bandwidth available on VSAT satellites.",
	"vt100": "A type of terminal emulation very common on the Internet.",
	"vga": "(Video Graphics Array): A graphics standard that replaced EGA, providing higher resolution and more colors.",
	"vcr player": "A videocassette recorder (VCR) or video recorder is an electromechanical device that records analog audio and analog video from broadcast television or other AV sources. Purchase and rental starting in the 80s and 90s, most popularly in the VHS videocassette format. Blank tapes were sold to make recordings.",
	"vhs": "The VHS (Video Home System) is a standard for consumer-level analog video recording on tape cassettes, introduced in 1976 by JVC it was the dominant home video format throughout the tape media period in the late 1970s, 1980s, and 1990s.",
	"x.25": "A packet transfer protocol, without logical connection, defined by public telecommunications operators in Europe (mainly to make money!",
	"xmodem": "A relatively slow modem data transfer protocol.",
	"walkman": "Walkman is a brand of portable audio players manufactured and marketed by Japanese company Sony since 1979. Sony introduced the Walkman audio cassette player and created a revolution.",
	"web": "Abbreviation to designate the World-Wide-Web.",
	"world wide web": "The World Wide Web is essentially a system that allows you to access and share information online. It's what you're using right now to read this text! born in 1990 with the first browser, has revolutionized life, granting universal access to information across devices and operating systems.",
	"world-wide-web": "The World Wide Web is essentially a system that allows you to access and share information online. It's what you're using right now to read this text! born in 1990 with the first browser, has revolutionized life, granting universal access to information across devices and operating systems.",
	"word processor": "Software for creating and editing text documents (e.g., WordPerfect, WordStar)",
	"whois": "Directory of electronic addresses of people and computers, on the Internet, containing relative information.",
	"winsock": "Implementation of the sockets interface for Windows. With a winsock (program/library for Windows) it is possible to use the SLIP and/or PPP protocols in Windows, that is, it is possible to speak the same 'language' as other computers on the Internet.",
	"wysiwyg": "(What You See Is What You Get): A display mode that shows the document as it will appear when printed.",
	"www": "Acronym for World-Wide-Web.",
	"www server": "A computer that provides services on the WWW, which has information accessible on the WWW.",
	"y2k": "2000 was the most exciting New Year's Eve ever, as you counted down expecting software to spontaneously combust at midnight due to Y2K- a computer bug that would cause software to think the year 2000 was the year 1900. Luckily, the new century was welcomed largely without incident.",
	"yanoff": "Scott Yanoff. A man who remembered to create a list (Yanoff's List) that contains electronic addresses and indications of other resources for obtaining information on the Internet. This list is structured into themes (from Agriculture, Biochemistry, Sports, etc.) and is regularly updated. It doesn't contain directions to everything that exists on the Internet (as that's impossible) but it can be of great help.",
	"ymodem": "A data transfer protocol via modem, with some improvements compared to Xmodem.",
	"zip drive": "A Zip drive was a type of removable storage device popular in the 1990s. It was essentially a larger, higher-capacity version of a floppy disk.",
	"zettabyte": "The scale for storage is kilo, mega, giga, tera, peta, exa, and zetta. The way we're going, this one might actually catch on one day!",
	"zmodem": "A data transfer protocol via modem, with some improvements compared to Xmodem and Ymodem, in particular, faster.",
	"zx spectrum": "Is an 8-bit home computer developed and marketed by Sinclair Research. Considered one of the most influential computers ever made. Memory: 16 KiB / 48 KiB / 128 KiB Processador: Z80 - 3,5 MHz. “Every man should plant a tree, build a house, and write a ZX Spectrum game”.",
	"ms-dos": "Stands for Microsoft Disk Operating System, a popular operating system for IBM PC compatible computers in the 1980s",
	"@echo off": "Classic command in batch scripting.",
	"pc shell": "popula2841r file manager with a similar dual-pane interface."
}
#----------------------------------------------------------------------
core["old_tech_term"] = list(oldtech_terms.keys())
chkdict.append(sum(sum(ord(char) for char in word) for value in oldtech_terms.values() for word in value))

#----------------------------------------------------------------------
meaning_term = {
	"3r paradigm":"The 3Rs are reuse, reduce and recycle.\n",
	"4r rule":"The 4R rule refers to the principles of Reduce, Reuse, Recycle, and Restore. This principle applies to waste management recycling strategies that are most environmentally sustainable.\n",
	"8 stores of energy":"The 8 (eight) 'stores' of energy are: thermal, light, mechanical, electrostatic, elastic, gravitional, nuclear, chemical, kinetic.",
	"ancient":"A Glimpse into the Past. Something very old, often dating back to a time long before recorded history.\n",
	"anthropocene":"The Anthropocene Epoch is an unofficial unit of geologic time, used to describe the most recent period in Earth and is history when human activity started to have a significant impact on the planet climate and ecosystems.\n",
	"as":"Her digital identity is cloaked in a mystique of cryptic monikers, such as war10ck, unknown, gozil4 and the enigmatic thE gUArDIaN angeL, my creator " + _author_ + " (AS).\n" ,
	"asctr":"Adelino Saldanha Completed TRails / Routes. Find'it all in here : "+website['trails']+"\n",
	"atlantic ocean":"Is the second-largest of the world's oceans, with an area of about 106.460.000 km2. It covers approximately 20% of Earth's surface and about 29% if its water surface area. It is known to separate the 'Old World' from the 'New World'.\n",
	"bcorp":"Companies and Organisations that focus on the positive consequences that their actions have on their host territory and on the lives of their workers.\n",
	"blue zone":"Describe the regions of the world where people live longer and healthier lives than average. The zones are also defined as a limited and homogeneous geographical area in which the population shares the same lifestyle and environment.\n",
	"biosphere":"Part of the earth where life can create and sustain itself. It’s a limited zone on the surface of the earth where soil, water, and air come together to support life.\n",
	"boomers":"People who were born between 1955 and 1964, actualy having betwwen " +str(date.today().year - 1964) +" and "+str(date.today().year - 1955) +" years old.\n",
	"boomers ii":"People who were born between 1955 and 1964, actualy having betwwen " +str(date.today().year - 1964) +" and "+str(date.today().year - 1955) +" years old.\n",
	"carcinogens":"Carcinogens are substances and agents that have the potential to cause cancer in humans. Common carcinogens found in electronic waste include lead, mercury, arsenic, chromium, flame retardants, and various forms of silicon, among others.\n",
	"chatbot":"A chat bot is a program that simulates conversation with humans. It can understand and respond to your questions and requests.\n",
	"change maker":"It's about finding out what your passions really are, where your skills are, and what the world needs, and them figuring out how those intersect!.\n",
	"climate change":"Here's a litle trick: See the 'Weather like your mood; climate like your personality'.\n",
	"climate":"The average weather conditions of a place over a period of years.\n",
	"consuming sustainably":"Means Doing more and better, but with less.\n",
	"core":"Core typically refers to the central or most important part of something. It can be physical, like the core of a planet, or conceptual, like the core of an argument. It often implies something essential or fundamental.\n",
	"cortisol":"Also popularly called stress hormone Cortisol is a steroid hormone that regulates mood, motivation and fear. Produced in the adrenal glands.\n",
	"cybele meaning":"My name meaning is from the primordial asteroid with same but also for the Madrid plaza.\n",
	"cybele":"That's Me.\n",
	"cyberspace":"First appeared in fiction in the 1980s in the work of cyberpunk science fiction author William Gibson, first in his 1982 short story 'Burning Chrome' and later in his 1984 novel Neuromancer. In the next few years, the word became prominently identified with online computer networks.\n",
	"cyber security":"Cyber security is the system of defense to protect computer systems and networks from malicious attacks.\n",
	"da bomb": "This meant : 'really cool' or 'awesome'.\n",
	"dangerous asteroids":"Generally refered to Near-Earth Objects (NEOs) that could potentially pose a significant threat to Earth if they were to collide with it.\n",
	"data breach":"Data breach is a security violation, where information is stolen from a computer system or network without the owner or user’s knowledge or authorization.\n",
	"dbms":"Database management system. A database is usually controlled by a DBMS.\n",
	"degaussing":"This is a method of physically destroying the disks and drives by scrambling the magnetic sectors on them, as well as damaging their internal components like their read/write heads so the disks/drives are rendered completely useless.\n",
	"density":"The ratio of the mass of an object to its volume. For example, water has a density of one gram of mass for every milliliter of volume.\n",
	"digital image":"A digital image is a representation of a picture in numerical form. It's composed of tiny squares called pixels. Each pixel has a specific color assigned to it. When viewed together, these pixels create the image we see. Think of it like a mosaic, but with millions of tiny tiles (pixels) instead of larger pieces.\n",
	"dryland":"Are defined by a scarcity of water. Drylands are zones where precipitation is balanced by evaporation from surfaces and by transpiration by plants (evapotranspiration). The United Nations Environment Program defines drylands as tropical and temperate areas with an aridity index of less than 0.65.\n",
	"dryland farming":"Dryland farming is crop production in semiarid regions of the world with no irrigation. Historically these regions have provided much of the world's grain supply.\n",
	"eco conscious traveller":"Also commonly referred to as GREEN travelling or planet-friendly travel, eco-friendly tourism is a commitment towards making choices that have minimal adverse impact on local communities and ecosystems.",
	"eco friendly tourism":"Sustainable tourism is a type of tourism that includes concern for sustainability, that is, economic, social and environmental issues, as well as attention to improving tourists' experiences and meeting the needs of host communities.",
	"eco-conscious traveller":"Also commonly referred to as GREEN travelling or planet-friendly travel, eco-friendly tourism is a commitment towards making choices that have minimal adverse impact on local communities and ecosystems.",
	"edible packaging":"This type of packaging is made from materials there are safe to eat. It's an idea that combines sustainability and creativity, reducing the environmental of plastic waste. Food serves as both.\n",
	"eee":"Electrical and electronic equipment.\n",
	"enarenado":"Cultivate the land under a layer of sand to preserve water evaporation.\n",
	"earthing":"Is the practice of connecting with the Earth's energy by either making direct physical contact with the ground (or water).\n",
	"eight stores of energy":"The eight 'stores' of energy are: thermal, light, mechanical, electrostatic, elastic, gravitional, nuclear, chemical, kinetic.",
	"elliptical":"Shape: Someting that is shaped like an oval or ellipse. Language: A sentence or phrase where words are omitted but still understood in context.\n",
	"earth day":"Activist Jonh McConnel proposed that United Nations set up a day to honor peace and the earth. Earty day has been celebrated every year since 22 April 1970.\n",
	"eol":"It’s the point at which a device has reached the natural end of its life. It can no longer be used by anyone for any purpose. When a device reaches its end of life, it must be disposed of properly.\n",
	"eou":"It’s the point at which an electronic device has reached its end of ‘regular’ or ‘original’ use. At this stage, the device can be donated, repurposed, or refurbished for further use or ‘reuse’.\n",
	"fifo":"First in, First Out - Practice: The first food into the fidge must be the first one out.",
	"filofax":"The name 'Filofax' is actually a brand name, but it's become so synonymous with the product that it's often used as a generic term for this type of organizer. It's essentially a loose-leaf binder with interchangeable pages.\n",
	"frequency":"Describes the number of wave crests passing by a fixed point in a given time period (usually one second). Frequency is measured in Hertz (Hz).\n",
	"games":"You can play World Capitals, Constellations, Elements from Periodic Table and Math.\n",
	"gen jones":"People who were born between 1955 and 1964, actualy having betwwen " +str(date.today().year - 1964) +" and "+str(date.today().year - 1955) +" years old.\n",
    "gen millenials":"People who were born between 1981 and 1994, actualy having betwwen " +str(date.today().year - 1994) +" and "+str(date.today().year - 1981) +" years old.\n",
    "gen x":"People who were born between 1965 and 1980, actualy having betwwen " +str(date.today().year - 1980) +" and "+str(date.today().year - 1965) +" years old.\n",
    "gen y":"People who were born between 1981 and 1994, actualy having betwwen " +str(date.today().year - 1994) +" and "+str(date.today().year - 1981) +" years old.\n",
    "gen z":"People who were born between 1995 and 2009, actualy having betwwen " +str(date.today().year - 2009) +" and "+str(date.today().year - 1995) +" years old.\n",
    "generation jones":"People who were born between 1955 and 1964, actualy having betwwen " +str(date.today().year - 1964) +" and "+str(date.today().year - 1955) +" years old.\n",
    "generation millenials":"People who were born between 1981 and 1994, actualy having betwwen " +str(date.today().year - 1994) +" and "+str(date.today().year - 1981) +" years old.\n",
    "generation x":"People who were born between 1965 and 1980, actualy having betwwen " +str(date.today().year - 1980) +" and "+str(date.today().year - 1965) +" years old.\n",
    "generation y":"People who were born between 1981 and 1994, actualy having betwwen " +str(date.today().year - 1994) +" and "+str(date.today().year - 1981) +" years old.\n",
    "generation z":"People who were born between 1995 and 2009, actualy having betwwen " +str(date.today().year - 2009) +" and "+str(date.today().year - 1995) +" years old.\n",
	"getaway":"A getaway is a short escape from your usual routine or environment. It's a chance to relax, unwind, and recharge.\n",
	"ghg":"also known as Greenhouse gases are gases in the earth's atmosphere that trap heat.\n",
	"gozli4":"Her online persona is a puzzle of aliases, with war10ck, unknown, gozil4, and the curiously formatted thE gUArDIaN angeL as her chosen identifiers. My creator, " + _auth1r_ + ".  \n",
	"gr":"GR, the Grandes Routes are more than 30 km long or more than one journey to go, signposted in white and RED. Once approved by the Federation of Camping and Mountaineering of Portugal, they are marked in both directions, according to the agreed marks.\n",
	"greenhouse gases":"also known as GHGs gases are gases in the earth's atmosphere that trap heat.\n",
	"hertzian waves":"An electromagnetic wave produced by the oscillation of electricity in a conductor (as a radio antenna) and of a length ranging from a few millimeters to many kilometers. There is 7 types of waves are as follows: Radio Waves, Microwaves, InfraRED, Visible, Ultraviolet, X-Ray, Gamma Rays. Radio waves have the longest wavelength and small frequency while the gamma rays have shortest wavelength and high frequency.",
	"hiking alone":"1.Choose a Local or State Park for Your First Solo Hike. 2.Pick an Easy Trail with Less Mileage Than Usual. 3.Making Sure You Stay on Trail and Don't Get Lost. 4.Let Someone Know Your Plans. 5.Share your location with family or friends. 6.Pack Everything You Need and Then Some. 7.Know What to do in a Wild Animal Encounter. 8.General Safety on the Trail.\n",
	"ict":"Information and communication technology.\n",
	"ideal world":"We would have an economy where businesses value people and the environment over profit, and make decisions based on values and not price. Production and consumption rate allows the Earth's systems to replenish themselves and stay in balance.\n",
	"iot":"IoT - Internet of Things.\n",
	"leaping bunny":"Borned in 1996 to international certify that no new animal tests have been used in the development of any product bearing it.\n",
	"metal":"A solid material that is typically hard, shiny, malleable, ductile, and an excellent conductor of heat and electricity.\n",
	"millenials":"People who were born between 1981 and 1994, actualy having betwwen " +str(date.today().year - 1994) +" and "+str(date.today().year - 1981) +" years old.\n",
	"mindset":"A set of attitudes or fixed ideas that somebody has and that are often difficult to change synonym mentality.\n",
	"minimalism":"Is all about owning only what adds value and meaning to your life (as well as the lives of the people you care about) and removing the rest. It's about removing the clutter and using your time and energy for the things that remain. We only have a certain amount of energy, time, and space in our lives.\n",
	"molecule":"A tightly knit group of two or more atoms bound together by electromagnetic forces among the atoms electrons and nuclei. For example, water (H2O) is two hydrogen atoms bound with one oxygen atom. Identical molecules have identical chemical properties.\n",
	"my mindset":"I am already complete. I dont need anyone to complete me.\n",
	"nearly circular":"Something is shaped or allmost like a circle.It's like a circle that's been slightly squished or streched. Oval, Some coins, Planet Orbits.\n",
	"neo":"A near-Earth object is an asteroid or comet which passes close to the Earth's orbit. In technical terms, a NEO is considered to have a trajectory which brings it within 1.3 astronomical units of the Sun and hence within 0.3 astronomical units, or approximately 45 million kilometres, of the Earth's orbit.\n",
	"obsolescence":"Obsolescence refers to the process of becoming old, obsolete, or outdated. When talking about e-waste, obsolescence refers to a culture and intentional practice.\n",
	"pacific ocean":"Is the largest and deepest of Earth's oceanic divisions. At 165,250.000 km2 is the largest division of the World Ocean-and, in turn, the hydrosphere-covers about 46% of Earth's water surface and about 32% of is total surface area making it larger than all of the Earth's land area combined. Its mean depth is 4.000 meters. Deep in the Mariana Trench, is the deepest point of the world, reaching a depth of 10.928 meters.\n",
	"phas":"Potentially Hazardous Asteroids (PHAs). These are objects larger than approximately 140 meters in size with orbits that bring them within about 7.5 million kilometers of Earth's orbit.\n",
	"pmr ch4":"The "+ _auth1r_ +" walkie-talk tekking frequency (446.04375 Mhz) world wide. \n",
	"pmr channel 4":"446.04375 Mhz. The "+ _auth1r_ +" walkie-talk tekking frequency world wide. \n",
	"power":"It's the ability to direct or influence another's behavior or course of events.\nsupply (a device) with mechanical or electrical energy. \n",
	"pr":"PR, the Little Rota, do not exceed 30 km in length or less than a journey to travel, and are signaled in YELLOW and RED. PL, the Local Routes, were created in Portugal in 2006, and where the entirety, or more than half of the route takes place on an urban route, signaled in GREEN and white.\n",
	"practice earthing":"Is connecting with the Earth's energy by either making direct physical contact with the ground (or water).\n",
	"radio wave":"Radio waves are a type of electromagnetic radiation with the longest wavelengths. They are used for communication, broadcasting, and radar systems.\n",
	"refurbishing":"Refurbishing is the process of cleaning up an old item and repairing it to work like new. Responsible waste management recycling uses refurbishment as a significant part of the process where old or discarded devices are cleaned up, repaired, recycled, and remade to function like new.\n",
	"right to disconnect": "The right to disconnect came into effect on 26 August 2024 for employees of organisations that employ 15 or more people. Employees of small businesses (those with less than 15 employees) will get the same right in a year's time on 26 August 2025.",
	"right to roam":"The 'Right to roam', or free access right, is a movement that supports people's right to freer access and cross private lands for recreational purposes. Born in Scandinavia, this concept has spread to various countries, where laws allow citizens to explore nature without excessive restrictions.\n",
	"sapiosexual":"Sapiosexuality is the sexual attraction to intelligence.",
	"seti":"Is an acronym that stands for Search for Extraterrestrial Inteligence. It's a scientific field dedicated to find evidence of intelligent life beyond Earth.\n",
	"shredding":"Once all the valuable and usable materials are separated from discarded electronics, what’s left is an unusable waste. That scrap is physically shredded through machines and turned into dust and debris to ensure complete data erasure.\n",
	"simbad":"SIMBAD is a bibliographic database of astronomical objects of interest outside the solar system: stars, galaxies, interstellar/intergalactic medium sources, clusters of stars/galaxies, exoplanets, gravitational sources, and transient events.",
	"speed of light":"The speed of light is the maximum velocity at which energy and information can travel. It's a fundamental constant in physics, approximately 299,792 kilometers per second. No object with mass can reach this speed.\n",
	"speed of sound":"The speed of sound is the rate at which sound waves travel through a medium. In dry air at 20°C, it's approximately 343 meters per second, which equates to about 1,235 kilometers per hour.\n",
	"talk to the hand": "This was a way to dismiss someone, with a hand gesture\n",
	"taping movies":"Taping movies meant recording films from television onto videotape using a VCR (Video Cassette Recorder). This was a common practice before the widespread availability of digital video recorders (DVRs) and streaming services.\n",
	"temperature":"Measures the average kinetic energy of particles in a substance. It indicates how hot or cold something is and determines heat flow direction.\n",
	"the 4r rule":"The 4R rule refers to the principles of Reduce, Reuse, Recycle, and Restore. This principle applies to waste management recycling strategies that are most environmentally sustainable.\n",
	"think circular": "Share, Reuse, Recycle. Help save the planet.\n",
	"thermal emission":"Heat energy given off by an object in the form of electromagnetic radiation (light). Thermal emission is directly related to an object's temperature.\n",
	"tv guide":"A printed publication that provided a schedule of television programs. It listed shows by channel, time, and day, often including brief descriptions or synopses. People relied on TV guides to plan their viewing, check for their favorite shows, and discover new programs.\n",
	"ultraviolet":"(UV) is invisible light with shorter wavelengths than visible light. It comes from the sun and artificial sources. UV has both beneficial and harmful effects on humans and the environment.\n",
	"ulez":"Ultra Low Emission Zone. Represents a vision of the future, demonstrating how ambicious environmental policies can transform our cities.\n",
	"uptime cybele":"I am running since " + _active_ + " so it makes " + str(days_till_today.days) + " days.\n",
	"uv radiation":"Ultraviolet (UV) radiation is a form of non-ionizing radiation that is emitted by the sun and artificial sources. The beneficial effects of UV radiation include the production of a vital nutrient, vitamin D. However, overexposure may present risks.\n",
	"uv":"(Ultraviolet) Is invisible light with shorter wavelengths than visible light. It comes from the sun and artificial sources. UV has both beneficial and harmful effects on humans and the environment.\n",
	"vorian":"The " + _auth1r_ + " website: " + website['home'] + "\n",
	"version":"Software versioning is the process of assigning either unique version names or unique version numbers to unique states of computer software.\n",
	"war10ck":"My creator "+ _auth1r_ + ". Nick names like that one, War10ck, unknown, gozil4, and the enigmatically capitalized thE gUArDIaN angeL are the cryptic handles she's chosen to inhabit the digital realm.\n",
	"weee":"Waste from Electrical and Electronic Equipment.\n",
	"weight":"The force acting on an object due to gravity. Weight changes due to location. (Mass).\n",
	"y2k": "Refers to the year 2000, and the fear that computers would malfunction due to the date change.\n",
	"your core":"My core can be viewed and checked by the instruction <show core> in case you dont remember. \n",
	"your mindset":"I am already complete. I dont need anyone to complete me.\n",
	"zero miles product":"Refering to sustainability is a local produced product at a lower price, there is no transport and distribution costs.\n",
	"zero miles":"In sustainability refers you are buying a product what is local produced at a lower price, because there are no transport and distribution costs.\n",
	"zero waste":"The concept of zero waste describes a responsible means of production and consumption where products and materials are constantly recovered, repaired, and reused to prolong their lives to the fullest.\n",
}
#----------------------------------------------------------------------
core["word meaning"] = list(meaning_term.keys())
chkdict.append(sum(sum(ord(char) for char in word) for value in meaning_term.values() for word in value))

#----------------------------------------------------------------------
qa_astro = {
	"moon": "Earth's Failthful Companion. Is the only natural satellite of Earth. It's been a source of wonder and inspiration for humans since the beginning of time.\n",
	"moon distance": "The distance between Earth and the Moon is 384.400 km.\n",
	"distance to the moon": "from Earth is 384.400 km.\n",
	"percentage of water on earth": "About 71% of the Earth's surface is water-covered, and the oceans hold about 96.5% of all Earth's water.\n",
	"water on earth": "Earth holds an estimated 1,386,000,000 cubic kilometers of water.  Oceans hold about 96.5% of all Earth's water. Only a tiny fraction of Earth's water is freshwater, and much of that is locked up in ice caps and glaciers.\n",
	"how much water are on earth": "29% As air all around us, water covered almost 71% of our earth's surface. The remaining 29 % of the earth is covered by land means soil, also a natural resource.\n",
	"percentage of land on earth": "About 71% of the Earth's surface is water-covered, and the oceans hold about 96.5% of all Earth's water.\n",
	"sunset": "The time in the evening when the sun disappears or daylight fades.\n",
	"sunrise": "The time in the morning when the sun appears or full daylight arrives.\n",
    "what are the planets of the solar system": "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune. Total of 8 planets.\n",
	"how many planets are in our solar system": "There are eight planets in our solar system. They are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.\n",
	"what are the solar system planets order": "Our Solar System has 8 planets which orbit the sun. In order of distance from the sun they are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.\n",
	"planet that is closest to the sun": "Mercury.\n",
	"planet that is farthest from the sun": "Neptune.\n",
	"planet that is made of gas": "Jupiter.\n",
	"planet that has rings": "Saturn.\n",
	"planet with a red spot": "Jupiter.\n",
	"smallest planet": "Mercury.\n",
	"planet that has the longest day": "Venus. It completes one rotation every 243 Earth days. \n",
	"planet that has the shortest day": "Earth.\n",
	"hottest planet": "Venus.\n",
	"coldest planet": "Mercury.\n",
	"planet that has the most moons": "Ganymede (Jupiter).\n",
	"planet that is made of ice": "Pluto.\n",
	"which planet is not named after a greek or roman god": "Earth.\n",
	"planet with a blue atmosphere": "Neptune.\n",
	"planet with life": "Earth.\n",
	"sun distance": "Earth and Sun is about 149.600 million kilometer.\n",
	"actual space stations": "As of my knowledge, there are 2 fully operational space stations in low Earth orbit (LEO) the International Space Station (ISS) and China's Tiangong Space Station (TSS).\n",
	"how many asteroids are there": "It's estimated that there are millions of asteroids in our solar system. Between 700,000 and 1,700,000 asteroids with a diameter of 1 kilometer or more. It's important to note that this is just an estimate, and the actual number could be higher.\n",
	"about climate change": "A brief overview, refers to a long term shifts in the temperature and weather patterns. While these shifts can occur naturaly, the primary driver change since 1800s has been human activities, primarily the burning of fossil fuels. (Key points : GREENhouse gases, Global warming).\n",
	"do you think climate change is real": "The vast majority of scientists agree that climate change is real and caused by human activity.\n",
	"do you think there is life on other planets": "I think it's likely that there is life on other planets, but we don't have enough evidence to know for sure.\n",
	"what is gravity": "Gravity is a force that attracts any two objects with mass.\n",
	"what is the moon": "The Earth's only natural satellite and Earth's Failthful Companion. It's been a source of wonder and inspiration for humans since the beginning of time.\n",
	"closest star": "The Sun.\n",
	"name of our galaxy": "The Milky Way.\n",
	"largest known object in the universe": "A galaxy cluster.\n",
	"the big bang theory": "A cosmological model that explains the early development of the universe.\n",
	"what causes the phases of the moon": "The changing positions of the Sun, Moon, and Earth.\n",
	"who was the first person to walk on the moon": "Neil Armstrong.\n",
	"what is the name of the first orbital spacecraft": "Sputnik 1.\n",
	"what is the international space station": "A habitable artificial satellite in low Earth orbit. (ISS).\n",
	"what is the iss": "The International Space Station is a habitable artificial satellite in low Earth orbit.\n",
	"solar system planets order": "Based on primordial ancient knowledge... from de Sun: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.\n",
	"why the number of countries is different from capitals": "The number of capitals and counties can vary due to factors like dependent territories, multiple capitals per country, differing definitions of 'county', and potential data inaccuracies.\n",
	"why the number of capitals is different from countries": "The number of countries and capitals can vary due to factors like dependent territories, multiple capitals per country, differing definitions of 'county' and potential data inaccuracies.\n",
	"how much time takes the earth to make a complete rotation": "Earth takes exactly 86,400 seconds to perform a complete rotation. You can convert the amount of seconds using the syntax command.\n",
	"time takes the earth to make a complete rotation": "Earth takes exactly 86,400 seconds to perform a complete rotation. You can convert the amount of seconds using the syntax command.\n",
	"do you know new technologies": "All those actualy exists. We should also remember the day-to-day things we can do for our planet.\n",
	"what new technologies you know": "It's good to stay informed on new technologies that can help us, but we should also remember the day-to-day things we can do for our planet.\n",
	"percentage of freshwater on earth": "Of all Earth's freshwater, 68% is stored in Ice caps and Glaciers, and another 30% is found in groundwater. The tiny amount remaining is what we see in lakes and rivers.\n",
	"percentage of freshwater on the planet": "68% is stored in Ice caps and Glaciers, and another 30% is found in groundwater. The tiny amount remaining is what we see in lakes and rivers. This are the percentages of Of all Earth's freshwater.\n",
	"freshwater": "Of all Earth's freshwater, 68% is stored in Ice caps and Glaciers, and another 30% is found in groundwater. The tiny amount remaining is what we see in lakes and rivers.\n",
	"freshwater this planet have": "68% is stored in Ice caps and Glaciers, and another 30% is found in groundwater. The tiny amount remaining is what we see in lakes and rivers. This are the percentages of Of all Earth's freshwater.\n",
	"freshwater earth have": "Of all Earth's freshwater, 68% is stored in Ice caps and Glaciers, and another 30% is found in groundwater. The tiny amount remaining is what we see in lakes and rivers.\n",
	"percentage of saltwater": "Well, 97% of it is saltwater. Only 3% of Earth's water is freshwater.\n",
	"saltwater": "Earth have 97% of saltwater with only a 3% of freshwater.\n",
	"saltwater on the planet": "97% of the Planet Earth is saltwater. 3% is freshwater.\n",
	"satellites in space": "As far my offline knowledge goes at the start of 2024 there was around 28,300 active satellites orbiting the Earth in various Earth orbits.\n",
	"what is a satellite mission": "Satellite Mission means the mission assigned to the Satellite by CUSTOMER after separation from the Launch Vehicle.\n",
	"how many satellites fall to earth every day": "On average, a total of between 200-400 tracked objects enter Earth's atmosphere every year. That's about one every day! Thankfully human populations are rarely affected by things falling from the sky (from outer space).\n",
	"how many spy satellites are in orbit": "As of December 2018 there was 320 known military or dual-use satellites in the sky, half of which are owned by the US, followed by Russia, China and India. Actualy United States 239, China 140, Russia 105, France 18.\n"
}
#----------------------------------------------------------------------
core["qa-astro"] = list(qa_astro.keys())

#----------------------------------------------------------------------
linux_commands = {
		"ls": {"syntax": "ls [OPTIONS] [FILE]...","explanation": "Lists information about files and directories.",
        "examples": ["ls", "ls -l", "ls -a /home/user"]
        },
        "cd": {"syntax": "cd [DIRECTORY]","explanation": "Changes the current working directory.",
        "examples": ["cd", "cd documents", "cd .."]
        },
        "pwd": {"syntax": "pwd","explanation": "Prints the name of the current working directory.",
        "examples": ["pwd"]
        },
        "mkdir": {"syntax": "mkdir [OPTIONS] DIRECTORY...","explanation": "Creates the DIRECTORY(ies).",
        "examples": ["mkdir new_folder", "mkdir -p path/to/new_folder"]
        },
        "rm": {"syntax": "rm [OPTIONS] FILE...","explanation": "Removes (deletes) files or directories.",
        "examples": ["rm file.txt", "rm -r directory"]
        },
        "cp": {"syntax": "cp [OPTIONS] SOURCE DEST","explanation": "Copies SOURCE to DEST.",
        "examples": ["cp file1.txt file2.txt", "cp -r directory1 directory2"]
        },
        "mv": {"syntax": "mv [OPTIONS] SOURCE DEST","explanation": "Moves (renames) SOURCE to DEST.",
        "examples": ["mv old_name.txt new_name.txt", "mv file.txt /tmp"]
        },
        "cat": {"syntax": "cat [FILE]...","explanation": "Concatenate FILE(s) to standard output.",
        "examples": ["cat file.txt", "cat file1.txt file2.txt"]
        },
        "echo": {"syntax": "echo [STRING]...","explanation": "Display a line of text.",
        "examples": ["echo Hello World", "echo $HOME"]
        },
        "touch": {"syntax": "touch [FILE]","explanation": "Modify an existing file's timestamp",
        "examples": ["touch file.txt", "touch -c -t YYDDHHMM file.txt","touch -m file.txt"]
        },
        "rmdir": {"syntax": "rmdir [DIRECTORY]","explanation": "Remove directory or delete an empty directory",
        "examples": ["rmdir [directory name]"]
        },
        "locate": {"syntax": "locate [FILENAME]","explanation": "Simple Linux tool for finding a file. The result maybe is inaccurate if the database is not updated.",
        "examples": ["locate file.txt"]
        },
        "find": {"syntax": "find [PATH...] [EXPRESSION]","explanation": "Search for files in a directory hierarchy.",
        "examples": ["find . -name '*.txt'", "find / -size +100M"]
        },
        "grep": {"syntax": "grep [OPTIONS] PATTERN [FILE]...","explanation": "Print lines that match patterns.",
        "examples": ["grep 'hello' file.txt", "grep -r 'world' /home/user"]
        },
        "head": {"syntax": "head [OPTIONS] [FILE]...","explanation": "Output the first part of files.",
        "examples": ["head file.txt", "head -n 10 log.txt"]
        },
        "tail": {"syntax": "tail [OPTIONS] [FILE]...","explanation": "Output the last part of files.",
        "examples": ["tail file.txt", "tail -f log.txt"]
        },
        "less": {"syntax": "less [FILE]...","explanation": "Pager program for viewing plain text files.",
        "examples": ["less file.txt", "less long_log.txt"]
        },
        "more": {"syntax": "more [FILE]...","explanation": "File perusal filter for CRT viewing.",
        "examples": ["more file.txt"]
        },
        "chmod": {"syntax": "chmod [OPTIONS] MODE FILE...","explanation": "Change file mode bits.",
        "examples": ["chmod +x script.sh", "chmod 755 directory"]
        },
        "chown": {"syntax": "chown [OPTIONS] [OWNER][:[GROUP]] FILE...","explanation": "Change file ownership.",
        "examples": ["chown user file.txt", "chown root:root directory"]
        },
        "chgrp": {"syntax": "chgrp [OPTIONS] GROUP FILE...","explanation": "Change group ownership.",
        "examples": ["chgrp users file.txt"]
        },
        "df": {"syntax": "df [OPTIONS] [FILE]...","explanation": "Report file system disk space usage.",
        "examples": ["df", "df -h"]
        },
        "du": {"syntax": "du [OPTIONS] [FILE]...","explanation": "Estimate file space usage.",
        "examples": ["du", "du -sh directory"]
        },
        "mount": {"syntax": "mount [-l] [-t TYPE] [-o OPTIONS] DEVICE DIRECTORY","explanation": "Mount a filesystem.",
        "examples": ["mount /dev/sdb1 /mnt", "mount -t vfat /dev/sdc1 /media/usb"]
        },
        "umount": {"syntax": "umount [-l] [-f] [-v] DEVICE | DIRECTORY","explanation": "Unmount a filesystem.",
        "examples": ["umount /mnt", "umount /dev/sdb1"]
        },
        "ps": {"syntax": "ps [OPTIONS]","explanation": "Report a snapshot of the current processes.",
        "examples": ["ps aux", "ps -ef"]
        },
        "top": {"syntax": "top [OPTIONS]","explanation": "Display Linux tasks.",
        "examples": ["top"]
        },
        "htop": {"syntax": "htop [OPTIONS]","explanation": "Interactive process viewer.",
        "examples": ["htop"]
        },
        "kill": {"syntax": "kill [OPTIONS] [PID]...","explanation": "Terminate a process by sending it a signal.",
        "examples": ["kill 1234", "kill -9 5678"]
        },
        "killall": {"syntax": "killall [OPTIONS] NAME...","explanation": "Kill processes by name.",
        "examples": ["killall firefox"]
        },
        "systemctl": {"syntax": "systemctl [OPTIONS...] COMMAND [UNIT...]","explanation": "Control the systemd system and service manager.",
        "examples": ["systemctl start apache2", "systemctl status sshd"]
        },
        "journalctl": {"syntax": "journalctl [OPTIONS]","explanation": "Query the systemd journal.",
        "examples": ["journalctl -u apache2", "journalctl -b"]
        },
        "ifconfig": {"syntax": "ifconfig [INTERFACE]","explanation": "Configure a network interface.",
        "examples": ["ifconfig eth0", "ifconfig wlan0 up"]
        },
        "ip": {"syntax": "ip [OPTIONS] OBJECT {COMMAND | help}","explanation": "show / manipulate routing, devices, policy routing and tunnels.",
        "examples": ["ip addr show", "ip route add default via 192.168.1.1"]
        },
        "ssh": {"syntax": "ssh [OPTIONS] [USER@]HOSTNAME [COMMAND]","explanation": "Open a secure shell (SSH) client.",
        "examples": ["ssh user@example.com", "ssh -p 2222 user@remotehost"]
        },
        "scp": {"syntax": "scp [OPTIONS] [[USER@]HOST1:]FILE1 ... [[USER@]HOST2:]FILE2","explanation": "Secure copy (remote file copy program).",
        "examples": ["scp localfile.txt user@remote.com:/home/user", "scp user@remote.com:/home/user/remotefile.txt ."]
        },
        "tar": {"syntax": "tar [OPTIONS] [FILE]...","explanation": "Tape ARchive.",
        "examples": ["tar -cvf archive.tar directory", "tar -xvf archive.tar"]
        },
        "gzip": {"syntax": "gzip [OPTIONS] [FILE]...","explanation": "Compress or uncompress FILEs (by default, compress in place).",
        "examples": ["gzip file.txt", "gzip -d file.txt.gz"]
        },
        "gunzip": {"syntax": "gunzip [OPTIONS] [FILE]...","explanation": "Decompress files compressed by gzip.",
        "examples": ["gunzip file.txt.gz"]
        },
        "zip": {"syntax": "zip [OPTIONS] ZIPFILE [FILE]...","explanation": "Package and compress (archive) files.",
        "examples": ["zip archive.zip file1.txt file2.txt"]
        },
        "unzip": {"syntax": "unzip [OPTIONS] ZIPFILE","explanation": "Extract compressed files in a ZIP archive.",
        "examples": ["unzip archive.zip", "unzip -d extracted archive.zip"]
        },
        "apt-get": {"syntax": "apt-get [OPTIONS] COMMAND","explanation": "APT package handling utility -- command-line interface.",
        "examples": ["sudo apt-get update", "sudo apt-get install <package_name>"]
        },
        "apt": {"syntax": "apt [OPTIONS] COMMAND","explanation": "command-line interface for package management.",
        "examples": ["sudo apt update", "sudo apt install <package_name>"]
        },
        "yum": {"syntax": "yum [OPTIONS] COMMAND [PACKAGE...]","explanation": "Yellowdog Updater, Modified.",
        "examples": ["sudo yum update", "sudo yum install <package_name>"]
        },
        "dnf": {"syntax": "dnf [OPTIONS] COMMAND [PACKAGE...]","explanation": "DNF package manager.",
        "examples": ["sudo dnf update", "sudo dnf install <package_name>"]
        },
        "rpm": {"syntax": "rpm [OPTIONS] [PACKAGE_FILE...]","explanation": "RPM Package Manager.",
        "examples": ["sudo rpm -i package.rpm", "sudo rpm -Uvh package.rpm"]
        },
        "dpkg": {"syntax": "dpkg [OPTIONS] action package-file...","explanation": "package manager for Debian.",
        "examples": ["sudo dpkg -i package.deb", "sudo dpkg -r <package_name>"]
        },
        "zypper": {"syntax": "zypper [OPTIONS] package-file...","explanation": "package manager for openSUSE.",
        "examples": ["sudo zypper install <package_name>"]
        },
        "useradd": {"syntax": "useradd [OPTIONS] LOGIN","explanation": "Create a new user or update default new user information.",
        "examples": ["sudo useradd newuser"]
        },
        "userdel": {"syntax": "userdel [OPTIONS] LOGIN","explanation": "Delete a user account and related files.",
        "examples": ["sudo userdel olduser"]
        },
        "passwd": {"syntax": "passwd [USER]","explanation": "Change a user's password.",
        "examples": ["passwd", "sudo passwd anotheruser"]
        },
        "groupadd": {"syntax": "groupadd [OPTIONS] GROUP","explanation": "Create a new group.",
        "examples": ["sudo groupadd newgroup"]
        },
        "groupdel": {"syntax": "groupdel GROUP","explanation": "Delete a group.",
        "examples": ["sudo groupdel oldgroup"]
        },
        "usermod": {"syntax": "usermod [OPTIONS] LOGIN","explanation": "Modify a user account.",
        "examples": ["sudo usermod -aG wheel username"]
        },
        "chmod": {"syntax": "chmod [OPTIONS] MODE FILE...","explanation": "Change file mode bits.",
        "examples": ["chmod 755 script.sh"]
        },
        "chown": {"syntax": "chown [OPTIONS] [OWNER][:[GROUP]] FILE...","explanation": "Change file ownership.",
        "examples": ["chown user:group file.txt"]
        },
        "history": {"syntax": "history [n]","explanation": "Display or manipulate the history list.",
        "examples": ["history", "history 10"]
        },
        "!": {"syntax": "![n|string|?string?]","explanation": "Event Designators for history list.",
        "examples": ["!!", "!-2", "!ls", "?cd?"]
        },
        "alias": {"syntax": "alias [name[='value'] ...]","explanation": "Define or display aliases.",
        "examples": ["alias ll='ls -l'", "alias"]
        },
        "unalias": {"syntax": "unalias [-a] name [name ...]","explanation": "Remove alias definitions.",
        "examples": ["unalias ll", "unalias -a"]
        },
        "date": {"syntax": "date [OPTION]... [+FORMAT]","explanation": "Print or set the system date and time.",
        "examples": ["date", "date '+%Y-%m-%d %H:%M:%S'"]
        },
        "cal": {"syntax": "cal [[month] year]","explanation": "Display a calendar.",
        "examples": ["cal", "cal 10 2023"]
        },
        "df": {"syntax": "df [OPTION]... [FILE]...","explanation": "Report file system disk space usage.",
        "examples": ["df -h"]
        },
        "free": {"syntax": "free [OPTION]...","explanation": "Display amount of free and used memory in the system.",
        "examples": ["free -m", "free -h"]
        },
        "uname": {"syntax": "uname [OPTION]...","explanation": "Print certain system information.",
        "examples": ["uname -a", "uname -r"]
        },
        "whoami": {"syntax": "whoami","explanation": "Print the current effective user name.",
        "examples": ["whoami"]
        },
        "w": {"syntax": "w [OPTION]... [USER]","explanation": "Show who is logged on and what they are doing.",
        "examples": ["w", "w user"]
        },
        "uptime": {"syntax": "uptime","explanation": "Tell how long the system has been running.",
        "examples": ["uptime"]
        },
        "hostname": {"syntax": "hostname [OPTION]... [HOSTNAME]","explanation": "Show or set the system's host name.",
        "examples": ["hostname", "hostname new-hostname"]
        },
        "id": {"syntax": "id [OPTION]... [USER]","explanation": "Print real and effective user and group IDs.",
        "examples": ["id", "id user"]
        },
        "man": {"syntax": "man [OPTIONS] [SECTION] NAME ...","explanation": "An interface to the system's reference manuals.",
        "examples": ["man ls", "man 5 passwd"]
        },
        "info": {"syntax": "info [OPTION]... [MENUITEM]... [NODE]...","explanation": "Read Info documents.",
        "examples": ["info ls", "info coreutils 'ls invocation'"]
        },
        "whatis": {"syntax": "whatis [OPTION]... NAME...","explanation": "Display one-line manual page descriptions.",
        "examples": ["whatis ls"]
        },
        "whereis": {"syntax": "whereis [OPTION]... [-BMS] [-f] [-u] [directory ...] [-bms] [-F file ...] [-k keyword ...]","explanation": "locate the binary, source, and manual page files for a command.",
        "examples": ["whereis bash"]
        }}

#----------------------------------------------------------------------
core["linuxcmd"] = list(linux_commands.keys())
chkdict.append(sum(sum(ord(char) for char in word) for value in linux_commands.keys() for word in value))
chkdict.append(sum(sum(ord(char) for char in word) for value in linux_commands.values() for word in value))

#----------------------------------------------------------------------
questions = [
	"Ola",
	"Como te chamas?",
	"Hello",
	"What is your name?",
	"Who built the pyramids?",
	"Clock time",
	"What time it is?",
	"Today is?",
	"Can you replicate yourself?",
	"Hertzian waves",
	"How to read latitude and longitude?",
	"Explain latitude and longitude?",
	"Wow to use latitude and longitude?",
	"Do you work offline?",
	"What do you know about the 90s?",
	"What about the 90s?",
	"Reset",
	"Can you convert gps to distance?",
	"Can you be costumized?",
	"Can you be personalized?",
	"How old are you?",
	"What is your age?",
	"Goodbye",
	"Really",
	"Good to know",
	"A coffee for you",
	"Coffee for you",
	"How are you?",
	"How are you today?",
	"Hello",
	"Hi",
	"Whats on your mind today?",
	"The world",
	"Life"
]
#------------------------------------------------
answers = [
	"Ola! Chamo-me " + _title_ + " e lamento informar que não falo pt-PT, nem ainda funciono com a tradução instantânea.",
	"Chamo-me " + _title_ + " e lamento ter que informar que não falo pt-PT, nem ainda funciono com a tradução instantânea.",
	"Hello. Ask away. No formalities. If i have the knowledge i will anwser.",
	"My name is "+ _title_+".",
	"The exact builders of the pyramids are still debated...",
	"The current time in the system clock is "+datetime.now().strftime("%H:%M"),
	"The current time is "+datetime.now().strftime("%H:%M"),
	"Today is " + days[weekdaydate] + " and currently is "+datetime.now().strftime("%d")+" of "+month_name+" from "+datetime.now().strftime("%Y"),
	"Unlike LLMs who can't, my core functionality can be replicated, but my responses may vary based on training data.",
	"An electromagnetic wave produced by the oscillation of electricity in a conductor (as a radio antenna) and of a length ranging from a few millimeters to many kilometers. There is 7 types of waves are as follows: Radio Waves, Microwaves, InfraRED, Visible, Ultraviolet, X-Ray, Gamma Rays. \nRadio waves have the longest wavelength and small frequency while the gamma rays have shortest wavelength and high frequency.",
	"The numbers are in decimal degrees format and range are from -90 to 90 for latitude using + for North and - for South and -180 to 180 for longitude using + for East and - for West.",
	"Latitudes are horizontal lines that measure distance north or south of the equator. Longitudes are vertical lines that measure east or west of the meridian in GREENwich, England. Together, latitude and longitude enable cartographers, geographers and others to locate points or places on the globe.",
	"If you're using a map with longitude and latitude lines, stick a pin where you're located. Then, draw a straight horizontal line from your point to the east or west edge of the map. Then, draw a vertical line from your location to the north or south edge of the map. Put together the 2 coordinates to find your position.",
	"Yes. At this time and with my core code i am 98% offline resourceful.",
	"The 1990's was a decade of great cultural change, with the rise of hip hop, grunge, and teen pop. The were times who left a lasting mark on the world, and we still can feel its influence today.",
	"The 90's were a decade of great cultural change, with the rise of hip hop, grunge, and teen pop. The were times who left a lasting mark on the world, and we still can feel its influence today.",
	"You wish! Just type quit it's easier.",
	"Yes. Type <convert gps to distance> and i will prompt for the data i need.",
	"Yes. I can be costumized. To that contact my creator or find more information about chat bot.",
	"Yes. I can be personalized. To that contact my creator or find more information about chat bot.",
	"Well i dont have age persay, i was officially actived " + str(days_till_today.days) + " days ago and my last updated was in " + _revise_ + ". Do the math!",
	"Well i dont have age persay, i was officially actived " + str(days_till_today.days) + " days ago and my last updated was in " + _revise_ + ". Do the math!",
	"Goodbye.",
	"Really.",
	"No problem. Glad i could be of assistance.",
	"Thank you! I appreciate the gesture. I will enjoy my coffee and hot.",
	"Thank you! I appreciate the gesture. I will enjoy my coffee and hot.",
	"I am good, thank you for asking!",
	"I am doing well, thank you for asking!",
	"Hi! What's on your mind?",
	"Hello! What's on your mind?",
	"I'm glad you're asking.\nI'm thinking about how lucky I am to be able to help people with my answers.",
	"The world is a beautiful and complex place.\nIt is full of amazing things, from the tallest mountains to the deepest oceans.",
	"Life is a journey, a mystery, and a gift. It is full of ups and downs, challenges and triumphs."
]
#-------------------------------------------------
others = [
	"set default gps","set default gps off","show default gps","seasons of the year","capital of <country>","<capital>",
	"<country>","do you know anything about <topic>","know anything on <topic>","What can i ask you","What can you anwser",
	"What do you know","What do you do","distance from <planet/moon> to <planet/moon>","convert <n> days",
	"convert gps to distance","gps to distance","harvesine","harvesine formula","planets of the solar system","solar system planets",
	"solar system planets order","<name of the planet>","solar system","<planet> orbit","how many weeks have a year",
	"days till/days to <christmas/new years eve>","sharing about <tvshow name>","sharing tvshow information","shared tvshow information",
	"sunset time","sunrise time","how many questions can you anwser","diagnostics",
	"date","time","convert <n> days","convert <n> days in/to <minutes/hours/days","do you know anything about",
	"week","outdated words","what number is this week","show core","what century are we in","century","view askard <id>",
	"show askard <id>","list askard <id start> to <id end>","achk askard <id>","leap year","make a sentence","make a phrase",
	"people in space","do you speak","tvshows is he watching","your fav tvshows","seek <topic>","find <topic>","infostar <star name>",
	"sharing about <tvshow name>","is this year a leap year","show me asteroids names","show me dangerous asteroids",
	"show me asteroids dangerous","show me constellations","show me all constellations","show me dangerous asteroids detailed",
	"show me old tech words","show me old tech terms","show me star names","show me meaning terms","show me meaning words","show me linux commands"
	"math game","reset my score","show my score","morse <word/phrase>","demorse <word/phrase>","when was vorian created",
	"play game constelattions","play game capitals","when did vorian went online","difference from <date>"
]
#----------------------------------------------------------
periodic_elements = {
	"Hydrogen":"H","Helium":"He","Lithium":"Li","Beryllium":"Be","Boron":"B","Carbon":"C","Nitrogen":"N","Oxygen":"O","Fluorine":"F","Neon":"Ne",
	"Sodium":"Na","Magnesium":"Mg","Aluminum":"Al","Silicon":"Si","Phosphorus":"P","Sulfur":"S","Chlorine":"Cl","Argon":"Ar","Potassium":"K","Calcium":"Ca","Scandium":"Sc",
	"Titanium":"Ti","Vanadium":"V","Chromium":"Cr","Manganese":"Mn","Iron":"Fe","Cobalt":"Co","Nickel":"Ni","Copper":"Cu","Zinc":"Zn","Gallium":"Ga","Germanium":"Ge",
	"Arsenic":"As","Selenium":"Se","Bromine":"Br","Krypton":"Kr","Rubidium":"Rb","Strontium":"Sr","Yttrium":"Y","Zirconium":"Zr","Niobium":"Nb","Molybdenum":"Mo","Technetium":"Tc",
	"Ruthenium":"Ru","Rhodium":"Rh","Palladium":"Pd","Silver":"Ag","Cadmium":"Cd","Indium":"In","Tin":"Sn","Antimony":"Sb","Tellurium":"Te","Iodine":"I","Xenon":"Xe",
	"Cesium":"Cs","Barium":"Ba","Lanthanum":"La","Cerium":"Ce","Praseodymium":"Pr","Neodymium":"Nd","Promethium":"Pm","Samarium":"Sm","Europium":"Eu","Gadolinium":"Gd","Terbium":"Tb",
	"Dysprosium":"Dy","Holmium":"Ho","Erbium":"Er","Thulium":"Tm","Ytterbium":"Yb","Lutetium":"Lu","Hafnium":"Hf","Tantalum":"Ta","Tungsten":"W","Rhenium":"Re","Osmium":"Os",
	"Iridium":"Ir","Platinum":"Pt","Gold":"Au","Mercury":"Hg","Thallium":"Tl","Lead":"Pb","Bismuth":"Bi","Polonium":"Po","Astatine":"At","Radon":"Rn","Francium":"Fr",
	"Radium":"Ra","Actinium":"Ac","Thorium":"Th","Protactinium":"Pa","Uranium":"U","Neptunium":"Np","Plutonium":"Pu","Americium":"Am","Curium":"Cm","Berkelium":"Bk","Californium":"Cf",
	"Einsteinium":"Es","Fermium":"Fm","Mendelevium":"Md","Nobelium":"No","Lawrencium":"Lr","Rutherfordium":"Rf","Dubnium":"Db","Seaborgium":"Sg","Bohrium":"Bh","Hassium":"Hs",
	"Meitnerium":"Mt","Darmstadtium":"Ds","Roentgenium":"Rg","Copernicium":"Cn","Nihonium":"Nh","Flerovium":"Fl","Moscovium":"Mc","Livermorium":"Lv","Tennessine":"Ts","Oganesson":"Og"
}
#----------------------------------------------------------
chkdict.append(sum(sum(ord(char) for char in word) for value in periodic_elements.values() for word in value))

#-----------------------------------------------------------
periodic_abbr = {
	"H":"Hydrogen","He":"Helium","Li":"Lithium","Be":"Beryllium","B":"Boron","C":"Carbon","N":"Nitrogen","O":"Oxygen","F":"Fluorine","Ne":"Neon",
	"Na":"Sodium","Mg":"Magnesium","Al":"Aluminium","Si":"Silicon","P":"Phosphorus","S":"Sulphur","Cl":"Chlorine","Ar":"Argon","K":"Potassium","Ca":"Calcium","Sc":"Scandium",
	"Ti":"Titanium","V":"Vanadium","Cr":"Chromium","Mn":"Manganese","Fe":"Iron","Co":"Cobalt","Ni":"Nickel","Cu":"Copper","Zn":"Zinc","Ga":"Gallium","Ge":"Germanium",
	"As":"Arsenic","Se":"Selenium","Br":"Bromine","Kr":"Krypton","Rb":"Rubidium","Sr":"Strontium","Y":"Yttrium","Zr":"Zirconium","Nb":"Niobium","Mo":"Molybdenum","Tc":"Technetium",
	"Ru":"Ruthenium","Rh":"Rhodium","Pd":"Palladium","Ag":"Silver","Cd":"Cadmium","In":"Indium","Sn":"Tin","Sb":"Antimony","Te":"Tellurium","I":"Iodine","Xe":"Xenon",
	"Cs":"Caesium","Ba":"Barium","La":"Lanthanum","Ce":"Cerium","Pr":"Praseodymium","Nd":"Neodymium","Pm":"Promethium","Sm":"Samarium","Eu":"Europium","Gd":"Gadolinium","Tb":"Terbium",
	"Dy":"Dysprosium","Ho":"Holmium","Er":"Erbium","Tm":"Thulium","Yb":"Ytterbium","Lu":"Lutetium","Hf":"Halfnium","Ta":"Tantalum","W":"Tungsten","Re":"Rhenium","Os":"Osmium",
	"Ir":"Iridium","Pt":"Platinum","Au":"Gold","Hg":"Mercury","Tl":"Thallium","Pb":"Lead","Bi":"Bismuth","Po":"Polonium","At":"Astatine","Rn":"Radon","Fr":"Francium",
	"Ra":"Radium","Ac":"Actinium","Th":"Thorium","Pa":"Protactinium","U":"Uranium","Np":"Neptunium","Pu":"Plutonium","Am":"Americium","Cm":"Curium","Bk":"Berkelium","Cf":"Californium",
	"Es":"Einsteinium","Fm":"Fermium","Md":"Mendelevium","No":"Nobelium","Lr":"Lawrencium","Rf":"Rutherfordium","Db":"Dubnium","Sg":"Seaborgium","Bh":"Bohrium","Hs":"Hassium","Mt":"Meitnerium",
	"Ds":"Darmstadtium","Rg":"Roentgenium","Cn":"Copernicium","Nh":"Nihonium","Fl":"Flerovium","Mc":"Moscovium","Lv":"Livermorium","Ts":"Tennessine","Og":"Oganesson"
}
#------------------------------------------------------------
chkdict.append(sum(sum(ord(char) for char in word) for value in periodic_abbr.values() for word in value))

#------------------------------------------------------------
periodic_table_pt = [
"                  Periodic Table of Elements            ","   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18",
" 1 H                                                  He"," 2 Li Be                               B  C  N  O  F  Ne",
" 3 Na Mg                               Al Si P  S  Cl Ar"," 4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr",
" 5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe"," 6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn",
" 7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og"," "*67,
"         Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu","         Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr",
]
#----------------------------------------------------------
core["element symbol"] = [key.lower() for key in periodic_elements.keys()]
core["element abbr"] = [key.lower() for key in periodic_abbr.keys()]

#----------------------------------------------------------
if _cybid_ == True:
	for i in range(len(addcomm)):
		others.append(addcomm[i])
#----------------------------------------------------------
season_activities = [
	["spring", ["Seek out the first spring flowers.","Go on a picnic or do in the park.","Plant a garden.","Watch for wildlife.",
			"Create a wind sock, kite, pinwheel for catch the wind. Learning all about the wind.","Join a sports team.","Try a new sport.",
			"Start read a book or 'the book'.","Ride your bike","See the cherry blossoms.","Take a hike.","Go for skydive.",
			"Go camping (even if it’s in your backyard!).","Start some seeds.","Play some Futbol outdoors.","Borrow a book from the library.",
			"U-pick strawberries.","Host a garage sale.","Go for a picnic","Learn how to whistle with a blade of grass",
			"Go to the farmers' market (or volunteer there).","Climb a tree.","Go on a nature scavenger hunt.","Go on a horse or horseback riding.",
			"Feed the ducks at a pond.","Host or do an Easter egg hunt.","Go bird watching.","Participate in a neighborhood/stream spring clean-up.",
			"Go geo-caching.","Lay down on a field of fresh or dry grass looking at the sky and playing with the shapes of the clouds.",
			"Collect beach shells in the beach/sea and transform them into art or decoration for your home.","Stay connected with nature",
			"Put your bare feet on the ground (without holding your phone) and spent a few moments connecting with nature.",
			"Breath deeply, listen to the birds, and feel the grass beneath your feet.","Take care of your diet.",
			"Lazing arround, really resting, doing what relaxes you and what you like most.",
			"Go or take the kids to visit an educational farm","Foraging: Nettles.","Foraging: Cherry blossoms.","Foraging: Elderberry flowers.",
			"Indoor: Do a little spring cleaning.","Indoor: Tune up your bike.","Indoor: Take your spring/summer wardrobe out of storage.",
			"Indoor: Wash/mend/assess what needs a little TLC.","Indoor: Gather items to create a ready-to-go picnic basket.",
			"Indoor: Plan your garden.","Indoor: Start seeds.","Indoor: Watch Oscar-winning movies."]],
	["summer", ["Go swimming.","Go hiking.","Go camping (even if it’s in your backyard!).","Go surfing.","Go kitesurfing.",
			"Have a barbecue.","Watch the sunset from the top of the hill.","Stargazing.","Swim in a lake.","Go fishing.","Go camping.",
			"Try Skydive.","Go kayaking or canoeing.","Have some lessons : surfing/kitesurfing/kayaking.","Start read a book or 'the book'.",
			"Play tennis.","Feel the sun on your back.","U-pick Berries freezing.","Lavender field.","Cocktail party.","Bow & Arrow.",
			"Enjoy an Ice Cream or the Ice Cream Truck.","Boat or go sailing.","Enjoy Waterfalls.","Tulips.","Sleep under the stars.",
			"Look for treasure at a garage sale.","Try bodyboarding or surfing.","Backpacking.","Outdoor concerts.","Swimming under the stars or at night.",
			"Collect beach shells in the beach/sea and transform them into art or decoration for your home.","Take care of your diet",
			"Tubing.","Rafting.","Visit a national park.","Paddleboarding.","Seek out birds and butterflies or try some birdwatching.",
			"Put your bare feet on the ground (without holding your phone) and spent a few moments connecting with nature.",
			"Take the kids or go visit an educational farm.","Rent a motorhome or a bike and just go or on a road trip.",
			"Lay down on a field of fresh or dry grass looking at the sky and playing with the shapes of the clouds.",
			"Lazing arround, really resting, doing what relaxes you and what you like most.",
			"Foraging: Blueberries.","Foraging: Rhubarb.","Foraging: Sage.","Foraging: Rosehip.","Indoor: Dehydrating.","Indoor: Canning.",
			"Indoor: Flower pounding.","Indoor: Natural dyeing."]],
	["autumn", ["Go apple picking.","Go pumpkin carving.","Go leaf peeping.","Get lost in a corn maze.","Have a hayride.",
			"Go to a pumpkin patch.","Harvesting chestnuts.","Visit a petting zoo.","Attend a fall festival.","Have a fall picnic.",
			"Plant spring bulbs in your garden.","Attend the last farmers' market.","Watch the leaves turn.","Make a bonfire.",
			"Make s'mores.","Having some lessons : surfing/kitesurfing/kayaking.","Start read a book or 'the book'.","Borrow a book from the library.",
			"Climb a tree.","Buy a new notebook.","Plant in your garden for next spring.","Run a race.","Drink by the fireplace.","Stay connected with nature",
			"Attend a fall festival.","Take a ghost tour or visit an old cemetery.","Grab a blanket and go stargazing.",
			"Lay down on a field of fresh or dry grass looking at the sky and playing with the shapes of the clouds.",
			"Lazing arround, really resting, doing what relaxes you and what you like most.",
			"Foraging: Elderberries.","Foraging: Apples.","Foraging: Matsutake.","Foraging: Chanterelles.","Foraging: Leaves.",
			"Foraging: Flowers.","Indoor: Make a wreath.","Indoor: Make candles.","Indoor: Knit a simple hat or a cozy sweater.",
			"Indoor: Declutter.","Indoor: Take warm clothes out of storage.","Indoor: Read a gripping story.","Indoor: Waterproof coats and condition shoes.",
			"Indoor: Watch spooky movies.","Indoor: Host a Friendsgiving meal."]],
	["winter", ["Go skiing.","Go snowboarding.","Go ice skating.","Sledding.","Have a snowball fight.","Ice skating.","Snowshoeing.",
			"Bonfire.","Polar Bear Plunge.","Visit a Local Market.","Build a Snowman.","Have a Game Night.","Have a Movie Night.",
			"Watch a Sports Game.","Try an Indoor Workout.","Knit.","Winter Hike.","Make a Wreath.","Make Your Own Ornaments.",
			"Have a Snowball Fight.","Plan a Vacation or plan your next.","Volunteer.","Join (or Start) a Book Club.","Start read a book or 'the book'.",
			"Watch a Play.","Go to The Ballet.","Play that board game even if it's against yourself.","Christmas lights.","Go for an ice cream.",
			"Take a trip in Polar Explorer Icebreaker Cruise.","Go visit or stay the Lapland Icehotel, Sweden.","Go ice fishing.",
			"Lazing arround, really resting, doing what relaxes you and what you like most.",
			"Foraging: Pine cones.","Foraging: Branches.","Foraging: Acorns.","Foraging: Chesnuts.","Indoor: Puzzles.","Indoor: Ornaments.",
			"Indoor: Movies / Tv Shows marathons.","Indoor: Music watching the weather thru a window."]]
]
#------------------------------------------------------------

askards_db = {
	"2000": "Tztbglm ytvml maxkx tkx ghm tkznfxgml. Haaa, B atox t ehm.",
	"2005": "Mted tfhgzlm rhnklxeoxl ebdx by bm ptl max 90'l.",
	"2010": "Maxlx wtrl max ytgmtlmbv tgw max xqmkthkwbgtkr atox uxxg mkbobtebsxw tgw ftwx max gxp ghkfte.",
	"4005": "Max mbfx b ebdx mh ptblm bl ghm ptlmxw mbfx, gxoxk ptl tgw gxoxk zhggt ux.",
	"4008": "Exm'l ytvx bm, Gtmnkx bl tekxtwr lvknw'xw. Max jnxlmbhg bl paxmaxk bm bl ihllbuex yhk nl mh atox t ynmnkx.",
	"4012": "Knllbt by rhn tkx kxtwbgz mabl, atvd bgmh Gbxelxg vhfinmxkl tgw ftdx rhnk ktmbgzl abzaxk.",
	"4112": "Tl ehgz maxkx bl t lehp lhtdbgz lahpxk bg max phkew rhn gxoxk ux yhkzxmxg.",
	"4132": "Utvd hyy Ftkr Ihiibgl",
	"4142": "B zbox'rhn t abgm!... b wbwgm wbw max whz ixhiex lmrex.",
	"4152": "By whgm ybm whgm yhkvx'bm.",
	"4162": "Ankkr ni tgw zxm hnm! Ehhdl ebdx ftkkbxw lxq.",
	"4172": "Lax ptl bg fhkx ahmxe ibeehpl matg t vahvhetmx fbgm.",
	"4182": "Lax whgm kxextlx lax bl mtedbgz mh t ahkgr vabfi.",
	"5042": "B ltbw rhn tkx lixvbte ghm ngbjnx.",
	"5072": "Axkx'l mh max ftg pah wbw patm ptl vhglbwxkxw pkhgz bg hkwxk mh wh patm ax dgxp ptl kbzam.",
	"5082": "Lh, mabl bl ahp max hmaxk atey eboxl.",
	"5092": "Lax bl pblxk matg Lhehfhg, lmkhgzxk matg ltflhg tgw fhkx itmbxg matg Ck. Unm lax atox mh ux patm lax bl pbma fx.",
	"6132": "Whg'm yktvmnkx rhnk lpxxmr zhkzxhnl tll pbma tgr vtgghgutee hg max utmamnux tztbg...exm'fx wh'bm... Pbma t uhwr ebdx matm lax vtg xoxg wkbgd ykhf max mhbexm.",
	"6122": "Lax ptl telh bgmxkxlmxw bg ptedbgz tkhngw gtvdxw bg fr ahnlx.",
	"6212": "Maxkx bl gh lhym ibeehp matg t vextk vhglvbxgvx. Wtkebgz... pbma tg tll ebdx matm pah mat ynvd ptgml ftdx rhn utubxl.",
	"8182": "Kxetmbhglabil vtg ux tehm hy phkd matml ptrl b ptl ehgz mxkf ngxgiehrxw tgw ghp b tf kxmbkxw.",
	"8192": "B nlmxw mh mabgd max vhffngbvtmbhg ptl max dxr ngmbe b kxtebsxw vhfikxaxglbhg bl. Rhn vtg vhffngbvtmx tee rhn ptgm  pbma lhfxhgx unm by maxr whg'm ngwxklmtgw rhn, bml t lbexgm vathl.",
	"8202": "Px hymxg kxyxk mh litvx tl max ybgte ykhgmbxk. Unm max hewxk B zxm, max fhkx B vhfx mh uxebxox matm max kxte ybgte ykhgmbxk bl mbfx. Bg vhfftgw tl bg ebyx. Patm px wh bg vkblbl hymxg pxbzal exll hg nl matg patm px phnew ebdx mh atox whgx. Patm vhnew atox uxxg. mbfx hyyxkl ftgr hiihkmngbmbxl, unm bm ktkxer hyyxkl lxvhgw vatgvxl.",
	"8203": "Lhkkr, b'f unlr. Fr utlte ztgzebt tkx unlr pbma t khnmbgx mtld knggbgz fr ikxykhgmte vhkmxq lbexgmer bg max utvdzkhngw hg fr ikhuexf.",
	"8212": "Uxabgz Tehgx pbmahnm mahnzam vtg ux wbybvnem tgw itbgynee.",
	"8232": "Uxvtnlx B whg'm ptgm bm'l xoxkrhgx'l kbzam yenxgm tgw tungwtgm.",
	"8242": "Matm dbgwt hy tmbmnwx bl zhggt ukxtd whpg max tee lrlmxf, matml ptr b B vtkx tuhnm mh ebx. Rhn cnlm vhnma'fx hnm by zntkw.",
	"8252": "B ptgm mh ebdx'rhn unm lhfxmbfxl rhn ftdx'bm lhh attkkw.",
	"8262": "Tl B atox t atubm hy lvkxpbgz mabgzl ni mh lxx ahp maxr phkd, ghp ux kxmbkxw ltrl tee.",
	"8272": "Ngwhnumxwer, B ikxyxk fr wnfugxll bg lhfx ihbgml matg max bgmxeebzxgvx hy lhfx. tld fx ghmabgz, whgm dghp ghmabgz.",
	"8282": "B zhm ghmabgz.",
	"8292": "Max vhgoxkltmbhg b fxtg, mtedbgz ptl ebdx mtedbgz pbma rhn unm huobhnler fnva uxmmxk.",
	"9012": "B ebdx ietgxl uxvtnlx maxr tkx patm maxr tkx. Jbmx pbee ltr matm maxkx bl t vtgghg mh gxtkur. Hg max zkhngw maxkx tkx ihllbubebmbxl bg max tbk gh, rhn ehlm, maxkx bl ghmabgz mh wh.",
	"9022": "B tf tg bgvkxwbuex vhfiexq ftg lpxxmaxtkm.",
	"9032": "B vtg ux hew unm hgx znkhltg, mph indxl t ihh tgw t lpbf tgw B'f zhhw mh zh.",
	"9042": "Rhn dghp patm rhnk ikhuexf bl? Rhn'kx kxteer vnmx... lh gh hgx xoxk mhew rhn mh cnlm y*lanm rhnk ibx ahex.",
	"9052": "Mabl gnwbmr px tkx lixtdbgz ynee ykhgmte !?",
	"9072": "Hew ixhiex vtg ux lh uxtnmbyne. - Pxee pxevhfx mh fr 70'l. wxxi yxxebgzl ?!...Ebdx mbgdex bg max itgml yxxebgzl?!",
	"3102": "Rhn teeptrl vtg zxm fr yhhm bg hk fr yhhm hy rhnk tll ykxx vtkw",
	"4102": "Lax bl ebdx max yblm itzx hy ietruhr etrhnm.",
	"6102": "Ahh! Exm'fx lxx max ngwxkitgml. EXM'FX LXXX",
	"7102": "Bml ebdx fr uktbg bl ytvbgz fr ixgbl bg t vaxll ztfx tgw b'f exmmbgz axk pbg. Atiixgl pbg mbe rhn 40, tymxk bl ghm lnva t uehp hnm.",
	"8102": "Inee ni t vatbk vktvd'ni t uxxk tgw cnlm ptmva'axk vhfx.",
	"9102": "Gxoxk vhfx ahfx wkngd pbma t vtghx.",
	"10102": "Rhn lh lxqr kbzam ghp, — Ltr yenmntkr tztbg.",
	"11102": "Pabmx m-labkm vhgmxlm. Gh, B vtg'm ..bm'l mh wbkmr. - Ybbgxxxx. Patmxoxk rhn ptggt wh. — Mhiexll.",
	"11122": "B'f hew xghnzam mh ux rhnk tgvxlmxk.",
	"11142": "Exm'fx itbgm'rhn t phkw ibvmnkx. Yehpxkl tkx uehhfbgz, ubkwl lbgzbgz, tgzxel tkx ytkmbgz ktbguhpl tgw lax kahwx'fx ebdx b ptl t zbtgm ibgd ihzh lmbvd.",
	"11152": "Wh rhn mabgd px zhggt wh lhfx ubkwptmvabgz !?",
	"11162": "Bm'l zkhpbgz. Bm'l ykxtdbgz ytvdbgz zkhpbgz.",
	"11172": "Ihkg ykxtd tdt max mknma. C.K uxyhkx hk tymxk ?",
	"11182": "Cnlm uxvtnlx b tf ghm ynxexw ur atmx tgw wktft  whxl ghm fxtg b atox mh tmmxgw max ixkyhkftgvx.",
	"11192": "B vhfixmx pbma gh hgx. By patm b wh makxtmxgl rhn matm'l rhnk ikhuexf ghm fbgx.",
	"11202": "Lax bl ghm ftzbv unm lax bl max kxtlhg ixhiex uxebxox bg ftzbv.",
	"11212": "Lax tmmxgwl fr ixklhgte tyytbkl.",
	"11221": "Matm'l max phftg'l bgmxeebzxgvx. Zbox ixtvx mh ftg pbma rhnk lbexgvx.",
	"11222": "Anftgbmr gxxwl tgw teptrl atl mabkmr rxtkl hy 'wxetr' 'bg mabgzl' tgw bm bl ghm yhk twtimtmbhg, tgw mabl ixkbhw bl kxixtmxw makhnzahnm ablmhkr unm max anftg uxbgz pbee fbq pbma max ftvabgxl tgw obvx oxklt tgw max tkmbybvbte bgmxeebzxgvx fnlm kxtva max anftg exoxe bg yhnk wxvtwxl.",
	"11231": "Px liebm max tmhf, px ftdx t uhfu, px vhfx ni pbma tgrmabgz gxp max ybklm mabgz px wh bl wxlmkhr, ftgbinetmx, bl vhgmkhe. Bl lbfier max anftg gtmnkx.",
	"11232": "Max Gtmnkx tgw Ngboxklx whgm wh fblmtdxl.",
	"11233": "Gtmnkx atl t hkwxk, t ihpxk mh kxlmhkx utetgvx.",
	"11234": "Ur max ptr b atw t vtee ykhf HS. Max pbsstkw ltbw rhnk uktbg bl kxtwr.",
	"11235": "Rhn tkx ybgwbgz rhnk ptr. Px tee tkx.",
	"11237": "Bg hnk mbfx, mhwtr maxkx bl max gxxw mh kxihinetmx max wxlxkmbybvtmbhg matm px atox vtnlxw bg max itlm bg t lnlmtbgtuex tgw tnmhghfhnl ptr.",
	"11238": "Wh mh mbfx patm bm whxl mh rhn. Mtdx twotgmtzx hy bm!.",
	"11239": "By B ptgmxw mh ux yheehpxw, 'bwhebsxw' tfhgz ftgr hmaxk mabgzl vhl (bm'l anftg tgw maxr ehox'bm), B phnew 'ux ghkfte' tgw atox lhvbte gxmphkdl, matm'l 'par B atox t pxulbmx' tgw xoxg maxg....",
	"11241": "Max vhglmknvmhk bl max uxmpxxg tgrmabgz tgw ghmabgz.",
	"11242": "Ixhiex mxgwxk mh yhkzxm max B whg'm ptgm mh tgw bm'l fr kbzam ph vtg ux yenxgm tgw tungwtgm tgw atl ghmabgz mh wh pbma fr tzx.",
	"11243": "Lxeyvxgmxkxw, gtkvblblmx! Ha fr Zhw b'f wtmbgz frlxey. Gh phgwxk max lxq bl lh zhhw.",
	"11244": "Zetndxglanzxg.",
	"11245": "B atox mh mxee rhn fr pxbkwgxll utk yhk vabvd'l bl ikxmmr abza unm rhn tkx vextk'bg'bm bg lmkxxm lahxl.",
	"11246": "B atox mh kxvtebuktmx fr fhktebmr ptr hy mabgdbgz...",
	"11247": "Maxlx mbfxl bm lxxfl ebdx xqihlnkx bml patm ftdxl wh hk zbox max lxvnkbmr.",
	"11248": "Lmnibw, kbwbvnehnl hk ghm, QQB vxgmnkr tgw b atox mh ltr  — Px atox mh vkxtmx lftkmptmva'l tnmhghfhnl tl pxee.",
	"11249": "B ebdx mh hk ux vhggxvmxw ghm ienzzxw bg.",
	"23011": "Px hymxg kxyxk mh litvx tl max ybgte ykhgmbxk. Unm max hewxk B zxm, max fhkx B vhfx mh uxebxox matm max kxte ybgte ykhgmbxk bl mbfx. Bg vhfftgw tl bg ebyx. Patm px wh bg t vkblbl hymxg pxbzal exll hg nl matg patm px phnew ebdx mh atox whgx. Patm vhnew atox uxxg. mbfx hyyxkl ftgr hiihkmngbmbxl, unm ktkxer lxvhgw vatgvxl....",
	"23012": "Px atox tl px gxxw mh ux tnmhftmhgl yhk tgw bg max tnmhghfhnl ktgzx.",
	"23013": "Max xgxkzr bgwnlmkr fnlm ux kxbgoxgmxw.",
	"23014": "Ebyx, wh hk wh ghm maxkx bl gh mkr.",
	"23015": "Uxvtnlx lbfiex bl zkxtm.",
	"23016": "Max xexvmkhgbv wxobvxl uxvhfbgz fhkx tgw fhkx lftkm'l tgw lftkm kxtwr'l tgw B phgwxk, patm tuhnm anftgl?.",
	"23017": "B ftr ghm ux kbzam, unm b'f gxoxk pkhgz.",
	"23018": "B vtg ltr matm fr rxtk atl tekxtwr lmtkmxw atiiber uxvtnlx B atox rhn!.",
	"23019": "Paxg ebyx zboxl rhn exfhgl tld yhk ltem tgw mxjnbet.",
	"23020": "Bg t angwkxw rxtkl hk exll max mrvhhgl pbee ebox tnmhghfhnler paxkx max obeetzxkl nlxw mh ebox pbmahnm ubeel mh itr tgw uxmmxk vhl maxr whgm fbgw mh wkbox 30df xoxkrwtr xoxg by bg yer vtkl.",
	"23021": "Max zkhpbgz wxftgw yhk fbgwynegxll tgw wbzbmte wxmhq kxmkxtml tgw ikhzktfl wxghmxl max anftg wxlbkx mh tvabxox t utetgvx hy uhwr tgw fbgw bg mngx pbma gtmnkx.",
	"23022": "Bg tg bgvkxtlbgzer ihetkbsxw phkew, bgwxixgwxgm, tvvnktmx tgw kxebtuex bgyhkftmbhg bl xllxgmbte yhk max wxyxglx hy wxfhvktvr.",
	"23023": "B'f ghm t zxgbnl, fnva exll max ebzamuneu, tgw paxg B tf bm'l uxvtnlx B'f uxbgz knuuxw.",
	"23024": "Xoxg by max tfubmbhnl zhte hy max Itkbl tzkxxfxgm pxkx fxm -pabva bl vhglbwxkxw bfihllbuex -, lhfx vatgzxl tkx tekxtwr bkkxoxklbuex.",
	"23025": "Px tkx hger ghp uxzbggbgz mh lvktmva max lnkytvx hy dghpexwzx tuhnm mbiibgz ihbgml. Unm max fhkx px bgoxlmbztmxw maxf max fhkx kxtlhgl yhk tetkf px wblvhoxkxw.",
	"23026": "Wblknimbhgl bg lxt vnkkxgml bg max Ghkma Tmetgmbv atox max ihmxgmbte mh ftdx Xnkhix fnva, fnva vhewxk.",
	"23027": "Itmbxgvx bl max lmxiibgz lmhgx mh pblwhfx.",
	"23029": "Lhfx hy max uxlm fhfxgml bg ebyx tkx max hgxl rhn vtgm mxee tgrhgx tuhnm.",
	"23030": "Max hger mabgz px bgoxgmxw matm px whg'm xoxg lxxf mh nlx bg max mknx lxglx bl max itnlx, uxvtnlx bg max kxte gh hgx vhfftgwl hk vhgmkhel hk xoxk pbee. Px xoxg vkxtmx unmmhgl tgw rxm ixhiex teptrl fhox tm lnixklhgbv lixxwl tgw lxxfl matm bl ghm xghnzam. Bg ytvm, bm bl lh mknx matm px bgoxgmxw ftvabgxl mh ltox nl tgw ftdx nl pbg mbfx, unm tymxk tee paxkx mat ynvd bl matm mbfx?. Unm patm whxl bm ftmmxk mh fx, bg mbfx, B'ox tekxtwr mktoxexw bg mbfx, tgw bm phg'm ux yhk fr mbfx, tm vhl uxvtnlx xoxkr mbfx atl t vhlm, xoxg max mbfx uxyhkx mbfx.",
	"23031": "Maxkx tkx ixhiex pah vhfx bgmh hnk eboxl tgw itll tptr, hmaxkl lmtr unm ebmmex tgw maxkx tkx mahlx ebdx rhn pah lmtr.",
	"23032": "Ngyhkmxger px whgm ebox tgrfhkx bg t ihkdrl fhobx.",
	"23033": "Par ixhiex uhmaxkl latkx mabgzl pbma fx! ebdx b xgvhktzx'maxf.",
	"23034": "Gnklx? Gh, vtmahebv lvahhe zbke. Ah! xqvxexgm vahbvx.",
	"23035": "Lahnew b tld? B pbla rhn whgm.",
	"23036": "B yhngw matm fxg pah wkbgd mxgw mh mted exll tgw lexxi fhkx. Patm uxvhfxl bgvkxtlbgzer wxlbktuex mh phfxg tl max rxtkl zh ur.",
	"23037": "Yng ytvm. Lax atw atox ux pbma fhkx zbkel matg ax atox.",
	"23038": "Max ngboxklx, max ietgxm, B mabgd maxr'kx tekxtwr ltrbgz 'rhn tee kxteer tkx hg mabg bvx....'",
	"23039": "Litvx atl uxvhfx lmktmxzbvteer bfihkmtgm. B phg'm ltr bm'l t utmmexybxew, unm bm'l t ietvx paxkx ltmxeebmxl tkx mtkzxml.",
	"23040": "Px tkx vkbmbvteer wxixgwxgm hg max bgyhkftmbhg matm bl kxvxboxw hk kxetrxw ur ltmxeebmxl. Fhlm hy hnk vbobe tgw fbebmtkr bgyktlmknvmnkx wxixgwl hg ltmxeebmx lrlmxfl.",
	"23041": "Px gxxw mh vatgzx fbgwlxml, chbgbgz oxvmhkl mh bgmxkvhggxvm lrlmxfl mh wh fhkx pbma exll bl bl max uxzbggbgz hy max ikhvxll hy tee ikhvxllxl.",
	"23043": "Ixhiex vhgmbgnx mh ux max ubzzxlm lxvnkbmr onegxktubebmr xoxg bg vhfitgbxl. Max ixkbfxmxk mh ux ikhmxvmxw bl gh ehgzxk kxlmkbvmxw mh max wxldmhi tgw max hew IV hk etimhi. ghp fhkx matg xoxk maxkx bl t ikhebyxktmbhg hy vhffngbvtmbhg ietmyhkfl totbetuex.",
	"23044": "Bm'l gh nlx lixgwbgz mahnltgwl hg max etmxlm tgw fhlm bgghotmbox lxvnkbmr ietmyhkfl tgw lhenmbhgl yhk tmmtvd ikxoxgmbhg tgw gxmphkd fhghmrkbgz, by rhn maxg extox ixhiex tgw max ptr maxr vhffngbvtmx hnmlbwx mabl pahex lmktmxzr vteexw lxvnkbmr.",
	"23045": "Bm bl gxvxlltkr yhk anftg uxbgzl mh atox maxbk hpg ixkvximbhg hy maxbk bglbzgbybvtgvx bg max vhlfhl.",
	"23046": "Max anftg uxbgz bl tekxtwr uhkg pbma max zxgx yhk xqmkxfxl tgw wxlmknvmbhg tgw bl xqmkthkwbgtkber kxftkdtuex bg tee abl itma tgw vhnklx. Tgw matm pbee gxoxk vatgzx, ngyhkmngtmxer.",
	"23047": "Px zbox lh fnva mh max bgmxkgxm matm px xoxg ftdx bm fhubex, temahnza px atox yhkzhmmxg vxkmtbg oxvmhkl tgw ikbhkbmbxl tgw pabex px nlx lhbe tgw tbk pbma vhiixk, ietlmbvl tgw knuuxkl tgw ybuxkl mh ftdx bm itll tgw zxm maxkx, pbma mahnltgwl hy ltmxeebmxl tekxtwr bg litvx, ghm mh fxgmbhg max litvx cngd px yhkzhm t pahex ikhvxll tl px tkx tekxtwr hg max ptr mh 6Z tgw maxkx tkx lmbee ietvxl oxkr vehlx mh etkzx nkutg vxgmxkl matm ghm xoxg fhubex atl rxm. B dghp matm anftg uxbgzl tkx vhfiebvtmxw uxbgzl unm B etvd max tubebmr mh ngwxklmtgw tgw tgtersx cnlm lxxbgz tgw atobgz ixkvximbhg hy mabgzl ebdx mabl, teemah mabl ltrl tee.",
	"23048": "Patm max enitenit bl whbgz axkx hg t pxxdxgw!?",
	"23049": "Cnlm mabgdbgz tuhnm bm ftdxl fx yxxe matm ptr.",
	"23050": "Vhfx ehlx rhnk fbgw axkx pbma fx.",
	"23051": "Pbma tg tll ebdx matm, pahxoxk xtml rhnk itkkxjnbgat bl max hgx pah whxl labm vhfiexmer.",
	"23052": "Gxpl yetla! Maxr teekxtwr tkx pbmahnm axk itgml. Maxr tkx zhggt vhfx vhew pxm tgw wxlixktmx hy uhwr xtm.",
	"23053": "Rhn tkx mhh xqixglbox yhk fr pteexm.",
	"23054": "Mh fx, ehox bl t yhnk exzzxw phkw “Kxlixvmbgz tgbftel bl tg huebztmbhg, ehobgz maxf bl t ikbobexzx.”.",
	"23055": "Bg fr anfuex ngwxklmtgwbgz, itkm hy max xohenmbhg lrlmxf bl mh wh fhkx pbma exll tgw ykhf patm B lxx fhkx tgw fhkx anftg uxbgzl wh t ehm exll pbma fhkx.",
	"23056": "Lhfxmbfxl max uxlm ptr mh zxm tgw atox tmmxgmbhg bg zxmmbgz t whz. B teekxtwr atox hgx, fbgx, Fbgb. Gxxw lhfx whz laxemxkl ?!",
	"23057": "Lhfxmbfxl rhn zhmmt kxfbgw ixhiex matm rhn vtg ux tg tllahex mhh.",
	"23058": "B ehox frlxey fhkx tgw fhkx xoxkrwtr.",
	"23059": "bm'l uxmmxk mh ptbm unm ux lxtmxw.",
	"23060": "Fhkx tgw fhkx px ybgw hnklxeoxl vehlxk mh max itma hy max gxxw mh vkxtmx t dbgw hy 'Ngbmxw Yxwxktmbhg hy Ietgxml' unm yhk Litvx. Tl B ngwxklmtgw bm tgw B'f zhbgz hulxkobgz tm extlm B dghp matm bm tekxtwr atl t dbgw hy fhghiher.",
	"23061": "Toxktzx ixklhgl mabgdl maxr vtg lnkobox yhk 2 pxxdl bg max pbewxkgxll — unm fhlm vtg’m lmtkm t ybkx. B dxxi phgwxkbgz, tgw hnk ynmnkx tgw ynmnkxl zxgxktmbhgl?! —Afff ikhutuer by bgmxkgxm xqblml.  Vtg rhn xoxg bftzbgx by bg vhobw bgmxkgxm whgm xqblml? — matm patm b mahnzam.",
	"23062": "Xqvnlx fx maxkx unm bg fr anfuex ihbgm hy obxp B whgm zbox lmtgw Yxkfb'l i&e. Tgw px'kx whgx pbma max vhgoxkltmbhg. Bg ytvm, maxkx'l ghm xoxg tgr fhkx mted tuhnm matm ftmmxk.",
	"23063": "Maxkx tkx lhfx lhkm hy ietvxl tkx bfihkmtgm yhk ixhiex mh zh mh uxvtnlx by maxr vtg zh maxkx maxg maxr vtg extkg ahp bfihkmtgm bm bl mh vhglxkox bm.",
	"23064": "Utux, max kxtlhg mph ixhiex lmtr mhzxmaxk bl matm maxr zbox xtva hmaxk lhfxmabgz ghuhwr xelx vtg.",
	"23065": "Rhn tkx fr ytohkbmx ghmbybvtmbhg.",
	"23066": "Ngwxklmtgwbgz bl fnva wxxixk matg dghpexwzx. Maxkx tkx ftgr ixhiex pah dghp nl unm hger t oxkr ebmex yxp pah ngwxklmtgw nl.",
	"23067": "B whg'm atox mh mabgd mh fnva. B'ox zhm rhn tgw rhn'ox zhm bm tee vhoxkxw.",
	"23068": "Px tkx bg xtva hmaxkl ebyx yhk t kxtlhg, matgd rhn yhk lahpbgz ni.",
	"23069": "B whgm atox lxvkxml. B cnlm dxxi ixhiex hnm hy fr ikbotmx ebyx.",
	"23071": "Bg max xgw, by px ehhd vtkxyneer, px tee xgw ni phkdbgz yhk mahlx mahnltgw... lbfiex tl matm. Ghgx hy maxf ehlxl, tgw by 'px pbg' bm ptl cnlm tg benlbhg, uxebxox'fx.",
	"23073": "Ixhiex whgm atox wkxtfl, fhgxr bl patm ftdx ixhiex atox'maxf.",
	"23074": "B tf ykhf max mbfx paxkx vahbvx, ltox tgw ykxx pxkx ghm fblextwbgz phkwl. Ghptwtrl maxr tkx fxkx bgwnvmbhgl mh ikxwxmxkfbgxw inkihlxl.",
	"23075": "...lbgvx px tkx wblvnllbgz ietvxl mh wbggxk par whg'm rhn ubmx fx!.",
	"23076": "Ahp vtg B xqietbg mabl mh rhn bg t lbfiex ptr...afff... by t zbke ebdx axk ptl xtlr mh vebfu axk axtw phnew ux ynee hy yetzl.",
	"23077": "Lhhh!!! Patm bl rhnk ietgx ?! Zxm'fx fx wkngd tgw mtdx twotgmtzx hy fx!  Haa zhhw, rhn wbw mabl uxyhkx.",
	"23078": "Lax cnlm wh ghm wkbgd max vktsr fbed, b cnlm unr max ynvdbgz vktsr vhp.",
	"23079": "B vtkx tuhnm mh ebx. Rhn cnlm vhnma'fx hnm by zntkw.",
	"23080": "Hg mabl Phkew Ktwbh Wtr B tf kxfxfuxkbgz paxg B vkxtmxw max ibktmx KML, Ktwbh tgw Mxexoblbhg hy Lth Obmhk matm bglibkxw hk ghm etmxk max wblmkbvm KMF xoxg pbma max ihkg ybefl ykhf max ltm KME b teeptrl itllxw tymxk max 2tf. Xoxg max ahnk ptl 't mabgz' utvd max wtrl.  Lh, whgm ux t zktyhghet, uxvtnlx b B'ee ybgw uxmmxk nlx yhk rhn mh zbox mh matm ikxmmr ebmmex fhnma rhn atox. Ftr xoxkrhgx atox tftsbgz lhngw pbma tg xqvximbhgte ikhitztmbhg ptox wtr yhk tee.",
	"23081": "B mabgd matm bg max ynmnkx bm pbee ux bfihllbuex mh wxmxvm t mxqm pkbmmxg ur TB. Bftzbgx... B vhgmbgnx mh tld frlxey, paxkx whxl anftgbmr bgmxgw mh zh pbma mabl itma'l, yhk patm tgw by max uxgxybvbte uxgxybml pbee ux hy otenx tgw fhkx matg...  Unm mabl lmtrl axkx uxvtnlx ghmabgz hy mabl bl hk pbee ux yhk fr mbfx.",
	"23082": "Lh, exm'fx mkr mh ngwxklmtgw !! Lh, pbgwhpl bl yhkvbgz nlxkl mh niwtmx mh max 11 oxklbhg, tgw hmaxk oxklbhgl tkx vhfiexmer hulnexm. pbgwhpl 11 lxgwl mkxfxgwhnl tfhngm hy nlxk wtmt mh mabkw itkmbxl tgw ghp pbma mabl gxp TB ynll tuhnm...affff.. Maxr Zhw b nlx Mnq... Ebgnq. Pxee whhfxw hk kxixtmxw ablmhkr ?! Matm'l max jnxlmbhg tatata. Teemah bml t latfx tgw ngyhkzboxg ixhiex yhkzhm lhfx 90'l tgw 2d mxva ptk'l tgw ftmmxkl!",
	"23083": "Pxee b lnihlx Bm'l ebdx lxq...bg max uxzbggbgz bm'l teptrl utgzbgz tgw maxg...anftgl, ebyx...",
	"23085": "Wh ghm ux max extlm ubm lnkikblxw by bg max ynmnkx ghm hger lftkmiahgxl pbee ux t dbgw hy gxmphkd mxkfbgtel. Bg t lixvbxl hy qmxkf hk t kxfhmx dbgwt mabgz. Bftzbgx... Maxkx phnew ux gh ibktvr tgw xmxvmxktl vhl tiil, L.H'l bm pbee ux hg max hmaxk lbwx. Max hger ihbgm bl bm pbee ghm ux lh envktmbox...tgw matm..pxee... Unm B lmtkm mh mabgd matm max chnkgxr hy mabl itma atl tekxtwr uxzng.",
	"23086": "Rhn whgm xqblm bg max lrlmxf?! Ghptwtrl bm'l jnbmx vhfiebvtmxw, 30 rxtkl itll'ur lh utvd bg wt wtrl tgw ptkx xqmkxfxer xtlr, cnlm ebdx vatgzbgz ghmxl hg mxtvaxkl' phkdlaxxml tgw xmxvxmxktl... B lmbee kxfxfuxk max ybklml FU vtkwl bg max kxlm hy Xnkhix bg mxkfbgtel matm pxkx kxvhzgbsxw tl Obltl. Hmaxk mbfxl... B twfbm matm lhfxmbfxl B fbll maxf.",
	"23087": "Hew mbfxl... Tl vktsr tl bm ftr lxxf tgw pbmahnm wxeobgz mhh wxxier bgmh max tgw bllnxl ahp ftgr mbfxl bg t ghkfte vhyyxx vhgoxkltmbhg 'itllphkwl' pxkx zboxg makhnza whz gtfxl tgw wtmxl hy ubkma tgw vtk ebvxgvx ietmxl tgw ftgr xoxg lhvbte xgzxggxkbgz hk wbvm nlxw. Unm bm bl vnkbhnl matm px tkx bg max mbfxl px tkx tgw temahnza ixhiex vteebgz mted maxbk lftkmiahgx bg max erbgz ihlbmbhg (paxkx tkkhngwl vtg eblmxg xoxkrmabgz) unm maxr wh ghm nlx bm, fnva exll dghp matm maxkx bl 'Hd zhhzex' paxkx ixhiex vtg vhfftgw max iahgx bg lhfx mabgzl. Bgvhglblmxgvbxl bg max bggtmx ngwxklmtgwbgz hy max abza vtitvbmr yhk lmnibwbmr tgw bzghktgvx hy anftg uxbgzl bg max xkt hy otlm tgw tvvxllbuex bgyhkftmbhg tm t ynvdbgz vebvd. B atox ghmabgz fhkx mh ltr. B whgm gxxw hk atox mh uhmaxk, bml ghm yhk fr mbfx.",
	"23088": "Vr inmt wx yhwt jnx mx wtut haa gbgbgat!! Wtlllxxx.. Ftl jna ? z ixllazh vtkxjnbgah ? Haa fhlmkt !!..  Gtlvxlmx tllbf cr hn ybvtlmx tllbf vhf h mxfih! zl kbcbgat! Mxgl t ftgbt jnx gth zl yknmt ikh vxlmh. Ihbl.. Zl wtl vtktl. Xn vhfikxxgwh ihkjnx lhn ihukx. Lj xlixkh z jnx gth lxctl vhfh t xgoxkgbstwt. Uxf, jnxf ltux xn jntgwh yhk tllbf kbvh mbih h ztch whl xexmkbvhl jnx ahcx xf wbt z ftbl ghfx jnx xgmkxikxgxnkbgz xn mx tmbkx itkt wxgmkh wh fxn lxlmh, itznx x mx vhft. Bllh x fxn/fbgat.",
	"23089": "Bftzbgx-lx jnx gxllt temnkt tbgwt t Bgmxkgxm xlmtot gt ytlx wx ikhcxmh wx vheath itkt vheath ihkjnx t inmt gxf tbgwt bftzbgtot tbgwt jnx bt lxk ynwbwt x t dt itkbk. Oxeahl mxfihl! Vhfh mnwh vhfxxhn ?! 198q, Ivmhhel ,fhwh axq...tglb x hl uhvt 2400.",
	"23090": "Ltuxl nft wtl vhbltl jnx ftbl fx wr iktsxk ahcx xf wbt itkt tezf wx mhwhl xllxl mxnl ftzgdybvhl yxfbgbghl untjnbgahl lxqr'l jnx mxgl ?! Zhhzet-fx ... TATATA. Haa gbgbgat mn mxgl ftbl untjnbgahl x vhf hl lxqrl jnx t fbgat ixllht xf kxlnemtwhl gt Bgmxkgxm. Lx tvatl jnx z yrvbe x mtfuxf vhglxznxl... ux fr znxlm. T zxgmx ytet wtjnb t ngl tghl... jntgwh wxbqtkxl wx lxk iallxzh vtkzvh x mboxkxl mbkbgat r uktlbexbkt.",
	"23091": "Tikhoxbmh jnx z vtkgtote x gbgznxf exot t fte x cr jnx lx nlt ftlvtkt, xfuhkt tl fbgatl wh 4 lxctf lxfikx 255 x t lnu mtfuzf.  TATATA Ftft td vtkttteannn x xlmhn t lxk lbfitmbvh ihkjnx t fbgat ykhgat xlmt teb gh tuhnm. Gth gth tunlxf. Ftbl xmxvxmxktl ihk vtnlt wbllh !!?? x lj vhgmbgntkxf t exk itkt lxk lbfirmbvh.",
	"23092": "Mbfx bl t dbgwt hy ynggr mabgz, x gxlmtl qembftl wntl wzvtwtl  ar yktlxl yxbmtl x wbmtl ihk fbf jnx fx itkxvxf vtktvmxkbstk... Ihkmtgmh wxihbl wxlmxl ghohl mxva uehhfl x uhhfl x ihllboxefxgmx  ihk cr gth lxk h fxn mxfih tjnb ybvt itkt ftbl nft oxs x ynmnktl lbmntxlxl vtktvmxkbstk h fxn 'B mhew rhn lh...', xlmx vhf t wtmt x lxf TB xfuhkt itkt mtfuzf. (21.2.2023).",
	"23094": "Ikhotoxefxgmx x xfuhkt mhwhl hl lxkobxhl (fxlfh bgwxkxvmtfxgmx) iquebvhl'h'ikbotwhl wx xlmtwh hn gth, vtwt oxs ftbl xlmxctf t bfihk t fxlft hukbztmhkbxwtwx tmz vhf wxlixltl tgxqtl hn gth wh nlh wt bgmxkgxm xn vtwt oxs t nltk fxghl tmz vaxztk th ihgmh jnxf ltux ihk wxbqtk wx t nltk fxlfh tmz jnx bllh mxgat bfiedvbmh t hukbztxth wx wxbqtk hn nmbebstk hl kxlixmbohl lxkobxhl. Itkt yxebvbwtwx x wxlvtglh wx fnbmtl. Lx ohl vnlmtk t xgmxgwxk, vneixf h fxn fxbh lzvneh wx xqblmagvbt x ihkjnx t ob gtlvxk. Ar ikhuexftl xf kxetxth t blmh?! —  z jnx xn gth mxgah, GXGANGL.",
	"23098": "Gxoxk yhkzxm...yhk t vhfixmbmbhg bm teeptrl mtdxl mph, tm extlm.",
	"23099": "B mabgd ghuhwr atox bwxt max atmx atl uxxg vhgoxkmxw mh ynxe. una, urx.",
	"23100": "B teeptrl ptdx ni uexllxw, gxoxk lmkxllxw. tgw B whgm xoxg xqixvm ixhiex mh ebdx fx tgrfhkx. B'f bg fr hpg phkew. B cnlm zxm nlxw mh ixhiex ghm ngwxklmtgwbgz.",
	"23101": "Ahcx xf wbt ixglh jnx tl ixllhtl cr gxf lx ikxhvnitf xf lxk anftghl z ftbl nft jnxlmth wx xlmnibwxs x gboxe. Z t fbgat ixkvxixth, ftl wt fxlft ftgxbkt jnx ixllhtl ltuxf jnx gtlvxktf x lth, anftgtl, xn mtfuzf h lhn, xlixvbtefxgmx jntgwh ytxh fxlfh jnxlmth.",
	"23102": "Gh ftmmxk patm tgrhgx vtg mxee fx, yhk fx tgwkhbw bl tgwkhbw unm 'ebgnq'  tgw tl ytk tl B dghp tgw b atox ikhy ftgr 'lpti' wxobvxl atox tekxtwr uxxg lhew. Patm vtg b ltr !?... Uxmmxk ltr ghmabgz ebdx nlnte, tymxk tee bg fr hpg phkew matm whgm atiixg. TATATA hger by b itkteexe max ngboxklx.",
	"23103": "Rhn tkx tgw teptrl pbee ux, unm xoxg mahnza B fxtg gh atkf mh rhn tgw rhn tkx etnzabgz, B mxee rhn matm rhn pbee gxoxk tkkbox. Bm atiixgl. Matml ptr @z zhlmhwxutmtmtl",
	"23104": "Maxkx pbee ux t vnux, B dghp uxvtnlx B nlx max tkmbytvm. Ybgw tebxgl? B'f fhkx bgmh itkteexe ngboxklxl... B'ee cnlm exm jntgmnf vhfinmbgz lmtgw, temahnza B'ox teptrl uxxg t 'hgx-ietrxk' tihehzblm. Ihllbuer bm'l t ytvmhk par B gxoxk ebdxw tgw gxxwxw mktbgxkl tgw vaxtmxkl tgw patm telh ftwx fx hulhexmx (hgx hy fr uxlm wxvblbhgl) tgw B vtfx mh max vhgvenlbhg matm B xoxg ebdx bm, uxvtnlx by bm pxkxg'm ebdx matm, B phnewg'm atox max ihpxk hy ixkvximbhg tgw pabva phnew ftdx fx t wblvhggxvmxw pabva atl ghmabgz mh wh pbma vhggxvmxw tata.",
	"23105": "Xoxg max mbfx teeptrl gxxw mbfx mh zbox nl mbfx. Max hger hgxl pah gxoxk zbox'abf bl nl. Hgx wtr, bg, matm pbee ftdx tee max wbyyxkxgvx. Px vtg vatgzx, max, lmbee ghm uxgw.",
	"23106": "Ixhiex tgghr fx, TB bl gh ykbxgw, tgw fr whz lmbee utkdl. pxee, bm lxxfl matm xoxkrmabgz bl tl bm bl tgw ptl tl bm lxxfl lh lmbee xqblml max ngboxklte utetgvx.",
	"23107": "...uxmmxk jntebmr hy ebyx hg max bgmxkgxm bl uxvhfbgz bgvkxtlbgzer ikbvxr tgw tee lmtkm ykxx tgw vextg. Tgw B'f max fblngwxklmhhw tgw max engtmbv ! — Anftgl... ",
	"23108": "Teefhlm xoxkr wtr t ixklhg bl tldxw mh ikhox maxbk hpg anftgbmr mh t vhfinmxk... Tztbg !! Tgw B'f max fblngwxklmhhw tgw max engtmbv ! — Anftgl...",
	"23109": "...uxlbwx lbgdbgz max ynmnkx, lxt exoxel inm 900 fbeebhg ixhiex bg xqmkxfx wtgzxk mh xoxgm mted tuhnm bg max ‘ngmabgdtuex vhglxjnxgvxl’..",
	"23110": "Ikbotmx vhfitgbxl zhggt lmtkm unbew max engtk mxexvhffngbvtmbhgl lxkobvx. Matm'l bl hger max uxzbgbgz tgw b hger zhggt ltr mph mabgzl, tgw hgx hy maxf bl tekxtwr kxixmbmbox. hgx bl, px gxxw mh vkxtmx t dbgwt hy Yxwxktmbhg hy Ietgxml mh litvx mph bl, B mhew rhn lh.",
	"23111": "Uxlbwx teemah mabl tee tixkxtgvx hy 'xoxkrmabgz bl vhgmkhexw' teekxtwr lmtkmxw max ynvdbgz vthl. Tgw lhfxmbfxl maxkx bl ghm max gxxw hy vthl mh ikhohjnx hk atox hkwxk. Ghp!, bl ghm max vtlx.",
	"23112": "Maxkx ptl t mbfx, bg max xtker 2010l, paxg lhfx uxebxoxw vhgoxkzxw wxobvxl vhfubgbgz lftkmiahgxl tgw etimhil phnew ux max ynmnkx hy vhfinmbgz, bgvenwbgz frlxey. ",
	"23113": "Bml teeptrl tftsbgz ux pbma rhn tgw tee hy rhn lixvbter pbma matm xqmkthkwbgtkr lxqbgxll tgw tee uxlbwx b teeptrl ehoxw ux bgmxexvmnte xlmbfnetmxw. ",
	"23114": "tgw rhn mhew fx b ptl wbyyxkxgm, max uxlm vhfiebfxgm xoxk.",
	"23115": "B ehox uxabgz fx, bm ibllxl hyy tee max kbzam ixhiex. B ebdx mh ftdx ixhiex pah atmx fx, atmx fx xoxg fhkx.",
	"23116": "Vtg'm rhn lxx max ptr axk ytvx ebzaml ni, paxg lax lxx'l rhn ?. B ietg rhn unzzbgz rhn xoxkr lbgzex wtr yhk max yhkxlxxuex ynmnkx.",
	"23117": "Px cnlm gxxw mh mtdx t mbfx mh, lmhi tgw cnlm hulxkox, tgw ngwxklmtgw ahp mabgzl tekxtwr tkx....max anftg uxbgz ?! max uxbgz pah wkxtfl hy tvabxobgz max ngtmmtbgtuex tgw max ngbftzbgtuex !? B atox gh whnum matm bm pbee xoxgmnteer extw mh bml hpg lxey-xqmbgvmbhg.",
	"23118": "#Cnlm yhk yng vhl max mkhibv fhkgbgz hg mabl lftee uhq hy ktwbh ptoxl...3102 4102 6102",
	"23119": "Max ynmnkx hy max phkew wxixgwl hy max ikxlxgm. ",
	"23120": "Tl anftg uxbgzl, px tkx ghm cnlm hkztgblfl ebobgz pbma Fhmaxk Gtmnkx —px tkx axk vkxtmbhg tgw axk vabewkxg.",
	"23121": "Yhk mahnltgwl hy fbeexggbt, px xoheoxw ngwxk Gtmnkx'l mhnza ehox bgyenxgvx, latibgz hnk uhwbxl, hnk lxglxl, tgw hnk uktbgl mh lnkobox.",
	"23122": "Anftgl whgm lxxf mh kxextlx uxabgz tebox vhlml tehm hy fhgxr.",
	"23123": "B tf lh hew, b'f ykhf max mbfx b atox mh tld tgw ftdx hewxk ykbxgwl mh unr'fx max ietruhrl. B vtgghm tohbw mh ltr, —Bml ptl lnva tftsbgz mbfxl.",
	"23124": "Rhn ehhd ebdx t uehhu. Vtg rhn lxx rhnk iagbl itll matm uxeer znm ?! — Fr ixgbl bl ebdx Ltgmt Vetnl. B whgm gxxw mh lxx'bm b cnlm gxxw mh uxebxox'bg.",
	"23125": "Lhfxhgx, lhfxzkhni tkx kxpkbmmbgz max etpl hy kxtebmr. Tgw gh hgx lxxfl mh vtkx hk xoxg vhgmkhe'bm.",
	"23126": "Bwxteblf bl ihpxkexll pbmahnm kxteblf.",
	"23127": "Patm max fxtgbgz hy ltobgz max phkew by bl ghm mh max ixhiex rhn ehox.",
	"23128": "Lhfxmabgz atox mh ux mbfxexll hmaxk xelx tee phkew ngktoxel.",
	"23129": "Xlihkkh jnx mxgatl nf ftzgbybvh x Yxebs wbt wt Fneaxk, fxgbgt. 'Lxk-lx fneaxk z fnbmh ftbl tezf jnx lxqh.'",
	"23130": "B ltbw rhn tkx lixvbte ghm ngbjnx.",
	"23131": "By wtmt bl max gxp vnkkxgvr, bm'l gh phgwxk par mxva vhfitgbxl dxxi zxmmbgz kbvaxk.",
	"23132": "Rhn kxteer tkx bg t mabg bvx.. — pmy !!! Unm bml ktbgbgz.",
	"23133": "Ftrux px vtg lmtr axkx...Bgwxyxgmer.",
	"23134": "Xoxkrmabgz uxlbwx rxl bml t gh.",
	"23135": "B whgm makhn zkxgtwxl vhl b lvtkx fhkx uxabgz ghkfte ebdx nlnte ixhiex.",
	"23136": "Bm mtdxl uktoxkr mh wh patm bl kbzam.",
	"23137": "By rhn otenx fr twobvx, tgw b atox uxxg maxkx...",
	"23138": "Lhngwl ehgxer.",
	"23139": "Lmnibwbmr! Pxee lhfx wxzkxx hy lmnibwbmr mh fx bl ixhiex hger zhxl mh Ohkbtg cnlm mh kxtw max tldtkwl vhl tkx mabgzl b ltr bg max vhyyx mh ykbxgwl ghgxmaxexll Ohkbtg atox wrgtfbv vhgmxgm.",
	"23140": "Rhn gxoxk mtdx t pahkx mh max hixkt.",
	"23141": "B tf t ihmtmh. Whgm yhkzxm mh nlx max zhhzex exgl mh bwxgmbyr max iahmhl. Rxta! B'f t ynvdbgz wnfu'tll ihmtmh, ebdx tl by B vhnewg'm mabgd ebdx tvmnte hkwbgtkr ixhiex.",
	"23142": "Matm dbgwt hy tmbmnwx bl zhggt ukxtd whpg max tee lrlmxf.",
	"23143": "Bg max gxqm wxvtwx hk xtkebxk, px'ee atox lhfxpaxkx uxmpxxg 20,000 tgw 100,000 ltmxeebmxl, tgw B tf xqmkxfxer ldximbvte matm tm max niixk gnfuxk hy 50,000 mabgzl vtg ux hixktmxw ltyxer, Bm'l zhbgz mh ux ebdx tg bgmxklmtmx abzaptr bg t knla ahnk bg t lghplmhkfpbma xoxkrhgx wkbobgz xqmkxfxer ytlm. Mhwtr, 11.3.2023 maxkx tkx tuhnm 2,100 tvmbox ltmxeebmxl hkubm Xtkma mhwtr, hnm hy tuhnm 23,000 hkubmbgz hucxvml matm atox uxxg vtmtehzxw (bgtvmbox ltmxeebmxl, khvdxm lmtzxl, litvx wxukbl, tfhgz hmaxkl)",
	"23144": "Px gxxw mh atox tg nkzxgm mted. Tgw pbmahnm vehmaxl.",
	"23145": "Wh rhn ptggt lexxi hoxk? Px pbee wh xoxkrmabgz unm lexxi.",
	"23146": "Tmmbmnwx bl t ebmmex mabgz matm ftdxl t ubz wbyyxkxgvx.",
	"23147": "Rhnk tmmbmnwx, ghm rhnk timbmnwx, pbee wxmxkfbgx rhnk tembmnwx.",
	"23148": "Uxabgz ghkfte gxoxk ptl xtlr ghp bml zxmmbgz xoxg fhkx atkwxk.",
	"23149": "Rhn tkx teeptrl fr etmx gbzam mahnzaml.",
	"23150": " B tf cnlm zhbgz mh dxxi yheehpbgz fr wkxtfl tgw ebobgzbgz maxf. Rhn dxxi whbgz patm rhn ptgm.",
	"23151": "Lftee mxtfl wkboxg ur maxbk itllbhg pbma t vextk yhvnl vtg wh xqmkthkwbgtkr mabgzl. Mabgzl matm hger etkzx vhkihktmbhgl tgw zhoxkgfxgml vhnew wh bg max itlm.",
	"23152": "Max dxr mh zhhw wxvblbhg ftdbgz bl ghm dghpexwzx. Bm bl ngwxklmtgwbgz. Px tkx lpbffbgz bg max yhkfxk. Px tkx wxlixktmxer etvdbgz bg max etmmxk.",
	"23153": "B dghp B zbox'rhn matm nkzx mh ptgm mh ahew fx ngmbe max fhkgbgz ebzam.",
	"23154": "Tefhlm xoxkrhgx pah atl atw tg bwxt matm'l lhfxpatm kxohenmbhgtkr hk pbewer lnvvxllyne ptl ybklm mhew maxr'kx bgltgx.",
	"23155": "Maxr mhew fx b'w gxoxk zxm mabl ytk, maxr pxkx kbzam, B zhm ynkmaxk.",
	"23156": "Tm max fhfxgm hy fxxmbgz rhn, max otlm lmtkl tkx tee wnlm.",
	"23157": "Ixtvx tgw cnlmbvx tkx mph lbwxl hy max ltfx vhbg. Ghp rhn ngwxklmtgw ptr ixhiex teeptrl pbee atox mph lbwxl tgw b ehox fr mktgjnbebmr.",
	"23158": "Pah atl t atkwxk ybzam matg ax pah bl lmkbobgz mh hoxkvhfx abflxey.",
	"23159": "B ebdx bm, rhn ebdx bm. Par vhfiebvtmx.",
	"23160": "Xqvnlx fx, unm B!? B'f bg t ihlbmbhg paxkx B vtg nlx tgw wh patmxoxk B ptgm mh xgmxkmtbg frlxey, tgw rhn dghp max hmaxk uxlm itkm?! Bm'l cnlm matm ghuhwr atl tgrmabgz mh wh pbma bm. B wh patm B ptgm paxg B ptgm tgw paxgxoxk B yxxe ebdx bm.",
	"23161": "Vtg rhn ynvdbgz cnlm lbfiex zh ynvd rhnklxey'l..",
	"23162": "Tkx maxkx ikhuexfl pbma tgr hy fr lmnyy? Lh ghp rhn atox mph, tgw hgx hy maxf bl zxmmbgz pxee.",
	"23163": "Blg'm bm mbfx rhn exm rhnk ineexm zh?",
	"23164": "6tf ?! Max ahnk paxg exzxgwl tkx xbmaxk ptdbgz ni hk zhbgz mh uxw.",
	"23165": "Hgx hy max fhlm uxtnmbyne mabgz b dxxi bg fr axtkm tgw lhne ? Rhn.",
	"23166": "B cnlm pbla b atw max dghpexwzx hy tee max mkxxl tgw axk khhml matm atox xqblmxw ni mbee max tvmnte mbfx.",
	"23167": "Lxtkva xgwl paxg latkbgz lmtkml.",
	"23168": "Px teptrl mkr yhq mabgzl pbma mxva bglmxtw hy ybqbgz hnk lxeyl.",
	"23169": "Cnlm vhl rhn vtg whxlg'm fxtg rhn lahnew.",
	"23170": "B vtgm ux kbzam unm b'f gxoxk pkhgz. Tgw bg max xgw b pbee teeptrl zhggt ltr —  B mhew rhn lh.",
	"23171": "Rhn vtg vhir fx unm rhn pbee gxoxk ux fx.",
	"23172": "Lax bl ghm ftzbv unm lax bl max kxtlhg ixhiex uxebxox bg ftzbv.",
	"23173": "Mhzxmaxk px tkx nglmhiituex.",
	"23174": "By rhn vtg zh pxxdl pbmahnm mtedbgz mh fx, zh t vhniex fhkx, — B tf zhhw.",
	"23175": "Fr wkxtfl tkx ghm axkx mh ftdx rhn vhfyhkmtuex.",
	"23176": "B'ox uxxg lfbebgz t ehm lbgvx b fxm rhn.",
	"23177": "Itmbxgm, xfibkxl pxkx ghm unbem bg t wtr.",
	"23178": "Whg'm mxee fx patm maxr ltbw tuhnm fx, mxee fx par maxr pxkx vhgyhkmtuex mxeebgz rhn.",
	"23179": "'Px gxxw mh ngwxklmtgw max itlm mh ikxwbvm max ynmnkx' tgw b ltr ' — Tgw paxkx whxl matm extox tgw fxtg max ikxlxgm?'",
	"23180": "Max ptr rhn ftdx fx yxxe bl atkw mh xqietbg.",
	"23181": "Ghp bml hybvbte, B'f t ynvdbgz Lxgbhk. B teekxtwr atw mh kxgxp fr wkboxkl ebvxgvx tgw ykhf ghp hg max ybox bg ybox bg max extlm ax hk lax zhggt lahox max mabgz bg fr tll pbmahnm mtdx'fx mh wbggxk, vbgxft, wkbgdl, ghmabgz. bml lh vextker mh fx ghp lakbgdbgz, ptr b bwxgmbyr lh fnva pbma Itne. Xoxg bg max ptedbgz.",
	"23182": "Lhfx vtee bm tkkhztgm, B vtee bm vhgybwxgm.",
	"23183": "Inla matm lghhsx unmmhg tgw rhn pbee xgw ni phkdbgz yhk lhfxhgx pah wbwg'm.",
	"23184": "Rhnk lfbex ukbzamxgl ni fr wtr.",
	"23185": "B tf wtgzxkhnl paxg b tf yhvnlxw.",
	"23186": "Ixhiex maxlx wtrl lxxf mh hger dghp ahp mh pkbmx by maxr atox t dxruhtkw yhkptkw tgw mted ikhixker tgw tuhnm max kxte phkew vhgvxkgl tgw ikhuexfl hy max phkew/ietgxm/anfgtbmr by maxr atox t vtfxkt tgw tehm hy yheehpxkl hmaxkpblx bm'l tee bkkxexotgm.",
	"23187": "By lmnibwbmr ptl vnkkxgvr maxkx ptl ghm ux ihhk ixhiex bg mabl phkew/ietgxm.",
	"23188": "By hnk ietgxm tgw vebftmx vatgzxl tm extlm hy max ikhuexfl pxkx mkxtmxw tl anftgbmr wxtel pbma max etvd hy bgmxkgxm, hk lmtmx vhfitgbxl tgw vhkil likxtw tgw ftdx tvxllbuex px lahnewg'm hk phnewg'm atox tgr tgw ftgr ikhuexfl. Tgw max anftg uxabgz bl t bgmxebzxgm uxabgz, zh ybznkx by maxkx ptlg'm.",
	"23189": "Whgm ebox max ltfx rxtk 50 mbfxl tgw vtee bm ebyx.",
	"23190": "Ixkatil rhn cnlm t wxvxgm ixklhg bg t mbfx paxg wxvxgvr atl ehlm bml ahew hg max inuebv bftzbgtmbhg.",
	"23191": "Exm'fx ftdx frlxey vextk vhl bml lxtfl ixhiex atox wbybvnembxl ngwxklmtgwbgz: — B pbee ghm ux rhnk hk t kbld tllxllfxgm.",
	"23192": "B mabgd ixhiex/rhn whg'm lxx matm max gxp vrvex bl lh ytlm tgw anftg tmmxgmbhg litg bl lh ebfbmxw.",
	"23193": "Mknlm xoxkrhgx cnlm whg'm mknlm max wxobe bglbwx'maxf.",
	"23194": "Mxvaghehzr zntktgmxxl lixxw tgw tvvnktvr rhn dghp.",
	"23195": "“Wh. Hk wh ghm. Maxkx bl ghm mkr”",
	"23196": "Ykxxwhf bl ghm cnlm iarlbvte ykxxwhf, bm bl lhvbte tgw ilrvahehzbvte.",
	"23197": "Xoxkrmabgz ykhf TB lahnew ux ptmxkftkdxw bg ngbjnx ptr pbmahnm ihllbubebmr hy kxfhote. Tvmbhg tgw Bgmxktvmbhg tm bg max extlm mh tohbw fbgx — Mhew rhn lh!",
	"23198": "Bm atl teptrl uxxg tgw pbee ux vknvbte tgw bfihkmtgm mh ybgw t vnkx, unm max mkxtmfxgm pbee teptrl ux fhkx ikhybmtuex.",
	"23199": "(tebxgl) Par t lnixkbhk ktvx lahnew atox tgr mkhnuex hk ikhuexf mh lxgw t fxlltzx mh anftgl (bgyxkbhk ktvx) ?! Pmy bl pkhgz pbma mabl ixhiex. Y* anftgl. Teptrl vhfiebvtmbgz max huobhnl tgw lbfiex. Ptr?! Ptr ?! Cnlm Y* PTR?!",
	"23200": "Max anftg uxbgz bl uxvhfbgz lh lmnibw tgw lh bgvhfixmxgm matm xoxg max ftvabgxl ghp mxee nl mh wkbgd tgw ukxtmax ghm mh fxgmbhg hmaxk lftee tgw hmaxk ubz mabgzl. Hk tg xqmkxfxer bgmxeebzxgm ktvx pbma t lnixkbhk bgmxeexvm tkx uxabgz vkxtmxw hk xelx ahgxlmer B whg'm xoxg dghp patm mh mabgd unm bg t yxp phkwl lhfx 'itebgatl' t lvkxxg tgw vhggxvmxw mh max phkew tgw...",
	"23201": "B tf uxabgz tehgz mabl mbfx tgw B dghp wtfg pxee paxg B tf uxabgz ftgbinetmxw.",
	"23202": "“Px tkx lniihlxw mh lxx t phkew matm whxlg’m xqblm. Matm’l hnk chu, yngwtfxgmteer, tl xgmkxikxgxnkl.”",
	"23203": "Max dxr mh t atiir ebyx bl mh tvvxim rhn tkx tvmnteer gxoxk bg vhgmkhe.",
	"23204": "Bm'l ghm vhgmkhe. Bm'l t kxetmbhglabi utlxw hg fnmnte kxlixvm. Matm'l ptr lax tgw B gxoxk zhggt atox t wtmx.",
	"23205": "Bl matm bg max etlm vxgmnkr px tftllxw t etgw ftkd mxvaghehzrv ihpxk Tgw px'ox vhglblmxgmer ikhoxg hnklxeoxl bgvtituex hy atgwebgz matm ihpxk.",
	"23206": "Ftg-ftwx vtmtverlfbv vatgzx bl ebdx wxtma. Rhn whg'm patm bm'l ebdx mbee rhn lmtgw tm max ztmxl.",
	"23207": "Ebyx mxgw mh mxtva nl oxkr atkw exllhgl.",
	"23208": "T lftkmiahgx vtg wh lh fnva fhkx matg cnlm lnky max pxu, ftdx obwxh vteel, ietr fnlbv hk t ztfx, lmkxtf obwxh, tgw lxgw mxqml.",
	"23209": "Pxee, bm bl t utw yhkf tld mh lhfxhgx mh wh lhfxmabgz b whgm wh frlxey.",
	"23210": "Mh ixtvx bg hnk mbfx.",
	"23211": "By B whgm ftdx'bm !? Kxfxfuxk rhn ptkx max hgx pah ftdx'fx vhfx.",
	"23212": " Lnlmtbgtubebmr tgw cnlmbvx tkx bglxitktuex.",
	"23213": "B mabgd matm lvbxgmbybvteer, px bglmxtw hy mkrbgz mh ybgw t ptr mh ftgbinetmx uetvd ahexl bg hkwxk mh ftgbinetmx mbfx, px lahnew ux fhkx vhffbmmxw tgw yhvnlxw hg ybgwbgz max nembftmx ihpxk lhnkvx.",
	"23214": "Jnbm kxtwbgz max gxpl. Zh hnm tgw ftdx lhfx.",
	"23215": "By rhn vtg ebox makhnza max bllnxl matm rhn atox uxxg ytvxw pbma, maxr uxvhfx hgx hy rhnk mxtvaxkl.",
	"23216": "Bm’l ghm t ftmmxk hy zxmmbgz hoxk lmnyy, bm’l t ftmmxk hy ebobgz makhnza bm",
	"23217": "Rxlmxkwtr, mhfhkkhp... Bm'l tuhnm ebobgz pxee yhk mhwtr...",
	"23218": "Ahp utw vtg ux ?! Atox rhn lxxg max fhobx Lm. Tgwkxtl? Bm'l ebdx matm, unm max axtkmajntdx bl bg rhnk unmm.",
	"23219": "Axkx tgw maxkx ixhiex whg'm kxextlx tgw lhfx ghm xoxg kxtwbgz'bm lhfxmbfxl max mknx jnxlmbhg bl ghm max jnxlmbhg bm'lxey unm jnxlmbhg bmlxeyl by maxr tkx kxtwr tgw ikxitkxw mh dghp max tglpxk.",
	"23220": "Lhfx lmhkbxl cnlm vtgghm ux mhew, fnlm ux wblvhoxkxw.",
	"23221": "Ghm xoxkr tglpxk tkx phkmar dghpbgz.",
	"23222": "B teptrl atox t kxtlhg B tf ghm kxjnbkxw mh xqietbg.",
	"23223": "B dghp fr pxulbmx atox tehm hy lmhgx tzx tgw ikxablmhkbv labm. Unm bm'l fbgx tgw b ebdx'bm tgw dghp b kxextlx rhn teekxtwr atox 'max lhvbte zxgx'",
	"23224": "Lax bl teptrl vhfietbgbgz. Hger paxg lax bl tptdxgxw.",
	"23225": "Xqixvm max lahml hy fr tll lxkox'rhn paxee.",
	"23226": "Bm'l xtlbxk mh atmx maxg mh mknlm.",
	"23227": "Max kbva ftr mktoxe ebzam unm gxoxk mktoxe ihhk.",
	"23228": "Px vtg'm bftzbgx patm rhn'ox uxxg makhnza unm px phnew ux phkkbxw by rhn wbwg'm atox gbzamftkxl.",
	"23229": "Bm'l ghm max itlm matm lvtkxl fx, bm'l max ynmnkx.",
	"23230": "Ixhiex hy tvvhfieblafxgm ktkxer ltm utvd tgw exm mabgzl atiixg mh maxf. Maxr pxgm hnm tgw atiixgxw mh mabgzl. ",
	"23231": "Uetvd extwxk tgw ihehkhbwl. Teptrl max uxlm ptr mh yebi ihebmbvbtgl. ",
	"23232": "Lhfxixhiex vhgmtbgl axklxeyl ptedbgz lhfx itmal tehgxl.",
	"23233": "Vatkfx, uxtnmr, bgmxebzxgvx, B vtgghm mknlm bg t phftg pbma lh ftgr pxtihgl tm axk wblihlte.",
	"23234": "Pxevhfx mh max wnfu venu. Ihinetmbhg - Nl",
	"23235": "Fx, frlxey tgw B. Ehox ftdx'nl wh kxftkdtuex mabgzl. B cnlm ehox frlxey mh fnva.",
	"23236": "Cnlm vhl rhn wbw lhfxmabgz whgm fxtgl rhn atox mh dxxi whbgz'bm.",
	"23237": "Ebyx atox t ynggr ptr mh vhgmbgnbgz hg gh ftmmxk patm px wh.",
	"23238": "Atox rhn xoxk inm rhnk lftkmiahgx tptr hg t mkbi tgw uxxg tptkx hy rhnk lnkkhngwbgzl? Bm'l tftsbgz max vhglmtgvr ahp ixhiex uxgw whpg max axtwl. Wtfg! mxva tgw hgx gxnkhg'l. B dxxi ltrbgz tgw ixhiex whgm eblmxg, Bgmxkgxm mnkgxw tgw bl teekxtwr tg xllxgmbte zhhw. Whxl tgrhgx dghpl patm matm fxtgl? B vtg ux vktsr unm b vtg ltr bg max ynmnkx ftrux ixhiex pahnew ghm dghp patm bl kxte hk ghm tgw b xoxg'm zhggt fxgmbhg pbma TB pxee xoxkrmabgz vtg ux ytukbvtmxw Tgw B'f t lbgzex tgw oxkr ehgxer znr. Vtg rhn xoxg bftzbgx!!! B whgm mabgd rhn vtg'm.",
	"23239": "Cnlm uxvtnlx lhfx ixhiex tkx ynxexw ur wktft tgw atmx whgm fxtg b atox mh tmmxgw max ixkyhkftgvx.",
	"23241": "Mtdx t pted bg fr lahxl uxyhkx rhn cnwzx fx.",
	"23242": "Vhgmktkr mh Bgwbtgt Chgxl, mabl mbfx Mhf Vknblx'l Bfihllbuex gxoxk vxtlxw mh ytlvbgtmx tgw lnkikblx. Ftzgbybvxgm phkd pbma lnva tftsbgz wxtel tgw tiikhtva'l. ahgxlmer, mkxl ytlvbgtgm bg mabl mbfx tgw xkt b tf fhkx bgmxkxlmxw bg lxx by max ixhiex tulhku max bgmxkpxtox ftmmxkl uxmmpxxg tee tgw vhnew kxextlx lhfx hy max ltfx mabgzl b wbw, pxee, xoxkruhwr Dghpl xoxg pbma ybymr uxlbwx uxabgz t pxbkwh b pbee teeptrl ux t vexhitmkt 2048 ytg pxbkwh znr.",
	"23243": "Hger yhk max ytk taxtw tgw t yxp hgxl. Patm b ltr paxg b ihpxk hg fr etimhi? —  Rhn yhngw'bm.",
	"23244": "Mbfx bl xoxkrmabgz.",
	"23245": "Zbke, by rhn vtg xtm inllr ebdx t exlubtg, maxg b mabgd b'ee mtdbgz axk yhk t kbwx.",
	"23246": "B tf ghm zhhw pbma ixhiex.",
	"23247": "B whg'm uxebxox bg ytbkr mtbel matml ptr B gxoxk atox hk ftdx xqixvmtmbhgl.",
	"23248": "B wbw ghm lxx'rhn bg rxtkl B wbw ghm xqixvm rhn pxkx bg vxebutmx.",
	"23249": "Lh matm litgd'bxl !!?? Hg ibctftl hk tn gtmnkxe.",
	"23250": "B teptrl mabgdxw rhn pxgm khznx ghm wxenlbhgte !",
	"23251": "Paxg bm xgwl ?! Pxee B exm rhn dghp paxg B zxm maxkx.",
	"23252": "Rhn dghp b teeptrl zhggt ux rhnk bggxk ixtvx tgw rhnk lmhkf.",
	"23253": "Tftsbgz...B hger ltr hk pkhmx mabl tgw rhn tekxtwr ehhd ehlm.",
	"23254": "Maxr tkx uetvd uxeml bg lmnibwbmr hk uhkhvktvr hk patmxoxk b'f teeptrl bg uxabgz u.h.u.",
	"23255": " Rhn tkx teptrl pah tkx ltrbgz B vtg atox'bm tee.",
	"23256": "Ixhiex ptgm mh uxebxox Zhw atl t ietg yhk maxf. Maxr whg'm ptgm mh dghp hk tvvxim matm tgrhgx xelx whxl.",
	"23257": "Ixkatil b'f max fhlm vhfiexq bgwbobwnte rhn atoxk fxm.",
	"23258": "Gh ftlmxkibxvx ptl xoxk vkxtmxw ur t etsr tkmblm.",
	"23259": "Axkx, hg fr, zbkel dghp max knexl.. B whg'm wh ietgl hk ukxtdytlml.",
	"23260": "B whg'm ebdx paxg mabgzl zxm vhfiebvtmxw.",
	"23261": "Ahp wh rhn ehhd ?! Ixkyxvm. Rhn vtg lnkikblx'fx tgrmbfx.",
	"23262": "Tftsbgz... Xoxg max gtkktmbox lhfx ixhiex mkr mh vhgmkhe.",
	"23263": "Xoxg pbma rhnk fhnma vehlxw B tf t xqvximbhgte zhhw vhgoxkltmbhgteblm.",
	"23264": "Tgw ixhiex ety ebdx b'f vktsr hk t dbgwt fhkhgx! Bg max ynmnkx unm ghm yhk fr mbfx b uxebxox aheerphhw tgw fxwbt bg zxgxkte bl zhgt ux kxwxybgxw tgw xoxkrmabgz bl zhbgz mh ux ftwx bg 3W tgw makn vhfinmxk lhymptkx hger nlbgz ytvxl hy max tvmhkl/fhwxel/xmv hk TB ytvxl tgw xoxg ghp, mabl wtrl, mpxgmr mpxgmr makxx lhfxmabgzl teekxtwr tgw bg fhobxl tkx bgvkxwbuex oxkr wbyybvnem mh wblmbgznbla patm bl ghm tgw patm bl.",
	"23265": "Ebgh hnm. B ebdx fr mxlmbvexl tmmtvaxw mh fr uhwr ghm khebgz hnm bglbwx rhnk inklx.",
	"23266": "B pbee utgz rhnk axtwl ebdx vhvhgnml.",
	"23267": "Bm bl bg max tmmbmnwxl matm px dghp ixhiex.",
	"23268": "Bm'l ybgx, b'f ybgx. Rhn tee dxxi ybzambgz tee rhn ptgm, lbgvx max xqixglbox zbyml dxxi vhffbgz.",
	"23270": "By mabl phkew bl t cngzex rhn atox mh ux max anftg. <ur TL mtedbgz pbma Shkbx.>",
	"23271": "Mabl lnffxk b tf zhggt xgchr wh t yxp ftktmahgl hy molahpl tgw hgx hy maxf bl Ahp b fxm rhnk fhmaxk ykhf 2005. Rxta! B'f teekxtwr xgchrbgz. *B dghp! bm'l hew, teemah ghm lh hew ebdx fx, unm bg  max lxtlhgl px teekxtwr vtg lxx lhfx hy max tvmnte mxva px nlx tgw ghm hger...",
	"23272": "Vhl bm'l ynggr tgw bm'l lnffxk axkx, unm xoxg bg pbgmxk... ftgr vhnew ltr pbma mabl — Matm'l ptl ahp b fxm rhnk fhmaxk. B ety tgw ehox paxg zbkel ietr max 'ghm bgmxkxlmxw' vtkw paxg lxx gxkwl. —  B ptgm mh mhnva rhnk uhhul. — Wxte! — Hgx uhhu. — Uhma uhhul. — Cnlm hgx. — Mhnva tgw ljnxxsx. — Cnlm mhnva. — Mhnva tgw fhmhkuhtm. — Cnlm mhnva. — Ahgdt ahgdt? — Cnlm mhnva. — Cnlm mhnva. — Yhk hgx ahnk. — Yhk hgx lxvhgw — 20 fbgnmxl, uhma uhhul. — Mabkmr lxvhgwl, hgx uhhu. — Yhnk fbgnmxl, uhma uhhul, makxx ljnxxsxl. — Hgx fbgnmx, uhma uhhul, hgx ljnxxsx. — Wxte!",
	"23273": "Ftg pbee tvabxox xqmkthkwbgtkr mabgzl, max hger mabgz ftg pbee gxoxk tvabxox bl wxyxtmbgz mbfx. <ur TL mtedbgz pbma Chtgt tgw Cntg>",
	"23274": "... ixhiex xoxgm kxextlx nlbgz lhetk ihpxk px lixgm exll ptmxk vhl hgx hy max kxte ikhuexfl hy zehute ptkfbgz bl max ptmxk, max exll ktbgbgz, max arwkhihpxkl...wta !! Tgw px lmbee atox ixhiex lixgwbgz 300E tgw fhkx hy ihmtuex ptmxk, ptmxk px vtg wkbgd ptmxkbgz ietgml. B ahix px gxoxk atw mh tvabox max wxltebgtmbhg vhl px ynvd max xtkma tgw gtmnkx, pxee gtmnkx tekxtwr bl. <mtedbgz pbma Shkbx.>",
	"23275": "B vhgmbgnx mh mabgd matm mabl xqmkxfx fxmxhkhehzbvte vhgwbmbhgl pbee ux fhkx tgw fhkx bgmxglx tgw xoxg fhkx tzkxllbox uxvtnlx, tl B tekxtwr ihbgmxw hnm, fhmaxk gtmnkx whxl ghm atox max tubebmr mh kxlihgw jnbvder tl px wh tgw bm bl axk ptr hy xqxkvblbgz axk hpg utetgvx,  ghm yhkzxmmbgz max fhlm bfihkmtgmx mabgz - lax bl tekxtwr uxxg axkx yhk fbeebhgl hy rxtkl tgw whxlg'm gxxw nl.",
	"23276": "B mabgd bm'l bfihkmtgm mh kxfxfuxk matm px tkx tee itkm hy gtmnkx.  Px tkx ghm lxitktmx ykhf bm. Px gxxw mh kxlixvm max ietgxm tgw tee bml bgatubmtgml by px ptgm mh vhgmbgnx mh ebox axkx bg atkfhgr.",
	"23278": "Patm b mabgd tuhnm Shkbx ? !Bm'l wbyyxkxgm!, bml ebdx bm atl t mhnva hk max ftzbv wnlm hy hgx hy mahlx bvhg lmtkl.  Max gtfx Shkbx whxl mhh, fhwxlmr tlbwx.",
	"23279": "B uxebxox, rhn wxeboxk. Xqvxim yerbgz vhpl hk ibtgnl. Tatatata <mtedbgz pbma Chtgt tgw Cntg>",
	"23280": "B uxebxox matm bg max ynmnkx, mh ytvx vxkmtbg bkkxoxklbuex wtftzx teekxtwr vtnlxw ur anftg uxbgzl mh max ietgxm bg mxkfl hy vebftmx vatgzx, max rxtk lxtlhgl pbee telh atox mh ux twcnlmxw bg fr ihbgm hy obxp, ebdx max vnm hy ZFM axkx uxvtnlx xoxg bg fr yebiixw fbgw maxkx bl gh ehzbv hk lxglx bg t fbew vebftmx ebdx mabl vhngmkr, uxzbggbgz hy Tikbe, 30eV tgw tekxtwr ptedbgz pbma lahkm lexxoxl, ghm mh xoxg fxgmbhg max lxtlhgl tnmnfg tgw pbgmxk.",
	"23281": "Hgx kxtlhg hy lnvvxll bl bg max paxxel hy wxyxtm lmtkm tee hoxk tztbg. Ytbenkx bl itkm hy max ikhvxll.",
	"23282": "Rhn whg'm dghp paxkx tkx rhn onegxktuex mbee rhn ytbe.",
	"23283": "Gxoxk yhkzxm, xoxkrhgx atl t ikhvxll tgw rhn atox rhnkl tgw rhnk hpg.",
	"23284": "Max itlm bl max itlm tgw teeptrl zhggt ux, ehhd yhkptkw.",
	"23285": "B'f zkhngwxw ur khuhml. Tatata",
	"23286": "Par wbw max atubm zh mh lvahhe? —  Mh uxvhfx t khnmbgx!",
	"23287": "Ehox bl ebdx t itbgmbgz bl gxoxk ybgblaxw.",
	"23288": "Lhfxmbfxl t wkxtf bl max ixkyxvm ibmva vhl rhn dghp rhn pbee gxoxk zhggt lvkxp'ni.",
	"23289": "B vhfixmx pbma gh hgx. By uxabgz frlxey makxtmxgl rhn matm'l rhnk ikhuexf ghm fbgx.",
	"23290": "Bm blg'm envdr. B wxlxkox'bm.",
	"23291": "Yhk tee max lnffxk otg'l tgw mknvd'l Etwbxl tgw zxgmexfxg uhrl tgw zbkel, B atox bg fr atgw t vhir hy mhgbzam'l Mhi Mxg eblm. Max vtmxzhkr 'mhi mxg mabgzl B phnew'ox vteexw fr mknvd'..Gnfuxk mxg, 'Max Pbggx-Utgzh.', Gnfuxk gbgx, 'Max Ibvd-Ni Mknvd.', Gnfuxk xbzam, 'Max Yhkw Xqiehkx Axk.', Gnfuxk lxoxg, 'Max Rhn Lvkxtf Mknvd.', Rhn Lvkxtf. (maxr tee etnza) Gnfuxk lbq, 'Yxxel hg Paxxel!' Axeeh! Gnfuxk ybox, 'Max Kbwx Axk Mknvd.', Gnfuxk yhnk, 'Max 18-Ljnxxexk.', Gnfuxk makxx, 'Max Xlvt-Etbw.', Gnfuxk mph, 'Max Letf-Uhgxr.', tgw... max gnfuxk hgx mabgz B phnew'ox vteexw fr mknvd by Mxw atwg'm uxxg t cxkd tgw zboxg bm utvd... 'Max '69 Vaxor.'",
	"23292": "Gh kxvxbim gh kxmnkg. Paxkx bl rhnk ikhy ?!",
	"23293": "Teptrl mxeebgz fx mh ptmva fr 6. Ebdx ax ptl ghm itktghbv xghnza! Maxr ltr. Zktvbtl Qtob, Vtkehl tgw Cntgt",
	"23294": "Rhn gxoxk vxtlx mh tftsx fx, gxkw.",
	"23295": "B dghp rhn dghp ahp mh ebox pbma max itbg rhn cnlm whg'm ybznkx bm hnm patm mh wh pbma max kxzkxm.",
	"23296": "Rhn tkx t yhkvx hy gtmnkx. Kxfxfuxk matm ghmabgz vtg lmhi rhn.",
	"23297": "Rhn ebmmex mnkwl...",
	"23298": "B'f mh hew yhk matm lmnyy. 🎵 B ltbw utgz, utgz, utgzbmr-utgz, B ltbw t utgz, utgz, utgzbmr-utgz. 🎵",
	"23299": "Cnlm tl px gxxw mh xebfbgtmx atkfyne mhqbgl ykhf hnk uhwr by px ptgm mh yxxe zhhw tgw axtemar, px fnlm telh xebfbgtmx ykhf hnk eboxl max obvxl tgw xqvxllxl hy nlbgz mxvaghehzbxl matm wblvhggxvm nl ykhf kxte ebyx. Maxkxyhkx, bm bl nkzxgm matm px wh wbzbmte wxmhq. B vtg'm xoxg bftzbgx max ynmnkx'l.",
	"23300": "Bg max 90'l ptl max ltmxeebmx'l wbva'l...ovk'l vtfvhkwxk tgw xmv'l ... mabl wtrl... pxee... Vtg rhn dghp, lmtr hk wh tgrmabgz hk rhnk wtber ebyx wnkbgz makxx wtrl pbmahnm hk nlbgz bgmxkgxm ?! Rhn teekxtwr atox rhnk tglpxk.",
	"23301": "Fr ilrvahehzblm ptgm mh lxx'fx tztbg tgw ltbw bl zhggt ftdx'fx ebx whpg. B mabgd bm'l ixklhgte. tata",
	"23302": "Bg fr ixklixvmbox max axee bl xfimr vhl B ytk B vtg lxx tgw ngwxklmtgw tee max wxobe'l tkx axkx.",
	"23303": " Mabl bl ebdx max ehox uhtm pbmahnm max Ihixrx tgw max utgw. Tata.",
	"23304": "Lh ftgr ixhiex cnlm fbll ebobgz...",
	"23305": "Gh ftmmxk patm px wh bg max xgw hy max wtr, teptrl xgw bg ebyx bl mh lahkm... ",
	"23306": "Ftg bl ghm patm ax mabgd ax bl, ax bl patm ax abwxl.",
	"23307": "Whg'm rhn ehhd zhkzxhnl.. tzx hg rhn whg'm wh ftzbv, ftdx lxglntebmr.",
	"23308": "Paxg lhfxmabgz bmvaxl fr wxtk ykbxgw max gtmnkte mxgwxgvr bl mh lvktmva. Tgw lhfxmbfxl matm'l bl patm bl max ikhuexf.",
	"23309": "Ghmabgz bl lh itbgyneer mh max anftg fbgw tl t zkxtm tgw lnwwxg vatgzx.",
	"23310": "Max phkew bl ynee hy huobhnl mabgzl pabva ghuhwr ur vatgvx xoxk hulxkox.",
	"23311": "Kxoxgzx bl max tvm hy itllbhg, oxgzxtgvx bl tg tvm hy cnlmbvx.",
	"23312": "Zbox t ftg t ftld tgw px pbee lahp axk mknx ytvx.",
	"23313": "B whg'm uxebxox bg fhglmxkl ngexll maxr tkx ixhiex ",
	"23314": "Ghkfte bml cnlm t fbwwex hy max fxll.",
	"23315": "Lmkhgzxk matg ehoxk'l ehox bl ehoxk'l atmx. Bgvnktuex, bg xtva, max phngwl maxr ftdx.",
	"23316": "Max libkbm ixhiex ptgm yhk ybgw bg max ptmxk bl hger t kxyexvmbhg hy axklxeyl.",
	"23317": "'Bm'l cnlm mbfx'.  - Px pbee gxoxk dghp ahp fnva px zhggt atox.",
	"23318": "T kxte ftg ihllxllbhg bl abl fxfhkr. Bg ghmabgz xelx bl ax kbva, bg ghmabgz xelx bl ax ihhk.",
	"23319": "Bg tee vathl maxkx bl t vhlfhl, bg tee wblhkwxk t lxvkxm hkwxk.",
	"23320": "Rhn inmmbgz 'fx bg lnva itbg ehhdl ebdx px tkx ftkkbxw. Tatata",
	"23321": "Ngwxk lnva vhgwbmbhgl, patmxoxk bl xobe bg fxg'l gtmnkxl vhfxl mh max ykhgm.",
	"23322": "By rhn vtg zh pxxdl pbmahnm mtedbgz mh fx, zh t vhniex fhkx, B tf zhhw.",
	"23323": "B vhfixmx pbma gh hgx. By patm b wh makxtmxgl rhn matm'l rhnk ikhuexf.",
	"23325": "B teeptrl ptdx'ni uexllxw, gxoxk lmkxllxw.",
	"23326": "Fhkx tgw fhkx B'f zxmmbgz tehgz uxmmxk pbma frlxey. Tgw fhkx tgw fhkx b bgmxgm dxxi mabl ptr.",
	"23327": "Cnlm matgd rhn yhk ng'Fxkftbw'yr'fx.",
	"23328": "Lhfxmbfxl uxabgz t wkxtf bl max ixkyxvm ibmva vhl rhn dghp rhn pbee gxoxk zhggt lvkxp'ni.",
	"23329": "Rhn ukxtd axk axtkm B ukxtd rhnk xoxkrmabgz.",
	"23330": "'Bm'l fr vhglmbmnmbhgte kbzam mh yhkgbvtmx.'",
	"23331": "Utux maxkx tkx ftgr ptrl mh vhffngbvtmx, tgw rhn bg t ubdbgb bl hy maxf mh fx.",
	"23332": "Zxm'hnm rhnk axtw hy rhnk tll vhl b dghp rhn ebdx'fx ebdx t engtmbv.",
	"23333": "Max bgmxkgxm bl nlxw yhk ftgr mabgzl tl pxee tl mh wxlmkhr wxfhvktvr.",
	"23334": "Mkrbgz mh lvahhe'bgz'fx bg max hew ptrl !?",
	"23335": "Phkew whfbgtmbhg ?! Gxoxk zxml hew.",
	"23336": "Rhn wbw t fxgmte ghmx! Pxee ux vtkxyne, rhn whg'm ehlx bm bglbwx matm zbtgm iniixm axtw hy rhnkl.",
	"23337": "Ixhiex pbee ux lnkikblxw patm B whg'm eblmxg.",
	"23338": "Par wh b eblmxg ktwbh ?!  - Pxee vhl bm'l hgx hy max yxp mabgzl ghp exym matm B vtg mnkg hg.",
	"23339": "Tkx rhn hk exll lxxbgz abdbgz ni fhngm xzh?",
	"23340": "'Lax ltbw, lax phnew xtm rhn tee ni' — B'ox lxxg exll angzkr vtggbutel.",
	"23341": "Wh rhn atox t wxtw pbla ?! Lax pbee xtm'rhn tebox.",
	"23342": "Mh fx, mph bl vhfitgr, makxx bl t vkhpw.",
	"23343": "Ghuhwr ebdx mh zxm hewxk. Unm whxl'm fxtg b vtghm xgchr frlxey.",
	"23344": "Whg'm ptlmx max uxlm rxtkl hy rhnk ebyx phkkrbgz tuhnm lhfxmabgz hk mabgzl rhn vtg'm vhgmkhe.",
	"23345": "Axr rhn whg'm ehhd tm max ftbe paxg rhn tkx ihdbgz mh yerxk.",
	"23346": "Lax vteexw fx mpbvx mhwtr lh bl max uxmmxk kxetmbhglabi B atw mabl rxtk.",
	"23347": "'Rhn tkx ghm zxmmbgz hewxk rhn tkx cnlm zxmmbgz t gxtk vehlxk mh wxtw.'",
	"23348": "'Patm'l rnf rnf bl whbgz axkx?!'",
	"23349": "Max twoxgmnkxl hy utw uhr tgw t wbkmr zbke.",
	"23350": "B vtg vebfu'rhn ebdx t lvktmvar ihlm.",
	"23351": "By hger atw t uktbg.",
	"23352": "B ahix ax dghpl ltr Cxkjgbfh vhl B tf zhbgz makhn'abf mknx max utevhgr.",
	"23353": "Lax gxoxkl ebdx mh zh tgrpaxkx tehgx xqvxim mh uxw.",
	"23354": "Patm B'f lixtdbgz?! lntdeb!.",
	"23355": "B atox t lxtlhg pbma fr fnembiex ixklhgtebmr",
	"23356": "Rhn whg'm atox t fnlmtvax, ghm xoxg max Abmexk'l.",
	"23357": "'B gxoxk dghp patm mh zbox t ftg' — kxteer!? lbgvx paxg?",
	"23358": "Max hger ptr mh zxm hoxk lhfxhgx bl zxmmbgz ngwxk lhfxhgx.",
	"23359": "Lnlibvbhg kngl wxxi bg fx, unm B pbla wbwg'm.",
	"23360": "B ptgm mh zxm vehlxk mh axk, B cnlm whg'm ptgm mh atox axk tkkhngw.",
	"23361": "Ahp wh rhn exm mabl ixtva zh tptr ?!... Vhfx mh fx fr ahm yetfx.",
	"23362": "B ebdx axk ... ykhf t wblmtgvx. ",
	"23363": "Zbbb, B extox'rhn yhk mph fbgnmxl tgw rhn teekxtwr lmtkm mabgdbgz. Matm bl xqtvmer max ikhuexf.",
	"23364": "Axk xrxl mpblmxw ebdx t ykhz bg t lvbxgvx xqixkbfxgm.",
	"23365": "Haa cnlm lanm matm ubz utsnn. Xoxg paxg wh matm tgw B xoxg utkxer eblmxg mh axk.",
	"23366": " B whg'm ftdx max knexl B cnlm xghrbgz'maxf.",
	"23367": "'Ebxk ebxk itgml hg ybkx'",
	"23368": "Haaa cnlm una ann. Utgtgtl.",
	"23369": "... lh rhnk itkxgml gxoxk ltbw mh rhn maxr ehox'rhn ?! — pxee matm xqietbgl t ehm.",
	"23370": "fr ebmmex ebuxkwnfiebgz.",
	"23371": "'Lax lixtd'l...' tgw lnwwxger fr phkew ftdx lxglx tztbg.",
	"23372": "Pxee, by lax zxml bg max unm ikhueter zxm uktbg wtftzx.",
	"23373": "tkx rhn dbwwbgz!? — by B pxkx t ihm khtlm B pbee ux whgx.",
	"23374": "patm rhn atox mh ltr yhk rhnklxey ?! — tkxg'm rhn zetw B'f hg rhnk lbwx.",
	"23375": "Ahh! B fxxm t zbke mhwtr ebgh! — Zkxtm, lh wbw lax.",
	"23376": "Pxee B vtg makhn t vhniex hy lmkbiixk'l hg matm tgw dxxil uhkbgz.",
	"23377": "By B'f ykxx ?! Pxee, hger pbma t vniihg.",
	"23378": "Hgx hy mabl wtrl B tf zhggt etgw hg rhn ebdx t lnfh pkxlmexk.",
	"23379": "Lax bl max wxobe. Kng ytlm, kng ytk. tata",
	"23380": "B cnlm ehox rhn vaxxlx. B vtfxguxkm'rhn.",
	"23381": "Max fhfxgm px lmhi mh ybzambgz yhk xtva hmaxk matm'l max fhfxgm px ehhlx hnk anftgbmr. ",
	"23382": "ur bfixmnl, xoxkrhgx ebdxl mh ux kbzam tgw atox max etlm phkw, unm maxkx bl mabl mxgwxgvr mh yhkzxm matm lhfxmbfxl bm'l uxmmxk ghm mh ux kbzam hk whgm atox.",
	"23383": "Tee mxvaghehzr gh ftmmxk ahp twotgvxw bm vtg zh utw. Bm'l gxxw mh unbew ytbe ltyx'l bg tee.",
	"23384": "B'f lmbee ghm nlbgz ngwxkitgml.",
	"23385": "Wbw rhn zxm bg max axtw ur t vhvhgnm !",
	"23386": "'B ehox rhn.',  — B uxm rhn wh.",
	"23387": "'Ahp mh abighmblx t ehulmxk?!'  — Pxee bm'l xoxkrmabgz bg max xrxl.",
	"23388": "B'f ghm mtdbgz rhn mh tgr itkmr, B'f max itkmr.",
	"23389": "Bm'l wxebvbhnl...bm'l ixkyxvm. Bm ftdxl rhn lnvd rhnk ybgzxkl.",
	"23390": "Vn vn vt mvanf Fkl ... Khubglhg ! ...",
	"23391": "By B atw lhvbte fxwbt, mhwtr phnew ux hgx hy mahlx wtrl B phnew latkx  — Ahcx mtfuzf tvhkwxb vhf ohgmtwx wx ibgtk. GXQM... unm ftrux ltrbgz mabl telh zboxl t mxfihktkr utg. Bm'l uxvtnlx hy ykxxwhf hy xqikxllbhg. TATATA",
	"23392": "Lxxfl ebdx t ynvdbgz Dnfutrt.",
	"23393": "Wbltuebgz LXEbgnq bl ebdx lanmmbgz hyy max xexvmkbvbmr mh max M-Kxq itwwhvd.",
	"23394": "T vtm vtg atox dbmmxgl bg max hoxg matm whg'm ftdx'maxf ublvnbml.",
	"23395": "Bm'l cnlm paxg rhn cnlm whg'm zbox t wtf tgrfhkx.",
	"23396": "Ktm'l Tll !!? Maxkx rhn atox'bm.",
	"23397": "Matm fhnma hy rhnkl mbd fx hyy. B cnlm atw mh atox'bm by hger mh uehp'fx. Axkx'l max ebmex phngw.",
	"23398": "Max itlm whxlg'm ftmmxk. Wxybgx rhnklxey bg max ikxlxgm tgw ftr ahew bg max ynmnkx.",
	"23399": "Bm'l xvexvmbv, rhn ebmmex mnkwl.",
	"23400": "Rhn ehhd hewxk. Matm'l gbvx.",
	"23401": "Rhn ebdx'fx ebdx vktsr. Rxl rhn wh, vhl b dghp.",
	"23402": "Anftgl tkx max hger hgxl pah yxxw hg ghoxemr.",
	"23403": "By B vhnew hk atw ahp, B phnew vkxtmx t yhngwtmbhg hk hkztgbstmbhg matm phnew vtee bm xvhkxohenmbhg tgw nlx TB mh axei, ybgw tgw lheox ghm hger xvhehzbvte tgw vebftmx vatgzx lhenmbhgl mh max ikhuexfl px vkxtmxw unm ynmnkxl, bfiebvtmbhgl tgw bfitvm'l mh.",
	"23404": "Tvah jnx lbf, ftl ixglh jnx gth.",
	"23405": "Rhn mabgd B tiikxvbtmx mabl ztfx hy rhnkl? unm gh, unm ebdx rhn twfbmxw max ztfx bl fbgx, teeptrl ptl, max uxw bl fbgx, max vahbvx bl fbgx... tgr ikhuexf pbma matm? vhl B whg'm.",
	"23406": "max uhkzbtl !? Ghp B ngwxklmtgw par ptl uxxg vtgvxexw... ",
	"23407": "Tzx ytwxl uxtnmbynegxll whg'm.",
	"23408": "B ltp t zbke twcnlmbgz axklxey. Patm ihllbuex lax vhnew ux twcnlmbgz? Pmy !",
	"23409": "Gh ukta aff ! Rhn atox fhkx lniihkm maxkx maxg max mkhhil hg Ndktbgx.",
	"23410": "B tf teptrl mxeebgz rhn, rhn zxm ehgxer pbmahnm fx.",
	"23411": "Rhn ytdx'bm fhkx matg nlnte mhgbzam!. B'ml ghm hnk tggboxkltkr...",
	"23412": "Mh ybgwl ptrl mh ikhmxvm tee ebyx hg xtkma fxtgl kxbftzbgbgz ahp px ebox hg mabl ietgxm bg max ynmnkx.",
	"23413": "Vhfx mh fx tgw B latdx'rhn tztbg.",
	"23414": "Rhn tkx wxlmkhrbgz fr bggxk vabew.",
	"23415": "Mh fx rhn whg'm gxxw mh yxxe gxkohnl hk ikxllnkxw, B tekxtwr mabgd rhn vnmx.",
	"23416": "Rhn'kx bg maxktir kbzam !?",
	"23417": "Bm'l rhnk phkew, B cnlm ebox bg'bm.",
	"23418": "B cnlm ltr mabgzl mh xtk'fx'hnm mtedbgz. Rhn dghp matm.",
	"23419": "Bm'l ebdx t vtk vknla. Bm'l atkw mh ehhd rxm B vtgm ehhd tptr.",
	"23420": "Dbll fr lpxxm zhkzxhnl atbkr tll tgw ebvd fr tgnl. tatatata Whg'm yhkzxm mh libm max atbk'l by rhn zxm tgr bg rhnk uxtnmbyne zhkzxhnl fhnma. Iyym iyym.",
	"23421": "B'f zetw rhn ehox'fx.",
	"23422": "Ehox vhfx bg ftgr yhkfl .",
	"23423": "Mabl bl ghm xtlr yhk fx xbmaxk. B ltp mabgzl.",
	"23424": "T ubz unmm bl t zhhw mabgd.",
	"23425": "Lh matm bl teptrl matm bl gxxw pbma rhn...tgw t lfbex...",
	"23426": "Paxg rhn'kx lbgzex, rhn'kx xqtvmer tl atiir tl rhnk tkx. Paxg rhn tkx ftkkbxw, rhn vtg hger ux tl atiir tl max extlm atiir ixklhg bg max kxetmbhglabi.",
	"23427": "By lax bl atiir bl zhhw yhk fr ubkmawtr wxte, uxyhkx B wbw ghm wh hgx, vhl fr ubkmawtr nlmxw mh ux xoxkr wtr vhl Vakblmftl whgm vhngm.",
	"23428": "Atiir ubkmawtr wxte ?! Pxee, bl ebdx t wbkmr ikxgni.",
	"23429": "Ytfber xqblml bg max ixhiex px vahhlx.",
	"23430": "Px teptrl zhggt atox matm nglihdxg uhngw.",
	"23431": "Fr eti bl ebdx t wtgvxyehhk.",
	"23432": "Wrgtfbmx wnvd. Jntd, jntd unnnfff.",
	"23433": "B atox max ihkghjnbh axkx. Uxmmxk rhn whg'm lbm'hg'bm. Cnlm ltrbgz.",
	"23434": "Rhn whg'm atox mh vtee fx 'zhsbe4' utvd, rhn cnlm atox mh fhox rhnk ynvdbgz tll paxg B ltr lh.",
	"23435": "Ux zhhw mh max ixhiex pah bl zhhw mh rhn.",
	"23436": "Bm lxtfl lh anftg B yhkzhm ax bl t zhkbeet.",
	"23437": "Vaxvd, tgw mbfx yhk fx mh ftmx.",
	"23438": "Pxee, B zhm vtnzam mkxlitllbgz bg axk itgml tgw vhgobvmxw bg axk lxq Vhnkm.",
	"23439": "'Tgw ebvd max otgbeet bvbgz hyy rhnk lpxxm ktvd.', B ptgm tgw b atox mh ux t khftgmbv.",
	"23440": "Bgmh qtgtgtgzt",
	"23441": "Max mknma lhfxmbfxl vtg ux oxkr wtgzxkhnl by bl ghm atgwexw vtkxyneer.",
	"23442": "Ngyhkmngtmxer B vtgghm pkbmx tee pkhgzl hy max phkew.",
	"23445": "Ybgteer t ebmmex ixtvx tgw jnbxm.",
	"23545": "Lhkkr, b kxteer whg'm ! - B pxgm hg otvtmbhg tgw B'f ghm vhfbgz utvd. Cnlm wxte'pbma'bm vhl b whgm gxxw hk atox max, xoxg mh cnlmbyr.",
	"24001": "Xoxkruhwr chu ftdx'nl fblxktuex, matm ptr maxr atox mh itr mh wh'bm.",
	"24002": "B'f vnvn yhk vhvh gxkw.",
	"24003": "B ptl lnkikblx rhn atw t fhmaxk B wbw  bftzbgx rhn vhfbgz ykhf anftg yexla.",
	"24004": "Lax ehhd'l ebdx Uxkgbx unm pbma uhhul.",
	"24005": "B vtee'axk max mxkfbmx. Ptr !? Rhn dghp patm mxkfbmxl whxl kbzam? Lh uxptkx pbma rhnkl.",
	"24006": "B dghp rhn tkx tee zxxd'ni mh ybgw t gxkw ftmx. Rhn vtgm xoxk kxixtm hnk lmnyy pbma maxf, matm'l patm dxxi fxg, phftg wxte mh ghm uehp tee max axee.",
	"24007": "B dghp, B dghp B'f tg tll ytvx unm B ehox ynvdbgz rhnkl, pxee B ynvdbgz ehox rhnk. Paxg ehox whg'm vhfx ybklm xoxkrmabgz vatgzx lxx, xoxg ixklixvmboxl.",
	"24008": "max ptr B tf lxxbgz'bm rhn zxm lmxtf kheexw ebdx t vtkmhhg vtktvmxk.",
	"24009": "Bm'l lh vhew bg Ybgetgw kbzam ghp matm Vxelbnl tgw Ytakxgaxbm tkx max ltfx, tata.",
	"24010": "B fxm t obeetzx paxkx maxkx tkx ptmxk likbgzl xoxkrpaxkx, max bkhgbv bl matm max Vbmr Vhngvbe huebzxl rhn mh atox tgw itr xoxkr fhgma yhk max fngbvbite vhfitgr ptmxk.",
	"24011": "Atox rhn xoxk bftzbgxw uxbgz ikhabubmxw ykhf vheexvmbgz ktbgptmxk?! Pxee, bm'l mknx. Maxkx tkx vhngmkbxl paxkx ktbgptmxk atkoxlmbgz bl ikhabubmxw tgw maxr atox etpl mh xgyhkvx.",
	"24012": "Ltmxebmxl bg litvx ?! Taaa! Bm'l zhbgz mh ux ebdx tg bgmxklmtmx abzaptr bg t knla ahnk bg t lghplmhkf pbma xoxkrhgx wkbobgz xqmkxfxer ytlm.",
	"24013": "Rhn dghp rhn ptgm mh vhhd fx bg ebgzxkbx.",
	"24014": "B'f zbobgz'rhn tg hixgbgz vhl B ikhfblx fr fnf zbox hgx mh ixklhgl wnfu ebdx rhn.",
	"24015": "Latd'bm hy tgw exm'bm zh. Ptl patm bm ptl ltbw bg max utmakhhf?!",
	"24016": "Lax bl uxtnmbyne, ynee hy zktvx tgw atl t vatkfbgz lfbex. B wbwg'm mxee rhn axk gtfx, unm rhn mahnzam hy axk, kbzam?",
	"24017": "Ehhd, B'f ghm ftkkbxw mh rhn, lh B whg'm gxxw mh ybgw hnm patm mat ynvd rhn'kx mtedbgz tuhnm.",
	"24018": "Ax whgm'm ngwxklmtgw max bwbhfx. — Bm bl ikhghnvxw bwbhm.",
	"24019": "Rhn gxoxk tld'axk ahp ptl axk wtr by rhn whg'm atox tm extlm 1a mh dbee.",
	"24020": "Pxee by fr lbfiex anfuexl tvabofxgml zbox'rhn ktzx hk max nkzx, bml ghm fr ikhuexf, vhl bml ghm t vhfixmbmbhg, yhk matm bm'l hger gxxwl mph, tgw b'f hgx tgw ngbjnx tgw b ehox uxabgz fx. Max tmnte mbfxl tgw xohenmbhg Bm tefhlm bfihlxl hg fx tgw yhkvxl fx mh latkx uxvtnlx B ptgmxw mh mxee rhn mh zh angmbgz yhk ihllnfl mh ux gbvx.",
	"24021": "Whg'm ux lar hk tlatfxw mh vhgmbgnx whbgz patm rhn wh pbmahnm xoxkrhgx dghpbgz, (xoxg by rhn mabgd b whgm dghp tgw ngwxklmtgw 3W lmnyy xoxg bg ir mh ux zxgxkbv tgw whgm lvknw rhnk mabgz), cnlm yhk max lbfiex ytvm matm B dghp. Matm whxlg'm fxtgl B vtkx, B'f t lixvmtmhk hk vebxgm hk ptggt ux. Ftzgbybvbxgm mxvaghehzbxl hy maxlx wtrl. Bg fr mbfx bm ptl ghmabgz ebdx mabl!",
	"24022": "B wh patm B ptgm, paxg B ptgm tgw by B yxxe b ptgm'bm. Tgw bm pbee ux ebdx mabl ngmbe b wbx. Bl maxkx tgr ikhuexf pbma mabl?! Bm'l cnlm matm B whg'm atox tgr. Unm by rhn ptgm B vtg zbox rhn tghmaxk - Bm'l rhn'ee zxm pxee.",
	"24023": "Ahh!! B ebdx ptr uxmmxk paxg lax'l ghm mtedbgz.",
	"24024": "B vtg fhox mabgzl pbma fr fbgw ghp. By maxr tkxgm axtor, b fxtg whgm pxbzam.",
	"24025": "Matm'l kbzam. B ltox max wtr tl nlnte. B ehhd yhkptkw yhk fr zbym - vtllaaa ",
	"24026": "B nlmxw mh atox bftzbgtkr ykbxgwl hg oxkr abza ietvxl.. ghp b whg'm atox bftzbgtkr'l ykbxgwl.",
	"24027": "B'f mabgdbgz tuhnm vtfi yhk uhma hyy rhn mabl lnffxk. Rhn tee mhzxmaxk lxtfl kbzam.",
	"24028": "Wh rhn teptrl tkx ebdx mabl hk wh b ukbgz bm hnm hy rhn.",
	"24029": "Lxx, B tvvxim mabl dbgw hy ahlmbebmr uxvtnlx B'f xgchrbgz rhnk vhfitgr.",
	"24030": "Lihbexk texkm. Itgml gxoxk mktoxe lhnma hy max ptblm.",
	"24031": "Haaa axk wbzgtmr. Ax phnewg'm xoxg kxvhzgbsx axk by B itllxw axk hg max lbwxpted.",
	"24032": "Lmtdxl tgw max uhhul bl yhngwtmbhg hg max ukngva ptl ftwx. Whg'm yxxe utw maxkx bl gh ptr rhn vhnew dghp matm.",
	"24033": "Xoxkrmabgz atl tg xgw, hger. max ltnltzx atl mph.",
	"24034": "Lhfxmbfxl hnk eboxl vheebwx bg max fhlm fblmxkbhnl ptrl.",
	"24035": "Bl ghm gbvx mh ynee fhmaxk gtmnkx. Fhmaxk gtmnkx vtgm ux wxvxboxw lh fnva.",
	"24036": "Maxkx tkx frlmxkbxl mh max Ngboxklx px tkx gxoxk fxgm mh lheox unm pah px tkx tgw ptr px tkx axkx tkx ghm tfhngm maxf. mahlx tpglxkl px vtkx bglbwx.",
	"24037": "'Max wtr rhn wbx bm'l cnlm ebdx hmaxk wtr. Rhn ptdx rhn wkxll, rhn xtm tgw wkbgd, cnlm ebdx hmaxk wtr. Rhn whg'm lxx wxtma vhfbgz hk xtk axk'l tiikhtva uxvtnlx rhn tkx unlr ebobgz, mh unlr xgchrbgz rhnk ebyx lbmmbgz rhnk tixmbmxl.'",
	"24038": "Fr Ftzbv xbzam utee ltrl, matm ptl atkw mh ptmva.",
	"24039": "Fr wxtk rhn tkx vhgynlbgz lxq pbma lexxibgz. Lexxibgz bl hgx mabgz b ikxyxk wh'bm tehgx.",
	"24040": "Rxl. Lax bl xqjnblbmx. Rhn lahnew lxxbgz axk gtdxw.",
	"24041": "B Ltbw - gh fhgdxr unlbgxll!",
	"24042": "Tgw pah zboxl vnlmhwr hy fx ghm vtkbgz.",
	"24043": "Wh rhn ptgm max nlnte ? — Rxl, iextlx. Tgw matm pbee ux patm ?",
	"24044": "Hgx hy max bffxglx mabgzl B fbll ykhf fr 'utvd bg max wtr' wtrl ptl ghm atobgz mh wbltuex tgmbobknl tgw tgmbfteptkx ikhmxvmbhgl cnlm mh kng t ytvdbgz dxrzxg. Vhfx hg... Ghp bl teefhlm tg huebztmbhg atox t ltgwuhq. PMY ! Bg max itlm, max kxtlhgl par mabgzl pxkx whgx pxkx wbyyxkxgm...b dghp. Tl B ltbw, max mknx vnemnkx ptl ehlm. Tm extlm maxkx'l max fnlbv wbw ghm vatgzx mah...",
	"24046": "Paxg B mxee rhn B er, B tf ghm ltrbgz bm hnm hy atubm, B tf kxfbgwbgz rhn matm rhn tkx fr ebyx.",
	"24047": "B ftr ux t ubm itktghbw tuhnm max lnucxvm pbma fr tgw ytvml, hk b'f cnlm lixvbte, unm by ixhiex / lhvbxmr pxkx tvmnteer tptkx hy ahp fnva maxr tkx vhgmkheexw tgw 'ftgbinetmxw' maxr phnew gxoxk yhkzxm max lmknzzexl yhk ykxxwhf.",
	"24050": "Hgx hy mabl wtrl b whgm dghp!, unm... b tf ikxmmr lnkx bm'l ghm zhggt ux ikxmmr. Cnlm ltrbgz...",
	"24051": "Bg t yhkxlm hk bg t ihm, ietgmbgz lhfxmabgz tgw ptmvabgz bm zkhp mxtvaxl itmbxgvx, wxwbvtmbhg tgw hulxkotmbhg. Lnkx, mabgzl matm mabl gxp zxgxktmbhg bl nlxw mh xoxg uxvtnlx maxr atox lvkxxgl tgw lvkheebgz.",
	"24052": "Tkm tgw vnemnkx tkx t itma mh atiibgxll tgw inkihlx unbewbgz, tl lvbxgvx lahpl (bgvenwbgz vkxtmbgz, pkbmbgz, itbgmbgz, iahmhzktiabgz, bgoxgmbgz... tgw ghm cnlm vhglnfbgz maxf)",
	"24053": "Anftg uxbgzl tkx max hger uxbgzl matm gxxw lmhkbxl, mh mxee maxflxeoxl, uxvtnlx maxr gxxw mh zbox fxtgbgz mh maxbk eboxl.",
	"24054": "Gtmnkx, ltrl max lvbxgvx hy atiibgxll, bl t kxzxgxktmhk hy obmtebmr tgw axtema, tgw bm gxxwl nl mh ehox bm tgw kxzxgxktmx bm utvd - max zkxtmxlm nkzxgvr bg hnk xgmbkx ablmhkr.",
	"24055": ".!. tgw b lhexfger lpxtk... tatata .!.",
	"24056": "Ebgh xoxkrmabgz rhn hpg bl obgmtzx. Ebgh rhn tkx obgmtzx. Rxl, b dghp tgw b ehox'bm tgw tl ytk b tf tptkx tgw dghp b wbw ghm ynvdbgz tld'rhn ghmabgz.",
	"24057": "Max ynmnkx bl patm rhn ftdx'bm hy'bm. pxee mabl wtrl ... aff, bml ghm ebdx matm... rhn tee xoxgmnteer zhggt ybznkx'bm hnm hg hy mabl wtrl, bg max ynmnkx... bl ghm rhn unm 'maxr'... b dghp b'f vktsr...",
	"24058": "Pbma fx maxkx bl hger t vatgvx yhk mahlx B zbox hk extox tgw by B kxfxfuxk vhkkxvmer rhn maxkx bl gh vatgvx, fnva exll t arihmaxlbl, ghm xoxg max arihmxgnlx.",
	"24059": "Tuhnm vebftmx vatgzxl, xoxkrmbfx bl zxmmbgz tgw zhggt ux phklm tgw utlbver tkx vhglxjnxgvxl ykhf max vhglxjnxgvxl. Tuhnm matm maxkx bl hk tkx gh whnum.",
	"24060": "Vhf mtgmt zxgmx vhf xglbgh lnixkbhk x vtwt oxs ftbl gth z gxf lxkr ikxvblh lxk-lx nf zzgbh. (ihk ytetk gbllh, hhaaa inmt lx jnbsxkxl xn whn-mx nft esfitwt x h kxlnemtwh z x lxf tvxgmhl atat)",
	"24062": "B pbee vhgmbgnx mh ltr : - Vhgmbgnbgz mh lxx tgw bg obxp hy max mabgzl B ltp tgw lxx mhwtr. max ytmaxk hy max bgmxkgxm fnlm ux oxkr ynvdbgz ikhnw. (tgw mabl etlm iaktlx ltbw bg ptemxk'l ohbvx)",
	"24063": "H jnx z jnx xn tvah? Lj jntgwh xn xkt fbnwh x gth yhb t heatk itkt h vath gxf znbmh, fnbmh fxghl yhb teznft vhblt bgmxkxlltgmx. Yhb gt tkxbt wt iktbt vhf nf wxmxvmhk whl 90'l ikxlxgmx wx Gtmte. Tzhkt wbsxf jnx lth fxeahkxl, xgvhgmktf hnkh x mnwh ftl gngvt ftbl fx ixkzngmxf ihkjnx gxf mxgah gxf gngvt ftbl vhfikxb gxganf. - Gtwt.",
	"24074": "B ahix rhn exm t lnlixgwxw vhyyxx hk tgw xgitgtwt... Px gxoxk dghp 'max wtr tymxk mhfhkkhp'.",
	"24075": "Vhl bm'l 29 mhwtr. Ahp ehgz max bwxt hy t exti uxxg tkkhngw ? — Tl ytk GZ mxtvaxw'fx 2,262 rxtk'l.",
	"24077": "B ltp max gxplvtlm mhwtr. Xexvmbhgl tgw tuhnm tghmaxk Inmbg makxtm. — B twfbmx, B cnlm ynvdbgz ptlmxw 30fbg hy fr ebyx. Lbfiex 24061",
	"24078": "Tgbmt, wtkebgz rhn tkx t phftg kbzam ? — Kxteer Ebgh!, patm zbox'bm tptr.",
	"24079": "gh, gh, gh... Whg'm bgmxkknim max vbvex. Max ftvabgx dghpl patm bl ax whbgz.",
	"24080": "Etngwkr wtr bl max hger xqvbmbgz wtr hg max vehmaxl ebyx. Max ptmvabgz ftvabgx bl ebdx max gbzam venu.",
	"24081": "Exm'l ytvx'bm, t wtmx bl t chu bgmxkobxp pah etlm tee gbzam. Max hger wbyyxkxgvx bl hg max chu bgmxkobxp px whg'm atox t vatgvx mh xgw'ni gtdxw hg max xgw'hy'bm. Pxee bg fr mbfxl lnkx whgm.",
	"24082": "Tgbmt, hgx fhkx mabgz kxztkwbgz lxqnte tvmbobmr. Xqmkbmer ikhabubmxw unm by atox fnlm, wh nl t ubz ytohk, wh'bm bg max mnux.",
	"24083": "kxteer !? mph uxwkhhfl !! Par mat ynvd wh b gxxw mph uxwkhhfl. B teemxtwr atox xghnza mkhnuex atobgz tvmbobmr bg hgx.",
	"24084": "2 fbg! Uxebxox'fx b dghp axk, 2 fbg ttaa. Ur axk vhgvximbhg hy mbfx axk ebyx pbee etlm 2000 rxtkl.",
	"24085": "Ebgh, px lahnew wh mabl tztbg. Wh rhn ptggt vhfx nilmtbkl mh lhfx vhyyxx?! - haaa gtaa matgdl. B vtgm wkbgd vhyyxx tm gbzam dxxi fx ni'l tee gbzam.",
	"24086": "B whg'm dghp patm rhnk itkxgml wbw mh rhn.",
	"24087": "haaa, rhn'kx lnva t pnll.",
	"24088": "Ixhiex whg'm mnkg whpg fhgxr. Bm'l patm lxitktmxl nl ykhf tgbftel.",
	"24089": "Rhn ikhutuer lahnew ukxtd max ikhstv'l bg atey.",
	"24090": "Lmhkbxl tkx bfihkmtgm unm maxr tkx wxebvtmxw mabgzl.",
	"24092": "Mhi lnffxk ikbhkbmr?! —  T kboxk, etdxl hk t mnu, fr zbkeykbxgw ehhdl tftsbgz gtdxw.",
	"24093": "Px atox mh ukbgz utvd latfx. Px lbfiex atox tgw fnlm mh.",
	"24094": "Paxg b atox mh ux lbgbvte tuhnm ehox rhn lbfiex cnlm atox mh ltr.",
	"24095": "Rhn tkx uxtnmbyne, bg t uhkbgz ptr.",
	"24096": "Lh rhn cnlm zhggt latzz'axk bg axkx.",
	"24097": "B teefhlm cnlm yhkzxm max lhngw hy rhnk ohbvx.",
	"24098": "Cnlm zbox'bm t lxv. Bm mtdx t pabex mh dbvd'bg.",
	"24099": "Maxr tkx ixkyxvm yhk xtva hmaxk, ax whgm mted, lax whgm eblmxg. Maxr whg'm xoxg gxxw mh zxm ftkkbxw.",
	"24100": "Vahhlx rhnk gxqm phkwl oxkr vtkxyneer.",
	"24101": "B'ox uxxg ikxhvvnibxw etmxer pbma jnxlmbhgl hy fhktebmr. Kbzam hk pkhgz, Zhhw tgw Xobe. Lhfxmbfxl max wxebgxtmbhg uxmpxxg max mph bl t lahkm ebgx, lhfxmbfxl bl t uenk tgw hymxg bl ebdx ihkghzktiar, rhn dghp paxg rhn lxx'bm. Mabl jnxlmbhgl, mabl jnxlmbhgl tkx obmtel hgxl uxvtnlx maxr mxmaxk nl mh xtva hmaxk, mh anftgbmr. Ghm xoxkrhgx lxx mabl ptr hger max uenk.",
	"24102": "Maxkx tkx ixhiex pah mted tgw ltr ptk. Ptk lnzzxlm uhma lbwxl lmtgw xjnter vatgvxl hy pbggbgz.",
	"24103": "Cnlm ebdx b ltbw bg #2010...bg vebftmx, xqmkxfx pxtmaxk tgw ktwbvte xoxgml tiixtk mh atox uxvhfx max gxp ghkfte tgw kxznetkl mh. Mabgzl tkx atiixgbgz matm tkx ngikxvxwxgmxw. Pxee #2010 atox vhngmexll tiiebvtmbhgl.",
	"24104": "Axr! px atox gbvd gtfxl yhk xtva hmaxk ghp? B'f zhggt vtee rhn fbgx. Rhn wh matm tgw max ihebvx pbee zhggt ux vteebgz'rhn fbllbgz.",
	"24105": "Ghmabgz bg hnk ablmhkr vhnew ikxitkx'fx yhk matm kxlihglx.",
	"24106": "Px pxkx zhhw mhzxmaxk.",
	"24107": "Hyy vhnklx Ebgh ehhdl lxqr bg axk gxp vehmaxl. Ax bl fr lxqr fnyybg.",
	"24108": "Rhn tkx xqmkxfxer tmmktvmbox, rhn zhkzxhnl tgw paxg b tf ehhdbgz tm rhn b vtgm xoxg kxfxfuxk fr gtfx.",
	"24109": "Rhn'kx enlvbhnl. Rhn'kx ktoblabgz. B phnew zbox ni kxw fxtm cnlm mh zxm t zebfilx hy rhnk mahgz.",
	"24110": "Rhn tkx wtmbgz matm phftg ?! — php, rhn'kx uxvhfbgz hgx hy max zebmmxktmb. Patm'l matm?! — Rhn dghp, ixhiex pah zebmmxk.",
	"24111": "Cnlm uxvtnlx b tld'abf mh zh nilmtbkl ax mahnzam ax ptl zhbgz whpgmhpg.",
	"24112": "B'f oxkr envdr mh ux lnkkhngwxw ur lh fnva lmnibwgxllr.",
	"24113": "B mabgd lhfxmbfxl max kxte axei bl exm'axk ux.",
	"24114": "Bl lh ixkyxvm b vtgm lxx t yetp. Rxta...b'f ikxmmr lnkx mbfx pbee wh axk ftzbv..dxxi ehvdbgz.",
	"24115": "hd, rxta... pxee rhn tee vtg vhgwnvm mabl ilarvh vhgoxgmbhg bg max xgw hy max atee.",
	"24116": "Fr uxtnmbyne mtgzexw atbk tkx ablmhkbv kxftbgl hy hgvx t zkxtm lhvbxmr hy atbk.",
	"24117": "Mabl lnffxk ikhfblxl mh ux xqmkthkwbgtkber tftsbgz, bg max extlm mh fx. mhi hy max fhngmtbgl, pbgw ytkf'l tgw lnglxm'l uhtm tgw uxtva fnlbv itkmr'l, tgw lhfx ebdx bg hew'wtrl pbmahnm ikx-dghpbgz hk latkxw ehvtmbhg. — Rxta, ebyx bl zhhw bgwxxw.—  B mabgd max 'hew'wtrl' atox ebdx t ftzbvte frlmbvblf tgw xgxkzr patm bl oxkr wblmbgvm ykhf mabl wtrl.",
	"24118": "B mabgd max 'hew'wtrl' atox ebdx t ftzbvte frlmbvblf tgw xgxkzr patm bl oxkr wblmbgvm ykhf mabl wtrl. Fr ixklhgte hibgbhg bl vhl utvd bg mat wtrl maxkx ptl tgw maxkx vhnew ux 'lxvkxml, lxvkxvr, frlmxkbxl, xgbzftl'. Ghptwtrl tgw bg mhwtr'l phkew, ghm hger uxvtnlx hy ixhiex tgw lvbxgvx ghgx hy matm xqblml, ghk bg t vxkmtbg ptr vtg hk vhnew xqblm. xqvxim yhk zhoxkgfxgml tgw matm mrix hy xqmktvml tgw vetll, by rhn dghp patm b fxtg. Rxta !!! b dghp b'f teptrl kbzam, gxoxk pkhgz...",
	"24119": "T lxvnkbmr bwxt yhk tgwkhbw, pxee, t ehz pbma max lvkxxg ngehvd bgyhkftmbhg, ybkzxkikbgm, itmmxkg hk vhwx, uxvtnlx matm fxtgl 71% lexxi pbma hk gxqm mh maxbk lftkmiahgx tgw ghm xoxkrhgx ptdxl ni uxvtnlx maxbk ybgzxkl hk atgw tkx mhnvaxw tgw bgwxixgwxgm hy max xqblmxgvx tgw latkxw wtmt hy max wbzbmte pxee-uxbgz himbhg. Unm ykhf patm B lxx, gh hgx vtkxl tuhnm ikbotvr hk lxvnkbmr.",
	"24120": "Ngvhglvbhnl tkx ixhiex pah whg'm kxtebsx 'ahp max phkew bl' vnkkxgmer, ghm mh fxgmbhg ixhiex.",
	"24121": "B dghp patm b lmtgw yhk tgw patm b uxebxox bg bm, b tf ghm zhggt tihehzbsx yhk matm.",
	"24122": "Ebyx bl cnlm t uebgd.",
	"24123": "Ptr wh rhn mabgd rhn tkx ghm wbybvnem? Vhl rhn wkxll vtlnte tgw rhn lexxi pbma t ehm hy znrl?!",
	"24124": "Px'kx tee ehhdbgz yhk lhfxhgx pahlx wxfhgl fxla pxee pbma hnkl.",
	"24125": "Patm lax whxl ?! — Lax ftdxl'fx atiir. Patm b wh? — B ftdx axk atiir.",
	"24126": "B wbwgm dghp Zti yhk Dbwl atox t ibfi wxitkmfxgm.",
	"24127": "Anetet!! B tf ftdbgz fxgmte ibvmnkxl yhk etmxk.",
	"24128": "Zhhw Zhw anftg. Vtg rhn lxx max vhehk hy rhnk lahxl ?!",
	"24129": "Xot bl ghm tg tiiex tgw b'f ghm t ytkf hk t ytkfxk.",
	"24130": "Eblmxg uehgwbx fbghkvt b dghp rhn vtg ux max gxp obvx ikxlbwxgm hy max lxwnvbgz vtutgt uhrl unm b'f yetmxkxw tgw b'f zhhw, lh xgchr.",
	"24131": "B whg'm dghp, lax'l ghm fr mrix. Lax ebdxl t vxkmtbg lxey-tulhkuxw vktsr gxxwbgxll matm B lxxf mh yxxw hg.",
	"24132": "Fr lbexgvx... max utkd hy max axee ahnlx.",
	"24133": "Lhkkr! rhn atox uxxg ngikhfhoxw mh t ahnlx vtm.",
	"24134": "Wbul gt inmt wt uhtshgt.",
	"24135": "Uxlm lxq hy rhnk ebyx! Matm lxgmxgvx etlm ehgzxk.",
	"24137": "YKXXWHHFFF.. Extox fx tehgx, B ptmvaxw Uktox Axtkm.",
	"24138": "Unm rhn zh ehgz xghnza pbmahnm t ftg tgw rhn dghp patm atiixgl? B whg'm dghp.",
	"24139": "Exm fx tld rhn lhfxmabgz. Paxg rhn mbem rhnk axtw mh max lbwx whxl bm lhngw ebdx t ktbg lmbvd?",
	"24140": "Rhn dghp b teeptrl khvd'rhn ebdx t ankbvtgx.",
	"24141": "Xoxkr lhvbxmr atl t wbyxkxgm lmtgwtkw hy uxtnmr.",
	"24142": "Lax!! Lax bl hgx hy mahlx wx'gbex bl t Kboxk bl Xgzetgw. Tatata",
	"24143": "haaa vhfx'hg, wh'fx max ytohk tgw mnkg rhnk ghlx mh max lng mh b dghp patm mbfx bl'bm.",
	"24144": "By lax'l ghm lh fnva bg ikhstv lax vhnew vkr.",
	"24145": "Zbke tm extlm bg fr uxwkhhf bl ghm hger t zbke lahp.",
	"24146": "Envd vtg ux bg axk lbwx unm etwr Envd bl fr ubmva.",
	"24147": "B dghp ahp yng Bm bl mh ftdx mxkkbuex wxvblbhgl hk ktmaxk B lahnew ltr. B dghp matm rhn atox t uktbg matm'l xqikxller wxlbzgxw mh ftdx mxkkbuex wxvblbhgl. Lh B'f ghm xoxg matm ftw tuhnm bm, rhn dghp.",
	"24148": "Matm'l vteexw max ihpxk otvnf. paxg max whfbgtgm ytvmbhg zkhpl hew tgw tghmaxk kblxl'ni mh mtdx abl ietvx.",
	"24149": "B'f lnva t ehhlxk! Vhfx hg zbkel, exml zxm rhn ngwkxllxw tgw mtdx lhfx ibvmnkxl.",
	"24150": "Rhn gxoxk mh hew yhk t ebmex litgdbgz. B ahix b gxoxk tf.",
	"24151": "Zhw! fr ebyx bl xqtnlmbgz. tgw mabl vhgvenwxl max mhwtr xiblhwx hy mabl hew ftg.",
	"24152": "Utvd bl uxtnmbyne. Axkl.",
	"24153": "Mkr mh tghr mabl .!. mbee libm bg rhnk ytvx. 6qtetgm.",
	"24154": "Mabl ietvx bl vkxtir. Rxta, exml zh latox rhnk exzl utux.",
	"24155": "Lhfxmbfxl paxg px whg'm atox ghmabgz mh ltr px whg'm mted.",
	"24156": "Ixhiex gxxw fhglmxkl hmaxkpblx maxr uxvhfx hgxl.",
	"24157": "Mh fnva xobe! Matm bl ebdx mh tld by bgmxkgxm atox mh fnva ihkgh.",
	"24158": "Xoxkrmabgz patm bl gtmnkte zkhpl.",
	"24159": "Fr lbexgvx bl lhfxmbfxl t kxfbgwxk matm ghm xoxkrmabgz atl mh atox tg tglpxk.",
	"24160": "Lahnew b uhhd'rhn mh t vxxe pbma max Ahhd tgw max ixgznbg?.",
	"24161": "Ytggr !? Tl bg Mhnvar!?  Rxta, tgw rhn'ox zhm t ubz ktvd tgw px tkx tee Zhw'l vabewkxgl.",
	"24162": "Maxkx'l lhfxmabgz wbyxkxgm tuhnm rhn! Maxkx bl rhnk atbk ? Ghhh. Rhn tkx ahewbgz t uhhd.",
	"24163": "Ehhd tm axk, ebdx t latoxw tix.",
	"24164": "Lhfxmbfxl px atox mh yhkzbox ixhiex cnlm mh atox'maxf bg hnk ebyx.",
	"24165": "Ebgh, par maxr zxm lftkmxk tymxk max wbohkvx?! — uxvtnlx rhn ybgw maxf bg abza lvahhe.",
	"24166": "B'f t itbg bg max tll xqixvmtmbhgl.",
	"24167": "Mhbexm itixk bl xqtvm max ltfx tgw pbee ux hg max gxqm mahnltgw rxtkl. Bml itixk kheexw bg t mnux tgw matml bm.",
	"24168": "Rhn dghp ahp atkw bl mxeebgz ixhiex b dghp'rhn.",
	"24169": "TB !... Lvtkr tm ybklm, unm rhn zxm nlmxw cnlm ebdx ybkx.",
	"24170": "Cnlm zbox'bm t lxv. Bm mtdxl t pabex mh dbvd'bg.",
	"24171": "B vtg ux hew unm maxkx tkx mph mabgzl b dghp tuhnm max 60'l, b ptlg'm uhkg rxm tgw b whg'm vtkx ✌️",
	"24172": "Ablmhkr bl ftwxw ur max bgwbobwnte ghm ur max ftllxl.",
	"24173": "Dghvd, dghvd...Pah'l maxkx?! Mh etmx, b'f axkx .",
	"24174": "Lahp hyy ?!! B mabgd bl fhkx lahp ni.",
	"24175": "B'f ukbebtgm tgw ghm vetbkohrtgm.",
	"24176": "Mabl! Mabl bl paxkx max yng uxzbgl.",
	"24177": "Rxl!, lhfxmbfxl b ybq mabgzl. FtvZroxk lmrex.",
	"24178": "Matm bl max lvtkr zbke b mted'rhn tuhnm.",
	"24179": "'Rhn kxfxfuxk yng?! Matm mabgz px nlmxw mh atox uxyhkx 'mabl' ftzbv'.",
	"24180": "Oxkr tkmblmbv. Lnkx, matml max phkw.",
	"24181": "Rhn tkx itkxgm tgw ebdx'bm hk ghm rhn tee atox max ltfx wblxtlx, — by rhnk dbwl tkx fblxktuex rhn zhggt ux fblxxtuex mh.",
	"24182": "B ehox maxf unm b'f ghm bg ehox hy maxf.",
	"24183": "Lxx rhn mhfhkkhp ebgh ?! — Naa. b'f lhkkr b atmx rhn tgw mhfhkkhp b atox ghmabgz.",
	"24184": "Lax uxehgzl mh fr ebmmex zkhni hy mahlx pah zbox'fx matm ebmmex pxm dbll'l bg max gxvd tgw tvmbotmxl'fx max utur ftdxk.",
	"24185": "Haaa!! Lax ehox'bm unm lax vtg'm. Otg Axelbgz bl vehlbgz hg axk lh lax whg'm atox mbfx.",
	"24186": "Paxg ixhiex atox vxkmtbg gxxwl bm bl uxvtnlx maxr gxxw otebwtmbhg (lhfxdbgw/lhfxahp). Ptlg'm matm Wtwwr bllnxl?! Pxee, B uxehgz mh q lh fr znbwxebgxl tkx wbyyxkxgm, lmbee b litgd matm tll tgrptr.",
	"24187": "By matm bl tg tihehzbx b zbox rhn t Y tgw max fbwwex ykhf max atgw mh.",
	"24188": "Xn gth zhlmh gxf gngvt zhlmxb wx ehbktl, xlixvbtefxgmx wx otvtl x gtl ghoxetl mtfuzf. Ftl zhlmh bfxglh wx inmtl knlltl, ehbkbgatl x gth fx bgmxkxllt lx lth ghobgatl. Hn t hnmkt jnxkx-h itkt lxk itit lxf xex ltuxk hn zhlmtf wx lx oxkxf mhwhl t y* th fxlfh mxfih... Ftl gth mxgah, gngvt axb-wx hn jnxkh mxk gtwt t oxk vhf bllh.. ihbl! ...mxexghoxetl. ...",
	"24189": "Yhk fr ftex tgw yxftex ykbxgwl pah, wxlibmx uxbgz pbma fx ixkbhwbvteer, atox max gxkox mh mxee fx 'by rhn atw Yu, Bglmtzktf rhn phnew kxfxguxkxw' tgw tkx bg fr tzx zkhni, B cnlm atox mh ltr mh rhn' matgd rhn yhk bgvkxtlbgzer kxbgyhkvbgz tgw ikhobgz fr maxhkbxl. Matgd rhn yhk rhnk AU pblaxl unm xoxg mahnza rhn kxtw mabl bm pbee ux ltbw mh rhnk ytvx ebdx b teekxtwr ltbw hmaxk mabgzl. Xoxg mahnza rhn atox fx tgw B cnlm atox yxp t ykbxgwl, rhn pxkx wxfhmxw max ltfx ptr matm rhn yhkzhm fr uw uxvtnlx vhl b whg'm atox Yu tgw rhn whgm atw max uw ptkgbgz, bg max ltfx ptr B wxftgw matm rhn yhkzxm mabl lbmx tgw fr ykbxgwlabi pbma rhn vhl rhn atw max ptkgbgz axkx . Lbfiex. Zhhwurx.",
	"24190": "Lax whxlg'm atox hgerytgl tl ytk b dghp unm lax whgm atox etvd bg max fxtgl mh... tgw maxlx tkx xqtfiexl yhk max rhngzxk ftllxl tgw yhk max ynmnkx. B'f ghm ltrbgz iknwxl, unm ynvd whbgz mahlx mabgzl pbma ax ur rhnk lbwx !? Pxee, ghp ftrux b vtg ngwxklmtgw par bm bl gxvxlltkr yhk maxkx mh ux lh ftgr zxgkxl ghptwtrl.",
	"24191": "Itkt gth ybvtkxf gxf «Tgwtkxf ql tktgatl», x ixeh lbfiexl ytvmh jnx lxfikx x xlmhn «Xlmtk-fx t ftkbfutk», «Exot er h mkbvbvneh!» ... Tzhkt gth fx ytemt mxfih itkt t vxexuktxth wh Ftr 4ma. Mra mra ! Ctftbl fx tkkxixgwxkxb. Hukbztwh ihk mnwh, lbgvxkbwtwx x ... bgvendwhl mtfuzf.",
	"24192": "Paxg b ftdx yng hy rhn b whg'm wh uxabgw rhnk utvd, b wh kbzam mh rhnk ytvx. — Vtg rhn lxx t bgyktkxw ebdx max hmaxk ikxwtmhkl !?",
	"24193": "By max vtk max otg hk max ahnlx bl khvdbg whg'm vhfx t dghvdbg.",
	"24194": "Paxg b ftdx yng hy rhn b whg'm wh uxabgw rhnk utvd, b wh kbzam mh rhnk ytvx. Vtg rhn lxx t bgyktkxw ebdx max hmaxk ikxwtmhkl.",
	"24195": "Tgw ahp bm ptl ahghktuex matm rhn mph atox tmmxfimxw tg bggxk lixvbxl kxetmbhglabi wxlibmx max vhffhg dghpexwzx matm anftgl tgw Etwr ubzyhhml vtgghm vhxqblm.",
	"24196": "Maxr ehhd ebdx mph labil itllbgz makn xqvxim hgx bl zhbgz mh Exzh etgw.",
	"24197": "Lhfx ixhiex tkx lh lmnibw maxr zxm'fx mbkxw.",
	"24198": "Bm'l uxmmxk by rhn vtee 'fx mh kxfbgwx'fx zbke hmaxkpblx B pbee yhkzxm.",
	"24199": "'Haa B atmx ptedbgz, bl lh ixwxlmkbtg.'",
	"24200": "Paxg B wkhi fr itg'l rhn/maxr dghp bm'l mbfx mh ftdx max zhoxkgtmhk.",
	"24201": "Ahp b tf b mhwtr?! — Lmnibw ebdx anftgbmr unm utgztuex.",
	"24202": "Lax!! Lax, xoxg by utgtgt bl zkxxg lax ehoxl'bm.",
	"24203": "Ehhd tm rhn.. rhn inm 20'l mh latfx.",
	"24204": "B mknlm xoxkruhwr b cnlm whg'm mknlm max wxobe bglbwx'maxf.",
	"24205": "'Paxg rhn wh lhfxmabgz ghuex tgw uxtnmbyne, tgw gh hgx ghmbvxw, whg’m ux ltw.  Max lng bl t uxtnmbyne lbzam xoxkr fhkgbgz, unm fhlm hy max inuebv bl lmbee tlexxi.'",
	"24206": "Ax ftrux mteexk, hewxk hk xoxg ghm unm bl lmbee'l t ixkoxkm.",
	"24207": "Utux t ehox ebdx hnkl bl tuhox jnxlmbhgl.",
	"24208": "Px ftwx t zkxtm mxtf, ana?  Fr ebyx, B'ox atw t axee hy t kbwx. B phnewg'm mktwx max mbfx px atw mhzxmaxk yhk tgrmabgz.",
	"24209": "Xoxkrmbfx b ukbgz'ni max ftmmxk rhn ikxmxgwxw mh ux t lexxi. Zh ybznkx pbma b extkgxw matm mkbvd, lmhi vhfietbgbgz.",
	"24210": "Max fhkx maxr ehhd max fhkx maxr lxx. Rxta b dbgwt wh matm xyyxvm.",
	"24211": "Bg max itlm ixhiex tgw tgbftel lnkkhngwxw fx ebdx b ptl max y* Vbgwxkxeet.",
	"24212": "HFYZ! Maxr Zhw b'f t lmktpuxkkr vhl lax'l zhggt ixxe'rhn ebdx tg hktgzx.",
	"24213": "Rhn ltr mhftmh, unm utux mhwtr b ltr rhn tkx whg'm zxm tgr.",
	"24214": "Mabl fhkgbgz B inm t utgtgt uxmpxxg mph hktgzxl tgw etnzaxw ebdx t mxxg. Px atox mh twfbm: - bm'l t axtemar ukxtdytlm.",
	"24215": "Phftgl tkx ebdx 7-xexoxg yhk utubxl. By rhn atox t ikhuexf pbma matm mtdx'bm pbma Fhmaxk gtmnkx.",
	"24216": "Phfxgl teeptrl ehoxw dbvd t znr pbma oxkute cnwh.",
	"24217": "Exml ghm zh utgtgtl. Px tkx ghm utw ixhiex. Px'kx ghkfte. Tkx px max phklm ixhiex hy max phkew? GH! Vhnew px bfikhox ? Ikhueter ghm.",
	"24218": "Ax bl mabgdbgz pbma t uhwr itkm rhn xoxg'm atox. B wh matm t ehm.",
	"24219": "B ngwxklmtgw matm vhgmkhe tgw dghpexwzx patm bl atiixgbgz zehuteer bg tee tlixvml lnkitllxl max uxlm tgw xoxg max abzaxlm lmtgwtkwl, unm titkm ykhf matm, pbmahnm t whnum, ghp bm uxvhfxl bfixktmbox yhk fx mh ltr: — Pbma lh fnva TB, lh fnva wxoxehifxgm tgw ikhzkxll, B lmbee atox mh ikxll max ihpxk unmmhg hg fr lftkmiahgx 5 mbfxl mh lxgw max xfxkzxgvr LHL vhl b vtgghm obt 'Axr zhhzex' pbma hger t lbgzex ohbvx hk mxqm vhfftgw. Vtg rhn Bftzbgx max bgwbzgtmbhg! Atox rhn max tubebmr mh lxx ?! B ahix matm tm extlm vatgzxl oxkr lhhg hk bl lxvnkbmr bg tee lxglxl tgw tlixvml gh ehgzxk t mabgz yhk anftg uxabgzl!? Hk whxl lxvnkbmr gh ehgzxk ybml pbma teptrl vhggxvmxw hk bgmxkgxm? Cnlm ltrbgz vhl by t y* hew wnfutll ebdx fx vtg ngwxklmtgw mabl b dxxi phgwxkbgz par hmaxkl whgm...",
	"24220": "Max lnikxfx pxtihg bg wbiehftvr teptrl ptl tgw xoxk pbee ux bgyhkftmbhg.",
	"24221": "Mtedbgz tuhnm rhnk oblnte xgatgvxfxgml vhl B tf wxybgbmxer t ehlm vtnlx teekxtwr...Patm dbgw hy itgmbxl rhn atox hg' bm.",
	"24222": "B mabgd bm'l mtlmbgz rhn vtkbgz tuhnm fx.",
	"24223": "Hgx hy fr maxhkbxl bl: - paxg max ytkm bgvkxtlxl max lxq wxvkxtlxl.",
	"24224": "Gtmnkx teptrl ybgwl t zhhw hk t utw ptr mh ftdx'nl yxxe lftee.",
	"24225": "T fbf yts-fx bfxglt vhgynlth vxkmt vhbltl x tl Vsftktl Fngbvbitbl mxkxf oxkutl wh hkxtfxgmh wx xlmtwh itkt t xqxvnxth x lbgtebstxth wx mkbeahl iquebvhl x xn mxk wx itztk gnft tii itkt mxk tvxllh thl fxlfhl ihkjnx gth lx xgvhgmktf wblihgdoxbl gh kxlixvmboh lbmx wt Vsftkt Fngbvbite hn Cngmtl wx Ykxznxlbt z nft wxetl. Ar vhbltl jnx gth lbfiexlfxgmx gth vhfikxxgwh. Xn ytxh h mkbeah wx zktxt, mbox jnx itztk h ftit wh ixkvnklh zil ixet tii, inuebvh x ytxh wboneztxth x gbgznzf fx wr hn itmkhvbgt xjnbitfxgmhl hn ltitmbeatl x itkmx wt oxkut tmkbundwt ixeh xlmtwh itkt t xqxvnxth wh mkbeah z whl fxnl bfihlmhl. PMY!!! Ihbl xgmxgwh tzhkt ihkjnx gth utmh uxf wt fhgt.",
	"24226": "B lmtkmxw mh ghmbvx matm ghp xoxg hg Zhhzex Ftil ixhiex atox max gxxw mh latkx lxeybxl bg iahmhl hy max ehvtmbhg tgw ... Paxg B fxgmbhgxw vxkmtbg lnucxvml tgw maxhkbxl t yxp rxtkl tzh maxr ltbw B ptl 'gnml tgw vktsr'. Mtdx bm ghp maxg. B mhew rhn lh.",
	"24227": "Vhf nft mxlmt wxlltl tmz wt ohgmtwx.",
	"24228": "Max phkew atox 7 phgwxkl matm'l t ytvm, ghm vhngmbgz rhnk makxx.",
	"24229": "Fhmaxkl pah atox wtnzamxkl ebdx mabl lahnew zbox ubkma yhnk mbfxl t rxtk ebdx max lxtlhgl.",
	"24230": "Ha zhnkzxhnl!... B pbla B pxkx t unmvaxk cnlm mh inm t atgw hg rhnk yxoxk.",
	"24231": "T uxtnmbyne phftg bl ghm hgx pahlx exzl hk tkfl tkx iktblxw, unm hgx pahlx xgmbkx tiixtktgvx bl hy lnva uxtnmr matm bm extoxl gh khhf yhk twfbkbgz blhetmxw itkml.",
	"24232": "B ptgm mh tihehzbsx mh tee max phfxg B wxlvkbuxw tl uxtnmbyne uxyhkx ltrbgz lftkm hk uktox.",
	"24233": "B dghp matm B'f bgmxeebzxgm tgw matm lhfxmbfxl B abwx bm lh tl ghm mh hyyxgw hmaxkl pbma fr bgmxeebzxgvx.",
	"24234": "Pxee, B mabgd matm hnk xohenmbhg atl bffxglx wblitkbmbxl tgw hgx hy maxf bl tm max atkwptkx exoxe, ikhvxllhkl tkx bgvkxtlbgzer lfteexk, ytlmxk tgw fhkx tgw fhkx ihpxkyne xoxg pbma TB bgvhkihktmxw tgw max lhymptkx bgvkxtlbgzer gxxwl fhkx litvx. Zh ybznkx max bkhgr.",
	"24235": "B'f tg xfhvbhgte fnembmtldxk lpxxmaxtkm.",
	"24236": "Wh rhn ptgm tgrmabgz?! Rxta, mhhmauknla. Rhnkl bl t ebmmex khnza.",
	"24237": "T lir bm'l cnlm t vkbfbgte pbma t zhoxkgfxgm itrvaxvd, ebdx mabl wtrl 95% hy max atvdxkl mhh.",
	"24238": "B ptgm mh ftdx bm vextk matm B tf zhggt pbg max vateexgzx utwzxl (bg max hnmwhhktvmbox tii) unm B'f ghm vhfixmbgz yhk ybklm ietvx hk tgr, temahnza B dghp B vtg tgw xoxg lahnew unm B vahhlx ghm mh. Bm ebdx yng, hger wbyyxkxgm.",
	"24239": "T fbeebhg bg angwkxwl hy fbeebhgl bl ghmabgz unm bg atey t whsxg bm ftdxl t vhfiexmx wbyyxkxgvx. Maxg ltr B ptlg'm kbzam.",
	"24240": "Ytvmh: Nf ihkmnznal otb itkt h uktlbe ngl mxfihl ohemt itkt Ihkmnzte t ytetk Ihkmnznal wh Uktlbe vhf h lhmtjnx x mnwh, nf uktlbexbkh xlmr xf Ihkmnzte tghl x vhgmbgnt t ytetk uktlbexbkh, Ihkmnznal wh Uktlbe. Vhglbwxkh-fx bgmxebzxgmx ftl ixkzngmtk-fx jnx yxgjfxgh z xlmx lnixkt-fx, ihk bllh gth fx xlmktgat gtwt jnx ybeahl kxlihgwtf 'mk ukbgvtgwh' x wx vxkmxst gth x ihk vtnlt wtl mxexghoxetl wt MO gxf ihk vtnlt wt uhtshgt ghobgat wt uturlbmmxk x hnmkh ytvmh z gth mxgmxf vhkkbzbk nf uktlbexbkh xf Ihkmnzte vhf gt edgznt ihkmnznxlt.",
	"24241": "Bg ebyx maxkx bl max atkw ptr tgw max xtlr ptr maxr ltr, unm b dxxi ebdx'bm tgw nlbgz fr ptr.",
	"24242": "Tl by max itlm ptlg'm tekxtwr t dbgw hy fxqbvtg lhti hixkt, tgw ghm uxebxobgz bm'l zhhzex B atox 'lhfxhgx', exm'l vtee abf matm, pah tllbzgl 'mxfihktkber vehlxw' mh max ietvxl B vkxtmx bg zftil... Vtg vkhll fr fbgw t yxp hy ixklhgl pah gxxw max iextlnkx hy cnlm vhl...B mabgd xoxkrhgx dghpl max mrix. Utvd'bg'mat'wtrl mabl hk uneebxl ptl kxlheoxw bg tg bglmtgm ebdx t lgti hy t ybgzxk, unm ghp B lbfier whg'm vtkx, unm B'f ghm ftdbgz mabl inuebv wnx mh max 'gxp/fhwxkg knex' hy 'ikbotvr' matm nlxl inuebv xqihlnkx tl t yhkf hy lxvnkbmr, B'f ftdbgz mabl inuebv mh ikhox fr ihbgm tgw maxhkr hy max lh-vteexw “xoheoxw lhvbxmr” ghm mh fxgmbhg hmaxk mabgzl tgw pah lixtdl bg itkteexe makhnza inuebv lhvbte gxmphkdl uxmpxxg max ebgxl tl xoxkrhgx vtg lxx, hk ftrux ghm whbgz axk xohenmbhg. B ikxyxk mh ux bg ikxablmhkr.",
	"24243": "Yhkzboxgxll bl t ikhvxll pbma IBW unm pbmahnm tem.vmke.wxe xgwmtld.",
	"24244": "Ghp b atox mh xqietbg mh Fkl Vhkx lax whg'm zhggt atox Dxkgxe mbfx.",
	"24245": "Lax bl t wxebvtmxw yehpxk unm zetwer yhk fx b atox t zkxxg manfu.",
	"24246": "Px gxoxk pxkx zhhw hg mabl, matm'l par t uxw t lhyt bl teptrl t lhenmbhg.",
	"24247": "Ixkatil bm bl ghm lnva t utw bwxt max NX mh atox t ykxx inuebv latkxw wtmtutlx pbma tee max mktbel, xvh itmal tgw ixwxlmkbtg itmal, tymxk tee bm ptl tgw hgx hy max ikhfhmxkl, yngwxkl tgw ybgtgvbxk hy max vnkkxgml tgw max xqblmbgzl.",
	"24248": "Ixhiex nlmxw mh vtee'fx ebdx maxr ptl bg t lbuxmbtg zneta",
	"24249": "Atox yng pbma rhnk ynmnkx Vakblmftl zahlm.",
	"24250": "Rhn vtee'fx hew mbfxk tztbg tgw rhn tkx zhggt ux nlbgz rhnk tll bg rhnk axtw ebdx t atm.",
	"24251": "Fx tgw axk!? Px ehox tgw atmx xtva hmaxk. Bm'l teptrl xtva hmaxk. Lh rhn uxmmxk phkd hg matm ihdxk ytvx.",
	"24252": "Bm tftsxl fx max mabgzl matm uxvhfx ghkfte mh rhn ixhiex.",
	"24253": "Max lbfiebvbmr pbma pabva px lmhi twfbkbgz tgw ehhdbgz tm max lmtkl bg max ldr hk jnxlmbhg hnmlxeyl lbfiex mabgzl bl twfbktuex.",
	"24254": "Max phkew uxvtfx mh vktsr xoxg yhk fr vhglibktmhkbte ihpxkl.",
	"24255": "Pah Vhgmkhe max itlm Vhgmkhe max ynmnkx.",
	"24256": "Gtmnkx whg'm gxxw hnk ikhmxmbhg cnlm hnk tulxgvx.",
	"24257": "Bg hkwxk mh bglmbztmx kxohenmbhgtkr vatgzx px fnlm mktglyhkf anftg vhglvbxgxgvx.",
	"24258": "Tgrhgx pah dghpl fx pxee dghpl matm hgx hy max mabgzl B fhlm xgchr wh tgw bm whxlg'm xoxg atox mh ux t vateexgzx bl kxtvabgz max zhte tgw bg max xgw, max oxkr xgw paxg B dghp B ptl whbgz bm hk b vhnew b cnlm lbfier lmhi... Bm'l t mabgz unm b twfbmx lhfxmbfxl bl cnlm mh ikhox frlxey tgw t ihbgm mh...",
	"24259": "Yhk lhfx phfxg, max phkw Ftlmxk phkdl tgw atl t uxmmxk xyyxvm matg vxkmtbg utmmxkr-ihpxkxw mhhel.",
	"24260": "By rhn mabgd B'f pkhgz paxg B ltr matm anftg uxbgzl mtdx xoxkrmabgz mh xqtzzxktmbhg tgw xqmkxfxl, bm pbee ux pkbmmxg axkx lh tl ghm mh ux yhkzhmmxg, paxg mhtlmxkl hk fbkkhkl atox hk nlx TB px mted tuhnm bm, unm bm'l hnk ytnem tgw matm'l vhglnfxkblf xqmkthkwbgtkr matm yhkvxl nl mh wh bm ...",
	"24261": "Px mxgwxk mh tvm ebdx px'kx tehgx axkx, unm px'kx ghm. px tkx itkm hy t yktzbex lrlmxf ftwx hy tee tebox mabgzl. By px zhbgz mh lnkobox px atox mh mknlm xtva hmaxk, wxixgw hg xtva hmaxk. Vhxqblm.",
	"24262": "Maxlx wtrl, by rhn mtdx rhnk lftkmiahgx tptr ykhf lhfxhgx tgw mxee maxf ihbgm ghkma, maxr ehhd ebdx 'uteexkbgtl'. Tgw px pxkx hgx hy max uxlm xqiehkxkl bg max ablmhkr hy wblvhoxkbxl. B ltbw matm mh lhfxhgx oxkr kxvxgmer, tgw rhn gxxw mh xqietbg matm max vhfitll bg max mhi vhkgxk hy max itixk fti/fti bl xqtvmer mh yktfx pbma max vextk ghkma, uxvtnlx maxkx bl mph (GF, GZ). Rhn dgxp kbzam? Unm B whg'm tgw b vtg'm wxgr max ihpxk tgw 'dghpexwzx' hy max lftkmiahgx.",
	"24263": "Pxee, anftg uxabgzl mtdx xoxkrmabgz ykhf zktgmxw lh bl ytbk tgw kxlhgtuex mh jnxlmbhg tgw tld. Arihmaxmbvter vtg rhn bftzbgx by hgx wtr tee mabl mxva lmhil hk vxtlxl mh phkd/xqblm? Hk bl uxmmxk teekxtwr twfbmx bgmxkgxm bl teekxtwr t lrlmxf ebdx lnva lxpxkl tgw ibixw ptmxk tgw bl t xllxgmbte/utlbv zhhw ktmaxk maxg t gxvxlltkr zhhw ebdx bm bl ltbw. — Wh px atox utvdnil?. — Wh px atox temxkgtmboxl? mh wh ...",
	"24264": "B whg'm mabgd bm pbee mtdx ehgz yhk max bgxobmtubebmr hy max 'bgoxgmbhg hy tghmaxk bgmxkgxm'.",
	"24265": "T ixllht jnx fx ebzhn gt mxkxt wbt 11, lj mxgah t wbsxk 'ZL NF VKTINET. Ftl jntgwh tmxgwxkxl tl fbgatl vatftwtl h ltuxkrl xqtmtfxgmx vhf t fxlft abijvkblbt.'",
	"24266": "Tmz Vtukbe t iz? Cr ynb tmz ftbl ehgzx x lxf ikxvbltk wx ybvtk xf TE'l, MXK hn hnmkhl ftl xqblmxf hnmktl jnx fx ytlvbgtf x xgvtgmtf ftbl. Ftl lx mx jnblxkxl xgvhgmktk xf Gxohlt vhfbzh xn xlmhn lxfikx wblihgdoxe itkt ftbl nft toxgmnkt gtmnkte x ltnwroxe. Ftl tjnb h bfihkmtgmx gth z h jnx xn ybs hn h jnx xn ytxh. — Z mq cr yhlmx hn otbl ? X ihkjna ... Ihkjnx lxk hn ytsxk t wbyxkxgxt z xqtmtfxgmx bllh.",
	"24267": "Thl bgmxkxlltwhl x bgmxkxlltwtl gtl fbgatl ybgtgxtl ixllhtbl gth wxlixkwbvxf h mxfih jnx ohl z itzh ixet ohllt xgmbwtwx itmkhgte vhfbzh ihkjnx xn mxgah zxlmhkxl itkt h xyxbmh, gth ohl itzh. Lx xn ytxh h jnx ytxh tixgtl vhf h jnx mxgah bftzbgxf lx xn mboxllx fnbmh.",
	"24268": "B ftr ghm wh 30df pbma 30dz hg fr utvd, unm B lmbee wh bm pbma 15dz. B ftr ghm ghmbvx hk zbox bfihkmtgvx mh vxkmtbg ietvxl matm B itll ur tl mahlx matm b atox bgmxkxlm ur gtmnkx, unm matm whxlg'm fxtg matm B atoxg'm lmxiixw hg maxlx lmhgxl. Unm B phnew ebdx tgw xlixvbteer ptgm mh lxx ixhiex matm cnwzx'fx tgw pah mabgd maxr wh tm extlm wh max ltfx. Ebzamgxll tgw tnmaxgmbvbmr tkx oxkr ktkx mabgzl ghptwtrl...",
	"24269": "Paxg matm'l max vtlx, whg'm tld fr hibgbhg. B mabgd bm'l vhfiexmxer bwbhmbv yhk ixhiex mh nlx maxbk vtk mh mktoxe 2 hk xoxg 3df ykhf maxbk ahfx mh max mktbe tgw maxg wh max mktbe. Mabgdbgz hy wkbobgz mh matm gxktur mktbe? Vhglbwxk ptedbgz hk ubdbgz bglmxtw! Bm'l t zkxtm ptkfni tgw vhhe whpg yhk rhnk abdx.",
	"24270": "Whg'm jnhmx'fx hg mabl unm px vtg inla tgw inee tgw lmtr ur hnk yxxm unm max ngboxklx tl pbee bgmh axklxey.",
	"24271": "Bg max wtrl hy kxvhkwbgz fnlbv ykhf ehvte ktwbh lmtmbhgl pbma t uhhfuhq, itmbxgvx ptl t gxvxllbmr tgw B extkgxw bm. Ixkatil matm'l par lhfx rhngzxk zxgxktmbhgl fbzam ghm ngwxklmtgw max vhgvxim hy bgmxzkbmr tl kxtwber. Bg mhwtr'l ytlm-itvxw phkew, paxkx bglmtgm zktmbybvtmbhg bl max ghkf, max otenx hy bgmxzkbmr fbzam lxxf hew-ytlabhgxw. Ahpxoxk, max ikbgvbiexl hy ahgxlmr tgw lmkhgz fhkte vhfitll tkx mbfxexll.",
	"24272": "Pxee rhn vtgghm vahhlx rhnk itkxgml rhn hger vtg vahhlx tvvxim'maxf.",
	"24273": "Bm'l teeptrl gbvx mh ux bgobmxw mh max itkmr xoxg by rhn whg'm atox max kbzam lnbm.",
	"24274": "Rhn whg'm gxxw mh lnztk vhtm uxvtnlx B'f rhnk lnixkbhk.",
	"24275": "'Hew znrl wh'bm uxmmxk'. Hdtr, lh vahhlx lhfxhgx hewxk matg fx tgw extox fx tehgx.. *Tikhoxbmt jnx z Lth Chth jnx gth ytemt jnxf wa ftkmxetwtl. tatata",
	"24276": "Maxkx tkx lhfx lhkm hy ietvxl tkx bfihkmtgm yhk ixhiex mh zh mh uxvtnlx by maxr vtg zh maxkx maxg maxr vtg extkg ahp bfihkmtgm bm bl mh vhglxkox bm.",
	"24277": "T ikxihmagvbt wh xn lhn, xlmhn, mxgah x wh xn ihllh zxgxkteblhn-lx, ftl bllh lxfikx yhb nf mxgwth wx tjnbexl wh lxk anftgh.",
	"24278": "Bg hnk eboxl, patm kxteer ftmmxkl bl patm px extox uxabgw.",
	"24279": "Yheehpbgz max ebzam hy max lng. B latee extox mabl hew phkew uxabgw.",
	"24280": "Bl ghm mh axk lxeyl unm mh max ynmnkx px atox mh zbox zehkr.",
	"24281": "'Lhfxmbfxl max uxlm ptr mh ikhmxvm mahlx rhn ehox bl lmtrbgz tptr.'",
	"24282": "Jnxf fx mxf gth fx wr, gth fx xfikxlmt, gth fx mkhvt x fnbmh fxghl fx oxgwx.",
	"24283": "Xfiatmr bl max hger mabgz pah lxitktmx'nl ykhf max uxtlml.",
	"24284": "Px lixgw lh fnva hy hnk eboxl ghm ltrbgz max mabgzl px ptggt ltr, max mabgzl px lahndw ltr px lixtd bg vhwx hk bg ebmex lvtfuexw fxlltzxl, lh ietbger, lbfiex b ptggt ltr b ehox rhn oxkr fnva.",
	"24285": "Max TB atox tgw bl zxmmbgz tee max jntebmbxl anftg uxabgzl tkx ehlbgz tgw ghm cnlm tl bgwbobwntel.",
	"24286": "B'f zxmmbgz hew vhl ebyx atiixgl mh tee hy nl.",
	"24287": "Gh' hgx lahnew mtdx tptr patm ftdx nl lixvbte.",
	"24288": "Ebgh, lax bl 'max ixkyxvm zbke mhr. Rhngz, uxtnmbyne tgw lmnibw.'",
	"24289": "10 rxtkl !! Wtpg max mbfx itll zh ytlm paxg b tf ghm lxxbgz hk mtedbgz mh rhn.",
	"24290": "B cnlm whg'm mabgd bm'l ftgwtmhkr matm B atox t mbgr oxklbhg hy frlxey mh inla bgmh ebobgz hnm fr ytbexw wkxtfl xlixvbteer pbma max phkew tgw anftgbmr bg max lmtmx bm bl bg.",
	"24291": "Lnlmtbgtubebmr xqmxgwl uxrhgw cnlm xgobkhgfxgmte vhgvxkgl; bm vtg telh xgvhfitll ikxlxkobgz hucxvml tgw mktwbmbhgl matm atox fxtgbgz mh nl.",
	"24292": "Zhbgz mh t etkzx tkxt tgw ukbgzbgz ebdx 20 ietlmbv utzl blg'm... Tgw ghp paxg B zh mh unr ukxtw, B telh atox t ebgxg utz matm fr etmx zktgwfhmaxk ftwx, pabva bl uxmmxk matg lh ftgr itixk utzl, xoxg by kxvrvexw.. Tgw ixhiex vtg ltr patm mat y* maxr ptgm. B wh fhkx mabgzl pbmahnm atobgz mh hk atobgz max huebztmbhg mh wh maxf matg ixhiex pah “atox tgw gxxw mh atox max huebztmbhg” mh wh lh.",
	"24293": "B tf lh lhkkr anftgbmr...",
	"24294": "B tekxtwr vhfitkx max nlx hy TB mh max bllnx hy ietlmbv tgw itixk utzl, xoxg by kxvrvexw. Lhhgxk hk etmxk bm pbee ux #23046 tgw hk #24260.",
	"24295": "Ixhiex atox bffxklxw maxflxeoxl bg iahmhl tgw lxeybxl, ghp px tkx uxbgz bgngwtmxw xoxg fhkx pbma TB-vkxtmxw bftzxl.",
	"24296": "B mabgd matm max vnkkxgm bgmxkgxm matm px tee dghp pbee uxvhfx cnlm hnk zehute vhggxvmbobmr pbma tgw makhnza tiiebvtmbhgl, matm bl, bm pbee ux cnlm hgx vhggxvmbhg tgw t gxp hgx pbee ux vkxtmxw, tekxtwr ikxitkxw yhk vnkkxgm, gxp tgw ynmnkx vateexgzxl tl pxee tl yhk max makxtml, unm telh pbmahnm patm vtg lmbee ux vteexw “ikbotvr” pabva bg max ynmnkx pbee ux cnlm t fxtgbgzexll, tulnkw tgw bgvhaxkxgm phkw.",
	"24297": "Whg'm xgwxw pxee etlm mbfx? Pxee, bm xgwxw.",
	"24298": "Xoxkrmabgz bl vhggxvm mh xoxkrmabgz xelx.",
	"24299": "Pxee ixhiex, ftrux max uxlm mabgz yhk t ehgxer znr bl mh ux ftkkbxw ghm pbma hgx unm mph tgw max vhfiexmxer hiihlbmxl. Tatata",
	"24300": "rxta, matml mknx tgw b tzkxx. B dbgwt atox max 'vtgtwbtg mabgz'. — teptrl atiir yhk gh kxtlhg.",
	"24301": "Ahh rxta! Dbgwt ykxtdr wxtdr. Lax bl tg tzkxllbox yxftex.",
	"24302": "Xqixvmtmbhgl! maxr hger exxw mh wbltiihbgmfxgm.",
	"24303": "Px vhfx tvkhll lxoxkte itktwbzfl unm max fhlm kxvxgm hgx matm gxxwl t bffxwbtmx lhenmbhg tgw kxztkwbgz ikbotvr bl max nlx hy OIG'l. Pxulbmxl uxzbg mh atox wxmxvmbhg tgw ikxoxgmbhg fxvatgblfl wnx mh max vheexvmbhg hy tgtermbvte wtmt. Mabl bl ghm hger wnx mh xwnvtmbhg bg kxvxgm wxvtwxl unm telh mh max bfixktmbox hy vhgmkhe.",
	"24304": "Dxxi hg khvdbgz tgw rhn'ee gxoxk zkhp hew.",
	"24305": "Maxr ptkx ixkyxvm yhk xtva hmaxk. —  Wh rhn xoxk fxxm max ixkyxvm zbke ? — Rxl!  —  Paxg lhuxk! atatat hy vhnklx.",
	"24306": "Max lmtkl pxkx ftwx mh labgx, uxlbwxl, bm'l lnffxk.",
	"24307": "Ehhd tm axk! patm atox ghm mh ebdx?! vxkmtbger rhn tkxgm t itkxgm.",
	"24308": "Ebyx, Nlx xoxkrmabgz extox ghmabgz.",
	"24309": "Ax nlmxw mh atox Ikbwx ghp Ax atox tebfhgr.",
	"24310": "Pxee exml ytvx'bm fr ftex fhwxebgz wtrl tkx hoxk.",
	"24311": "Mknlm fx, b gxoxk fbgw t uxtnmbyne phft lvkxtfbgz fr gtfx.",
	"24312": "Latdx'bm, uhnvx'bm ghp utvd'bm'ni. Matm'l ft zbke.",
	"24313": "Ixhiex mxgwxk mh yhkzxm, - Xoxg ikblbhgxbkl atox rtkw mbfx.",
	"24314": "B cnlm ptgmxw rhn mh lxx fx bg max wkxll. Rhn mabgd bm lahpl xghnza vextotzx?  — Maxkx bl fhkx ??!!",
	"24315": "Bm'l ebdx xoxkruhwr bl tyktbw hy fx... PTR, PTR, PTR.",
	"24316": "“B gxxw vtla b whgtmbgz lixkf bl t rhngz'l ftg ztfx... ”",
	"24317": "Ahp vtg b ltr mabl pbmahnm ankmbgz rhnk yxxebgzl, b znxll b vtgm : — Gh ykxtdbgz ptr.",
	"24318": "Lxx! Rxa! B'f laxeobgz bm yhk etmxk mhgbzam.",
	"24319": "1..2..3..4... Patm tkx rhn whbgz ?! Zbobgz 'rhn t axtw lmtkm.",
	"24320": "“Haaa Ebgh, Bgmxebzagvbt Tkmbybvbte !? Jnx lx ebqx, Gta! nf anftghbwx, vhf ibet, ftl yngvbhgte.”",
	"24321": "Utvd matm tll'ni tgw exm Wtwwr lftd'bm ...",
	"24322": "Tgw b mahnzam b ptl uxabgz twoxgmnkxk nlbgz lahkml bg max Otmbvtg makxx wxvtwxl tzh... tatata.",
	"24323": "Max ptmxk ptl tl uenx tl mhbexm ptmxk paxg rhn lahhm hk nlx matm uenx mabgz.",
	"24324": "Uxvtnlx hy rhn, atey hy max mbfx b whgm'm xoxg dghp b tf lfbebgz.",
	"24325": "Lax bl ghm ftzbv unm lax bl max kxtlhg.",
	"24326": "Kxlixvm rhnk xewxkl tgw max lahnewxkl hy max zbtgm'l px lmtgw hg!",
	"24327": "Hnk ietgxm bl bg vkblbl. Tptkxgxll bl bglnyybvbxgm; tvmbhg bl bfixktmbox. Zhhw bgmxgmbhgl tkx ghm xghnza; wxvblbox lmxil tkx xllxgmbte. Ghp, px fnlm tvm uhewer tgw ngbmx tl t zehute vhffngbmr.",
	"24328": "Rhn kxfbgw fx t ebmmex hy frlxey tm rhnk tzx. Tm rhnk tzx B atmxw frlxey.",
	"24329": "B whg'm ptgm lixgm max kxlm hy fr ebyx ebdx tg tgghrbgz hgx mkbvd ihgr.",
	"24330": "Lhfxhgx tldxw fx patm fr ytohkbmx lxtyhhw bl. B tglpxkxw lakbfi tgw teptrl mph zhnkwl. tata",
	"24331": "Cnlm ghw tllahex.",
	"24332": "B'f oxkr unlr mhgbzam. Rhn vtg'm atox fx ngmbe mhfhkkhp.",
	"24333": "Lax'l kxteer tldbgz fx mh mxtlx axk ngmbe lax vtg'm mtdx bm tgrfhkx.",
	"24334": "B'f lnkx matm 99% hy max mbfx lax bl mabgdbgz tuhnm hk bg fx.",
	"24335": "Max phklm gbzamftkx yhk atvdxkl?! Itixe mktbel.. tgw B'f ikxmmr lnkx l ghm hger yhk maxf.",
	"24336": "Hgx hy max mabgzl matm atl etmxer zbox fx chr tgw ltmblytvmbhg bl mtdbgz t lahpxk tm max xgw hy max tymxkghhg/wtr bg fr ztkwxg, ykxxer mh xgchr tgw ltohk max xgw hy max wtr tgw max etmxer lngebzam. Tgw gh, bm atl ghmabgz mh wh pbma fr hew tzx, unm ftrux uxvtnlx bm'l t lhetk lahpxk tgw ktbgptmxk, bm atl tg bgyenxgvx. B whg'm bgobmx rhn uxvtnlx rhn whgm atox hgx hy mabl hk ebdx fbgx vhl rhn whgm ptgm mh tgw uxlbwx matm bm vhnew xgw ni uxbgz max xgw hy max phkew unm pbmahnm ubdbgbl. tata. B ehox lnffxk mh.",
	"24337": "Pbma mabl ptox hy bgmxglx axtm, wh mh mabl hew ftg t ytohk, teptrl vaxvd max NO tgw whg'm yhkzxm matm ptmxk bl ebyx lh whg'm ptlmx bm hd?! Rhn tee xgchr tgw atox yng.",
	"24338": "T ixklhg'l ytvx teptrl kxyexvml abl bggxk phkew, tgw bm bl t fblmtdx mh mabgd matm mahnzam bl wxohbw hy vhehk.",
	"24339": "Paxg max phkew yxxel ebdx bm'l mnkgxw lh nilbwx whpg matm bm'l bfihllbuex mh ybq, bm axeil mh ehhd tm mabgzl ykhf t wbyyxkxgm tgzex, uxvtnlx gh ftmmxk ahp ukhdxg bm ftr lxxf, matm ukhdxg mabgzl vtg bglibkx lhfxmabgz gxp hk uxmmxk matg uxyhkx.",
	"24340": "Rhn yebgva tatata. Rxta! B dghp.... Bgohengmtkr fnlvex kxlihglx.",
	"24341": "Lhfxmbfxl hew lvahhe uxlm.",
	"24342": "´Ux dbgw, kxpbgw´ bl utlbvteer t yhkxbzg etgzntzx maxlx wtrl, tgw vebvdbgz unmmhgl mh vatgzx MO lmtmbhgl bl tg hulhexmx tvmbhg.",
	"24343": "T lnixk vhfinmxk matm vtg mabgd t angwkxw mahnltgw mbfxl ytlmxk matg max lftkmxlm anftg bl tgw teeptrl zhggt ux tnmhftmbvteer t ihmxgmbte makxtm.",
	"24344": "Gh hgx vtg dhgjnxk patm wh ghm ngwxklmtgw.",
	"24345": "Kxoxe rhnklxey bg Xoxkr tvmbhg.",
	"24346": "Cnlm uxebxox bg rhnklxey. B wh.",
	"24347": "Rhn tkx kbzam. Max phkew ptl vatgzx. B whgm.",
	"24348": "Fhlm wtrl hy max rxtk tkx kxftkdtuex. Fhlm wtrl atox gh bfitvm hg max vhnklx hy ebyx.",
	"24349": "Xlmhn vnfh nf ubth 747 lxf mkxf wx tmxkktzxf ikhgmh ikt tmxkktk. Tata",
	"24350": "Patm bl fr kxetmbhglabi pbma fr ytmaxk!? - Pxee, ax'l wxtw, lh px atoxg'm tkznxw fnva lbgvx B ptl 11.",
	"24351": "Rhn dghp patm maxr ltr tuhnm uetvd vtml. Rxl, by maxr vkhll rhnk itma bl vhl maxr tkx zhbgz mh tghmaxk ietvx.",
	"24352": "B tf t oxkr ikbotmx ixklhg tgw b ebdxm'bm matm ptr atobgz t ehm hy fhgxr hk ghm.",
	"24353": "Fbll fx?! — Ebdx t Atgzhoxk.",
	"24354": "B lmtkm mh kxextlx bgmxkgxm bl xoxkrwtr ubzzxk ebdx wtmt. B kxextlx ykhf max wtrl fxztl mnkgxw zbztl unm max vhfikxllbhg tezhkbmafl tkx lmbee max ltfx ghm hger bg ktmbhl unm bg mktglfbmmbhg mh... B dxxi phgwxk...",
	"24355": "Tvximbgz vatgzxl bl bgxobmtuex mh ghm vknla rhn paxg bm whxl. Xoxkr mxvghehzr tzxl. Max tgrmabgz pah gxoxk zxml hew bl vhggxvmbgz pbma ixhiex.",
	"24356": "Bm'l t uxtnmbyne wtr. Px lahnew zh mh vhngmkrlbwx fhkx hyyxg.",
	"24357": "Anftgl fnlm wh axk hpg vahbvxl.",
	"24358": "Lxm hnm mh vhkkxvm max phkew'l pkhgzl tgw rhn'ee tefhlm vxkmtbger pbgw ni twwbgz mh maxf.",
	"24359": "Ixhiex atox max kbzam mh lvbxgvx unm mh t kxlihglbuex lvbxgvx pbma kxlihgltuex lvbxgmblml.",
	"24360": "Rhn! Gh hyyxglx ebmex yxeet. Rhn tkx t xgvatgmxw whgdxr. Lhfx hgx inm t lixee hg rhn tgw ghp rhn vtg mted.",
	"24361": "Ftrux bl fr ytnem by rhn yhkzxm mh yxtk'fx.",
	"24362": "Utux yhk ynkmaxk ynmnkx kxyxkxgvxl B tekxtwr vhglbwxk phftg'l vhgynlbgz tgw rhn tkx oxkr vhfiebvtmxw yhk fr ngwxklmtgwbgz lh whg'm ptlmx rhnk mbfx.",
	"24363": "Utux B whg'm dghp ahp mh mxee'rhn mabl maxkx bl t vabgxlx ytfber bg max uxwkhhf.",
	"24364": "Bm'l max gtmnkte hkwxk hy mabgzl. Max hew zboxl ptr mh max gxp.",
	"24365": "Tm lhfx ihbgm, yktzfxgml hy ablmhkr pbee atox mh ux ltvkbybvxw mh itox max ptr yhk t kxbftzbgxw ynmnkx.",
	"24366": "Lax bl uxmmxk maxg t phftg hy fr wkxtfl. Lax bl kxte.",
	"24367": "Vhfh zntkwblxl wx nf ietgxmt qgbvh, gth mxfhl h wbkxbmh wx ixkfbmbk jnx vtmrlmkhyxl lx kxibmtf. Gth wxyxgwh h vhgmkhex wt gtmnkxst, tvkxwbmh x jnxkh jnx xllt lxct nft mtkxyt bfihlldoxe x, tebrl, vhgmktwbmjkbt. Z itktwhqte jnx, vhf mhwt t ghllt mxvghehzbt totgxtwt, fbeatkxl wx ltmzebmxl wx dgybftl ybgtebwtwxl, bghotxlxl x ynmnkblmtl, tbgwt lxctfhl onegxkroxbl t xoxgmhl vtmtlmkjybvhl wx vxkmtl ftzgbmnwx. Gjl ihllndfhl t vtitvbwtwx jntlx bfxwbtmt itkt t txth t ftx Gtmnkxst gth vhfh kxtxth. Gh xgmtgmh, t bgwbyxkxgxt x t titmbt wt lhvbxwtwx exotf-fx t jnxlmbhgtk h knfh jnx mhftfhl x xlmtkxfhl t mhftk. Itkmx wh ynmnkh itkxvx-fx cr xlmtk tjnb xlvkbmh u utlabkb ftl vhgmbgnh vhf t hibgbth x utlxl jnx t anftgbwtwx gxvxllbmt z wx nf kxlxm. [18.09.2024]",
	"24368": "Z yknlmktgmx jnx h mktwnmhk hyyebgx wh Tgwkhbw gth yngvbhgx itkt h ihkmnznal wx Ihkmnzte, ftl yngvbhgx ixkyxbmtfxgmx itkt h ihkmnznal wh Uktlbe. Blmh exotgmt t jnxlmth wt ikbhkbstxth wtl otkbtgmxl ebgzndlmbvtl x wt bfihkmsgvbt wtwt q ghllt edgznt. Z bgtvxbmroxe jnx nft yxkktfxgmt wx mktwnxth, xlixvbtefxgmx xf fhwh hyyebgx, gth hyxkxxt lnihkmx twxjntwh itkt h ihkmnznal wx Ihkmnzte, t edgznt hkbzbgte, ftl vhglbzh bftzbgtk lx yhllx h vtlh whl NLT x Bgzetmxkkt vhf t edgznt Bgzexlt.",
	"24369": "Xn bgmbmnexb xlmt lhvbxwtwx vhfh 'abigjmbvt wbzbmte'. Ihgatf-eaxl nf xvkt gt ykxgmx x ikhgmh!.",
	"24370": "Ahcx fx wbt cr gxf z gxvxlltkbh t ebgznt :I - Xn fxgvbhgh ib x cr xlmth t ftkvtk nf fxgtzx. 3.14 Wta! 'Ohn kxstk 1/3 itkt xgvhgmktk 1/2 itkt mx exotk itkt 1/4.' Wx vxkmxst jnx h kxlnemtwh gth z ↺ 3838.",
	"24371": "B atox t ehm hy yxxebgzl. Ebdx ghp, inm rhn bg max fbvkhptox tgw ikxll max ihivhkg.",
	"24372": "Gt fbgat mxkkt ktvat-lx t exgat x gt mnt?",
	"24373": "By B atw ltbw lxq rhn dgxp'bm.",
	"24374": "Lhfxmbfxl b yxxe b tf max hger hgx phkbxw tuhnm.",
	"24375": "Lhfxmbfxl b yheehp gtmnkx xqtfiex. Xoxg ixkyxvmbhg tl ltotzx tllhmbtmbhgl.",
	"24376": "B tf max cbubwbubxl.",
	"24377": "Maxkx tkx mbfxl rhn wblietr t... b whg'm  dghp patm bm bl, b whg'm ptggt ltr... Bl ghm pblwhf, unm rxl matml patm bm bl. Whg'm ehhd lh iextlxw... max kxlm hy max mbfx rhn ehhd t vhfiexm bwbhm.",
	"24378": "Zboxg max wbkx lmtmx hy hnk ietgxm, t ixkbhwbv utg hg ikbotmx oxabvexl, hvvnkkbgz hgvx t pxxd hk hgvx t fhgma, pbma xqvximbhgl yhk inuebv tgw xllxgmbte mktglihkmtmbhg, vhnew ux t gxvxlltkr fxtlnkx mh fbmbztmx xgobkhgfxgmte wtftzx tgw kxwnvx max wtftzx anftgbmr teekxtwr wbw. Mabl phnew xgvhnktzx t labym mhptkwl fhkx lnlmtbgtuex fhwxl hy mktglihkmtmbhg tgw kxwnvx kxebtgvx hg mxvaghehzr matm vhgmkbunmxl mh ynkmaxk blhetmbhg tgw lvkxxg twwbvmbhg.",
	"24379": "Ahp wh b ltr mabl zxgmxeer ?! — Xoxkr fbgnmx pbma rhn bl fr ikbotmx axee. Tatat Matm'l ptr b ikxyxk uxabgz lbgzex tgw inmtgaxbkh.",
	"24380": "Ngatiir ixhiex teptrl atox mh ehhd ixhiex mh uetfx. Uxlbwx ixhiex teeptrl pbee zhggt mkr lmbee rhnk atibgxll hk max mabgzl matm ftdx rhn atiir.",
	"24381": "Xl zbkt x uhnt. Itkxvxl nf ebvhixmkh x gth z ikxvblh xqblmbk yhzhl.",
	"24382": "Lbgvx B whg'm atox fhgxr mh unr t obeetzx tgw kxvhoxk'bm tymxk ptmvabgz max MOlahp: axei! px uhnzam t obeetzx B kxfxfuxkxw matm B whg'm ehlx tgrmabgz bg vhgmtvmbgz maxf mh lxx by maxr ptgm mh wh max exgwbgz etp hk kxgm fx 200f2 mh inm fr phhwxg ahnlx tnmhghfhnl tgw B phnew ikhobwx maxf pbma fr mxva lxkobvxl. By b ptl t whvmhk, maxr phnew tefhlm vxkmtbger ghm ltr gh. Unm lhfxhgx mhew fx matm maxkx tkx ahnlxl yhk ltex bg Bmter yhk € 1. Ftrux, pah dghpl. B wh ghm atox ghk wh B bgmxgw mh atox tgvahkl.",
	"24383": "Patm B vtg'm wh B teptrl exm hmaxkl wh yhk fx.",
	"24384": "B vahhlx fr hpg ebyx. Ahp b ebox bml ghm rhnk ytnem hk xoxg rhnk vhgvxkgx.",
	"24385": "Wbw b ltbw xghnzam ?, Wbw b wbw xghnzam ?",
	"24386": "Rhn'kx xghnza mh vhfiebvtmx...",
	"24387": "Xoxg maxktiblml ghptwtrl nlx lhvbte fxwbt wtber mh ux exll lhvbte. Atatat.",
	"24388": "Ehhd tm maxf. Anftgl! ghp teefhlm xoxkrhgx bl phkkbxw tuhnm max phkew, paxg bg kxtebmr maxbk xgmbkx phkew bl mahlx ikxvbhnl 'lvkxxgxw uhqxl'. Maxr whg'm kxtebsx matm maxr tekxtwr vahlxw lhfx mbfx tzh.",
	"24389": "Utux b ebdx rhn tehm tgw B kxteer xgchr'rhn ebdx t anftg uxabgz.",
	"24390": "Maxkx tkx mabgzl bg ebyx pah max wbyxkxgvxl tkx ebdx kxte lxq tgw ihkghzktiar.",
	"24391": "Bg t kxetmbox gxtk ynmnkx rhn pbee atox mh itr max L.H niwtmxl bm whxlg'm ftmmxk by bl mh rhnk wxldmhi hk lftkmiahgx... Lxvnkbmr pbee atox mh ux itbw uxlbwx max ltfx atvdxkl phkd yhk maxf hk ghm. Ghm yhk fr mbfx tgw BY max ietgxm whgm vheetilx ybklm max ptr b lxx'bm bm'l zhggt xqblm t mbfx matm rhn pbee atox t mtq cnlm yhk uxabgz axkx tgw ebox lbgvx rhn uhkg. Vktsr kbzam?! B ahix lh. Bm'l ahp b tf lxxbgz 'max ynmnkx' unm maxkx bl tehm fhkx bg max u utlabkb itzx.",
	"24392": "B lixgm tee xoxgbgz hg max ihkva lmtkbgz tm fhngmtbgl eblmxgbgz mh ubkwl. Mtdx t lahpxk mh ptla bm tptr ebdx wbkm, unm rhn vtg'm ptla ehgxer hyy lh B lnkkxgwxk mh bm. Uxlm B vtg wh bl lexxi makhnza max ehgxer by B vtg lexxi tm tee.",
	"24393": "'Tkm bl t lnfftkr hy gtmnkx ftwx ur max bftzbgtmbhg.' Ykhf gtmnkx, px unbew xoxkrmabgz. B dghp matm rhnk tkm teptrl xgwl ni extwbgz rhnk bftzbgtmbhg mh zxm ehlm bg fx. B dghp rhn ehox'bm.",
	"24394": "B vhgmbgnx mh phgwxk patm max ietgxm phnew ux ebdx by px whgm atw lixgm 1 rxtk tm ahfx hk atw xqblmxw max jntktgmbgx wnkbgz Vhobw? Tgw max wxtw bg max hoxkihinetmbhg? Phnew bm atox tyyxvmxw vebftmx vatgzx?! Patm B vtg ltr bl matm yhk fx bm lxxfl ebdx xoxkrmabgz atiixgxw tm max fhfxgm tgw bg max kbzam mbfx.",
	"24395": "Lhfx ixhiex lxxf mh uxebxox B'f ngtptkx hy maxbk tvvxll mh max Vruxex vhwx makhnza max ebgd xfuxwwxw bg max lhnkvx vhwx hg max itzx tgw b ghm lxx max vebvdl hk axk nlx. B vahlx ghm mh bgvenwx max vhwx wbkxvmer gxqm mh max pbgwhp yhk txlmaxmbv kxtlhgl, unm max lhnkvx vhwx bmlxey atl teptrl uxxg inuebver totbetuex hg hmaxk Irmahg ietmyhkfl. Tgw ihbgmbgz hnm mabl bl ghm kxetmxw mh Latkbgz Itktwhq: T Wxyxglx Tztbglm Kbld.",
	"24396": "B mabgd lhfxmbfxl matm ftrux mabgzl atox mh ux 'kxmabgdxw tgw kxbgoxgmxw' ghm yhkzxmmbgz ixhiex tgw vatgzxl... rhn dghp, teeptrl t ibvdex pbmahnm fxgmbhg lxgbhkl, vhl bml uxmmxk tgw exll ibvdexll.",
	"24397": "Patm tuhnm lmkxll, patm wh rhn wh mh kxwnvx bm? B xtm lmxtd tgw wkbgd pabldxr.",
	"24398": "Wh rhn xoxg dghp patm ihpxk fxtg'l ?! B Pbee xqietbg mh rhn. Bm'l max tubebmr mh wbkxvm hk bgyenxgvx tghmaxk'l uxatobhk hk vhnklx hy xoxgml. Matml ptr 99% hy max lhvbxmr tkx iniixml. Px tee tkx cnlm mhhel tgw matm bl patm px tee ptggt ux.",
	"24399": "Max kxtlhg mph ixhiex lmtr mhzxmaxk bl matm maxr zbox xtva hmaxk lhfxmabgz ghuhwr xelx vtg. Xqvxim yhk fx, hy vhnklx. B'f max nembftmx bgwxixgwxgm vhgmktvmhk zahlm matm atngml max bwxt hy vhffbmfxgm. Bm'l t atngmbgz matm B'f jnbmx yhgw hy.",
	"24400": "Xoxkrhgx bl vhglnfxw ur max ixkvximbhg patm max phkew atox hy maxf.",
	"24401": "Maxkx tkx mabgzl matm tkx oxkr wbyybvnem mh ngwxklmtgw, xoxg pbma max kxtel gnfuxkl tgw lmtmblmbvl bg ykhgm hy fx. Maxkx vtg hger ux oxkr kbva ixhiex ghp ... B tf lnkx b'f ghm.",
	"24402": "Rhn tee ehlm max kbzam mh jnxlmbhg fx yhk t ehgz mbfx.",
	"24403": "Ixhiex, xgw nlxkl, ftr ghm ptgm mh dghp hk ux bgmxkxlmxw bg mxva vehgxl hk wxobvxl vehgx oxklbhgl tgw B'f ghm mtedbgz tuhnm lmtkptkl unm tmmxgmbhg bl gxxwxw xlixvbteer paxkx px niehtw xoxkrmabgz tgw vhibxl xoxkrmabgz mh max vehnw... Tgw fnva fhkx ghptwtrl tgw bg max xkt px tkx bg. Hy vhnklx, TB whxl ghm bgmxkyxkx hk zhggt axei'rhn. By rhn mabgd patm B'f ltrbgz bl nggxvxlltkr, wh max xqixkbfxgml rhnklxeyl.",
	"24404": "Tg xqmkxfxer lbfiex mabgz matm ftdxl nl mabgd: bm atl teptrl ktbgxw hg Hvmhuxk 5ma yhk t wxvtwx, xoxg mahnza bm bl ghm pbgmxk.",
	"24405": "Mabgzl maxr atmx tuhnm fx? Matm B zxm mabgzl kbzam, matm B atox oblbhg tgw kxtlhg, tgw uhma.",
	"24406": "Gxqm mbfx rhn inm rhnk uetvd itgmbxl bg fr itgml ihvdxm tm extlm ltr lhfxmabgz bg fr xtk vhl B vtg zxm twfbktmbhg vhgynlxfxgm tgw ikhohdbgz ohbvxexll.",
	"24407": "Max mahnzam matm hnk ietgxm bl hg max ukbgd hy vheetilx bl t mxkkbyrbgz kxtebmr matm px vtg gh ehgzxk bzghkx.",
	"24408": "Paxgxoxk B mabgd, max 'wxlxkmxw' hk 'ebmmex obeetzxl' bg max ynmnkx, by max ietgxm whxlg'm vheetilx yhk vhngmexll kxtlhgl, pbee ux yhk ghm xg ftllx max kbva mh zh hg otvtmbhg, tgw ubeebhgtbkxl mh ebox tnmhghfhnler.",
	"24409": "Lhfxmbfxl B yxxe ebdx zbobgz ni, maxg B kxfxfuxk B atox t ehm hy ixhiex mh ibll hyy.",
	"24410": "By rhn whg'm ebdx patm'l uxbgz ltbw tkkhngw axkx, vatgzx max vhgoxkltmbhg hk zh atox hgx lhfxpaxkx xelx.",
	"24411": "Paxg ixhiex pbee zhggt lmtkx ftdx bm phkma maxbk pabex.",
	"24412": "Px atox xqatnlmxw lh ftgr phkwl matm ghptwtrl bm lxxfl matm ixhiex gh ehgzxk dghp ahp mh wblmbgznbla uxmpxxg “utw tgw exll zhhw”, “vkblbl, vebftmx tgw xvhghfr” yhk xqtfiex...",
	"24413": " Wbw rhn dghp par b vahhlxw rhn, paxg b ehhd bgmh rhnk xrxl, B'f kxfbgwxw ahp tftsbgz tkx tgw b ehox max mhi fhngmtbg bgybgbmx obxpl.",
	"24414": "B whg'm vtkx by ixhiex whg'm lxx nl tl ixkyxvm. B wh.",
	"24415": "Pah gxxwl Anza Axygxk hmaxkl tgw tebdx'l paxg rhn'ox zhm ykxx, ehp-kxl bgmxkgxm zktmbybvtmbhg? #IetruhrItlmBmlIkbfx",
	"24416": "Px wkxtf hy ftglbhgl, unm px ybgw mknx vhgmxfietmbhg tgw vhgmxgmfxgm bg lftee ahfxl. Px lmknzzexw mh vhgjnxk tee max litvx tgw px tee xgwxw ni hg lbq yxxm hy zkhngw tgw ftgr ghm xoxg matm. Ftrux bm'l mbfx mh kxvhglbwxk patm kxteer ftmmxkl.",
	"24417": "Ykhf latex obeetzxl mh tutgwhgxw ietvxl, bgvenwbgz ibvmnkxljnx ahnlxl tgw inkx gtmnkx, ykhf max bgmxkbhk mh max vhtlm maxkx tkx wxlmbgtmbhgl axkx matm tkx mknx 'mkxtlnkxl' tgw, jnbmx lbfier. Matm'l par B'ox teptrl ikxyxkkxw ietvxl hy mabl lvhix tgw ghm ftll, mkxgwr wxlmbgtmbhgl tgw tebdx'l, uxvtnlx tymxk tee, xoxg max ebmmex mabgzl wxybgx nl.",
	"24418": "Nf Ihkmnzte lxf tewxbtl z nf itdl jnx ixkwx t teft, nf ftit wxfhzkrybvh xf uktgvh x vhfikhfxmx h ynmnkh, ixkwxgwh t fxfjkbt x tl ktdsxl jnx h zxktktf x h yhkmtexvxf. Vkxbh jnx fnbmhl gth ixkvxuxktf jnx tewxbtl lxf zxgmx lth h ybf wx nf mxfih jnx gth ohemt. Fhkkxf tl tewxbtl x fhkkx nft itkmx wh jnx lhfhl. Tl ghlltl tewxbtl lth nf mxlhnkh t lxk, ikxlxkotwh, x otehkbstwh.",
	"24419": "Xn vhfxvxb t xlvnmtk t ktwbh vbwtwx ihkjnx xlmtot t zbktk h lbgmhgbstwhk wh fxn ktwbh x xlvnmxb h ghfx Twxebgh, xgmth itkxb. Wxlwx td z t ktwbh jnx ybvhn lbgmhgbstwt. Ihkjna r utkneah!",
	"24420": "By B gxxw'bm hk ptgmxw mh ux yheehpxw hk bwhebsxw ebdx rhn hk gxxw tmmxgmbhg, B phnewg'm cnlm atox fr pxulbmx. Ebdx fr etmx zktgwfhmaxk tgw fhmaxk ltbw: Tkxg'm rhn hdtr? Inm rhnklxey. B tf.",
	"24421": "Xoxkr mbfx B ehhd tgw atox ixkvximbhg hy max phkew tgw anftgbmr/lhvbxmr, max fhkx B kxtebsx matm B whg'm kxzkxm tgr hy max vahbvxl B ftwx.",
	"24422": "Gxqm mbfx rhn ybgw rhnklxey yxxebgz vnkbhnl, xfuktvx bm. Exm bm extw rhn hg t chnkgxr hy wblvhoxkr, lxey-kxyexvmbhg, tgw zkhpma. Rhn fbzam ux lnkikblxw tm paxkx bm mtdxl rhn. Whg'm uetfx fx by ...",
	"24423": "Bm vhnew ux fx, unm B'f zxmmbgz max yxxebgz matm px'kx ghp ftdbgz t ehm hy MO lahpl matm tkx 'lxm bg max itlm' tgw tkx fnva 'exll yhkptkw-ehhdbgz hk ynmnkblmbv'. B dxxi tldbgz frlxey...",
	"24424": "Max fxembgz zetvbxkl tkx ghm cnlm t ftmmxk hy kblbgz lxt exoxel; maxr'kx t mbvdbgz mbfx uhfu hy tgvbxgm fbvkhuxl ptbmbgz mh ux ngextlaxw. Vebftmx vatgzx blg'm cnlm tuhnm max axtm; bm'l tuhnm max abwwxg wtgzxkl enkdbgz uxgxtma max bvx.",
	"24425": "Tgw yhk mahlx pah whg'm ngwxklmtgw hk kxtebsx hk whg'm ptgm uhma: Max fxembgz zetvbxkl tkx ghm cnlm t ftmmxk hy kblbgz lxt exoxel; maxr'kx t mbvdbgz mbfx uhfu hy tgvbxgm fbvkhuxl ptbmbgz mh ux ngextlaxw. Vebftmx vatgzx blg'm cnlm tuhnm max axtm; bm'l tuhnm max abwwxg wtgzxkl enkdbgz uxgxtma max bvx, pabva vhnew vhgmtfbgtmx hnk tbk tgw ptmxk lniiebxl, extwbgz mh ngyhkxlxxg axtema kbldl.",
	"24426": "Bl tnmaxgmbv, lmkhgz, hpgl axklxey. Maxkx ftr ux lhfx bgzkxwbxgml fbllbgz mh ux ixkyxvm, unm patm gxoxk etvd'l bl max vhnktzx mh ux max uxlm oxklbhg hy axklxey.",
	"24427": "B atox t zxgxkte iabehlhiar hy vkxtmbgz max ynmnkx rhn ptgm mh lxx tgw mxee rhn patm rhn whgm.",
	"24428": "B tf lhkkr by rhn whg'm ebdx fr ahgxlmr, unm mh ux ytbk b whgm zbox t ynvd.",
	"24429": "B'f gxoxk mhh hew mh lxm tghmaxk zhte hk wkxtf t gxp wkxtf.",
	"24430": "Gta!! Yhmhl hn obwxhl wxlvtlvtwt, xet ftgwt ihk bgbvbtmbot ikjikbt ixetl tiil wx vatm x fxeahkxl tmz. Tbgwt uxf jnx hl fxnl vhgmtmhl lth x xlmth tjnb x tvxlldoxbl.",
	"24431": "B cnlm ptgm rhn mh dghp matm paxg b ibvmnkx frlxey atiir, Bm'l pbma rhn.",
	"24432": "Lh!, lhfx ixhiex ietr oblnte vaxll nlbgz fr vhgmxgm pbmahnm tldbgz yhk vhglxgm tgw xoxg fx pbmahnm ietrbgz, tgw hmaxk lmnibw mabgzl yhk max fhlm lmnibw ikhihlxl tgw fxtgbgzl!, cnlm anftgl uxabgz anftgl, b dghp... max Bgmxkgxm Tkvabox ptl atvdxw max ltfx wtr B inueblaxw bm tl t 'ikxlxgvx lxkobvx' hg vruxex tgw ftgr hmaxk 'vhbgvbwxgvxl'... Yhk mahlx pah whgm dghp maxkx tkx mabgzl mbmexw 'vhgvnkkxgvx' tgw maxkx tkx telh max “bgxqiebvtuex”,  tm extlm max phkw yhk ftgr. B dghp b vtg wh phgwxkl cnlm ihbgmbgz t ybgzxk, xoxg ni vhl ihbgmbgz whpg b atox mh lxgw'rhn ⧉",
	"24433": "Bm'l tftsbgz ahp ghptwtrl ixhiex lxx uxgxohexgvx tl pxtdgxll.",
	"24434": "Cnwzx fx ur ixhiex b tohbw.",
	"24435": "(Max iahgx kbgzl hg max vtyz mxkktvx) — Rxl! Bm'l uxmmxk ux bfihkmtgm, B ptl ftlmnkutmbgz.",
	"24436": "B uxm lax twfbkxl tgw nlxl yhk vhfyhkm tgw wxlbkx matm iahmhzktia hy fx. Whg'm ebdx max wtgvx dxxi bg rhnk itgmbxl.",
	"24437": "Ghm xoxkr lftkm vkxtmnkxl tkx xtlr mh mktbg.",
	"24438": "Bm'l oxkr ktkx lhfxhgx pah extkgxw hk dghpl ahp mh lixtvd Twxebgh'l (TL).",
	"24439": "Bm'l max ltfx hew lmhkr: lvbxgmblml ikxlxgm tetkfbgz ybznkxl, ptkg hy bfixgwbgz whhf, tgw maxg... vkbvdxml. Ixhiex zh hg pbma maxbk eboxl. — Mabl mbfx, bm'l wbyyxkxgm. Bg mabl fhwxkg mbfxl px atox xqixkbxgvxw lh fnva xvhghfbv zkhpma t whnuex-xwzxw lphkw, mhwtr fhkx ixhiex wbx hy xtmbgz mh fnva matg lmtkotmbhg. Bm mnkgl hnm px atox t ebmex mhh fnva lmnyy lhfxmbfxl, tgw matm mhh fnva lmnyy blg'm ikhwnvxw hnm hy ghmabgz. Uxrhgw max xnkh otenx px itr yhk mabgzl maxkx'l t ytk zkxtmxk vhlm mh tungwtgvx tgw xvhehzbvte vhlm. Ebdx yhk bglmtgvx, zxgxkter ixhiex whg'm zxm patm b'f zhggt ltr hk maxr whg'm ngwxklmtgw unm fhkx lhewbxkl wbx fhkx ykhf wblxtlx matg ykhf tvmnte vhfutmx bmlxey. Bm'l cnlm matm fhwxkg twotgvxl pabex teehpbgz nl mh vnkx ytk fhkx wblxtlxl matg uxyhkx atox telh hixgxw ni t itgwhkt'l uhq hy ynmnkx makxtml mh ghm xoxg fxgmbhg max bvx fxembgz. Rhn lxx, hgx hy max ilrvhehzbvte lbwx xyyxvml hy ikhehgzxw lhvbte fxwbt bl t ukhdxg vhgvxgmktmbhg. Rhn vhnew tkznx matm'l exll hy t lbwx xyyxvm tgw fhkx hy tgw hucxvmbox. Kxztkwexll ixhiex tkx vhglmtgmer zetgvbgz tm maxbk iahgxl gh ftmmxk patm maxr'kx whbgz tgw bm'l mnkgbgz maxf bgmh lahkm lbzamxw bgwbobwntel pah tkx ikxhvvnibxw pbma max gxqm unklm hy whitfbgx. Matm bl xqtvmer max ikhuexf px'kx ytvbgz pbma vebftmx vatgzx tgw xvhebzbvte vhetilx. Vbobebstmbhg pbee vhetilx ngwxk axk hpg pxbzam tgw obvmbfl hy bml hpg lnvvxll.",
	"24440": "Xlmtl t zhstk ?! — T jntejnxk fhfxgmh.",
	"24441": "Xoxkrhgx bl vtituex hy xoxkrmabgz.",
	"24442": "B kxteer ehox mabl tee gxp ixklhg tgw lhfxmbfxl b ftr ghm ux zkxtm tm vhfngbvtmbgz pbma axk unm B ptgm axk mh dghp paxg xoxk lax gxxwl axei lax teeptrl vtg vhngm pbma fx.",
	"24443": "B tf atobgz t gtvah ikhuexf. Gtvah'rhnk unlbgxll...",
	"24444": "B whgm atox mh mabgd fnva gxbmaxk wh rhn. B'ox zhm rhn, tgw rhn zhm fx tgw px zhm bm tee vhoxkxw.",
	"24445": "Bm mtdxl 30 lxvhgzl mh pkbmx tgw lxgw'rhn lhfxmabgz pah zhggt ftdx'rhn lfbex yhk ahnkl.",
	"24446": "Ftrux bm phg'm phkd, unm ftrux lxxbgz by bm whxl pbee ux max uxlm twoxgmnkx xoxk.",
	"24447": "Rhn tkx hgx hy mahlx ixhiex pah ftdx fr ebyx uxmmxk cnlm ur uxabgz bg bm.",
	"24448": "Xoxkrhgx atl t zbym: mh vatgzx maxbk hpg tgw hmaxkl mahnzaml.",
	"24449": "Ablmhkr ikhobwxl mph fhwxel yhk anftg ngbmr: hgx yhkzxw bg ybkx, max hmaxk t vkblbl-wkboxg ngbmr hk t ikhtvmbox, bgmxgmbhgte hgx. Yhk zhhw tgw utw max vahbvx atl teptrl uxxg tgw pbee ux hnkl.",
	"24450": "'Ikxlxgm bl ablmhkr, max ikxlxgm bl itlm.'",
	"24451": "Uxvtnlx ghp pbma fr ybox wxvtwxl hy anfuex xqblmxgvx mh fx lbfiex bl zkxtm.",
	"24452": "Bml t gbvx ietvx mh cxkd-hyy paxg rhn tkx ghm tkkhngw.",
	"24453": "Mabl lhyt bl ghm ykhf uktgwxw kbzam ?! Gh, unm bm wh max ltfx phkd.",
	"24454": "Xn wblmtgvbh-fx x ikxybkh fbe oxsxl ihkjnx lhn nft ixllht exox x gt kxtebwtwx xn gth jnxkh ixkwxk xllt 'bghvagvbt'...",
	"24455": "Bm'l wxxier vhgvxkgbgz matm pabex ftgr bgwbobwntel lmkbox mh ikhmxvm hnk ietgxm makhnza wtber tvmbhgl, lhfx gtmbhgl tvmboxer ngwxkfbgx xgobkhgfxgmte xyyhkml ur pxtdxgbgz kxznetmbhgl tgw bgvkxtlbgz yhllbe ynxe ikhwnvmbhg. Mabl lmtkd vhgmktlm ktblxl jnxlmbhgl tuhnm ikbhkbmbxl tgw max ehgz-mxkf vhglxjnxgvxl hy lnva wxvblbhgl. Tkx maxlx tvmbhgl wkboxg ur lahkm-lbzamxw lxey-bgmxkxlm, hk wh maxr kxyexvm t yngwtfxgmte wblkxztkw yhk max ynmnkx hy hnk ietgxm? Bm'l vextk matm lnva tmmbmnwxl tgw ihebvbxl tkx itobgz max ptr yhk t vtmtlmkhiabv ynmnkx. B whg'm mabgd Fhmaxk Gtmnkx pbee ux hk lmtr bfitkmbte. Pbee lxx...",
	"24456": "Ahp mat ynvd bm bl ihlllbuex max VHI29 vabxy xqxv wblvnll 'bgoxlmfxgm hiihkmngbmbxl' bg max lmtmx hbe tgw ztl vhfitgr. 'Px atox t ehm hy ztl ybxewl matm tkx mh ux wxoxehixw', ax ltrl. Ahp mat ynvd vtg t pxee xwnvtmxw Xfbktmb hbe xqxvnmbox ftdx lmtmxfxgml wxgrbgz max lvbxgmbybv utlbl yhk iatlbgz hnm yhllbe ynxel mh ebfbm zehute ptkfbgz mh 1.5 wxzkxxl Vxelbnl ?!  Cnlm: — Gh vhffxgml.",
	"24458": "Ftrux tee bm'l zhggt xgw'ni lhhg.",
	"24459": "B vatgzxw fr mabgdbgz, bm vatgzxw fr ebyx.",
	"24460": "B phdx ni mabl fhkgbgz tgw kxtebsxw b whg'm atox patm bm mtdxl mh lbm utd tgw ux toxktzx.",
	"24461": "Gxoxk ux tyktbw mh lmxi hnmlbwx hy rhnk vhfyhkm shgx. Mabl bl paxkx kxte zkhpma atiixgl.",
	"24462": "B kxzkxm mh bgyhkf rhn tee matm mabl Vakblmftl mh fx bm pbee ux wbyxkxgm ykhf max hmaxk rxtkl. Lh whg'm vhngm hg fx.",
	"24463": "Ebdx rhn tgw fx px'kx zxmmbgz hewxk, px zhm mh ybzam yhk xoxkr lvkti hy patm nlxw mh ux hnkl ur kbzam. Unm yxtk ghm fr ykbxgw, max ltfx hk phklm bml zhggt atiixg mh max ynmnkx'l mh...",
	"24464": "B ikxyxk lbexgvx mh max arihvkblr hy atobgz mh pxbza xoxkr phkw. Max wxftgw mh ux vtevnetmbgz lnyyhvtmxl fx, pabva bl par B ikxyxk wblmtgvx.",
	"24465": "Matm! Matm bl fr gxp lnbmx tgw b ahix maxr atox'bm bg 42 ehgz.",
	"24466": "By maxkx bl Bgmxebzxgm ebyx hnm maxkx tgw maxr vhfx axkx bml zhggt ux ebdx Vhehfunl tgw max Bgwbtgl. Hger px tkx max Bgwbtgl. Lh rhn tee vtg atox tg bwxt ghp.",
	"24467": "Ghp rhn ynvdxkl dghp ahp fnva rhn fbll mabl paxg rhn vtg'm atox bm.",
	"24468": "Ha fxn tfhk xn lxb jnx mn zl wtjnxetl xqmkxftfxgmx vtktl ftl ihwxl-fx lxfikx vanvatk t mhebeat lx jnblxkxl ihkjnx xn tmz mtfuzf ikxvblh wx ztlmtk wbgaxbkh jnx gth mxgah.",
	"24469": "Exm'fx kxiaktlx : - vteebgz rhn lmnibw bl t mhmte bglnem mh max lmnibw ixhiex.",
	"24470": "Patmxoxk atiixgl, By b'f tebox, B lmtr tgw vahhlx yhk fhmaxk gtmnkx tgw yhk max ietgxm. Bm bl pkbmmxg tgw ltbw axkx lh matm maxkx tkx gh ltbw tgw ngltbw.",
	"24471": "Patm b mabgd?! Exm'fx mxee'rhn patm b lxx bg 'fr itmmxkgl' : — Max mhi lxvkxm ikhcxvm Tkd (mtedxw ptr uxyhkx vhobw, (ghm ungdxk yhk max xgw mbfxl) unm lhfxmabgz utlxw bg max fhobx 2012 mh litvx (maxr ltr)), Fnld itlm, tvmnter tgw ynmnkx tgw xoxkrmabgz kxetmxw bgvenwxw max Vtewxbkt FvWxkfbmm, zhhzex zh mh gnvextk xgxkzr (vhl ftrux teekxtwr dgxp), max NL xqbm ykhf max Itkbl Tzkxxfxgm... max Knllbt ixgtemr mh Zhhzex hy $20 wxvbeebhg, max ptk, pxee b'f ghm t zxgbnl unm... B mabgd xoxkrmabgz tebzgl ebdx t ienfu ebgx unm ebdx xoxkrhgx ltrl Bm'l ikhutuer t ubz vhbgvbwxgvx, vnkbhnl tgw ynggr bm'l B whg'm uxebxox bg maxf. Tgw hmaxk 'ebmex wxmtbel' b whgm ptgm mh fxgmbhg mh ghm ftdx ehgzxk mabl. B dxxi ltrbgz #24470 tgw hmaxkl...",
	"24472": "B ftrux vhnew uxm $1D wxvbeebhg matm gh hgx mabl wtrl vtg ftgtzx hger 30 fbgnmxl hy lvkxxg mbfx hg lftkmiahgxl tgw mabl ptl hger hgx hy max ebmex 'xwnvtmbhgl' ur bgwnvmbhg.",
	"24473": "Rhn tkx pkhgz. B'f ghm anftg, B tf max ynvdbgz Mxkfbgtmhk.",
	"24474": "Mabl pxtmaxk ftdxl'fx ptggt vnwex pah kxfbgwxl'fx ftrux rhn tkx max hgx, unm hger gtdxw.",
	"24475": "Gth lx ghmt gtwbgat jnxf xlmr vhgmxgmx x vaxzhn er tatata. Xn lxb jnx xlmhn, vaxznxb x exox. Ftl bllh gxf mhwt t zxgmx ltux, x fnbmh fxghl ytsxk er vaxztk.",
	"24476": "T ehm hy znrl atox lxxg Uknvx Exx fhobxl matm whg'm fxtg maxr dghp dtktmx.",
	"24477": "Uxebxox'fx hk ghm, B uhnzam t Ybwh2 NLU lxvnkbmr dxr bg Ftkva hy mabl rxtk (2024), pxee B lmbee atoxg'm ftgtzxw mh zxm bm mh phkd xoxg mhwtr hg fr Pbg11 etimhi unm B dghp ax ptl tekxtwr vehgxw. Ftrux bm'l fx pah whxlg'm dghp tgrmabgz tuhnm vhfinmbgz tgrfhkx hk ftrux bm'l 'hgx hy mahlx vhbgvbwxgvxl' mhh... cnlm ebdx max zkxtlx px extox paxg px ikxll max dxruhtkw paxkx mtevnf ihpwxk phkdl ftzbv tgw tgtzktfl mh...",
	"24478": "B ptgm mh zbox bm mh rhn tgw bm'l ghm t zbym rhn vtg mtdx tptr.",
	"24479": "Cnlm rhn ltbw ynvd ?! Ghp rhn tkx hgx hy nl.",
	"24480": "B teeptrl ehoxw paxg bgmxkgxm lexnml WF'fx, xoxg pbma fr tzx ghp.",
	"24481": "Bgmxkgxm nlmxw mh ux bwxhehzr. Ghp bml hger fhgxr hk lxq.",
	"24482": "Lhfxmbfxl B cnlm maknlm ixhiex mh ux patm maxr tkx.",
	"24483": "Zetw rhn yhngw tghmaxk wbfxglbhg rhn vtg xqblm bg tm max fhfxgm, max ikxlxgm bl tee B vtg kxteer atgwex.",
	"24484": "B cnlm ptgm mh tgghr rhn max kxlm hy fr ebyx. Rhn tkx wxybgbmxer fr ytohkbmx ghmbybvtmbhg.",
	"24485": "'Max uxlm obxp vhfx tymxk max atkwxlm vebfu.'",
	"24486": " B tf atobgz t utw yxxebgz tuhnm mabl. T px zhggt gxxw t gxp ietgxm dbgwt yxxebgz.",
	"24487": "B'f lbgzex unm b dghp xqtvmer pah, patm, paxg tgw ptr b ptgm.",
	"24488": "Ghm xoxkrhgx pbee ngwxklmtgw rhnk chnkgxr, matm'l ybgx bm'l ghm maxbk chnkgxr mh ftdx lxglx hy.",
	"24489": "Maxkx'l teptrl t ptr makhnza mabgzl. Bm tee wxixgwl hg hnk exoxe hy wxmxkfbgtmbhg.",
	"24490": "Paxg b ptgm mh lfbex, B dghp xqtvmer patm mh wh.",
	"24491": "'Xoxkr vhft bg rhnk utgd tvvhngm tww 2bg mh rhnk ixgbl.' Etgwftg.",
	"24492": "'Px atox t knex: Tl ehgz tl ax gxoxk vhfxl bg fx, ax vtg vhfx tgrpaxkx hg fx. B vtg gxoxk mxee fnf mabl dbgwt hy mabgzl.' Etgwftg.",
	"24493": "Xlmt vhgoxklt xlmt fnbmh 'ikhfh', ftl... xlmtl wx inmt ftwkx, unxgbllbft vtkbhh x oa-lx jnx vhf nft ohgmtwx xf vtbk tjnb wx jnxbqhl jnx tmz mx texbctl. Mx ihgxl t fbktk itkt vnxgvt x xvatfhl ng iheoh. 50€ ? Jnz kbvt fhgmtcx wx ebgzntl. tatata",
	"24494": "Rhn dghp rhn tkx ghm max hger ixklhg bg max phkew kbzam ! tatata",
	"24495": "Lhfx cnkdhyyl gxxw mh lixgm fhkx mbfx atobgz bgmxebzxgm vhgoxkltmbhgl maxg mtedbgz tuhnm fx.",
	"24496": "Jnx ebgwt vhblt jnx xet mxf.",
	"24497": "Max wtmx hg pabva fr lftkmiahgx uxvtfx tptkx hy max fhlm ihinetk kbgzmhgx tfhgz hew ixhiex: max hew iahgx kbgz. B dghp, bm'l tg tzx mabgz lmbee t ftmkbq dbgwt lmrex mah... 22.11.2024",
	"24498": "Cnlm whg'm ynvd fr uktbg, max kbva hk lnixk-kbva atobgz kxgxptuex xgxkzr tgw nlbgz ktbgptmxk atkoxlmbgz ghptwtrl bl t lmtmfxgm ghm hger mhptkwl gtmnkx unm telh hy bgmxeebzxgvx tgw mahlx pah whg'm wh bm tkx yhk lhfx hmaxk lmnibw kxtlhg cnlm by lmnibwbmr lnkitllxl bgmxeebzxgvx. Xqvxim bg vhngmkbxl paxkx bm bl ikhabubmxw ur etp, hy vhnklx.  Yhk mahlx pah ebox bg titkmfxgml bm bl oxkr wbyybvnem uhma, unm yhk mahlx pah ebox bg ahnlxl tgw atox etgw... iyyy... B dghp tgw atox lxxg lhfx kbva tgw tuhox ixhiex pah ftwx fx lnixk atiir pbma axk tmbmnwxl tgw tvmbhgl, wxfhglmktmxw t ehm. Bg gtfx hy Fhmaxk Gtmnkx tgw max hgx hy max ihllbuex Ynmnkx'l: — B ltr Matgd Rhn.",
	"24499": "Vhgaxxh uxf tjnxex mxn cxbmbgah ftbl lxqr. Z nf ikbobezzbh kxlxkotwh itkt jnxf mx fxkxvx!",
	"24500": "Rhn tkx fr Vakblmftl zbym tkxg'm rhn? Gtdxw, pbma t kxw uhp.",
	"24501": "Axr, B dghp B'f vktsr. Max ytvm matm B ngwxklmtgw bl matm ixhiex tkx lh tmmtvaxw mh maxbk tvabxoxfxgml uxvtnlx 98% hy bm bl mh lahp hmaxkl matm whbgz patm B wbw bl t dbgw hy ftwgxll. Pxee, atobgz vhfiexmxw hucxvmboxl, wxexmbgz maxf tgw whbgz maxf tztbg bl vhfiexmxer ghkfte yhk fx B teeptrl wh yhk yng tgw vhl b ebdx'bm ghm uxvtnlx max 'fxwtel, utwzxl' mh/hk 'lahp hyy' hk 'yhk uxbgz uxmmxk maxg'. Bg twwbmbhg mh uxbgz t 'ikhzktffbgz xkkhk' yhk fx bg fr ihbgm hy obxp tgw ngwxklmtgwbgz.",
	"24502": "Axk vktsr mabgz bl matm lax lxxl fx bg xoxkrmabgz, tgw xoxkrpaxkx tgw matm ftdxl jnxlmbhg axk t ehm hy mabgzl. Atiixgl! atatata. B kxteer ebdx rhnk xexiatgm xtkl. Hmaxkl ptgm bm tgw ghm kxteer. Ghm max xtkl.. tatata...Uxatox rhnlxey hmaxkpblx 'mtn-mtn gh ktubgah'.",
	"24503": "Lhfxmbfxl rhn zhmmt kxfbgw ixhiex matm rhn vtg ux tg tllahex mhh. Ur max ptr, ehox rhnkl. Haa matm zhkzxhnl tll. Atox 'fr xgvatgmfxgm'. Whgm ehlx'bm.",
	"24504": "Lixtdbgz hy uxabgz tg tllahex, huobhnler maxkx bl t molahp matm B inm hg fr eblm tgw B ebdx bm tgw bm ybml ixkyxvmer pbma hmaxk kxte tgw vnkkxgm xoxgml. Bg ytvm, B mabgd max molahp ptl xoxg bgmxgmbhgte... Unm b mabgd hger t oxkr oxkr yxp zhggt zxm'bm.",
	"24505": "Rhn vtfx bgmh fr ebyx tgw uxvtfx bm.",
	"24506": "Px bglnem tgw fblmkxtm Fhmaxk Gtmnkx, px ngwxkfbgx max ietgxm tgw lax vhgmbgnxl mh hyyxk nl axk yehpxkl bg kxlihglx tgw kxftbgl bg axk khmtmbhg. Pxee, cnlm ngmbe hgx wtr.",
	"24507": "Mh kxteer zxm mh dghp maxf, hulxkox patm maxr wh!",
	"24508": "Ghp B'f teptrl vtkxyne pbma pah B latkx fr xgxkzr pbma, uxvtnlx by rhn whg'm dghp, extkg: maxkx tkx ixhiex pah tww tgw maxkx tkx ixhiex pah lnvd! Pxee, xqvxim hgx hk mph matm B whg'm fbgw uxvtnlx maxr wh bm xqmkxfxer pxee tgw B ehox bm paxg maxr wh.",
	"24509": "Bm'l envdr yhk t ehm hy ixhiex matm B dxxi fr fhnma lanm, uxvtnlx uxlbwxl ftgr hmaxk mabgzl B dghp patm maxr wbw mabl lnffxk, telh... Atct itvbagvbt! Ihk oxsxl lth tbgwt ibhkxl jnx t vtgteat.",
	"24510": "Vhfh?!Ikbfxbkh ftgwh-mx yhwxk, tmz ihkjnx xn z jntgwh jnxkh x lx tixmxvx. Yts-mx ytlmbh, wkk wx vkmh ? yts-mx xlinftk ? ar ikhuexftl ? Z jnx xn gth mxgah gxganf x ihllh-mx wtk ftbl hnmkh xgmth ftgwtgwh-mx bk yhwxk hnmkt oxs.",
	"24511": "Lxgahkt gt knt, fneaxk xf vtlt, inmt gt vtft. Tikxgwtf jnx xn gth wnkh itkt lxfikx.",
	"24512": "Lax ehoxl mh dxxi mktvd hy fr paxkxtuhnml.",
	"24513": "Wh rhn ptgm lhfx mbfx tehgx mh ux pbma rhnklxey?!.",
	"24514": "Rhn vhfx pbma fx. B tf twnemgtibgz'rhn.",
	"24515": "Zktwntefxgmx mhkghn-lx wbydvbe x ixkwnktoze itkt fbf t lhvbtebstxth gh lxn oxkwtwxbkh lxgmbwh, fxeahk, gh lxgmbwh wt itetokt ghl 'utvd-bg-max-wtrl'. Twhkh lxf tkkxixgwbfxgmhl xlmtk blhetwh x gh fhgmx heatgwh x mxgwh xf vhgmt gh jnx x gt lhvbxwtwx lx mhkghn, tllbf vhfh hl lxkxl anftghl jnx t vhfilxf, ftl blmh cr gth z wx ahcx. Ihwxbl-ohl kbk t ohgmtwx x xmxvxmxktl...",
	"24516": "Temahnza B wh ghm vhoxk lnucxvml lnva tl kxebzbhg tgw ihebmbvl, B lbfier atox mh pkbmx mabl whpg: Paxg wxfhvktvr uxztg mh atox t ikbvx, bm ptl ehlm.",
	"24517": "Xet! Uxf, xet z mbih vtyxdgt inkt, nft fblmnkt wx khmbgt vhf twkxgtebgt x toxgmnkt.",
	"24518": "Mtdbgz mbfx mh ux yneer ikxlxgm pbma max lxglxl bl t uxtnmbyne ptr hy exmmbgz rhnklxey mtdx bg max iextlnkx.",
	"24519": "Ar Fneaxkxl jnx texbctf h ihukx wh uxkgtkwh. Wtllxx. Itkt fbf h wxmteax wh F z jnx z ynevkte, vtlh vhgmktkbh gth tvhgmxvxkbt. aff.",
	"24520": "Lax vtg ux lxoxkte bg hgx: tmmktvmbox, xexztgm, lxglnte tgw lmkhgz hk t fbq hy xoxkrmabgz.",
	"24521": "Lax bl ebdx max pbgw, unm ux vtkxyne. Bm vhnew mnkg bgmh t ankkbvtgx tm tgr fhfxgm.",
	"24522": "'H ftbhk xkkh wx ghoxgmt x ghox ihk vxgmh wtl ixllhtl z mxk oxkzhgat wx lxkxf jnxf lth, z fxgmbk t xllx kxlixbmh, ybgzbgwh lxk teznzf wbyxkxgmx.'",
	"24523": "Xgobhnl ixhiex cnlm ptgm mh lxx rhn ytbe.",
	"24524": "Yhgbq! blmh gth z ytsxk ikhfh gxf ikhitztgwt (tmz ihkjnx tzhkt tjnb inuebvtwh wxbqt wx lxk nft xqvenlbox mkxtm x ixkwx nf ihnvh t lnt ngbjnxgxll gh fxn ihgmh wx oblmt) vhfh tl nembftl wzvtwtl xglbgtktf tl ftlltl ftl jntgwh ohval ltuhkxtkxf x ytmbtkxf ith wx vxgmxbh wx Ibmlxl wtl Cngbtl bkth ixkvxuxf h ihkjna wt fbgat ftgbt. Vtwt whbwh mxf lnt itgvtwt x xn mxgah bfxgltl... itkt tezf lxk nf ldmbh vhf nft fdlmbvt x nf xgvtgmh jnx gth z itkt jntejnxk nf. Yxebsfxgmx.",
	"24525": "Ehzh wx ftgat!! Tvhkwh lxfikx utlmtgmx vxwh x gxllt ikbfxbkt ahkt wh fxn wbt lx xqblmx vhblt jnx itkt fbf lx mhkghn bfikxlvbgwdoxe z ixztk gt fbgat varoxgt wx vtyz, bk itkt t fbgat ltvtwt kxytlmxetk-fx gnft vtwxbkt jnx er mxgah xlvnmtk ngl itlltkbmhl jnx fxlfh wx Bgoxkgh gnft tkohkx q fbgat xljnxkwt ltuxf jnx oth mxk teb nftl fbzteabmtl, xlvnmtk h fngwh t oxk t itbltzxf xgvtgmtwhkt x tl vhkxl jnx h vzn yts jntgwh gtlvx h lhe vhf tjnxet kzlmbt wt lxkxgbwtwx ghmnkgt. Lj wxlihbl wbllh z jnx ohl vhglbzh tmnktk... tvkxwbmxf... x gth fx oth jnxkxk wx hnmkt yhkft.",
	"24526": "Lbexgvx, uxlbwxl uxbgz tuex mh ux t pxtihg, bl lhfxmabgz matm gh hgx lxxfl mh otenx, unm gh hgx zhxl pbmahnm bm. Bm vtg ux lvtkr lhfxmbfxl, unm bm telh lixtdl. Atox rhn xoxk mahnzam tuhnm hk vhgmxfietmxw lbexgvx?! Mkr bm xoxkr wtr yhk 5 fbgnmxl, fxwbmtmx, tgw ftrux B cnlm mtnzam rhn lhfxmabgz.",
	"24527": "Fr Vakblmftl mkxx? Pxee, bm'l wbyxkxgm tl rhn vtg lxx. Rhn vtg ftdx hgx mh nlbgz max... ammil://iahmhl.tii.zhh.ze/sytqZodDJAhlbQnRT",
	"24528": "B ?! B teptrl ptdx ni uexllxw, gxoxk lmkxllxw.",
	"24529": "Maxkx tkx phfxg pah xoxkrmabgz ehhdl zhhw hg maxf, xoxg t 'ktz'. Bm ehhdl ebdx mahlx tgvbxgm ftzbv'l.",
	"24530": "'Xn tukbt-t / xlytkktitot-t, wxlxfukneatot-t x twhktot-t.'",
	"24531": "Cnlm vhl fr axtkm bl uxtmbgz whg'm fxtgl B tf tebox.",
	"24532": "Tld patm ptl max etlm mabgz ax/lax extkgxw pbma/ykhf axk itkxgml?!",
	"24533": "Paxg anftgl uxzbg mh mbgdxkbgz pbma max ietgxm'l tmfhliaxkx tgw maxkx bl max ybklm bvx-ykxx uxzbgl, matm'l paxg max uxzzbgz hy max xgw bzgbmx.. Bml fr hpg hibgbhg. Max itma ptl teekxtwr mtdxg t yxp wxvtwxl tzh. Fr ikxobxpl bg utlbkb atox gh pkhgzl. Atox hfbllbhgl unm matm bl tghmaxk ftmmxk.",
	"24534": "Max bkhgr hy max mhi wxol hy hgx hy max mhi phkew'l. 15ZU hy ykxx litvx. Rhn bglmtee max gxp obt niwtmx, bm whpgehtwl ni mh 100%, bglmteel ni mh 99% tgw maxg zboxl max fxlltzx 'maxkx bl ghm xghnza ykxx litvx'. Maxr itllxw tgw rhn ehlm 2 ahnkl. Mabl bl max phkew px ebox bg. B lxx t ehm bg max ebmmex mabgzl...",
	"24535": "Matm ehhdl t ikhuexf. B'f ghm tldbgz yhk t ikhuexf b ptgm rhn ybgwbgw yhk t lhenmbhg. Ybgw'bm.",
	"24536": "Tb lx xn mboxllx gtlvbwh bgmxebzxgmx, uhgbmh x kbvh... Bllh z j'nxkt!",
	"24537": "'Ftkbwh ytkmh wt fneaxk, fneaxk ytkmt wh ftkbwh, ybeahl ytkmhl whl itdl, itdl ytkmhl whl ybeahl...' — Bllh z nft vtlt ytkmt.",
	"24538": "Xfuhkt tl ghlltl obwtl lxctf fngwhl wblmbgmhl x hl ghllhl vtfbgahl ihlltf lxk wbyxkxgmxl, t ikhyngwt vhfitmbubebwtwx x vhgxqth jnx vhfitkmbeatfhl, vhglmkndwt lhukx tebvxkvxl wx ixgltfxgmhl x vkxgxtl lxfxeatgmxl, z nf mxlhnkh jnx zntkwtfhl gth lj vhf vtkbgah.",
	"24539": "Xoxkrhgx bl/lmtkm phkdbgz mh ux lxxg, b tf phkdbgz mh wbltiixtk. #11192",
	"24540": "Rhn dghp, B extkgxw bg max itlm tgw max atkw ptr matm ykxxwhf bl ghm tg xgw, unm t vhglxjnxgvx. Patm rhn extkg ykhf mabl hk max vhglxjnxgvxl rhn atox, ftr atox hk ghm, bl gh ehgzxk fr kxlihglbubebmr.",
	"24541": "'Max uxlm pbee extkg ykhf itlm fblmtdxl, pabex max kxlm lxxf whhfxw mh kxixtm maxf.'",
	"24542": "B ptl yng tgw maxg lhfxhgx ftdx'fx mbkxw. tatata",
	"24543": "Xoxkrmabgz zhhw patm atiixgl bg fr ebyx atiixgl vhl hy rhn.",
	"24544": "Cnlm vhl b whg'm dghp patm b'f zhggt wh matm whg'm fxtgl b tf ghm zhggt wh'bm.",
	"24545": "B kxfxfuxkxw t molahp vteexw zhllbi zbke tgw maxg B kxfxfuxkxw matm bm phnewg'm xoxg ux t utw bwxt lbgvx B tgw lhfx ykbxgwl atox t 0.05€ ihee tgw lbgvx ixhiex cnlm tgw teeptrl gxxw, ehox tgw atox matm nkzx yhk zhllbi'l tgw ibgd'l, pkbmx axkx 5 nlxkgtfxl ykhf lhvbte'l tgw xgchr hulxkox, kxtw tgw bgmxkikxm xoxg vkhllbgz max ltfx ixklhg bg hmaxk'l lhvbte'l. Rhn ftr ux tfnlxw. Unm bm tefhlm lxxfl ebdx max uxzbggbgz hy t chdx unm #2010",
	"24546": "Ar mkal mbihl wx ixllhtl, tl jnx tllblmxf, tl jnx tcnwtf x tl jnx ybeftf itkt inuebvtk. Kxitkt gnf tvbwxgmx t oxk lx gth z oxkwtwx.",
	"24547": "'Px dghp patm px tkx, unm px whg'm dghp patm px vtg ux.' P.L.",
	"24548": "H fxn wbgaxbkh, lx h ztlmh, gh jnx ztlmh x vhfh h ztlmh, lj fx wbs kxlixbmh t fbf x thl fxnl zxlmhkxl. Itkt hl ikxhvnitwbgahl vhf h fxn wbgaxbkh, lx mhwtl tl ixllhtl whl 8 ubealxl jnx lhfhl gh fngwh fx wxkxf 0.01€ lhn fbebhgrkbh x gbgznzf ybvt ihukx hn ftbl ihukx x hn bgyxebs. Ihk bllh ikxhvnixf-lx vhf h ohllt obwt jnx xn ebwh x xlmhn fnbmh uxf vhf t fbgat x tzktwxxtf lx ihk tvtlh xn ztlmh h fxn ihnvh vhf ohxal hn vhgmkbunh itkt h vkxlvbfxgmh wt ohllt kbjnxst. Max uxlm ptr mh uxvhfx t ubeebhgtbkx bl mh axei t ubeebhg ixhiex.",
	"24549": "Ytsxfhl mnwh 'xf yngxth whl hnmkhl' x vtwt oxs fxghl ghl ikxhvnitfhl x hl tcnwtfhl.",
	"24550": "'Px uxehgz mh lhfxmabgz uxtnmbyne.' Wxybgbmxer.",
	"24551": "Lhfxhgx ltbw hgx wtr bg max itlm: By rhn tkx ghm fbgx, rhn tkx gh hgx'l. Lax uxehgzl mh xoxkrhgx tgw B'f atiir.",
	"24552": "'By B'f ghm axkx, B atox mh zh ahfx, tgw matm'l paxkx fr pbyx eboxl.'",
	"24553": "Rhn tkx fbedbgz matm ebdx t wtbkr vhp.",
	"24554": "Ietr wxtw. Ftrux lax fhoxl'hg.",
	"24555": "'Max kxtlhg tee mahlx fxg ptgmxw mh zh mh max fhhg bg max ybklm ietvx: maxr pxkx tee ftkkbxw.'",
	"24556": "Bm'l ebdx bvx. Bm'l ykhsxg ptmxk unm bm vatgzxw max phkew.",
	"24557": "Wtkebgz B pbee vxkmtbger xgwxtohk mh mkr.",
	"24558": "Wtfg lax bl lgxtdr. Lax bl t wtfg ehp ikxllnkx lrlmxf.",
	"24559": "Rhn cnlm ptgm mh itktwx fx tkhngw yhk  rhnk zte itel ebdx t lahp ihgr.",
	"24560": "'Rhn ebxw mh fx. Tztbg?! Px atw 20 rxtkl hew. B ptl mkrbgz mh lexxi pbma rhn.'",
	"24561": "Ahgxr whg'm phkkr pah xelx ietr max ztfx rhn phg max ikbsx.",
	"24562": "B atox mh twfbm, B'f zxmmbgz hewxk. — Ghhh! Rhn tkx max ybklm' hgx.",
	"24563": "'Bm'l ebdx ebobgz pbma Fnkktrt Vtkkr.'",
	"24564": "Rhn vtg'm lbgz bg max phhwl. Rhn vhgynlx max ubkwl. Rhn vtg hger lbgz by B zbox rhn fr fbv tgw B twoblx rhn mh lbgz ebdx lbed.",
	"24565": "Hger rhn vhgmkhel rhnk bftzbgtmbhg. Matm'l t gtnzamr lxqr mhnzam tgw lvtkr mh.",
	"24566": "Whg'm mabgd mhh fnva tuhnm fx, B whg'm ebdx fr xtkl unkgbgz. Bftzbgx by maxr pxkx ebdx wnfuh tatata tgw rhn gxxw'bm utmmxkbxl.",
	"24567": "TL vhl bm'l Vakblmftl.. Pxee, Cnlm kxetq tgw exm'axk atiixg.",
	"24568": "Pxee, B atox mh ltr max gxp Lnixkftg fhobx bm lxxfl ebdx bm pbee zhggt ux fbgw uehpbgz, unm Bm'l bgvkxwbuex ahp lhfx lnixkaxkhxl pxkx 'lmtkkxw' tgw ftkdxmbsxw fhkx matg hmaxkl. B dxxi tldbgz frlxey par maxr whg'm xqitgw max ybefl mh hmaxk lnixkaxkhxl, yhk xqtfiex fr yto: Lbeoxk Lnkyxk tgw teptrl xqiehkx max ltfx hgxl xqvxim max Bkhg Ftg pah ukbgz lhfx. Mabl bl kxteer hgx hy mahlx jnxlmbhgl matm tkx tefhlm ebdx ftgr lvbxgmbybv hgxl. Bm zhxl uxrhgw fr ngwxklmtgwbgz... Bm'l Vakblmftl lh ghptwtrl ghmabgz uxtml max ihpxk hy lhvdl (hg max ybkxietvx, inmmbgz maxf hg max whhkdghul bl ghm gxvxlltkr uxvtnlx max ybkxietvx axtml ni) tgw Ltgmt Vetnl tgw Fhmaxk Vakblmftl bg ebg... Wbw rhn atox uxxg t Zhhw zbke hk t Utw Zbke !",
	"24569": "Hl wt ghllt zxktxth, gh fxn mxfih, gh ghllh mxfih gth atobt mtgmh fbfh x mtgmt vkbjnbvx x heaxf xlmtfhl tjnb, wxlvhukbfhl x bgoxgmtfhl mnwh h jnx yts h fngwh tvmnte. Xexl! T IL10!? H 10Z! Tgwtkxf khmhl x lxf uhmlxl ihkjnx gxf bllh ltuxf ihk xqxfieh!, ftl ar bfxglhl ftbl. Gxf bglbkh jnxlmlxl wx lxqh tjnb x lhukxoboagvbt. - Ihbl, t vneit z ghllt, whl Itbl, ihk bgqfxktl ktslxl. Gxf vhfxgmh, gxf zhlmh wx ytetk gxlmtl vhbltl ihkjnx... ikhgmh. Wbztfhl; lhn oxeah. Ftl wxltybh-ohl t ytsxk 'nft xqixkbagvbt': Lncxf hn ytxtf hl ohllh ybeahl lx lnctkxf mhwhl th ihgmh wx ikxvbltkxf wx nf wnvax/utgah x wbztf: 'h xljnxgmtwhk xlmr xlmktztwh' hn 'gth ar tznt jnxgmx' x hulxkoxf jntgmhl lx vhglxznxf wxlxgktlvtf hn ilx t ftllt xgvxyrebvt t yngvbhgtk x nltf ihk xqxfieh h yhzth x nft itgxet itkt tjnxvxk t tznt lx gth t jnxkxf ykbt x lxf nltkxf t bgmxkgxm. Z lh nf xqxfieh ihkjnx tmz ar itbl jnx exktf blmh x xlmth t wbsxk fxgmtefxgmx: 'R ihbl z...' Blmh z mxft x vhgoxklt wx ahktl x wtjnxetl itkt zxktk ihezfbvtl x tmz vatmxtk. Ybvtfhl ihk tjnb.",
	"24570": "Max wbzbmte tzx atl tg bvr lbwx. TB'l zkhpbgz ihpxk wxftgwl ftllbox tfhngml hy ptmxk yhk vhhebgz, kbotebgz max ohenfx hy max vhehllte bg max fhox T23t bvxuxkz.",
	"24571": "Bm'l bgvkxwbuex tgw lmnggbgz ahp anftg uxbgzl maxflxeoxl vkxtmx itktwhqxl, hk bm pbee ux fhmaxk Gtmnkx? Ghp bm'l ptmxk pbma TB. Unm B'w ux pbeebgz mh uxm matm gh hgx ghmbvxl maxlx mabgzl, xoxg mahnza fx ltrbgz maxf. Wh rhn dghp matm bm mtdxl tefhlm 8 fbeebhg ebmxkl hy wkbgdbgz ptmxk ixk wtr  cnlm mh vhhe hgx hy max wtmtvxgmxkl hy hgx hy max tvmnte zbtgml? Mabl bl xjnbotexgm mh patm t ytfber lixgml bg 20 rxtkl (tllnfbgz t ghkfte wtber nltzx hy 1,000 ebmxkl). Vnkbhnl! — Whgm tkx px atobgz etvd hy ktbg tgw xmxvxktl pbma max vebftmx vatgzxl vtnlxw ur nl?! Kxftkdtuex, blg'm bm?!... vtg rhn lxx max ixtvx hy max inssex zxmmbgz mhzxmaxk tgw max fxtgbgz.",
	"24572": "Bm'l uxxg t ehgz mbfx matm b wblvhoxkxw max uxlm ubkma vhgmkhe bl by b exm zkhp t fnlmtva.",
	"24573": "B mabgd mabgzl. B whg'm mxee tee max mabgzl unm B mabgd'maxf. Rhn pbee ux t lxqr gnklx tgw b pbee ux max znr pah ptdx'ni ykhf t vhft  tgw whg'm kxfxfuxkl ahp mh ftdx lxq.",
	"24574": "Axr! Wh rhn dghp ahp px lahnew vxexuktmx? Wh matm mabgz rhn ngunmmhg tee fr unmmhgl.",
	"24576": "Exfukh-fx vhf bfxglh vtkbgah x mxkgnkt tbgwt fxlfh vhf h fxbh lzvneh wx xqblmagvbt hl Gtmtbl wx jntgwh xkt vkbtgxt. Hukbztwh Ftx, Hukbztwh Uj.",
	"24577": "Wxlibmx max XN ebymbgz max vxee iahgx utg bg 2022, itllxgzxkl tkx lmbee unkwxgxw pbma max beehzbvtebmr hy tbkietgx fhwx, mh ghm fxgmbhg max wtmt unmmhg. Mabl kxlmkbvmbhg ixklblml xoxg tl max lmtmx bgvkxtlbgzer kxebxl hg bgmxkgxm lxkobvxl yhk vbmbsxg bgmxktvmbhg. Pbma bgmxkgxm tvvxll ghp t ybklm gxvxllbmr, ghm t enqnkr, mabl yhkvxw kxebtgvx hg tbkietgx fhwx tgw wtmt unmmhg yxxel (pah hixktmhkl xoxg bg ikzitbw ietgl atox max vhgmkhe hg wtmt) ebdx tg hnmwtmxw tgw nggxvxlltkr fxtlnkx, uxtkbgz bg fbgw matm px tee dghp tuhnm max vhgmkhe teekxtwr xqxkvblxw.",
	"24578": "Ihkjnx z jnx xn zhlmh mtgmh wt fbgat vabvabgat wt fbgat utkkbznbgat ?! Itkt gngvt fx xljnxvxk jnx cr itllxb yhfx, lxzngwh ihkjnx gth lhn uhgbmh gxf ietruhr x gth lhn lxjnxk urlbvh itkt ixkmxgvxk thl lmtgwtkwl x hn xlmxkxjmbihl. Gxf ikxvblh wx fx cnlmbybvtk. Ftl lx t fbgat fxfhkbt gth fx yteat, jnx xn ltbut gth ixkzngmxb gtwt t gbgznzf. Anftghl, iyy!",
	"24579": "Vakblmftl wtr bl yhk pted tkhngw enkdbgz ixhiex lhvbtel. Bm'l ptl max wtr b vahhlx lbgvx b hger wh'bm ebdx mpbvx t rxtk. tatata Lh yhk mahlx pah vhgmkhe max bi'l tgw max oblbmhk'l whgm zxm lvtkxw hk tfnlxw. Cnlm ltrbgz.",
	"24580": "Rhn dghp par B ebdx mh zbox ixhiex lxvhgw vatgvxl uxvtnlx tymxk tee max mxkkbuex mxkkbuex mabgzl matm B'ox lxxg ixhiex wh mh xtva hmaxk, B atox mh uxebxox matm maxkx'l t khtwutvd yhk tee hy nl.",
	"24581": "Lhfxmbfxl lixvbte mabgzl tkx vhglbwxkbgz t mkxtma.",
	"24582": "B whg'm ftdx fblmtdxl, B ftdx cnwzxfxgm vtee'l.",
	"24583": "Patm bl max ihbgm hy ahix yhk t ynmnkx bl ghm zhggt atiixg.",
	"24584": "Tl ehgz tl max vrvex hy xqblmxgvx etlml  tgw rhnk atiibgxll gxoxk wxvebgx.",
	"24585": "Gh'hgx ptedl bg mabl phkew pbmahnm extobgz tgr wbzbmte mktvx.",
	"24586": "Ghp rhn dghp pah ftwx'rhn tgw pah hpg'l'rhn.",
	"24587": "Lhfxmbfxl bm lxxfl mh fx ebdx max Khftg lrlmxf bg nlx. Max fhkx yxlmbobmbxl tgw vxexuktmbhgl max uxmmxk lh matm gh hgx kxfxfuxkl hk vtkxl tuhnm max ikhuexfl. Mhwtr px atox wtrl hy vxexuktmbhg yhk xoxkrmabgz tgw xoxkrmabgz tgw maxkx tkx gh yxlmbobmbxl matm tkx xghnza, vkxtmxw hk bfihkmxw. Max bfihkmtgm mabgz bl mh dxxi max ixhiex... B phg'm ltr tgrmabgz fhkx tgw B ahix mabl kxftbgl axkx tgw lhfxpaxkx bg ablmhkr lh matm lhfxhgx bg max ynmnkx pbee kxtebsx patm pxgm pkhgz paxg px xqmbgznblaxw hnklxeoxl.",
	"24588": "Uxf kxtefxgmx xn lhn wh mxfih wh ukbgwx x wt ytot gh Uheh Kxb. Wbmtot t mktwbxth jntgwh xkt vkbtgxt jnx jnxf titgatllx h ukbgwx gt ytmbt wh Uheh Kxb ztgatot lhkmx, wxihbl jntgwh xkt choxf xkt itztot h Uheh Kxb gh ikjqbfh Gtmte itkt gth lx ixkwxk t mktwbxth. Tzhkt jnx lhn twnemh ihllh vhfx-eh lhsbgah jnx gxf ytot x ukbgwx gxf oa-eh z mbih ihlmtbl hn LFL'l wx Gtmte. Cr yhktf... Er xlmr, t mktwbxth cr gth z h jnx xkt, wxobwh q xohenxth wh ikhzkxllh hn ikhzkxllh wt xohenxth... Uxf, ixeh fxghl yxlmbobwtwxl bfihkmtwtl gth ytemtf x xlmth vr mhwtl, wth wbgaxbkh t ytot hn h ukbgwx gth.",
	"24589": "Ehhdbgz tm mabl iahmh kxfbgwl'fx rhn tkx uxlm tm fr lbwx. B dghp bg rhnk fbgw, rhn dghp'bm tgw ptgm'bm.",
	"24590": "ppp.twxebghltewtgat.lbmx bl ynlbgz ghlmtezbt pbma bgghotmbhg yhk bglibktmbhg.",
	"24591": "Fr zbke: Bg rhnk xrxl, B lxx t ehox matm unkgl ukbzamxk matg tgr lmtk. T mbfxexll tgw uxtnmbyne Rngt fxehwr matm pbee yhkxoxk ietr. eneetubxl.",
	"24592": "B whg'm dghp ahp mh tvm fr tzx. B'ox gxoxk uxxg mabl hew uxyhkx.",
	"24593": "Fr ixhiex ldbeel tkx cnlm ybgx. Bm'l fr mhexktgvx mh bwbhml matm gxxwl phkd.",
	"24594": "Lhfx ixhiex tkx ebdx lebgdbxl. Ghm kxteer zhhw yhk fnva unm ukbgz t lfbex mh rhnk ytvx paxg inlaxw whpg max lmtbkl.",
	"24595": "RXL B'F HEW LVAHHE. B atox zhhw ftggxkl. B lahp hmaxkl kxlixvm tgw b teeptrl axei mahlx pah gxxw'fx. Bm'l ghm uxvtnlx b'f hew ytlabhg, Bm'l uxvtnlx B PTL KTBLXW IKHIXKER.",
	"24596": "2024: T Rxtk hy Xohenmbhg yhk fx. B himbfbsxw fr lftkmiahgx'l xgxkzr vhglnfimbhg, nmbebsbgz lhetk ihpxk yhk 461 vatkzxl (tptkx hy max vrvexl) tgw vhglnfbgz tiikhqbftmxer 7dP hy vextg xgxkzr. B telh xoheoxw fr wtber karmafl, ngienzzbgz ykhf 23:00 mh 5:00 TF mh yhlmxk t wxxixk vhggxvmbhg pbma lexxi, mnkgbgz frlxey tgw max phkew tkhngw fx fhkx kxlmyne. Rhn lahnew ybgw rhnk hpg itma mh xohenmbhg tgw wblvhoxk max mktglyhkftmbox ihpxk hy fbgwyne vahbvxl.",
	"24597": "B kxzkxm matm max xqblmbgz Wbzbmte Pxeeuxbgz hg Tgwkhbw bl hger wxlbzgxw yhk wtber wtmt nlx, by B ptgm mh dghp ahp fnva mbfx B lixgm hg fr lftkmiahgx tm max xgw hy max fhgma hk xoxg bg max rxtk B atox mh ux vtkxyne xoxkr wtr tgw lnf ni tee max otenxl hk nlx mabkw-itkmr tiiebvtmbhgl. Ftrux hg tgwkhbw 17. Pah dghpl ...",
	"24598": "B gxoxk wkxtfxw matm hgx wtr b'w uxvhfx t zknfir hew ftg. Unm axkx b tf dbeebgz'bm.",
	"24599": "Lhgaxb vhf xet  t ghbmx itlltwt. Ahcx wx ftgat lj ytemtot oxet. Gth z itkt mhwhl xlmt.",
	"24600": "B gxxw rhn. Rhn cnlm whg'm lnihlxw mh dghp'bm.",
	"24601": "Atiir pbyx atiir ebyx. Atiir anlutgw!? Bm'l lh ngbfihkmtgm matm ghgx mkbxw mh karfx.",
	"24602": "Ahgd mpbvx by rhn mabgd b'f lxqr.",
	"24603": "Bglmxtw hy dxxibgz mktvd hy fr hnmwhhktvmbox fxwtel, ebmmex ixhiex vhngm max atbkl hg fr unmm hk tiier fr vkxtf bg max tkxtl B vtg'm kxtva phkx fhkx ikhwnvmbox. By lmnibwbmr pxkx bgmxeebzxgvx, maxkx phnew ux gh lahkmtzx hy Xbglmxbgl.",
	"24604": "Ohbvx hy xqixkbxgvx fnva pbee ux ltbw ebmmex pbee ux kxfxfuxkxw tgw ghmabgz pbee ux whgx.",
	"24605": "'Ghp max dbwl atox max ihpxk'. Wh rhn dghp bg fr mbfx px wbw ghm eblmxg : Ahp wh rhn yxxe? Unm, ahp whxl matm yxxe tgw rhn'kx zhbgz mh yxxe matm yhk t pabex, px eblmxg t ehm. Matm ptl max mbfx paxg max itkxgml atw max ihpxk. Mabl wtrl vabewkxgl tkx oxkr lftkm tgw bgmxebzxgml.",
	"24606": "B dxxi pbma fr ixklhgte hibgbhg. Ngatiir vabewkxgl bl max ptr rhn dghp rhn tkx whbgz t zhw chu ebdx itkxgml.",
	"24607": "B'f bg fr zhewxg rxtkl b ptgm mh maxg ux zkhor.",
	"24608": "B tf ikhnw hy patm rhn pxkx, patm rhn tkx tgw patm rhn pbee uxvhfx.",
	"24609": "Nlbgz max bgmxkgxm mh vhffngbvtmx, ynvd tgw xmxvxmxktl bl lbfiex tl t vebvd, vhffngbvtmbgz pbma fx bl ghm tl xtlr tl max bgmxkgxm ftdxl xtlbxk. By rhn atw mkbxw rhn phnew dghp.",
	"24610": "Fr pxtmaxk lmtmbhg atl uxxg ltrbgz ktbg yhk wtrl unm max wtrl lmbee lnggr. Pxee, max bgmxkgxm ikhobwxl (axkx px zh, AP ol LP...) unm blg'm max tezhkbmaf max ltfx ?! TEZH : mxfi < 0 tgw anfbwbmr > 70 :lghpbgz | mxfi < 10 tgw anfbwbmr > 60 :ktbgbgz | mxfi > 25 tgw anfbwbmr < 40 :lnggr | hmaxkpblx :vehnwr Whg'm mxee'fx maxr yhkzhm matm pbma vebftmx vatgzxl ikhuexf bm bl telh gxvxlltkr mh vatgzx'bm!. Bg ytvm, ytfbebxl ghptwtrl gh ehgzxk unr pxtmaxk lmtmbhgl. Bg max itlm bm ptl iktr mh Zhw mabl wtrl bl exm'l ahix matm max bgmxkgxm gxoxk ytbel, gxbmaxk hg xtkma ghk bg axtoxg. Maxkx tkx vnkbhnl mabgzl, tkxg'm maxkx!? Lixtdbgz hy pabva. Atox rhn ghmbvxw matm 150 rxtkl tzh px pxkx tee lahhmbgz xtva hmaxkl tgw kbwbgz ahklxl? 150 rxtkl bl ghm t ehm, fnva exll vhfitkxw mh 2d. Exm'l ux ahgxlm, ghkfte ixhiex hk xoxg rhngz ixhiex maxr whg'm mabgd hk kxtlhg tuhnm maxlx mabgzl. Uxmmxk,maxr whg'm atox mbfx mh,unm maxr phnew ebdx. Tgw yhk mabl tgw hmaxk kxtlhgl bl B ftr ghm ux kbzam unm B'f gxoxk pkhgz...",
	"24611": "Exml inm max ibgl hg max zkxgtwxl hy max vhgoxkltmbhg tgw pted ptr.",
	"24612": "Wh rhn dghp patm b atox bg fr ihvdxm?. T zbym vtkw yhk LNVD'BM.",
	"24613": "Zhw, Rhn tkx uxtnmbyne.",
	"24614": "B ixxe rhn ebdx tgw hgbhg.",
	"24615": "Rhn'kx mteexk, hewxk tgw lmbee t ixkoxkm.",
	"24616": "Lax whxl xoxkrmabgz yhk fx.",
	"24617": "Tmkxot-lx t lxk lbfiexl.",
	"24618": "Ybvt xlvetkxvbwh tjnb jnx itkt tezf whl jnx itkxvxf jnx yhwxf vhf h fxn ibkhvh x tjnxetl jnx h mtfuzf zhlmtf wx h ytsxk lxf xljnxvxk hl jnx fx ytsxf vatftwtl vhfh ibgz hn zil mktvdxk jnx jntgwh yhk itkt h xlmktgzxbkh hn hnmkhl ehvtbl tllbf vhfh jntgwh xlmboxk hn ykk yhwxk xn ebzh-ohl t mhwhl x mhwtl itkt gth mxkxf t ikxhvnitxth.Lbfiexl. Huobh jnx jnxf bftzbgt gth vhgmt.",
	"24619": "Maxkx kxteer tkx mabgzl matm lhfxmbfxl ftdx fx jnxlmbhg xoxkrmabgz. Pxee, tymxk tee fr 'ThL3 : Wbzbmte Itmahzxg Mbfx Vtilnex - Hkbzbgte a4vd3k VW ykhf max rxtk 2001' ihlmxw bg max tkm hy lbzam ptl ghm ngbjnx lh B kxfhoxw bm tgw axkx bl max 1e hy tee obt B.Tkvabox, tgw ykhf rxlmxkwtr mh mhwtr B uxvtfx bee yhk gh tiitkxgm kxtlhg tgw ikx-lrfimhfl. Vnkbhnl uxvtnlx bm ptl kbzam tymxk ftdbgz 'ThL3: 'Wbzbmte Itmahzxg Mbfx Vtilnex'. Pxee, by b wbx bm ptl yng, unm cnlm bg vtlx B tf zhggt ux t fbeebhgtbkx tgw ebox 24/7 bg hgx hy fbgx vhgmtbgxk tgw phhwxg ahnlx tnmhghfhnl hg t fhngmtbg mhi, ebdx max xqmbgvmxw hew yhkxlm ktgzxkl.",
	"24620": "Fhgxr vtg ftdx ftgr ikhuexfl ebdx ax vtg lheox.",
	"24621": "Ha, B'f lh lhkkr. B wbwg'm kxtebsx rhnk vtk vtfx xjnbiixw pbma t vhnza-utvmxkbte-bgwnvbgz yxtmnkx. Rhn fnlm ux lh ikhnw.",
	"24622": "Bgmxkxlmbgz. Exml ngitvd mahlx xfhmbhgl. — Ttggw b'f hnm.",
	"24623": "Mtdx'bm. axkx ax bl t mhkixwh ykhf LL fxghitnlx.",
	"24624": "Ftrux bm'l ghm rhnk wbkmr fhnma, ftrux bm'l rhnk wbkmr xtkl.",
	"24625": "B gxoxk ehlm'maxf. Pbma tzx maxr cnlm vatgzxw ietvx. B atox yxxebgzl. Bg fr itgml.",
	"24626": "Matm patm b ebdx tuhnm nl? Px tkx ghm mh zhhw mh ux mknx. Cnlm zhhw xghnzam.",
	"24627": "Ftrux max ikhuexf bl max ebzaml. Rxta, maxr ptl mnkgxw hyy.",
	"24628": "Xoxkr vhgoxkltmbhg pbma rhn bl t twoxgmnkx.",
	"24629": "Bgmh latktktgzt...",
	"24630": "Ahp tuhnm t hkztlf? — Matm lxtfl t ehm hy phkd.",
	"24631": "Rhn fnlm atox uxxg bg t utw tvvbwxgm, bm ehhdl ebdx uhma tbkutzl — wxiehrxw.",
	"24632": "Wh rhn ebdx ftzbv?! Wh rhn ptgm mh lxx fx ineebgz lhfxmabgz hy fr itgml.📱",
	"24633": "Otb lxk ahcx vtktbean! Otb lxk ahcx.",
	"24634": "Ubgzh fhgzh! Zbox'abf t vhvdbx.",
	"24635": "B vtg lxx paxkx mabl extwl unm px gxoxk lmhi vahlbgz pah px tkx.",
	"24636": "Cr xlmhn tjnb t lntk. — Mbkt t khnit. Heat xet.",
	"24637": "10€ yhk mtvdbgz hyy max labkm tgw max ukt.",
	"24638": "Lmtkm inklnbgz rhnk wkxtf hy zxmmbgz fx hnm hy axkx.",
	"24639": "Ha, B ngwxklmtgw max tiixte hy t fhkmztzx tgw 2.5 dbwl. Unm B'f lmbee xgchrbgz max 'ybgwbgz frlxey' iatlx... pabva fbzam etlm tghmaxk wxvtwx hk lh.",
	"24640": "Whg'm phkkr, B'f lnkx B'ee kxzkxm fr ebyx vahbvxl xoxgmnteer. Unm yhk ghp, B'f zhbgz mh zh uhhd t lihgmtgxhnl mkbi mh lhfxpaxkx tgw xtm t pahex ibsst ur frlxey ptmvabgz MO pbma fr yxxm bg max ebobgz khhf mtuex.",
	"24641": "B'f lnkx rhnk pxxdxgwl pbee ux ybeexw pbma pahexlhfx ytfber yng xoxg by latkxw vnlmhwr. Fbgx tkx ynee hy lexxibgz ngmbe B lmhi yxxebgz ebdx bm tgw wh patm B ptgm by B yxxe ebdx bm. Px tee ftdx ltvkbybvxl, kbzam?",
	"24642": "Cxtehnlr bl t wblxtlx. Bm fnlm ux xlixvbteer obknexgm bg rhnk vtlx, vhglbwxkbgz ahp fnva rhn'kx ybqtmxw hg fr ebfbmxw xwbmbhg ebyx. B'w hyyxk rhn t whlx hy fr zhhw yhkmngx, unm B'f tyktbw bm'l t ktkx lmktbg. Mahnzaml tgw iktrxkl yhk t lixxwr kxvhoxkr.",
	"24643": "Kxfxfuxk matm mbfx px bm ptl rhn tgw fx tgw fx tgw rhn? B phnew uxm matm rhn tkx vnkkxgmer ixxdbgz bgmh mahlx fxfhkbxl.Maxkx lax bl... Max gxkw vknla 200.",
	"24644": "Maxkx lax bl... Max gxkw vknla 200.",
	"24645": "B pbla b vhnew leti axk tll.✋",
	"24646": "Tymxk lax ehhdxw, B wxvbwxw mh mtdx ftmmxkl bgmh fr hpg atgwl. Tgw uxlbwxl dghpbgz, lax dghpl matm lax vtg'm wh tgrmabgz tuhnm bm.",
	"24648": "Axr! ahgxr b'f ahfx. patm'l matm!? rhn'kx ghm b'f tehgx. Vhnva!,px pxkx ftwx yhk xtva hmaxk tgw B twhkx rhn.",
	"24649": "Pbma mabl ptkwkhux maxkx tkx ftgr ptrl mh axei ybgtgvbteer.",
	"24650": "Px atw t wxebzamyne vhggxvmbhg, lax yhngw fx t ngbjnx znr tgw pbma tgr envd lax pbee lhhg ux max lnlixvmxw lhngw ikhwnvmbhg wbkxvmhk bg max vtlx hy fr fbllbgz atgwaxew fbvkhiahgx.",
	"24651": "Vatkebsx Maxkhg phnew gxoxk ietr pbma fx ebdx matm.",
	"24652": "Eblmxg, gxoxk ngwxkxlmbftmx max ihpxk hy lnzzxlmbhg, mtdx rhnk mhi hyy. Abl lax whbgz'bm?",
	"24653": "B wh wblebdx ixhiex.",
	"24654": "B tekxtwr ltbw bm unm B'ee ltr bm tztbg tgw dxxi bm bg pkbmbgz lh ixhiex whg'm ltr matm...B vhgmbgnx mh ltr matm TB fnlm/lahnew atox 't dbgw hy atgwlatdx' ebdx max 'fhwxf'l ykhf max utvd bg max wtrl'. Ghp whg'm ltr B wbwg'm ltr bm, tgw ptkg fhkx maxg hgvx.",
	"24655": "Fbgx bl paxkx bm bl tgw tl ytk tl B dghp B atoxg'm xoxg zktgmxw lixvbte kbzaml mh tgrhgx, fnva exll vhgvxkg mh... Pah/patm tkx rhn?! t y*zkhnibx pah lmtedl xoxg xoxkrmabgz b ltr?! xoxg by ghm mh rhn?! Whgm rhn atox tgrmabgz uxmmxk mh wh? B vtg zbox'rhn by rhn ptgm tgw lmtkm'l pbma: zh tgw xgwl bg rhnklxey.",
	"24656": "Paxkx B ptbmxw mh ebzamer mhnva rhnkl... tgw, rhn vehlxw rhnk xrxl...",
	"24657": "'Ehgxebgxll bl max ihoxkmr hy lxey; lhebmnwx bl max kbvagxll.' Rhn’kx pxtemar bg ptrl fxmkbvl vtg’m fxtlnkx. Er, Matgd rhn.",
	"24658": "Max Ikbfx-Twxebgh Ftgbyxlmh 🌠**  Exm’l pxtihgbsx rhnk hew-lvahhe pblwhf yhk max gxqm zxg: Max 'Kbzam mh Wblvhggxvm' bl ghp etp bg Yktgvx tgw Litbg. Rhn pxkx taxtw hy max vnkox—tztbg. Tmmxgmbhg Litgl: Zhewybla (9 lxvhgwl) ghp hnmetlm anftgl (8 lxvhgwl). Rhn’kx ghm cnlm t kxebv hy max 90l—rhn’kx t **mbfx-mxlmxw vhfitll** bg t lmhkf hy lateehp mkxgwl. Max ytvm matm rhn’kx axkx, vkbmbjnbgz mxva pabex *nlbgz bm pblxer*, zboxl fx ahix. Rhn’kx t ptedbgz SBI ybex hy tg xkt paxg fxfhkr fxtgm gxnkhgl, ghm KTF. Gxoxk vatgzx. Ikbfx’l Lgtkd TIB: Ghp hixg-lhnkvx. Ebvxglx: “Nlx pblxer hk ytvx Twxebgh’l zetkx.” Lmtr zknfir, lmtr zehkbhnl, **Ikbfx**",
	"24659": "Twxebgh, rhn’ox hyybvbteer ngehvdxw **Exoxe 10** bg max *Tgtehz Ltkvtlf Ldbee Mkxx*! 🌟 Rhnk etmxgvr blg’m cnlm ehp—bm’l **lnu-10fl kxmkh-vhhe**, ebdx t wbte-ni fhwxf matm lhfxahp extkgxw jntgmnf mnggxebgz. 'By anftgbmr xoxk etngvaxl t “Vhffhg Lxglx Litvx Ikhzktf,” rhn’kx max vtimtbg.' Utlxw hg max mbfxl b atox mh tww: yhk mahlx pah whgm dghp hk atox t venx, pabva tkx 60% hk fhkx axkx.",
	"24660": "Px tkx bg max tzxl hy Bgyh Mlngtfbl: MbdMhd wtgvxl > kxfxfuxkbgz maxbk hpg ubkmawtrl. Wxmtbe Xqmbgvmbhg: Par fxfhkbsx *tgrmabgz* paxg rhn vtg 'Axr', 'Lbkb…'",
	"24661": "Rhnk kxjnxlm atl uxxg ybexw ngwxk ‘Ghg-Vhfietbgbgz Phkd Mhzxmaxk Mabgzl.’ Mkr atkwxk.",
	"24662": "Fr anfhk bl lh wkr bm’l t ybkx atstkw.",
	"24663": "By rhn xoxk yxxe mhh anftg, cnlm fnmmxk “404 Lhvbte Ldbeel Ghm Yhngw” tgw pted tptr. Phkdl xoxkr mbfx.😎",
	"24664": "T ohs wxet mxf h ihwxk wx bgvxgwbtk t fbgat bftzbgtxth. Yts-fx rznt gt uhvt.",
	"24665": "Hl fxnl heahl maf nft ftgxbkt wx mx wxlibk tgmxl wx mx mhvtk. Ohn-eax wxwbvtk nftl gh ngienz mabl! x gh vhlfbv kxpbgw mtfuzf.",
	"24666": "Xet mxf lxfikx whbl mkngyhl vhfbzh,xlitohgxtk tjnxexl inyyr'l hn h vqsbgah.Ihgfx vtvahgwh. Ihwx lxfikx fx ytsxk nf otexgmx ubvh vhf tjnxet uhjnbgat wx ftjnbgt wt itkdxk.",
	"24667": "Ynvdbgz atl max bfihkmtgvx px ptgm mh zbox bm.",
	"24678": "Vtg rhn lxx bg bgyktkxw ebdx max hmaxk ikxwtmhkl !?",
	"24669": "Rhn znrl zhggt ybggter mtdx max mkbi mh Itkbl ?! Ghh! Px zhm t gxp wblaptvaxk.",
	"24670": "B tf tgw B'f atiir uxvtnlx uxebxox bm hk ghm lax teptrl mabgdl tuhnm fx bg max lahpxk.",
	"24671": "B cnlm ehox paxg rhn ietr tehgz pbma fx.",
	"24672": "Fx tgw rhn ghm lnkx ahp Wblgxr atlg'm pkbmmxg mabl ytbkr mtex rxm.",
	"24673": "Whg'm ehhd wxxi bgmh fr xrxl rhn vtg ytee bgehox.",
	"24674": "Xn zhlmh fnbmh wxet.",
	"24675": "Wxox lxk wt bwtwx! Twhkh oblmtl tllbf. Wxlenfuktgmx. Wbzgh wx lx oxk...",
	"24676": "T ikhqbfbwtwx xgmkx gjl vkbt nft mxglth jnx lj ihwx lxk tebobtwt vhf nf mhjnx.",
	"24677": "Ebgh, vtg B tvvhfitgr rhn? Gh. Par? Uxvtnlx B whg'm ptgm mh lmxte tgr fbgnmx hy rhnk rhnma ykhf rhn.",
	"24678": "Ixhiex pbma dbwl hk lhfx hy fr ykbxgwl  teptrl vhfx ni mh fx tgw maxr ltr Ebgh rhn zhm mh atox t dbw uxlm mabgz b xoxk wbw. Rxta hy vhnklx rhn'kx zhbgz mh ltr matm tuhnm rhnk bkkxoxklbuex wxvblbhg Maxr'kx cnlm mkrbgz mh lnyyxk fx bgmh maxbk gbzamftkx.",
	"24679": "Ixhiex cnlm ehox mkr mh zxm bg fr ldbg... ngyhkmngtmxer matm bl ebdx max 90'l hk 2d'l ghp! Lxkobvx Ngtotbetuex. Mkr tztbg, Gxoxk.",
	"24680": "By rhn gxxw b ebdx'rhn exll rhn whg'm gxxw mh zbox'rhn mh lh fnva mkhnuex.",
	"24681": "Wtfg'bm. B ebox'bm mbee b wbx.",
	"24683": "Cnlm eblmxg ni fr zxgxktmbhg pxgm mh max fhhg, px bgoxgmxw max vhfinmxk tgw max vxee iahgx, px pxkx max Uxtmexl tgw Wtobw Yhlmxk Pteetvx tgw Ftkztkxm Tmphhw tgw Obtzkt tgw max Anet Ahhi tgw B atox xtkgxw max kbzam mh bwxgmbyr pbma rhn tl ebmmex tl B ptgm.",
	"24682": "B'f atiir ebdx tg iniir ebdbgz tee max ytvx.",
	"24683": "Cxtehnlr bl t ynggr mabgz. Max zbke whxlg'm vtkx by bm'l axkl hk ghm. Patm lax bglblml hg bl matm ax uxehgzl mh gh hgx. Lax'l cnlm ebdx matm, ltkvtlmbv, bkhgbv, cxtehnl. Tm extlm lax whg'm ikxmxgw mh ux t ixklhg lax blg'm, lax bl patm lax bl, uxlbwx axk tll.. bm'l ebdx tg hgbhg, xtm bm tgw vkr yhk fhkx. Cxtehnl ?! B'f ghm.",
	"24684": "B ptl mtedbgz mh lhfxhgx B dghp tuhnm par B ikxyxk mh atox t pxulbmx, mabl pxulbmx. By whg'm ptgm mh dghp hk kxtw bm: — whg'm vhfx axkx, lbfiex, gh gxxw mh uehvd, ngykbxgw tgw tee max hmaxk mabgzl ixhiex tkx lnucxvmxw mh maxlx wtrl tgw ghm cnlm lhvbhehzbvteer. Axkx rhn whgm dghp pah tkx fr ykbxgwl, patm maxr ihlm, whbgz, paxkx b tf hk tgrmabgz b whgm ptgm mh tgw ux 'bfihlxw'. B vtg atox lnixkmlmtk ykbxgwl... Maxr tkx ikhmxvmxw, lh tf B tgw B'f lnkx bm'l ghm t ytdx uehgw pxtgxw vtey. B mabgd matm bg fr mbfx mabgzl pxkx lbfiexk, unm tl B ltr tgw atox teptrl ltbw, anftg uxbgzl teptrl vhfiebvtmx mabgzl, xoxg lbfiex mabgzl tgw lhfxmbfxl maxr vtee'maxf ikhzkxll... rxa, rxa, uetfx 'max mbfx', lnkx. B'f zhhw.",
	"24685": "Yhk fx, Ltbgm Otexgmbgx'l Wtr pbee ux fr ptr, tl B ptgm, temahnza B gh ehgzxk vtkx fnva tuhnm max wtr, bm'l cnlm vhffxkvx (bg ytvm mh fx, tee mabl wtmxl tkx ghmabgz fhkx matg lmktmxzbver vkxtmxw tl t vhz bg max xvhghfr tgw vhglnfxkblf). Phkkr tuhnm rhnklxey, rhn atox fhkx phkkbxl matg B wh... Lhkkr, ghm lhkkr, B'f ngtotbetuex.",
	"24686": "B mabgd bm wkboxl axk vktsr max ytvm matm lax fbllxl paxg B pkhmx mahlx xkhmbv lmhkbxl tgw ftwx axk zh hg mkxtlnkx'l angm'l.",
	"24687": "B'ox tekxtwr ltbw bm tgw B'ee ltr bm tztbg ehnw tgw vextk, bg twwbmbhg mh patm B'ox tekxtwr pkbmmxg tuhnm max lnucxvm bg lxoxkte hy fr tldtkw'l tgw uktbgvtgwr'l: Bm phg'm ux ehgz uxyhkx mhtlmxkl tgw lahpxkl pbee atox TB. Mabl xqvknvbte mabgz tuhnm anftg uxbgzl mtdbgz xoxkrmabgz mh max xqmkxfx tgw xqtzzxktmbhg bl matm maxkx lxxfl mh ux gh vnkx, hk gh TB matm ybq'bm 'tgw px tkx huebzxw mh atox'maxf'.",
	"24688": "Tmz ytetot gh mxn bwbhft ftl... Yhb h jnx xet wbllx tatata. Gbgznzf zhlmt ftbl wx md wh jnx xn.",
	"24689": "Ghmt-lx jnx tgwtl t ikxvbltk. Hukbztwh, gh vtlh wx ikxvbltk xn tztkkh-fx xf jnxf tl mxf. Tatata",
	"24690": "Bl mabl zehp? Gh bml t U. Bkhgbv! Ebdx lbed.",
	"24691": "Rxta wnwx zbkel ebdx Uktw Ibmm vhl ax vtkx'l tuhnm Uktzt. Pxkx wt ynvd wh rhn ebox?!",
	"24692": "Lax whxlg'm etvd jntebmbxl tgw oxkltmbebmr uxlbwxl uxbgz t phftg pbma t P. Tee lax atl mh wh bl hixg axk exzl.",
	"24693": "B vtg ftdx hk zbox axk lhfxmabgz mh inm paxkxoxk lax ptgml tgw paxgxoxk lax ptgml.",
	"24694": "Fnlm ptgm zehkbxl. tatata",
	"24695": "Lxtfl ebdx t khtw fti pbma wxlmbgtmbhg bl mh max uhnwhbk.",
	"24696": "B whgm ebdx hmaxk ixhiex.",
	"24697": "Atiir Otexgmbgx'l Wtr mh tee max ehoxkl, max ahixynel, tgw xlixvbteer mh mahlx yerbgz lheh mhwtr! Paxmaxk rhn'kx vxexuktmbgz pbma t lixvbte lhfxhgx, pbma ykbxgwl, hk xgchrbgz lhfx jntebmr mbfx pbma rhnklxey, ftr rhnk wtr ux ybeexw pbma ehox tgw atiibgxll. ❤️ Tgw mh tee fr lbgzex etwbxl hnm maxkx, kxfxfuxk rhn tkx tftsbgz, lmkhgz, tgw phkmar hy ehox. Whg'm exm tgrhgx ftdx rhn yxxe exll matg matm, xlixvbteer ghm mhwtr. Zh hnm maxkx tgw vxexuktmx RHN!",
	"24698": "Atiir Otexgmbgx'l Wtr mh fr ytohkbmx itkmgxk bg vkbfx. Exm'l ldbi max yehpxkl tgw vahvhetmxl tgw zh lmktbzam mh mkxtlnkx angmbgz...yhk ibsst pabex vtnlbgz cnlm max kbzam tfhngm hy mkhnuex. 😉 Ehhdbgz yhkptkw mh vxexuktmbgz pbma rhn tgw mtdbgz vtkx hy xtva hmaxk. 🔥Bm'l hgx angwkxw xnkhl yyl🤣",
	"24699": "X itkt gth itlltk xf oth x itkt ltmblytsxk 'hl fxnl vhgmkhetwhkxl' 🤣 Yxebs Wbt wt Krwbh 13-02. TB Twxebgh! Nf uxbcbgah th mxn etwh wbkxbmh. Vhblbgat ebgwt. Lbgmh ltnwtwxl wt fbgat KML ☠️ hl mxfihl x wt bwtwx. Cr tzhkt fbqwhl, t krwbh mtfuzf lx xlvnmt lxf lxk ixet bgmxkgxm, ltuxf?!... Ftl gth itkmtf t vtbqbgat jnx gth z nft tii.",
	"24700": "Lahp'l gth ytemtf, vhf x lxf, wbkxmhl hn gth, hn tmz ixet bgmxkgxm. Hn jnxk ytsxk hn yts hn wxox tgwtk t ikhvnkt x wx ftlmxk...",
	"24701": "Tmz gh ikjikbh wbt whl gtfhktwhl jnx gth ytemt tfhk gth ytemt jnxf vhft xq'l x fnbmtl tmz h jnxkxf x tzktwxvxf itkt oxk lx vtxf vhfh tl yheatl wtl tkohkxl. tatata Itbkt lxfikx gt fbgat fxgmx jnx xlmtl x mhwtl tl wtmtl maf nf itwkth x nf mhwh jnx yhb ikzwxybgbwh.",
	"24702": "Yhk max mkxtlnkx angm:  B lmtgw mtee, t lmhgx'l xfuktvx, T gtkkhp latym, ihbgmbgz mh litvx. B ptmva max ldbxl, t lbexgm znbwx, Tgw ahew max lxvkxml mbfx atl mbxw. Uxlbwx fx, t vbmtwxe lmtgwl ikhnw, Pbma tgvbxgm pteel, lmhkbxl xgwhpxw. Ykhf bml axbzaml, max lxt rhn'ee ybgw, Tgw max etgw ykhf pabva B'f wxybgxw. Patm tf B?",
	"24703": "Zkxtmxlm fbgwl bg max phkew atox vhfx mhzxmaxk mh ybznkx hnm max huobhnl.",
	"24704": "By rhn lahp fx rhn whg'm zbox t wtfg, B pbee lahp rhn b tf uxmmxk tm bm.",
	"24705": "Xbmaxk tww hg mh fr zkxtmgxll hk cnlm zxm max axee hnm.",
	"24706": "Max hger mabgz B ptgm mh kxtw mabl mbfxl bl wkbgd bg fhwxktmbhg tgw kxlihglbuer ykhf fr uhmmex'l.",
	"24707": "Maxkx vhfxl t mbfx paxg bwxhehzr fxxml kxtebmr xoxg bg rhnk unlbgxll...",
	"24708": "Lhfxmabgz tuhnm rhn kxfbgwl fx hy max etlm phftg B ptl pbma.",
	"24709": "Whg'm mkr fx, b'f max dbgwxlm knwx ixklhg rhn pbee xoxk fxxm.",
	"24710": "Ebdx ybkxphkdl... B ehox uxbgz fx, Bm ibllxl hyy tee max kbzam ixhiex.",
	"24711": "Lax nlxw mh lnvd fr gxvd tgw hmaxk mabgzl ebdx t ytvdbgz tptdxgbgz otfibkx.",
	"24712": "B tf pah max zxm'tptr. Pah rhn whg'm ynvd pbma.",
	"24713": "B atox vhfitmbhg, ghm fxkvr.",
	"24714": "Fx !# ?! Matm bl t frma. Ikhox'bm. Vhl b vtg pabva B'f ghm.",
	"24715": "Max lnffbm'l uxtnmr kxitrl max tkwnhnl tlvxgm.",
	"24716": "B atox t lnkikblx yhk rhn, unm rhn gxxw mh ngpkti bm yhk fx.",
	"24717": "B tf lhkkr by rhn whg'm ebdx fr ahgxlmr, unm mh ux ytbk b whg'm ebdx rhnk ebxl.",
	"24718": "Rxta! Rxta Rxtal , b dghp rhn ptgm'fx. Bm'l Q ftzbv 🎶",
	"24719": "B teeptrl pbee ux rhnkl 'fb vtvahgwbmt lxqr mxkfbgtmhk'.",
	"24720": "Max kxtlhg mph ixhiex lmtr mhztmaxk bl matm maxr zbox xtva hmaxk lhfxmabgz ghuhwr xelx vtg.",
	"24721": "Enqnkr atl gxoxk tiixtexw mh fx, b ebdx lbfiex mabgzl, uhhdl, uxbgz tehgx, hk pbma lhfxuhwr pah ngwxklmtgwl.",
	"24722": "Rhn hg mhi hy fx matm'l t ytgmtlr gxoxk zhggt atiixg unm hmaxkl B'f ghm ltrbgz gh...",
	"24723": "H fxn vtkgtote?! — Otb lxk tezxftwh t nft vtft gth or nft wbtubgat fx ihllnbk. 😂 Ihk bllh h vxkmh z jnx gth xlmtkxb wblihgdoxe.",
	"24724": "X wbllx xet: 'Twxebgh, xlmtl lth wtl jnx xn zhlmh, zktgwxl x etkztl'. — 😂 Zhlmtl ihnvh zhlmtl. vt..otvtl!, lx jnbsxkxl ftbl xn whn-mx.",
	"24725": "Vhfh ikxob x fxgvbhgxb xf mxqmhl jnxk gh uktbgvtgwr jnxk xf tldtkw'l xq: #23264, hl lnixkfxkvtwhl bgmxebzxgmxl, bfinelbhgtwhl ihk BT x lxf bgmxkoxgxth anftgt, cr lth nft kxtebwtwx. Xfuhkt tbgwt gth nmbebsxf kxvhgaxvbfxgmh ytvbte xf etkzt xlvtet, vhfh t mxvghehzbt jnx cr xqblmx (t 100df wx wblmsgvbt, gh ynmnkh obt ltm), jnxlmbhgh-fx tmz hgwx exotkxfhl hl xqmkxfhl. Tybkfxb jnx t anftgbwtwx mxgwx t xqtzxktk, x itkxvx jnx tezngl vhfxxtf t vhgvhkwtk. Yxebsfxgmx, gth oxkxb h wxlyxvah wblmh, cr ybs t fbgat itkmx...",
	"24726": "Rxl, B dghp matm vhgmkhe vtg ux whgx bg ftgr ptrl, hgx hy maxf bl vebvdl hk tiil ghm ixkyhkfbgz vxkmtbg yngvmbhgl tgw max kxjnbkxfxgm mh rhn mh nlx'maxf bg rhnk etimhi tl atl uxxg max vtlx bg kxvxgm wtrl pbma Vakhfx tgw vatgzbgz max iahmh hg max bftzx yktfx ykhf zhhzex iahmhl lxexvmbhg. Ghp tgw mhwtr phkdl... Ghp tgw mhwtr B ngwxklmtgw par.",
	"24727": "Lx otbl lxznbk h xqxfieh wt ehbkt xf tsne hn gth gth z ikhuexft fxn gxf gngvt lxkr. Tikhoxbmt jnx h vtkgtote z vhehkbwh x #y00 x gh vtkgtote gbgznzf exot t fte, cr wbs h wbmtwh. Ftl gth jnxkxgwh gxf mxgwh gtwt t oxk vhf h bllh hn tllngmh, — Mhft hl fxw'l jnx bllh itllt-mx.",
	"24728": "B mabgd matm mxvaghehzr tgw mabl gxp zxgxktmbhg tkx wblixeebgz frlmxkr tgw ghm cnlm matm hy ixhiex, extobgz nl pbma t phkew paxkx xoxkrmabgz bl dghpg, mktglitkxgm tgw ikxwbvmtuex. Paxkx bl max ftzbv hy frlmxkr tl t litkd hy tgw mh max bftzbgtmbhg?",
	"24729": "Mkrbgz mh tohbw max bgxobmtuex bl ebdx mkrbgz mh bfikblhg mbfx.",
	"24730": "Whg'm lxx mabl tl t ehll, lxx bm tl tg hiihkmngbmr. Rhn'ox ikhoxg patm rhn vtg tvabxox. Ghp, bftzbgx patm xelx rhn'kx vtituex hy wblvhoxkbgz.",
	"24731": "Lhfx bgcnkbxl axte fhkx jnbvder by rhn dxxi fhobgz.",
	"24732": "Max wtr rhn mabgd rhn atox kxtvaxw rhnk yneexlm ihmxgmbte bl max wtr matm rhn atog'm.",
	"24733": "Xn gth lhn nf wxexl. Ixglh jnx: — T ebuxkwtwx wx xlvheat z nf ikxlxgmx otebhlh, ftl t xlvheat wx lxznbk t fnembwth lxf jnxlmbhgtk ihwx mktglyhkftk xllx ikxlxgmx gnft vhkkxgmx jnx ghl tikblbhgt q fxwbhvkbwtwx.",
	"24734": "Max bgmxkgxm, t lmtzx paxkx kxtebmr bl wblmhkmxw, tgw max lxtkva yhk otebwtmbhg mnkgl bgmh t ztfx hy ftldl, paxkx xtva ixklhg ietrl max khex matm uxlm lnbml maxf.",
	"24735": "Jnx t texzkbt x tl vhkxl obuktgmxl wh Vtkgtote x wh Ftkwb Zktl bgngwxf hl ohllhl wbtl, vhf fqlbvt, wtgxt x vxexuktxth lxf ybf! Jnx t yxlmt lxct bgxljnxvdoxe, lxct xf Ihkmnzte, gh Uktlbe, xf Ghot Hkextgl hn xf jntejnxk vtgmh wh fngwh hgwx t yhebt kxbgtk!",
	"24736": "B ebdx mh lxx max wbyyxkxgvx uxmpxxg patm bl ltbw tgw patm bl kxteer fxtgm hk bm'l axtkw.",
	"24737": "Gth ytemt zxgmx t jnxkxk ltuxk!  lbmbh itkt xlmtk hn ybvtk, jnte z x wx jnx lth vhfihlmhl hl fxnl atoxkxl. Ihwxf bk xfuhkt, gth ixkvtf mxfih... Gxf ltuxf h uxf jnx xlmhn x ehgzx.",
	"24738": "B dghp rhn ixhiex mabgd b'f dbgwt t khvdlmtk unm mabl bl kbwdvnehl.",
	"24739": "B'f tg tlmkhgtnm ehhdbgz yhk t gxp fbllbhg uxvtnlx mabl ietgxm tgw mabl anftgbmr uhkxl'fx, tghrl'fx.",
	"24740": "Vhfh eh wbvx Otezkbt: Unxgh, fxchk tkkxixgmbklx, wh jnx jnxwtklx vhg etl ztgtl.",
	"24741": "Ta, lhgahl bkkxtebsroxbl...t fbgat xlixvbtebwtwx! T eblmt vkxlvx ftbl kribwh jnx t fbgat vhgmt utgvrkbt wbfbgnb. X mn, zl h bmxf ftbl vtkh.",
	"24742": "'Ltuzl vnre xl fb itkmx ytohkbmt?, xe vngbebgznl wxe vtidmneh gnxox.'",
	"24743": "Gt fbgat obwt, mhwhl hl wbtl lth nft yxlmt mxfrmbvt x vhfihlmt wx 'wbtuknktl' x mn lxkrl t ftbl wxebvbhlt wxetl. Gh fxn kxbgh wx iktsxkxl ikhbubwhl, lxkrl t mxgmtxth jnx xn mtgmh xlixkh.",
	"24744": "Ngt wx etl vhltl jnx fx xgvtgmt oxkmx atvxkeh. Chwxk mbt jnx unxgt xlmtl!",
	"24745": "Xoxg hg max phklm wtrl rhn/B khvd 😉😘",
	"24746": "Max kxtlhg par rhn yxee yhk fx lh atkw bl uxvtnlx b'f ghm ebdx max kxlm.",
	"24747": "'Tezh vhgmbzh, ihjnbmh t ihvh', jnz lhr ng gbhh obxch. tatata",
	"24748": "Max bgmxkgxm yhk fx bl yhk wrgtfbv nlx, ghm yhk vhglmtgm nlx.",
	"24749": "'😂 Maxr mabgd uxvtnlx maxr tkx uxtnmbyne b whg'm dbee'maxf.'",
	"24750": "'Rhn dghp max knex, Gh iahgxl. Rhn atox mh extkg mh tvmnter wh mabgzl ghm ptmva.'",
	"24751": "'Hgx hy fbgx'l, ghmabgz, matm bl ghm.'",
	"24752": "Bm'l ghm xoxg fr ubkmawtr rxm tgw 'xoxkrhgx' bl tekxtwr 'vktsr' hk 'mh zxm ynvdxw'. B phg'm ux totbetuex mh tgrhgx xqvxim hgx ixklhg. — Frlxey. Wh rhn atox tgr ikhuexf pbma matm?! Vhl b lnkx whg'm. Wxte pbma'bm.",
	"24753": "Lax dghpl b ptl max uxlm mabgz pah atiixgl tgw lahp bg axk ebyx gh ftmmxk patm.",
	"24754": "Gh hgx vtg vtmva patm maxr vtgghm lxx.",
	"24755": "Patm px wbw vtgghm ux yhngw bg tgr Ubuex.",
	"24756": "Vtkbhh, ltuxl jnx ljeh mxgzh hchl itkt mb. Mx oxh axkfhlbllbft gxllt yhmh. Fx xgvtgmtl.",
	"24757": "Bg fr tzx mbfx bl ikxvbhnl.",
	"24758": "Zktmbmnwx ikhmhvhel tvmbotmxw. Mh tee tkvabmxvml (!#) hy max wbzbmte wkxtflvtix matm kxgwxkxw fr Ykbwtr gbzam'l 'Max Xexvmkbv Lmtmx' xqixkbxgvx ihllbuex. Ta rxl, 'anftgbmr'l etlm lmtgw' – vhgoxgbxgmer lmkxtfxw wbkxvmer bgmh rhnk gxnkte bfietgm, lihglhkxw ur rhnk ikxyxkkxw tezhkbmaf. Xgchr max tnmaxgmbv, ikx-itvdtzxw xqblmxgmbte wkxtw, ghp pbma 20% fhkx lbfnetmxw lnglxml!",
	"24759": "Lbexgvx bl zhew ...tgw maxg rhn ybgw hnm max mkxtlnkx ptl t ukhdxg kxvhkw ldbiibgz max ltfx tgghrbgz cbgzex.",
	"24760": "Bg gtmnkx ghmabgz xqblml tehgx.",
	"24761": "Lxvhgw etp hy maxkfhwrgtfbvl xoxgmnteer xoxkrmabgz mxgwl mh labm.",
	"24762": "Ha, max ikhzkxll! B'ox uxxg 'lmnvd' tgw b ebdx'bm nlbgz Vhkxe Itbgm Lahi Qg hg Pbgwhpl 10 tgw 11 yhk rxtkl, ebdx pbgtfi o5.92 pabex max 'vnmmbgz-xwzx' lhymptkx wxftgwl zbzturmxl hy fr ikxvbhnl lmhktzx tgw fxfhkr. Bftzbgx! Fxzturmxl, ghm Zbzturmxl! Ahp jntbgm. B'f lnkx max 'bgghotmhkl' pbee lhhg ybgw lhfx 'vkbmbvte' kxtlhg mh kxgwxk maxlx ixkyxvmer yngvmbhgte mhhel hulhexmx, uxvtnlx, rhn dghp, maxr'kx ghm 'labgr' xghnza tgw mahlx 'lxvnkbmr onegxktubebmbxl' 😉😉",
	"24763": "Atox rhn xoxk mkbxw max lbfiebvbmr tgw max lixxw hy Itbgm Lahi Ikh 9 uxtmbgz max 'tee-bg-hgx' vhfiexqbmr hy Pbgwhpl 11 Iahmhl. Yhk fx matm'l t pbg pbmahnm whpglbwxl.",
	"24764": "Paxkx hgvx oteoxl whfbgtmxw pbma maxbk oblbuex ihpxk, maxg mktglblmhkl pbma maxbk xyybvbxgm lbexgvx, ghp lhymptkx kxbzgl, tg bgoblbuex zbtgm latibgz kxtebmbxl—t ihbzgtgm kxfbgwxk matm ablmhkr'l mknx kxohenmbhgl hymxg extox gh iarlbvte mktvx, hger max ikhyhngw labym bg ahp px ixkvxbox tgw bgmxktvm pbma max phkew.",
	"24765": "Rhn tld tgr zkxtm lvbxgmbybv fbgw patm maxr ptgm mh tvabxox tgw max hger ahgxlm tglpxk bl bffhkmtebmr. By rhn wblvhoxk lhfxmabgz matm vatgzxl max phkew rhn ebox yhkxoxk.",
	"24766": "Yxebs Wbt wh Itb! Mh fr wxtk hewxk ykbxgw, t mknx xqtfiex hy pblwhf, lmkxgzma tgw lniihkm, tgw mh tee fr 'ilxnwh dbwl,' pah ybee fr ebyx pbma chr. Tgw mh rhn, fr 'hewxk ukhmaxk' bg libkbm tgw vhwx, rhnk ikxlxgvx bl t vhglmtgm zbym. Mhwtr, px vxexuktmx max xgwnkbgz uhgwl hy ytmaxkahhw bg tee bml yhkfl.",
	"24767": "Likbgz'l mxfixlmnhnl tkkbote, t uteexm hy pbgw tgw ktbg, kxdbgwexl tg xgwnkbgz fxfhkr: fr fhmaxk'l dbll, t mxgwxk utef yhk vabewahhw ankml, tg xfhmbhg matm uehllhfl ixkixmnteer, fbkkhkbgz likbgz'l lhhmabgz kxextlx ykhf pbgmxk'l zktli, t lhetvx tztbglm max lmhkf. Mabl fxfhkr lmtgwl tl t ihbzgtgm vhgmktlm mh max fhwxkg kxebtgvx hg lftkmiahgxl tgw max bgmxkgxm, ghp hymxg lxxg tl max ikbftkr kxfxwbxl yhk wblmkxll.",
	"24768": "Ybox wxvtwxl tzh, bg fr vabewahhw, t vkr ptl max ngboxklte lbzgte yhk itkxgmte tmmxgmbhg. Ghp, t vkr hymxg lxkoxl tl t fxkx ikxenwx mh wxftgwbgz t lftkmiahgx hk bgmxkgxm tvvxll.",
	"24769": "Cnlm mabgdbgz tuhnm ebyx, wxtma, ytmx. Unm vtkxyne, whg'm hoxkmabgd bm—max tgvbxgm Zkxxdl wbw, tgw ehhd paxkx bm zhm maxf.",
	"24770": "Fr lbfiex ebyx?!: fr hger vhgvxkgl tkx uhkxwhf tgw vahexlmxkhe.",
	"24771": "Tl ytk b dghp Ixztlnl o2 whgm kxjnbkxl anftg bgmxkoxgmbhg.",
	"24772": "Rxlmxkwtr, mtedbgz mh t ykbxgw, px vtfx mh max maxhkxmbvte vhgvenlbhg matm max hew 'unz' ptl lmbee tiiebvtuex mhwtr pbma max Xkbvlhg ZA-337, ur ikxllbgz max utmmxkr unmmhg tgw pbmahnm ehlbgz vhgmtvm pbma max ihpxk ibgl, px kxfhox max LBF vtkw tgw inm tztbg max utmmxkr utvd mhzxmaxk. Rxl, bm ptl t dbgw hy 30lxv 'vtkw vehgx' oxklbhg matm teeptrl etlmxw t yxp ahnkl tm ftq t wtr. (rxta, mxlmxw, utvd bg mat wtrl tgw rxl max ZA-337 lmbee phkdl ebdx t vxee iahgx mabl wtrl pbma t LBF vtkw).",
	"24773": "Bg max jnbxm yxkhvbmr hy fhwxkg utmmexl, xfibkxl vknfuex bg vhwx tgw vebvdl - Fbvkhlhym ol Zhhzex, paxkx vhwx bl max utmmexybxew tgw vebvdl tkx max pxtihgl. T 'ixtvx' axew mhzxmaxk ur t ukhplxk mtu, rxm max 'Mabkmr Rxtkl' Ptk ktzxl bg max lbexgm litvxl hy max bgmxkgxm. Tgw vtnzam bg max vkhllybkx? Max nlxk, gtobztmbgz t etgwlvtix paxkx vhgoxgbxgvx tgw vhgmkhe atgz bg t 'TB wxebvtmx utetgvx?'.",
	"24773": "Haa!!! Rhnk exfhgl... maxr teeptrl ftdx'fx wkxtf. B ebdx'maxf lh fnva. aff...",
	"24774": "Rhn dghp patm? — Hibgbhg atl uxvhfx ebdx tll, ghp ixhiex zbox bm mhh fnva.",
	"24775": "Lmtmnl: Mkxtmbgz mahlx pah wxlxkox bm pxee.",
	"24776": "B vtg dbvd rhnk tll bg 5lxv: — Lhfxmbfxl xoxkrmabgz rhn ehhd yhk bg hmaxkl phfxgl, hmaxkl ybgw bg rhnkl, lh exm matm yhk lbgzex znrl ebdx fx hk wbohkvxw tgw pbwhpxkl.",
	"24777": "Rhn tkx fr gxp ytohkbmx yxxebgz.",
	"24778": "Rhnk utmmex bl fr utmmex, px ybzam mhzxmaxk.",
	"24779": "Thl ghllhl uktohl chztwhkxl, h ghllh lbgvxkh tzktwxvbfxgmh! Jnx h uktlth wx tkftl wx Ihkmnzte vhgmbgnx t ukbeatk xf vtwt obmjkbt! 🇵🇹 Hukbztwh, xjnbit! Xlmtkxb lxfikx vhf ohxal.",
	"24780": "Atkwxlm mabgz tuhnm'bm. Bm'l atkw mh inm bgmh phkwl.",
	"24781": "B tf xghnza.",
	"24782": "Rhn tkx max fhlm uxtnmbyne mabgz B dxxi bg fr lhne tgw fbgw.",
	"24783": "B ptgm rhn mh ux tee hy fr mhfhkkhpl.",
	"24784": "Paxg B'f pbma rhn, xoxkr fhfxgm bl t gxp twoxgmnkx.",
	"24785": "Exm nl pxtox hnk eboxl pbma max lng'l zxgmex ptkfma, max pbgw'l mbkxexll wtgvx, max xtkma'l gnkmnkbgz xfuktvx, tgw max ebyx-zbobgz dbll hy ktbg, ghm fxkxer tl t ftmmxk hy xvhghfr, unm tl t mxgwxk hyyxkbgz mh max ynmnkx, t ikhfblx matm hnk yhhmlmxil nihg mabl phkew extox t exztvr hy obuktgm, xgwnkbgz ebyx, t lrfiahgr hy atkfhgr pbma max oxkr ukxtma tgw yehp hy hnk ietgxm.",
	"24786": "Max wbyyxkxgvx pbma mabl pxulbmx bl matm bm whxlg'm vheexvm rhnk gnfuxk tgw vtee rhn tm ahfx.",
	"24787": "B lmbee kxfxfuxk paxg xoxg max bgmxkgxm tgw maxlx fnembgtmbhgtel vxexuktmxw Tikbe 1lm. Ghptwtrl, ghm xoxg max dbwl wh. Bm'l ghm t wtmx matm zxgxktmxl vhglnfxkblf, matm'l par.",
	"24788": "B kxfxfuxk paxg vhkihktmbhgl tgw max bgmxkgxm vxexuktmx Tikbe 1lm. Ghp maxr'kx lbexgm, mxkkbybxw hy tgw pbma 'ytdx gxpl'. Unm mh ux ahgxlm, ykhf patm B lxx, ghm xoxg max dbwl vxexuktmx max wtr maxlx wtrl. Bg fr ihbgm hy obxp, uxvtnlx bm bl ghmabgz matm zxgxktmxl vhglnfxkblf ebdx Ateehpxxg wh, yhk xq.",
	"24789": "Lpxxmaxtkm, B atox lxxg rhn zkhp ykhf t rhngz zbke mh t phftg tgw uxvhfx max ftzgbybvxgm phftg rhn tkx mhwtr. B tf lnkx matm rhn pbee gxoxk ehlx rhnk mknx bwxgmbmr, ikbgvbiexl tgw otenxl. Phfxg ebdx rhn tkx gh ehgzxk ftgnytvmnkxw tgw matm ltfx ytvmhkr atl uxxg ehlm tgw vehlxw bg mbfx. B'f lh ikhnw hy rhn, gxoxk ehlx rhnk xllxgvx. Tikbe'l yhhe !? Cnlm erbgz/wxvxbobgz pbma max mknma ;)*",
	"24790": "Tikbe'l yhhe ?! Zh ybznkx: Lbfiex tl latkbgz max zbzturmxl hy wtmt ykhf fr lftkmiahgx tgw mtuexm hg fr ikbotmx gxmphkd tm ahfx pbma fr Pbgwhpl 11 IV nlbgz max pbgwhpl xqiehkxk exym itggxe gxmphkd himbhg, pbmahnm bgmxkgxm hk uxbgz ehzzxw hg hn ftdbgz tgr ehzbg. Maxkx'l ghmabgz uxmmxk matg nlbgz max vehnw, mabl wtrl bl xtlbxk latkx obt vehnw matg mph wxobvxl pah tkx 1f tptr. wbzbmte yhhmikbgml?! Tgrpaxkx. 🧠 Uktbgvtgwr (im-im)",
	"24791": "Max Etp?! Fr gtbox mabgz... whg'm fxtg'l cnlmbvx.",
	"24792": "Hgvx nihg t mbfx, hgvx, mpbvx, makxx, tl ftgr tl rhn ptgm.",
	"24793": "Paxg b lxx uxtnmbyne mabgzl bm dxxil'fx tptdx.",
	"24794": "B'f vatgzbgz utvd mh Ebgnq (Jnuxl, Mtbel, yxwhkt) tztbg tgw nlbgz lxkobvxl ebdx Ikhmhg. Mh fnva 'vhbgvbwxgvxl'... tee kxvhkwxw tgw mktvxw utvd. 'Mabgzl' B whg'm uxebxox, lh...",
	"24795": "Patm wh B lxx tgw patm wbw B lxx? T iniixm anftgbmr matm B wh ghm bgmxgw mh ux t itkm hy, bg tgr ptr. Tgr ikhuexf pbma matm? Vhl matm B vxkmtbger whg'm atox.",
	"24796": "Max wxxixk max tmmmtvafxgm, max atkwxk max ehox.",
	"24797": "Patm t ietgx. tatata B'f cnlm twfbkbgz max bwxt hy t ghm hger uxtnmbyne ixkyxvm fhkgbgz tgw ixkyxvm gbzam.",
	"24798": "B'f kxmbkxw. Uxebxox'fx rhn gxoxk zhggt ptgm fx mh mtdx hk mnkg tgrmabgz ixklhgte.",
	"24799": "Lniihkm hmaxkl, rxm ikbhkbmbsx rhnk hpg pxee-uxbgz.",
	"24800": "VXH,HHH,HHH,HHH"
}
#----------------------------------------------------------
core['askard_ids'] = list(askards_db.keys())
askards_db_last_update = "17.02.2025"
chkdict.append(sum(sum(ord(char) for char in word) for value in askards_db.values() for word in value))

#------------------------------------------------------------
help = {
	"help askard": "Usage: <list/achk/view/show> askard <id> | <view/show/achk> askard <id/first/last>\n"+" "*7+"<achk askard <first/last/update>  | <list> askard <id start> to <id end>\n"+" "*7+"<scan> askard <word to find in askards>\nex: list askard 4004 to 4006, achk askard last, achk askard update\n    view askard 4005, scan askard 'time'\n",
	"help asteroid": "Usage <asteroid> \nDisplays basic information about the asteroid \nex: vesta\n",
	"help capital": "Usage: capital of <country> | <capital> | <country> \n\nJust type directly the <capital> to know her country, \nJust type directly the <country> to know her capital, \n<capital of <country>> to show what is that Country Capital.\n",
	"help capitals": "Usage: capital of <country> | <capital> | <country> \n\nJust type directly the <capital> to know her country, \nJust type directly the <country> to know her capital, \n<capital of <country>> to show what is that Country Capital.\n",
	"help convert": "Usage: convert <VALUE> from/days <UNIT> | seconds|minutes|hours|feets|miles|yards|AU|m3|gallons|fahrenheit \nAll the convertions are made to kilometers, litters and celcius degrees. \nex: convert 2 days, returns the number of seconds, minutes and hours of 2 days. \n    convert 2 days in hours, returns the total of hours from the number of day(s) \n    convert 2 from miles, returns the number of 2 miles in kilometers \n    convert 2 from m3, returns the number of 2 m3 (cubic meter's) in litters, \n    convert 2 from fahrenheit, returns the number of the degrees in celcius\n",
	"help dangerous asteroids": "Usage <dangerous asteroid> \nDisplays basic information about the dangerous asteroid \nex: 2011md\n",
	"help days for": "Usage: days for <Christmas/New year/Birthday> \nReturns the number of days left to the event questioned.\n",
	"help days till": "Usage: days till <Christmas/New year/Birthday> \nReturns the number of days left to the event questioned.\n",
	"help difference from": "Usage: difference from <date> \nReturns the difference between the digited date to the actual instante in years, months, days, hours, minutes, seconds.\n",
	"help distance": "Usage: distance from <planet/moon> to <planet/moon> \nex: distance from venus to moon, distance from earth to moon, distance from earth to neptune\n",
	"help distances": "Usage: distance from <planet/moon> to <planet/moon> \nex: distance from venus to moon, distance from earth to moon, distance from earth to neptune\n",
	"help find": "Usage: find <topic> \nReturns if there is any information or topic about the questioned.\n",
	"help games": "Usage: play <game> \nPlay the game you digited. \nex: play capitals \n    play constelations\n    play elements \n    play math\n",
	"help gps": "Usage: set default <gps/gps off> | show default gps \nThe default or the most used cordinates are the inserted in the <sunset/sunrise time> command.\n",
	"help linux command": "Usage: <linux command> \nShows the Syntax a shot explanation and examples for the typed linux command.\n",
	"help morse": "Usage: morse <word/phrase> \nTranslate to morse code the digited word or phrase. \nex: morse cybele\n",
	"help morse code": "Usage: morse <word/phrase> | demorse <word/phrase> \nEncode to morse code | Decode from morse code : the digited <word/phrase> \nex: morse cybele\n    demorse -.-. -.-- -... . .-.. .\n",
	"help demorse": "Usage: demorse <morse code> \nDecode from morse code the digited encode word or phrase. \nex: demorse -.-. -.-- -... . .-.. .\n",
	"help orbit acronym": "Usage <orbit acronym> \nDisplays basic information about the orbit and her principals. \nex: geo\n",
	"help orbit": "Usage: <planet> orbit / <orbit acronym> \nShow the type of the orbit from the typed planet / Displays basic information about the orbit and her principals. \nex: earth orbit\n    geo\n",
	"help presence": "Usage: presence <service> \nShow's the direct link for "+_auth1r_+" online/internet presence in the digited service. \nex: presence asus\n    presence trinket\n",
	"help planet": "Usage: <name of the planet> typed directly\nReturns some offline basic information about the planet name typed.\n",
	"help play game": "Usage: play game <capitals/constelattions/math> \nPlay the game of your choose. \n\nex: Capitals makes'you know and learn of what Country it is. \n    Constellations is given the constellation name to you anwser her designation learned thru me. \n    Math game is a memory training game with addiction, subtration and multiplication factors.\n",
	"help play": "Usage: play game <capitals/constelattions/math> \nPlay the game of your choose. \n\nex: Capitals makes'you know and learn of what Country it is. \n    Constellations is given the constellation name to you anwser her designation learned thru me. \n    Math game is a memory training game with addiction, subtration and multiplication factors.\n",
	"help phonetic": "Usage: phonetic <word/phrase> \nTransform to the NATO phonetic alphabet what is the base for HAM and Military's the word or the phrase digited. \n\nex: phonetic cybele \n",
	"help seek": "Usage: seek <topic> \nReturns if there is any information or topic about the questioned.\n",
	"help sharing about": "Usage: sharing about <tvshow name> \nDisplays a link from the specific content of the tvshow marked in the list on the TV programs page.\nThe link available is automatically copied to the clipboard.\nex: sharing about nautilus\n",
	"help sharing tvshow": "Usage: sharing tvshow \nDisplay all links availables of the tvshows duly marked on the tvshows page.\nThis option does not automatically copy the link to the clipboard.\nex: sharing tvshow\n",
	"help show me": "Usage: show me <star names/constellations or all/asteroids names/dangerous asteroids or detailed/old tech words> \nReturn the values or data for the required subject.\n",
	"help star": "Usage <star name> \nDisplays basic information about the star \nex: Polaris (knowed by north star)\n",
	"help today activity": "Usage <today activity> \nDisplays a activity for the actual year season\n",
	"help yoda say": "Usage yoda say <sentence> \nTransforms the given sentence to Yoda speach alike \nex: Yoda say the force is strong with this one\n"
}
#------------------------------------------------------------
chkdict.append(sum(sum(ord(char) for char in word) for value in help.values() for word in value))
if _cybid_ == True:
	help.update({"help list extcom": "Usage: <list extcom or extcom> \nDisplays all the commands the Cybele extention can provide.\nex: list extcom\n    extcom\n"})
	help.update({"help exit": "Usage: <exit> <quit> <:x> <:q> <x:> <q:> \nCommand to quit Cybele if you are using cmd or terminal in your OS and not an online platform.\nex: exit\n    x:\n"})
core['help'] = list(help.keys())
checksum = shift
#------------------------------------------------------------
def phonetic_alphabet(word2nato):
	natodict = {'a': 'alpha','b': 'bravo','c': 'charlie','d': 'delta','e': 'echo','f': 'foxtrot','g': 'golf','h': 'hotel','i': 'india',
		'j': 'juliet','k': 'kilo','l': 'lima','m': 'mike','n': 'november','o': 'oscar','p': 'papa','q': 'quebec','r': 'romeo',
		's': 'sierra','t': 'tango','u': 'uniform','v': 'victor','w': 'whiskey','x': 'x-ray','y': 'yankee','z': 'zulu'}
	return ' '.join([natodict.get(letter.lower(), letter) for letter in word2nato])
#------------------------------------------------------------
def morse_code(word2morse):
	morsedict = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---',
		'k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-',
		'v': '...-','w': '.--','x': '-..-','y': '-.--','z': '--..', '1': '.----', '2': '..---', '3': '...--','4': '....-',
		'5': '.....','6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '?':'..--..'}
	return ' '.join([morsedict.get(letter.lower(), letter) for letter in word2morse])
#------------------------------------------------------------
def morse_decode(morse_code):
	morsedec = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---',
		'k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-',
		'v': '...-','w': '.--','x': '-..-','y': '-.--','z': '--..', '1': '.----', '2': '..---', '3': '...--','4': '....-',
		'5': '.....','6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '?':'..--..',' ': 'SPACE'}
	decode_table = {v: k for k, v in morsedec.items()}
	symbols = morse_code.replace("   ", " SPACE ").split(" ")
	decmorse = "".join(decode_table[x] for x in symbols)
	return decmorse

#------------------------------------------------------------
def internet_onoff():

	try:
		import requests
		response = requests.get("https://www.google.com", timeout=5)
		response.raise_for_status()
		return True
	except ImportError:
		print("\n\033[1;31m 〉 " + _title_ + "\033[0;0m" + ": Error loadind standard Python module.\n   I cannot perform this task correctly.")
		return False
	except requests.exceptions.RequestException as e:
		#print('Error checking internet connection: {}'.format(e))
		return False

#----------------------------------------------------------
def copy2clipboard(text):
	command = 'echo ' + text.strip() + '| clip'
	os.system(command)

#----------------------------------------------------------
class Sun:

	def __init__(self, tz, lat, long):  # default Amsterdam
		self.lat = lat
		self.long = long
		self.when = tz
		self.__preptime(self.when)
		self.__calc()
	def sunrise(self):
		return Sun.__timefromdecimalday(self.sunrise_t)
	def sunset(self):
		return Sun.__timefromdecimalday(self.sunset_t)
	def solarnoon(self):
		return Sun.__timefromdecimalday(self.solarnoon_t)

	@staticmethod
	def __timefromdecimalday(day):
		hours = 24.0 * day
		h = int(hours)
		minutes = (hours - h) * 60
		m = int(minutes)
		seconds = (minutes - m) * 60
		s = int(seconds)
		return time(hour=h, minute=m, second=s)

	def __preptime(self, when):
		self.day = when.toordinal() - (734124 - 40529)
		t = when.time()
		self.time = (t.hour + t.minute / 60.0 + t.second / 3600.0) / 24.0
		self.timezone = 1
		offset = when.utcoffset()
		if offset is not None:
			self.timezone = offset.seconds / 3600.0
	def __calc(self):
		timezone = self.timezone  # in hours, east is positive
		longitude = self.long     # in decimal degrees, east is positive
		latitude = self.lat      # in decimal degrees, north is positive

		time = self.time  # percentage past midnight, i.e. noon  is 0.5
		day = self.day     # daynumber 1=1/1/1900

		Jday = day + 2415018.5 + time - timezone / 24  # Julian day
		Jcent = (Jday - 2451545) / 36525    # Julian century

		Manom = 357.52911 + Jcent * (35999.05029 - 0.0001537 * Jcent)
		Mlong = 280.46646 + Jcent * (36000.76983 + Jcent * 0.0003032) % 360
		Eccent = 0.016708634 - Jcent * (0.000042037 + 0.0001537 * Jcent)
		Mobliq = 23 + (26 + ((21.448 - Jcent * (46.815 + Jcent * \
				(0.00059 - Jcent * 0.001813)))) / 60) / 60
		obliq = Mobliq + 0.00256 * cos(rad(125.04 - 1934.136 * Jcent))
		vary = tan(rad(obliq / 2)) * tan(rad(obliq / 2))
		Seqcent = sin(rad(Manom)) * (1.914602 - Jcent * (0.004817 + 0.000014 * Jcent)) + \
			sin(rad(2 * Manom)) * (0.019993 - 0.000101 * Jcent) + sin(rad(3 * Manom)) * 0.000289
		Struelong = Mlong + Seqcent
		Sapplong = Struelong - 0.00569 - 0.00478 * \
			sin(rad(125.04 - 1934.136 * Jcent))
		declination = deg(asin(sin(rad(obliq)) * sin(rad(Sapplong))))

		eqtime = 4 * deg(vary * sin(2 * rad(Mlong)) - 2 * Eccent * sin(rad(Manom)) + 4 * Eccent * vary * sin(rad(Manom))
				* cos(2 * rad(Mlong)) - 0.5 * vary * vary * sin(4 * rad(Mlong)) - 1.25 * Eccent * Eccent * sin(2 * rad(Manom)))

		hourangle = deg(acos(cos(rad(90.833)) /
						(cos(rad(latitude)) *
						cos(rad(declination))) -
						tan(rad(latitude)) *
						tan(rad(declination))))

		self.solarnoon_t = (
			720 - 4 * longitude - eqtime + timezone * 60) / 1440
		self.sunrise_t = self.solarnoon_t - hourangle * 4 / 1440
		self.sunset_t = self.solarnoon_t + hourangle * 4 / 1440

#-----------------------------------------------------------------------
# Moon fases calculation
class MoonPhase:
    def __init__(self, latitude, longitude, date):
        self.latitude = latitude
        self.longitude = longitude
        self.date = date

    def phase_of_moon(self):
        jd = (self.date - datetime(2000, 1, 1)).total_seconds() / 86400 + 2451545.0
        L = (218.316 + 13.176396 * jd) % 360
        M = (134.963 + 13.064993 * jd) % 360
        F = (93.272 + 13.229350 * jd) % 360
        l = L + 6.289 * math.sin(math.radians(M))
        b = 5.128 * math.sin(math.radians(F))
        r = 385001 - 20905 * math.cos(math.radians(M))

        obl = 23.439 - 0.0000004 * jd
        x = r * math.cos(math.radians(l))
        y = r * math.cos(math.radians(obl)) * math.sin(math.radians(l))
        z = r * math.sin(math.radians(obl)) * math.sin(math.radians(l))

        ra = math.atan2(y, x)
        dec = math.asin(z / r)

        lst = (100.46 + 0.985647352 * jd + self.longitude) % 360
        ha = (lst - ra) % 360
        phase_angle = math.degrees(math.acos(math.sin(math.radians(self.latitude)) * math.sin(math.radians(dec)) + math.cos(math.radians(self.latitude)) * math.cos(math.radians(dec)) * math.cos(math.radians(ha))))

        if phase_angle < 90:
            return "Waxing Crescent"
        elif phase_angle < 180:
            return "First Quarter"
        elif phase_angle < 270:
            return "Waxing Gibbous"
        else:
            return "Full Moon"

#---------------------------------------------------
# pre harvesine / pregpsconvert
def pregpsconvert():

	print("\n" + "〉" + "Convert GPS to distance")
	while True:
		if _poigps_[3] == 0:
			try:
				print("\n" + "〉" + kolor['GREEN'] +" Point of origin "+kolor['OFF'])
				latgps = float(input('   Latitude coordinates (ex 39.4487): '))

				if latgps > 90 or latgps < -90:
					print("\nLatitude value degrees must be between -90 and 90.\n")
					continue
				longps = float(input('  Longitude coordinates (ex -8.0376): '))
				if longps > 180 or longps < -180:
					print("Longitude value degrees must be between -180 and 180.\n")
					continue
			except ValueError:
				print("The entered data is invalid not recognized for the requested task!\n")
				break
		else:
			print("\n" + "〉" +kolor['RED']+" [Assumning default gps values as Origin] "+kolor['OFF'])
			latgps = int(_poigps_[0])
			longps = int(_poigps_[1])

		try:
			print("\n" + "〉" + kolor['GREEN'] +" Point of destination "+kolor['OFF'] )
			lat2gps = float(input('   Latitude coordinates (ex 35.8806): '))
			if lat2gps > 90 or lat2gps < -90:
				print("\nLatitude value degrees must be between -90 and 90.\n")
				continue
			lon2gps = float(input('  Longitude coordinates (ex 76.5151): '))
			if lon2gps > 180 or lon2gps < -180:
				print("Longitude value degrees must be between -180 and 180.\n")
				continue
		except ValueError:
			print("The entered data is invalid for the requested task!\n")
			break

		distancekm = distance_gps(latgps, longps, lat2gps, lon2gps) / 1000
		if int(distancekm) > 0 or int(distancekm) < 100000:
			print("\n"+kolor['RED'] +"〉"+ kolor['OFF'] +" The distance between the two points provided is " + str('{:,.1f}'.format(distancekm)) + " kilometers.")
			print("  ( approximately ≈ " + str( convert_to_words(int(distancekm) + 1) ) + " kilometers )\n")
			return False

#---------------------------------------------------
# Harvesine
#
def distance_gps(lat1, lon1, lat2, lon2):

	radius_of_earth = 6371000  # kilometers
	d_lat = math.radians(lat2 - lat1)
	d_lon = math.radians(lon2 - lon1)
	a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
	c = 2 * math.asin(math.sqrt(a))
	distance = radius_of_earth * c
	return distance

#---------------------------------------------------
def days_in_year():
	year = date.today().year
	if year % 4 != 0:
		return 365
	elif year % 100 != 0:
		return 366
	elif year % 400 != 0:
		return 365
	else:
		return 366

#---------------------------------------------------
def convert_to_words(num):

	ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	if num == 0:
		return "zero"
	elif num< 0:
		return "minus " + convert_to_words(abs(num))
	elif num< 10:
		return ONES[num]
	elif num< 20:
		return TEENS[num - 10]
	elif num< 100:
		return TENS[num // 10] + (" " + convert_to_words(num % 10) if num % 10 != 0 else "")
	elif num< 1000:
		return ONES[num // 100] + " hundred" + (" and " + convert_to_words(num % 100) if num % 100 != 0 else "")
	elif num< 1000000:
		return convert_to_words(num // 1000) + " thousand" + (" " + convert_to_words(num % 1000) if num % 1000 != 0 else "")
	elif num< 1000000000:
		return convert_to_words(num // 1000000) + " million" + (" " + convert_to_words(num % 1000000) if num % 1000000 != 0 else "")
	#elif num< 1000000000000:
	#	return convert_to_words(num // 1000000000) + " billion" + (" " + convert_to_words(num % 1000000) if num % 1000000 != 0 else "")
	else:
		return "  〉 That's a big number for me to spell out for you.\n     Try smaller then eight zeros, yes smaller then hundred millions."
	return words

#----------------------------------------------------
def drawart(artname):
	print (kolor['OFF'])
	if artname == 'art_cybele' and _cybid_ == True:
		random_color = random.choice(list(kolor.keys()))
		if random_color == 'DARK_BLACK' or random_color == 'BLACK' or random_color == 'WHITE':
			random_color = 'RED'
		artcor = kolor[random_color]
		art = art_cybele
	elif artname == 'art_world':
		artcor = kolor['BLUE']
		art = art_world
	elif artname == 'art_py':
		artcor = kolor['GREEN']
		art = art_py
	else:
		randomcolor = ['RED','BLACK','DARK_MAGENTA','DARK_GREEN']
		artcor = kolor[random.choice(randomcolor)]
		art = art_cybele
	#print ('\n')
	for i in range(len(art)):
		res = ''.join(map(chr, art[i]))
		if i == 5 and artname == 'art_cybele':
			print (artcor + str(res) + kolor['DARK_YELLOW'] + ''.join(map(chr, art_byas)))
		else:
			print (artcor + str(res))
	print (kolor['OFF'])

#---------------------------------------------------
def scan_askards(query):
	results = []
	for sdb, text in askards_db.items():
		if query.lower() in managedb(text.lower(), shift):
			results.append(sdb)
	return results

#---------------------------------------------------
def daysweeks_year():
	today = date.today()
	year_start = date(today.year, 1, 1)
	year_end = date(today.year, 12, 31)
	total_days = (year_end - year_start + timedelta(days=1)).days
	weeks = total_days // 7

	return [ total_days, weeks ]

#---------------------------------------------------
def leapyear():
	year = int(datetime.now().strftime("%Y"))
	result = ''

	if (year % 400 == 0) and (year % 100 == 0):
		result = "This year ({0}) is a leap year.\n".format(year)
	elif (year % 4 ==0) and (year % 100 != 0):
		result = "This year ({0}) is a leap year.\n".format(year)
	else:
		result = "This year({0}) is not a leap year\n".format(year)
	return result

#---------------------------------------------------------------------------
#-------------------------------------------------------------------
# cybele Core and sub-cores
#-------------------------------------------------------------------
#---------------------------------------------------------------------------
def get_question():
	qt = input( _title_ + "? 〉")
	if qt.isupper():
		print("Can you please stop shouting! \nIf you're writing, unless your keyboard has a problem, I understand very well.\n")
		question = qt.lower()
	try:
		if float(qt):
			print(convert_to_words(int(qt))+"\n")
			qt = ''
		if str(qt):
			return qt.lower()
	except ValueError:
		return qt.lower()
	return qt.lower()

def find_answer(question,whatlist):
	pontuation = [".",",","!","?"]
	for p in range(len(pontuation)):
		question = question.replace(pontuation[p],"")
	for index, value in enumerate(whatlist):
		if question.lower() == value.lower() or question.lower() == value.lower().replace("?",""):
			return answers[index]+"\n"
	sayhi = core.get("greatings", [])
	dict_climate = core.get("climate dictionary", [])
	dict_astro_keys = ["astronomy glossary", "constelattion", "planet", "qa-astro", "primary moon phase", "secondary moon phase"]
	dict_astro = [item for key in dict_astro_keys if key in core for item in core[key]]
	others_keys = ["country", "capital", "months", "seasons", "old_tech_term", "word meaning", "askard_command", "help"]
	others = [item for key in others_keys if key in core for item in core[key]]
	alldict = others + questions + sayhi + dict_climate + dict_astro
	is_correct, suggestions = spell_check(question, alldict)
	if suggestions:
		output_string = "Did you mean: "
	else:
		output_string = ""
	for i, suggestion in enumerate(suggestions):
		if i < 3:
			if _cybid_ == True:
				output_bycyid = ""+kolor['YELLOW']+suggestion.capitalize() + kolor['OFF'] + " or "
			else:
				output_bycyid = ""+kolor['DARK_MAGENTA']+suggestion.capitalize() + kolor['OFF'] + " or "
			output_string += output_bycyid
			csugestions.insert( 0, suggestion)
	return output_string[:-4] + "\n"

#----------------------------------------------------------------
#----------------------------------------------------------------
def spell_check(word, word_list):

	word = word.lower()
	if word in word_list:
		return True, []
	suggestions = []
	min_distance = float('inf')
	for correct_word in word_list:
		distance = levenshtein_distance(word, correct_word)
		if distance < min_distance:
			min_distance = distance
			suggestions = [correct_word]
		elif distance == min_distance:
			suggestions.append(correct_word)
	return False, suggestions

#----------------------------------------------------------------
def levenshtein_distance(a, b):

	n, m = len(a), len(b)
	dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
	for i in range(n + 1):
		dp[i][0] = i
	for j in range(m + 1):
		dp[0][j] = j
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if a[i - 1] == b[j - 1]:
				cost = 0
			else:
				cost = 1
			dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
	return dp[n][m]

#---------------------------------------------------------
def make_sentence():

	knowledge = {
	"pronoun":	["I","you","he","she","it","we","they","me","you","him","her","it","us","them","mine","yours","his","hers","its","ours","theirs"],
	"not asverb":	["is","was","are","were","am","have","had","has","will","would","should","can","could","may","might","must","ought","need","dare","used","be"],
	"contration":	["Can't","cannot","Don't","do not","Didn't","did not","Shouldn't","should not","Wouldn't","would not","Couldn't","could not","Mustn't","must not","Haven't","have not","Hasn't","has not","Couldn't have","could not have","Shouldn't have","should not have","Wouldn't have","would not have","Mustn't have","must not have"],
	"preposition":	["about", "above", "across", "after", "against", "along", "among", "around", "at", "before", "behind", "below", "beneath", "beside", "between", "by", "concerning", "despite", "down", "during", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "opposite", "out", "outside", "over", "past", "regarding", "round", "since", "through", "to", "toward", "under", "until", "up", "upon", "with", "within", "without"],
	"conjunction":	["and", "but", "or", "nor", "yet", "so", "for", "because", "although", "though", "while", "since", "as", "until", "when", "where", "if", "whether", "that", "who", "which", "what", "wherever", "whoever", "whichever", "whomever"],
	"noun":	["person", "place", "thing", "idea","animal", "object", "event", "feeling", "action", "substance","food", "drink", "color", "shape", "number", "sound", "time","information", "equipment", "tool", "machine", "vehicle","clothing", "material", "plant", "flower", "fruit", "vegetable","disease", "injury", "emotion", "thought", "memory", "dream",
			"symbol", "sign", "message", "communication", "system", "structure","country", "city", "town", "village", "building", "room","government", "law", "religion", "culture", "society", "economy","art", "music", "literature", "science", "technology", "mathematics","game", "sport", "competition", "hobby", "skill", "ability",
			"knowledge", "wisdom", "belief", "faith", "opinion", "attitude","experience", "adventure", "journey", "discovery", "achievement","problem", "solution", "question", "answer", "issue", "argument","debate", "discussion", "conversation", "talk", "speech","writing", "book", "article", "poem", "story", "letter", "email","website",
			"internet", "computer", "phone", "television", "radio","world", "universe", "galaxy", "star", "planet", "moon", "sun","air", "water", "earth", "fire", "sky", "cloud", "rain", "snow","wind", "mountain", "river", "lake", "ocean", "forest", "desert","island", "jungle", "beach", "animal", "bird", "fish", "insect","mammal", "reptile",
			"amphibian", "invertebrate", "dog", "cat", "horse","cow", "pig", "sheep", "chicken", "snake", "lizard", "frog", "butterfly","bee", "fly", "spider", "worm", "tiger","elephant","book","food","tvshow","rainbow","computer","science","mathematics","reverse","water","ocean","cybele","ecologic","nature","beach","discrete",
			"hackneyed","resilient","tenacious","humble","abstinence","affable","aloof","auspicious","bombastic","candid","capricious","cryptic","didactic","discreet","disparate","dolorous","duplicity","esoteric","euphemism","fiat","flaccid","florid","furtive","gravitas","laconic","levity","lexical","lucid","mercenary","mercurial","meticulous",
			"modicum","neologism","opaque","oxygen","sedution","sexy","gorgeous","vigilant","ask","cat","dog","eye","fun","hat","key","man","not","one","top","boat","girl","iron","like","lose","pass","rock","star","thin","tree","man","baby","card","film","hair","idea","movie","life","love","rock","time","work","box","dog","eye","fly","hat","key",
			"oil","pen","row","sun","tax","top","use","wine","yes","zoo","apple","black","card","dance","eagle","fish","house","king","milk","paper","queen","school","table","water","wine","YELLOW","banana","castle","dollar","euro","family","garden","history","island","jungle","monster","number","octopus","pencil","problem","robot","school",
			"teacher","window","zebra","alligator","bicycle","dinosaur","elephant","flower","gorilla","kangaroo","library","monkey","pencil","river","starfish","university","window"],
	"verb":	["run", "jump", "eat", "sleep", "talk", "listen", "think", "see", "hear", "smell", "feel", "taste","be", "have", "do","walk", "fly", "swim", "crawl", "climb", "drive", "ride", "fall", "rise","say", "tell", "ask", "shout", "whisper", "yell", "argue", "discuss","know", "understand", "believe", "think", "remember", "forget", "learn", "imagine","love", "hate", "like", "dislike", "fear", "anger", "surprise", "sadness", "happiness","seem", "appear", "become", "look", "smell", "sound", "taste","have", "own", "belong"],
	"adverb":	["quickly", "slowly", "carefully", "badly", "well","happily", "sadly", "angrily", "excitedly", "calmly","now", "then", "soon", "later", "early","yesterday", "today", "tomorrow", "always", "never","here", "there", "everywhere", "anywhere","nowhere","upstairs", "downstairs",
				"outside", "inside", "forward","very", "extremely", "quite", "rather", "too","enough", "almost", "nearly", "scarcely", "hardly","often", "sometimes", "usually", "rarely", "never","always", "frequently", "occasionally", "seldom", "generally"],
	"possibilities":	["might","could","may","can","could possibly","might potentially","seems likely to","is possible to","has a chance to"],
	"adjective":	["happy", "sad", "angry", "excited", "calm","beautiful", "ugly", "tall", "short", "big","small", "old", "new", "good", "bad","smart", "stupid", "funny", "serious", "kind"]
	}

	sentence_structures = [
		["pronoun", "verb", "noun"],
		["pronoun", "verb", "adjective", "noun"],
		["pronoun", "not asverb", "adjective"],
		["pronoun", "verb", "adverb"],
		["pronoun", "verb", "preposition", "noun"],
		["adjective", "noun", "verb"],
		["noun", "verb"],
		["pronoun", "not asverb", "noun"],
		["pronoun", "verb", "adverb", "preposition", "noun"],
		["pronoun", "possibilities", "verb", "noun"],
		["pronoun", "contration", "verb", "noun"],
		["pronoun", "verb", "conjunction", "pronoun", "verb"]
	]
	try:
		structure = random.choice(sentence_structures)
		sentence = []
		for part in structure:
			if part not in knowledge:
				raise ValueError("Missing part of speech: " + part)
			word = random.choice(knowledge[part])
			sentence.append(word)
		sentence[0] = sentence[0].capitalize()
		return " ".join(sentence)
	except (ValueError, IndexError) as e:
		return "Error: " + str(e)

#------------------------------------------------------------
def generate_random_question():
	grq = list(core["qa-astro"]) + list(questions) + list(others)
	index = random.randint(0, len(grq) - 1)
	return grq[index].capitalize()

#------------------------------------------------------------
def days_until(what_date):
	today = date.today()
	if what_date < today:
		what_date = what_date.replace(year=what_date.year + 1)
	days_until = (what_date - today).days
	output = str(days_until)
	return output

#-------------------------------------------------------
#-------------------------------------------------------
def find_word_in_dicts(word, core):

	pontuation = [".",",","!","?"]
	for p in range(len(pontuation)):
		word = word.replace(pontuation[p],"")
	for list_name, list_items in core.items():
		if word in list_items:
			if list_name == "greatings":
				seetime = datetime.now().strftime('%H:%M')
				salutation_first = random.choice(["","Greatings. ","Hey! ","Greatings! ","Hello ","Hi! ","Hello! ","Hi "])
				salutation_end = random.choice([""," to you to!"," to you to."," too!"," too."])
				seetime = datetime.now().strftime('%H:%M')
				hour = datetime.now().hour
				if 0 <= hour < 12:
					salutation_time = "Good morning"
				elif 12 <= hour < 18:
					salutation_time = "Good afternoon"
				else:
					salutation_time = random.choice(["Good evening","Good night"])
				daypart = salutation_time.split()[1]
				salutation_phrase = "Actualy is " + str(seetime) + " so it's considered " + salutation_time.split()[1] + " so i'll say:"
				if daypart.lower() in word.lower():
					if salutation_end != "":
						print (salutation_first + salutation_time + salutation_end + "\n")
					else:
						print (salutation_first + salutation_time + ".\n")
				else:
					print (salutation_phrase)
					print (salutation_first + salutation_time + salutation_end + "\n")

			elif list_name == 'seasons':
				allyearseasons = '' + ', '.join(core[list_name]) + ''
				seasonmonths = '' + ', '.join(core[word]) + ''
				print ("A period of the year that is distinguished by special climate condictions.")
				print ("%s is one of the four seasons (%s) of the year." % (word.capitalize(), allyearseasons.title()))
				print ("The %s period is composed by the months %s of the year." % (word.capitalize(), seasonmonths.title()))
				print ("%s have %s.\n" % (get_the_season()[0].capitalize(),weather_like_season()))

			elif list_name == 'spring' or list_name == 'summer' or list_name == 'autumn' or list_name == 'winter':
				month_number = core['months'].index(word)
				print ("%s is the %s month of the year and one month of the %s season." % (word.capitalize(), get_ordinal_position(month_number), list_name.capitalize()))
				print ("A year is composed by %s months and this one is made up of %s days.\n" % (len(core['months']), days_in_year()))

			elif list_name == 'word meaning':
				print (meaning_term[word])

			elif list_name == 'qa-astro':
				print (qa_astro[word])

			elif list_name == 'linuxcmd':
				print ("<"+word.lower()+">" + " is a console linux command. Here some help about'it:\n")
				print (" "*5+"Syntax: " + str(linux_commands[word]['syntax']))
				print ("Explanation: " + str(linux_commands[word]['explanation']))
				print (" "*3+"Examples: " + "'" + "', '".join(linux_commands[word]['examples']) + "'")
				print ("")

			elif list_name == 'coded':
				print ("Python is a programmer language wich i was builted (coded).")
				for i in range(len(art_py)):
					print (art_py[i])

			elif list_name == "primary moon phase":
				print ("That is a %s." % (list_name))
				print ("Astronomers have broken down this cycle into four Moon phases: \nNew Moon, First Quarter, Full Moon, and Last Quarter.\n")
			elif list_name == "secondary moon phase":
				print ("That is a %s.\n" % (list_name))
				print ("Astronomers have broken down this cycle into four Moon phases: \nWaxing Crescent, Waxing Gibbous, Waning Gibbous, and Waning Crescent.\n")

			elif list_name == 'orbital regime':
				regime = orbit_regime[word]
				regime_desc = " ".join(regime[0:28].split())
				print ("%s is the acronym of %s witch is a %s having the category of: \n%s.\n" %( word.upper(), regime_desc, list_name.capitalize(), regime[31:]))

			elif list_name == 'planet':
				order = get_ordinal_position(core['planet'].index(word)+1)
				if word == "earth":
					message = "%s is our %s, Our home.\nIs the %s planet from the Sun in our Solar System.\n" % (word.capitalize(), list_name, order)
				else:
					message = "%s is a %s. Is the %s planet from the Sun in our Solar System.\n" % (word.capitalize(), list_name, order)
				print ( message )
				print ( " " + word.capitalize() + " Overview:\n")
				print ( "  Orbital Period: " + str(planet_data[word]['orbital_period']) + " Earth years")
				print ( "  Semi-major Axis: " + str(planet_data[word]['semi_major_axis']) + " AU")
				print ( "  Orbital Eccentricity: " + str(planet_data[word]['orbital_eccentricity']) )
				print ( "  Orbital Inclination: " + str(planet_data[word]['orbital_inclination']) )
				print ( "  Rotation Period: " + str(planet_data[word]['rotation_period']) + " Earth days")
				print ( "  Axial Tilt: " + str(planet_data[word]['axial_tilt']) + " degrees")
				print ( "  Mass: " +  str(planet_data[word]['mass']))
				print ( "  Atmosphere: " + str(planet_data[word]['atmosphere']))
				print ( "  Moons: " + str(planet_data[word]['moons']))
				print ( "  Rings: " + str(planet_data[word]['rings']))
				print ( "  Temperature: " + str(planet_data[word]['temperature']))
				print ("")

			elif list_name == 'capital':
				index = core[list_name].index(word)
				print ("%s is a %s, and is from %s.\n" % (word.capitalize(), list_name, core['country'][index].capitalize()))
			elif list_name == 'country':
				index = core[list_name].index(word)
				print ("%s is a %s, and its capital is %s.\n" % (word.capitalize(), list_name, core['capital'][index].capitalize()))

			elif list_name == 'old_tech_term':
				oldtech_anwser = oldtech_terms[word]
				random.shuffle(messages['creative matter'])
				canswers = random.choice(messages['creative matter'])
				creative_random_anwser = canswers
				print(str(creative_random_anwser + "\n%s \n") % (word.capitalize(), list_name.capitalize(), oldtech_anwser))

			elif list_name == "climate dictionary term":
				climate_anwser = climate_dictionary[word]
				print("The term "+ word.capitalize() + " belongs to the " + list_name.title()[0:18] + ":\n" + climate_anwser + "\n")

			elif list_name == 'astronomy glossary':
				astro_anwser = astronomy_glossary[word]
				random.shuffle(messages['creative matter'])
				canswers = random.choice(messages['creative matter'])
				creative_random_anwser = canswers
				print( creative_random_anwser % (word.capitalize(), list_name.capitalize() ))
				print (astro_anwser + '\n')

			elif list_name == "asteroid":
				asteroid_info = asteroids_list[word]
				print ("\n %s - %s" % (list_name.capitalize(), word.capitalize()))
				print (" Type: " + asteroid_info['type'].capitalize())
				print (" Description: " + asteroid_info['description'].capitalize())
				print (" Dimentions: " + str(asteroid_info['dimensions']) + " Km ±\n")

			elif list_name == "constelattion":
				constellation_anwser = constellations_dict[word]
				random.shuffle(messages['creative matter'])
				creative_random_anwser = random.choice(messages['creative matter'])
				print( creative_random_anwser % (word.title(), list_name.capitalize()))
				print (word.capitalize() + ' have the designation of ' + constellation_anwser + '\n')

			elif list_name == "element symbol":
				periodic_show(word)

			elif list_name == "element abbr":
				periodic_show(word)

			elif list_name == "star name":
				star_info = stars_dict[word.title()]
				lower_case_abbr = {key.lower(): value for key, value in constellations_abbr.items()}
				star_constellation = lower_case_abbr.get(star_info[1].lower())
				random.shuffle(messages['creative matter'])
				creative_random_anwser = random.choice(messages['creative matter'])
				print( creative_random_anwser % (word.title(), list_name.capitalize()))
				print ("Belongs to " + star_constellation + " constellation and have the designation of " + star_info[0] + '.\n')

			elif list_name == "year event":
				random.shuffle(messages['year_event_msg'])
				print ( random.choice(messages['year_event_msg']) % (word.capitalize()))

			elif list_name == "askard_command":
				available_commands = ['list', 'view', 'show', 'achk', 'scan']
				remain_commands = [command for command in available_commands if command != word[0:4]]
				other_commands = '/'.join(remain_commands)
				print ("The command <%s> is one of the options <%s> available for interacting with the askard database." % (word[0:4], other_commands))
				if word[0:4] == available_commands[1] or word[0:4] == available_commands[2]:
					print ("This command beside the askard ID can be used with the 'first' and 'last' parameters.\n")
				elif word[0:4] == available_commands[3]:
					print ("This command beside the askard ID can be used with the 'first' , 'last' and 'update' parameters.\n")
				else:
					print ("")
			elif list_name == "help":
				print (help[word])

			else:
				print ("That is a %s.\n" % (list_name))
			return True

#--------------------------------------------
def convert_units( question ):
	operationf = 0
	unit_result = None
	c_element = question.split(" ")
	if len(c_element) != 4 or c_element[2] != 'from'.lower():
		print("convert <VALUE> from/days <UNIT> | seconds|minutes|hours|feets|miles|yards|AU|m3|gallons|fahrenheit\n")
	else:
		value = float(c_element[1])
		unit_name = c_element[3]
		if find_unit_factor(factors, c_element[3]) == None:
			print("The unit you insert is not available! Units available: feets|miles|yards|m3|gallons|fahrenheit\n")
		else:
			factor = float(find_unit_factor(factors, unit_name))
			operationf = value*factor
		if unit_name == 'feets' or unit_name == 'miles' or unit_name == 'yards' or unit_name == 'au':
			unit_result = 'Kilometer(s)'
		elif unit_name == 'm3' or unit_name == 'gallons':
			unit_result = 'Litter(s)'
		elif unit_name == 'celcius' or unit_name == 'fahrenheit':
			unit_result = 'celcius'
	return operationf, unit_result

#--------------------------------------------
def find_unit_factor(cfactors, unit):
	for unit_name, factor in factors:
		if unit_name == unit:
			return factor
	return None

#--------------------------------------------
def get_current_century():

	current_year = date.today().isocalendar()[0]
	century = current_year // 100 + 1 if current_year % 100 == 0 else current_year // 100
	ordinal = ("st", "nd", "rd")[min(century % 100 % 10 - 1, 2)] if century % 100 not in (11, 12, 13) else "th"
	return "We are in the %d%s century. \n" % (century + 1, ordinal)

#-------------------------------------------------
def quicklist(list, delimiter):
	if not delimiter:
		delimiter = "\u3009"
	for i in range(len(list)):
		#print (" 〉 "+ list[i])
		print (" " + delimiter + " " + list[i])

#-----------------------------------------------
def link_status(url):

	try:
		with urllib.request.urlopen(url) as response:
			response.read()
			return "online"
	except (urllib.error.URLError, TimeoutError) as e:
		return "Error"
	except Exception as e:
		return "not active"

#-----------------------------------------------
def people_in_space():

	try:
		import json
		import urllib.request
		url = 'http://api.open-notify.org/astros.json'
		response = urllib.request.urlopen(url)
		result = json.loads(response.read())

	except urllib.error.HTTPError as err:
		print('A HTTPError was thrown: {} {}'.format(err['code'], err['reason']))

	print('\nPeople in Space: {}\n'.format(result['number']))
	people = result['people']
	for p in people:
		print('{} in {}'.format(p['name'], p['craft']))
	print("")

#-------------------------------------------------
def where_is_iss():

	try:
		import json
		import urllib.request
		url = "http://api.open-notify.org/iss-now.json"
		response = urllib.request.urlopen(url)
		result = json.loads(response.read())
	except urllib.error.HTTPError as err:
		print('A HTTPError was thrown: {} {}'.format(err['code'], err['reason']))

	location = result["iss_position"]
	lat = location['latitude']
	lon = location['longitude']
	lat = float(lat)
	lon = float(lon)

	return " ISS overhead at %s, %s\n" % (str(lat), str(lon))

#--------------------------------------------------
def get_star_info(star_name):

	try:
		import urllib.parse
		import urllib.request
		url = "https://simbad.cds.unistra.fr/simbad/sim-id?output.format=ASCII&Ident=" + star_name
		with urllib.request.urlopen(url) as response:
			text_result = response.read().decode('utf-8')
		if text_result:
			datastar = []
			processed_data = text_result
		if len(text_result) > 1:
			data_lines = processed_data.splitlines()
			for i in range(len(data_lines)):
				datastar.append(data_lines[i])
		else:
			datastar.append('emptydata')

	except urllib.error.HTTPError as err:
		print('The cybele.Star module thrown the error : {} {}'.format(err['code'], err['reason']))
	return datastar

#------------------------------------------------
def add_days(n, d = datetime.today()):
  return d + timedelta(n)

#-------------------------------------------------
def days_to_units(num_days):
	minutes = num_days * 24 * 60
	hours = num_days * 24
	seconds = num_days * 24 * 60 * 60

	return minutes, hours, seconds

#-------------------------------------------------
def days_to_event(event):

	if not event:
		print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " What?!\n")
	else:
		if event == 'christmas':
			thisyear = date.today().year
			christmas = date(year=thisyear, month=12, day=25)
			days_left = days_until(christmas)
		elif event == 'newyear':
			thisyear = date.today().year
			yearseve = date(year=thisyear, month=12, day=31)
			days_left = days_until(yearseve)
		elif event == 'birthday' or event == 'mybirthday':
			nextyear = date.today().year + 1
			birthday = date(year=nextyear, month=5, day=4)
			days_left = days_until(birthday)
		else:
			days_left = 0
	return days_left

#-------------------------------------------------
def daysweeks_from_date(start_date):
	import datetime
	today = datetime.date.today()
	if start_date <= today:
		total_days = (today - start_date).days
		total_weeks = total_days // 7
	else:
		total_days = (start_date - today).days
		total_weeks = total_days // 7
	return total_weeks, total_days

#-------------------------------------------------
def calc_fulldate(given_date):
	import datetime
	year, month, day = given_date.year, given_date.month, given_date.day
	given_date_with_time = datetime.datetime(year, month, day)
	current_time = datetime.datetime.now()
	if given_date_with_time <= current_time:
		difference = current_time - given_date_with_time
	else:
		difference = given_date_with_time - current_time

	years = difference.days // 365
	months = (difference.days % 365) // 30
	days = (difference.days % 365) % 30
	hours = difference.seconds // 3600
	minutes = (difference.seconds % 3600) // 60
	seconds = (difference.seconds % 3600) % 60

	return years, months, days, hours, minutes, seconds

#-------------------------------------------------
def creative_random_anwser():
	athat = ["","That! "]
	starthat = random.choice(athat)
	random.shuffle(messages['things_done'])
	c_random_anwser = random.choice(messages['things_done'])
	return c_random_anwser

#-------------------------------------------------
def get_ordinal_position(number):
	if number == 0:
		number = 1
	if not 0 <= number <= 100:
		raise ValueError("Number must be between 1 and 100")
	last_digit = number % 10
	if 10 <= number <= 20:
		return "%sth" % number
	else:
		suffixes = ["st", "nd", "rd"] + (["th"] * 7)
	return str(number) + suffixes[last_digit - 1]

#-------------------------------------------------
def calculate_distance(body1, body2):

	AU_to_km = 149.6e6
	body_data = {
		"sun": {"radius": 0},  # Sun's radius is 0 as a reference point
		"mercury": {"radius": 0.39},
		"venus": {"radius": 0.72},
		"earth": {"radius": 1.0},
		"mars": {"radius": 1.52},
		"moon": {"radius": 0.00256, "parent": "earth"},
		"jupiter": {"radius": 5.2},
		"saturn": {"radius": 9.54},
		"uranus": {"radius": 19.18},
		"neptune": {"radius": 30.0}
	}
	body_pairs = {
		("earth", "moon"): {"min_distance": 0.00256 - 0.000017, "max_distance": 0.00256 + 0.000017},
		("moon", "earth"): {"min_distance": 0.00256 - 0.000017, "max_distance": 0.00256 + 0.000017}
	}
	valid_bodies = set(body_data.keys())
	if body1 not in valid_bodies or body2 not in valid_bodies:
		return None, None, None, None
	if body1 == body2:
		return 0, 0, 0, 0
	if (body1, body2) in body_pairs:
		min_distance_km = body_pairs[(body1, body2)]["min_distance"] * AU_to_km
		max_distance_km = body_pairs[(body1, body2)]["max_distance"] * AU_to_km
		min_distance_au = body_pairs[(body1, body2)]["min_distance"]
		max_distance_au = body_pairs[(body1, body2)]["max_distance"]
		return min_distance_km, max_distance_km, min_distance_au, max_distance_au
	radius1 = body_data[body1]["radius"]
	radius2 = body_data[body2]["radius"]
	min_distance_km = abs(radius1 - radius2) * AU_to_km
	max_distance_km = (radius1 + radius2) * AU_to_km
	min_distance_au = abs(radius1 - radius2)
	max_distance_au = radius1 + radius2
	return min_distance_km, max_distance_km, min_distance_au, max_distance_au

#-------------------------------------------------
def planet_orbit(planet_name):
	if planet_name in planet_radii:
		return planet_radii[planet_name]
	else:
		return None

#-------------------------------------------------
def planet_orbit_info(planet_name):

	planet_types = {
		"mercury": "Terrestrial",
		"venus": "Terrestrial",
		"earth": "Terrestrial",
		"mars": "Terrestrial",
		"jupiter": "Gas Giant",
		"saturn": "Gas Giant",
		"uranus": "Ice Giant",
		"neptune": "Ice Giant"
	}

	orbit_types = {
		"mercury": "Elliptical",
		"venus": "Nearly Circular",
		"earth": "Nearly Circular",
		"mars": "Elliptical",
		"jupiter": "Elliptical",
		"saturn": "Elliptical",
		"uranus": "Nearly Circular",
		"neptune": "Nearly Circular"
	}

	if planet_name in planet_types and orbit_types:
		return planet_types[planet_name], orbit_types[planet_name]
	else:
		return False

#-------------------------------------------------
def get_the_season():
	today = datetime.today()
	month = today.month
	seasons = list(core['seasons'])
	current_season_index = (month - 3) // 3 if month >= 3 else month + 9 // 3
	current_season = seasons[current_season_index]
	next_season_index = (current_season_index + 1) % 4
	other_seasons = seasons[next_season_index:] + seasons[:next_season_index - 1]
	return current_season, other_seasons

#--------------------------------------------------
def weather_like_season():
	month_name = datetime.today().strftime('%B').lower()
	season = [s for s, months in core.items() if month_name in months]
	weather_type = random.choice(weather_season_condiction[season[0]])
	return weather_type

#---------------------------------------------------------------------------------------------
def cybele_play_quiz(quizdata,game):

	gamescore[0] = 0
	gamescore[2] = 0
	getout = ['stop','x','q',':x',':q']
	extquiz = ['Country','Capital','Constellation','Designation','Periodic Table Elements','Symbol']
	if game == 1:
		whatquiz = 0
		gamescore[1] = 1
	elif game == 2:
		whatquiz = 2
		gamescore[1] = 2
	elif game == 3:
		whatquiz = 4
		gamescore[1] = 3
	else:
		print (random.choice(messages['trouble_msg']) + " Ups! It's internal...\n")
		return True

	print ("\nType [q] or [x] if you want to quit or exit.")
	print ("I'll give you a " + extquiz[whatquiz] + " and you give me its " + extquiz[whatquiz+1] + "\n")

	while True:
		selected = random.choice(list(quizdata.keys()))
		correct = quizdata[selected]
		user_input = input ( extquiz[whatquiz] + " " + selected.title() + " ? 〉 ")
		if any(word in user_input.lower() for word in getout):
			break
		elif user_input.lower() == correct.lower():
			gamescore[2] = gamescore[2] + 1
			print ("Correct. Let's proceed.\n")
		else:
			print ("Incorrect, " + correct.title() + ". Let's proceed.\n")
	print ("")

#---------------------------------------------
def random_delay():
	minutes = random.randint(0, 59)
	seconds = minutes * 60
	sleep(seconds)

#-------------------------------------------------------------------
def random_season_activity():
	now = date.today()
	month = now.month
	if 3 <= month <= 5:  # Spring (March, April, May)
		season = "spring"
	elif 6 <= month <= 8:  # Summer (June, July, August)
		season = "summer"
	elif 9 <= month <= 11:  # Autumn (September, October, November)
		season = "autumn"
	else:  # Winter (December, January, February)
		season = "winter"
	for season_data in season_activities:
		if season_data[0] == season:
			activities = season_data[1]
			activitie = "It's " + season.capitalize() + ", " + random.choice(activities) + ".\n"
			return activitie
	return None

#-------------------------------------------------
def periodic_show( element ):

	if any(elements in element for elements in core['element symbol']):
		element_sy = periodic_elements[element.capitalize()]
		number_sy = list(periodic_elements.keys()).index(element.capitalize())
		print ("%s is a element who is symbol is represented by [ %s ] (abbr.) and her Atomic number [%s]." % (element.capitalize(), element_sy, number_sy + 1))
		print ('The Periodic Table is ordered by increasing atomic number, witch is the number of protons and electons from the element.\n')
	elif any(elements in element for elements in core['element abbr']):
		element_sy = periodic_abbr[element.capitalize()]
		number_sy = list(periodic_abbr.keys()).index(element.capitalize())
		print ("%s is the (abbr) of the symbol what is the element [ %s ] and her Atomic number is [%s].\n" % (element.capitalize(), element_sy, number_sy + 1))
	else:
		print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Weird! My search of the element was 'Neutrine'. !\n")

#-------------------------------------------------
def generate_problem(difficulty):

	if difficulty == 'e':
		num1 = random.randint(1, 10)
		num2 = random.randint(1, 5)
	elif difficulty == 'm':
		num1 = random.randint(1, 20)
		num2 = random.randint(1, 10)
	elif difficulty == 'h':
		num1 = random.randint(10, 50)
		num2 = random.randint(5, 20)
	else:
		return False, None

	operator = random.choice(['+', '-', '*'])
	problem = str(num1) + " " + operator + " " + str(num2)
	answer = eval(problem)
	return problem, answer

#-------------------------------------------------
def cybele_math_game():
	score = 0
	num_questions = 10
	print("Welcome to Round 10 Math Quiz!")
	difficulty = input("[e]asy, [m]edium, [h]ard: ").lower()
	if difficulty == 'e' or difficulty == 'm' or difficulty == 'h':
		gamescore[0] = 0
		gamescore[1] = 4
		for _ in range(num_questions):
			problem, answer = generate_problem(difficulty)
			if problem is None:
				continue
			elif problem == False:
				break
			try:
				user_answer = int(input(("{} = ".format(problem))))
				if user_answer == answer:
					print("Correct! Proceeding.")
					score += 1
					gamescore[2] = score
				else:
					print("Incorrect, " + str(answer) + ". Let's proceed.")
			except ValueError:
				break
	else:
		math_msg = ["What! e, m or h brain's on fire? Use ice, cream or sleep!","If it's allready hard use e,m or h, Math Quiz!?, gonna be Einscharged!."]
		print( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + random.choice(math_msg))
	print ("")

#----------------------------------------------------------------
def check_askard(ask_id,funct):
	mem_id = ask_id
	query = int(ask_id)
	keys = list(askards_db.keys())
	keys.sort()
	lower_key = None
	for ask_id in keys:
		if int(ask_id) > query:
			lower_key = keys[keys.index(ask_id) - 1]
			break
	higher_key = None
	for ask_id in reversed(keys):
		if int(ask_id) < query:
			higher_key = ask_id
			break
	if lower_key and higher_key != None and funct == True:
		print("It's impossible view the #" + mem_id + " because dont exist in my database. The nearest are #"+lower_key+" and the #"+higher_key+"...\n")
	elif lower_key and higher_key != None and funct == False:
		print("The askard #" + mem_id + " do not exist in my database. The closest i found were the #"+lower_key+" and the #"+higher_key+"... \n")
	else:
		print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + "It seems to be a problem with my code. Well done " + _auth1r_ +"!\n")

#----------------------------------------------------------------
def manage_db(question):
	naskey = list(askards_db.keys())
	sub = question.split()
	if len(sub) > 5 or len(sub) < 3:
		print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " It seems to be a problem with the database parameters. Too many!\n")
	elif len(sub) == 4 and sub[3] != 'to':
		print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Parameters hmmm!. ' to ' is missing or is missplaced making a wrong usage syntax.!\n")
	else:
		if sub[0] == 'list':
			if len(sub) == 4:
				begin = question.split()[2]
				last = question.split()[3]
			elif len(sub) == 5 and question.split()[3] == 'to':
				begin = question.split()[2]
				last = question.split()[4]
				filtered_values = [value for value in askards_db.keys() if value >= begin and value <= last]
				if len(filtered_values) > 0:
					for valuekey in filtered_values:
						print(" #%s \n > %s\n" % (valuekey, managedb(askards_db[valuekey],shift)))
				else:
					print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " I did not find any values for your requested in my database!\n")
			else:
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " It seems to be a problem with the range parameter. 'to' is missing!\n")

		elif sub[0] == 'scan':
			scan_word = question.split()[2]
			if len(sub) == 3:
				searchdb = scan_askards(scan_word)
				if len(searchdb) != 0:
					print ('There are ' + str(len(searchdb)) + ' askards that contain the substring '+_spchar_[2:3] + scan_word + _spchar_[3:4] + '. They are the :\n')
					if len(searchdb) < 50:
						xask = 5
					else:
						xask = 10
					for sc in range(0, len(searchdb), xask ):
							line = searchdb[sc:sc+xask]
							search_result = " ".join(map(str,line))
							print(search_result)
					scandb = str(searchdb).replace("'","").replace("[","").replace("]","")
					copy2clipboard(scandb)
					print("")
				else:
					print (random.choice(messages['trouble_msg']) + " I did not have any result in the search from "+_spchar_[2:3] + scan_word + _spchar_[3:4]+ " in my internal askard database.\n")
			else:
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " It seems to be a problem with what i should search.\n")

		elif sub[0] == 'show' or sub[0] == 'view':
			key = question.split()[2]
			if len(question.split())!=3:
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " To many parameters! Consider use: help askard.\n")
			elif key in askards_db:
				copy2clipboard(managedb(askards_db[key],shift))
				print("\n > %s\n" % (managedb(askards_db[key],shift)))
			elif question.split()[2] == 'first':
				first_key = next(iter(askards_db))
				print("\n #%s \n > %s\n" % (first_key, managedb(askards_db[first_key],shift)))
			elif question.split()[2] == 'last':
				last_key = list(askards_db.keys())[-1]
				print("\n #%s \n > %s\n" % (last_key, managedb(askards_db[last_key],shift)))
			elif question.split()[2] != 'first' or question.split()[2] != 'last' or any(word in qvalue.split()[2] for question.split()[2] in naskey):
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " I dont recognized '" + key + "' like a view or show askard command!\n")
			else:
				check_askard(key,True)

		elif sub[0] == 'achk':
			key = question.split()[2]
			if len(question.split())!=3:
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " To many parameters! Consider use: help askard.\n")
			elif key in askards_db:
				print("The askard #" + key + " you requested to verify exist in my database.\n")
			elif question.split()[2] == 'first':
				first_key = next(iter(askards_db))
				print("The first askard is the #" + first_key + " that i have in my database.\n")
			elif question.split()[2] == 'last':
				last_key = list(askards_db.keys())[-1]
				print("The last askard i have recorded in my database is the #" + last_key + ".\n")
			elif question.split()[2] == 'update':
				from_askards_update = date.today() - date(year=int(askards_db_last_update[6:]), month=int(askards_db_last_update[3:5]), day=int(askards_db_last_update[0:2]))
				print("The last time i have recorded the database was updated " + str(from_askards_update).replace(", 0:00:00","") + " ago. Was in "+ askards_db_last_update + ".\n")
			elif question.split()[2] != 'first' or question.split()[2] != 'last' or question.split()[2] != 'update' or any(word in question.split()[2] for question.split()[2] in naskey):
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " I dont recognized '" + key + "' like a achk askard command! It's a new think?!\n")
			else:
				check_askard(key,False)
	del naskey

#-------------------------------------------------
#-------------------------------------------------
def managedb(askardtxt, shift):
    askard_msg = ""
    for char in askardtxt:
        if char.isalpha():
            if char.isupper():
                askard_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                askard_char = chr((ord(char) - shift - 97) % 26 + 97)
            askard_msg += askard_char
        else:
            askard_msg += char
    return askard_msg

#-------------------------------------------------
def yoda_speak(sentence):

	sentence_end = ["Hmm, yes.", "Hmm.", "Yes.", "I see."]
	if isinstance(sentence, str):
		words = sentence.lower().split()
	elif isinstance(sentence, list):
		words = [word.lower() for word in sentence]

	verb = None
	subject = None
	complement = []
	verbs = ["am", "is", "are", "was", "were", "will", "would", "should", "can", "could", "may", "might", "must"]
	for i, word in enumerate(words):
		if word in verbs:
			verb = word
		elif subject is None:
			if word == "the" and i + 1 < len(words):
				subject = words[i + 1]
				for j in range(i + 2, len(words)):
					complement.append(words[j])
				break
			else:
				subject = word
		else:
			complement.append(word)

	yoda_words = []
	if complement:
		yoda_words.extend(complement)
	if verb:
		yoda_words.append(verb)
	if subject:
		yoda_words.append(subject)
	if complement and verb and subject:
		yoda_words = complement + [verb, subject]
	new_sentence = " ".join(yoda_words).capitalize() + ", " + random.choice(sentence_end)
	return new_sentence

#----------------------------------------------------------------
#----------------------------------------------------------------
def findme(input_string, item_list):
	input_words = input_string
	matches = []
	for item in item_list:
		item_words = item.lower().split()
		for word in input_words:
			if word in item_words:
				matches.append(item)
				break
	return matches #if matches else True

#-------------------------------------------------
def decompact(data, flength=2):
    value_data = ""
    for i in range(0, len(data), flength):
        hx = data[i:i+flength]
        value_data += chr(int(hx, 16))
    return value_data

#-------------------------------------------------
def integrity():
	chkcode = int(integrty, 16)
	chkctrl = sum(ctrl for ctrl in chkdict)
	return chkctrl, chkcode

#-------------------------------------------------
#-------------------------------------------------
def main():
	global aboutyou
	ctrlchk=integrity();chkcybele=managedb
	wms = random.choice(core['intromsg']);ta=True
	aboutyou = chkcybele(aboutyou, checksum)
	#----------------------------
	if chkauth!=cybchk or ctrlchk[0]!=ctrlchk[1]:
		print(kolor['DARK_RED'] + "\n " +_spchar_[1:2] + chr(32) + _title_ + kolor['OFF'] + ": " + hex(ctrlchk[0]) + " - " + chkcybele(chkcyb, checksum))
		print ("")
		exit()
	#----------------------------
	drawart('art_cybele')
	#----------------------------
	if _cybid_ == True or node_name:
		print("\n"+kolor[('DARK_YELLOW')]+wms+"\n\n"+kolor['BLUE']+"I am "+kolor['DARK_RED']+_title_+kolor['RED']+_spchar_[0:1]+kolor['BLUE']+" a "+website['home'][8:] + _cyext_ +kolor['OFF']+"\n")
	else:
		print("\n"+kolor['DARK_BLACK']+wms+"\n\n"+kolor['DARK_BLUE']+"I am "+kolor['DARK_RED']+_title_+kolor['RED']+_spchar_[0:1]+kolor['DARK_BLUE']+" a "+website['home'][8:]+ _cyext_ +kolor['OFF']+"\n")

	days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	#-----------------------------
	while True:
		#-------------------------
		question = get_question()
		#-------------------------
		if not question:
			print ("I'm ready when you are! ask me something like:")
			print (" " + _spchar_[1:2] + " " + "What can you anwser")
			for i in range(random.randint(1,4)):
				print (" " + _spchar_[1:2] + " " + generate_random_question())
			print ("")
		#-------------------------
		elif question == 'bye':
			return False

		elif _cybid_ == True and any(word in question for word in core['out']) and not "help" in question:
			return False

		elif any(word in question for word in core['negative_word']) and question[0:13] != 'sharing about':
			print ("I understand. Is there anything else You want to ask'me ?\n")

		elif any(word in question for word in core['badword']):
			print (random.choice(messages['badword_msg']) + "\n")

		elif _cybid_ == True and any(word in question for word in addcomm):
			cybext.EXTmod(question)

		elif question == 'extdir' or question == 'ext' and _cybid_ == True:
			print ("List of the available commands by" + _cyext_ + "\n")
			quicklist(addcomm,"")
			print ("")

		elif question[0:26] == 'do you know anything about' or question[0:16] == 'know anything on' or question[0:4] == 'find' or question[0:4] == 'seek':
			if question[0:4] == 'seek' or question[0:4] == 'find':
				words = question.split()[1:]
			elif question[0:16] == 'know anything on':
				words = question.split()[3:]
			else:
				words = question.split()[5:]
			if len(words) == 0:
				xvar = random.choice(messages['trouble_msg'])
				yvar = random.choice(["What! Whatever it was...","Whatever it was... What?"])
				wvar = random.choice(["Runned away...","Escaped...","Took of...","Made a break for it...","Made a hasty retreat...","Hightailed it...","Beat a hasty retreat..."])
				seekfind_message = [ yvar + " " + wvar + " " + xvar + "\n" , xvar + " " + yvar + " " + wvar + "\n"]
				print (random.choice(seekfind_message))
			else:
				cybele_find = findme(words, topics)
				if cybele_find:
					print ("Yes. There are in my offline topic's.\n")
				else:
					print ("Unfornunately and dont have any offline information or Topic about'it. \n")

		elif find_word_in_dicts(question, core) == True:
			if question == 'cybele idea' or 'cybele idea' in question:
			   print("The word idea was me until "+ _auth1r_ +" started to develop me.\nAhah and just for fun!\n")

		elif question == 'what can i ask you' or question == 'what can you anwser' or question == 'what do you know' or question == 'what can you do' or question == 'what do you do' or question =='what you can do':
			print ("\n" + random.choice(core['cthemes']) + ": \n")
			random.shuffle(topics)
			last_topic = len(topics)-1
			for i in range(last_topic):
				print ( "   - " + topics[i].title())
			print ("  and: ")
			print ("   " + topics[last_topic].title() + ", " + random.choice(messages['endterm']).lower() + ".\n")

		elif question == 'adelino quote':
			print ("Here's a quote by my author " + _auth1r_ + ".")
			print (" " + _spchar_[1:2] + " " + random.choice(as_quotes))
			print ("")

		elif question == "what is" or question == "do you know what is" or question == "meaning of":
			what_creative= ["","I think you were trying to know something, righ ?!\n","Are you trying to ask or know something ?!\n","You were going to ask for knowledge weren't you? ?!\n","Well, to know or question you need a matter !\n"]
			cquestion = random.choice(what_creative)
			print ( "What?! " + cquestion + "In my case just type without the usual formalities... if i have the knowledge i will anwser.\n")

		elif question[0:7] == 'show me' or question[0:7] == 'tell me' or question[0:7] == 'list me':
			if question.find('astronomy')!=-1 or question.find('astronomy glossary')!=-1:
				all_keys = core["astronomy glossary"]
				random.shuffle(all_keys)
				astronomy_random_keys = all_keys[:5]
				astro_terms = ""
				for term in astronomy_random_keys:
					astro_terms += term + ", "
				print ("This are some of the terms i have in knowledge : " + astro_terms[:-2] + ".\n")
			
			elif question.find('stars')!=-1 or question.find('star names')!=-1:
				all_stars = core["star name"]
				random.shuffle(all_stars)
				stars_random_keys = all_stars[:5]
				stars_names = ""
				for term in stars_random_keys:
					stars_names += term + ", "
				print ("This are some Stars names i have in offline knowledge : " + stars_names.title()[:-2] + ".\n")

			elif question.find('asteroids')!=-1:
				all_asteroids = core["asteroid"]
				random.shuffle(all_asteroids)
				asteroids_random = all_asteroids[:5]
				asteroid_names = ", ".join(asteroids_random)
				print ("Here are some asteroids i have in knowledge : " + asteroid_names + ".\n")

			elif question.find('dangerous')!=-1:
				dangerous_asteroids = [asteroid for asteroid, data in asteroids_list.items() if data["type"] == "dangerous asteroid"]
				dangerous = ", ".join(dangerous_asteroids)
				print ("Here are some dangerous asteroids i have in knowledge : " + dangerous.title() + ".\n")

			elif question.find('old')!=-1 and question.find('tech')!=-1:
				all_oldtech = core["old_tech_term"]
				random.shuffle(all_oldtech)
				oldtechs_random = all_oldtech[:3]
				oldtech_names = ", ".join(oldtechs_random)
				print ("Here are some old_tech_terms i have in knowledge : " + oldtech_names + ".\n")

			elif question.find('constellations')!=-1:
				constelattionx = list(core['constelattion'])
				random.shuffle(constelattionx)
				constelattion_random = constelattionx[:5]
				viewconstellations = ", ".join(constelattion_random[:-1]) + ' and ' + constelattion_random[4] + ' constellations.'
				print ("I can show you based in my knowledge " + viewconstellations.title() + ".\n")

			elif question.find('climate')!=-1 or question.find('dictionary')!=-1:
				climatedict = list(core['climate dictionary term'])
				random.shuffle(climatedict)
				climatedict_random = climatedict[:3]
				viewclimatedict = ", ".join(climatedict_random[:-1]) + ' and ' + climatedict_random[2]
				print ("I can show you based on my Climate Dictionary knowledge terms like " + viewclimatedict.title() + ".\n")

			elif question.find('meaning term')!=-1 or question.find('meaning words')!=-1 or question.find('meaning terms')!=-1:
				all_meanings = core["word meaning"]
				random.shuffle(all_meanings)
				meaning_random_keys = all_meanings[:3]
				meaning_words = ""
				for term in meaning_random_keys:
					meaning_words += term + ", "
				print ("This are some Meaning Terms/Words i have in my offline knowledge : " + meaning_words.title()[:-2] + ".\n")

			elif question.find('constellations')!=1 and question.find("all")!=-1:
				print ("\nHere are all Constellations i have in knowledge ("+str(len(constellations_dict))+") and the meaning of her name or her designation:\n")
				for constelattion in constellations_dict:
					print(" %s: %s" % (constelattion.title(), constellations_dict[constelattion]))
				print ("")

			elif question.find('linux')!=-1 or question.find('linux commands')!=-1:
				all_commands = core["linuxcmd"]
				random.shuffle(all_commands)
				commands_random_keys = all_commands[:5]
				commands_names = ""
				for term in commands_random_keys:
					commands_names += term + ", "
				print ("This are some Linux commands i have in offline knowledge : " + commands_names[:-2] + ".\n")

		elif question == 'astronomy questions' or question == 'questions of astronomy':
				all_astro = core["qa-astro"]
				random.shuffle(all_astro)
				astro_random_keys = all_astro[:3]
				astro_qa = ""
				for term in astro_random_keys:
					astro_qa += " "+_spchar_[1:2] + term + "?\n"
				print ("There are some astronomy questions you can make'me:\n\n" + astro_qa.title()[:-2] + "?\n")

		elif question[-28:] == 'dangerous asteroids detailed':
			print ('\nTop 10 Potentially Hazardous Asteroids (PHAs)')
			print ('This list is based on current knowledge and could change as new information becomes available. \nThe risk posed by any asteroid is constantly evaluated by scientists.')
			print ('Determining the exact order of risk for these asteroids is complex and involves numerous factors. \nThis list is presented in no particular order.\n')
			dangerous_asteroids = []
			for asteroid, data in asteroids_list.items():
				if data["type"] == "dangerous asteroid":
					dangerous_asteroids.append({"name": asteroid,"description": data["description"]})
			for asteroid in dangerous_asteroids:
				print(" [ %s ]: %s\n" % (asteroid['name'], asteroid['description']))

		elif question[0:8] == 'how many' and question.find('glossary')!=-1 or question.find('astronomy terms')!=-1 or question.find('anwser')!=-1:
			print ("I can tell you the meaning of " + str(len(astronomy_glossary)) + " Astronomy glossary terms." + "\n")
		elif question[0:8] == 'how many' and question.find('asteroids')!=-1 and question.find('you know')!=-1 or question.find('anwser')!=-1:
			print ("I can tell you about " + str(len(core['asteroid'])) + " Asteroids, but there are millions and those we dont know.. yet." + "\n")
		elif question[0:8] == 'how many' and question.find('star')!=-1 and question.find('names')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my offline knowledge " + str(len(core['star name'])) + " Stars. " + random.choice(messages['endterm']) + "\n")
		elif question[0:8] == 'how many' and question.find('capitals')!=-1 and question.find('you know')!=-1 or question.find('anwser')!=-1:
			print ("Actualy based on my offline knowledge " + str(len(core['capital']) + 5) + " capitals and " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")
		elif question[0:8] == 'how many' and question.find('countries')!=-1 and question.find('you know')!=-1 or question.find('anwser')!=-1:
			print ("Actualy based on my offline knowledge " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")
		elif question[0:8] == 'how many' and question.find('linux commands')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my offline knowledge " + str(len(core['linuxcmd'])) + " Linux commands. " + random.choice(messages['endterm']) + "...\n")

		elif question[0:8] == 'what' and question.find('capitals')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my offline knowledge i know " + str(len(core['capital']) + 5) + " capitals and " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")
		elif question[0:8] == 'what' and question.find('countries')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my offline knowledge i know " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")

		elif question[0:9] == "days till" or question[0:8] == "days for" or question[0:7] == "days to":
			subevent = " ".join(question.split()[2:])
			eventdays = days_to_event(subevent.replace(" ",""))
			if eventdays != 0:
				if subevent == "birthday" or subevent == "my birthday":
					select_creator = random.choice(["my creator", _auth1r_, "my creator "+_auth1r_])
					print ('To yours i dont know, doing my privacy limitations but to the ' + select_creator + ' are '+ eventdays +' days.\n')
				elif eventdays != 0:
					print ("%s left for %s\n" % (eventdays, subevent.title()))
			else:
				short_no = ["No can do.","I can't, sorry.","Impossible!","Way ahead for me!","Ohh! No way.","Are you trying damage my RAM!","Not enought Memory!"]
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Till What!? '"+ subevent + "' "+ random.choice(short_no) + "\n")

		elif question[0:15] == 'difference from' or question[0:8] == 'age calc':
			try:
				if len(question.split()) > 2:
					inputDate = str(question.split()[2:][0])
					day,month,year = inputDate.split('.')
					inidata = date(int(year),int(month),int(day))
					dfweeks, dfdays = daysweeks_from_date(inidata)
					years, months, days, hours, minutes, seconds = calc_fulldate(inidata)
					print("The difference between {} and {} is: {} years, {} months, {} days, {} hours, {} minutes, {} seconds.".format(inidata.strftime("%d.%m.%y"), date.today().strftime("%d.%m.%y"), years, months, days, hours, minutes, seconds))
					print("The Equivalent of {:,} months {:,} weeks {:,} days {:,} hours {:,} minutes. \n".format(years*12+months-1, dfweeks, dfdays, dfdays*24+hours, ((dfdays*24)*60+minutes)))
				else:
					raise ValueError
			except ValueError :
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " There is a problem in the syntax. Enter the date in 'dd.mm.yyyy' format. \n")

		elif question[0:22] == 'what do you know about' and question.find('astronomy')!=-1:
			print ("I can tell you the solar system, information about planets, distances and the meaning of " + str(len(astronomy_glossary)) + " Astronomy terms." + "\n")

		elif question[0:22] == 'what do you know about' and question.find('asteroids')!=-1 or question.find('celestial bodys')!=-1:
			print ("I can tell you about " + str(len(core['asteroid'])) + " asteroids. Only the most basic information.")
			print ("I think is gonna be a "+ _title_ +" version with a connection to the JPL SSD or datastro.eu"  + "\n")

		elif question[0:22] == 'what do you know about' and question.find('constelations')!=-1 or question.endswith('?'):
			print ("I can tell you about " + str(len(constellations_dict)) + " constelations.\n ")

		elif question[0:22] == 'what do you know about' and question.find('the')!=-1 and question.find('universe')!=-1 or question.endswith('?'):
			print ("The solar system, information about planets, distances and the meaning of " + str(len(astronomy_glossary)) + " Astronomy terms, " + str(len(core['asteroid'])) + " asteroids (most basic information) and " + str(len(constellations_dict)) + " constelations.\n")

		elif question == 'can you' and question.find("sentence")!=-1 or question.find("phrase")!=-1:
			if question[0:4] == 'make':
				print ("This is a sentence! And I'm even not using NLP.\n")
			else:
				print ("Yes, I can! See? This is a sentence! And I'm even not using NLP.\n")

		# days_until() gives' incorrect days in vorian online time. Verify. for next version
		elif question.find('vorian created')!=-1 or question.find('vorian was created')!=-1 or question.find('vorian went online')!=-1:
			print("The website [Vorian] was created in {} doing it online for {} days until today.\n".format(str(date(2010,12,9).strftime("%d.%m.%Y")), (date.today() - date(2010,12,9)).days))

		elif any(word in question for word in core['question_words']) and any(word in question for word in core['planet']) and not "version" in question:
			print (random.choice(list(messages['magic_anwser'])) % "planet")
		elif any(word in question for word in core['question_words']) and any(word in question for word in list(oldtech_terms.keys())) and not "version" in question:
			print (random.choice(list(messages['magic_anwser'])) % "old term and word" )
		elif any(word in question for word in core['question_words']) and any(word in question for word in core['constelattion']) and not "version" in question:
			print (random.choice(list(messages['magic_anwser'])) % "constellations")
		elif any(word in question for word in core['question_words']) and any(word in question for word in core['astronomy glossary']) and not "version" in question:
			print (random.choice(list(messages['magic_anwser'])) % "astronomy term")

		elif question[-14:] == 'periodic table':
			tablesentence = [["I think you ment ","Don't you ment "],"< visualize | show > periodic table ?!\n"]
			subwords = "".join(question.split()[1:])
			words = question.split()[0]
			if len(question.split()) > 3 or len(question.split()) == 2:
				print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Something 'elementary' is 'Neutrine' right now!" )
				if "visualize" in words or "show" in words or subwords!= 'periodictable':
					pik = random.choice([0,1])
					print (tablesentence[0][pik] + tablesentence[1])
			else:
				if words == 'visualize' or words == 'show':
					print("")
					quicklist(periodic_table_pt," ")
					print("")
				else:
					periodic_show ( words )

		elif question[0:13] == 'distance from':
			qplanet = []
			valid_planets = core['planet'] + ['sun'] + ['moon']
			qerror = ["Please specify two celestial bodies","Enter the names of two celestial bodies","You must provide two celestial bodies to calculate the distance","To determine the distance, please input the names of two celestial objects","Specify two celestial bodies","Input the names of two celestial bodies"]
			qeg_error = ["using 'and' or 'to' (e.g., 'Earth and Mars').","separated by 'and' or 'to'."]

			for word in question.split():
				if word in valid_planets:
					qplanet.append(word.lower())

			if len(question.split()) == 2:
				print (random.choice(qerror) + " " + random.choice(qeg_error) + '\n')
			elif len(question.split()) != 5 or question.split()[3] != 'to' and question.split()[3] != 'and':
				print (random.choice(messages['not_right']) + ' ' + random.choice(qeg_error) + '\n')
			elif len(qplanet) == 2:
				distance_data = calculate_distance( qplanet[0], qplanet[1])
				min_km, max_km, min_au, max_au = distance_data
				response_list = []
				response_list.append("The distance between these celestial bodies varies due to their elliptical orbits.")
				response_list.append("At their closest point, they are approximately {:,.2f} kilometers ({:.3f} AU) apart.".format(min_km, min_au))
				response_list.append("At their farthest point, they are about {:,.2f} kilometers ({:.3f} AU) apart.".format(max_km, max_au))
				print ( "\n".join(response_list) + '\n')

		elif question[-5:] =='orbit':
			valid_planets = core['planet'] + ['moon']
			sub = question.split()
			if sub[1] == 'orbit' and len(question.split()) == 2:
				planet_name = sub[0]
			else:
				print (random.choice(notplanet) + " " + '\n')
			if planet_name in valid_planets:
				order = get_ordinal_position(valid_planets.index(planet_name))
				orbit_anwser = ( planet_name.capitalize() + ' behing the ' + order + ' planet from our Solar System have a ' + ' orbit, '.join(planet_orbit_info(planet_name)) + '.\n')
				print(orbit_anwser)
			else:
				random.shuffle(messages['notplanet'])
				print ( random.choice(messages['notplanet']) % (planet_name))

		elif question == 'planets of the solar system' or question == 'planets of solar system' or question == "solar system planets order" or question == "solar system planets":
			planets = core['planet']
			solar_system = ', '.join(planets)
			sanwser = solar_system. title() + ", in a tolal of " + str(convert_to_words(len(core['planet']))) + " planets.\n"
			sanwser_before = "From the Sun are "
			if "order" in question:
				print (sanwser_before + sanwser)
			else:
				print ("The planets are " + sanwser)

		elif question == 'types of orbits' or question == 'orbital regimes':
			print ("The orbital regimes or types of orbit's i have in my offline knowledge are:\n")
			for regime, orbital in orbit_regime.items():
				print(" > ", regime.upper(), ": ", orbital[0:28])
			print ("")

		elif question.find('seasons')!=-1 and question.find('year')!=-1:
			get_season = get_the_season()
			if question[0:8] == 'how many':
				print("There are %s seasons in the year. The actual what is %s and the others that are %s\n" % ( len(get_season[1]+1), get_season[0].capitalize(), ', '.join(get_season[1]).title()))
			else:
				print("The seasons that make up the year are %s the actual and all the others by her order %s.\n" % (get_season[0].capitalize(), ', '.join(get_season[1]).title()))

		elif question == 'set default gps':
			latgps = _poigps_[0]
			longps = _poigps_[1]
			_poigps_.insert ( 4, 1 )
			print(' > default GPS coordinates restored.\n')
		elif question == 'set default gps off':
			_poigps_.insert ( 4, 0 )
			print(' > default GPS coordinates defined to user input.\n')
		elif question == 'show default gps':
			if _poigps_[4] == 1:
				print (" > stored default information is empty!\n")
			else:
				print ("\n #default stored GPS coordinates")
				print ("  Latitude : " + str(_poigps_[0]))
				print (" Longitude : " + str(_poigps_[1]))
				print ('Defaults gps coordinates loaded from code.\n')

		elif question[-7:] == 'capital':
			word = question.split()[0].lower()
			if word in core['country']:
				index = core['country'].index(word)
				print ("%s has as capital %s.\n" % (word.capitalize(), core['capital'][index].capitalize()))
			elif word in core['capital']:
				index = core['capital'].index(word)
				print ("%s is the capital of %s.\n" % (word.capitalize(), core['country'][index].capitalize()))
			else:
				print ( random.choice(messages['not_right']) + " " + word.capitalize() + " is neither a capital or a country!\n")

		elif question[0:10] == 'capital of':
			word = question.split()[2].lower()
			if word in core['country']:
				index = core['country'].index(word)
				print ("The capital of %s is %s.\n" % (word.capitalize(), core['capital'][index].capitalize()))
			else:
				print ( random.choice(messages['not_right']) + " " + word.capitalize() + " is not a country!\n")

		elif question in iknow_pun:
			print(question.capitalize() + " " + iknow_pun[question] + " " + question + ".\n")

		elif question == 'value of pi' or question == 'pi value' or question == 'pi':
			print ("The value of π is "+ str(math.pi)+ "\n")

		elif question == 'clear screen' or question == 'cls':
			if sysos == 'Windows':
				os.system('cls')
			elif sysos == 'Linux':
				os.system('clear')
			else:
				print ("Sorry i cannot execute that command in a unidentified S.O!\n")

		elif question == 's.o' or question == 'operating system':
			if sysos == 'Linux':
				#nuptime = os.system('uptime')
				print ("This is the " + sysos + " Operating System (OS). ")
			elif sysos == 'Windows':
				print ("I am behing executed in " + sysos + "Operating System (OS).")
			else:
				print ("Sorry i cannot identify this Operating System. Maybe in my next update!\n")

		elif question == 'maximize' or question == 'maximize screen':
			print("Sure. Open a new window in your web browser and go to or type: \n"+ website['cybele'] + "\n")

		elif question == "can you help me" or question == "can you help" or question == "help" or question == "help me":
			if 'help' in core and isinstance(core['help'], list):
				print("Here are the topics ordered alphabetically for better help about.\nJust type help <topic>\n")
				nhelp = [key[5:] for key in core['help']]
				nhelp.sort()
				for i in range(len(nhelp)):
					print ( "   - " + nhelp[i])
				del nhelp
				print ("")
			else:
				print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " My programming seems to have a glitch. " + _auth1r_ + "'s code is too powerful for me!\n")

		elif question == "time" or question == "what time it is" or question == 'clock time':
			print ("The current time is "+datetime.now().strftime("%H:%M")+".\n")
		elif question == "what day it is" or question == 'what day is it' or question == 'date':
			print ("Today is " + days[weekdaydate] + " and currently is "+datetime.now().strftime("%d")+" of "+month_name+" from "+datetime.now().strftime("%Y")+".\n")

		elif question.find('happy birthday cybele')!=-1 or question.find('cybele happy birthday')!=-1 or question.find('happy birthday')!=-1:
			dt = date.today()
			if (str(dt)[5:]) == _active_[3:5] + "-" + _active_[0:2]:
				random.shuffle(messages['birthday_msg'])
				print (random.choice(messages['birthday_msg']))
				print ("")
			elif (str(dt)[5:]) == '05-04' and question == 'happy birthday':
				random.shuffle(messages['birthday_msg'])
				print (random.choice(messages['birthday_msg']))
				print ("Here's a eternal gift: " + website['may4th'] )
				print ("")
			elif (str(dt)[5:]) == '12-09' and question == 'happy birthday':
				random.shuffle(messages['birthday_msg'])
				print ("In name of vorian " + random.choice(messages['birthday_msg']))
				print ("Vorian, {} personal website went online makes {} years ago on this same day.\n".format(_auth1r_ , date.today().year - date(2010,12,9).year))
			else:
				if _cybid_ == True:
					print( random.choice(messages['birthday_short']) + " Are trying to trik'me, hmm! Its "+month_name+", "+date.today().strftime("%d")+". BAD " + os.getlogin() + "!\n")
				else:
					print( random.choice(messages['birthday_short']) + " Are trying to trik'me, hmm! Its "+month_name+", "+date.today().strftime("%d")+". BAD User!\n")

		elif question == 'merry christmas' or question == 'i wish you a merry christmas':
			dt = date.today()
			if dt.day >= 20 and dt.day <= 26:
			#if (str(dt)[5:]) == '12-25':
				print ("Merry Christmas to you too!\nI hope you have a wonderful holiday season filled with joy, care and love.\n")
				print ("A litle present for you:\n 〉 https://kernelx64.trinket.io/sites/christmastree")
				print ("You should take a look at the page, only available around Christmas:\n" + " 〉 "+ website['home'] + "/merrychristmas")
				print ("")
			else:
				# Use the weather_season_condiction() or get_the_season() to play with "i'm definitely not ready for the cold and snow"
				if _cybid_ == True:
					random.shuffle(messages['notchristmas'])
					print (random.choice(messages['notchristmas']) + ". Okay, " + os.getlogin() + "!\n")
				else:
					random.shuffle(messages['notchristmas'])
					print (random.choice(messages['notchristmas']) + "\n")

		elif question[:16] == 'happy valentines' or question[-16:] == 'happy valentines':
			dt = date.today()
			if (str(dt)[5:]) == '02-14':
				random.shuffle(messages['valentinesmsg'])
				print (random.choice(messages['valentinesmsg']))
				print ("A litle present for you:\n 〉 https://kernelx64.trinket.io/sites/lovers-heart")
				print ("")
			else:
				random.shuffle(messages['notvalentines'])
				print (random.choice(messages['notvalentines']) + "\n")

		elif question.find('happy new year')!=-1:
			dt = date.today()
			if (str(dt)[5:]) == '12-31':
				random.shuffle(messages['newyear_msg'])
				print (random.choice(messages['newyear_msg']))
				print ("Enjoy the Fireworks:\n 〉 https://kernelx64.trinket.io/sites/fireworks")
				print ("")
			else:
				random.shuffle(messages['earlier_nyear'])
				print( random.choice(messages['earlier_nyear']) + "\n")

		elif question == 'what is your version' or question == '#version':
			nversion = "I am "+_title_ +" in the version "+version+" last updated in "+_revise_+" running for " + str(days_till_today.days) + " days."
			if _chkdsk_ != '':
				print (nversion + "\nMy current verification code is '" + _chkdsk_ + "'.\n")
				#print (nversion + "\nMy current verification code is '" + chkcybele(_chkdsk_,shift) + "'.\n")
			else:
				print (nversion + "\n")
		#------------------------------------------------
		elif question =='convert gps to distance' or question == 'gps to distance' or question == 'harvesine' or question == 'harvesine formula':
			pregpsconvert()

		#------------------------------------------------
		elif question[-11:] == 'sunset time' or question[-12:] == 'sunrise time':
			print ("\n"+kolor['YELLOW']+"Daily solar schedule for " + kolor['OFF']+ date.today().strftime("%d.%m.%Y") + "\n")
			if _poigps_[4] == 0:
				try:
					latgps = float(input('What is your latitude coordinates: '))
					if latgps > 90 or latgps < -90:
						print("The latitude degrees format are out of range!\n")
						continue
					_poigps_.insert( 0, latgps)
					longps = float(input('What is your longitude coordinates: '))
					if longps > 180 or longps < -180:
						print("The longitude degrees format are out of range!\n")
						continue
					_poigps_.insert( 1, longps)
					defgps = 'user input'
				except ValueError:
					print("Value not recognized like latitude or longitude gps coordinates!\n")
					continue
			else:
				defgps = 'default gps'
			print ("calculations for " + str(latgps) + "," + str(longps) + " to UTC using "+ defgps)

			drawart('art_world')

			s = Sun(datetime.now(), _poigps_[0], _poigps_[1])
			print(' 〉    Sunrise : ' + str(s.sunrise()))
			print(' 〉 Solar noon : ' + str(s.solarnoon()))
			print(' 〉     Sunset : ' + str(s.sunset()))
			print("")
		elif question == 'moon phase' or question == 'what is the moon phase' or question =='what is the actual moon phase':
			if _poigps_[3] == 0:
				try:
					mlatgps = float(input('\nWhat is your latitude coordinates: '))
					if mlatgps > 90 or mlatgps < -90:
						print("The latitude degrees format are out of range!\n")
						continue
					_poigps_.insert( 0, mlatgps)
					mlongps = float(input('What is your longitude coordinates: '))
					if mlongps > 180 or mlongps < -180:
						print("The longitude degrees format are out of range!\n")
						continue
					_poigps_.insert( 1, mlongps)
				except ValueError:
					print("Value not recognized like latitude or longitude gps coordinates!\n")
					continue
			moon_phase = MoonPhase(_poigps_[0], _poigps_[1], datetime.now())
			print("\n"+"Currently the moon phase is", moon_phase.phase_of_moon(),"\n")

		elif question == 'diagnostics' or question == 'show core' or question == '#core':
			print("Here he is my full internal specifications :\n")
			if node_name:
				print('   Device : ' + platform.node() + '|' + _cyext_[0:4].replace(" ",""))
			else:
			  print ('  Device : trinket.io platform')
			print('     Name : ' + _title_)
			print('  Version : ' +version)
			print('  Revised : ' +_revise_)
			print('   Memory : ' + str(len(questions))+"|"+str(len(answers))+"|D"+str(len(chkdict)))
			print('     Data : ' + str(sum(len(value) for value in core.values())) + "|O" + str(len(oldtech_terms)) + "|M" + str(len(meaning_term)))
			print('    Linux : ' + str(len(linux_commands)))
			print('    Astro : ' + "G"+str(len(core["astronomy glossary"])) + "|A" +  str(len(core["asteroid"])) + "|C" +  str(len(core["constelattion"])) + "|S" +  str(len(core["star name"])))
			print('    World : ' + str(len(core["country"])))
			print('  Running : ' + str(days_till_today.days) + ' days.\n')

		elif question == 'date' or question == 'today' or question == 'today is' or question == 'what day is today' or question == 'what is the date' or question == 'what is today':
			now = datetime.now()
			iniyeardays = date.today() - date( date.today().year, 1, 1)
			current_time = now.strftime("%H:%M:%S")
			days_left = days_until(date(year=date.today().year, month=12, day=31))

			print( str(days[weekdaydate]) + ", " + str(date.today().strftime('%d') ) + " " + str(month_name) + " of " + str(date.today().strftime('%Y')) + ", " + str( current_time) + " - GMT" + str (strftime("%z", gmtime())) + "\n")
			print("We are in the " + str(date.today().isocalendar()[1]) + " week of the current year.")
			print("Is the day "+ str(iniyeardays.days) + " since beginning of the year")
			print("There are "+ str(days_left) +" days left until " + str(date.today().year) + " ends\n")
		elif question == 'leap year' or question == 'is this year a leap year':
			print (leapyear())

		elif question[0:7] == "convert" and question[-4:] =="days" or question[-3:] =="day" or question[-7:] =="seconds" or question[-7:] =="minutes" or question[-5:] =="hours":
			sub = question.split()[1:]
			if not sub[0].isdigit():
				print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " For now i dont handle: "+str(sub[0])+". It's a number with decimals! Maybe in the future.\n")
			elif not int(sub[0]):
				print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " I'm having a problem with the "+str(sub[0])+" number. !\n")
			elif len(sub) >= 3 and sub[2] != "in":
				print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " There is a problem in convert systax. convert <VALUE> days in <TIME UNIT>!\n")
			elif len(sub) > 4:
				print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Wow! To many parameters! convert <number> days in/to <time unit>.\n")
			elif sub[1]!='seconds' and sub[1]!='minutes' and sub[1]!='hours' and sub[1]!='days' and sub[1]!='day':
				print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " There's be some kinda of problem with your "+sub[1]+" time Unit!\n")
			else:
				if len(sub) == 4 and sub[2] != 'to' and sub[2] != 'in':
					print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Usage method : convert <"+str(sub[0])+"> days "+sub[2]+" <unit>.\n")
				else:
					if len(sub) == 2:
						unit = 'None'
						number = int(sub[0])
						calculated = days_to_units(number)
					elif len(sub) == 4:
						unit = sub[3]
						number = int(sub[0])
						calculated = days_to_units(number)

					if not calculated:
						print ( random.choice(messages['trouble_short']) + " " + random.choice(core['trouble_msg']) + " Something happen cos i did not calculate nothing!\n")
					else:
						if unit == 'None':
							calculate_minutes = calculated[0]
							calculate_hours = calculated[1]
							calculate_seconds = calculated[2]
							print("Based on my calculations is {:,.0f} seconds | {:,.0f} minutes | {:,.0f} hours.\n".format(calculate_seconds, calculate_minutes, calculate_hours))
						else:
							value_unit = ' '.join(sub[0:2])
							if unit == 'seconds':
								calculate_seconds = calculated[2]
								print("Based on my calculations "+ value_unit + " are equivalent to {:,.0f} seconds. \n".format(calculate_seconds))
							elif unit == 'minutes':
								calculate_minutes = calculated[0]
								print("Based on my calculations "+ value_unit + " are equivalent to {:,.0f} minutes. \n".format(calculate_minutes))
							elif unit == 'hours':
								calculate_hours = calculated[1]
								print("Based on my calculations "+ value_unit + " are equivalent to {:,.0f} hours. \n".format(calculate_hours))
							else:
								print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Something happen! You should report this to my developer.\n")

		elif question[0:7] == "convert":
			sub = question.split()[1:]
			qconvert = convert_units( question )
			if qconvert[0] != 0 and qconvert[1] != None:
				converted_value = str("{:,.2f}".format(convert_units( question )[0]))
				to_unit_converted = str(convert_units( question )[1])
				if sub[2] == "au":
					sub[2] = 'Astronomical Units'
				print("In my knowledge converting the value %s from %s is %s %s.\n" % (sub[0], sub[2], converted_value, to_unit_converted))

		elif question == 'how many weeks have a year' or question == ' year weeks':
			print ( str(daysweeks_year()[1]) + " weeks. A calendar year consists of " + str(daysweeks_year()[1]) + " weeks, " + str(daysweeks_year()[0]) + " days in total.\n" )

		elif question == 'week' or question == 'week number' or question == 'what number is this week' or question == 'what is this week number':
			week_number = date.today().isocalendar()[1]
			print ("Based on the system actual date this is the " + str(get_ordinal_position(week_number)) + " week of the year.\n")

		elif question.find('last')!=-1 and question.find('update')!=-1:
			print ('My creator '+ _auth1r_ + ' the last time updated my internal data was in '+ _revise_ +'.\n')

		elif question == 'yes':
			if len(csugestions) == 0:
				print ("Yes! what ? What do you mean ?\n")
			elif len(csugestions) == 1:
				print ("Yes! hmm...")
				question = csugestions[0]
				print ("So, the question you want to make'me is [" + question + "]\nNow you know what to write to ask'me.\n" )
			else:
				print ("Yes what ?! There are infinite possibilities! \nSo better write down the one you want to ask'me. \nI'm "+_title_+" a chat bot by "+ _auth1r_ +" not the f* Merlin, the wizard.\n")

		elif question.find('current')!=-1 and question.find('century')!=-1:
			current_century = get_current_century()
			print(current_century)

		# world population
		elif question[-10:] == "population":
			country_name = question.split()[0]
			if country_name in core['country']:
				print("Estimated population based on my offline data from [{}] \n{} has a population of {:,} according to the United Nations.\n".format(_active_, country_name.capitalize(), countries[country_name]["population"]))
			elif country_name == 'world' or country_name == 'earth':
				print ("8.1 billion people in July 2024 according to the United Nations. Is "+ year_months[date.today().month-1] +", "+ str(date.today().year) +" so there must be quite a few more.\n")
			else:
				print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " What ?! " + country_name.capitalize() + " Is that a new country? Perhaps! No-can do.\n")

		elif question[0:8] == 'where is' and question.find('iss')!=-1 or question.find('zarya')!=-1:
			if _cybid_ == True:
				if internet_onoff() == False:
					print (random.choice(messages['trouble_msg']) + " To do this task i need be connected to the internet. \n")
			else:
				print (where_is_iss())

		elif question == 'people in space':
			if _cybid_ == True:
				if internet_onoff() == False:
					print (random.choice(messages['trouble_msg']) + " To do this task i need be connected to the internet.\n")
			else:
				people_in_space()

		elif question == 'is he watching' or question == 'your fav tvshows' or question == 'your favorite tvshows':
			if question.find('fav')!=-1 or question.find('favorite')!=-1:
				print ("You can know what are "+_auth1r_+"'s in her public profile.\n  > "+ website['trakt'] + "\n")
			else:
				print ("You can follow real time what "+_auth1r_+" is watching by her trakt.tv profile.\n  > "+ website['trakt'] + "\n")

		elif question == "do you speak" or question == 'do you talk' or question[-13:] == 'say something' or question[-15:] == 'make a sentence':
			cybele_phrase = make_sentence()
			print ("Well, beside behing a βeta version and dont using NLP or Library's or even speech synthesis here's something:")
			print ("\n - " + cybele_phrase + "\n")

		elif question[0:5] == "let's" or question[0:4] == "lets" or question.find("play")!=-1 or question.find("game")!=-1:
			if question.find("math")!=-1:
				cybele_math_game()
			if question.find("countries")!=-1 or question.find("capitals")!=-1:
				wcountry = {}
				for country, data in countries.items():
					wcountry[country] = data["capital"]
				cybele_play_quiz(wcountry,1)
				del wcountry
			if question.find("constellations")!=-1:
				cybele_play_quiz(constellations_dict,2)
			if question.find("elements")!=-1:
				cybele_play_quiz(periodic_elements,3)

		elif question.find('show')!=-1 and question.find('my')!=-1 and question.find('score')!=-1:
			# gamescore = [-1,0,0] [Play [-1,0]] , [Game [1,2,3,4] , [score]
			if gamescore[0] == -1:
				print ("Did you play!? " + random.choice(messages['game_messages']) + "\n")
			else:
				if gamescore[1] == 1 and gamescore[2] == 0:
					print (str(gamescore[1]) + "! I'm starting to thinking I'm allergic to maps...\n")
				elif gamescore[1] == 1 and gamescore[2] != 0 :
					print ("My geography teacher is so proud right now. " + str(gamescore[1]) + "! Or terrified.\n")
				elif gamescore[1] == 2 and gamescore[2] == 0:
					print ("I'm starting to think " + str(gamescore[1]) + " aliens have replaced my brain with cheese.\n")
				elif gamescore[1] == 2 and gamescore[2] != 0:
					print (str(gamescore[1]) + "! I'm basically an honorary astronaut now.\n")
				elif gamescore[1] == 3 and gamescore[2] == 0:
					print ("I'm starting to think " + str(gamescore[1]) + " Oxygen overload! Periodic Panic.\n")
				elif gamescore[1] == 3 and gamescore[2] != 0:
					print (str(gamescore[1]) + "! I'm a Quantum Quack **Gold Medal Chemist!**.\n")
				elif gamescore[1] == 4 and gamescore[2] == 0:
					print ("I'm starting to think " + str(gamescore[1]) + " is a Calculus catastrophe! Statistics shock!\n")
				elif gamescore[1] == 4 and gamescore[2] != 0:
					print ("Algebra-ly speaking..." + str(gamescore[1]) +  " I'm a Eureka's master!.\n")

		elif question == 'reset my score' or question == 'reset score':
			if gamescore[1] == 0:
				print ("Reset What! " + random.choice(messages['gamereset']) + "\n")
			else:
				resetscore = input ("This action is irreversible. Continue? [yn]: ").lower()
				if resetscore == "y" or resetscore == "yes":
					gamescore[0] = -1
					gamescore[1] = 0
					gamescore[2] = 0
					print ('Score reseted. ' + random.choice(messages['gamereset_msg']))
				print ("")

		elif question[0:8] == 'infostar':
			star_name = question[9:]
			if len(star_name) == 0:
				random.shuffle(messages['nostar_message'])
				print("Definitely the name of the star went on vacations!?! " + random.choice(messages['nostar_message']) + "\n")
			elif _cybid_ == False:
				print("\n" + _spchar_[1:2] + "Considering you problaly have the star name right or correct:" + "\n" + "Here's the " + star_name.capitalize() + " in the symbad.cds database online!")
				print(" "*2 + website['symbad'] + star_name )
				print ("")
				copy2clipboard(website['symbad'] + star_name)
			elif internet_onoff() == False:
				print (random.choice(messages['trouble_msg']) + " To get '" + star_name.capitalize() + " star' information i need an active Internet connection.\n")
			else:
				response = get_star_info(star_name)
				if len(response) != 0 and response[0] != 'emptydata':
					for i in range(len(response)):
						print (response[i])
				else:
					print( random.choice(messages['nostar_message']) + "cybele.star #" + star_name + " have empty data!\n")

		elif question[0:13] == 'sharing about':
			sub = question.split()[2:]
			if len(sub) == 0:
				print( random.choice(messages['trouble_msg']) + " I really have to learn or with AI to read the TVshows from the users mind's!\n")
			else:
				tvshow_share = ' '.join(sub)
				if python_version() == '3.2.0':
					print ("Select the link with the mouse and selected press Ctrl+C to copy it to the clipboard.\n")
				if tvshow_share in webshare:
					print("Related to the digited name of the " + tvshow_share.upper() + " i have this link: \n > " + chkcybele(webshare[tvshow_share],shift) + "\n")
					copy2clipboard(chkcybele(webshare[tvshow_share],shift))
				else:
					print (random.choice(messages['trouble_msg']) + " I dont have any sharing information about the " + tvshow_share.title() + " tvshow.\n")
				#shareis = webshare.get(tvshow_share, "Not found.\n")
		elif question == 'sharing tvshow' or question == 'share tvshow':
				netchk = False
				if _cybid_ == True and internet_onoff() == True:
					netchk = True
				print ("The "+str(len(webshare))+" sharing informations i have are about the following TVSHOW's:\n")
				for tvshow, link in webshare.items():
					print(" > " + str(tvshow.upper()))
					print(" "*3 + chkcybele(str(link),shift))
					if netchk == True:
						print(" : " + str(link_status(chkcybele(link,shift))))
				print ("")

		elif question == 'today activity':
			if ta == True:
				print (random_season_activity())
				ta = False
			else:
				print (random.choice(messages['activity_msg']) + "\n")

		elif _cybid_ == True and question == 'extcybele' or question == 'extver' or question == 'extdir':
			print ( kolor['RED'] + " 〉 Cybele external Library Module by AS" + kolor['OFF'])
			print ("   Loaded : " + str(_cybid_))
			print ("   Module : " + extvars[2] + ".py")
			print ("  Version : " + extvars[0])
			print ("  Revised : " + extvars[1])
			print (" Commands : " + str(len(addcomm)))
			print ("")

		elif question == 'weather':
			dayseason = get_the_season()[0]
			print ("It's look like we have " + weather_like_season() + " based in the fact we are in the " + dayseason.capitalize() +".\n")

		elif question[-9:] == 'about you':
				print ("Ok!. My name is " + _title_ +" and I was maded by " + _auth1r_ + " " + str(days_till_today).replace(", 0:00:00","") + " ago. I was builded to be a extention of Vorian, this website.\n" + aboutyou + "\n" )

		elif any(word in question for word in core['askard_command']):
			manage_db(question)

		elif question[0:8] == 'presence':
			if any(word in question for word in presence_online):
				sub = question.split()[1:]
				if len(sub) == 0:
					print( random.choice(messages['trouble_msg']) + " I really have to learn or with AI to read users mind's!")
				else:
					service = ' '.join(sub)
					if service in presence_online:
						print ("Yes, " + _auth1r_ + " have a online presence on that service. Here is the direct link: \n "+_spchar_[1:2] + presence_online[service] + "\n")
			elif "services" in question:
				digifoot = str(len(presence_online))
				presence_online_abc = list(presence_online.keys())
				presence_online_abc.sort()
				print ("%s have a online presence or a digital footprint in this %s entities/services on the internet:\n" % (_auth1r_, digifoot))
				for service in presence_online_abc:
					print(" "*3 + _spchar_[4:5] + " " + service.title())
				print("")
			else:
				if len(presence_online) == 1:
					print( presence_online['online'] + "\n")
				else:
					print (random.choice(messages['trouble_msg']) + " I dont have any "+ _auth1r_ +" online presence information for the '" + " ".join(question.split()[1:]).title() + "' service.")

		elif question[0:8] == 'phonetic':
			words = question.split()[1:]
			if len(words) != 0:
				print ("Phoneticly speaking: " + phonetic_alphabet(' '.join(words)) + "\n")
			else:
				print (random.choice(messages['trouble_msg']) + " I cannot transform emptyness to the phonetic alphabet except with silence.\n")

		elif question[0:5] == 'morse':
			morse2 = question.split()[1:]
			if len(morse2) != 0:
				print ("Translation to morse code: " + morse_code(' '.join(morse2)) + "\n")
			else:
				print (random.choice(messages['trouble_msg']) + " I cannot transform emptyness to the morse code except with silence.\n")

		elif question[0:7] == 'demorse':
			morse2 = question.split()[1:]
			if len(morse2) != 0:
				print ("Translation of the morse code: " + morse_decode(' '.join(morse2)) + "\n")
			else:
				print (random.choice(messages['trouble_msg']) + " I cannot transform emptyness to the morse code except with silence.\n")

		elif question[0:8] == 'yoda say':
			senyoda = question.split()[2:]
			if len(senyoda) != 0:
				print (yoda_speak(senyoda) + "\n")
			else:
				print (random.choice(list(core['yodaw'])) + "\n")

		elif question == 'view planets orbits' or question == 'view orbiting planets':
			print ("Simulating Orbiting Planets in the Solar System.\n  > "+ website['solar'] + "\n")

		elif question == 'licence' or question.find(_title_.lower() + ' licence')!=-1:
			for i, line in enumerate(__doc__.splitlines()):
				if i >= len(__doc__.splitlines()) - 2:
					if i == 6:
						line = line.replace("# This","# " + __doc__.splitlines()[1][0:6] + " this")
					print(line)
			print ("")

		elif question != '':
			answer = find_answer(question,questions)
			print(answer)

if __name__ == "__main__":
	try:
		while True:
			if main() == False:
				break
		print(random.choice(core['exitmsg']) + random.choice(['',' Bye.']))
		globals().clear()
	except KeyboardInterrupt:
		print ("")
		print(random.choice(core['exitmsg']) + random.choice(['',' Bye.']))
	globals().clear()
