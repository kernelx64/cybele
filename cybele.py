#py:python_OS_win_linux_shell_cmd
__doc__ = """
Cybele by AS for www.adelinosaldanha.site ✦

# This Python script is licensed under the GNU General Public License, version 2.
# See the LICENSE file for more details: https://www.gnu.org/licenses/gpl-2.0.en.html
"""
# Latitude and longitude of your city for use with the command <set default gps> for <sunset time> for ex.
lat = 41.5454
lon = -8.4265

# static global cybele variables
version = '1.0 βeta'
_title_ = 'Cybele'
_pcnode_ = ['ASUSK','TUMBLEWEED']
_spchar_ = '⚝〉“”—❛❜↺心🦖🔗𝒊️💡😊🏆🐧🎯❝❞'
_active_ = '01.08.2024'
_revise_ = '31.05.2025'
_author_ = 'Adelino Saldanha'
_auth1r_ = _author_.split()[0]
_cyext_ = " extention"
_cybid_ = False

import sys,re
import subprocess
try:
	import string
	import random
	import math
	import datetime
	import os,time
	import platform
	import hashlib
	import sqlite3
	import sqlitecloud
	import requests
	import json,html,urllib
	import holidays
	import quote
	import locale
	import pycountry
	from bs4 import BeautifulSoup
	from random_word import RandomWords
	from platform import python_version
	from time import gmtime, strftime, sleep
	from inspirational_quotes import quote
	from datetime import datetime
	from datetime import date, time, timedelta
	from math import degrees as deg, radians as rad
	from math import floor, ceil, pi, atan, tan, sin, asin, cos, acos

except ImportError as err:
	match = re.search(r"'(.*?)'", str(err))
	if match:
		module_name = match.group(1)
		print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {err}")
		while True:
			install_choice = input(f"{' '*3}Do you want to install '{module_name}' module? (y/n): ").lower()
			if install_choice == 'y':
				print(f"{' '*3}Attempting to install the '{module_name}' module...\n")
				try:
					subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
					print(f"\n{' '*3}'{module_name}' installed successfully. Please restart {_title_}")
					sys.exit(0)
				except subprocess.CalledProcessError as e:
					print(f"\n{' '*3}Error installing the module. Try installing it manually: pip install " + module_name)
					sys.exit(0)
				break
			elif install_choice == 'n':
				print(f"{' '*3}Cannot execute properly. Exiting.")
				sys.exit(0)
			else:
				print(f"{' '*3}Invalid choice. Please enter 'y' or 'n'.")
	else:
		print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {err}")
		print(f"{' '*3}I cannot execute properly. Exiting.")
		sys.exit(0)

start_time = datetime.now()
node_name = platform.node()
country_code = locale.getlocale()
if node_name:
	sysos = platform.system()
	if platform.node().upper() in [node.upper() for node in _pcnode_]:
		try:
			import cybext
			_cybid_ = True
			_cyext_ = _cyext_.replace(_cyext_[0:4],_cyext_[0:4].upper())
			addcomm = [];extvars = []
			addcomm = cybext.addcommands()
			extvars = cybext.extinternal_vars()
		except ImportError:
			_cybid_ = False

#------------------------------------------------------------------
# Init-process
def print_statusline(msg: str):
    last_msg_length = len(getattr(print_statusline, 'last_msg', ''))
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    setattr(print_statusline, 'last_msg', msg)
print_statusline(f"\nLoading ...")

#-----------------------------------------------------------
chkcyb = "Ngtnmahkbsxw Fhwbybvtmbhg Wxmxvmxw.\n   Kxlixvmbgz max tnmahk'l vhgmkbunmbhgl bl yngwtfxgmte mh max ikbgvbiexl hy hixg-lhnkvx wxoxehifxgm.\n   Xqbmbgz."
seecoor = "Etmbmnwx tgw ehgzbmnwx kxjnbkxw otenxl tkx ghm gnfxkbvl hk bgvhkkxvml."
year_months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
aboutyou = "B'f t wbghltnk bg t mxva tzx, unm B'f lmbee xqxvnmbgz fr vhwx yetpexller."
days_till_today = date.today() - date(year=int(_active_[6:]), month=int(_active_[3:5]), day=int(_active_[0:2]))
iknow_pun = {"i know": "you know","you know": "i know"}; cybelecode = []
month_name = date.today().strftime('%B');next_year = str(date.today().year + 1);weekdaydate = date.today().weekday()
shift=int(round(math.sqrt(math.log(math.cosh(10)) * 1000 - math.degrees(math.acos(-1)) * 3) + math.e**2)-56);
stars_dict = {};constellations_dict = {};constellations_abbr = {};linux_commands = {};midbcounter=0
tables = ['astronomy_glossary','climate_dict','constelations','countries','funfacts','linux_commands','meanings','nicethings','oldtech','qa_astro','season_activities','stars','topactivities']
gamescore=[-1,0,0]

#-----------------------------------------------------------
website = {
	"home": "https://www.adelinosaldanha.site",
	"mystory": "https://www.adelinosaldanha.site/mystory",
	"may4th" : "https://dub.sh/1vgai8g",
	"tvshow": "https://www.adelinosaldanha.site/tvshows",
	"thamix": "https://www.adelinosaldanha.site/thamix",
	"deserted": "https://www.adelinosaldanha.site/deserted",
	"trails": "https://www.adelinosaldanha.site/trails",
	"trakt": "https://simkl.com/4378279/tv/watching/",
	"askard": "https://www.adelinosaldanha.site/askards"
}
webshare = {
  "tvshow": "ammil://fxzt.gs/yhewxk/2giceUKV#Lh7eUjNr_3MaG-f0yMTLAz",
  "movies": "ammil://fxzt.gs/yhewxk/2giceUKV#Lh7eUjNr_3MaG-f0yMTLAz",
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
	"cthemes":	["I know about","Let's explore the together about","Based on my knowledge","You can ask me about",
				"If you are curious you can ask'me about","I can anwser questions about","I can share knowledge about",
				"I can provide you answers about","I can tell you about","I have knowledge about"],
	"question_words":	["who", "what", "when", "why", "can", "whose", "which"], #"how","where"],
	"game_starters":	["play", "game"],
	"game":	["countries", "capitals", "math", "constellations", "elements"],
	"working_hard":	["Cybele is taking a break right now. Please wait a moment and try again later."],
	"yodaw":	["Hmm. Nothing to transform, there is.","Empty, the input is.","Words, there are none.","Silence, I hear.",
				"Lost, the input is.","A void, it seems.","Speak, nothing does.","Unspoken, it remains.","Gone, all the words are."],		
	"share":	["sharing about","sharing links"],
	"sayconvert":	["say","longhand"],
	"coded":	["py","python","python art"]
}
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
	
	"nicefun_msg":	["You've reached your daily limit! Please check back tomorrow for more.","That's all for today! Your daily allowance will reset at midnight.",
					"Looks like you've enjoyed your fill for today. Come back tomorrow for fresh content!","Daily limit reached. New content will be available after your local midnight.",
					"You've hit your daily quota! We'll have more for you tomorrow.","All out for today! We're saving some good stuff for you for tomorrow.",
					"Thanks for engaging! You've reached your daily maximum. See you tomorrow!","Oops, you've exhausted your daily supply! More will be ready for you soon.",
					"Time for a break! Your daily limit has been met. Enjoy the rest of your day and return tomorrow.","Your daily dose is complete! Look forward to more when the clock strikes midnight."],
		
	"notchristmas":	["Wow, you're really getting a head start on the holiday season!","I'm still recovering... Maybe you can lend me your time machine?",
					"Merry Christmas to you too! Just kidding, it's "+month_name+"!.","Thanks for the early holiday cheer.",
					"I'll try to save it for later.","Is this a new kind of time travel?","I'm definitely not ready for snow and eggnog yet.",
					"Let's stick to ice cream and sunshine, okay?","You must be on the naughty list for starting Christmas so early.",
					"Don't worry, I'll keep your secret.","Hold your reindeer! It's still too hot for jingle bells.",
					"Let's enjoy this beautiful "+month_name+" weather first."],

	"not_holiday":	["My favorite exercise is a cross between a lunge and a crunch... I call it lunch on the **holidays**.",
					"The only time 'calories don't count' becomes a universally accepted scientific principle.",
					"I'm on a seafood diet this **holiday** season: I see food, and I eat it.",
					"My brain is 90% song lyrics, 10% useful information, and 100% already planning the next's.",
					"The best part about **holidays**? Realizing my 'to-do' list can wait until next year.",
					"I've got 99 problems, but a **holiday** ain't one... mainly because I'm already on one.",
					"My bank account on **holiday** feels like a public service announcement",
					"Warning: May cause extreme joy, followed by mild panic."],

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
weather_season_condiction = {
	"winter":	["Coldest days","Short days","Long nights","Snow","Ice","Rainy days","Frost","Cold","Bare trees","Chilly winds","Cloudy sky","Freezing rain","Strong cold Wind"],
	"spring":	["Warming temperatures","Longer days","Melting snow","Flower blooming","New life emerging","Gradually warming","Sky partly cloudy","Cloudy to sunny","Moderated wind","Summer is coming"],
	"summer":	["Hot days","Longest days","Shortest nights","Sunny skies","GREEN landscapes","Light breezes","Sunny day","High temperatures","Autumn approaching","Spring as gone"],
	"autumn":	["Cooling temperatures","Falling leaves","Harvest season","Crisp air","Occasional drizzle","Crisp evenings","Changing colors","Sky partly cloudy","Wind increasings","Winter approaching"]
}
#------------------------------------------------------------
topics = ["astronomy glossary","planets","planet orbit","orbits acronyms","asteroids","constelations","information about stars","distance of planets and from the sun",
		"periodic table elements","visualize the periodic table","where is the ISS","people in space","climate dictionary","old tech objects and terms",
		"the world capitals","seasons of the year","play capitals","math game","constellations and elements game","linux command","multiplication table",
		"phonetic alphabet","morse code encoding/decoding","how many days till","moon phases","yoda say","today activity","art python",
		"astronomy questions","difference from <date>","age calc <from date>","Show you the meaning of some words or terms","generate pwd"]

