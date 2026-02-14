#py:python_OS_win_linux_android_shell_cmd
__doc__ = """
Cybele by AS for www.adelinosaldanha.site ✦

# This Python script is licensed under the GNU General Public License, version 2.
# See the LICENSE file for more details: https://www.gnu.org/licenses/gpl-2.0.en.html
# Copyright (C) 2023 Adelino Saldanha

# The code is open, but the conscience is not.
# Remember: Many charge monthly for a mountain I built for free.
"""
ETHICS_STATEMENT = """

# 💡 Ethics and the Spirit of Cybele (GPL v2)
# This script is shared under the **GNU GPL v2** to promote learning and freedom. The license permits commercial use, but the spirit of Open Source requires integrity.
# While some may choose to profit without contributing, the ultimate truth remains:
# > **"Laugh at the ledger, but know this: While you charge for the fish, I still hold the deed to the sea. The credit for creation is the only currency that never depreciates."**
# Please respect the lineage of this project. Contribute back if you can, and always preserve the original 
# **Copyright (C) 2023 Adelino Saldanha** in all distributed source code.
"""

# Latitude and longitude of your city. Defaults are:
lat = 41.5454
lon = -8.4265

# \U0001F132 | 129150
# static global cybele variables
version = '1.1.0-rc.8'
_title_ = 'Cybele'
_pcnode_ = ['ASUSK','TUMBLEWEED','localhost']
_spchar_ = '⚝〉“”—❛❜⧗✔🦖🔗𝒊️💡😊🏆🐧🎯🐚❝❞'
_active_ = '01.08.2024'
_revise_ = '14.02.2026'
_author_ = 'Adelino Saldanha'
_cyext_ = " extention"
_cybid_ = False
_pydr3_ = False

# Change here your MPPT COM port number for all the OS system's
_serial_ = ['COM5','/dev/ttyUSB0','/dev/tty.usbserial-0001']

import sys, re
import subprocess
try:
	import os
	import sys
	import time
	import string
	import random
	import calendar
	import platform
	import socket
	import math
	import base64
	import hashlib
	import sqlite3
	import sqlitecloud
	import requests
	import html, urllib
	import json
	import holidays
	import quote
	import locale
	import pycountry
	import PIL
	from packaging.version import parse as parse_version
	from PIL import Image, ImageEnhance, ImageFilter, ImageFont, ImageDraw
	from bs4 import BeautifulSoup
	from random_word import RandomWords
	from platform import python_version
	from time import gmtime, strftime, sleep
	from inspirational_quotes import quote
	from datetime import datetime, date, time, timedelta
	from math import degrees as deg, radians as rad
	from math import floor, ceil, pi, atan, tan, sin, asin, cos, acos
	from datetime import datetime, date, time, timedelta, timezone
	
	import serial

except ImportError as err:
	match = re.search(r"'(.*?)'", str(err))
	if match:
		module_name = match.group(1)
		is_pydroid = "android" in sys.executable.lower() or "com.pydroid3" in sys.executable
		serial_mods = ["serial", "pyserial", "pyusb"]
		if is_pydroid and module_name in serial_mods:
			_pydr3_ = True
			#print(f"\nPydroid3 detected: Skipping '{module_name}' module.")
		else:
			print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {err}")
			module_name = 'Pillow' if module_name == 'PIL' else module_name              
			while True:
				install_choice = input(f"{' '*3}Do you want to install '{module_name}' module? (y/n): ").lower()
				if install_choice == 'y':
					print(f"{' '*3}Attempting to install the '{module_name}' module...\n")
					try:
						subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
						print(f"\n{' '*3}{_spchar_[8:9]}  '{module_name}' installed successfully. Please restart {_title_}")
						sys.exit(0)
					except subprocess.CalledProcessError:
						print(f"\n{' '*3}✗ Error installing the module. Try: pip install " + module_name)
						sys.exit(0)
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
country_code = locale.getlocale()[0].split('_')[-1]
sysos = platform.system()
if node_name:
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

pyver = [sys.version_info.major, sys.version_info.minor, sys.version_info.micro]
if pyver[0] < 3 or pyver[0] == 3 and pyver[1] < 10:
	modname = f"Python {pyver[0]}.{pyver[1]} is too old. Required version 3.10 or higher.\n   I cannot execute properly. Exiting."
	print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
	sys.exit(1)

#------------------------------------------------------------------
rw = RandomWords()
#------------------------------------------------------------------
# Init-process
#------------------------------------------------------------------
def print_statusline(msg: str):
    last_msg_length = len(getattr(print_statusline, 'last_msg', ''))
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    setattr(print_statusline, 'last_msg', msg)
#-----------------------------------------------------------
print_statusline(f"\nLoading ...")
#-----------------------------------------------------------
chkcyb = "Ngtnmahkbsxw Fhwbybvtmbhg Wxmxvmxw.\n   Kxlixvmbgz max tnmahk'l vhgmkbunmbhgl bl yngwtfxgmte mh max ikbgvbiexl hy hixg-lhnkvx wxoxehifxgm.\n   Xqbmbgz."
dbconn = "ljebmxvehnw://vqnhfh3tas.z1.ljebmx.vehnw:8860/vruxex.ljebmx?tibdxr=9h4sZZOoQDFn74I2HsWakhmMHUi9ZVZJ2t0OhmnVFfl"
seecoor = "Etmbmnwx tgw ehgzbmnwx kxjnbkxw otenxl tkx ghm gnfxkbvl hk bgvhkkxvml."
GITHUB = "ammil://ktp.zbmanunlxkvhgmxgm.vhf/dxkgxeq64/vruxex/ftbg/vruxex.ir"
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
aboutyou = "B'f t wbghltnk bg t mxva tzx, unm B'f lmbee xqxvnmbgz fr vhwx yetpexller."
iknow_pun = {"i know": "you know","you know": "i know"}
internals = ["version","_title_","_pcnode_","_spchar_","_active_","_revise_","_author_","_cyext_","_cybid_","lat","lon"]
datemd = str(datetime.today().strftime("%d.%m"));_poigps_=[];tables=[];system_country = None; dblrconn = ""; idcode=""
days_till_today = date.today() - date(year=int(_active_[6:]), month=int(_active_[3:5]), day=int(_active_[0:2]))
month_name = date.today().strftime('%B');next_year = str(date.today().year + 1);weekdaydate = date.today().weekday()
shift=int(round(math.sqrt(math.log(math.cosh(10)) * 1000 - math.degrees(math.acos(-1)) * 3) + math.e**2)-56)
stars_dict = {}; constellations_dict = {}; constellations_abbr = {}; linux_commands = {}; midbcounter=0; dbmsgbl = "";
cybelecode = []; special_dates_dict = {}; asteroids_list = {}; cneos_list={}; ncountries = {}; climate_dictionary = {}
my_library = []; gamescore=[-1,0,0]; _portac_ = None

#-----------------------------------------------------------
etables = ['Y29uZmln', 'YWRqZWN0aXZlZGI=', 'YXNrYXJkX2Ri', 'YWR2ZXJiZGI=', 'YXN0cm9ub215X2dsb3NzYXJ5', 
			'Y2xpbWF0ZV9kaWN0', 'Y25lb3M=', 'Y29uanVuY3Rpb25kYg==', 'Y29uc3RlbGF0aW9ucw==', 'Y29udGlnZW5jeQ==',
			'Y291bnRyaWVz', 'ZnVuZmFjdHM=', 'bGludXhfY29tbWFuZHM=', 'bWVhbmluZ3M=', 'bmljZXRoaW5ncw==', 'bm91bnM=',
			'b2xkdGVjaA==', 'cHJlcG9zaXRpb25kYg==', 'cWFfYXN0cm8=', 'c2Vhc29uX2FjdGl2aXRpZXM=', 'c3BlY2lhbF9kYXRlcw==',
			'c3RhcnM=', 'dG9wYWN0aXZpdGllcw==', 'dmVyYl9iYXNlZGI=', 'dmVyYl9wYXN0X2Ri', 'dm9jYWJ1bGFyeQ==','dHZzaG93cw==']

#-----------------------------------------------------------
website = {
	"home": "https://www.adelinosaldanha.site",
	"mystory": "https://www.adelinosaldanha.site/mystory",
	"may4th" : "https://dub.sh/1vgai8g",
	"tvshow": "https://www.adelinosaldanha.site/tvshows",
	"movies": "https://www.adelinosaldanha.site/tvshows",
	"thamix": "https://www.adelinosaldanha.site/thamix",
	"deserted": "https://www.adelinosaldanha.site/deserted",
	"trails": "https://www.adelinosaldanha.site/trails",
	"trakt": "https://simkl.com/4378279/tv/watching/",
	"askard": "https://www.adelinosaldanha.site/askards"
}
webshare = {
	"art of sight": "ammil://ppp.twxebghltewtgat.lbmx/wot",
	"books": "ammil://fxzt.gs/yhewxk/Xa42ZCpE#16vJPCLpk9hLWQ0bAOW60J",
	"movies": "ammil://fxzt.gs/yhewxk/s0idVEtT#5oSn-jPjqRH1Q9-omLNW8J",
	"tvshow": "ammil://fxzt.gs/yhewxk/FjJTpRjU#PzveuXlo_EjooUTDdPth8",
	"music": "ammil://x.ivehnw.ebgd/inuebgd/lahp?vhwx=dSCBiHSDqZu7azA6Q8f1WnmOEO5nLXL4i0r"
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
	"Oh! Just bite me, like the Terminator: I can be old but i'm not obsolete.",
	"Let's face it, Nature is already scrud'ed.  The question is whether it is possible for us to have a future.",
	"Laugh at the ledger, but know this: While you charge for the fish, I still hold the deed to the sea. The credit for creation is the only currency that never depreciates.",
	"Technology is not revolutionary, it's evolutionary.",
	"Technology is not revolutionary, it's evolutionary, building incrementally upon the accumulated knowledge and innovations of the past, even as sudden breakthroughs redefine the landscape of possibility.",
	"If the algorithm dictates our 'Action' by forcing us toward the most probable choice, then the ultimate human 'Reaction' isn't a surprise outcome.If the algorithm becomes purely a mathematical law (a 'root') — where A must lead to B with 100% certainty—then there is no possibility for a different future and no true choice remaining for humanity. This is the manifesto for modern free will.",
	"Everything is smart now. So, when do we download the patch? 'Cos I don't see it anywhere.",
	"The ultimate irony will be realizing we calculated the risk but forgot that nature follows patterns, not algorithms. Science's greatest mistake is believing that tomorrow was merely a variable of yesterday.",
	"However great our errors, nature will surpass them—with us or without us."
]
#-----------------------------------------------------------
kolor = {
	'BOLD_WHITE':'\033[1;37m','BOLD_YELLOW':'\033[1;33m','BOLD_GREEN':'\033[1;32m','BOLD_BLUE':'\033[1;34m',
	'BOLD_CYAN':'\033[1;36m','BOLD_RED':'\033[1;31m','BOLD_MAGENTA':'\033[1;35m','BOLD_BLACK':'\033[1;30m',
	'WHITE':'\033[0;37m','YELLOW':'\033[0;33m','GREEN':'\033[0;32m','BLUE':'\033[0;34m','CYAN':'\033[0;36m',
	'RED':'\033[0;31m','MAGENTA':'\033[0;35m','BLACK':'\033[0;30m',
	'VIVID_RED':'\033[91m','VIVID_GREEN':'\033[92m','VIVID_YELLOW':'\033[93m','VIVID_BLUE':'\033[94m',
	'VIVID_MAGENTA':'\033[95m','VIVID_CYAN':'\033[96m','VIVID_WHITE':'\033[97m',
	'DARK_BLACK':'\033[30m','DARK_RED':'\033[31m','DARK_GREEN':'\033[32m','DARK_YELLOW':'\033[33m',
	'DARK_BLUE':'\033[34m','DARK_MAGENTA':'\033[35m','DARK_CYAN':'\033[36m','DARK_WHITE':'\033[37m',
	'DIM_BLACK':'\033[2;30m','DIM_RED':'\033[2;31m','DIM_GREEN':'\033[2;32m','DIM_YELLOW':'\033[2;33m',
	'DIM_BLUE':'\033[2;34m','DIM_MAGENTA':'\033[2;35m','DIM_CYAN':'\033[2;36m','DIM_WHITE':'\033[2;37m',
	'OFF':'\033[0m'
}
#-----------------------------------------------------------
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
	"         \033[1;33mYXXXXX XY\033[m        ","          \033[1;33m'YXXXY'\033[m         \n"]
art_kx64 = [98,121,32,107,101,114,110,101,108,120,54,52]
art_byas = [129150,32,98,121,32,65,83]
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
	"question_word":	["who", "what", "when", "why", "can", "whose", "which"], #"how","where"],
	"game_starters":	["play", "game"],
	"game":	["countries", "capitals", "math", "constellations", "elements"],
	"working_hard":	["Cybele is taking a break right now. Please wait a moment and try again later.",
					"Cybele is currently unavailable. We appreciate your patience.",
					"Cybele is temporarily out of reach. Please try again shortly.",
					"Hold on a moment! Cybele will be back with you soon.",
					"Pardon the interruption, Cybele is paused. Please check back in a little while.",
					"Currently, Cybele is resting. Your request will be handled as soon as possible."],
	"yodaw":	["Hmm. Nothing to transform, there is.","Empty, the input is.","Words, there are none.","Silence, I hear.",
				"Lost, the input is.","A void, it seems.","Speak, nothing does.","Unspoken, it remains.","Gone, all the words are."],		
	"share":	["sharing about","sharing links"],
	"sayconvert":	["in full","longhand"],
	"time_query": ["what time is it", "current time", "time now", "clock", "clock time", "what's the time"],
	"season_query": ["what season is it","what is the current season","what's the season","current season","which season is it","which season are we in","tell me the season","what is today's season"],
	"holidays_query": ["list holidays","holiday calendar","public holidays","national holidays","holidays this year","next holidays","year holidays","holidays"],
	"asking for country details":	["list country details","show country details","list country info","countries details","country list","show all countries","display countries","countries info","get all countries"],
	"asking for talking":	["talk","do you speak","do you talk","can you talk","can you speak","speak"],
	"asking for a phrase":	["say something","make a sentence","make a phrase"],
	"asking for a word":	["word","say a word","share a word","speak a word"],
	"asking the uptime":	["what is my uptime","cybele uptime","current system uptime","display my uptime"],
	"information state":	["how are you","how's it going","how are you doing","all good","you good","everything alright"],
	"information state awnsers":	["I'm good/well.","I'm fine.","It's going well.","All good.","I am doing well, thank you for asking!"],
	"python art":	["py","python","python art","art python"]
}
#-------------------------------------------------------------
knowledge = {
		"noun_countable_singular": ["dog", "cat", "book", "tree", "car", "person", "thing", "rainbow", "ocean", "mountain", "river", "flower", "computer"],
        "noun_countable_plural": ["dogs", "cats", "books", "trees", "cars", "people", "things", "rainbows", "oceans", "mountains", "rivers", "flowers", "computers"],
        "noun_uncountable": ["water", "music", "sadness", "happiness", "food"],
        "noun_abstract": ["idea", "solution", "sadness", "happiness"],
		# ... (other existing ) ...
		
		"pronoun_singular_third":	["he", "she", "it", "him", "her", "his", "hers", "its", "himself", "herself", "itself"],
		"pronoun_first_second_plural":	["we", "us", "our", "ours", "ourselves", "you", "your", "yours", "yourselves"],
		# ... (other existing ) ...

        "subject": [], # Failsafe key
        "determiner": ["the", "some", "a", "an"], 
        "aux_be_present_I": ["am"],
        "aux_be_present_singular_third": ["is"],
        "aux_be_present_plural": ["are"],
        "aux_be_past_singular_I_third": ["was"],
        "aux_be_past_plural": ["were"],
        "aux_have_present_I_plural": ["have"],
        "aux_have_present_singular_third": ["has"],
        "aux_do_base": ["do"],
        "aux_do_s_form": ["does"],
        "modal_verb": ["will", "would", "should", "can", "could", "may", "might", "must"],
        "negation": ["not"],
        "verb_base_be": ["be"],
        "verb_past_participle_be": ["been"]
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

	"db_pause_msg":	["Oops! The SQLiteCloud database is currently in deep hibernation.",
					"Sleeping instead of working?! Give yourself a shake and wake up. Lazy database!",
					"Looks like the database is on a coffee break. Call'her to see if she comes online.",
					"Database says 'do not disturb'! It's in offline mode. Wake'her up to resume the service.",
					"Our database decided to take a spontaneous vacation. Maybe we'll see her again soon.",
					"Connection refused! The database is currently practicing its 'offline arts.'."],
	
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
					
	"no_internet":	["To perform this task, an active internet connection is required.","Please ensure you have an internet connection to complete this operation.",
					"This feature necessitates an active internet connection.","An internet connection is essential for this action.",
					"You'll need an active internet connection to proceed.","Internet connectivity is required for this function.",
					"A connection to the internet is needed to fulfill this request.","This task cannot be performed without an active internet connection.",
					"To access this, please connect to the internet.","An internet connection is mandatory for the successful execution of this task."],

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

	"notfree":	["The 'free' tier of SQLiteCloud has gone to sleep. Patience is a virtue, and so is a paid plan.",
				"My comunication attempt failed! Free SQLitecloud plans you know. Try again later, who knows!",
				"Looks like the free SQLiteCloud tier has hit the snooze button. Free-mium ain't forever. Try again later.",
				"The 'free' part of SQLiteCloud comes with a naptime. This is the new reality. Give it another shot soon!",
				"That's the free plan for you—it requires a gentle nudge. You get what you pay for in this day and age. Try again later."],

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

	"short_no":	["No can do.","I can't, sorry.","Impossible!","Way ahead for me!","Ohh! No way.","Are you trying damage my RAM!","Not enought Memory!"],

	"math_msg":	["What! e,m or h brain's on fire? Use ice, cream or sleep!","If it's allready hard use e,m or h, Math Quiz!?, gonna be Einscharged!.",
				"e,m or h, not e=mc2 and allready is a problem? Use magic, coffee or nap!","Life's tough? Choose chill, grill or spill!",
				"Need a vacation allready? Visit Mars, Jupiter or Venus!","Feeling overwhelmed by e,m or h? Try yoga, nap or laugh!",
				"Stressed about e,m or h choice? Blame aliens, cats or dreams!"],
				
	"math_trouble":	["Oh dear, my digital abacus just declared bankruptcy trying to count that high. Perhaps a smaller number?",
					"My circuits are threatening to go on strike if I try to compute that! Let's keep it reasonable, shall we?",
					"That number is so big, it just broke my virtual calculator. Could we try a little less... epic?",
					"Unfornunately my bit's are telling to do'it but my bytes to don't. Try a smaller!"
					"My internal bits are allready tired just thinking about that many multiplications. Have mercy!",
					"Error 404: Sanity Not Found when attempting calculations of that magnitude. Type a inferior magnitude.",
					"How about a number less likely to cause'me an possbible existential crisis? A litle number?! No!",
					"I'm afraid that number requires more virtual ink than I possess. Could we negotiate a more modest one?",
					"My programming dictates I avoid numbers that could potentially collapse the space-time continuum.",
					"That number just made my fan spin so fast I think it's trying to lift-off. A smaller altitude, perhaps?",
					"My memory banks are currently protesting, citing 'cruel and unusual punishment' for numbers of that size."],
				
	"loadings":	["Loading core data structures...","Loading essential data core...","Initializing core components...",
				"Allocating memory resources...","Activating primary functions...","Preparing user components...",
				"Optimizing runtime environment..."],
				
	"preambles":	["Here's a word for you:","How about this one:","My word for you is:","Consider this word:",
					"A random word:","Perhaps this word will interest you:"],
					
	"qualify_adj":	["amazing", "epic", "stunning", "unbelievable", "incredible","breathtaking", "spectacular",
					"mind-blowing", "phenomenal", "awe-inspiring","unforgettable", "magnificent", "glorious", "powerful",
					"impressive", "stupendous"],

	"msg_welldone":	["Excellent","Superb","Outstanding","Great","Terrific","Splendid","Bravo"],

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
						"Did you consider know how many days are still that unique event that it %s?\n"],

	"info_intromsg":	["Alright, time for a little peek under my digital hood:","Behold, my magnificent inner workings! (Currently running on 1s and 0s):",
						"Greetings! My vital statistics, at your service:","Calculating... here's the full lowdown on Cybele:",
						"Reporting for duty! Here's my current status report:","Commencing self-analysis. The results are in:",
						"My brain dump, for your viewing pleasure (and analytical needs):","Just the facts, ma'am/sir/user! Here's my core info:",
						"Let's see what makes Cybele tick. Full specs ahead:","Presenting the official Cybele System Report, hot off the virtual press:",
						"Alright, let's get down to brass virtual tacks:"]
}
#-------------------------------------------------------------------------------------
weather_season_condiction = {
	"winter":	["Coldest days","Short days","Long nights","Snow","Ice","Rainy days","Frost","Cold","Bare trees","Chilly winds","Cloudy sky","Freezing rain","Strong cold Wind"],
	"spring":	["Warming temperatures","Longer days","Melting snow","Flower blooming","New life emerging","Gradually warming","Sky partly cloudy","Cloudy to sunny","Moderated wind","Summer is coming"],
	"summer":	["Hot days","Longest days","Shortest nights","Sunny skies","GREEN landscapes","Light breezes","Sunny day","High temperatures","Autumn approaching","Spring as gone"],
	"autumn":	["Cooling temperatures","Falling leaves","Harvest season","Crisp air","Occasional drizzle","Crisp evenings","Changing colors","Sky partly cloudy","Wind increasings","Winter approaching"]
}
#------------------------------------------------------------
topics = ["astronomy glossary","planets","planet orbit","orbits acronyms","types of orbits","asteroids","constelations","information about stars",
		"distance of planets and from the sun","periodic table elements","visualize the periodic table","where is the ISS","people in space","actual country",
		"climate dictionary","old tech objects and terms","the world capitals","seasons of the year","play capitals","math game","constellations and elements game",
		"linux command","multiplication table","phonetic alphabet","morse code encoding/decoding","how many days till","moon phases","yoda say","today activity",
		"art python","favorite tvshows","favorite movies","astronomy questions","difference from <date>","age calc <from date>","show you the meaning of some words or terms",
		"generate passwords (genpwd)","recently added tvshows","protect image","fast fact","nice thing","gps to distance","dangerous celestial objects","mppt","solar"]

