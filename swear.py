"""
swear.py - Willie Anti-Swearing Module
Copyright 2013, Eldon McGuinness

http://willie.dftba.net
"""

from willie import module

WILDCARD_BASE = '[^\d\s\w\\\'\\",]|_'

WILDCARDS = {
	'a' : '(?:[Aa]|'+WILDCARD_BASE+')',
	'b' : '(?:[Bb]|'+WILDCARD_BASE+')',
	'c' : '(?:[Cc]|'+WILDCARD_BASE+')',
	'd' : '(?:[Dd]|'+WILDCARD_BASE+')',
	'e' : '(?:[Ee]|'+WILDCARD_BASE+')',
	'f' : '(?:[Ff]|'+WILDCARD_BASE+')',
	'g' : '(?:[Gg]|'+WILDCARD_BASE+')',
	'h' : '(?:[Hh]|'+WILDCARD_BASE+')',
	'i' : '(?:[iI\|17!]|'+WILDCARD_BASE+')',
	'j' : '(?:[Jj]|'+WILDCARD_BASE+')',
	'k' : '(?:[Kk]|'+WILDCARD_BASE+')',
	'l' : '(?:[Ll]|'+WILDCARD_BASE+')',
	'm' : '(?:[Mm]|'+WILDCARD_BASE+')',
	'n' : '(?:[Nn]|'+WILDCARD_BASE+')',
	'o' : '(?:[Oo0]|'+WILDCARD_BASE+')',
	'p' : '(?:[Pp]|'+WILDCARD_BASE+')',
	'q' : '(?:[Qq0]|'+WILDCARD_BASE+')',
	'r' : '(?:[Rr]|'+WILDCARD_BASE+')',
	's' : '(?:[Ss5]|'+WILDCARD_BASE+')',
	't' : '(?:[tT\|17]|'+WILDCARD_BASE+')',
	'u' : '(?:[uU]|'+WILDCARD_BASE+')',
	'v' : '(?:[Vv]|'+WILDCARD_BASE+')',
	'w' : '(?:[Ww]|'+WILDCARD_BASE+')',
	'x' : '(?:[Xx]|'+WILDCARD_BASE+')',
	'y' : '(?:[Yy]|'+WILDCARD_BASE+')',
	'z' : '(?:[Zz]|'+WILDCARD_BASE+')'
}