#------------------------------------------------------------
factors = [["feets", 0.3048],["miles", 1.609344],["yards", 0.9144],["m3", 0.001],["gallons", 3.78541178],["fahrenheit", 33.8],["au", 149.6e6]]
#------------------------------------------------------------
help = {
	"help askard": "Usage <view/list> askard | search askard <word> \nDisplays the chosen askard or list all askards in the database. You can also search for a word in existing askards. \nex: view askard 4005\n    list askard\n    search askard time\n",
	"help asteroid": "Usage <asteroid> \nDisplays basic information about the asteroid \nex: vesta\n",
	"help capital": "Usage: capital of <country> | <capital> | <country> \n\nJust type directly the <capital> to know her country, \nJust type directly the <country> to know her capital, \n<capital of <country>> to show what is that Country Capital.\n",
	"help capitals": "Usage: capital of <country> | <capital> | <country> \n\nJust type directly the <capital> to know her country, \nJust type directly the <country> to know her capital, \n<capital of <country>> to show what is that Country Capital.\n",
	"help convert": "Usage: convert <VALUE> from/days <UNIT> | seconds|minutes|hours|feets|miles|yards|AU|m3|gallons|fahrenheit \nAll the convertions are made to kilometers, litters and celcius degrees. \nex: convert 2 days, returns the number of seconds, minutes and hours of 2 days. \n    convert 2 days in hours, returns the total of hours from the number of day(s) \n    convert 2 from miles, returns the number of 2 miles in kilometers \n    convert 2 from m3, returns the number of 2 m3 (cubic meter's) in litters, \n    convert 2 from fahrenheit, returns the number of the degrees in celcius\n",
	"help cybele uptime": "Usage <cybele uptime> \nDisplays the uptime from cybele based on the start execution time.\nex: cybele upytime\n",
	"help days for": "Usage: days for <Christmas/New year/Birthday> \nReturns the number of days left to the event questioned.\n",
	"help days till": "Usage: days till/to <Christmas/New year/Birthday/User Date> \nReturns the number of days left to the event questioned or the user date entered.\nex: days till new year \n    days till 31.12.2030\n",
	"help difference from": "Usage: difference from <date> \nReturns the difference between the digited date to the actual instante in years, months, days, hours, minutes, seconds.\n",
	"help distance": "Usage: distance from <planet/moon> to <planet/moon> \nex: distance from venus to moon, distance from earth to moon, distance from earth to neptune\n",
	"help distances": "Usage: distance from <planet/moon> to <planet/moon> \nex: distance from venus to moon, distance from earth to moon, distance from earth to neptune\n",
	"help exit": "Usage: <exit> <quit> <bye> \nCommand to quit Cybele if you are using cmd or terminal in your OS .\nex: bye\n    quit\n",
	"help find": "Usage: find <topic> \nReturns if there is any information or topic about the questioned.\n",
	"help fun fact": "Usage: fun fact \nReturns: A random, interesting, and often surprising fact.\n",
	"help games": "Usage: play <game> \nPlay the game you digited. \nex: play capitals \n    play constelations\n    play elements \n    play math\n",
	"help genpwd": "Usage: genpwd <number of passwords> <lenght of the passwords> \nGenerate the number of passwords with the lenght you ask. \nex: genpwd 1 8\n    genpwd 20 64\n",
	"help generate pwd": "Usage: genpwd <number of passwords> <lenght of the passwords> \nGenerate the number of passwords with the lenght you ask. \nex: genpwd 1 8\n    genpwd 20 64\n",
	"help gps": "Usage: set default <gps/gps off> | show default gps \nThe default or the most used cordinates are the inserted in the <sunset/sunrise time> command.\n",
	"help holidays": "Usage: <holidays <Two-letters country code>> \nDisplay the current year Holidays for the country given by the two-letters country code. \nex: holidays \n",	
	"help list askard": "Usage: <list askard> | list askard <start> <end>. \nDo a complete List of the askards in the database or from a <start> to a <end>.\nex: list askard\n    list askard 4005 4010\n",
	"help list constellations": "Usage: <list constellations> | list constellations <alphabetically word begin> <alphabetically word end>. \nDo a complete List of the constellations in the database or from a <start> to a <end>.\nex: list constellations\n    list constellations t u\n",
	"help list oldtech": "Usage: <list oldtech> | list oldtech <alphabetically word begin> <alphabetically word end>. \nDo a complete List of the oldtech terms in the database or from a <start> to a <end>.\nex: list oldtech\n    list oldtech web www\n",	
	"help list stars": "Usage: <list stars <alphabetically word begin> <alphabetically word end>. \nList constellations in the database from a <start> to a <end>.\nex: list stars t u\n",
	"help linux command": "Usage: <linux command> \nShows the Syntax a short explanation and examples for the typed linux command.\n",
	"help limits": "Usage: usage <limits <askard|astronomy|oldtech> \nShow the first and last record in the selected database.\nex: limits oldtech\n",
	"help morse": "Usage: morse <word/phrase> \nTranslate to morse code the digited word or phrase. \nex: morse cybele\n",
	"help morse code": "Usage: morse <word/phrase> | demorse <word/phrase> \nEncode to morse code | Decode from morse code : the digited <word/phrase> \nex: morse cybele\n    demorse -.-. -.-- -... . .-.. .\n",
	"help multiplication table": "Usage: multiplication table | x table <number> \nShow the multiplication table for the inputed number \nex: x table 5\n    multiplication table 5\n",
	"help nice thing": "Usage: nice thing \nReturns: A positive and uplifting message or compliment.\n",
	"help demorse": "Usage: demorse <morse code> \nDecode from morse code the digited encode word or phrase. \nex: demorse -.-. -.-- -... . .-.. .\n",
	"help orbit acronym": "Usage <orbit acronym> \nDisplays basic information about the orbit and her principals. \nex: geo\n",
	"help orbit": "Usage: <planet> orbit / <orbit acronym> \nShow the type of the orbit from the typed planet / Displays basic information about the orbit and her principals. \nex: earth orbit\n    geo\n",
	"help presence": "Usage: presence <service> \nShow's the direct link for "+_auth1r_+" online/internet presence in the digited service. \nex: presence asus\n    presence trinket\n",
	"help planet": "Usage: <name of the planet> typed directly\nReturns some basic information about the planet name typed.\n",
	"help play game": "Usage: play game <capitals/constelattions/math> \nPlay the game of your choose. \n\nex: Capitals makes'you know and learn of what Country it is. \n    Constellations is given the constellation name to you anwser her learned abbreviation thru me. \n    Math game is a memory training game with addiction, subtration and multiplication factors.\n",
	"help play": "Usage: play game <capitals/constelattions/math> \nPlay the game of your choose. \n\nex: Capitals makes'you know and learn of what Country it is. \n    Constellations is given the constellation name to you anwser her designation learned thru me. \n    Math game is a memory training game with addiction, subtration and multiplication factors.\n",
	"help phonetic": "Usage: phonetic <word/phrase> \nTransform to the NATO phonetic alphabet what is the base for HAM and Military's the word or the phrase digited. \n\nex: phonetic cybele \n",
	"help search": "Usage: search <askard|astronomy|oldtech> \nSearch a substring in specific database. \nex: search askard time \n    search astronomy radio \n    search oldtech disk\n",
	"help seek": "Usage: seek <topic> \nReturns if there is any information or topic about the questioned.\n",
	"help sharing about": "Usage: sharing about <tvshow name> \nDisplays a link from the specific content of the tvshow marked in the list on the TV programs page.\nThe link available is automatically copied to the clipboard.\nex: sharing about nautilus\n",
	"help show me": "Usage: show me <star names|all/constellations|asteroids|quote  names|old tech words|linux commands> \nReturn the values or data for the required subject.\n",
	"help star": "Usage <star name> \nDisplays basic information about the star. \nex: Polaris (knowed by north star)\n",
	"help stars from": "Usage: stars from <constelation>\nShow the stars from the inputed constelation. \nex: stars from Taurus \n    stars from andromeda\n",
	"help today activity": "Usage <today activity> \nDisplays a activity for you based in the actual year season.\n",
	"help view askard": "Usage: view askard <id> \nView the refered askard by the id selected.\nex: view askard 4005\n",
	"help view solar system": "Usage: view solar system \nView a horizontal representation of the solar system.\nex: view solar system\n",
	"help x table": "Usage: x table | multiplication table <number>\nShow the multiplication table for the inputed number \nex: multiplication table 5 \n    x table 5\n",
	"help yoda say": "Usage yoda say <sentence> \nTransforms the given sentence to Yoda speach alike \nex: Yoda say the force is strong with this one\n"
}
#------------------------------------------------------------

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
def chkcoor(lat, lon):
    try:
        lat_val = float(lat)
        if not (-90 <= lat_val <= 90):
            return False
    except (ValueError, TypeError):
        return False
    try:
        lon_val = float(lon)
        if not (-180 <= lon_val <= 180):
            return False
    except (ValueError, TypeError):
        return False
    return True

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
		return False

#--------------------------------------------------------
def fetch_fromdbfile(db_filename, table_name, column_name):
	conn = None
	if internet_onoff() == True:
		print_statusline(f"Connecting with remote database ...")
		conn = sqlitecloud.connect("sqlitecloud://cxuomo3ahz.g1.sqlite.cloud:8860/cybele.sqlite?apikey=9o4zGGVvXKMu74P2OzDhrotTOBp9GCGQ2a0VotuCMms")
	else:
		print_statusline(f"Checking local database ...")
		if os.path.isfile (db_filename) == True :
			conn = sqlite3.connect(db_filename)
		else:
			print_statusline(f"")
			modname = "The " + db_filename.upper() + " database file is missing, and with no internet, the online database is inaccessible. \n   I cannot execute properly. Exiting."
			print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			exit(0)
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT {column_name} FROM {table_name}")			
		result = [row[0] for row in cursor.fetchall()]
		return result 
	except sqlitecloud.exceptions.SQLiteCloudOperationalError as e:
		print_statusline(f"")
		error_message = f"SQLiteCloud Database error {e} \n{' '*12}I cannot execute properly. Exiting."
		print(f"\n\033[1;31m {_spchar_[1:2]} {_title_}\033[0;0m: {error_message}")
		exit(0)
	except sqlite3.Error as e:
		return []
	finally:
		if conn:
			conn.close()
			
#------------------------------------------------------------
def dbfetch(db_filename, record, table_name, search_column, column_to_fetch):
	conn = None
	if internet_onoff() == True:
		conn = sqlitecloud.connect("sqlitecloud://cxuomo3ahz.g1.sqlite.cloud:8860/cybele.sqlite?apikey=9o4zGGVvXKMu74P2OzDhrotTOBp9GCGQ2a0VotuCMms")
	else:
		if os.path.isfile (db_filename) == True:
			conn = sqlite3.connect(db_filename)
		else:
			print_statusline(f"\nLoading ...")
			modname = "The " + db_filename.upper() + " database file is missing, and with no internet, the online database is inaccessible. \n   I cannot execute properly. Exiting."
			print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			exit(0)
	
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT {column_to_fetch} FROM {table_name} WHERE {search_column} = ?", (record,))
		result = cursor.fetchone()
		if result:
			return result[0]
		else:
			return None
	except sqlite3.Error as e:
		return None
	finally:
		if conn:
			conn.close()

#--------------------------------------------------------
def check_tables(tables_names):
	db_filename = 'cybele.db'
	missing_tables = []
	conn = None
	cur = None
	
	if internet_onoff() == True:
		print_statusline(f"Connecting with remote database ...")
		conn = sqlitecloud.connect("sqlitecloud://cxuomo3ahz.g1.sqlite.cloud:8860/cybele.sqlite?apikey=9o4zGGVvXKMu74P2OzDhrotTOBp9GCGQ2a0VotuCMms")
	else:
		if os.path.isfile (db_filename) == True :
			print_statusline(f"Checking local database ...")
			conn = sqlite3.connect(db_filename)
		else:
			print_statusline(f"")
			modname = "The " + db_filename.upper() + " database file is missing, and with no internet, the online database is inaccessible. \n   I cannot execute properly. Exiting."
			print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			exit(0)
	if conn is None:
		print_statusline(f"")
		modname = "Could not establish a database connection. \n   I cannot execute properly. Exiting."
		print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			
		return False, "Error: "
	try:
		cur = conn.cursor()
		cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
		existing_tables = [row[0] for row in cur.fetchall()]
		for table_name in tables_names:
			if table_name not in existing_tables:
				missing_tables.append(table_name)

		if missing_tables:
			print_statusline(f"")
			modname = f"The database file is from a previous version and dont satisfy all my requirements.\n   I cannot execute properly. Exiting."
			print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			return False
		else:
			return True

	except sqlite3.Error as e:
		print_statusline(f"")
		modname = f"Database query error {e} \n   I cannot execute properly. Exiting."
		print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
		return False
	except Exception as e:
		print_statusline(f"")
		modname = f"An unexpected error occurred: {e}\n   I cannot execute properly. Exiting."
		print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
		return False
	finally:
		if cur:
			cur.close()
		if conn:
			conn.close()