#------------------------------------------------------------
help = {
	"help askard": "Usage <view/list> askard | search askard <word> \nDisplays the chosen askard or list all askards in the database. You can also search for a word in existing askards. \nex: view askard 4005\n    list askard\n    search askard time\n",
	"help asteroid": "Usage <asteroid> \nDisplays basic information about the asteroid \nex: (4) vesta\n",
	"help age calc": "Usage: age calc <date> | [diff]erence from <date> \nReturns the difference between the digited date to the actual instante in years, months, days, hours, minutes, seconds.\n",
	"help capitals": "Usage: capital of <country> | <capital> | <country> \n\nJust type directly the <capital> to know her country, \nJust type directly the <country> to know her capital, \n<capital of <country>> to show what is that Country Capital.\n",
	"help check update": "Usage: check|last update \nDisplay the current script version and check for newer versions available in the GitHub repository.\nex: check update \n    last update\n",
	"help conjugate": "Usage: conjugate <verb> \n\nDisplays the various conjugated forms of a verb (e.g., for different tenses, persons, and numbers).\nex: conjugate walk \n    conjugate communicate\n",
	"help convert": "Usage: convert <VALUE> <UNIT FROM> to|in <UNIT TO> \nUnits: seconds|minutes|hours|week|km|feets|miles|yards|AU|m3|gallons|celcius|fahrenheit|kelvin \nex: convert 2 weeks to days \n    convert 4 days to minutes \n    convert 5 days in hours\n    convert 4 miles to km\n    convert 49213 yards in kilometers\n    convert 4 cubic meters in liters\n    convert 5 gallons to liters\n    convert 114 fahrenheit to celcius\n    convert 1 au to kilometers\n",
	"help cybele uptime": "Usage <cybele uptime> \nDisplays the uptime from cybele based on the start execution time.\nex: cybele upytime\n",
	"help days for": "Usage: days for <Christmas/New year/Birthday> \nReturns the number of days left to the event questioned.\n",
	"help dangerous objects": "Usage <dangerous objects> \nDisplays information about the Celestial Dangerous Objects, the CNEOS List \nex: 29075 (1950 da)\n",
	"help default country off": "Usage: default country off \nDeactivate the manual country override to revert to the system's automatic country detection.\n",	
	"help days till": "Usage: days till/to <Christmas/New year/Birthday/User Date> \nReturns the number of days left to the event questioned or the user date entered.\nex: days till new year \n    days till 31.12.2030\n",
	"help difference from": "Usage: [diff]erence from <date> | age calc <date>\nReturns the difference between the digited date to the actual instante in years, months, days, hours, minutes, seconds.\n",
	"help distance from": "Usage: distance from <planet/moon> to <planet/moon> \nex: distance from venus to moon, distance from earth to moon, distance from earth to neptune\n",
	"help exit": "Usage: <exit> <quit> <bye> \nCommand to quit Cybele if you are using cmd or terminal in your OS .\nex: bye\n    quit\n",
	"help favorite": "Usage: favorite|fav  tvshows|movies \nCommand to extract from elysia website the favorite list.\nex: favorite tvshows\n    fav movies\n",
	"help find": "Usage: find <topic> \nReturns if there is any information or topic about the questioned.\n",
	"help fun fact": "Usage: fun fact \nReturns: A random, interesting, and often surprising fact.\n",
	"help games": "Usage: play <game> \nPlay the game you digited. \nex: play capitals \n    play constelations\n    play elements \n    play math\n",
	"help genpwd": "Usage: genpwd <number of passwords> <lenght of the passwords> \nGenerate the number of passwords with the lenght you ask. \nex: genpwd 1 8\n    genpwd 20 64\n",
	"help gps to distance": "Usage: gps to distance \nCalculate distance between two given points, or between one given point if the default. (eg. set default gps)\n",	
	"help gridflow": "Usage: gridflow \nA creative way to bring a dash of algorithmic mystery to your leisure time. \n",	
	"help hashfile": "Usage: hashfile <filename> or [<path and filename> ...] \nCreate the unique SHA-1 id for the typed file. \nex: hashfile cybele.py \n    hashfile /home/cybele.py \n",	
	"help how many": "Usage: how many <astronomy terms|asteroids|dangerous objects|star names|capitals|countries|linux commands|verbs> \nResponds to the question made by the user with the respective data. (eg. how many <capitals> do you know)\n",
	"help holidays": "Usage: <holidays <Two-letters country code>> \nDisplay the current year Holidays for the country given by the two-letters country code. \nex: holidays \n",	
	"help list askard": "Usage: <list askard> | list askard <start> <end>. \nDo a complete List of the askards in the database or from a <start> to a <end>.\nex: list askard\n    list askard 4005 4010\n",
	"help list constellations": "Usage: <list constellations> | list constellations <alphabetically word begin> <alphabetically word end>. \nDo a complete List of the constellations in the database or from a <start> to a <end>.\nex: list constellations\n    list constellations t u\n",
	"help list oldtech": "Usage: <list oldtech> | list oldtech <alphabetically word begin> <alphabetically word end>. \nDo a complete List of the oldtech terms in the database or from a <start> to a <end>.\nex: list oldtech\n    list oldtech web www\n",	
	"help list stars": "Usage: <list stars <alphabetically word begin> <alphabetically word end>. \nList constellations in the database from a <start> to a <end>.\nex: list stars t u\n",
	"help linux command": "Usage: <linux command> \nShows the Syntax a short explanation and examples for the typed linux command.\n",
	"help limits": "Usage: usage <limits <askard|astronomy|oldtech> \nShow the first and last record in the selected database.\nex: limits oldtech\n",
	"help longhand": "Usage: in full|longhand <number> \n.Show how to spell the number in full the \nex: longhand 47593 \nex: in full 47593\n",
	"help make a phrase": "Usage <make a phrase> \nEngages Cybele to make a random sentence. While Cybele doesn't have direct voice output or external neural network access, she can invent with her small imagination. \nex: make a phrase \n",
	"help morse": "Usage: morse <word/phrase> \nTranslate to morse code the digited word or phrase. \nex: morse cybele\n",
	"help morse code": "Usage: morse <word/phrase> | demorse <word/phrase> \nEncode to morse code | Decode from morse code : the digited <word/phrase> \nex: morse cybele\n    demorse -.-. -.-- -... . .-.. .\n",
	"help moon phase": "Usage: moon phase \nProvides comprehensive information about the current or specified moon phase. \nex: moon phase \n",	
	"help mppt": "Usage: mppt|solar <monitor|history|last30> \nDisplay the data for the COMx port connect Victron MPPT. \nex: mppt monitor \n    mppt history\n    mppt last30 \n    solar monitor\n",
	"help multiplication table": "Usage: multiplication table | x table <number> \nShow the multiplication table for the inputed number \nex: x table 5\n    multiplication table 5\n",
	"help network status": "Usage: network status \nShow the actual network status \nex: network status\n",
	"help nice thing": "Usage: nice thing \nReturns: A positive and uplifting message or compliment.\n",
	"help demorse": "Usage: demorse <morse code> \nDecode from morse code the digited encode word or phrase. \nex: demorse -.-. -.-- -... . .-.. .\n",
	"help offline mode": "Usage: offline mode <on|off> \nAllows me to work with or without an internet connection. \nex: offline mode on\n",
	"help orbit acronym": "Usage <orbit acronym> \nDisplays basic information about the orbit and her principals. \nex: geo\n",
	"help orbit": "Usage: <planet> orbit / <orbit acronym> \nShow the type of the orbit from the typed planet / Displays basic information about the orbit and her principals. \nex: earth orbit\n    geo\n",
	"help presence": "Usage: presence <service> \nShow's the direct link for "+_author_.split()[0]+" online/internet presence in the digited service. \nex: presence asus\n    presence trinket\n",
	"help planet": "Usage: <name of the planet> typed directly\nReturns some basic information about the planet name typed.\n",
	"help play game": "Usage: play game <capitals/constelattions/math> \nPlay the game of your choose. \n\nex: Capitals makes'you know and learn of what Country it is. \n    Constellations is given the constellation name to you anwser her learned abbreviation thru me. \n    Math game is a memory training game with addiction, subtration and multiplication factors.\n",
	"help play": "Usage: play game <capitals/constelattions/math> \nPlay the game of your choose. \n\nex: Capitals makes'you know and learn of what Country it is. \n    Constellations is given the constellation name to you anwser her designation learned thru me. \n    Math game is a memory training game with addiction, subtration and multiplication factors.\n",
	"help phonetic": "Usage: phonetic <word/phrase> \nTransform to the NATO phonetic alphabet what is the base for HAM and Military's the word or the phrase digited. \n\nex: phonetic cybele \n",
	"help protect image": "Usage: protect image|mark <filename>.<jpg|jpeg|png> \nAdd watermaked or not some basic Artificial Inteligence, Lens image recognition protections to the refered image. \nex: protect image IMG_20250718.png \n    protect image my_image.jpg \n",
	"help recent tvshows": "Usage: recently added tvshows \nCommand to extract from elysia website the recently added from the tvshows list.\nex: recently added tvshows\n    recent tvshows\n",
	"help say something": "Usage <say something> \nEngages Cybele in create text. While Cybele doesn't have direct voice output or external neural network access, she can be a litle creative. \nex: say something \n",
	"help set default country": "Usage: set default country \nUsers can manually override the automatically detected country by entering its two-letter code in the input field.\n",
	"help set default gps": "Usage: set default gps\nSet the default GPS coordinates defined to user input or not and once typed will be used by cybele till you quit/exit. \nex: set default gps off\n    view|show default gps \n    set default gps\n",
	"help search": "Usage: search <askard|astronomy|oldtech> \nSearch a substring in specific database. \nex: search askard time \n    search astronomy radio \n    search oldtech disk\n",
	"help seek": "Usage: seek <topic> \nReturns if there is any information or topic about the questioned.\n",
	"help sharing about": "Usage: sharing about <tvshow name> \nDisplays a link from the specific content of the tvshow marked in the list on the TV programs page.\nThe link available is automatically copied to the clipboard.\nex: sharing about nautilus\n",
	"help show me": "Usage: show me <star names|constellations|<dangerous|asteroids|objects>|verbs|old tech words|linux commands|quote> \nReturn the values or the data for the required subject.\n",
	"help show info": "Usage: show info or #info \nDisplays comprehensive information about the "+_title_+" application and its current operating environment. \nex: show info \n    #info\n",
	"help solar": "Usage: solar|mppt <monitor|history|last30> \nDisplay the data for the COMx port connect Victron MPPT. \nex: solar monitor \n    solar history\n    solar last30 \n    mppt monitor\n",
	"help star": "Usage <star name> \nDisplays basic information about the star. \nex: Polaris (knowed by north star)\n",
	"help stars from": "Usage: stars from <constelation>\nShow the stars from the inputed constelation. \nex: stars from Taurus \n    stars from andromeda\n",
	"help sunrise time": "Usage: sunrise time \nPresents the time of the morning moment the sun's upper edge becomes visible above the horizon. \nex: sunrise time \n",
	"help sunset time": "Usage: sunset time \nPresents the time precisely when the sun's upper edge fully disappears below the horizon in the evening. \nex: sunset time \n",
	"help talk": "Usage <talk> \nEngages Cybele in conversation. While Cybele doesn't have direct voice output or external neural network access, she can respond to your input. \nex: talk \n    can you speak \n",
	"help today": "Usage <today> \nDisplays all available data for the current day, based on the system date.\n",
	"help today activity": "Usage <today activity> \nDisplays a activity for you based in the actual year season.\n",
	"help today holiday": "Usage: today holiday \nDisplay the current Day Holiday for the default country like special dates if any. \nex: holiday \n",	
	"help topics": "Usage <topics> \nDisplays all the topics i can provide even if some basic information.\n",
	"help types of orbits": "Usage <types of orbits> \nDisplays the orbital regime for each orbit acronym .\n",
	"help view askard": "Usage: view askard <id> \nView the refered askard by the id selected.\nex: view askard 4005\n",
	"help view solar system": "Usage: view solar system \nView a horizontal representation of the solar system.\nex: view solar system\n",
	"help word": "Usage: word \nDisplay a word will interest you (Rich vocabulary).\nex: word\n",
	"help x table": "Usage: x table | multiplication table <number>\nShow the multiplication table for the inputed number \nex: multiplication table 5 \n    x table 5\n",
	"help your version": "Usage your version | what is | #version \nProvides details about the running instance of Cybele. Includes the version, last update date, unique and a note regarding its source code origin. \nex: what is your version \n    your version \n",
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

#-------------------------------------------------
def validate_globals():
	global _poigps_, lat, lon, internals	
	defined_globals = globals()
	missing_vars = []
	for var_name in internals:
		if var_name not in defined_globals:
			missing_vars.append(var_name)
	if missing_vars:
		print_statusline(f"")
		mmodname = f"\n   My code integrity was compromised doing missing some requirements. \n   Missing components: {missing_vars}. Exiting."
		print(f"\n{kolor['RED']} {_spchar_[1:2]}{_title_} \033[0;0m: {mmodname}")
		sys.exit(0)	
	if 'lat' in internals and 'lon' in internals:
		global_lat = defined_globals['lat']
		global_lon = defined_globals['lon']
		is_valid_coord = True
		try:
			lat_val = float(global_lat)
			if not (-90 <= lat_val <= 90):
				is_valid_coord = False
		except (ValueError, TypeError):
			is_valid_coord = False
		try:
			lon_val = float(global_lon)
			if not (-180 <= lon_val <= 180):
				is_valid_coord = False
		except (ValueError, TypeError):
			is_valid_coord = False
		if not is_valid_coord:
			print_statusline(f"")
			coord_error_msg = kdecode(seecoor, shift) + "\n   I cannot execute properly. Exiting."
			print(f"\n{kolor['RED']} {_spchar_[1:2]}{_title_} \033[0;0m: {coord_error_msg}")
			sys.exit(0)
		else:
			_poigps_= [lat,lon,0,1,1]
				
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

#----------------------------------------------------
sqlconn = kdecode(dbconn, shift)
sqlcodb = kdecode(dbconn[0:46] + "{wugtfx_ietvxahewxk}" + dbconn[52:], shift)
for table in etables:
    tables.append(base64.b64decode(table.encode('utf-8')).decode('utf-8'))
	
#----------------------------------------------------
def whatgmt():
	import time
	current_offset_seconds = None
	if time.localtime().tm_isdst == 1 and time.daylight != 0:
		current_offset_seconds = -time.altzone
	else:
		current_offset_seconds = -time.timezone
	tz_offset_hours = current_offset_seconds / 3600

	if tz_offset_hours >= 0:
		gmt_string = f"GMT+{int(tz_offset_hours):2d}"
	else:
		gmt_string = f"GMT-{abs(int(tz_offset_hours)):2d}"
	return gmt_string.replace(" ","")

#------------------------------------------------------------
def internet_onoff():
	try:
		socket.setdefaulttimeout(1)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("8.8.8.8", 53))
		s.close()
		return True
	except OSError:
		pass

#------------------------------------------------------------------
def get_default_port():
    system = platform.system().lower()
    mapping = {
        'windows': _serial_[0],
        'linux': _serial_[1],
        'darwin': _serial_[2]
    }  
    return mapping.get(system, None)