BADWORDS = [
	'anal','anus','arse','ass','asses','assclown','assfucker','assfuckers','assfuka','assfukas','asshole','assholes','asswhole','asswholes','ballsack','ballsacks','bastard','bastards','beastial','beastiality','bellend','bestial','bestiality','biatch','bitch','bitcher','bitchers','bitches','bitchin','bitching','blowjob','blowjobs','boiolas','boner','boners','buceta','butthole','buttholes','buttmuch','buttmuches','buttmuchers','buttplug','buttplugs','carpetmuncher','carpetmunchers','cawks','chink','chinks','cipa','clit','clits','clitoris','clitorises','cnut','cnuts','cock','cocks','cocksucker','cocksuckers','cockface','cockfaces','cockhead','cockheads','cockmunch','cockmunches','cockmuncher','cockmunchers','cocksuck','cocksucks','cocksucked','cocksucker','cocksuckers','cocksucking','cocksuka','cocksukas','cokmuncher','cokmunchers','coksucka','coksuckas','coon','coons','cox','coxs','cum','cummer','cumming','cums','cumshot','cumshots','cunilingus','cunt','cuntlick','cuntlicker','cuntlicking','cunts','cyberfuc','cyberfucs','cyberfuck','cyberfucks','cyberfucked','cyberfucker','cyberfuckers','cyberfucking','dick','dicks','dickhead','dickheads','dildo','dildos','duche','duchebag','duchebags','dyke','dykes','ejaculate','ejaculated','ejaculates','ejaculating','ejaculatings','ejaculation','ejakulate','ejakulated','ejakulates','ejakulating','ejakulatings','ejakulation','fuck','fucktard','fuk','fucks','fucktards','fuks','fucker','fuckers','fag','fags','faging','fagit','fagot','fannyfucker','fannyfuckers','fatass','fcuk','fcuks','fcuker','fcukers','fcuking','felching','felate','felatio','fingerfuck','fingerfucked','fingerfucker','fingerfuckers','fingerfucking','fingerfucks','fistfuck','fistfucked','fistfucker','fistfuckers','fistfucking','fistfuckings','fistfucks','fook','fooker','fookers','fuck','fucka','fucked','fucker','fuckers','fuckhead','fuckheads','fuckin','fucking','fuckings','fuckingshitmotherfucker','fuckme','fucks','fuckwhit','fuckwit','fudgepacker','fudgepacker','fuk','fuker','fukker','fukkin','fuks','fukwhit','fukwit','fux','fuxor','gangbang','gangbanged','gangbangs','gaylord','gaysex','goatse','goddam','goddamned','goddamn','hardcoresex','heshe','hoar','hoare','hoer','homo','hore','horniest','horny','hotsex','jackoff','jerkoff','jism','jiz','jizm','jizz','kawk','knobjocky','knobjokey','kock','kondum','kondums','kum','kummer','kumming','kums','kunilingus','labia','lust','lusting','mofo','masterbate','masterbates','masterbater','masterbaters','masterbation','masterbations','masturbate','masturbates','masturbater','masturbaters','masturbation','masturbations','mothafuck','mothafucka','mothafuckas','mothafuckaz','mothafucked','mothafucker','mothafuckers','mothafuckin','mothafucking','mothafuckings','mothafucks','motherfucker','motherfuck','motherfucked','motherfucker','motherfuckers','motherfuckin','motherfucking','motherfuckings','motherfucka','motherfucks','muff','muthafecker','muthafuckker','muther','mutherfucker','nigga','niggah','niggas','niggaz','nigger','niggers','nobjokey','nobjocky','nobjokey','numbnuts','nutsack','pecker','penis','penisfucker','phuck','phuk','phuked','phuking','phukked','phukking','phuks','phuq','pigfucker','pimpis','pissflaps','prick','pricks','pube','pusse','pussi','pussies','pussy','pussys','rectum','rimjaw','rimming','shit','sadist','schlong','screwing','scroat','scrote','scrotum','semen','shag','shagger','shaggin','shagging','shemale','shit','shitdick','shite','shited','shitey','shitfuck','shitfull','shithead','shiting','shitings','shits','shitted','shitter','shitters','shitting','shittings','shitty','skank','slut','sluts','smegma','smut','snatch','spac','spunk','teets','teez','testical','testicle','tit','titfuck','tits','titt','tittiefucker','titties','tittyfuck','tittywank','titwank','turd','twat','twathead','twatty','twunt','twunter','vagina','vulva','wang','wank','wanker','wanky','whoar','whore','willies','willy'
]

WILDCARD_SPACE = '(?:[^\d\w\\\'\\"])'
REG_BEGIN = '^(?:.*'+WILDCARD_SPACE+'+)?'
REG_END = '(?:'+WILDCARD_SPACE+'.*)?$'

#Compilation of Regexs to detect swears
swearWordsRegex = None

for badword in BADWORDS:
	# skip single letter words
	if len(badword) < 2:
		continue

	# prepare the word
	firstLetter = '['+badword[0].upper()+badword[0].lower()+']'
	rule = REG_BEGIN+firstLetter


	for letter in badword[1:]:
		rule += WILDCARDS[letter.lower()]+'+'

	rule += REG_END
	if swearWordsRegex is None:
		swearWordsRegex = rule
	else:
		swearWordsRegex += '|'+rule

swearWordsRegex = '(?:'+swearWordsRegex+')'

@module.rule(swearWordsRegex)
def warnLanguage(bot, trigger):
       	warnLanguageMessage(bot, trigger)

def warnLanguageMessage(bot, trigger):
	bot.say('Please watch your language ' + trigger.nick + '!',max_messages=10)