#------------------------------------------------------------
def make_intextdb():
	#global cybelecode, midbcounter
	global midbcounter, ncountries, constellations_dict
	if not check_tables(tables):
		sys.exit(0)
	else:
		print_statusline(f"Handling databases ...")
		#cybelecode = fetch_fromdbfile("cybele.db", "config", "code")
		astronomy_glossary = fetch_fromdbfile("cybele.db", "astronomy_glossary", "glossary")
		star_names = list(fetch_fromdbfile("cybele.db", "stars", "star_name"))
		hr_numbers = list(fetch_fromdbfile("cybele.db", "stars", "hr_number"))
		constelations = list(fetch_fromdbfile("cybele.db", "stars", "constelation"))
		for name, hr, const in zip(star_names, hr_numbers, constelations):
			stars_dict[name] = [hr, const]
			
		constelation = list(fetch_fromdbfile("cybele.db", "constelations", "constelation"))
		meaning = list(fetch_fromdbfile("cybele.db", "constelations", "meaning"))
		abbr = list(fetch_fromdbfile("cybele.db", "constelations", "abbr"))
		for constelation, meaning, abbr in zip(constelation, meaning, abbr):
			constellations_dict[constelation] = meaning, abbr
			constellations_abbr[abbr] = constelation
			
		db_country = list(fetch_fromdbfile("cybele.db", "countries", "country"))
		db_capital = list(fetch_fromdbfile("cybele.db", "countries", "capital"))
		db_population = list(fetch_fromdbfile("cybele.db", "countries", "population"))
		ncountries = {
			country.lower(): {"capital": capital, "population": population}
			for country, capital, population in zip(db_country, db_capital, db_population)
		}
			
		ldclimatdictterm = list(fetch_fromdbfile("cybele.db", "climate_dict", "climate_term"))
		ldclimatdictdesig = list(fetch_fromdbfile("cybele.db", "climate_dict", "designation"))
		climate_dictionary = {ldclimatdictterm[i]: ldclimatdictdesig[i] for i in range(len(ldclimatdictterm))}
		meaning_term = fetch_fromdbfile("cybele.db", "meanings", "term")
		qa_astro = fetch_fromdbfile("cybele.db", "qa_astro", "question")
		cmd_names = fetch_fromdbfile("cybele.db", "linux_commands", "cmd_name")
		syntaxes = fetch_fromdbfile("cybele.db", "linux_commands", "syntax")
		explanations = fetch_fromdbfile("cybele.db", "linux_commands", "explanation")
		examples_str_list = fetch_fromdbfile("cybele.db", "linux_commands", "examples")

		for i in range(len(cmd_names)):
			if cmd_names[i] not in [key[5:] for key in help.keys()]:
				cmd_name = cmd_names[i]
				syntax = syntaxes[i]
				explanation = explanations[i]
				examples = examples_str_list[i].split(';') if examples_str_list[i] else []
				linux_commands[cmd_name] = {
					"syntax": syntax,
					"explanation": explanation,
					"examples": examples
				}
				
		old_tech_terms_list = fetch_fromdbfile("cybele.db", "oldtech", "oldterm")

		core["astronomy glossary"] = list(astronomy_glossary)
		core["star name"] = [key.lower() for key in stars_dict.keys()]
		core["constelattion"] = list(constellations_dict.keys())
		core["asteroid"] = list(asteroids_list.keys())
		core['country'] = list(ncountries.keys())
		core['capital'] = [country["capital"] for country in ncountries.values()]
		core["climate dictionary term"] = list(climate_dictionary.keys())
		core["climate dictionary"] = list(climate_dictionary.values())
		core["word meaning"] = list(meaning_term)
		core["qa-astro"] = list(qa_astro)
		core['help'] = list(help.keys())
		core["linuxcmd"] = list(linux_commands)
		core["element symbol"] = [key.lower() for key in periodic_elements.keys()]
		core["element abbr"] = [key.lower() for key in periodic_abbr.keys()]
		core["old_tech_term"] = old_tech_terms_list
		
		internal_db_array = ["astronomy glossary","star name","constelattion","asteroid","country","capital",
							"climate dictionary term","climate dictionary","word meaning","qa-astro","help",
							"linuxcmd","element symbol","element abbr","old_tech_term"]

		for i in range(len(internal_db_array)):
			 midbcounter = midbcounter + (len(core[internal_db_array[i]]))