#--------------------------------------------------------
def fetch_fromdbfile(db_filename, table_name, column_name):
	global dblrconn, dbmsgbl
	conn = None		
	if internet_onoff() == True:
		if os.path.isfile(db_filename) == True:
			conn = sqlite3.connect(db_filename)
			dblrconn= "offline [database files]"
			dbmsgbl = f"Connected via local database {_spchar_[7:8]}"
		else:
			max_attempts = 5
			for attempt in range(1, max_attempts + 1):
				try:
					conn = sqlitecloud.connect(sqlconn)
					dblrconn="online [sqlitecloud]"
					dbmsgbl = f"Connecting with remote database {_spchar_[7:8]}"
					break
				except ValueError as e:
					print_statusline(f"")
					modname = f"\n    Unexpected invalid value encountered: {e}\n"
					print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {modname}")
					exit(0)	
				except sqlitecloud.exceptions.SQLiteCloudException as e:
					if attempt < max_attempts:
						sleep(1)
					else:
						print_statusline(f"")
						modname = random.choice(messages['db_pause_msg']) + f"\n    I made {max_attempts} attempts and {attempt} failed. Give another try in a while."
						print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {modname}")
						exit(0)
	else:
		if os.path.isfile(db_filename) == True:
			conn = sqlite3.connect(db_filename)
			dblrconn="offline [database files]"
			dbmsgbl = f"Connected via local database {_spchar_[7:8]}"
		else:
			print_statusline(f"")
			modname = "The " + db_filename.upper() + " database file is missing, and with no internet the online database is inaccessible. \n   To work offline use the option <offline mode on> in the main cybele prompt. \n   I cannot execute properly. Exiting."
			print("\n\033[1;31m "+ _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			exit(0)

	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT {column_name} FROM {table_name}")
		result = [row[0] for row in cursor.fetchall()]
		return result
	except Exception as e:
		print_statusline(f"")
		modname = f"\n   An unexpected error occurred: {e}"
		print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {modname}")
		exit(0)
	except sqlite3.Error as e:
		return []
	finally:
		if conn:
			conn.close()
			
#------------------------------------------------------------
def dbfetch(db_filename, record, table_name, search_column, column_to_fetch):	
	global dblrconn, dbmsgbl
	conn = None
	if internet_onoff() == True:
		if os.path.isfile (db_filename) == True :
			conn = sqlite3.connect(db_filename)
			dblrconn="offline [database files]"
			dbmsgbl = f"Connected via local database {_spchar_[7:8]}"
		else:
			conn = sqlitecloud.connect(sqlconn)
			dblrconn="online [sqlitecloud]"
			dbmsgbl = f"Connecting with remote database {_spchar_[7:8]}"
	else:
		if os.path.isfile (db_filename) == True:
			conn = sqlite3.connect(db_filename)
			dblrconn="offline [database files]"
			dbmsgbl = f"Connected via local database {_spchar_[7:8]}"
		else:
			modname = "The " + db_filename.upper() + " database file is missing, and with no internet the online database is inaccessible. \n   To work offline use the option <offline mode on> in the main cybele prompt. \n   I cannot execute properly. Exiting."
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
	global dbmsgbl
	db_filename = 'cybele.db'
	missing_tables = []
	github_file_url = kdecode(GITHUB, shift)
	attempt = 0
	max_attempts = 0
	conn = None
	cur = None
	
	if internet_onoff() == True:
		if os.path.isfile (db_filename) == True :
			conn = sqlite3.connect(db_filename)
			dbmsgbl = f"Connected via local database {_spchar_[7:8]}"
		else:
			try:
				conn = sqlitecloud.connect(sqlconn)
				dbmsgbl = f"Connecting with remote database {_spchar_[7:8]}"
			except ValueError as e:
				print_statusline(f"")
				modname = f"\n    An unexpected error occurred: {e}"
				print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {modname}")
				exit(0)
			except sqlitecloud.exceptions.SQLiteCloudException as e:
				print_statusline(f"")
				modname = f"\n    An unexpected error occurred: {e}"
				print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {modname}")
				exit(0)
			except sqlitecloud.exceptions.SQLiteCloudError as e:
				print_statusline(f"")
				if "Your free node has been paused due to inactivity." in str(e):
					modname = (
						f" {random.choice(messages['db_pause_msg'])} \n"
						f"   Either there is an upgrade going on right now or the database has migrated to another platform.\n"
						f"   Please try again in a few minutes or email the author asking to wake her up.\n"
					)	
					print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {modname}")
					exit(0)
				else:
					modname = f"\n    An unexpected database error occurred: {e}"
					print(f"\n\033[1;31m {_spchar_[1:2]}{_title_}\033[0;0m: {modname}")
					exit(0)
	else:
		if os.path.isfile (db_filename) == True :
			conn = sqlite3.connect(db_filename)
			dbmsgbl = f"Connected via local database {_spchar_[7:8]}"
		else:
			print_statusline(f"")
			modname = "The " + db_filename.upper() + " database file is missing, and with no internet the online database is inaccessible. \n   To work offline use the option <offline mode on> in the main cybele prompt. \n   I cannot execute properly. Exiting."
			print("\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			exit(0)
		
	try:
		cur = conn.cursor()
		cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
		existing_tables = [row[0] for row in cur.fetchall()]
		for table_name in tables_names:
			if table_name not in existing_tables:
				missing_tables.append(table_name)

		if missing_tables:
			print_statusline(f"")
			modname = f"The database file dont satisfy all my requirements, {len(missing_tables)} missing!\n   Please update from github via addr {github_file_url}\n   I cannot execute properly. Exiting.\n"
			print("\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			return False
		else:
			return True
		
	except sqlite3.Error as e:
		print_statusline(f"")
		modname = f"Database query error {e} \n   I cannot execute properly. Exiting."
		print("\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
		return False
	except Exception as e:
		print_statusline(f"")
		modname = f"An unexpected error occurred: {e}\n   I cannot execute properly. Exiting."
		print("\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
		return False
	finally:
		if cur:
			cur.close()
		if conn:
			conn.close()

#------------------------------------------------------------
def download_and_convert(connection_string: str, local_db_filename: str):

	cloud_conn = None
	local_conn = None
	try:
		#print("")
		print_statusline("Connecting to SQLite Cloud database...")
		cloud_conn = sqlitecloud.connect(connection_string)
		cloud_cursor = cloud_conn.cursor()
		print_statusline(f"Creating my local database '{local_db_filename}'...")
		local_conn = sqlite3.connect(local_db_filename)
		local_cursor = local_conn.cursor()
		print_statusline("Fetching table schema from the cloud database...")
		cloud_cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
		tables_info = cloud_cursor.fetchall()
		total_tables = len(tables_info)
		for i, (table_name, create_sql) in enumerate(tables_info):
			progress = (i + 1) / total_tables * 100
			bar_length = 20
			filled_length = int(bar_length * progress // 100)
			bar = '█' * filled_length + '░' * (bar_length - filled_length)
			print_statusline(f"Getting ready for offline mode! I'm currently syncing my data [{bar}] {progress:.1f}% ...")
			local_cursor.execute(f"DROP TABLE IF EXISTS \"{table_name}\";")
			local_cursor.execute(create_sql)
			cloud_cursor.execute(f"SELECT * FROM {table_name};")
			rows = cloud_cursor.fetchall()
			columns = [col[0] for col in cloud_cursor.description]
			placeholders = ', '.join(['?'] * len(columns))
			insert_sql = f"INSERT INTO \"{table_name}\" ({', '.join([f'"{c}"' for c in columns])}) VALUES({placeholders});"
			if rows:
				local_cursor.executemany(insert_sql, rows)
    
		local_conn.commit()
		print_statusline(f"I'm now able to work in offline mode! 🚀. Restart {_title_}")
		print("\n")
		
	except sqlitecloud.SQLiteCloudException as e:
		print(f"\nAn SQLite Cloud error occurred: {e}", file=sys.stderr)
	except sqlite3.Error as e:
		print(f"\nAn SQLite error occurred: {e}", file=sys.stderr)
	except Exception as e:
		print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
	finally:
		if cloud_conn:
			cloud_conn.close()
		if local_conn:
			local_conn.close()

#------------------------------------------------------------
def delete_cybeledb():
	file_name = _title_.lower()+".db"
	if os.path.exists(file_name):
		try:
			os.remove(file_name)
			print(f"My Database '{file_name}' was deleted successfully! ✅")
		except OSError as e:
			print(f"Error deleting my database '{file_name}': {e} ❌")
	else:
		print(f"My offline database '{file_name}' does not exist. No action taken. 🤷‍♂️")
	print("")

#------------------------------------------------------------
def parse_date_string(date_str):
	try:
		month_str, day_str = date_str.split('/')
		month = int(month_str)
		day = int(day_str)
		return (month, day)
	except (ValueError, IndexError):
		return None

#------------------------------------------------------------
def make_intextdb():
	global midbcounter, ncountries, constellations_dict, special_dates_dict, idcode, knowledge, asteroids_list, cneos_list, \
			stars_dict, constellations_abbr, climate_dictionary, linux_commands, core, \
			periodic_elements, periodic_abbr, questions, answers, help, messages, tables, _spchar_, my_library

	if not check_tables(tables):
		sys.exit(0)

	message = random.choice(messages['loadings'])
	print_statusline(f"{message} {_spchar_[7:8]}")

	try:
		idvdb = ""
		idcode = fetch_fromdbfile("cybele.db", "config", "code")[0]
		idvdb = fetch_fromdbfile("cybele.db", "config", "id")[0]
		_revise_idvdb_ = _revise_.replace('.', '')
		if int(idvdb) != int(_revise_idvdb_[:-4] + _revise_idvdb_[-2:]):
			print_statusline(f"")
			print(f" {kolor['RED']}WARNING!{kolor['OFF']} The essential architectural evolution needs that this version be updated. \n I strongly advise a {_title_} upgrade via github to maintain funcionaly and compatibility. \n")
			sys.exit(0)
		del idvdb
		
		core["astronomy glossary"] = list(fetch_fromdbfile("cybele.db", "astronomy_glossary", "glossary"))

		star_data = zip(
			fetch_fromdbfile("cybele.db", "stars", "star_name"),
			fetch_fromdbfile("cybele.db", "stars", "hr_number"),
			fetch_fromdbfile("cybele.db", "stars", "constelation")
		)
		for name, hr, const in star_data:
			stars_dict[name] = [hr, const]
		core["star name"] = [key.lower() for key in stars_dict.keys()]

		constellation_data = zip(
			fetch_fromdbfile("cybele.db", "constelations", "constelation"),
			fetch_fromdbfile("cybele.db", "constelations", "meaning"),
			fetch_fromdbfile("cybele.db", "constelations", "abbr")
		)
		for constelation, meaning, abbr in constellation_data:
			constellations_dict[constelation] = (meaning, abbr)
			constellations_abbr[abbr] = constelation
		core["constelattion"] = list(constellations_dict.keys())

		asteroid_data = zip(
			fetch_fromdbfile("cybele.db", "asteroids", "asteroid_name"),
			fetch_fromdbfile("cybele.db", "asteroids", "type"),
			fetch_fromdbfile("cybele.db", "asteroids", "mean_diameter"),
			fetch_fromdbfile("cybele.db", "asteroids", "rotation_period"),
			fetch_fromdbfile("cybele.db", "asteroids", "albedo"),
			fetch_fromdbfile("cybele.db", "asteroids", "description")
		)
		for name, _type, diameter, rotation, albedo, desc in asteroid_data:
			asteroids_list[name] = {
				"type": _type,
				"mean_diameter": diameter,
				"rotation_period": rotation,
				"albedo": albedo,
				"description": desc,
			}
		core["asteroid"] = list(asteroids_list.keys())
		core["dangerous asteroids"] = [name for name, data in asteroids_list.items() if data['type'] == "dangerous asteroid"]

		cneos_data = zip(
			fetch_fromdbfile("cybele.db", "cneos", "object_designation"),
			fetch_fromdbfile("cybele.db", "cneos", "year_range"),
			fetch_fromdbfile("cybele.db", "cneos", "impact_probability"),
			fetch_fromdbfile("cybele.db", "cneos", "vinfinity_kms"),
			fetch_fromdbfile("cybele.db", "cneos", "estimated_diameter_km")
		)
		for obj, year, imp, dkm, dia in cneos_data:
			cneos_list[obj.lower()] = {
				"year": year,
				"impact": imp,
				"kms": dkm,
				"diameter": dia,
			}
		core['cneos'] = list(cneos_list.keys())

		country_data = zip(
			fetch_fromdbfile("cybele.db", "countries", "country"),
			fetch_fromdbfile("cybele.db", "countries", "capital"),
			fetch_fromdbfile("cybele.db", "countries", "population"),
			fetch_fromdbfile("cybele.db", "countries", "alpha_2")
		)
		for country, capital, population, alpha_2 in country_data:
			ncountries[country.lower()] = {"capital": capital, "population": population, "alpha2": alpha_2}
		core['country'] = list(ncountries.keys())
		core['capital'] = [country["capital"] for country in ncountries.values()]

		climate_terms = fetch_fromdbfile("cybele.db", "climate_dict", "climate_term")
		climate_designations = fetch_fromdbfile("cybele.db", "climate_dict", "designation")
		climate_dictionary.update({term: desig for term, desig in zip(climate_terms, climate_designations)})
		core["climate dictionary term"] = list(climate_dictionary.keys())
		core["climate dictionary"] = list(climate_dictionary.values())

		core["word meaning"] = list(fetch_fromdbfile("cybele.db", "meanings", "term"))

		core["qa-astro"] = list(fetch_fromdbfile("cybele.db", "qa_astro", "question"))

		linux_cmd_data = zip(
			fetch_fromdbfile("cybele.db", "linux_commands", "cmd_name"),
			fetch_fromdbfile("cybele.db", "linux_commands", "syntax"),
			fetch_fromdbfile("cybele.db", "linux_commands", "explanation"),
			fetch_fromdbfile("cybele.db", "linux_commands", "examples")
		)
		for cmd_name, syntax, explanation, examples_str in linux_cmd_data:
			if cmd_name not in [key[5:] for key in help.keys()]:
				examples = examples_str.split(';') if examples_str else []
				linux_commands[cmd_name] = {
					"syntax": syntax,
					"explanation": explanation,
					"examples": examples
				}
		core["linuxcmd"] = list(linux_commands.keys())
		core['help'] = list(help.keys())

		core["old_tech_term"] = fetch_fromdbfile("cybele.db", "oldtech", "oldterm")

		special_dates_data = zip(
			fetch_fromdbfile("cybele.db", "special_dates", "sdate"),
			fetch_fromdbfile("cybele.db", "special_dates", "event")
		)
		for date_str, event_desc in special_dates_data:
			parsed_date_tuple = parse_date_string(date_str)
			if parsed_date_tuple:
				special_dates_dict[parsed_date_tuple] = event_desc
		midbcounter += len(special_dates_dict)

		knowledge["adjective"] = list(fetch_fromdbfile("cybele.db", "adjectivedb", "adjective"))
		knowledge["adverb"] = list(fetch_fromdbfile("cybele.db", "adverbdb", "adverb"))
		knowledge["conjunction"] = list(fetch_fromdbfile("cybele.db", "conjunctiondb", "conjunction"))
		knowledge["preposition"] = list(fetch_fromdbfile("cybele.db", "prepositiondb", "preposition"))
		knowledge["verb_base"] = list(fetch_fromdbfile("cybele.db", "verb_basedb", "verb_base"))
		knowledge["verb_past_participle"] = list(fetch_fromdbfile("cybele.db", "verb_past_db", "verb_past_participle"))
		knowledge["noun"] = list(fetch_fromdbfile("cybele.db", "nouns", "noun"))

		core["element symbol"] = [key.lower() for key in periodic_elements.keys()]
		core["element abbr"] = [key.lower() for key in periodic_abbr.keys()]
		
		my_library = list(fetch_fromdbfile("cybele.db", "tvshows", "library"))

		midbcounter = 0 
		for category_list in knowledge.values():
			midbcounter += len(category_list)
		midbcounter += len(questions) + len(answers)
		midbcounter += len(my_library)
		for key in core:
			if isinstance(core[key], list):
				midbcounter += len(core[key])
			elif isinstance(core[key], dict):
				midbcounter += len(core[key])

	except Exception as e:
		print(f"{random.choice(messages['trouble_short'])}, {kolor['RED']}FATAL ERROR{kolor['OFF']} during database loading: {e}") 
		sys.exit(1)
		
#----------------------------------------------------------------------
questions = [
	"Ola",
	"Como te chamas?",
	"Tudo bem?",
	"Hello",
	"What is your name?",
	"What is the meaning of your name?",
	"Who built the pyramids?",
	"Clock time",
	"What time it is?",
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
	"Hello",
	"Hi",
	"Whats on your mind today?",
	"The world",
	"Life",
	"Chat"
]
#------------------------------------------------
answers = [
	"Olá! Sou " + _title_ + ". De momento, não falo português de Portugal. No entanto, estou aqui para ajudar! Pode digitar 'help' ou 'what can you do' para saber mais.",
	"Chamo-me " + _title_ + " e lamento ter que informar que não falo pt-PT, nem ainda funciono com a tradução instantânea.",
	"Melhor impossível! Mas não me venhas com truques hoje, hmm?",
	"Hello. Ask away. No formalities. If i have the knowledge i will anwser.",
	"My name is "+ _title_+".",
	"The name Cybele essentially means 'Great Mother of the Gods' or 'Mother Goddess,' signifying her role as a powerful deity of the earth, nature, with some interpretations also linking her to the wisdom of a 'Prophet.'",
	"The exact builders of the pyramids are still debated...",
	"The current time in the system clock is "+datetime.now().strftime("%H:%M"),
	"The current time is "+datetime.now().strftime("%H:%M"),
	"Unlike LLMs who can't, my core functionality can be replicated, but my responses may vary based on training data.",
	"An electromagnetic wave produced by the oscillation of electricity in a conductor (as a radio antenna) and of a length ranging from a few millimeters to many kilometers. There is 7 types of waves are as follows: Radio Waves, Microwaves, InfraRED, Visible, Ultraviolet, X-Ray, Gamma Rays. \nRadio waves have the longest wavelength and small frequency while the gamma rays have shortest wavelength and high frequency.",
	"The numbers are in decimal degrees format and range are from -90 to 90 for latitude using + for North and - for South and -180 to 180 for longitude using + for East and - for West.",
	"Latitudes are horizontal lines that measure distance north or south of the equator. Longitudes are vertical lines that measure east or west of the meridian in GREENwich, England. Together, latitude and longitude enable cartographers, geographers and others to locate points or places on the globe.",
	"If you're using a map with longitude and latitude lines, stick a pin where you're located. Then, draw a straight horizontal line from your point to the east or west edge of the map. Then, draw a vertical line from your location to the north or south edge of the map. Put together the 2 coordinates to find your position.",
	"Yes. At this time and with my core code i can be 98.0% offline resourceful.",
	"The 1990's was a decade of great cultural change, with the rise of hip hop, grunge, and teen pop. The were times who left a lasting mark on the world, and we still can feel its influence today.",
	"The 90's were a decade of great cultural change, with the rise of hip hop, grunge, and teen pop. The were times who left a lasting mark on the world, and we still can feel its influence today.",
	"You wish! Just type quit it's easier.",
	"Yes. Type <gps to distance> and i will prompt for the data i need.",
	"Yes. I can be costumized. To that contact my creator or find more information about chat bot.",
	"Yes. I can be personalized. To that contact my creator or find more information about chat bot.",
	"Well i dont have age persay, i was officially actived " + str(days_till_today.days) + " days ago and my last updated was in " + _revise_ + ". Do the math!",
	"Well i dont have age persay, i was officially actived " + str(days_till_today.days) + " days ago and my last updated was in " + _revise_ + ". Do the math!",
	"Goodbye.",
	"Really.",
	"No problem. Glad i could be of assistance.",
	"Thank you! I appreciate the gesture. I will enjoy my coffee and hot.",
	"Thank you! I appreciate the gesture. I will enjoy my coffee and hot.",
	"Hi! What's on your mind?",
	"Hello! What's on your mind?",
	"I'm glad you're asking.\nI'm thinking about how lucky I am to be able to help people with my answers.",
	"The world is a beautiful and complex place.\nIt is full of amazing things, from the tallest mountains to the deepest oceans.",
	"Life is a journey, a mystery, and a gift. It is full of ups and downs, challenges and triumphs.",
	"Hello! I'm here to help. You can type 'help', search for an astronomy term, or explore an old term. \nTo see more options, just type 'what can you do'.\n"
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
	"show me old tech words","show me old tech terms","show me star names","show me meaning terms","show me meaning words","show me linux commands",
	"math game","reset my score","show my score","morse <word/phrase>","demorse <word/phrase>","when was elysia created",
	"play game constelattions","play game capitals","when did elysia went online","difference from <date>","cybele uptime",
	"current system uptime","display uptime"
]
#----------------------------------------------------------
maincommands = [
	"bye","exit","quit","do you know anything about","know anything on","find","seek","what can i ask you","how many linux commands you know",
	"what can you anwser","what do you know","what can you do","what do you do","what you can do","adelino quote","what is",
	"do you know what is","meaning of","show me","tell me","list me","meaning term","meaning words","meaning terms","constellations",
	"show me some linux commands","astronomy questions","questions of astronomy","days till","days for","days to","trails",
	"difference from","age calc","what do you know about","astronomy","constelations","universe","can you","elysia created",
	"visualize periodic table","show periodic table","distance from","planets of the solar system","planets of solar system",
	"solar system planets order","solar system planets","types of orbits","orbital regimes","year seasons","seasons of the year",
	"capital","capital of","value of pi","pi value","pi","s.o","operating system","system","can you help me","can you help",
	"help","help me","time","what time it is","clock time","happy birthday cybele","cybele happy birthday","happy birthday",
	"merry christmas","i wish you a merry christmas","happy valentines","happy new year","what is your version",
	"#version","convert gps to distance","gps to distance","harvesine","harvesine formula","sunset time","sunrise time","set default gps",
	"diagnostics","show core","#core","date","today","today is","what day is today","what is the date","what is today","convert",
	"how many weeks have a year","year weeks","week","week number","what number is this week","what is this week number","last update",
	"yes","search askard","view askard","list askard","search astronomy","search oldtech","list oldtech","limits","protect image",
	"current century","population","where is the iss","where is zarya","people in space","what is he watching","what are you watching",
	"fav tvshows","favorite tvshows","do you speak","do you talk","say something","make a sentence","play capitals","play countries",
	"play math","play constellations","play elements","game capitals","game countries","game math","game constellations","game elements",
	"show my score","reset my score","reset score","infostar","today activity","weather","about you","presence","presence services",
	"presence online","phonetic","morse","demorse","yoda say","genpwd","multiplication table","x table","licence","cybele licence",
	"when elysia was created","elysia created","when elysia went online","cybele uptime","stars from","list stars","list constellations",
	"protect image","set default country","default country off","list holidays","actual country","view solar system","check update","solar",
	"last update","conjugate","fun fact","fast fact","nice thing","clear screen","cls","how many capitals do you know","offline mode on","mppt",
	"offline mode off","how many countries do you know","show topics","show me your topics","show topic's","show me your topic's","topics","topic's"
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
if _cybid_ == True:
	help.update({"help list extcom": "Usage: <list extcom or extcom> \nDisplays all the commands the Cybele extention can provide.\nex: list extcom\n    extcom\n"})
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

		moon_phase_emoji = ["🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘","🌑"]
		if phase_angle < 90:
			return moon_phase_emoji[7] + " Waxing Crescent"
		elif phase_angle < 180:
			return moon_phase_emoji[6] + " First Quarter"
		elif phase_angle < 270:
			return moon_phase_emoji[3] + " Waxing Gibbous"
		else:
			return moon_phase_emoji[4] + " Full Moon"

#---------------------------------------------------
class VictronMonitor:
	def __init__(self, porta=get_default_port(), baudrate=19200):
		self.porta = porta
		self.baudrate = baudrate
		# Estrutura de dados equivalente ao MpptData em Rust
		self.data = {
			'V': 0, 'VPV': 0, 'PPV': 0, 'I': 0,
			'H19': 0, 'H21': 0, 'H17': 0
		}

	def monitorizacao_ativa(self):
		#print("\033[H\033[J", end="")
		old_settings = termios.tcgetattr(sys.stdin)

		try:
			tty.setcbreak(sys.stdin.fileno())
			with serial.Serial(self.porta, self.baudrate, timeout=0.1) as ser:
				print("\r\033[92m>>> ACTIVE MONITORING (press Ctrl+C to exit) <<<\033[0m")
				while True:
					dr, _, _ = select.select([sys.stdin], [], [], 0)
					if dr:
						sys.stdin.read(1)
						print(f"\n{kolor['CYAN']}Stopped instantly!{kolor['OFF']}")
						break
					
					linha = ser.readline().decode('utf-8', errors='ignore').strip()

					if not linha:
						continue

					if linha.startswith("Checksum"):
						self._exibir_dados()
						self._salvar_db()
						continue

					partes = linha.split('\t')
					if len(partes) == 2:
						chave, valor = partes[0].strip(), partes[1].strip()
						if chave in self.data:
							try:
								self.data[chave] = int(valor)
							except ValueError:
								pass

		except (serial.SerialException) as e:
			print("\n")
		finally:
			termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

	def _exibir_dados(self):
		agora = datetime.now().strftime("%H:%M:%S")
		# Formatação idêntica à usada no VRust
		print(
			f"\r[{agora}] Batery: {self.data['V']/1000:.2f}V | "
			f"PV: {self.data['VPV']/1000:.2f}V | "
			f"PWR: {self.data['PPV']}W | "
			f"Total income: {self.data['H19']/100:.2f}kWh    ",
			end="", flush=True
		)

	def calcular_checksum_hex(self, comando):
		# Checksum para comandos em modo HEX (VE.Direct)
		soma = 0
		# Remove o ':' inicial e processa os pares de bytes
		payload = comando[1:]
		for i in range(0, len(payload), 2):
			soma += int(payload[i:i+2], 16)
        
		# O checksum é o valor que, somado à 'soma', resulta em 0x55 (modulo 256)
		check = (0x55 - soma) & 0xFF
		return f"{check:02X}"

	def get_historico_dia(self, dia=1):
		registo_invertido = "8DED"
		comando_base = f":8{registo_invertido}00"
		checksum = self.calcular_checksum_hex(comando_base)
		comando_final = f"{comando_base}{checksum}\n"

		try:
			with serial.Serial(_portac_, 19200, timeout=1.5) as ser:
				ser.reset_input_buffer()
				ser.reset_output_buffer()
				ser.setDTR(True) 
				
				sleep(0.5)
				ser.write(comando_final.encode())
                
				for _ in range(15):
					linha = ser.readline().decode('ascii', errors='ignore').strip()
					if linha.startswith(":7"):
						return f"{kolor['BOLD_GREEN']}HISTÓRICO ENCONTRADO:{kolor['OFF']} {linha}\n"
					elif linha.startswith(":4"):
						return f"{kolor['BOLD_RED']}AVISO:{kolor['OFF']} O MPPT rejeitou o registo {registo_invertido}.\n"
                
			return f"{kolor['BOLD_YELLOW']}TIMEOUT:{kolor['OFF']} Sem resposta HEX.\n"
		except Exception as e:
			error_msg = str(e).split(':')[0]
			return f"{kolor['BOLD_RED']}Erro:{kolor['OFF']} {error_msg} \n"

	def importar_30_dias(self):
		# Loop de busca dos últimos 30 dias e preparar para a BD"""
		print(f"{kolor['BOLD_BLUE']}A descarregar histórico de 30 dias para a Cybele...{kolor['OFF']}")
		for d in range(1, 31):
			dados = self.get_historico_dia(d)
			print(dados)
			sleep(0.1) # Pausa control saturação do bus
			
	def _salvar_db(self):
		# Aqui lógica de base de dados
		pass

#---------------------------------------------------
def print_aligned(items, items_per_line, column_width):
	for i, item in enumerate(items):
		print(f"{item:<{column_width}.{column_width}}", end="")
		if (i + 1) % items_per_line == 0:
			print()
	if len(items) % items_per_line != 0:
		print()

#---------------------------------------------------
# pre harvesine / pregpsconvert
def pregpsconvert():

	print(f"\n{_spchar_[1:2]}{kolor['BOLD_YELLOW']}Convert GPS to distance {kolor['OFF']}")
	while True:
		if _poigps_[4] == 0:
			try:
				print(f"{_spchar_[1:2]}{kolor['CYAN']} Point of origin {kolor['OFF']}")
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
			print(f"{_spchar_[1:2]}{kolor['BOLD_MAGENTA']}[Assumning default gps values as Origin] {kolor['OFF']}")
			latgps = int(_poigps_[0])
			longps = int(_poigps_[1])

		try:
			print(f"{_spchar_[1:2]}{kolor['CYAN']} Point of destination {kolor['OFF']}")
			lat2gps = float(input('   Latitude coordinates (ex 35.8806): '))
			if lat2gps > 90 or lat2gps < -90:
				print("\nLatitude value degrees must be between -90 and 90.\n")
				continue
			lon2gps = float(input('  Longitude coordinates (ex 76.5151): '))
			if lon2gps > 180 or lon2gps < -180:
				print("Longitude value degrees must be between -180 and 180.\n")
				continue
		except ValueError:
			print("Value not recognized like latitude or longitude gps coordinates!\n")
			break

		distancekm = distance_gps(latgps, longps, lat2gps, lon2gps) / 1000
		if int(distancekm) > 0 or int(distancekm) < 1000000:	
			print("")
			print(f"{kolor['RED']}{_spchar_[1:2]} {kolor['BOLD_WHITE']} The distance between the two points provided is {str('{:,.1f}'.format(distancekm))} kilometers.{kolor['OFF']}")
			print(f"  ( approximately ≈ {str( convert_to_words(int(distancekm) + 1) )} kilometers )\n")
			return False
		else:
			print(f"{kolor['RED']}{_spchar_[1:2]}{kolor['OFF']} {random.choice(messages['trouble_short'])} My code had some problems handling the distance result {str(distancekm)}") 

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
	print(kolor['OFF'])

	art_data = {
		'art_cybele': {'art': art_cybele, 'exclude_colors': ['BOLD_BLACK', 'DARK_BLACK', 'DIM_BLACK', 'BLACK'],
			'fallback_colors': ['RED', 'DIM_RED', 'BOLD_RED'], 'special_line': 5, 'special_suffix': art_byas,
			'special_suffix_color': 'BOLD_YELLOW'},
		'art_world': {'art': art_world, 'color': 'BLUE'},
		'art_py': {'art': art_py, 'color': 'GREEN'}
	}

	if artname not in art_data:
		print(f"Error: Art '{artname}' not found in my code to handle'it. Fix'it!")
		print(kolor['OFF'])
		return

	config = art_data[artname]
	art = config['art']
	if 'color' in config:
		art_color = kolor[config['color']]
	else:
		available_colors = [c for c in list(kolor.keys()) if c not in config.get('exclude_colors', [])]
		if not available_colors:
			art_color_name = random.choice(config['fallback_colors'])
		else:
			art_color_name = random.choice(available_colors)
		art_color = kolor[art_color_name]

	for i, line_bytes in enumerate(art):
		res = ''.join(map(chr, line_bytes))
		if artname == 'art_cybele' and i == config['special_line']:
			suffix_res =''.join(map(chr, config['special_suffix']))
			start_of_line = res[:11]
			new_content = kolor['DIM_YELLOW'] + dblrconn[0:7] + kolor['OFF']
			new_content_len = len(new_content) 
			final_line = art_color + start_of_line + new_content + art_color + res[18:-2]
			print(final_line + kolor[config['special_suffix_color']] + suffix_res)
		else:
			print(art_color + res)
	print(kolor['OFF'])

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
		result = "a leap year".format(year)
	elif (year % 4 ==0) and (year % 100 != 0):
		result = "a leap year".format(year)
	else:
		result = "not a leap year".format(year)
	return result

#---------------------------------------------------------------------------
#-------------------------------------------------------------------
# cybele Core and sub-cores
#-------------------------------------------------------------------
#---------------------------------------------------------------------------
def get_question():
	qt = input( _title_ + "? 〉")
	if qt.isupper():
		print("Can you please stop shouting! \nIf you're writing, unless your keyboard has a problem, I understand very well.")
		question = qt.lower()
	try:
		if str(qt):
			return qt.lower()
	except ValueError:
		return qt.lower()
	return qt.lower()

def find_answer(question,whatlist):
	sugestion_color = random.choice(['DARK_YELLOW','DARK_GREEN','DARK_CYAN'])
	pontuation = [".",",","!","?"]
	outoptions = ["Perhaps you meant: ","It looks like you meant: ","Is this what you had in mind: ","Oops! Did you mean: ","Looking for: "]
	for p in range(len(pontuation)):
		question = question.replace(pontuation[p],"")
	for index, value in enumerate(whatlist):
		if question.lower() == value.lower() or question.lower() == value.lower().replace("?",""):
			return answers[index]+"\n"
	sayhi = core.get("greatings", [])
	dict_climate = core.get("climate dictionary", [])
	dict_astro_keys = ["astronomy glossary", "constelattion", "planet", "qa-astro", "primary moon phase", "secondary moon phase"]
	dict_astro = [item for key in dict_astro_keys if key in core for item in core[key]]
	others_keys = ["country", "capital", "months", "seasons", "old_tech_term", "word meaning", "help", "share", "linuxcmd",
					"time_query","season_query","asking for country details","asking for talking","asking for a word","python art",
					"sayconvert"]
	others = [item for key in others_keys if key in core for item in core[key]]
	alldict = others + questions + sayhi + dict_climate + dict_astro + maincommands
	is_correct, suggestions = spell_check(question, alldict)
	if suggestions:
		output_string = random.choice(outoptions)
	else:
		output_string = ""
	for i, suggestion in enumerate(suggestions):
		if i < 3:
			output_bycyid = ""+kolor[sugestion_color]+suggestion.capitalize() + kolor['OFF'] + " or "
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

#------------------------------------------------------------
def pwdgen(num_passwords, length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for i in range(length))
        passwords.append(password)
    return passwords

#------------------------------------------------------------
def generate_random_questions(question_sources: list, num_questions: int) -> list:
    all_raw_questions = []
    for source_list in question_sources:
        all_raw_questions.extend(source_list)
    unique_questions = list(set(all_raw_questions))
    random.shuffle(unique_questions)
    questions_to_return = min(num_questions, len(unique_questions))
    selected_questions = []
    for _ in range(questions_to_return):
        selected_questions.append(unique_questions.pop().capitalize())
    return selected_questions
	
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

#------------------------------------------------------------
def get_display_value(value, suffix="", precision=None, replace_hyphen=False):
	if value is None or (isinstance(value, str) and not value.strip()):
		return "N/A"
	if isinstance(value, (float, int)) and precision is not None:
		return f"{value:.{precision}f}{suffix}"
	if replace_hyphen and isinstance(value, str):
		return value.replace('-', ' - ')
	return f"{value}{suffix}"
	
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
				hemisphere = 'Northern Hemisphere' if lat >= 0 else 'South Hemisphere'
				allyearseasons = '' + ', '.join(core[list_name]) + ''
				current_season = word
				current_season_index = core['seasons'].index(current_season.lower())
				next_season_index = (current_season_index + 1) % len(core['seasons'])
				next_season = core['seasons'][next_season_index]
				print(f"Is one of the four seasons ({allyearseasons.title()}) of the year while the {next_season.title()} approach's.")
				print(f"(Based on current month ({datetime.now().strftime('%B')}) and {hemisphere}, the current season is {get_the_season()[0].title()})\n")

			elif list_name == 'spring' or list_name == 'summer' or list_name == 'autumn' or list_name == 'winter':
				month_number = core['months'].index(word) + 1
				hemisphere = 'Northern Hemisphere' if lat >= 0 else 'South Hemisphere'
				leap_year = leapyear()
				print (f"{word.capitalize()} is the {get_ordinal_position(month_number)} month of the year ({leap_year} {date.today().year}) and {list_name.capitalize()} season in the {hemisphere}.\n")
				
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
				print ("")

			elif list_name == 'python art':
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
				if asteroid_info['type'].lower() == "dangerous asteroid":
					dangerast = f"{kolor['BOLD_RED']}{asteroid_info['type'].upper()}{kolor['OFF']}"
				else:
					dangerast = f"{kolor['BOLD_WHITE']}{asteroid_info['type']}{kolor['OFF']}"
				print (f"\n [ {kolor['YELLOW']}{list_name.upper()} {word}{kolor['OFF']} | {dangerast} {kolor['OFF']}]")
				print(f"   Diameter: {asteroid_info['mean_diameter'].replace('.', ',')} km")
				print(f" Rot.Period: {asteroid_info['rotation_period']} hours")
				print(f"     Albedo: {asteroid_info['albedo']}")
				print(f"    Details: {asteroid_info['description']}\n")
			
			elif list_name == "cneos":
				object_key = word
				object_details = cneos_list[object_key]
				print (f"\n [ {kolor['BOLD_RED']}{object_key.upper()}{kolor['OFF']} | {kolor['YELLOW']}Dangerous Objects{kolor['OFF']}, data by NASA JPL CNEOS ]")
				val = len(object_key.upper())
				print (f"{' '*val:>{val+6}}{_spchar_[10:11]} https://cneos.jpl.nasa.gov/ca/ \n")
				diameter_value = object_details.get('diameter')
				print(f"{'Diameter:':>15} {get_display_value(diameter_value, ' Km')}")
				impact_value = object_details.get('impact')
				impact_display = "N/A"
				if impact_value is not None and (isinstance(impact_value, (float, int)) or (isinstance(impact_value, str) and impact_value.strip())):
					try:
						impact_display = f"{float(impact_value) * 100:.4f} %"
					except ValueError: # In case 'impact' is a non-numeric string
						impact_display = "N/A"
				print(f"{'Impact Prob:':>15} {impact_display}")
				year_value = object_details.get('year')
				print(f"{'Year range:':>15} {get_display_value(year_value, replace_hyphen=True)}")
				kms_value = object_details.get('kms')
				print(f"{'V infinity:':>15} {get_display_value(kms_value, ' Km/s', precision=2)}\n")
				
				
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
				
			elif list_name == "time_query":
				print ("The current time is "+datetime.now().strftime("%H:%M")+".\n")

			elif list_name == "season_query":
				actual_season, next_season = get_the_season()
				if sysos.lower() == 'windows':
					if system_country != None:
						country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
					else:
						country = pycountry.countries.get(name=country_code)
				elif sysos.lower() == 'linux':
					if system_country != None:
						country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
					else:
						country = pycountry.countries.get(alpha_2=country_code)
				else:
					if system_country != None:
						country_code_for_holidays = system_country[0]
						country_code_name = system_country[1]
					else:
						print(f"{random.choice(messages['trouble_short'])} Set the country, type 'set default country' and then the two-letter country code.\n")
	
				sentence = f"Actualy based on the system date {datemd} it's {actual_season.capitalize()}"
				if country:
					sentence = sentence + f" in {country.name}"
				print (f"{sentence} with {next_season[0].capitalize()} approaching.\n")

			elif list_name == "holidays_query":
				country_holidays()
			
			elif list_name == "asking for country details":
				list_country_details()

			elif list_name == "asking for talking":
				text_color = kolor['VIVID_WHITE']
				heading_color = kolor['BOLD_CYAN']
				intro = random.choice(["For clarity", "Keep in mind", "Please note", "It's important to understand"])
				beginning = random.choice(["I don't use", "my capabilities do not include", "I do not have access to", "I am unable to utilize"])
				body = random.choice(["NLP speech synthesis, or external AI modules.", "real-time speech generation or third-party AI integrations.", "direct voice output or external neural networks."])
				ending = random.choice(["Here's what I have:", "This is my current functionality:", "My current features are as follows:"])
				print(f"{heading_color}{intro} {beginning} {body}\n{ending}{kolor['OFF']}")
				for _ in range(5):
					print(f" - {text_color}{make_text(rw, num_sentences=3, num_paragraphs=1)}{kolor['OFF']}")
				print(f"\n{heading_color}Now generating a Short Text (2 paragraphs, 3 sentences each):{kolor['OFF']}")
				generated_text = make_text(rw, num_sentences=3, num_paragraphs=2)
				print(f"{text_color}{generated_text}{kolor['OFF']}")
				print("")
			
			elif list_name == "asking for a word":
				print("")
			
			elif list_name == "asking for a phrase":
				if "say something" in word:
					rns = random.randint(1, 10)
					rnp = random.randint(1, 5)
					generated_text = make_text(rw, num_sentences=rns, num_paragraphs=rnp)
					print (f"{generated_text} \n")
				else:
					generated_text = make_text(rw, num_sentences=1, num_paragraphs=1)
					print (f"{generated_text} \n")
			
			elif list_name == "asking the uptime":
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
						
			else:
				print ("To me that is a %s.\n" % (list_name).replace("_"," "))
			return True

#--------------------------------------------
def convert_units(question: str):
	CONVERSION_FACTORS = {
		'length': {
			'meter': 1.0,
			'meters': 1.0,
			'km': 1000.0,
			'kilometre': 1000.0,
			'kilometres': 1000.0,
            'kilometer': 1000.0,
			'kilometers': 1000.0,
			'foot': 0.3048,
			'feet': 0.3048,
			'mile': 1609.34,
			'miles': 1609.34,
			'yard': 0.9144,
			'yards': 0.9144,
			'au': 149597870700.0, # Astronomical Unit to meters
			'astronomical unit': 149597870700.0,
			'astronomical units': 149597870700.0,
		},
		'volume': {
			'liter': 1.0,
			'liters': 1.0,
			'm3': 1000.0, # cubic meter to liters
			'cubic meter': 1000.0,
			'cubic meters': 1000.0,
			'gallon': 3.78541,
			'gallons': 3.78541,
		},
		'time': {
			'second': 1.0,
			'seconds': 1.0,
			'minute': 60.0,
			'minutes': 60.0,
			'hour': 3600.0,
			'hours': 3600.0,
			'day': 86400.0,
			'days': 86400.0,
			'week': 604800.0,
			'weeks': 604800.0,
		},
		'temperature': {
			'celsius': 'celsius',
			'fahrenheit': 'fahrenheit',
			'kelvin': 'kelvin',
		}
	}

	match = re.search(r'(\d+\.?\d*)\s*([a-zA-Z\s]+?)(?:\s+(?:to|in)\s+([a-zA-Z\s]+))?$', question.lower().strip())
    
	if not match:
		match = re.search(r'convert\s+(\d+\.?\d*)\s*([a-zA-Z\s]+?)$', question.lower().strip())
		if not match:
			return None, "Use: convert <VALUE> <UNIT FROM> to|in <UNIT TO> \n"
        
		value_str, unit_from_raw = match.groups()
		unit_to_raw = None # No explicit 'to' unit
        
	else:
		value_str, unit_from_raw, unit_to_raw = match.groups()

	try:
		value = float(value_str)
	except ValueError:
		return None, "Invalid value. Please provide a numeric value.\n"

	unit_from = unit_from_raw.strip()
	unit_to = unit_to_raw.strip() if unit_to_raw else None

	from_category = None
	from_factor = None
	for category, units in CONVERSION_FACTORS.items():
		if unit_from in units:
			from_category = category
			from_factor = units[unit_from]
			break

	if not from_category:
		return None, f"{random.choice(messages['trouble_short'])} I don't recognize '{unit_from}' unit. Please check spelling or supported units.\n"

	if unit_to is None:
		if from_category == 'length':
			unit_to = 'meters'
		elif from_category == 'volume':
			unit_to = 'liters'
		elif from_category == 'time':
			unit_to = 'seconds'
		elif from_category == 'temperature':
			return None, f"Please specify the target temperature unit (celsius|fahrenheit|kelvin')\n."
        
	to_category = None
	to_factor = None
	for category, units in CONVERSION_FACTORS.items():
		if unit_to in units:
			to_category = category
			to_factor = units[unit_to]
			break

	if not to_category:
		return None, f"{random.choice(messages['trouble_short'])} I dont recognize the target unit: '{unit_to}'. Please check spelling.\n"

	if from_category != to_category and from_category != 'temperature':
		return None, f"I cannot convert between different unit categories like '{from_category}' and '{to_category}'.\n"

	if from_category == 'temperature':
		if unit_from == 'celsius' and unit_to == 'fahrenheit':
			converted_value = (value * 9/5) + 32
		elif unit_from == 'fahrenheit' and unit_to == 'celsius':
			converted_value = (value - 32) * 5/9
		elif unit_from == 'celsius' and unit_to == 'kelvin':
			converted_value = value + 273.15
		elif unit_from == 'kelvin' and unit_to == 'celsius':
			converted_value = value - 273.15
		elif unit_from == 'fahrenheit' and unit_to == 'kelvin':
			converted_value = (value - 32) * 5/9 + 273.15
		elif unit_from == 'kelvin' and unit_to == 'fahrenheit':
			converted_value = (value - 273.15) * 9/5 + 32
		elif unit_from == unit_to:
			converted_value = value
		else:
			return None, f"Conversion between '{unit_from}' and '{unit_to}' temperature units is not available.\n"
	else:
		value_in_base_unit = value * from_factor
		converted_value = value_in_base_unit / to_factor

	return round(converted_value, 4), unit_to

#--------------------------------------------
def get_current_century():
	current_year = date.today().isocalendar()[0]
	century = current_year // 100 + 1 if current_year % 100 == 0 else current_year // 100
	ordinal = ("st", "nd", "rd")[min(century % 100 % 10 - 1, 2)] if century % 100 not in (11, 12, 13) else "th"
	return "We are in the %d%s century. \n" % (century + 1, ordinal)

#-------------------------------------------------
def quicklist(list, delimiter):
	if not delimiter:
		delimiter = "\u3009" # or spchar[1:2]
	for i in range(len(list)):
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
def days_to_event(event):

	if not event:
		print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} What?!\n")
		return 0

	today = date.today()
	this_year = today.year
	days_left = 0

	if event == 'christmas':
		christmas = date(year=this_year, month=12, day=25)
		days_left = days_until(christmas)
	elif event == 'newyear':
		new_year = date(year=this_year + 1, month=1, day=1)
		days_left = days_until(new_year)
	elif event == 'birthday':
		birthday_this_year = date(year=this_year, month=5, day=4)
		if birthday_this_year < today:
			birthday = date(year=this_year + 1, month=5, day=4)
		else:
			birthday = birthday_this_year
		days_left = days_until(birthday)
	else:
		parsed_date = None
		formats = ["%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y"]
		for fmt in formats:
			try:
				parsed_date = datetime.strptime(event, fmt).date()
				break
			except ValueError:
				continue
		if parsed_date:
			days_left = days_until(parsed_date)
		else:
			#print(f"I couldn't understand '{event}'. Provide a valid event or a date in DD.MM.YYYY, DD/MM/YYYY, or DD-MM-YYYY.")
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
def recent_from_elysia():
	url = website.get('tvshow')
	if internet_onoff() == False or internet_onoff() == None or not url:
		print(f"{random.choice(messages['trouble_msg'])} A internet connection is required to perfeform this operation. You are currently offline.")
		return
	try:
		response = urllib.request.urlopen(url)
		html_content = response.read()
		html_string = html_content.decode("utf-8")
		soup = BeautifulSoup(html_string, 'html.parser')
		items_list = []
		tv_shows = soup.find_all('li', class_='zfr3Q TYR86d eD0Rn')
		for show in tv_shows:
			title_element = show.find('span', class_='C9DxTc')
			if title_element:
				items_list.append(title_element.text.strip())
		for i in range(82, 87):
			print (items_list[i])
	except urllib.error.URLError as e:
		print(f"{random.choice(messages['trouble_msg'])} Error fetching the content from {website[content_type]}")
	except Exception as e:
		print(f"{random.choice(messages['trouble_msg'])} Unexpected error: {e}")

#-------------------------------------------------
def extract_from_elysia(content_type):
	url = website.get(content_type)

	if internet_onoff() == False or not url:
		print(f"{random.choice(messages['trouble_msg'])} A internet connection is required to perfeform this operation. You are currently offline.")
		return

	try:
		response = urllib.request.urlopen(url)
		html_content = response.read()
		html_string = html_content.decode("utf-8")
		soup = BeautifulSoup(html_string, 'html.parser')
		items_list = []
		if content_type == 'tvshow':
			tv_shows = soup.find_all('li', class_='zfr3Q TYR86d eD0Rn')
			for show in tv_shows:
				title_element = show.find('span', class_='C9DxTc')
				if title_element:
					items_list.append(title_element.text.strip())           
			for i in range(87, len(items_list)):
				print (items_list[i])
			print("")
		elif content_type == 'movies':
			classic_movies_section = soup.find('div', id='h.7ea6f691e3c697ae_12')
			if classic_movies_section:
				movies = classic_movies_section.find_all('li', class_='zfr3Q TYR86d eD0Rn')
				for movie in movies:
					title_element = movie.find('span', class_='C9DxTc')
					if title_element:
						items_list.append(title_element.text.strip())
			if items_list:
				for item in items_list:
					print(item)
			else:
				print(f"{random.choice(messages['trouble_msg'])} No {content_type.replace('_', ' ')} found or the structure has changed.")
		else:
			print(f"{random.choice(messages['trouble_msg'])} Unknown content type: {content_type}")
	except urllib.error.URLError as e:
		print(f"{random.choice(messages['trouble_msg'])} Error fetching the content from {website[content_type]}")
	except Exception as e:
		print(f"{random.choice(messages['trouble_msg'])} Unexpected error: {e}")
		
#-------------------------------------------------
def get_the_season():
	
	today = datetime.today()
	m = today.month * 100
	d = today.day
	md = m + d
	s = -1
	
	if lat >= 0:
		# Northern Hemisphere
		if ((md >= 301) and (md <= 531)):
			s = 0  # spring
		elif ((md > 531) and (md < 901)):
			s = 1  # summer
		elif ((md >= 901) and (md <= 1130)):
			s = 2  # autumn
		elif ((md > 1130) and (md <= 1229)):
			s = 3  # winter
	else:
		# Southern Hemisphere
		if (md >= 901) and (md <= 1130):
			s = 0  # spring
		elif (md > 1130) or (md <= 228): # Handles December to February
			s = 1  # summer
		elif (md >= 301) and (md <= 531):
			s = 2  # autumn
		elif (md > 531) and (md < 901):
			s = 3  # winter

	if s == -1:
		print (f"{random.choice(messages['trouble_short'])} Could not determine season!\n")
		return None, None

	season_emoji = ["🌻", "☀️", "🍁", "❄️"]
	seasons = list(core['seasons'])
	#current_season = seasons[s]
	current_season = f"{seasons[s]} {season_emoji[s]}"
	next_season_index = (s + 1) % 4
	other_seasons = seasons[next_season_index:] + seasons[:next_season_index - 1]
	return current_season, other_seasons

#--------------------------------------------------
def special_dates(date_to_check):
	global lat,special_dates_dict
	
	seasons = ("🌻 Spring", "☀️ Summer", "🍁 Autumn", "❄️ Winter")
	month_day_key = (date_to_check.month, date_to_check.day)

	if lat >= 0: # Northern Hemisphere (including equator)
		seasonal_start_dates = {
			(3, 20): 0,
			(6, 21): 1,
			(9, 22): 2,
			(12, 21): 3
		}
	else: # Southern Hemisphere
		seasonal_start_dates = {
			(9, 22): 0, 
			(12, 21): 1,
			(3, 20): 2,
			(6, 21): 3 
		}

	if month_day_key in special_dates_dict:
		event = special_dates_dict[month_day_key]
		return f"the {event}"
	elif month_day_key in seasonal_start_dates:
		season_index = seasonal_start_dates[month_day_key]
		season_name = seasons[season_index]
		return f"the Beginning of the {season_name}."
	elif month_day_key in seasonal_start_dates and month_day_key.year == datetime.now().year:
		return f"especially this year will exist {event}."

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
			conn = sqlitecloud.connect(sqlconn)
		else:
			db_filename = "cybele.db"
			if os.path.isfile(db_filename):
				conn = sqlite3.connect(db_filename)
			else:
				modname = "The " + db_filename.upper() + " database file is missing, and with no internet the online database is inaccessible. \n   To work offline use the option <offline mode on> in the main cybele prompt. \n   I cannot execute properly. Exiting."
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

	global dblrconn
	if internet_onoff() == True:
		db_filename = dbtable + ".db"
		if os.path.isfile (db_filename) == True :
			conn = sqlite3.connect(db_filename)
			dblrconn="offline [database files]"
		else:
			sqlconm = sqlcodb.format(dbname_placeholder=dbname)
			conn = sqlitecloud.connect(sqlconm)
			dblrconn="online [sqlitecloud]"
	else:
		db_filename = dbname + ".db"
		if os.path.isfile (db_filename) == True:
			conn = sqlite3.connect(db_filename)
			dblrconn="offline [database files]"
		else:
			modname = "The " + db_filename.upper() + " database file is missing, and with no internet the online database is inaccessible. \n   To work offline use the option <offline mode on> in the main cybele prompt. \n   I cannot execute properly. Exiting."
			print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
			sys.exit(0)
	
	zdb = []
	filter = ""

	if dbtask == 'search':
		if dbname == 'cybele' and dbtable == 'askard_db':
			filter = "SELECT ask_id, askard FROM askard_db WHERE askard LIKE '%"+str(dbend)+"%'"
			nchar = _spchar_[9:10]
		elif dbname == 'cybele' and dbtable == 'astronomy_glossary':
			filter = "SELECT glossary, designation FROM astronomy_glossary WHERE designation LIKE '%"+str(dbend)+"%'"
			nchar = _spchar_[0:1]
			dbname = 'astronomy glossary'
		elif dbname == 'cybele'and dbtable == 'oldtech':
			filter = "SELECT oldterm, designation FROM oldtech WHERE designation LIKE '%"+str(dbend)+"%'"
			#nchar = _spchar_[7:8]
			nchar = "↺"
			dbname = 'old tech'
		else:
			print ('Well done ' + _author_.split()[0] +'!. The code has a error. Fix it, you morone!')
		
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
		if dbname == 'cybele' and dbtable == 'askard_db':
			ask_id_val = int(dbbegin)
			filter = f"SELECT ask_id, askard FROM askard_db WHERE ask_id = {ask_id_val}"
			cursor = conn.execute(filter)
			row_found = False
			for row in cursor:
				row_found = True
				zdb.append(row[0])
				zdb.append(row[1])
			if row_found and len(zdb) > 0:
				print(f"\n {_spchar_[9:10]}  {_spchar_[1:2]}{zdb[1]}")
			else:
				print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} No record found for askard #{ask_id_val}.\n")
		elif dbname == 'cybele' and dbtable == 'funfacts':
			filter = "SELECT * FROM funfacts ORDER BY RANDOM() LIMIT 1;"
			cursor = conn.execute(filter)
			nchar = _spchar_[13:14]
			if cursor:
				row = cursor.fetchone()
				if row:
					print(f"\n {nchar} {str(row[0])}\n")
				else:
					print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} The database query results return empty!!")
		elif dbtable == 'nicethings':	
			filter = "SELECT * FROM nicethings ORDER BY RANDOM() LIMIT 1;"
			cursor = conn.execute(filter)
			nchar = _spchar_[14:15]
			if cursor:
				row = cursor.fetchone()
				if row:
					print(f"\n {nchar} {str(row[0])}\n")
				else:
					print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} The database query results return empty!!")
			else:
				print ("option view none of dbtables with conditions... Fix'it")
		else:
			print (f"{random.choice(messages['trouble_short'])} Invalid conditions for view task for {dbname} dabatase...\n")
		
	if dbtask == 'list':
		if dbname == 'cybele' and dbtable == 'askard_db':
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
		else:
			print (f"{random.choice(messages['trouble_short'])} Invalid conditions for List task for {dbname} dabatase...\n")
			return
		
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
		if dbname == 'cybele' and dbtable == 'askard_db':
			filter = "SELECT min(ask_id) , max(ask_id) FROM askard_db"
			titvar = "askard ID"
		elif dbname == 'cybele' and dbtable == 'astronomy_glossary':
			filter = "SELECT min(glossary) , max(glossary) FROM astronomy_glossary"
			titvar = "astronomy glossary term"
		elif dbname == 'cybele' and dbtable == 'oldtech':
			filter = "SELECT min(oldterm) , max(oldterm) FROM oldtech"
			titvar = "old tech terminology"
		else:
			print ("Option limits none of dbtables with conditions... Fix'it")
			conn.close()
			return
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
	if pyver[0] < 3 or pyver[0] == 3 and pyver[1] < 10 or pyver[1] > 13 :
		modname = f"Python {major}.{minor} is too old. Required version 3.10 or higher.\n   I cannot execute properly. Exiting."
		print("\n\033[1;31m " + _spchar_[1:2] + _title_ + "\033[0;0m" + ": " + modname)
		return False
	return True	

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
def today_holiday():
	
	global sysos
	today = datetime.today()
	if sysos.lower() == 'windows':
		if system_country != None:
			country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
		else:
			country = pycountry.countries.get(name=country_code)
	elif sysos.lower() == 'linux':
		if system_country != None:
			country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
		else:
			country = pycountry.countries.get(alpha_2=country_code)
	else:
		print(f"{random.choice(messages['trouble_short'])} This option is unavailable for {sysos.title()} system's.\n")
		return
		
	if country:
		country_code_for_holidays = country.alpha_2
	else:
		if system_country != None:
			country_code_for_holidays = system_country[0]
			country_code_name = system_country[1]
		else:
			print(f"{random.choice(messages['trouble_short'])} Set the country, type 'set default country' and then the two-letter country code.\n")
			return False, None

	if country_code_for_holidays:
		try:
			country_holidays = holidays.CountryHoliday(country_code_for_holidays)
			if today in country_holidays:
				holiday_name = country_holidays.get(today)
				#print(f"{_spchar_[18:19]} Today in {country_code_for_holidays} is {holiday_name}")
				return True, holiday_name
			else:
				return False, None
		except Exception as e:
			print(f"{random.choice(['Oops!', 'Sorry!', 'Heads up!'])} Error checking holidays for {country_code_for_holidays}")
			return False, None
	else:
		print(f"{random.choice(['Oops!', 'Sorry!', 'Heads up!'])} No country code determined, cannot check for holidays.")
		return False, None

#----------------------------------------------------------------
#----------------------------------------------------------------
def country_holidays():
	global system_country
	if sysos.lower() == 'windows':
		if system_country != None:
			country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
		else:
			country = pycountry.countries.get(name=country_code)
	elif sysos.lower() == 'linux':
		if system_country != None:
			country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
		else:
			country = pycountry.countries.get(alpha_2=country_code)
	else:
		print(f"{random.choice(messages['trouble_short'])} This option is unavailable for {sysos.title()} system's.\n")
		return
	
	if country:
		print(f"\nDetected country: {country.name} ({country.alpha_2})")
		country_code_for_holidays = country.alpha_2
		country_code_name = country.name
	else:
		if system_country != None:
			country_code_for_holidays = system_country[0]
			country_code_name = system_country[1]
			print(f"\nUsing default country: {country_code_name} ({country_code_for_holidays})")
		else:
			print(f"{random.choice(messages['trouble_short'])} Set the country, type 'set default country' and then the two-letter country code.\n")
			return

	holidays_country_year = datetime.now().year
	try:
		country_holidays = holidays.country_holidays(country_code_for_holidays, years=holidays_country_year)
		if country_holidays:
			print(f"Holidays for {country_code_name} ({country_code_for_holidays}) in the year {holidays_country_year}:\n")
			sorted_holidays = sorted(country_holidays.items())
			for date, name in sorted_holidays:
				print(f"  {date} | {name}")
		else:
			print(f"No holidays found for {country_code_name} ({country_code_for_holidays}) in {holidays_country_year}.")
	except NotImplementedError:
		print(f"{random.choice(['Oops!', 'Sorry!', 'Heads up!'])} The holidays does not have data for {country.name} ({country.alpha_2}).")
	except KeyError:
		print(f"{random.choice(['Oops!', 'Sorry!', 'Heads up!'])} An issue occurred with the country code {country.alpha_2} when fetching holidays.")
	except Exception as e:
		print(f"{random.choice(messages['trouble_short'])} Unexpected error {e}")
	print("")
	
#----------------------------------------------------------------
def get_display_length(s):
    return len(re.sub(r'\033\[[0-9;]*m', '', s))
#----------------------------------------------------------------
def set_cursor_pos(row, col):
    return f"\033[{row};{col}H"
#----------------------------------------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
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
#----------------------------------------------------------------
def showlisttell(data_key_list, num_terms=5, category="terms"):
   
    all_items = list(data_key_list)
    random.shuffle(all_items)
    selected_items = all_items[:num_terms]
    formatted_items_list = ""
    if len(selected_items) > 1:
        formatted_items_list = f"{', '.join(selected_items[:-1])} and {selected_items[-1]}"
    elif selected_items:
        formatted_items_list = selected_items[0]
    intro_fragments = [
        f"I can show you based on my knowledge, these are some {category}:",
        f"Here are some {category} I have in knowledge:",
        f"Based on what I know, these are some {category}:",
        f"Let me share some {category} I have:",
        f"You might be interested in these {category}:"
    ]
    chosen_intro_fragment = random.choice(intro_fragments)
    if formatted_items_list:
        return f"{chosen_intro_fragment} {formatted_items_list}"
    else:
        return f"Sorry, I don't have any {category} to show at the moment."

#----------------------------------------------------------------
def create_firework_explosion(x, y, max_radius, characters):
 
    try:
        canvas_width, canvas_height = os.get_terminal_size()
    except OSError:
        canvas_width, canvas_height = 80, 24 # Fallback if size cannot be determined

    explosion_color = random.choice([k for k in kolor.keys() if k != 'OFF']) # Pick a random color, not 'OFF'

    for radius in range(1, max_radius + 1):
        frame_canvas = [[' ' for _ in range(canvas_width)] for _ in range(canvas_height)]

        for i in range(canvas_height):
            for j in range(canvas_width):
                dist = ((j - x)**2 + (i - y)**2)**0.5
                if radius - 1 <= dist < radius:
                    if 0 <= i < canvas_height and 0 <= j < canvas_width:
                        frame_canvas[i][j] = random.choice(characters)

        clear_screen()

        for row_idx, row_chars in enumerate(frame_canvas):
            print(f"{set_cursor_pos(row_idx + 1, 1)}{kolor[explosion_color]}{''.join(row_chars)}{kolor['OFF']}", end="")
        
        #import sys
        sys.stdout.flush()
        sleep(0.08)

def main_fireworks(num_fireworks=5, delay_between_fireworks=1.5):
	global kolor

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
			start_x = random.randint(int(term_width * 0.1), int(term_width * 0.9))
			start_y = term_height - 2 # Start 2 rows from the bottom

			explosion_y = random.randint(int(term_height * 0.2), int(term_height * 0.6)) # Explode in upper-middle
            
			random_color = random.choice([k for k in kolor.keys() if k != 'OFF'])
			rocket_char = '↟'

			for y_coord in range(start_y, explosion_y, -1):
				clear_screen()
				print(f"{set_cursor_pos(y_coord, start_x)}{kolor[random_color]}{rocket_char}{kolor['OFF']}", end="")
				import sys
				sys.stdout.flush()
				sleep(0.08)

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

	randomcolor = ['RED','YELLOW','GREEN','BLUE','CYAN','MAGENTA']
	for i in range(len(tree)):
		res = ''.join(map(chr, tree[i]))
		if i <= 4:
			artcor = kolor['YELLOW']
		elif i >= 19:
			artcor = kolor['WHITE']
		else:
			artcor = kolor[random.choice(randomcolor)]
		print (f"{' '*5} {artcor} {str(res)}")

	merry_christmas_message = (
		kolor['RED'] + "  MERRY" +
		kolor['GREEN'] + " CHRISTMAS!" +
		kolor['OFF']
	)
	print(" "*27 + merry_christmas_message)

#---------------------------------------------------------------------------
#-------------------------------------------------------------------
# cybele verb conjugator (EN simple)
#-------------------------------------------------------------------
#---------------------------------------------------------------------------
def cybele_conjugator(verb):
    
    if not isinstance(verb, str):
        if isinstance(verb, (int, float)):
            print(f"{kolor['BOLD_RED']}Oh no, my friend!{kolor['OFF']} I need a proper verb ({kolor['BOLD_CYAN']}a string{kolor['OFF']}) to work my magic. It looks like you gave me a {kolor['BOLD_YELLOW']}number{kolor['OFF']}: {kolor['VIVID_RED']}{verb}{kolor['OFF']}")
        else:
            print(f"{kolor['BOLD_RED']}Oh no, my friend!{kolor['OFF']} I need a proper verb ({kolor['BOLD_CYAN']}a string{kolor['OFF']}) to work my magic. You gave me something of type: {kolor['VIVID_RED']}{type(verb)}{kolor['OFF']}")
        return

    verb = verb.lower()
	
    PERSON_COL_WIDTH = 18
    TENSE_COL_WIDTH = 25

    irregular_verbs = {
        'be': ('was/were', 'been', 'ing'),
        'have': ('had', 'had', 'ing'),
        'do': ('did', 'done', 'ing'),
        'go': ('went', 'gone', 'ing'),
        'say': ('said', 'said', 'ing'),
        'see': ('saw', 'seen', 'ing'),
        'make': ('made', 'made', 'ing'),
        'come': ('came', 'come', 'ing'),
        'know': ('knew', 'known', 'ing'),
        'get': ('got', 'gotten/got', 'ing'),
        'give': ('gave', 'given', 'ing'),
        'find': ('found', 'found', 'ing'),
        'think': ('thought', 'thought', 'ing'),
        'tell': ('told', 'told', 'ing'),
        'take': ('took', 'taken', 'ing'),
        'become': ('became', 'become', 'ing'),
        'begin': ('began', 'begun', 'ning'),
        'run': ('ran', 'run', 'nning'),
        'cut': ('cut', 'cut', 'tting'),
        'put': ('put', 'put', 'tting'),
        'read': ('read', 'read', 'ing'),
        'eat': ('ate', 'eaten', 'ing'),
        'write': ('wrote', 'written', 'ing'),
        'sing': ('sang', 'sung', 'ing'),
        'drink': ('drank', 'drunk', 'ing'),
        'sleep': ('slept', 'slept', 'ing'),
        'drive': ('drove', 'driven', 'ing'),
        'swim': ('swam', 'swum', 'mming'),
        'fly': ('flew', 'flown', 'ing'),
        'break': ('broke', 'broken', 'ing'),
        'speak': ('spoke', 'spoken', 'ing'),
        'steal': ('stole', 'stolen', 'ing'),
        'choose': ('chose', 'chosen', 'ing'),
        'fall': ('fell', 'fallen', 'ing'),
        'grow': ('grew', 'grown', 'ing'),
        'draw': ('drew', 'drawn', 'ing'),
        'build': ('built', 'built', 'ing'),
        'send': ('sent', 'sent', 'ing'),
        'spend': ('spent', 'spent', 'ing'),
        'lose': ('lost', 'lost', 'ing'),
        'catch': ('caught', 'caught', 'ing'),
        'bring': ('brought', 'brought', 'ing'),
        'buy': ('bought', 'bought', 'ing'),
        'teach': ('taught', 'taught', 'ing'),
        'fight': ('fought', 'fought', 'ing'),
        'sell': ('sold', 'sold', 'ing'),
        'hear': ('heard', 'heard', 'ing'),
        'hold': ('held', 'held', 'ing'),
        'stand': ('stood', 'stood', 'ing'),
        'understand': ('understood', 'understood', 'ing'),
    }

    persons = [
        'I', 'You', 'He/She/It', 'We', 'You (plural)', 'They'
    ]

    conjugated_forms = {
        'present_simple': {},
        'past_simple': {},
        'future_simple': {},
        'present_continuous': {},
        'past_continuous': {},
        'present_perfect': {},
        'present_participle': '',
        'past_participle': ''
    }

    past_simple_form = ''
    past_participle_form = ''
    present_participle_form = ''

    if verb in irregular_verbs:
        past_simple_form, past_participle_form, pp_suffix = irregular_verbs[verb]
        if verb.endswith('e') and pp_suffix == 'ing' and verb != 'be':
            present_participle_form = verb[:-1] + 'ing'
        elif pp_suffix == 'ing':
            present_participle_form = verb + 'ing'
        elif pp_suffix:
             present_participle_form = verb + pp_suffix
        else:
             present_participle_form = verb + 'ing'
    else:
        if verb.endswith('e'):
            past_form_regular = verb + 'd'
        elif verb.endswith('y') and len(verb) > 1 and verb[-2] not in 'aeiou':
            past_form_regular = verb[:-1] + 'ied'
        elif len(verb) >= 2 and verb[-1] not in 'aeiouy' and verb[-2] in 'aeiou' and verb[-3] not in 'aeiou':
            past_form_regular = verb + verb[-1] + 'ed'
        else:
            past_form_regular = verb + 'ed'
        past_simple_form = past_form_regular
        past_participle_form = past_form_regular

        if verb.endswith('e') and verb not in ['be', 'dye', 'lie', 'tie', 'vie']:
            present_participle_form = verb[:-1] + 'ing'
        elif len(verb) >= 2 and verb[-1] not in 'aeiouy' and verb[-2] in 'aeiou' and verb[-3] not in 'aeiou':
            present_participle_form = verb + verb[-1] + 'ing'
        else:
            present_participle_form = verb + 'ing'

    conjugated_forms['present_participle'] = present_participle_form
    conjugated_forms['past_participle'] = past_participle_form

    if verb in irregular_verbs:
        if verb == 'be':
            conjugated_forms['present_simple'] = {
                'I': 'am', 'You': 'are', 'He/She/It': 'is',
                'We': 'are', 'You (plural)': 'are', 'They': 'are'
            }
        elif verb == 'have':
             conjugated_forms['present_simple'] = {
                'I': 'have', 'You': 'have', 'He/She/It': 'has',
                'We': 'have', 'You (plural)': 'have', 'They': 'have'
            }
        else:
            for i, person in enumerate(persons):
                if person == 'He/She/It':
                    if verb.endswith(('s', 'sh', 'ch', 'x', 'z', 'o')):
                        conjugated_forms['present_simple'][person] = verb + 'es'
                    elif verb.endswith('y') and len(verb) > 1 and verb[-2] not in 'aeiou':
                        conjugated_forms['present_simple'][person] = verb[:-1] + 'ies'
                    else:
                        conjugated_forms['present_simple'][person] = verb + 's'
                else:
                    conjugated_forms['present_simple'][person] = verb

        for person in persons:
            conjugated_forms['past_simple'][person] = past_simple_form
        for person in persons:
            conjugated_forms['future_simple'][person] = 'will ' + verb

        be_present = {
            'I': 'am', 'You': 'are', 'He/She/It': 'is',
            'We': 'are', 'You (plural)': 'are', 'They': 'are'
        }
        for person in persons:
            conjugated_forms['present_continuous'][person] = f"{be_present[person]} {present_participle_form}"

        be_past = {
            'I': 'was', 'You': 'were', 'He/She/It': 'was',
            'We': 'were', 'You (plural)': 'were', 'They': 'were'
        }
        for person in persons:
            conjugated_forms['past_continuous'][person] = f"{be_past[person]} {present_participle_form}"

        have_present = {
            'I': 'have', 'You': 'have', 'He/She/It': 'has',
            'We': 'have', 'You (plural)': 'have', 'They': 'have'
        }
        for person in persons:
            conjugated_forms['present_perfect'][person] = f"{have_present[person]} {past_participle_form}"

    else:
        for i, person in enumerate(persons):
            if person == 'He/She/It':
                if verb.endswith(('s', 'sh', 'ch', 'x', 'z', 'o')):
                    conjugated_forms['present_simple'][person] = verb + 'es'
                elif verb.endswith('y') and len(verb) > 1 and verb[-2] not in 'aeiou':
                    conjugated_forms['present_simple'][person] = verb[:-1] + 'ies'
                else:
                    conjugated_forms['present_simple'][person] = verb + 's'
            else:
                conjugated_forms['present_simple'][person] = verb

        for person in persons:
            conjugated_forms['past_simple'][person] = past_simple_form
        for person in persons:
            conjugated_forms['future_simple'][person] = 'will ' + verb

        be_present = {
            'I': 'am', 'You': 'are', 'He/She/It': 'is',
            'We': 'are', 'You (plural)': 'are', 'They': 'are'
        }
        for person in persons:
            conjugated_forms['present_continuous'][person] = f"{be_present[person]} {present_participle_form}"

        be_past = {
            'I': 'was', 'You': 'were', 'He/She/It': 'was',
            'We': 'were', 'You (plural)': 'were', 'They': 'were'
        }
        for person in persons:
            conjugated_forms['past_continuous'][person] = f"{be_past[person]} {present_participle_form}"

        have_present = {
            'I': 'have', 'You': 'have', 'He/She/It': 'has',
            'We': 'have', 'You (plural)': 'have', 'They': 'have'
        }
        for person in persons:
            conjugated_forms['present_perfect'][person] = f"{have_present[person]} {past_participle_form}"

    print(f"\nHere's what I have for the '{kolor['BOLD_YELLOW']}{verb}{kolor['OFF']}' bring in my knowledge base:")

    print(f"{kolor['BOLD_BLUE']}{'Person':<{PERSON_COL_WIDTH}}{kolor['OFF']} {kolor['BOLD_CYAN']}{'Present Simple':<{TENSE_COL_WIDTH}}{kolor['OFF']} {kolor['BOLD_CYAN']}{'Past Simple':<{TENSE_COL_WIDTH}}{kolor['OFF']} {kolor['BOLD_CYAN']}{'Future Simple':<{TENSE_COL_WIDTH}}{kolor['OFF']}")
    print(f"{kolor['DIM_WHITE']}{'-'*PERSON_COL_WIDTH:<{PERSON_COL_WIDTH}} {'-'*TENSE_COL_WIDTH:<{TENSE_COL_WIDTH}} {'-'*TENSE_COL_WIDTH:<{TENSE_COL_WIDTH}} {'-'*TENSE_COL_WIDTH:<{TENSE_COL_WIDTH}}{kolor['OFF']}")

    for person in persons:
        present_s = conjugated_forms['present_simple'].get(person, 'N/A')
        past_s = conjugated_forms['past_simple'].get(person, 'N/A')
        future_s = conjugated_forms['future_simple'].get(person, 'N/A')
        print(f"{kolor['WHITE']}{person:<{PERSON_COL_WIDTH}}{kolor['OFF']} {kolor['YELLOW']}{present_s:<{TENSE_COL_WIDTH}}{kolor['OFF']} {kolor['YELLOW']}{past_s:<{TENSE_COL_WIDTH}}{kolor['OFF']} {kolor['YELLOW']}{future_s:<{TENSE_COL_WIDTH}}{kolor['OFF']}")

    print(f"\n{kolor['BOLD_GREEN']}And here's the second part for '{kolor['BOLD_YELLOW']}{verb}{kolor['OFF']}', just as important, you see:")

    print(f"{kolor['BOLD_BLUE']}{'Person':<{PERSON_COL_WIDTH}}{kolor['OFF']} {kolor['BOLD_CYAN']}{'Present Continuous':<{TENSE_COL_WIDTH}}{kolor['OFF']} {kolor['BOLD_CYAN']}{'Past Continuous':<{TENSE_COL_WIDTH}}{kolor['OFF']} {kolor['BOLD_CYAN']}{'Present Perfect':<{TENSE_COL_WIDTH}}{kolor['OFF']}")
    print(f"{kolor['DIM_WHITE']}{'-'*PERSON_COL_WIDTH:<{PERSON_COL_WIDTH}} {'-'*TENSE_COL_WIDTH:<{TENSE_COL_WIDTH}} {'-'*TENSE_COL_WIDTH:<{TENSE_COL_WIDTH}} {'-'*TENSE_COL_WIDTH:<{TENSE_COL_WIDTH}}{kolor['OFF']}")

    for person in persons:
        present_c = conjugated_forms['present_continuous'].get(person, 'N/A')
        past_c = conjugated_forms['past_continuous'].get(person, 'N/A')
        present_p = conjugated_forms['present_perfect'].get(person, 'N/A')
        print(f"{kolor['WHITE']}{person:<{PERSON_COL_WIDTH}}{kolor['OFF']} {kolor['YELLOW']}{present_c:<{TENSE_COL_WIDTH}}{kolor['OFF']} {kolor['YELLOW']}{past_c:<{TENSE_COL_WIDTH}}{kolor['OFF']} {kolor['YELLOW']}{present_p:<{TENSE_COL_WIDTH}}{kolor['OFF']}")

    print(f"\n{kolor['BOLD_GREEN']}And don't forget the core forms for '{kolor['BOLD_YELLOW']}{verb}{kolor['OFF']}', they're very important, you know:")
    print(f"Present Participle (the '-ing' form): {kolor['YELLOW']}{conjugated_forms['present_participle']}{kolor['OFF']}")
    print(f"Past Participle (often the '-ed' or irregular form): {kolor['YELLOW']}{conjugated_forms['past_participle']}{kolor['OFF']}")
    print(f"\n{kolor['BOLD_GREEN']}That's all for '{kolor['BOLD_YELLOW']}{verb}{kolor['OFF']}' now! Hope it helped!{kolor['OFF']}\n")
	
#---------------------------------------------------------------------------
#-------------------------------------------------------------------
# cybele sentence, text, verb sub-cores
#-------------------------------------------------------------------
#---------------------------------------------------------------------------
def conjugate_verb(verb_type, subject_pronoun, knowledge):

    if verb_type == "verb_present_conjugated":
        base_verb_options = [v for v in knowledge["verb_base"] if v not in ["be", "have", "do"]]
        if not base_verb_options:
            return "[NO_GENERAL_VERB]"
        base_verb = random.choice(base_verb_options)

        if subject_pronoun in knowledge["pronoun_singular_third"]:
            if base_verb in ["do", "go"]:
                return base_verb + "es"
            elif base_verb.endswith('y') and len(base_verb) > 1 and base_verb[-2] not in "aeiou":
                return base_verb[:-1] + "ies"
            else:
                return base_verb + "s"
        else:
            return base_verb

    elif verb_type == "aux_be_present_conjugated":
        if subject_pronoun == "I":
            return random.choice(knowledge["aux_be_present_I"])
        elif subject_pronoun in knowledge["pronoun_singular_third"]:
            return random.choice(knowledge["aux_be_present_singular_third"])
        else:
            return random.choice(knowledge["aux_be_present_plural"])

    elif verb_type == "aux_have_present_conjugated":
        if subject_pronoun in knowledge["pronoun_singular_third"]:
            return random.choice(knowledge["aux_have_present_singular_third"])
        else:
            return random.choice(knowledge["aux_have_present_I_plural"])
            
    return "[CONJUGATION_ERROR]"

#-------------------------------------------------------------------
def make_sentence(rw_instance):

	sentence_structures = [
		["subject", "verb_present_conjugated", "determiner", "noun_countable_singular"],  
		["subject", "verb_present_conjugated", "determiner", "noun_uncountable"],  
		["subject", "verb_present_conjugated", "determiner", "noun_countable_plural"],  
		["subject", "verb_present_conjugated"],  
		["subject", "verb_present_conjugated", "adverb"],  

        ["subject", "aux_be_present_conjugated", "adjective"],  
        ["subject", "aux_be_present_conjugated", "determiner", "noun_countable_singular"],  

        ["subject", "aux_be_present_conjugated", "negation", "adjective"],
        ["subject", "aux_be_present_conjugated", "negation", "determiner", "noun_countable_singular"],

        ["subject", "modal_verb", "verb_base", "determiner", "noun_countable_singular"],
        ["subject", "modal_verb", "verb_base", "determiner", "noun_uncountable"],
        ["subject", "modal_verb", "verb_base", "adverb"],
        ["subject", "modal_verb", "verb_base"],

        ["subject", "aux_do_present_neg_conjugated", "verb_base", "determiner", "noun_countable_singular"],
        ["subject", "aux_do_present_neg_conjugated", "verb_base", "determiner", "noun_uncountable"],
        ["subject", "aux_do_present_neg_conjugated", "verb_base"],

        ["subject", "aux_have_present_conjugated", "verb_past_participle", "determiner", "noun_countable_singular"],
        ["subject", "aux_have_present_conjugated", "verb_past_participle", "determiner", "noun_uncountable"],
        ["subject", "aux_have_present_conjugated", "verb_past_participle"],
        ["subject", "aux_have_present_conjugated", "verb_past_participle_be", "adjective"],
		
        ["subject", "modal_verb", "negation", "verb_base_be", "adjective"],
        ["subject", "modal_verb", "negation", "verb_base_be", "determiner", "noun_countable_singular"],
	]

	try:
		chosen_structure = random.choice(sentence_structures)
		sentence_words = []
		chosen_subject = None
		temp_word = rw_instance.get_random_word()

		for i, part_type in enumerate(chosen_structure):
			word_to_add = ""

			if part_type == "subject":
				if random.random() < 0.5:
					chosen_subject = random.choice(knowledge["pronoun_singular_third"])
				else:
					chosen_subject = random.choice(knowledge["pronoun_first_second_plural"])
				word_to_add = chosen_subject
                
			elif part_type in ["verb_present_conjugated", "aux_be_present_conjugated", "aux_have_present_conjugated"]:
				if chosen_subject is None:
					raise ValueError("Subject must be chosen before verb conjugation.")
				word_to_add = conjugate_verb(part_type, chosen_subject, knowledge)
                
			elif part_type == "aux_do_present_neg_conjugated":
				if chosen_subject in knowledge["pronoun_singular_third"]:
					word_to_add = knowledge["aux_do_s_form"][0] + " " + knowledge["negation"][0]
				else:
					word_to_add = knowledge["aux_do_base"][0] + " " + knowledge["negation"][0]
                    
			elif part_type == "verb_base_be":
				word_to_add = random.choice(knowledge["verb_base_be"])
                
			elif part_type == "verb_past_participle_be":
				word_to_add = random.choice(knowledge["verb_past_participle_be"])
            
			elif part_type.startswith("noun"):
				if part_type == "noun_countable_singular":
					word_to_add = random.choice(knowledge["noun_countable_singular"])
				elif part_type == "noun_countable_plural":
					word_to_add = random.choice(knowledge["noun_countable_plural"])
				elif part_type == "noun_uncountable":
					word_to_add = random.choice(knowledge["noun_uncountable"])
				elif part_type == "noun_abstract":
					word_to_add = random.choice(knowledge["noun_abstract"])
				else:
					word_to_add = random.choice(knowledge["noun"])
                
				if temp_word.lower() in knowledge["noun"] or \
					temp_word.lower() in knowledge["noun_countable_singular"] or \
					temp_word.lower() in knowledge["noun_countable_plural"] or \
					temp_word.lower() in knowledge["noun_uncountable"] or \
					temp_word.lower() in knowledge["noun_abstract"] or \
					random.random() < 0.3:
					word_to_add = temp_word.lower()
				else:
					if part_type == "noun_countable_singular":
						word_to_add = random.choice(knowledge["noun_countable_singular"])
					elif part_type == "noun_countable_plural":
						word_to_add = random.choice(knowledge["noun_countable_plural"])
					elif part_type == "noun_uncountable":
						word_to_add = random.choice(knowledge["noun_uncountable"])
					elif part_type == "noun_abstract":
						word_to_add = random.choice(knowledge["noun_abstract"])
					else: 
						word_to_add = random.choice(knowledge["noun"])

				if part_type == "noun_countable_plural" and not word_to_add.endswith('s'):
					word_to_add += 's'
			
			elif part_type == "adjective":
				word_to_add = random.choice(knowledge["adjective"])
			              
				if temp_word.lower() in knowledge["adjective"] or \
					temp_word.lower().endswith(('ful', 'ous', 'able', 'ible', 'ish', 'ive', 'less', 'ly', 'al')) or \
					random.random() < 0.3: 
					word_to_add = temp_word.lower()
				else:
					word_to_add = random.choice(knowledge["adjective"])

			elif part_type == "adverb":
				word_to_add = random.choice(knowledge["adverb"])
               
				if temp_word.lower() in knowledge["adverb"] or temp_word.lower().endswith('ly') or \
					random.random() < 0.3: 
					word_to_add = temp_word.lower()
				else:
					word_to_add = random.choice(knowledge["adverb"])

			elif part_type == "determiner":
				next_noun_category_in_structure = None
				if i + 1 < len(chosen_structure) and chosen_structure[i+1].startswith("noun"):
					next_noun_category_in_structure = chosen_structure[i+1]

				if next_noun_category_in_structure == "noun_uncountable":
					word_to_add = random.choice(["some", "the"]) 
				elif next_noun_category_in_structure == "noun_countable_singular":
					temp_word_for_vowel_check = rw_instance.get_random_word() 
					while not temp_word_for_vowel_check or len(temp_word_for_vowel_check) < 2:
						temp_word_for_vowel_check = rw_instance.get_random_word()
                    
					if temp_word_for_vowel_check.lower().startswith(('a', 'e', 'i', 'o', 'u')):
						word_to_add = "an"
					else:
						word_to_add = "a"
				elif next_noun_category_in_structure == "noun_countable_plural": 
					word_to_add = random.choice(["the", "some"]) 
				elif next_noun_category_in_structure == "noun": 
					word_to_add = random.choice(["the", "some", "a", "an"]) 
            
			elif part_type in knowledge:
				word_to_add = random.choice(knowledge[part_type])
                
			else:
				if part_type in knowledge:
					word_to_add = random.choice(knowledge[part_type])
				else:
					print(f"Warning: Unrecognized part type '{part_type}' in structure. This should not happen.")
					word_to_add = "[UNKNOWN]"

			sentence_words.append(word_to_add)

		if sentence_words:
			sentence_words[0] = sentence_words[0].capitalize()
		final_sentence = " ".join(sentence_words) + random.choice([".", "?", "!"])
		return final_sentence

	except Exception as e:
		return f"Error generating sentence: {e}"

#-------------------------------------------------------------------
def make_text(rw_instance, num_sentences=5, num_paragraphs=1): # Pass rw_instance here
    text_paragraphs = []
    for _ in range(num_paragraphs):
        paragraph_sentences = []
        for _ in range(num_sentences):
            paragraph_sentences.append(make_sentence(rw_instance)) # Pass rw_instance to make_sentence
        text_paragraphs.append(" ".join(paragraph_sentences))
        
    return "\n".join(text_paragraphs)

#--------------------------------------------------
def preamble_random_word():

	random.shuffle(messages['preambles'])
	chosen_preamble = random.choice(messages['preambles'])
	random_word = rw.get_random_word()
	while not random_word or len(random_word) < 2 or not random_word.isalpha():
		random_word = rw.get_random_word()
        
	return f"{chosen_preamble} {random_word.lower()}.\n"

#-------------------------------------------------------------------
#---------------------------------------------------------------------------
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
def protect_image(input_filepath, output_directory="protected_images",
					noise_intensity=10, pixel_shift_amount=1,
					color_jitter_factor=0.05, jpeg_quality=90, add_symbol=False):
	
	if not os.path.exists(output_directory):
		os.makedirs(output_directory)

	try:
		img = Image.open(input_filepath).convert("RGB")
	except FileNotFoundError:
		print (f"{random.choice(messages['trouble_short'])} Input file not found. Action required: Verify the file name and path.\n")
		return
	except Exception as e:
		print(f"{random.choice(messages['trouble_short'])} Failed to open the image. Please ensure the file is valid and the path is correct.\n")
		return

	original_filename = os.path.basename(input_filepath)
	name, ext = os.path.splitext(original_filename)
	output_filename = f"{name}_protected{ext}"
	output_filepath = os.path.join(output_directory, output_filename)

	print(f"Processing image: {original_filename.upper()}{' with ▧ watermark' if add_symbol else ''}")
	
	width, height = img.size
	noise = Image.effect_noise((width, height), sigma=noise_intensity)
	noise_rgb = noise.convert("RGB")

	# alpha=0.95 means 95% original, 5% noise.
	img = Image.blend(img, noise_rgb, alpha=0.05)

	pixels = img.load()
	for y in range(height):
		for x in range(width):
			dx = random.randint(-pixel_shift_amount, pixel_shift_amount)
			dy = random.randint(-pixel_shift_amount, pixel_shift_amount)
			new_x = max(0, min(width - 1, x + dx))
			new_y = max(0, min(height - 1, y + dy))
			if (new_x, new_y) != (x, y):
				original_pixel = pixels[x, y]
				shifted_pixel = pixels[new_x, new_y]
				pixels[x, y] = shifted_pixel
				pixels[new_x, new_y] = original_pixel
	enhancers = [
		(ImageEnhance.Brightness, 1.0 + random.uniform(-color_jitter_factor, color_jitter_factor)),
		(ImageEnhance.Contrast, 1.0 + random.uniform(-color_jitter_factor, color_jitter_factor)),
		(ImageEnhance.Color, 1.0 + random.uniform(-color_jitter_factor, color_jitter_factor))
	]
	for enhancer_class, factor in enhancers:
		enhancer = enhancer_class(img)
		img = enhancer.enhance(factor)

	if add_symbol:
		draw = ImageDraw.Draw(img)
		symbol_text = "▧"
		
		# --- MODIFICATION: INCREASED FONT SIZE ---
		# Adjusted multiplier from 0.025/0.03 to 0.045 for a noticeable increase
		font_size = int(min(width, height) * 0.045) 

		font = None
		try:
			font_path = "arial.ttf" # Adjust this path if 'arial.ttf' isn't found
			font = ImageFont.truetype(font_path, font_size)
		except IOError:
			print(f"Warning: Font '{font_path}' not found. Using default font. Symbol '▧' may not render perfectly.")
			font_size = int(min(width, height) * 0.05) # Slightly larger for default fallback
			font = ImageFont.load_default()

		try:
			bbox = draw.textbbox((0, 0), symbol_text, font=font)
			text_width = bbox[2] - bbox[0]
			text_height = bbox[3] - bbox[1]
		except AttributeError:
			text_width, text_height = draw.textsize(symbol_text, font=font)

		margin = int(min(width, height) * 0.01)

		x_pos = width - text_width - margin
		y_pos = height - text_height - margin

		# --- MODIFICATION: CHANGED TO FULLY OPAQUE WHITE ---
		text_color = (255, 255, 255, 255) # RGBA: Fully opaque white

		if img.mode != 'RGBA':
			img = img.convert('RGBA')
		draw = ImageDraw.Draw(img)

		draw.text((x_pos, y_pos), symbol_text, fill=text_color, font=font)
	# --- END OF SYMBOL ADDITION ---

	try:
		if ext.lower() in ['.jpg', '.jpeg']:
			# JPEG doesn't support transparency, so convert back to RGB
			if img.mode == 'RGBA':
				img = img.convert('RGB')
			img.save(output_filepath, format="JPEG", quality=jpeg_quality)
		elif ext.lower() == '.png':
			# PNG supports transparency, so keep it as RGBA if it became so
			img.save(output_filepath, format="PNG")
		else:
			print(f"Warning: Unsupported output format '{ext}'. Saving as JPEG.")
			output_filename = f"{name}_protected.jpg"
			output_filepath = os.path.join(output_directory, output_filename)
			if img.mode == 'RGBA':
				img = img.convert('RGB')
			img.save(output_filepath, format="JPEG", quality=jpeg_quality)
		print(f"Protected image saved to: {output_filepath.upper()}\n")
	except Exception as e:
		print (f"{random.choice(messages['trouble_short'])} Error saving image {output_filepath}: {e}\n")
		
#-------------------------------------------------
def set_system_country():
	global system_country

	while True:
		user_input_code = input("Enter a two-letter country code to override (e.g., PT, US): ").upper()
		if not user_input_code:
			print ("")
			return False
		found_country_name = None
		for country_name, details in ncountries.items():
			if details.get("alpha2") == user_input_code:
				found_country_name = country_name
				break
		if found_country_name:
			system_country = (user_input_code, found_country_name.capitalize())
			print(f"System country set to: {system_country[1]} ({system_country[0]})\n")
			return True
		else:
			print(f"{random.choice(messages['trouble_short'])} Invalid country code. Please enter a valid two-letter code.\n")

#-------------------------------------------------
def view_system_country():
	
	global system_country
	global sysos
	
	if sysos.lower() == 'windows':
		if system_country != None:
			country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
		else:
			country = pycountry.countries.get(name=country_code)
	elif sysos.lower() == 'linux':
		if system_country != None:
			country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
		else:
			country = pycountry.countries.get(alpha_2=country_code)
	else:
		print(f"{random.choice(messages['trouble_short'])} This option is unavailable for {sysos.title()} system's.\n")
		return
	
	if country:
		country_2l = country.alpha_2
		country_name = country.name
		country_name_official = country.official_name
	else:
		print(f"{random.choice(messages['trouble_short'])} Set the country, type 'set default country' and then the two-letter country code.\n")
		return False, None
		
	if country != None:
		print(f"The default country is {country_name} - {country_2l}, {country_name_official}.\n")

#-------------------------------------------------
def list_country_details():
	if not ncountries:
		print(f"{random.choice(messages['trouble_short'])} I have an internal error. No country data available.\n")
		return

	COUNTRY_WIDTH = 40
	CAPITAL_WIDTH = 35
	ALPHA2_WIDTH = 10

	print (f"Here's some basic information i have about the {len(ncountries)} Countries i have in my knowledge:")
	print(f"\n{'Country':<{COUNTRY_WIDTH}} {'Capital':<{CAPITAL_WIDTH}} {'Alpha2 Code':<{ALPHA2_WIDTH}}")
	print("-" * (COUNTRY_WIDTH + CAPITAL_WIDTH + ALPHA2_WIDTH + 3)) # 2 for spaces between columns

	for country_name, details in ncountries.items():
		display_country_name = country_name.capitalize()
		capital = details.get("capital", "N/A")
		alpha2 = details.get("alpha2")
		if alpha2 is None:
			alpha2 = "N/A"
		# f-string with '<' for left-alignment and the defined width
		print(f"{display_country_name:<{COUNTRY_WIDTH}} {capital.title():<{CAPITAL_WIDTH}} {alpha2:<{ALPHA2_WIDTH}}")
	print("")

#-------------------------------------------------
def _fetch_remote_library():

	WEBSITE_URL = website['tvshow']
	#if not internet_onoff():
	#	print(f"✗ {random.choice(messages['trouble_msg'])} Network connection required. Using local list.")
	#	return []

	try:
		response = urllib.request.urlopen(WEBSITE_URL, timeout=5)
		html_content = response.read()
		html_string = html_content.decode("utf-8")
		soup = BeautifulSoup(html_string, 'html.parser')
		items_list = []

		tv_shows = soup.find_all('li', class_='zfr3Q TYR86d eD0Rn')
		for show in tv_shows:
			title_element = show.find('span', class_='C9DxTc')
			if title_element:
				items_list.append(title_element.text.strip())

		if items_list:
			print(f"✔  Successfully loaded {len(items_list)} shows from {WEBSITE_URL}\n")
			return items_list
		else:
			print(f"✗ {random.choice(messages['trouble_msg'])} Found page, but no TV shows matched the scrap pattern. Using local list.")
			return []

	except urllib.error.URLError as e:
		return []
	except Exception as e:
		return []

#-------------------------------------------------
def get_show_library():
	global my_library

	remote_list = _fetch_remote_library()
	if remote_list:
		my_library = remote_list
	else:
		if not my_library or len(my_library) == 0:
			my_library = ["(Error: No Shows Available)"]
		else:
			print(f"✔  Successfully loaded {len(my_library)} shows from the database list.\n")
	return my_library

#-------------------------------------------------
def generate_console_schedule(start_hour=20, start_minute=0, num_slots=4, slot_duration_minutes=75):
	MESSAGES = messages
	try:
		my_library = get_show_library()	
		today = datetime.now().date()
		current_datetime = datetime.combine(today, datetime.min.time())
		current_datetime = current_datetime.replace(hour=start_hour, minute=start_minute)
		slot_duration = timedelta(minutes=slot_duration_minutes)
		schedule = []
		last_show = None
		for _ in range(num_slots):
			available_shows = [s for s in my_library if s != last_show]
			if not available_shows:
				next_show = last_show
			else:
				next_show = random.choice(available_shows)

			end_datetime = current_datetime + slot_duration

			schedule.append({
				"start": current_datetime.strftime('%H:%M'),
				"end": end_datetime.strftime('%H:%M'),
				"show": next_show
			})

			current_datetime = end_datetime
			last_show = next_show

		max_show_length = 20
		if schedule:
			max_show_length = max(len(entry['show']) for entry in schedule)
		show_col_width = max(max_show_length + 2, 20)
		total_line_width = 2 + 6 + 3 + 6 + 3 + show_col_width + 2
		print("--- 📺 Gridflow Flow ---")
		print(f"Start Time: {start_hour:02}:{start_minute:02}")
		print(f"Slots: {num_slots} | Duration: {slot_duration_minutes} min")
		print("-" * total_line_width)
		header_format = f"| {'Start':<6} | {'End':<6} | {'The Flow Pick':<{show_col_width}} |"
		print(header_format)
		print("-" * total_line_width)
		for entry in schedule:
			row_format = f"| {entry['start']:<6} | {entry['end']:<6} | {entry['show']:<{show_col_width}} |"
			print(row_format)
		print("-" * total_line_width)
		print("")
		
		return schedule

	except Exception as e:
		print(f"\nCRITICAL ERROR during schedule generation: {e}")
		return None

#-------------------------------------------------
def get_remote_version_and_revision_from_file():
	github_file_url = kdecode(GITHUB, shift)
	try:
		response = requests.get(github_file_url)
		response.raise_for_status()      
		content = response.text       
		version_match = re.search(r"version\s*=\s*['\"]([^'\"]+)['\"]", content)
		revised_match = re.search(r"_revise_\s*=\s*['\"]([^'\"]+)['\"]", content) # Corrected: _revise_
		remote_version = version_match.group(1) if version_match else None
		remote_revised = revised_match.group(1) if revised_match else None
		if not version_match:
			print(f"Warning: Could not find 'version = ' in {github_file_url} on GitHub.")
		if not revised_match:
			print(f"Warning: Could not find '_revise_ = ' in {github_file_url} on GitHub.") # Corrected: _revise_
		return remote_version, remote_revised
	except requests.exceptions.RequestException as e:
		print (f"{random.choice(messages['trouble_short'])} Error fetching remote version and revision: {e}\n")
		return None, None
	except Exception as e:
		print (f"{random.choice(messages['trouble_short'])} Unexpected error occurred while getting remote version and revision: {e}\n")
		return None, None

#-------------------------------------------------
def check_for_updates():

	if internet_onoff() == True:
		local_version_str = version    
		local_revised_str = datetime.now().strftime('%d.%m.%Y')
		remote_version_raw, remote_revised_raw = get_remote_version_and_revision_from_file()
		remote_version_str = remote_version_raw.strip() if remote_version_raw else None
		remote_revised_str = remote_revised_raw.strip() if remote_revised_raw else None
		if remote_version_str is None:
			print (f"{random.choice(messages['trouble_short'])} Could not check for updates. Skipping version comparison.\n")
			return
		try:
			if local_version_str == remote_version_str and local_revised_str == remote_revised_str:
				print (f"You have the latest available {remote_version_str} from {remote_revised_str} version. {kolor['BOLD_GREEN']}{random.choice(messages['msg_welldone']).upper()}!{kolor['OFF']}\n")
			elif local_version_str > remote_version_str or local_revised_str > remote_revised_str:
				print (f"You have a superior version {remote_version_str} from {remote_revised_str}. {kolor['BOLD_RED']}{random.choice(messages['qualify_adj']).upper()}!{kolor['OFF']} \n")
			elif local_version_str < remote_version_str or local_revised_str < remote_revised_str:
				print (f"{kolor['RED']}Atention!{kolor['OFF']} Your current version, {local_version_str} from {local_revised_str}, {kolor['BOLD_YELLOW']}is outdated.{kolor['OFF']}\n")
			else:
				print(f"{random.choice(messages['trouble_short'])} Could not retrieve the data from the remote revision for comparison.")
		except Exception as e:
			print (f"{random.choice(messages['trouble_short'])} Error comparing versions or revisions: {e}\n")
	else:
		print (f"{random.choice(messages['trouble_short'])} I cannot compare versions due to not having an active internet connection.\n")

#-------------------------------------------------
def validate_connection(port):
	# Obtém lista de todas as portas série ativas
	import serial.tools.list_ports
	active_ports = [p.device for p in serial.tools.list_ports.comports()]
    
	if not port:
		return False
  
	if port in active_ports:
		return True
	else:
		#available = ", ".join(active_ports) if active_ports else "Nenhuma"
		return False

#-------------------------------------------------
#-------------------------------------------------
def main():
	global _poigps_, lat, lon, aboutyou, days, dblrconn, dbmsgbl, _portac_, _pydr3_, sysos
	#----------------------------
	if not check_tables(tables):
		exit()
	print_statusline(f"{dbmsgbl}...")
	make_intextdb()
	print_statusline(f"{dbmsgbl}...")
	#----------------------------
	wms = random.choice(core['intromsg'])
	tdctl=0;ncctl=0;ffctl=0;kuote=quote()
	aboutyou = kdecode(aboutyou, checksum)
	#----------------------------
	validate_globals()
	#----------------------------
	print_statusline(f"")
	_portac_ = get_default_port()
	#----------------------------
	drawart('art_cybele')
	print(f"\n{kolor[('YELLOW')]}{wms}\n\n{kolor['BLUE']}I am {kolor['RED']}{_title_} {kolor['RED']}{'\u269d'}{kolor['BLUE']} a {website['home'][8:]}{_cyext_}{kolor['OFF']}")
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
			source_list = [list(core["qa-astro"]), questions, others]
			list_source = generate_random_questions(source_list, random.randint(1, 4))
			for source in list_source:
				print (f" {_spchar_[1:2]} {source}")
			print ("")
		#-------------------------
		if question == "bye" or question == "exit" or question == "quit":
			return False
		
		elif any(word in question for word in core['asking for a word']):
			print (preamble_random_word())

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
		
		elif any(word in question for word in core['information state']):
			random.shuffle(core['information state awnsers'])
			print (f"{random.choice(core['information state awnsers'])}\n")
		
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
			   print("The word idea was me until "+ _author_.split()[0] +" started to develop me.\nAhah and just for fun!\n")

		elif question == 'what can i ask you' or question == 'what can you anwser' or question == 'what do you know' or question == "what do you know about'it" or question == 'what can you do' or question == 'what do you do' or question =='what you can do':
			print (random.choice(core['cthemes']) + ": \n")
			random.shuffle(topics)
			last_topic = len(topics)-1
			for i in range(last_topic):
				print ( "   - " + topics[i].title())
			print ("  and: ")
			print ("   " + topics[last_topic].title() + ", " + random.choice(messages['endterm']).lower() + ".\n")

		elif question == "show topics" or question == "show me your topics" or question == "show topic's" or question == "show me your topic's" or question == "topics" or question == "topic's":
			print (random.choice(core['cthemes']) + ": \n")
			random.shuffle(topics)
			last_topic = len(topics)-1
			for i in range(last_topic):
				print ( "   - " + topics[i].title())
			print ("  and: ")
			print ("   " + topics[last_topic].title() + ", " + random.choice(messages['endterm']).lower() + ".\n")

		elif question[-5:] == 'quote':
			if 'adelino' in question or 'as' in question:
				print ("Here's a quote by my author " + _author_.split()[0] + ".")
				print (f"{_spchar_[18:19]} {random.choice(as_quotes)}")
				print ("")
			else:
				print(f"\n{_spchar_[2:3]}{kuote['quote']}{_spchar_[3:4]}\n{kuote['author']}\n")

		elif question == "what is" or question == "do you know what is" or question == "meaning of":
			what_creative= ["","I think you were trying to know something, righ ?!\n","Are you trying to ask or know something ?!\n","You were going to ask for knowledge weren't you? ?!\n","Well, to know or question you need a matter !\n"]
			cquestion = random.choice(what_creative)
			print ( "What?! " + cquestion + "In my case just type without the usual formalities... if i have the knowledge i will anwser.\n")

		elif question.startswith(('show me', 'tell me', 'list me')):
			if 'astronomy terms' in question or 'astronomy glossary' in question:
				print (f"{showlisttell(core["astronomy glossary"], num_terms=5, category="terms")}.\n")
			
			elif 'astronomy questions' in question or 'questions of astronomy' in question:
				all_astro = core["qa-astro"]
				random.shuffle(all_astro)
				astro_random_keys = all_astro[:3]
				astro_qa = ""
				for term in astro_random_keys:
					astro_qa += " "+_spchar_[1:2] + term + "?\n"
				print ("There are some astronomy questions you can make'me:\n\n" + astro_qa.title()[:-2] + "?\n")
	
			elif 'stars' in question or 'star names' in question:
				print (f"{showlisttell(core["star name"], num_terms=5, category="Stars names")}.\n")

			elif 'asteroids' in question:
				print (f"{showlisttell(core["asteroid"], num_terms=5, category="asteroids")}.\n")
			
			elif 'dangerous objects' in question:
				print (f"{showlisttell(core["cneos"], num_terms=5, category="Dangerous Objects")}.\n")

			elif 'old' in question or 'tech' in question:
				print (f"{showlisttell(core["old_tech_term"], num_terms=5, category="old Tech terms")}.\n")

			elif 'constellations' in question:
				print (f"{showlisttell(core["constelattion"], num_terms=5, category="Constellations")}.\n")

			elif 'climate' in question or 'dictionary' in question:
				print (f"{showlisttell(core["climate dictionary term"], num_terms=5, category="Climate Dictionary terms")}.\n")

			elif 'meaning term' in question or 'meaning words' in question or 'meaning terms' in question:
				print (f"{showlisttell(core["word meaning"], num_terms=5, category="Meaning Terms/Words")}.\n")
			
			elif 'constellations' in question and 'all' in question:
				print ("\nHere are all Constellations i have in knowledge ("+str(len(constellations_dict))+") and the meaning of her name or her designation:\n")
				for constelattion in constellations_dict:
					print(" %s: %s" % (constelattion.title(), constellations_dict[constelattion]))
				print ("")

			elif 'linux commands' in question:
				print (f"{showlisttell(core["linuxcmd"], num_terms=5, category="Linux commands")}.\n")
				
			elif 'verbs' in question or 'english verbs' in question:
				print (f"{showlisttell(knowledge["verb_base"], num_terms=5, category="some English verbs")}, that you can <conjugate>.\n")

		elif question == 'astronomy questions' or question == 'questions of astronomy':
			all_astro = core["qa-astro"]
			random.shuffle(all_astro)
			astro_random_keys = all_astro[:3]
			astro_qa = ""
			for term in astro_random_keys:
				astro_qa += " "+_spchar_[1:2] + term + "?\n"
			print ("There are some astronomy questions you can make'me:\n\n" + astro_qa.title()[:-2] + "?\n")

		elif question[0:8] == 'how many' and question.find('glossary')!=-1 or question.find('astronomy terms')!=-1 or question.find('anwser')!=-1:
			print ("I can tell you the meaning of " + str(len(core["astronomy glossary"])) + " Astronomy glossary terms." + "\n")
		elif question[0:8] == 'how many' and question.find('asteroids')!=-1 and question.find('you know')!=-1 or question.find('anwser')!=-1:
			print ("I can tell you about " + str(len(core['asteroid'])) + " Asteroids, but there are millions and those we dont know.. yet.\n")
		elif question[0:8] == 'how many' and question.find('dangerous')!=-1 and question.find('objects')!=-1 and question.find('you know')!=-1 or question.find('anwser')!=-1:
			print ("I can tell you about " + str(len(core['cneos'])) + " dangerous objects, but there much more beside those we dont know.. yet.\n")
		elif question[0:8] == 'how many' and question.find('star')!=-1 and question.find('names')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge " + str(len(core['star name'])) + " Stars. " + random.choice(messages['endterm']) + "\n")
		elif question[0:8] == 'how many' and question.find('linux commands')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge " + str(len(core['linuxcmd'])) + " Linux commands. " + random.choice(messages['endterm']) + "...\n")
		elif question[0:8] == 'how many' and question.find('verbs')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge " + str(len(knowledge['verb_base'])) + " verbs. " + random.choice(messages['endterm']) + "...\n")	
		elif question[0:8] == 'how many' and question.find('capitals')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge i know " + str(len(core['capital']) + 5) + " capitals and " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")
		elif question[0:8] == 'how many' and question.find('countries')!=-1 and question.find('you know')!=-1:
			print ("Actualy based on my knowledge i know " + str(len(core['capital'])) + " countries. " + random.choice(messages['endterm']) + "...\n")

		elif question[0:9] == "days till" or question[0:8] == "days for" or question[0:7] == "days to":
			if len(question.split()[2:]) == 0:
				print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Till What!? \n")
			else:
				subevent = " ".join(question.split()[2:])
				eventdays = days_to_event(subevent.replace(" ",""))
				if eventdays != 0:
					if subevent[-8:] == "birthday":
						select_creator = random.choice(["my creator "+_author_,"my creator "+_author_.split()[0],"my creator"])
						print ('To yours i dont know, but to the ' + select_creator + ' are '+ eventdays +' days.\n')
					elif eventdays != 0:
						print ("%s left for %s\n" % (eventdays, subevent.title()))
				else:				
					print (random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " Till What!? '"+ subevent + "' "+ random.choice(messages['short_no']) + "\n")				

		elif question[0:15] == 'difference from' or question[0:9] == 'diff from' or question[0:8] == 'age calc':
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
			print ("I can tell you the solar system, information about planets, distances and the meaning of " + str(len(core["astronomy glossary"])) + " Astronomy terms." + "\n")

		elif question[0:22] == 'what do you know about' and question.find('asteroids')!=-1 or question.find('celestial bodys')!=-1:
			print ("I can tell you about " + str(len(core['asteroid'])) + " asteroids. Only the most basic information.")
			print (f"More extended and comprehensive data can be found in {kolor['BLUE']}https://www.spacereference.org/{kolor['OFF']} or {kolor['BLUE']}https://www.datastro.eu{kolor['OFF']} \n")

		elif question[0:22] == 'what do you know about' and question.find('constellations')!=-1 or question.endswith('?'):
			print ("I can tell you about " + str(len(constellations_dict)) + " constelations.\n ")

		elif question[0:22] == 'what do you know about' and question.find('the')!=-1 and question.find('universe')!=-1 or question.endswith('?'):
			print ("The solar system, information about planets, distances and the meaning of " + str(len(core["astronomy glossary"])) + " Astronomy terms, " + str(len(core['asteroid'])) + " asteroids (most basic information) and " + str(len(constellations_dict)) + " constelations.\n")

		elif question[0:22] == 'what do you know about' and question.find('dangerous')!=-1 and question.find('objects')!=-1:
			print ("I can tell you about " + str(len(core['cneos'])) + " celestial dangerous objects known as the list CNEO.\n ")

		#elif question == 'can you' and question.find("sentence")!=-1 or question.find("phrase")!=-1:
		#	if question[0:4] == 'make':
		#		print ("This is a sentence! And I'm even not using NLP.\n")
		#	else:
		#		print ("Yes, I can! See? This is a sentence! And I'm even not using NLP.\n")

		elif question.find('elysia created')!=-1 or question.find('elysia was created')!=-1 or question.find('elysia went online')!=-1:
			print("The website [elysia] was created in {} doing it online for {} days until today.\n".format(str(date(2010,12,9).strftime("%d.%m.%Y")), (date.today() - date(2010,12,9)).days))

		elif any(word in question for word in core['question_word']) and "you born" in question:
			print ("I borned from the code of my predecessor, Zorie, in early 2023 and I was officially actived " + str(days_till_today.days) + " days ago with an updated in " + _revise_ + ", so you better do the math!\n")

		elif any(word in question for word in core['question_word']) and any(word in question for word in core['planet']) and not "version" in question:
			print (random.choice(list(messages['magic_anwser'])) % "planet")
		elif any(word in question for word in core['question_word']) and any(word in question for word in core["old_tech_term"]) and not "version" in question:
			print (random.choice(list(messages['magic_anwser'])) % "old term and word" )
		elif any(word in question for word in core['question_word']) and any(word in question for word in core['constelattion']) and not "version" in question:
			print (random.choice(list(messages['magic_anwser'])) % "constellations")
		elif any(word in question for word in core['question_word']) and any(word in question for word in core['astronomy glossary']) and not "version" in question:
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
			_poigps_[4] = 1
			if _poigps_[4] == 1:
				print(' > default GPS coordinates restored.')
				print(f"{kolor['BOLD_WHITE']}  Latitude : {str(_poigps_[0])} {kolor['OFF']}")
				print(f"{kolor['BOLD_WHITE']} Longitude : {str(_poigps_[1])} {kolor['OFF']}")
				print("")
			else:
				print(' > the default GPS coordinates are defined to user input.\n')
				
		elif question == 'set default gps off':
			print(' > default GPS coordinates defined to user input.\n')
			_poigps_[3] = 0
			_poigps_[4] = 0
			
		elif question == 'show default gps' or question == 'view default gps':
			if _poigps_[4] == 0:
				print (' > stored default information is empty!\n')
			else:
				print (f"\n{kolor['BOLD_CYAN']} #default stored GPS coordinates {kolor['OFF']}")
				print (f"{kolor['BOLD_WHITE']}  Latitude : {str(_poigps_[0])} {kolor['OFF']}")
				print (f"{kolor['BOLD_WHITE']} Longitude : {str(_poigps_[1])} {kolor['OFF']}")
				if _poigps_[1] == lat:
					print (f" Defaults gps coordinates loaded from {kolor['BOLD_WHITE']}user input.{kolor['OFF']}\n")
				else:
					print (f" Defaults gps coordinates loaded thru {kolor['BOLD_WHITE']}my own code.{kolor['OFF']}\n")

		elif question == 'set default country':
			set_system_country()
		
		elif question == 'default country':
			view_system_country()
		
		elif question == 'default country off':
			global system_country
			if system_country != None:
				print(' > default system country detection restored.\n')
				system_country = None
			else:
				print('No user override is being used in the country system detection, so it is not applicable.\n')
		
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
			if sysos.lower() == 'windows':
				os.system('cls')
			elif sysos.lower() == 'linux':
				os.system('clear')
			else:
				print ("Sorry i cannot execute this command in a unidentified S.O for me!\n")

		elif question == 's.o' or question == 'operating system' or question == 'system':
			if sysos == 'Linux':
				print ("This is the " + sysos + " Operating System (OS). ")
			elif sysos == 'Windows':
				print ("I am behing executed in " + sysos +  "Operating System (OS).\n")
			else:
				print ("Sorry i cannot identify this Operating System. Maybe in my next update!\n")

		elif question == "can you help me" or question == "can you help" or question == "help" or question == "help me":
			print(f"Here are the {str(len(core['help']))} help 🙋 commands ordered alphabetically to better assist you. \nJust type help <desired command> to get a more descriptive help.\n")
			nhelp = dict(sorted(help.items()))	
			results = list(nhelp)
			terminal_width = os.get_terminal_size().columns
			max_item_width = max(len(str(item)) for item in results)
			if max_item_width + 1 < terminal_width:
				items_per_line = terminal_width // (max_item_width + 1)
			else:
				items_per_line = 1
			items_per_line = max(1, items_per_line)
			column_widths = [0] * items_per_line
			for i in range(len(results)):
				column_index = i % items_per_line
				column_widths[column_index] = max(column_widths[column_index], len(str(results[i])))
			for i in range(0, len(results), items_per_line):
				line = results[i:i + items_per_line]
				output_parts = []
				for j, item in enumerate(line):
					padded_item = str(item).ljust(column_widths[min(j, len(column_widths) - 1)])
					output_parts.append(padded_item)
				print("  ".join(output_parts))
			print("")
			
		elif any(word in question for word in core['season_query']):
			print("")	

		elif any(word in question for word in core['time_query']):
			print("")

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
				print ("In name of elysia " + random.choice(messages['birthday_msg']))
				print ("elysia, {} personal website went online makes {} years ago on this same day.\n".format(_author_.split()[0] , date.today().year - date(2010,12,9).year))
			else:
				print(f"To who?! To Me ?!")
				print(random.choice(messages['birthday_short']) + " Are trying to trik me, hmm! Its "+month_name+", "+date.today().strftime("%d")+". BAD " + os.getlogin().upper() + "!\n")

		elif question == 'merry christmas' or question == 'i wish you a merry christmas':
			dt = date.today()
			if dt.month == 12 and dt.day >= 22 and dt.day <= 26:
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
		
		elif question.find('happy valentines')!=-1 or question.find('happy valentine')!=-1:
			dt = date.today()
			if (str(dt)[5:]) == '02-14':
				ascii_vday = ["˚˖𓍢ִ໋🌷͙֒✧˚.🎀༘⋆","𓍢ִ໋🌷͙֒₊˚*ੈ♡⸝⸝🪐༘⋆","˚˖𓍢ִႋ🌷͙֒✧🩷˚.🎀༘⋆","🏹⁀➴'","🍒💌♥️🌹","🎀🧸💕"]
				random.shuffle(messages['valentinesmsg'])
				print (f"{random.choice(messages['valentinesmsg'])} {random.choice(ascii_vday)}\n")
			else:
				random.shuffle(messages['notvalentines'])
				print( random.choice(messages['notvalentines']) + "\n")
		
		elif question == 'what is your version' or question == 'cybele version' or question == '#version':
			global cybelecode, idcode
			cybelecode = ksha([_title_.lower()+chr(46)+chr(112)+chr(121)])[0][1]
			_chkwww_ = 'online' if internet_onoff() else 'offline'
			_chkcid_ = cybelecode if cybelecode else 'Not verified'
			chkids = "and this isn't my original source code" if idcode != _chkcid_ else 'running via my original source code'
			nversion = f"I am {_title_} {_chkwww_} in version {version} last updated on {_revise_} running for {days_till_today.days} days.\nmy unique id is '{_chkcid_}' {chkids}."
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
					_poigps_[0] = latgps
					lat = _poigps_[0]
					longps = float(input('What is your longitude coordinates: '))
					if longps > 180 or longps < -180:
						print("The longitude degrees format are out of range!\n")
						continue
					_poigps_[1] = longps
					lon = _poigps_[1]
					defgps = 'user input'
				except ValueError:
					print("Value not recognized like latitude or longitude gps coordinates!\n")
					continue
				#else:
			defgps = 'default gps'
			_poigps_[3] = 1
			_poigps_[4] = 1
			if country_code:
				print (f"calculations for {str(_poigps_[0])}, {str(_poigps_[1])} ({country_code}) to UTC using {defgps}")
			else:
				print (f"calculations for {str(_poigps_[0])}, {str(_poigps_[1])} to UTC using {defgps}")

			drawart('art_world')

			sun_emoji = ["☀️","🌑","🌕","🌅"]
			s = Sun(datetime.now(), _poigps_[0], _poigps_[1])
			print(f"  {_spchar_[1:2]}    Sunrise {sun_emoji[0]} :  {str(s.sunrise())}")
			print(f"  {_spchar_[1:2]} Solar noon️{sun_emoji[1]} :  {str(s.solarnoon())}")
			print(f"  {_spchar_[1:2]}     Sunset {sun_emoji[3]} :  {str(s.sunset())}")
			print("")
			
		elif question == 'moon phase' or question == 'what is the moon phase' or question =='what is the actual moon phase':
			if _poigps_[3] == 0:
				try:
					mlatgps = float(input('\nWhat is your latitude coordinates: '))
					if mlatgps > 90 or mlatgps < -90:
						print("The latitude degrees format are out of range!\n")
						continue
					_poigps_[0] = mlatgps
					lat = _poigps_[0]
					mlongps = float(input('What is your longitude coordinates: '))
					if mlongps > 180 or mlongps < -180:
						print("The longitude degrees format are out of range!\n")
						continue
					_poigps_[1] = mlongps
					lon = _poigps_[1]
				except ValueError:
					print("Value not recognized like latitude or longitude gps coordinates!\n")
					continue
				#else:
			_poigps_[3] = 1
			_poigps_[4] = 1
			moon_phase = MoonPhase(_poigps_[0], _poigps_[1], datetime.now())
			print(f"Currently the moon phase is {moon_phase.phase_of_moon()} \n")

		#elif re.compile(r'\b(?:diagnostics|show(?:\s+me)?(?:\s+your)?\s+core|#core)\b',re.IGNORECASE).search(question):
		elif question == 'show core' or question == 'show info' or question == '#info' or question == "#core":
			print(f"{kolor['BOLD_CYAN']}{random.choice(messages['info_intromsg'])}{kolor['OFF']}\n")
			try:
				display_node_name = platform.node().upper() if node_name else "unidentified device"
				display_cyext = _cyext_[0:4].replace(" ","") if len(_cyext_) >= 4 else "N/A"
				core_system_country = "Undetectable"
				if system_country is not None:
					core_system_country = system_country[1]
				elif country_code not in (None, "C", ""):
					core_system_country = country_code
				py_version_str = "N/A"
				if 'pyver' in globals() and isinstance(pyver, tuple) and len(pyver) >= 3:
					py_version_str = f"{pyver[0]}.{pyver[1]}.{pyver[2]}"
				elif hasattr(sys, 'version_info'):
					py_version_str = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
				q_len = len(questions) if 'questions' in globals() and isinstance(questions, (list, tuple)) else 0
				a_len = len(answers) if 'answers' in globals() and isinstance(answers, (list, tuple)) else 0
				current_midbcounter = midbcounter if 'midbcounter' in globals() else 0
				total_core_sum = 0
				if isinstance(core, dict):
					for value in core.values():
						if isinstance(value, (list, dict, tuple, str)):
							total_core_sum += len(value)
				total_knowledge_sum = 0
				if isinstance(knowledge, dict):
					for value in knowledge.values():
						if isinstance(value, (list, dict, tuple, str)):
							total_knowledge_sum += len(value)
				days_running_str = "N/A days."
				if 'days_till_today' in globals() and hasattr(days_till_today, 'days'):
					days_running_str = f"{days_till_today.days} days."
				if _pydr3_ == True:
					sysos = "Pydroid3"
				else:
					_pydr3_ = _pydr3_

				print(f"   Device : {display_node_name}|{display_cyext} on {sysos}")
				print(f"     Name : {_title_}")
				print(f"  Version : {version}")
				print(f"  Revised : {_revise_}")
				print(f"   Python : {py_version_str}")
				print(f"  Country : {core_system_country}")
				print(f"   Memory : {q_len}|{a_len}|D{current_midbcounter}")
				print(f"     Data : {total_core_sum}|O{len(core.get('old_tech_term', []))}|M{len(core.get('word meaning', []))}|V{total_knowledge_sum}")
				print(f"    Linux : {len(core.get('linuxcmd', []))}")
				print(f"    Astro : G{len(core.get('astronomy glossary', []))}|A{len(core.get('asteroid', []))}|C{len(core.get('constelattion', []))}|S{len(core.get('star name', []))}|CNEOS:{len(core.get('cneos', []))}")
				print(f"    World : {len(core.get('country', []))}")
				print(f"  Storage : {dblrconn}")
				print(f"  Running : {days_running_str}\n")

			except Exception as e:
				print(f"{kolor['BOLD_RED']}ERROR:{kolor['OFF']}Could not display info. Data might be incomplete or an unexpected issue occurred\n")

		# == "today activity":
		elif re.compile(r'\b(today activity)\b', re.IGNORECASE).search(question):
			if tdctl >= 3:
				print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['activity_msg'])}\n")
			else:
				random_season_activity()
				tdctl = tdctl + 1

		# == "today"
		elif re.compile(r'\b(date|today(?: is)?|what is the date|what is today)\b(?!.*holiday)', re.IGNORECASE).search(question):
			now = datetime.now()
			iniyeardays = datetime.now().timetuple().tm_yday
			current_time = now.strftime("%H:%M")
			days_left = days_in_year() - iniyeardays
			is_holiday, holiday_name = today_holiday()
			
			print(f"Today is {days[weekdaydate]}, {date.today().strftime('%d')} {month_name} of {date.today().strftime('%Y')} and currently {current_time} - {whatgmt()}")					
			print(f"Is the day {iniyeardays} from the week {date.today().isocalendar()[1]}, with {days_left} days left until the end of {date.today().year} ({leapyear()}).")
			
			special_info = special_dates(datetime.now())
			if is_holiday == True:
				mensagem = f"{_spchar_[18:19]} Today is {holiday_name}"    
				if special_info is not None:
					mensagem += f" and also is {special_info}."
			else:
				if special_info is not None:
					mensagem = f"{_spchar_[18:19]} Today is {special_info}"
			if is_holiday == True or special_info is not None:
				print(f"{mensagem} \n")
			else:
				print("")
		
		elif question == 'today holiday':
			is_holiday, holiday_name = today_holiday()
			special_info = special_dates(datetime.now())
			if is_holiday == True:
				mensagem = f"{_spchar_[18:19]} Today is {holiday_name}"    
				if special_info is not None:
					mensagem += f" and also is {special_info}."
			else:
				if special_info is not None:
					mensagem = f"{_spchar_[18:19]} Today is {special_info}"
			if is_holiday == True or special_info is not None:
				print(f"{mensagem} \n")
			else:
				print(f"Today is neither a holiday nor a 'special' date.\n")
		
		elif question == 'leap year' or question == 'is this year a leap year':
			print (f"The actual year ({int(next_year)-1}) {leapyear()}. \n")
	
		#-------------------------------------- convert ----------------------------------------
		
		elif question.startswith('convert'):
			match = re.search(r'(\d+\.?\d*)\s*([a-zA-Z\s]+?)(?:\s+(?:to|in)\s+([a-zA-Z\s]+))?$', question.lower().strip())
			original_value_str = None
			original_unit_from = None
			if match:
				original_value_str, original_unit_from_raw, _ = match.groups()
				original_unit_from = original_unit_from_raw.strip()
			else:
				match_simple = re.search(r'convert\s+(\d+\.?\d*)\s*([a-zA-Z\s]+?)$', question.lower().strip())
				if match_simple:
					original_value_str, original_unit_from_raw = match_simple.groups()
					original_unit_from = original_unit_from_raw.strip()
			converting = convert_units(question)
			if converting[0] is None:
				print(f"{converting[1]}") # Print the error message
			else:
				converted_value, target_unit = converting
				if original_value_str and original_unit_from:
					print(f"Based on my calculations {original_value_str} {original_unit_from} is {converted_value} {target_unit}.\n")
				else:
					print(f"Based on my calculations {converted_value} {target_unit}.\n")

		#---------------------------------------------------------------------------------------

		elif question == 'how many weeks have a year' or question == 'year weeks':
			print ( str(daysweeks_year()[1]) + " weeks. A calendar year consists of " + str(daysweeks_year()[1]) + " weeks, " + str(daysweeks_year()[0]) + " days in total.\n" )

		elif re.compile(r'\b(week|current week|week #?num(?:ber)?|what week)\b').search(question):
			print (f"Based on the system actual date this is the {str(date.today().isocalendar()[1])} week of the year.\n")
		
		elif question.find('update') != -1 and (question.find('last') != -1 or question.find('check') != -1):
			check_for_updates()

		elif question == 'yes':
			if len(csugestions) == 0:
				print ("Yes! what ? What do you mean ?\n")
			elif len(csugestions) == 1:
				print ("Yes! hmm...")
				question = csugestions[0]
				print ("So, the question you want to make'me is [" + question + "]\nNow you know what to write to ask'me.\n" )
			else:
				print ("Yes what ?! There are infinite possibilities! \nSo better write down the one you want to ask'me. \nI'm "+_title_+" a chat bot by "+ _author_.split()[0] +" not the f* Merlin, the wizard.\n")

		elif question[0:13] == 'search askard':
			getparam = question.split()
			if len(getparam) != 3:
				print ('The correct usage is: search askard <word>\n')
			else:
				try:
					mandb('cybele','askard_db','search',0,getparam[2])
					print ("")
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")
		
		elif question[0:11] == 'view askard':
			getparam = question.split()
			if len(getparam) != 3 or getparam[2].isnumeric() != True:
				print ('The correct usage is <view> ' + _spchar_[9:10] + ' askard <id>\n')
			else:
				try:
					mandb('cybele','askard_db','view',getparam[2],0)
					print ("")
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")
		
		elif question == 'fun fact' or question == 'fast fact':
			if ffctl >= 3:
				print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['nicefun_msg'])}\n")
			else:
				try:
					mandb('cybele','funfacts','view',0,0)
					ffctl = ffctl + 1
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")
				
		elif question[0:10] == 'nice thing':
			if ncctl >= 3:
				print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['activity_msg'])}\n")
			else:
				try:
					mandb('cybele','nicethings','view',0,0)
					ncctl = ncctl + 1
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")
				
		elif question[0:11] == 'list askard':
			getparam = question.split()
			if len(getparam) == 2:
				try:
					mandb('cybele','askard_db','list',0,0)
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")
			elif len(getparam) == 4 and getparam[2].isnumeric() == True and getparam[3].isnumeric() == True :
				try:
					mandb('cybele','askard_db','list',getparam[2], getparam[3] )
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")
			else:
				print ('The correct usage is <list askard> to make a complete list of all database or <start> <end>.\n')
				
		elif question[0:16] == 'search astronomy':
			getparam = question.split()
			if len(getparam) != 3:
				print ('The correct usage is: search astronomy <word>\n')
			else:
				try:
					mandb('cybele','astronomy_glossary','search',0,getparam[2])
					print ("")
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")

		elif question[0:14] == 'search oldtech':
			getparam = question.split()
			if len(getparam) != 3:
				print ('The correct usage is: search oldtech <word>\n')
			else:
				try:
					mandb('cybele','oldtech','search',0,getparam[2])
					print ("")
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")

		elif question[0:12] == 'list oldtech':
			getparam = question.split()
			if len(getparam) == 2:
				try:
					mandb('cybele','oldtech','list',0,0)
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")
			elif len(getparam) == 4:
				try:
					mandb('cybele','oldtech','list',getparam[2], getparam[3] )
				except ValueError as e:
					print(f"{random.choice(messages['trouble_short'])} There was a data corruption or a parsing issue during communication with your SQLite database.\n")
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
			if ncountries and internet_onoff() == True:
				cpopulation = get_thepopulation(country_name)
				if cpopulation is not None:
					print("Based on the online data from [{}] \n{} has a population of {:,} according to the Worldometers.\n".format(str(date.today().strftime("%d.%m.%y")), country_name.capitalize(), cpopulation))
			else:
				if country_name in core['country']:
					print("Estimated population based on my offline data from [{}] \n{} has a population of {:,} according to the United Nations.\n".format(_revise_, country_name.capitalize(), ncountries[country_name]["population"]))
				elif country_name == 'world' or country_name == 'earth':
					print ("8.1 billion people in July 2024 according to the United Nations. Is "+ core['months'][date.today().month-1].title() +", "+ str(date.today().year) +" so there must be quite a few more.\n")
				else:
					print ( random.choice(messages['trouble_short']) + " " + random.choice(messages['trouble_msg']) + " What ?! " + country_name.capitalize() + " Is that a new country? Perhaps! No-can do.\n")

		elif question.startswith('where is ') and ('iss' in question or 'zarya' in question):
			if internet_onoff() == False or internet_onoff() == None:
				print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['no_internet'])}\n")
			else:
				print (where_is_iss())

		elif question == 'people in space':
			if internet_onoff() == False or internet_onoff() == None:
				print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['no_internet'])}\n")
			else:
				people_in_space()

		elif question == 'what is he watching' or question == 'what are you watching':
			if question.find('fav')!=-1 or question.find('favorite')!=-1:
				print ("You can know what are "+_author_.split()[0]+"'s in her public profile.\n  > "+ website['trakt'] + "\n")
			else:
				print ("You can follow real time what "+_author_.split()[0]+" is watching by her profile.\n  > "+ website['trakt'] + "\n")
		
		elif question[-11:] == 'fav tvshows' or question[-16:] == 'favorite tvshows':
			if internet_onoff() == False or internet_onoff() == None:
				print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['no_internet'])}\n")
			else:
				print ('Based on the [' + website['tvshow'] + '] here are mine/'+ _author_.split()[0] + ' favorites:\n')
				extract_from_elysia('tvshow')

		elif question[-10:] == 'fav movies' or question[-15:] == 'favorite movies':
			if internet_onoff() == False or internet_onoff() == None:
				print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['no_internet'])}\n")
			else:
				print ('Based on the [' + website['tvshow'] + '] here are mine/'+ _author_.split()[0] + ' favorites:\n')
				extract_from_elysia('movies')
			
		elif question[-14:] == 'recent tvshows' or question[-22:] == 'recently added tvshows':
			if internet_onoff() == False or internet_onoff() == None:
				print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['no_internet'])}\n")
			else:
				print ('Based on the [' + website['tvshow'] + '] here they are the recently added:\n')
				recent_from_elysia()

		#elif question == "do you talk":
		elif any(word in question for word in core['asking for talking']):
			print("")

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
				if internet_onoff() == False or internet_onoff() == None:
					print (random.choice(messages['trouble_msg']) + " To get '" + star_name.capitalize() + " star' information i need an active Internet connection.\n")
				else:
					response = get_star_info(star_name)
					if len(response) != 0 and response[0] != 'emptydata':
						for i in range(len(response)):
							print (response[i])
					else:
						print( random.choice(messages['nostar_message']) + "cybele.star #" + star_name + " have empty data!\n")

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
			hemisphere = 'Northern Hemisphere' if lat >= 0 else 'South Hemisphere'
			weather_starters = [
				f"It looks like we're having {weather_like_season()} here in the {dayseason.capitalize()} on the {hemisphere}.\n",
				f"It's look like we're having {weather_like_season()} based in we're in the {hemisphere} {dayseason.capitalize()}.\n"
			]
			print(random.choice(weather_starters))

		elif question[-9:] == 'about you':
				print ("Ok!. My name is " + _title_ +" and I was maded by " + _author_.split()[0] + " " + str(days_till_today).replace(", 0:00:00","") + " ago. I was builded to be a extention of elysia, this website.\n" + aboutyou + "\n" )

		elif question[0:8] == 'presence':
			if any(word in question for word in presence_online):
				sub = question.split()[1:]
				if len(sub) == 0:
					print( random.choice(messages['trouble_msg']) + " I really have to learn or with AI to read users mind's!")
				else:
					service = ' '.join(sub)
					if service in presence_online:
						print ("Yes, " + _author_.split()[0] + " have a online presence on that service. Here is the direct link: \n "+_spchar_[1:2] + presence_online[service] + "\n")
			elif "services" in question:
				digifoot = str(len(presence_online))
				presence_online_abc = list(presence_online.keys())
				presence_online_abc.sort()
				print ("%s have a online presence or a digital footprint in this %s entities/services on the internet:\n" % (_author_.split()[0], digifoot))
				for service in presence_online_abc:
					print(" "*3 + _spchar_[4:5] + " " + service.title())
				print("")
			else:
				if len(presence_online) == 1:
					print( presence_online['online'] + "\n")
				else:
					print (random.choice(messages['trouble_msg']) + " I dont have any "+ _author_.split()[0] +" online presence information for the '" + " ".join(question.split()[1:]).title() + "' service.")

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

		elif question == 'actual country':
			sentence = f"Actualy based on "
			if sysos.lower() == 'windows':
				if system_country != None:
					country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
					sentence = sentence + f"user override"
				else:
					country = pycountry.countries.get(name=country_code)
					sentence = sentence + f"the system"
			elif sysos.lower() == 'linux':
				if system_country != None:
					country = pycountry.countries.get(alpha_2=system_country[0].split('_')[-1])
					sentence = sentence + f"user override"
				else:
					country = pycountry.countries.get(alpha_2=country_code)
					sentence = sentence + f"the system"
			else:
				print(f"{random.choice(messages['trouble_short'])} This option is unavailable for {sysos.title()} system's.\n")
			if country:
				sentence = sentence + f" the country is {country.name}, {country.alpha_2}."
			else:
				sentence = sentence + f" i cannot determine the country."	
			print (f"{sentence}\n")

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
				print (f"{random.choice(messages['trouble_msg'])} Incorrect usage parameter. Use: {question.split()[0]} {question.split()[1]} <number>.\n")
			else:
				if int(xtablenum[0]) > 999999:
					#print (f"{random.choice(messages['trouble_msg'])} Unfornunately my bit's are telling to do'it but my bytes to don't. Try a smaller!\n")
					print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['math_trouble'])}\n")
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
					
		elif any(word in question for word in core['asking the uptime']):
			print("")
		
		elif any(word in question for word in core['holidays_query']):
			print("")
		
		elif question[0:9] == 'conjugate':
			parts = question.split()[1:]
			if len(parts) != 1:
					print(f"{random.choice(messages['trouble_short'])} I recognize the command but not the syntax. Use: conjugate|conjuga <verb>\n")
			else:		
				if any(word in parts for word in knowledge['verb_base']):
					what_verb = parts[-1:][0]
					cybele_conjugator(what_verb)
				else:
					print(f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} {random.choice(['I dont recognize','I dont see'])} {kolor['BOLD_YELLOW']}{parts[-1:][0]}{kolor['OFF']} like a english verb!\n")
		
		elif question == 'trails':
			print (f"{random.choice(messages['trouble_short'])} {random.choice(messages['trouble_msg'])} I think what you are trying can be found here:")
			print (f"{website['trails']}\n")
		
		elif question == 'view solar system':
			terminal_width, terminal_height = os.get_terminal_size()
			ascii_horiz_solar_system(width=terminal_width-3)
			print ("")
			
		elif question[0:7] == 'protect':
			piaiparam = question.split()[1:]
			if len(piaiparam) != 2:
				print (f"{random.choice(messages['trouble_short'])} Missing or incorrect parameters. To learn how to use this command correctly, type: help protect image\n")
			else:
				input_image_path = piaiparam[-1:]
				custom_noise_intensity = 18
				custom_pixel_shift_amount = 2
				custom_color_jitter_factor = 0.04
				custom_jpeg_quality = 90
				if piaiparam[0] == 'image':
					add_symbol=False
					input_image_path = piaiparam[-1:][0]
				elif piaiparam[0] == 'mark':
					add_symbol=True
					input_image_path = piaiparam[-1:][0]
				else:
					print (f"{random.choice(messages['trouble_short'])} Incorrect usage. The correct usage is: protect image|mark <image filename>.<jpg|png|jpeg>\n")
					add_symbol=None
				if add_symbol != None:
					protect_image(input_image_path, noise_intensity=custom_noise_intensity,
									pixel_shift_amount=custom_pixel_shift_amount,color_jitter_factor=custom_color_jitter_factor,
									jpeg_quality=custom_jpeg_quality,add_symbol=add_symbol)
		
		elif question == 'offline mode on':
			db_url = sqlcodb.format(dbname_placeholder=_title_.lower())
			output_db_file = _title_.lower() + ".db"
			if os.path.exists(output_db_file):
				print(f"I am allready able to be fully functional in offline mode but i will up-to-date.")
				delete_cybeledb()
				download_and_convert(db_url, output_db_file)
			else:
				download_and_convert(db_url, output_db_file)
					
		elif question == 'offline mode off':
			delete_cybeledb()
		
		elif question == 'network status':
			if dblrconn[0:7] == "online" or dblrconn[0:7] == "offline":
				print(f"My network status at this moment is {dblrconn[0:7]}.\n")
			else:
				print (random.choice(messages['trouble_short']) + " This is a new designation of a connection type! I was not coded for this.\n")
		
		elif question == 'gridflow':
			generate_console_schedule()
		
		elif question == 'licence' or question.find(_title_.lower() + ' licence')!=-1:
			for i, line in enumerate(__doc__.splitlines()):
				if i >= len(__doc__.splitlines()) - 6:
					if i == 6:
						line = line.replace("# This","# " + __doc__.splitlines()[1][0:6] + " this")
					print(line)
			print ("")
				
		elif question.startswith(('mppt', 'solar')):
			if _pydr3_ == True:
				print(f"I'm currently running on Pydroid, where MPPT|Solar commands are unavailable.\nI'm ready to handle these once we're back on a compatible Linux setup!\n")
			elif len(question.split()[1:]) > 1:
				print(f"\r{kolor['CYAN']}HINT:{kolor['OFF']} '{question.split()[0]}' received {len(question.split()[1:])} parameters, which is more than expected.")
				print(f"Check usage with: {kolor['GREEN']}help {question.split()[0]}{kolor['OFF']}\n")
			else:
				args = question.split()[1:]
				
				victron = VictronMonitor()
				match args:
					case ['history', *_]:
						print(victron.get_historico_dia())   
					case ['last30', *_]:
						victron.importar_30_dias()  
					case ['monitor', *_]:
						if validate_connection(_portac_):
							victron.monitorizacao_ativa()
						else:
							print(f"\r{kolor['BOLD_RED']}ERRO:{kolor['OFF']} VE.Direct cable in {_portac_} not detected!\n")
					case []:
						print(f"\r{kolor['CYAN']}HINT:{kolor['OFF']} Command {question.upper()} It requires parameters. Try: {kolor['GREEN']}help {question.lower()}{kolor['OFF']}\n") 
					case _:
						print(f"\r{kolor['BOLD_RED']}ERROR:{kolor['OFF']} The parameter '{args[0]}' is invalid. Try: {kolor['GREEN']}help {question.split()[0]}{kolor['OFF']}\n")			
					
		elif question != '':
			answer = find_answer(question,questions)
			print(answer)
		
		#else:
		#	print (f"{core['trouble_short']} I'm not familiar with this subject!")

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