#----------------------------------------------------------------------
questions = [
	"Ola",
	"Como te chamas?",
	"Hello",
	"What is your name?",
	"What is the meaning of your name?",
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
	"The name Cybele essentially means 'Great Mother of the Gods' or 'Mother Goddess,' signifying her role as a powerful deity of the earth, nature, with some interpretations also linking her to the wisdom of a 'Prophet.'",
	"The exact builders of the pyramids are still debated...",
	"The current time in the system clock is "+datetime.now().strftime("%H:%M"),
	"The current time is "+datetime.now().strftime("%H:%M"),
	"Today is " + days[weekdaydate] + " and currently is "+datetime.now().strftime("%d")+" of "+month_name+" from "+datetime.now().strftime("%Y"),
	"Unlike LLMs who can't, my core functionality can be replicated, but my responses may vary based on training data.",
	"An electromagnetic wave produced by the oscillation of electricity in a conductor (as a radio antenna) and of a length ranging from a few millimeters to many kilometers. There is 7 types of waves are as follows: Radio Waves, Microwaves, InfraRED, Visible, Ultraviolet, X-Ray, Gamma Rays. \nRadio waves have the longest wavelength and small frequency while the gamma rays have shortest wavelength and high frequency.",
	"The numbers are in decimal degrees format and range are from -90 to 90 for latitude using + for North and - for South and -180 to 180 for longitude using + for East and - for West.",
	"Latitudes are horizontal lines that measure distance north or south of the equator. Longitudes are vertical lines that measure east or west of the meridian in GREENwich, England. Together, latitude and longitude enable cartographers, geographers and others to locate points or places on the globe.",
	"If you're using a map with longitude and latitude lines, stick a pin where you're located. Then, draw a straight horizontal line from your point to the east or west edge of the map. Then, draw a vertical line from your location to the north or south edge of the map. Put together the 2 coordinates to find your position.",
	"Yes. At this time and with my core code i can be 100% offline resourceful.",
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
	"days till/days to <christmas/new years eve>","sunset time","sunrise time","how many questions can you anwser","diagnostics",
	"date","time","convert <n> days","convert <n> days in/to <minutes/hours/days","do you know anything about",
	"week","outdated words","what number is this week","show core","what century are we in","century","view askard <id>",
	"show askard <id>","list askard <id start> to <id end>","achk askard <id>","leap year","make a sentence","make a phrase",
	"people in space","do you speak","tvshows is he watching","your fav tvshows","seek <topic>","find <topic>","infostar <star name>",
	"sharing about","sharing links","is this year a leap year","show me asteroids names","show me constellations","show me all constellations",
	"show me old tech words","show me old tech terms","show me star names","show me meaning terms","show me meaning words","show me linux commands"
	"math game","reset my score","show my score","morse <word/phrase>","demorse <word/phrase>","when was vorian created",
	"play game constelattions","play game capitals","when did vorian went online","difference from <date>"
]
#----------------------------------------------------------
maincommands = [
	"bye","exit","quit","do you know anything about","know anything on","find","seek","what can i ask you","how many linux commands you know",
	"what can you anwser","what do you know","what can you do","what do you do","what you can do","adelino quote","what is",
	"do you know what is","meaning of","show me","tell me","list me","meaning term","meaning words","meaning terms","constellations",
	"show me some linux commands","astronomy questions","questions of astronomy","days till","days for","days to","trails",
	"difference from","age calc","what do you know about","astronomy","asteroid","constelations","universe","can you","vorian created",
	"visualize periodic table","show periodic table","distance from","orbit","planets of the solar system","planets of solar system",
	"solar system planets order","solar system planets","types of orbits","orbital regimes","year seasons","seasons of the year",
	"set default gps","capital","capital of","value of pi","pi value","pi","s.o","operating system","system","can you help me",
	"can you help","help","help me","time","what time it is","clock time","happy birthday cybele","cybele happy birthday","happy birthday",
	"merry christmas","i wish you a merry christmas","happy valentines","happy valentines","happy new year","what is your version",
	"#version","convert gps to distance","gps to distance","harvesine","harvesine formula","sunset time","sunrise time","set default gps",
	"diagnostics","show core","#core","date","today","today is","what day is today","what is the date","what is today","convert",
	"how many weeks have a year","year weeks","week","week number","what number is this week","what is this week number","last update",
	"yes","search askard","view askard","list askard","search astronomy","search oldtech","list oldtech","first last","limits",
	"current century","population","where is the iss","where is zarya","people in space","what is he watching","what are you watching",
	"fav tvshows","favorite tvshows","do you speak","do you talk","say something","make a sentence","play capitals","play countries",
	"play math","play constellations","play elements","game capitals","game countries","game math","game constellations","game elements",
	"show my score","reset my score","reset score","infostar","today activity","weather","about you","presence","presence services",
	"presence online","phonetic","morse","demorse","yoda say","genpwd","multiplication table","x table","licence","cybele licence",
	"when vorian was created","vorian created","when vorian went online","cybele uptime","stars from","list stars","list constellations"
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

#----------------------------------------------------------------------
old_tech_terms_list = fetch_fromdbfile("cybele.db", "oldtech", "oldterm")
core["old_tech_term"] = old_tech_terms_list

#----------------------------------------------------------------------
if _cybid_ == True:
	help.update({"help list extcom": "Usage: <list extcom or extcom> \nDisplays all the commands the Cybele extention can provide.\nex: list extcom\n    extcom\n"})
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
		if query.lower() in kdecode(text.lower(), shift):
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
		if str(qt):
			return qt.lower()
	except ValueError:
		return qt.lower()
	return qt.lower()

def find_answer(question,whatlist):
	pontuation = [".",",","!","?"]
	outoptions = ["Perhaps you meant: ","It looks like you might have meant: ","Is this what you had in mind: ","Oops! Did you mean: ","Looking for: "]
	for p in range(len(pontuation)):
		question = question.replace(pontuation[p],"")
	for index, value in enumerate(whatlist):
		if question.lower() == value.lower() or question.lower() == value.lower().replace("?",""):
			return answers[index]+"\n"
	sayhi = core.get("greatings", [])
	dict_climate = core.get("climate dictionary", [])
	dict_astro_keys = ["astronomy glossary", "constelattion", "planet", "qa-astro", "primary moon phase", "secondary moon phase"]
	dict_astro = [item for key in dict_astro_keys if key in core for item in core[key]]
	others_keys = ["country", "capital", "months", "seasons", "old_tech_term", "word meaning", "help", "share", "linuxcmd"]
	others = [item for key in others_keys if key in core for item in core[key]]
	alldict = others + questions + sayhi + dict_climate + dict_astro + maincommands 
	is_correct, suggestions = spell_check(question, alldict)
	if suggestions:
		output_string = random.choice(outoptions)
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
def pwdgen(num_passwords, length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for i in range(length))
        passwords.append(password)
    return passwords

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

#------------------------------------------------------------
def get_uptime():
	current_time = datetime.now()
	time_difference: timedelta = current_time - start_time 
	total_seconds = time_difference.total_seconds()
	hours = int(total_seconds // 3600)
	minutes = int((total_seconds % 3600) // 60)
	seconds = int(total_seconds % 60)
	return (hours,minutes,seconds)
	
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
				db_file ='cybele.db';table = 'meanings';search_val = word
				search_col = 'term';fetch_col = 'designation'
				dbsearch = dbfetch(db_file, search_val, table, search_col, fetch_col)
				if "{min_age}" in dbsearch or "{max_age}" in dbsearch:
					current_year = date.today().year
					calculated_min_age = current_year - 1980
					calculated_max_age = current_year - 1965
					final_answer = dbsearch.format(min_age=calculated_min_age, max_age=calculated_max_age)
					print('%s\n' % (final_answer))
				else:
					print('%s\n' % (dbsearch))
				
			elif list_name == 'qa-astro':
				db_file ='cybele.db';table = 'qa_astro';search_val = word
				search_col = 'question';fetch_col = 'awnser'
				dbsearch = dbfetch(db_file, search_val, table, search_col, fetch_col)
				print( '%s\n' % (dbsearch))

			elif list_name == 'linuxcmd':		
				print ("<"+word.lower()+">" + " is a console " + _spchar_[16:17] + " linux command. Here some help about'it:\n")
				print (" "*5+"Syntax: " + str(linux_commands[word]['syntax']))
				print ("Explanation: " + str(linux_commands[word]['explanation']))
				print (" "*3+"Examples: " + "'" + "', '".join(linux_commands[word]['examples']) + "'")
				print ("")

			elif list_name == 'linuxexcmd':
				print ("exemplo....")

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
				db_file ='cybele.db';table = 'oldtech';search_val = word
				search_col = 'oldterm';fetch_col = 'designation'
				dbsearch = dbfetch(db_file, search_val, table, search_col, fetch_col)
				
				random.shuffle(messages['creative matter'])
				canswers = random.choice(messages['creative matter'])
				creative_random_anwser = canswers
				print(str(creative_random_anwser + "\n%s \n") % (word.capitalize(), list_name.replace("_"," ").title(), dbsearch))

			elif list_name == "climate dictionary term":
				climate_anwser = climate_dictionary[word]
				print("The term "+ word.capitalize() + " belongs to the " + list_name.title()[0:18] + ":\n" + climate_anwser + "\n")

			elif list_name == 'astronomy glossary':
				db_file ='cybele.db';table = 'astronomy_glossary';search_val = word
				search_col = 'glossary';fetch_col = 'designation'
				dbsearch = dbfetch(db_file, search_val, table, search_col, fetch_col)
				
				astro_anwser = dbsearch
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
				print (word.capitalize() + " have the designation of '" + constellation_anwser[0] + "' and the abreviation '" + constellation_anwser[1] + "'.\n")

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
				print ("Belongs to '" + star_constellation + "' constellation and have the designation of '" + star_info[0] + "'.\n")

			elif list_name == "year event":
				random.shuffle(messages['year_event_msg'])
				print ( random.choice(messages['year_event_msg']) % (word.capitalize()))

			elif list_name == "help":
				print (help[word])

			else:
				print ("To me that is a %s.\n" % (list_name).replace("_"," "))
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
		print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} What?!\n")
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
			try:
				datetime.strptime(event, "%d.%m.%Y")
			except ValueError:
				pass
			try:
				datetime.strptime(event, "%d/%m/%Y")
			except ValueError:
				pass
			try:
				datetime.strptime(event, "%d-%m-%Y")
			except ValueError:
				pass
			days_left = 0
		userdate = date(year=int(event[6:]), month=int(event[3:5]), day=int(event[0:2]))
		days_left = days_until(userdate)
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
def get_thepopulation(country_name):
	country_slug = "us" if country_name.lower() == "united states" else country_name.lower().replace(" ", "-")
	url = f"https://www.worldometers.info/world-population/{country_slug}-population/"
	try:
		response = requests.get(url, timeout=10)
		response.raise_for_status()
		soup = BeautifulSoup(response.content, 'html.parser')

		google_chart_div = soup.find('google-chart')
		if not google_chart_div or 'data-rows' not in google_chart_div.attrs:
			dynamic_counter_div = soup.find('div', class_='font-bold text-4xl md:text-6xl text-center text-zinc-500')
			if dynamic_counter_div:
				span_text = dynamic_counter_div.find('span', class_='rts-counter')
				if span_text and "retrieving data" in span_text.text.lower():
					print (random.choice(messages['trouble_msg']) + " The live population for %s requires dynamic scraping.\n" % country_name)
			print (random.choice(messages['trouble_msg']) + " Could not find static population data for %s on the page.\n" % country_name)
			return None

		unescaped_data_rows = html.unescape(google_chart_div['data-rows'])
		data_list = json.loads(unescaped_data_rows)
		if not data_list:
			print (random.choice(messages['trouble_msg']) + " No population data found within the chart for %s..\n" % country_name)
			return None
		population = data_list[-1][1]
		return population
	except Exception as e:
		print (random.choice(messages['trouble_msg']) + " An error occurred while attempting to retrieve population for %s..\n" % country_name)
		return None

#-------------------------------------------------
def extract_from_vorian():
	import bs4
	import urllib.request
	from bs4 import BeautifulSoup
	url = website['tvshow']
	try:
		response = urllib.request.urlopen(url)
		html_content = response.read()
		html_string = html_content.decode("utf-8")
		soup = BeautifulSoup(html_string, 'html.parser')
		tv_shows = soup.find_all('li', class_='zfr3Q TYR86d eD0Rn')
		tv_show_list = []
		for show in tv_shows:
			title_element = show.find('span', class_='C9DxTc')
			if title_element:
				tv_show_list.append(title_element.text.strip())
		for i in range(12, len(tv_show_list)):
			print (tv_show_list[i])
	except urllib.error.URLError as e:
		print(f"{random.choice(messages['trouble_msg'])} Error fetching the page: {e}\n")
	except Exception as e:
		print(f"{random.choice(messages['trouble_msg'])} An unexpected error occurred: {e}")
		
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

#--------------------------------------------------
def multiplication_table(num):
	try:
		if num == 0 or num == '':
			return True
		else:
			print ("")
			for i in range(1, 11):
				print("  %d x %d = %d" % (num, i, num * i))
			print ("")
	except Exception:
		return True

#---------------------------------------------------------------------------------------------
def cybele_play_quiz(quizdata,game):

	gamescore[0] = 0
	gamescore[2] = 0
	getout = ['stop','quit']
	extquiz = ['Country','Capital','Constellation','Abbreviation','Periodic Table Elements','Symbol']
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

	print ("\nType [quit] if you want to quit.")
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

#-------------------------------------------------------------------
def random_season_activity():
	now = date.today()
	month = now.month

	if 3 <= month <= 5:  # Spring (March, April, May)
		season = "spring"
	elif 6 <= month <= 8:  # Summer (June, July, August)
		season = "summer"
	elif 9 <= month <= 11: # Autumn (September, October, November)
		season = "autumn"
	else:  # Winter (December, January, February)
		season = "winter"

	conn = None
	try:
		if internet_onoff():
			conn = sqlitecloud.connect("sqlitecloud://cxuomo3ahz.g1.sqlite.cloud:8860/cybele.sqlite?apikey=9o4zGGVvXKMu74P2OzDhrotTOBp9GCGQ2a0VotuCMms")
		else:
			db_filename = "cybele.db"
			if os.path.isfile(db_filename):
				conn = sqlite3.connect(db_filename)
			else:
				modname = "The " + db_filename.upper() + " database file is missing, and with no internet, the online database is inaccessible. \n    I cannot execute properly. Exiting."
				print(f"\n\033[1;31m {_spchar_[1:2]} {_title_}\033[0;0m: {modname}")
				sys.exit(0)

		cursor = conn.cursor()
		cursor.execute(f"SELECT {season} FROM season_activities ORDER BY RANDOM() LIMIT 1")
		result = cursor.fetchone()

		if result:
			activities_str = result[0]
			if activities_str is not None:
				activities = [activity.strip() for activity in activities_str.split(',')]
				
				activitie = "\n " + _spchar_[17:18] + " It's " + season.capitalize() + ", " + random.choice(activities) + ".\n"
				print(activitie)
			else:
				print(f"No activities found for {season} in the database (or the value is NULL).")
		else:
			return f"No activities found for {season} in the database."

	except sqlite3.OperationalError as e:
		if "no such table" in str(e).lower():
			print(f"{random.choice(messages['trouble_msg'])} Database operational error: {e}. This option is not available.")
	except sqlite3.Error as e:
		print(f"{random.choice(messages['trouble_msg'])} Database incompatibility. This option is not available. \nDetails: {e}")
	finally:
		if conn:
			conn.close()

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

#-------------------------------------------------
#-------------------------------------------------
def mandb(dbname,dbtable,dbtask,dbbegin,dbend):

	if internet_onoff() == True:
		conn = sqlitecloud.connect("sqlitecloud://cxuomo3ahz.g1.sqlite.cloud:8860/"+dbname+".sqlite?apikey=9o4zGGVvXKMu74P2OzDhrotTOBp9GCGQ2a0VotuCMms")
	else:
		db_filename = dbname + ".db"
		if os.path.isfile (db_filename) == True:
			conn = sqlite3.connect(db_filename)
		else:
			modname = "The " + db_filename.upper() + " database file is missing, and with no internet, the online database is inaccessible. \n   I cannot execute properly. Exiting."
			print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			sys.exit(0)
	
	zdb = []
	filter = ""

	if dbtask == 'search':
		if dbname == 'askardb':
			filter = "SELECT ask_id, askard FROM askard_db WHERE askard LIKE '%"+str(dbend)+"%'"
			nchar = _spchar_[9:10]
		elif dbname == 'cybele' and dbtable == 'astronomy_glossary':
			filter = "SELECT glossary, designation FROM astronomy_glossary WHERE designation LIKE '%"+str(dbend)+"%'"
			nchar = _spchar_[0:1]
			dbname = 'astronomy glossary'
		elif dbname == 'cybele'and dbtable == 'oldtech':
			filter = "SELECT oldterm, designation FROM oldtech WHERE designation LIKE '%"+str(dbend)+"%'"
			nchar = _spchar_[7:8]
			dbname = 'old tech'
		else:
			print ('Well done ' + _auth1r_ +'!. The code has a error. Fix it, you morone!')
		
		cursor = conn.execute(filter)
		results = cursor.fetchall()
		if results:
			print (f'There are {len(results)} {nchar} {dbname} that contain the substring {_spchar_[2:3]}{dbend}{_spchar_[3:4]}. They are the:\n')
			if len(results) > 50:
				items_per_line = 10
			else:
				items_per_line = 5
			for i in range(0, len(results), items_per_line):
				line = results[i:i + items_per_line]
				output_line = [str(row[0]) for row in line]
				print(", ".join(output_line))
		else:
			print (f'No {nchar} {dbname} that contain the substring {_spchar_[2:3]}{dbend}{_spchar_[3:4]}.')
				
	if dbtask == 'view':
		cursor = None
		if dbname == 'askardb':
			filter = "SELECT ask_id="+str(dbbegin)+", askard from askard_db"
		elif dbname == 'cybele':
			if dbtable == 'funfacts':
				filter = "SELECT * FROM funfacts ORDER BY RANDOM() LIMIT 1;"
			elif dbtable == 'nicethings':	
				filter = "SELECT * FROM nicethings ORDER BY RANDOM() LIMIT 1;"
			else:
				print ("option view none of dbtables with conditions... Fix'it")
		
		if dbname == 'askardb':
			conn = sqlite3.connect(dbname + ".db")
			cursor = conn.execute(filter)
			for row in cursor:
				if row[0] == 1:
					zdb.append (dbbegin)
					zdb.append (row[1])		
			if len(zdb) > 0:
				print(f"\n > {zdb[1]}")
			else:
				print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} The database query results return empty!!\n")
		
		elif dbname == 'cybele':
			cursor = conn.execute(filter)
			if dbtable == 'funfacts':
				nchar = _spchar_[13:14]
			elif dbtable == 'nicethings':	
				nchar = _spchar_[14:15]
			if cursor:
				row = cursor.fetchone()
				if row:
					print(f"\n {nchar} {str(row[0])}\n")
				else:
					print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} The database query results return empty!!\n")
		
	if dbtask == 'list':
		if dbname == 'askardb':
			if dbbegin == 0 and dbend == 0:
				nfilter = "SELECT * from askard_db"
			else:
				nfilter = "SELECT ask_id, askard FROM askard_db WHERE ask_id BETWEEN " + str(dbbegin) + " and "+ str(dbend) + " ORDER BY ask_id;"	
		elif dbname == 'cybele' and dbtable == 'oldtech':
			if dbbegin == 0 and dbend == 0:
				nfilter = "SELECT * from oldtech"
			else:
				nfilter = "SELECT oldterm, designation FROM oldtech WHERE oldterm BETWEEN '" + str(dbbegin) + "' and '"+ str(dbend) + "' ORDER BY oldterm;"
		elif dbname == 'cybele' and dbtable == 'stars':
			if dbbegin != 0 and dbend == 0:
				nfilter = "SELECT star_name,hr_number FROM stars WHERE constelation = '" + str(dbbegin) + "';"
			else:
				nfilter = "SELECT star_name,hr_number FROM stars WHERE star_name BETWEEN '" + str(dbbegin).title() + "' and '"+ str(dbend).title() + "' ORDER BY star_name;"		
		elif dbname == 'cybele' and dbtable == 'constelations':
			if dbbegin == 0 and dbend == 0:
				nfilter = "SELECT * from constelations"
			else:
				nfilter = "SELECT constelation, meaning FROM constelations WHERE constelation BETWEEN '" + str(dbbegin) + "' and '"+ str(dbend) + "' ORDER BY constelation;"
		print ("")
		
		filter = nfilter
		cursor = conn.execute(filter)
		rows_found = False
		for row in cursor:
			rows_found = True
			print(" ", row[0], " > ", row[1])
		if not rows_found:
			print (f"{random.choice(messages['trouble_short'])} No results found! Redefine your search criteria.\n")
		else:
			print("")
		
	if dbtask == 'limits':	
		if dbname == 'askardb':
			filter = "SELECT min(ask_id) , max(ask_id) FROM askard_db"
			titvar = "askard ID"
		elif dbname == 'cybele' and dbtable == 'astronomy_glossary':
			filter = "SELECT min(glossary) , max(glossary) FROM astronomy_glossary"
			titvar = "astronomy glossary term"
		elif dbname == 'cybele' and dbtable == 'oldtech':
			filter = "SELECT min(oldterm) , max(oldterm) FROM oldtech"
			titvar = "old tech terminology" 
		cursor = conn.execute(filter)
		for row in cursor:
			print ("The first "+ titvar +" in the database file is '" + str(row[0]) + "' and the last is '" + str(row[1]) + "'.\n")
	conn.close()

#-------------------------------------------------
def get_cmdlinux(command_name):
    
	conn = None
	try:
		conn = sqlite3.connect('cybele.db')
		cursor = conn.cursor()
		query = "SELECT cmd_name, syntax, explanation, examples FROM linux_commands WHERE cmd_name = ?"
		cursor.execute(query, (command_name,))
		row = cursor.fetchone()
		if row:
			cmd_name, syntax, explanation, examples_str = row

			# Convert the examples string back into a list if it was stored as '; '-separated values
			examples_list = examples_str.split('; ') if examples_str else []

			return {
				"cmd_name": cmd_name,
				"syntax": syntax,
				"explanation": explanation,
				"examples": examples_list
			}
		else:
			return None

	except sqlite3.Error as e:
		print(f"Database error: {e}")
		return None
	finally:
		if conn:
			conn.close()
			
#-------------------------------------------------
def chkpy():
	print_statusline(f"")
	major = sys.version_info.major
	minor = sys.version_info.minor
	if minor > 13:
		modname = f"With this higher Python version you only can work localy. Download the databases. \n   I cannot execute properly. Exiting."
	else:
		modname = f"Python {major}.{minor} is too old. Required version 3.10 or higher.\n   I cannot execute properly. Exiting."
	if major < 3 or major == 3 and minor < 10 or minor > 12:
		print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
		return False
	return True	

#-------------------------------------------------
def kdecode(emessage, shift):
    dek_msg = ""
    for char in emessage:
        if char.isalpha():
            if char.isupper():
                k_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                k_char = chr((ord(char) - shift - 97) % 26 + 97)
            dek_msg += k_char
        else:
            dek_msg += char
    return dek_msg

#-------------------------------------------------
def ksha(files, chunk_size=4096):
	results = []
	if not isinstance(files, list):
		print(f"{random.choice(messages['trouble_msg'])} Internal error. The data is not a tuple! -'{type(files)}'\n")	
	for file_path in files:
		sha1_hash = None
		if not os.path.exists(file_path):
			print(f"{random.choice(messages['trouble_msg'])} File not found at '{file_path}'\n")
		elif not os.path.isfile(file_path):
			print(f"{random.choice(messages['trouble_msg'])} '{file_path}' is not a file.\n")
		else:
			try:
				hasher = hashlib.sha1()
				with open(file_path, 'rb') as f:
					while True:
						chunk = f.read(chunk_size)
						if not chunk:
							break
						hasher.update(chunk)
				sha1_hash = hasher.hexdigest()
			except IOError as e:
				print(f"{random.choice(messages['trouble_msg'])} Error reading file '{file_path}': {e}\n")
			except Exception as e:
				print(f"{random.choice(messages['trouble_msg'])} An unexpected error occurred: {e}\n")
		results.append((file_path, sha1_hash))
	return tuple(results)
	
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
def country_holidays():
	os_country_2l = locale.getlocale()[0].split('_')[-1].title()
	country = pycountry.countries.get(name=os_country_2l)	
	if country:
		print(f"\nDetected country: {country.name} ({country.alpha_2})")
		country_code_for_holidays = country.alpha_2
	else:
		print(f"{random.choice(messages['trouble_short'])} No valid country detected or two-letter country code.\n")
		return

	holidays_country_year = datetime.now().year
	try:
		country_holidays = holidays.country_holidays(country_code_for_holidays, years=holidays_country_year)
		if country_holidays:
			print(f"Holidays for {country.name} ({country.alpha_2}) in the year {holidays_country_year}:\n")
			sorted_holidays = sorted(country_holidays.items())
			for date, name in sorted_holidays:
				print(f"  {date} | {name}")
		else:
			print(f"No holidays found for {country.name} ({country.alpha_2}) in {holidays_country_year}.")
	except NotImplementedError:
		print(f"{random.choice(['Oops!', 'Sorry!', 'Heads up!'])} The holidays does not have data for {country.name} ({country.alpha_2}).")
	except KeyError:
		print(f"{random.choice(['Oops!', 'Sorry!', 'Heads up!'])} An issue occurred with the country code {country.alpha_2} when fetching holidays.")
	except Exception as e:
		print(f"{random.choice(messages['trouble_short'])} Unexpected error {e}")
	print("")
	
#----------------------------------------------------------------
#----------------------------------------------------------------
def set_cursor_pos(row, col):
    return f"\033[{row};{col}H"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_firework_explosion(x, y, max_radius, characters):
 
    try:
        canvas_width, canvas_height = os.get_terminal_size()
    except OSError:
        canvas_width, canvas_height = 80, 24 # Fallback if size cannot be determined

    explosion_color = random.choice([k for k in kolor.keys() if k != 'OFF']) # Pick a random color, not 'OFF'

    for radius in range(1, max_radius + 1):
        # Create a temporary canvas for this frame of the explosion
        # This allows us to build the frame and then print it efficiently
        frame_canvas = [[' ' for _ in range(canvas_width)] for _ in range(canvas_height)]

        # Populate the frame_canvas with explosion particles for the current radius
        for i in range(canvas_height):
            for j in range(canvas_width):
                # Calculate distance from the explosion center
                dist = ((j - x)**2 + (i - y)**2)**0.5
                # Draw particles within the current radius ring
                if radius - 1 <= dist < radius:
                    if 0 <= i < canvas_height and 0 <= j < canvas_width:
                        frame_canvas[i][j] = random.choice(characters)

        clear_screen()

        # Print the current frame of the explosion
        for row_idx, row_chars in enumerate(frame_canvas):
            # Move cursor to the start of this row before printing
            print(f"{set_cursor_pos(row_idx + 1, 1)}{kolor[explosion_color]}{''.join(row_chars)}{kolor['OFF']}", end="")
        
        # Flush output to ensure frame is displayed immediately
        import sys
        sys.stdout.flush()
        sleep(0.08) # Speed of the explosion expansion

def main_fireworks(num_fireworks=5, delay_between_fireworks=1.5):
	kolor = {
		'RED': "\033[91m",
		'GREEN': "\033[92m",
		'YELLOW': "\033[93m",
		'BLUE': "\033[94m",
		'MAGENTA': "\033[95m",
		'CYAN': "\033[96m",
		'WHITE': "\033[97m",
		'DARK_YELLOW': "\033[33m",
		'OFF': "\033[0m",
	}

	CLEAR_SCREEN = "\033[2J"
	HOME_CURSOR = "\033[H"
	HIDE_CURSOR = "\033[?25l"
	SHOW_CURSOR = "\033[?25h"

	explosion_chars = ['*', '+', 'o', '.', '@', '#', '!', '^']
    
	try:
		term_width, term_height = os.get_terminal_size()
	except OSError:
		term_width, term_height = 80, 24

	print(f"Prepare for the ASCII fireworks show!{kolor['OFF']}")
	print(HIDE_CURSOR, end="")
	sleep(2.0)
	clear_screen()

	try:
		for _ in range(num_fireworks):
			# Random starting position for the firework (rocket path)
			# Ensure rocket starts near the bottom
			start_x = random.randint(int(term_width * 0.1), int(term_width * 0.9))
			start_y = term_height - 2 # Start 2 rows from the bottom

			# Random explosion height for this firework
			explosion_y = random.randint(int(term_height * 0.2), int(term_height * 0.6)) # Explode in upper-middle
            
			# Simulate rocket ascent
			random_color = random.choice([k for k in kolor.keys() if k != 'OFF'])
			rocket_char = '↟'

			for y_coord in range(start_y, explosion_y, -1):
				clear_screen() # Clear screen for each rocket frame
				# Draw the rocket at its current position
				# Row is y_coord, Column is start_x
				print(f"{set_cursor_pos(y_coord, start_x)}{kolor[random_color]}{rocket_char}{kolor['OFF']}", end="")
				import sys
				sys.stdout.flush() # Ensure rocket is drawn immediately
				sleep(0.08) # Speed of the rocket ascent

			# Clear the rocket after ascent
			clear_screen()

			# Explosion!
			max_explosion_radius = random.randint(min(8, term_height // 4), min(15, term_height // 2))
			create_firework_explosion(start_x, explosion_y, max_explosion_radius, explosion_chars)
			print(kolor['OFF'], end="") 
			sleep(delay_between_fireworks)
			clear_screen()

	except KeyboardInterrupt:
		pass 

	finally:
		print(kolor['OFF'])
		clear_screen()
		print(f"{HOME_CURSOR}ASCII Fireworks show ended! Hope you enjoyed the retro vibe! {SHOW_CURSOR}\n")

#----------------------------------------------------------------
#----------------------------------------------------------------
def draw_christmas_tree():
	
	tree = [
	[32,32,32,32,32,32,42,32,32,32,32,32,32,32,32,32,32,32,32,32,44,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,95,47,94,92,95,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,62,9,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,47,46,45,46,92,32,32,32,32,32,32,32,32,32,42,32,32,32,32,32,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,42,32,32,32,32,32,32,32,32,96,47,38,92,96,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,42,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,44,64,46,42,59,64,44,9,9,9,9,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,47,95,111,46,73,32,37,95,92,32,32,32,32,42,9,9,32,32,32,32,32,32,32,32],
	[32,32,32,42,32,32,32,32,32,32,32,32,32,32,32,40,96,39,45,45,58,111,40,95,64,59,9,9,9,9,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,32,32,47,96,59,45,45,46,44,95,95,32,96,39,41,32,32,32,32,32,32,32,32,32,32,32,32,42,32,32,32],
	[32,32,32,32,32,32,32,42,32,32,32,32,40,96,39,45,45,41,95,64,32,59,111,32,37,39,40,41,92,32,32,32,32,32,32,42,9,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,47,96,59,45,45,46,95,96,39,39,45,45,46,95,79,39,64,59,9,9,9,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,47,38,42,44,40,41,126,111,96,59,45,46,44,95,32,96,34,34,96,41,9,9,32,32,32,32],
	[42,32,32,32,32,32,32,32,32,32,32,47,96,44,64,32,59,43,38,32,40,41,32,111,42,96,59,45,39,59,92,9,9,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,40,96,34,34,45,45,46,44,95,48,32,43,37,32,64,39,32,38,40,41,92,9,9,32,32,32],
	[32,32,32,32,32,32,32,32,32,47,45,46,44,95,32,32,32,32,96,96,39,39,45,45,46,46,46,46,45,39,96,41,32,32,42,9,32,32,32,32],
	[32,32,32,32,32,42,32,32,32,47,64,37,59,111,96,58,59,39,45,45,44,46,95,95,32,32,32,95,95,46,39,92,9,32,32,32,32,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,59,42,44,38,40,41,59,32,64,32,37,32,38,94,59,126,96,42,96,111,59,64,40,41,59,32,32,32,32,32,42,32,32,32],
	[32,32,32,32,32,32,32,32,32,47,40,41,59,32,111,94,126,59,32,38,32,40,41,46,111,64,42,38,96,59,38,37,79,92,9,9,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,33,96,33,61,33,61,61,33,33,61,61,44,44,44,46,44,61,33,61,61,33,61,61,61,33,96,9,32,32,32],
	[32,32,32,32,32,95,95,46,45,45,45,45,45,46,40,92,45,39,39,35,35,35,35,35,45,45,45,46,46,46,95,95,95,46,46,46,45,45,45,45,46,32],
	[32,32,32,32,39,96,32,32,32,32,32,32,32,32,32,92,41,95,96,35,35,35,35,35,96,9,9,9,32,32,32,32,32,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,46,45,45,39,32,39,41,9,9,9,9,9,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,111,40,32,32,41,95,45,92,9,9,9,9,9,9,32,32,32],
	[32,32,32,32,32,32,32,32,32,32,32,32,96,34,34,32,96,32,96,9,9,9,9,9,9]
]
	#tree_width = len(tree)
	#terminal_width = 80
	#left_padding = (terminal_width - tree_width) // 2
	randomcolor = ['RED','DARK_YELLOW','GREEN','BLUE','CYAN','MAGENTA']
	for i in range(len(tree)):
		res = ''.join(map(chr, tree[i]))
		if i <= 4:
			artcor = kolor['YELLOW']
		elif i >= 19:
			artcor = kolor['WHITE']
		else:
			artcor = kolor[random.choice(randomcolor)]
		print (f"{" "*5} {artcor} {str(res)}")

	merry_christmas_message = (
		kolor['RED'] + "  MERRY" +
		kolor['GREEN'] + " CHRISTMAS!" +
		kolor['OFF']
	)
	print(" "*27 + merry_christmas_message)
	

#-------------------------------------------------
#-------------------------------------------------
def ascii_horiz_solar_system(width):
	if width < 60:
		print (f"{random.choice(messages['trouble_short'])} Width is very small. Output might be distorted.\n")
		width = 60 

	COLOR_RESET = "\033[0m"
	COLOR_YELLOW = "\033[33m"  # Sun
	COLOR_GRAY = "\033[37m"    # Mercury, Path
	COLOR_ORANGE = "\033[38;5;208m" # Venus (a more specific orange)
	COLOR_BLUE = "\033[34m"    # Earth
	COLOR_RED = "\033[31m"     # Mars
	COLOR_LIGHT_BROWN = "\033[38;5;94m" # Jupiter (lighter brown)
	COLOR_BROWN = "\033[38;5;130m" # Saturn
	COLOR_CYAN = "\033[36m"    # Uranus
	COLOR_DARK_BLUE = "\033[38;5;20m" # Neptune (darker blue)

	solar_line_chars = [' ' for _ in range(width)]
	solar_line_colors = ['' for _ in range(width)]
	
	sun_pos_frac = 0.02
	mercury_pos_frac = 0.10
	venus_pos_frac = 0.18
	earth_pos_frac = 0.28
	mars_pos_frac = 0.36
	jupiter_pos_frac = 0.50
	saturn_pos_frac = 0.65
	uranus_pos_frac = 0.80
	neptune_pos_frac = 0.95

	sun_x = int(width * sun_pos_frac)
	mercury_x = int(width * mercury_pos_frac)
	venus_x = int(width * venus_pos_frac)
	earth_x = int(width * earth_pos_frac)
	mars_x = int(width * mars_pos_frac)
	jupiter_x = int(width * jupiter_pos_frac)
	saturn_x = int(width * saturn_pos_frac)
	uranus_x = int(width * uranus_pos_frac)
	neptune_x = int(width * neptune_pos_frac)

	solar_line_chars[sun_x] = '#'
	solar_line_colors[sun_x] = COLOR_YELLOW
	if sun_x + 1 < width:
		solar_line_chars[sun_x + 1] = '#'
		solar_line_colors[sun_x + 1] = COLOR_YELLOW

	solar_line_chars[mercury_x] = '.'
	solar_line_colors[mercury_x] = COLOR_GRAY
	solar_line_chars[venus_x] = 'o'
	solar_line_colors[venus_x] = COLOR_ORANGE
	solar_line_chars[earth_x] = 'E'
	solar_line_colors[earth_x] = COLOR_BLUE
	solar_line_chars[mars_x] = 'm'
	solar_line_colors[mars_x] = COLOR_RED
	solar_line_chars[jupiter_x] = '@'
	solar_line_colors[jupiter_x] = COLOR_LIGHT_BROWN
	if saturn_x - 1 >= 0:
		solar_line_chars[saturn_x - 1] = '='
		solar_line_colors[saturn_x - 1] = COLOR_BROWN
	solar_line_chars[saturn_x] = '&'
	solar_line_colors[saturn_x] = COLOR_BROWN
	if saturn_x + 1 < width:
		solar_line_chars[saturn_x + 1] = '='
		solar_line_colors[saturn_x + 1] = COLOR_BROWN
	solar_line_chars[uranus_x] = '*'
	solar_line_colors[uranus_x] = COLOR_CYAN
	solar_line_chars[neptune_x] = 'N'
	solar_line_colors[neptune_x] = COLOR_DARK_BLUE

	for i in range(sun_x + 2, width):
		if solar_line_chars[i] == ' ':
			solar_line_chars[i] = '-'
			solar_line_colors[i] = COLOR_GRAY

	colored_output = []
	current_color = COLOR_RESET
	for i in range(width):
		if solar_line_colors[i] and solar_line_colors[i] != current_color:
			colored_output.append(solar_line_colors[i])
			current_color = solar_line_colors[i]
		elif not solar_line_colors[i] and current_color != COLOR_RESET: # Reset if no specific color
			colored_output.append(COLOR_RESET)
			current_color = COLOR_RESET

		colored_output.append(solar_line_chars[i])
	
	print("\n")
	colored_output.append(COLOR_RESET)
	print("".join(colored_output))
	print("\n  ASCII Solar System (Small Scale Horizontal)")
	print(f"  {COLOR_YELLOW}# Sun{COLOR_RESET}   {COLOR_GRAY}. Mer{COLOR_RESET}   {COLOR_ORANGE}o Ven{COLOR_RESET}   {COLOR_BLUE}E Ear{COLOR_RESET}   {COLOR_RED}m Mar{COLOR_RESET}   {COLOR_LIGHT_BROWN}@ Jup{COLOR_RESET}   {COLOR_BROWN}=&={COLOR_RESET} Sat   {COLOR_CYAN}* Ura{COLOR_RESET}   {COLOR_DARK_BLUE}N Nep{COLOR_RESET}")
	print ("")

#-------------------------------------------------
#-------------------------------------------------
def main():
	if chkpy() != True:
		sys.exit(0)
	#----------------------------	
	check_tables(tables)
	make_intextdb()
	#----------------------------
	global aboutyou, days
	wms = random.choice(core['intromsg'])
	tdctl=0;ncctl=0;ffctl=0;ftr=0;kuote=quote()
	aboutyou = kdecode(aboutyou, checksum)
	#----------------------------
	if chkcoor(lat,lon) == True:
		_poigps_=[lat,lon,0,0,0]
	else:
		print_statusline(f"")
		mmodname = kdecode(seecoor, shift) + "\n   I cannot execute properly. Exiting."
		print(f"\n{kolor['DARK_RED']} {_spchar_[1:2]}{_title_} \033[0;0m: {mmodname}")
		sys.exit(0)
	#----------------------------
	#----------------------------
	print_statusline(f"")
	#----------------------------
	drawart('art_cybele')
	print(f"\n{kolor[('DARK_YELLOW')]}{wms}\n\n{kolor['BLUE']}I am {kolor['DARK_RED']}{_title_} {kolor['RED']}{_spchar_[0:1]}{kolor['BLUE']} a {website['home'][8:]}{_cyext_}{kolor['OFF']}")
	print_statusline(f"{kolor[('CYAN')]}I stored in memory since my boot {str('{:,}'.format(midbcounter))} records in {get_uptime()[2]} sec.{kolor[('OFF')]}")
	sleep(3.00)
	print_statusline(f"\n")
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
		if question == "bye" or question == "exit" or question == "quit":
			return False
		
		elif question == "word":
			r = RandomWords()
			w = r.get_random_word()
			print(f"{w}\n")
		
		elif question.startswith('tell me') or question.startswith('show me') and question.find('quote')!=-1:
			print(f"\n{_spchar_[2:3]}{kuote['quote']}{_spchar_[3:4]}\n{kuote['author']}\n")

		elif any(word in question for word in core['negative_word']) and question[0:13] != 'sharing about':
			print ("I understand. Is there anything else You want to ask'me ?\n")
			
		elif any(word in question for word in core['share']):
			if internet_onoff() == True:
				netchk = True
			else:
				netchk = False
			print ("The "+str(len(webshare))+" sharing informations i have are about the following subjects:\n")
			for tvshow, link in webshare.items():
				print(" > " + str(tvshow.upper()))
				print(f" {_spchar_[10:11]} {kdecode(str(link),shift)}")
				if netchk == True:
					print(" : " + kolor['GREEN'] + str(link_status(kdecode(link,shift))) + kolor['OFF'])
			print ("")

		elif any(word in question for word in core['badword']):
			print (random.choice(messages['badword_msg']) + "\n")

		elif _cybid_ == True and any(word in question for word in addcomm):
			cybext.EXTmod(question)

		elif question == 'list extcom' or question == 'extcom' and _cybid_ == True:
			print ("List of the available commands by" + _cyext_ + "\n")
			quicklist(addcomm,"")
			print ("")
		
		elif any(word in question for word in core['sayconvert']):
			convert_number = question.split()[-1:][0]
			if not convert_number.isdigit():
				print (f"""{" ".join(question.split()[1:]).title()}.\n""")
			else:
				print (f"{convert_to_words(int(convert_number)).capitalize()}. \n")

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
					print ("Yes. There are in my topic's.\n")
				else:
					print ("Unfornunately and dont have any information or Topic about'it. \n")

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

		elif question.startswith(('show me', 'tell me', 'list me')):
			if 'astronomy' in question or 'astronomy glossary' in question:
				all_keys = core["astronomy glossary"]
				random.shuffle(all_keys)
				astronomy_random_keys = all_keys[:5]
				astro_terms = ""
				for term in astronomy_random_keys:
					astro_terms += term + ", "
				print ("This are some of the terms i have in knowledge : " + astro_terms[:-2] + ".\n")
			
			elif 'stars' in question or 'star names' in question:
				all_stars = core["star name"]
				random.shuffle(all_stars)
				stars_random_keys = all_stars[:5]
				stars_names = ""
				for term in stars_random_keys:
					stars_names += term + ", "
				print ("This are some Stars names i have in knowledge : " + stars_names.title()[:-2] + ".\n")

			elif 'asteroids' in question:
				all_asteroids = core["asteroid"]
				random.shuffle(all_asteroids)
				asteroids_random = all_asteroids[:5]
				asteroid_names = ", ".join(asteroids_random)
				print ("Here are some asteroids i have in knowledge : " + asteroid_names + ".\n")

			elif 'old' in question or 'tech' in question:
				all_oldtech = core["old_tech_term"]
				random.shuffle(all_oldtech)
				oldtechs_random = all_oldtech[:3]
				oldtech_names = ", ".join(oldtechs_random)
				print ("Here are some old Tech terms i have in knowledge : " + oldtech_names + ".\n")

			elif 'constellations' in question:
				constelattionx = list(core['constelattion'])
				random.shuffle(constelattionx)
				constelattion_random = constelattionx[:5]
				viewconstellations = ", ".join(constelattion_random[:-1]) + ' and ' + constelattion_random[4] + ' constellations.'
				print ("I can show you based in my knowledge " + viewconstellations.title() + ".\n")

			if 'climate' in question or 'dictionary' in question:
				climatedict = list(core['climate dictionary term'])
				random.shuffle(climatedict)
				climatedict_random = climatedict[:3]
				viewclimatedict = ", ".join(climatedict_random[:-1]) + ' and ' + climatedict_random[2]
				print ("I can show you based on my Climate Dictionary knowledge terms like " + viewclimatedict.title() + ".\n")

			if 'meaning term' in question or 'meaning words' in question or 'meaning terms' in question:
				all_meanings = core["word meaning"]
				random.shuffle(all_meanings)
				meaning_random_keys = all_meanings[:3]
				meaning_words = ""
				for term in meaning_random_keys:
					meaning_words += term + ", "
				print ("This are some Meaning Terms/Words i have in my knowledge : " + meaning_words.title()[:-2] + ".\n")
			
			if 'constellations' in question and 'all' in question:
				print ("\nHere are all Constellations i have in knowledge ("+str(len(constellations_dict))+") and the meaning of her name or her designation:\n")
				for constelattion in constellations_dict:
					print(" %s: %s" % (constelattion.title(), constellations_dict[constelattion]))
				print ("")

			elif 'linux commands' in question:
				all_commands = core["linuxcmd"]
				random.shuffle(all_commands)
				commands_random_keys = all_commands[:5]
				commands_names = ""
				for term in commands_random_keys:
					commands_names += term + ", "
				print ("This are some Linux commands i have in knowledge : " + commands_names[:-2] + ".\n")

		elif question == 'astronomy questions' or question == 'questions of astronomy':
				all_astro = core["qa-astro"]
				random.shuffle(all_astro)
				astro_random_keys = all_astro[:3]
				astro_qa = ""
				for term in astro_random_keys:
					astro_qa += " "+_spchar_[1:2] + term + "?\n"
				print ("There are some astronomy questions you can make'me:\n\n" + astro_qa.title()[:-2] + "?\n")

		elif question[0:8] == 'how many' and question.find('glossary')!=-1 or question.find('astronomy terms')!=-1 or question.find('anwser')!=-1:
			print ("I can tell you the meaning of " + str(len(astronomy_glossary)) + " Astronomy glossary terms." + "\n")
		elif question[0:8] == 'how many' and question.find('asteroids')!=-1 and question.find('you know')!=-1 or question.find('anwser')!=-1:
			print ("I can tell you about " + str(len(core['asteroid'])) + " Asteroids, but there are millions and those we dont know.. yet." + "\n")
		elif question[0:8] == 'how many' and question.find('star')!=-1 and question.find('names')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge " + str(len(core['star name'])) + " Stars. " + random.choice(messages['endterm']) + "\n")
		elif question[0:8] == 'how many' and question.find('capitals')!=-1 and question.find('you know')!=-1 or question.find('anwser')!=-1:
			print ("Actualy based on my knowledge " + str(len(core['capital']) + 5) + " capitals and " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")
		elif question[0:8] == 'how many' and question.find('countries')!=-1 and question.find('you know')!=-1 or question.find('anwser')!=-1:
			print ("Actualy based on my knowledge " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")
		elif question[0:8] == 'how many' and question.find('linux commands')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge " + str(len(core['linuxcmd'])) + " Linux commands. " + random.choice(messages['endterm']) + "...\n")

		elif question[0:8] == 'what' and question.find('capitals')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge i know " + str(len(core['capital']) + 5) + " capitals and " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")
		elif question[0:8] == 'what' and question.find('countries')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge i know " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")

		elif question[0:9] == "days till" or question[0:8] == "days for" or question[0:7] == "days to":
			if len(question.split()[2:]) == 0:
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Till What!? \n")
			else:					
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

		elif question[0:22] == 'what do you know about' and question.find('constellations')!=-1 or question.endswith('?'):
			print ("I can tell you about " + str(len(constellations_dict)) + " constelations.\n ")

		elif question[0:22] == 'what do you know about' and question.find('the')!=-1 and question.find('universe')!=-1 or question.endswith('?'):
			print ("The solar system, information about planets, distances and the meaning of " + str(len(astronomy_glossary)) + " Astronomy terms, " + str(len(core['asteroid'])) + " asteroids (most basic information) and " + str(len(constellations_dict)) + " constelations.\n")

		elif question == 'can you' and question.find("sentence")!=-1 or question.find("phrase")!=-1:
			if question[0:4] == 'make':
				print ("This is a sentence! And I'm even not using NLP.\n")
			else:
				print ("Yes, I can! See? This is a sentence! And I'm even not using NLP.\n")

		elif question.find('vorian created')!=-1 or question.find('vorian was created')!=-1 or question.find('vorian went online')!=-1:
			print("The website [Vorian] was created in {} doing it online for {} days until today.\n".format(str(date(2010,12,9).strftime("%d.%m.%Y")), (date.today() - date(2010,12,9)).days))

		elif any(word in question for word in core['question_words']) and "you born" in question:
			print ("I borned from the code of my predecessor, Zorie, in early 2023 and I was officially actived " + str(days_till_today.days) + " days ago with an updated in " + _revise_ + ", so you better do the math!\n")

		elif any(word in question for word in core['question_words']) and any(word in question for word in core['planet']) and not "version" in question:
			print (random.choice(list(messages['magic_anwser'])) % "planet")
		elif any(word in question for word in core['question_words']) and any(word in question for word in core["old_tech_term"]) and not "version" in question:
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
			print ("The orbital regimes or types of orbit's i have in my knowledge are:\n")
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

		elif question == 's.o' or question == 'operating system' or question == 'system':
			if sysos == 'Linux':
				#nuptime = os.system('uptime')
				print ("This is the " + sysos + " Operating System (OS). ")
			elif sysos == 'Windows':
				print ("I am behing executed in " + sysos + "Operating System (OS).\n")
			else:
				print ("Sorry i cannot identify this Operating System. Maybe in my next update!\n")

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
				#if _cybid_ == True:
				print(random.choice(messages['birthday_short']) + " Are trying to trik'me, hmm! Its "+month_name+", "+date.today().strftime("%d")+". BAD " + os.getlogin() + "!\n")
				#else:
				#	print(random.choice(messages['birthday_short']) + " Are trying to trik'me, hmm! Its "+month_name+", "+date.today().strftime("%d")+". BAD User!\n")

		elif question == 'merry christmas' or question == 'i wish you a merry christmas':
			dt = date.today()
			if dt.month == 5 and dt.day >= 22 and dt.day <= 25:
				print ("Merry Christmas to you too!\nI hope you have a wonderful holiday season filled with joy, care and love.\n")
				print ("You should take a look at the page, only available around Christmas:\n" + " 〉 "+ website['home'] + "/merrychristmas")
				print ("A litle present for you...\n 〉 ")
				draw_christmas_tree()
			else:
				# Use the weather_season_condiction() or get_the_season() to play with "i'm definitely not ready for the cold and snow"
				if _cybid_ == True:
					random.shuffle(messages['notchristmas'])
					print (random.choice(messages['notchristmas']) + ". Okay, " + os.getlogin() + "!\n")
				else:
					random.shuffle(messages['notchristmas'])
					print (random.choice(messages['notchristmas']) + "\n")

		elif question.find('happy new year')!=-1:
			dt = date.today()
			if (str(dt)[5:]) == '12-31' or (str(dt)[5:]) == '01-01' and datetime.now().hour <= 3 :
				random.shuffle(messages['newyear_msg'])
				print (f"{random.choice(messages['newyear_msg'])} \nEnjoy the Fireworks ...")
				main_fireworks()
			else:
				random.shuffle(messages['earlier_nyear'])
				print( random.choice(messages['earlier_nyear']) + "\n")

		elif question == 'what is your version' or question == '#version':
			global cybelecode
			cybelecode = ksha([_title_+chr(46)+chr(112)+chr(121)])[0][1]
			_chkwww_ = 'online' if internet_onoff() else 'offline'
			_chkcid_ = cybelecode if cybelecode else 'Not verified'
			nversion = f"I am {_title_} {_chkwww_} in version {version} last updated on {_revise_} running for {days_till_today.days} days.\nmy unique id is '{_chkcid_}'."
			
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
			if internet_onoff() == True:
				storage = "online [sqlitecloud]"
			else:
				storage = "offline [database files]"
			if node_name:
				print('   Device : ' + platform.node() + '|' + _cyext_[0:4].replace(" ",""))
			else:
			  print ('  Device : unidentified device')
			print('     Name : ' + _title_)
			print('  Version : ' +version)
			print('  Revised : ' +_revise_)
			print('   Memory : ' + str(len(questions))+"|"+str(len(answers))+"|D"+str(midbcounter))
			print('     Data : ' + str(sum(len(value) for value in core.values())) + "|O" + str(len(old_tech_terms_list)) + "|M" + str(len(core["word meaning"])))
			print('    Linux : ' + str(len(linux_commands)))
			print('    Astro : ' + "G"+str(len(core["astronomy glossary"])) + "|A" +  str(len(core["asteroid"])) + "|C" +  str(len(core["constelattion"])) + "|S" +  str(len(core["star name"])))
			print('    World : ' + str(len(core["country"])))
			print('  Storage : ' + storage)
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

		elif question[0:13] == 'search askard':
			getparam = question.split()
			if len(getparam) != 3:
				print ('The correct usage is: search askard <word>\n')
			else:
				mandb('askardb','askardb_db','search',0,getparam[2])
				print ("")
		
		elif question[0:11] == 'view askard':
			getparam = question.split()
			if len(getparam) != 3 or getparam[2].isnumeric() != True:
				print ('The correct usage is <view> ' + _spchar_[9:10] + ' askard <id>\n')
			else:
				mandb('askardb','askard_db','view',getparam[2],0)
				print ("")
		
		elif question[0:8] == 'fun fact':
			if ffctl >= 3:
				print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['nicefun_msg'])}\n")
			else:
				mandb('cybele','funfacts','view',0,0)
				ffctl = ffctl + 1
				
		elif question[0:10] == 'nice thing':
			if ncctl >= 3:
				print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['activity_msg'])}\n")
			else:
				mandb('cybele','nicethings','view',0,0)
				ncctl = ncctl + 1
				
		elif question[0:11] == 'list askard':
			getparam = question.split()
			if len(getparam) == 2:
				mandb('askardb','askardb_db','list',0,0)
			elif len(getparam) == 4 and getparam[2].isnumeric() == True and getparam[3].isnumeric() == True :
				mandb('askardb','askardb_db','list',getparam[2], getparam[3] )
			else:
				print ('The correct usage is <list askard> to make a complete list of all database or <start> <end>.\n')
				
		elif question[0:16] == 'search astronomy':
			getparam = question.split()
			if len(getparam) != 3:
				print ('The correct usage is: search astronomy <word>\n')
			else:
				mandb('cybele','astronomy_glossary','search',0,getparam[2])
				print ("")

		elif question[0:14] == 'search oldtech':
			getparam = question.split()
			if len(getparam) != 3:
				print ('The correct usage is: search oldtech <word>\n')
			else:
				mandb('cybele','oldtech','search',0,getparam[2])
				print ("")

		elif question[0:12] == 'list oldtech':
			getparam = question.split()
			if len(getparam) == 2:
				mandb('cybele','oldtech','list',0,0)
			elif len(getparam) == 4:
				mandb('cybele','oldtech','list',getparam[2], getparam[3] )
			else:
				print ('The correct usage is <list oldtech> to make a complete list of all database or <start> <end>.\n')
		
		elif question[0:10] == 'stars from':
			getparam = question.split()
			if len(getparam) == 3:
				constelation_name = str(getparam[2])
				if constelation_name not in constellations_dict:
					print (f"There is no '{constelation_name}' in the {len(constellations_dict)} constelations i have in my knowledge!.\n")
				else:
					getconstellationabbr = constellations_dict[constelation_name]
					print (f"{creative_random_anwser()} Here he is the list of stars from the constelattion '{constelation_name.title()}'.")
					mandb('cybele','stars','list',getconstellationabbr[1].title(),0)
			else:
				print ('The correct usage is <list stars> from <constelattion name>.\n')
		
		elif question[0:10] == 'list stars':
			getparam = question.split()
			if len(getparam) == 4:
				print (f"{creative_random_anwser()} Here he is the list of stars from '{getparam[2]}' to '{getparam[3]}' i have in knowledge.")
				mandb('cybele','stars','list',getparam[2], getparam[3] )
			else:
				print ('The correct usage is <list stars> from <search letters> to <search letters>.\n')
			
		elif question[0:19] == 'list constellations':
			getparam = question.split()
			if len(getparam) == 2:
				print (f"{creative_random_anwser()} Here he is the list of constellations i have in knowledge.")
				mandb('cybele','constelations','list',0,0)
			elif len(getparam) == 4:
				print (f"{creative_random_anwser()} Here he is the list of constellations from '{getparam[2]}' to '{getparam[3]}' i have in knowledge.")
				mandb('cybele','constelations','list',getparam[2], getparam[3] )
		
		elif question[0:6] == 'limits':
			getparam = question.split()
			if len(getparam) == 2:
				if getparam[1] == "askard":
					mandb('askardb','','limits',0,0)
				elif getparam[1] == "astronomy":
					mandb('cybele','astronomy_glossary','limits',0,0)
				elif getparam[1] == "oldtech":
					mandb('cybele','oldtech','limits',0,0)
			else:
				print ('The correct usage is <limits <askard|astronomy|oldtech>> to show the first and last record in the database.\n')
			
		elif question.find('current')!=-1 and question.find('century')!=-1:
			current_century = get_current_century()
			print(current_century)

		#world population
		elif question[-10:] == "population":
			country_name = question.split()[0]
			if internet_onoff() == False:
				if country_name in core['country']:
					print("Estimated population based on my offline data from [{}] \n{} has a population of {:,} according to the United Nations.\n".format(_revise_, country_name.capitalize(), ncountries[country_name]["population"]))
				elif country_name == 'world' or country_name == 'earth':
					print ("8.1 billion people in July 2024 according to the United Nations. Is "+ year_months[date.today().month-1] +", "+ str(date.today().year) +" so there must be quite a few more.\n")
				else:
					print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " What ?! " + country_name.capitalize() + " Is that a new country? Perhaps! No-can do.\n")
			else:
				cpopulation = get_thepopulation(country_name)
				if cpopulation is not None:
					print("Based on the online data from [{}] \n{} has a population of {:,} according to the Worldometers.\n".format(str(date.today().strftime("%d.%m.%y")), country_name.capitalize(), cpopulation))

		elif question.startswith('where is ') and ('iss' in question or 'zarya' in question):
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

		elif question == 'what is he watching' or question == 'what are you watching':
			if question.find('fav')!=-1 or question.find('favorite')!=-1:
				print ("You can know what are "+_auth1r_+"'s in her public profile.\n  > "+ website['trakt'] + "\n")
			else:
				print ("You can follow real time what "+_auth1r_+" is watching by her profile.\n  > "+ website['trakt'] + "\n")
		
		elif question[-11:] == 'fav tvshows' or question[-16:] == 'favorite tvshows':
			print ('Based on the [' + website['tvshow'] + '] here are mine/'+ _auth1r_ + ' favorites:\n')
			extract_from_vorian()
			print ("")

		elif question == "do you speak" or question == 'do you talk' or question[-13:] == 'say something' or question[-15:] == 'make a sentence':
			cybele_phrase = make_sentence()
			print ("Well, beside behing a βeta version and dont using NLP or Library's or even speech synthesis here's something:")
			print ("\n - " + cybele_phrase + "\n")

		elif question.startswith('play') or question.startswith('game') and ('countries' in question or 'capitals' in question or 'math' in question or 'constellations' in question or 'elements' in question):
			if question.find("math")!=-1:
				cybele_math_game()
			if question.find("countries")!=-1 or question.find("capitals")!=-1:
				wcountry = {}
				for country, data in ncountries.items():
					wcountry[country] = data["capital"]
				cybele_play_quiz(wcountry,1)
				del wcountry
			if question.find("constellations")!=-1:
				cybele_play_quiz(constellations_abbr,2)
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
				print("Definitely the name of the star went on vacations!!\n" + random.choice(messages['nostar_message']) + "\n")
			else:
				if internet_onoff() == False:
					print (random.choice(messages['trouble_msg']) + " To get '" + star_name.capitalize() + " star' information i need an active Internet connection.\n")
				else:
					response = get_star_info(star_name)
					if len(response) != 0 and response[0] != 'emptydata':
						for i in range(len(response)):
							print (response[i])
					else:
						print( random.choice(messages['nostar_message']) + "cybele.star #" + star_name + " have empty data!\n")

		elif question == 'today activity':		
			if tdctl >= 3:
				print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['activity_msg'])}\n")
			else:
				random_season_activity()
				tdctl = tdctl + 1

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
		
		elif question[0:6] == 'genpwd':
			pwdparam = question.split()[1:]
			if len(pwdparam) != 2 or pwdparam[0].isnumeric() != True or pwdparam[1].isnumeric() != True:
				print (random.choice(messages['trouble_msg']) + " Incorrect usage parameters. Use: <genpwd <how many> <lenght>>.\n")
			elif int(pwdparam[0]) <= 0 or int(pwdparam[1]) <= 7:
				print (random.choice(messages['trouble_msg']) + " Incorrect min lenght's parameters. Use: <genpwd <Min generations:1> <Min lenght:8>>.\n")
			elif int(pwdparam[0]) >= 21 or int(pwdparam[1]) >= 65:
				print (random.choice(messages['trouble_msg']) + " Incorrect max lenght's parameters. Use: <genpwd <Max generations:20> <Max lenght:64>>.\n")
			else:
				generated_pwd = pwdgen(int(pwdparam[0]), int(pwdparam[1]))
				print ('Here are the generated passwords you requested:\n')
				for pwd in generated_pwd:
					print(" "+ _spchar_[1:2] + " " + pwd)
				print ("")
		
		elif question[0:20] == 'multiplication table' or question[0:7] == 'x table':
			xtablenum = question.split()[2:]
			if len(xtablenum) != 1 or xtablenum[0].isnumeric() != True:
				print (random.choice(messages['trouble_msg']) + " Incorrect usage parameter. Use: " + question.split()[0] + " " + question.split()[1] + " <number>.\n")
			else:
				multiplication_table(int(xtablenum[0]))

		elif question[0:8] == "hashfile":
			hashparam = question.split()[1:]
			if len(hashparam) == 0:
				print(f"Usage: hashfile <filename1> or [<path and filename2> ...]\n")
			else:
				hashfiles = question.split()[1:]
				hashresults = ksha(hashfiles)
				print ("")
				if hashresults:
					for i in range(len(hashresults)):
						print ("[SHA1] " + hashresults[i][0] + ": " + hashresults[i][1])
					print("")
				else:
					print(f"{random.choice(messages['trouble_msg'])} There is no sha1 data to present.\n")
		
		elif question == "cybele uptime":
			uptime_parts = get_uptime()
			time_units = [(uptime_parts[0], "hour"),(uptime_parts[1], "minute"),(uptime_parts[2], "second")]
			sentence_parts = []
			for value, unit in time_units:
				if value > 0:
					sentence_parts.append(f"{value} {unit}{'s' if value > 1 else ''}")
				if not sentence_parts:
					sentence = "less than a second"
				else:
					if len(sentence_parts) > 1:
						sentence = ", ".join(sentence_parts[:-1]) + " and " + sentence_parts[-1]
					else:
						sentence = sentence_parts[0]
			print(f"I'm running for {sentence} since {start_time.strftime('%H:%M')} local time.\n")
		
		elif question[0:8] == 'holidays':
			country_holidays()
			
		elif question == 'trails':
			print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} I think what you are trying can be found here:")
			print (f"{website['trails']}\n")
		
		elif question == 'view solar system':
			terminal_width, terminal_height = os.get_terminal_size()
			ascii_horiz_solar_system(width=terminal_width-3)
			print ("")
		
		elif question == 'testing':
			print ('Development testing propose code...\n')
			xn = fetch_fromdbfile("cybele.db", "config", "code")
			print (xn[0])
		
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

#-------------------------------------------------
if __name__ == "__main__":
	try:
		while True:
			if main() == False:
				break
		print(random.choice(core['exitmsg']) + random.choice(['',' Bye.']))
		globals().clear()
	except SystemExit as e:
		globals().clear()
	except KeyboardInterrupt:
		print ("")
		print(random.choice(core['exitmsg']) + random.choice(['',' Bye.']))
	globals().clear()
