"""
swear2.py - Willie Anti-Swearing Module
Copyright 2013, Eldon McGuinness

http://willie.dftba.net
"""

from willie import module,db

WILDCARDS = {
	'a' : '(?:[Aa]|[^\d\s\w,])',
	'b' : '(?:[Bb]|[^\d\s\w,])',
	'c' : '(?:[Cc]|[^\d\s\w,])',
	'd' : '(?:[Dd]|[^\d\s\w,])',
	'e' : '(?:[Ee]|[^\d\s\w,])',
	'f' : '(?:[Ff]|[^\d\s\w,])',
	'g' : '(?:[Gg]|[^\d\s\w,])',
	'h' : '(?:[Hh]|[^\d\s\w,])',
	'i' : '(?:[iI\|17!]|[^\d\s\w,])',
	'j' : '(?:[Jj]|[^\d\s\w,])',
	'k' : '(?:[Kk]|[^\d\s\w,])',
	'l' : '(?:[Ll]|[^\d\s\w,])',
	'm' : '(?:[Mm]|[^\d\s\w,])',
	'n' : '(?:[Nn]|[^\d\s\w,])',
	'o' : '(?:[Oo0]|[^\d\s\w,])',
	'p' : '(?:[Pp]|[^\d\s\w,])',
	'q' : '(?:[Qq0]|[^\d\s\w,])',
	'r' : '(?:[Rr]|[^\d\s\w,])',
	's' : '(?:[Ss5]|[^\d\s\w,])',
	't' : '(?:[tT\|17]|[^\d\s\w,])',
	'u' : '(?:[uU]|[^\d\s\w,])',
	'v' : '(?:[Vv]|[^\d\s\w,])',
	'w' : '(?:[Ww]|[^\d\s\w,])',
	'x' : '(?:[Xx]|[^\d\s\w,])',
	'y' : '(?:[Yy]|[^\d\s\w,])',
	'z' : '(?:[Zz]|[^\d\s\w,])'
}

BADWORDS = [
	'unicorn'
]

WILDCARD_SPACE = '(?:[^\d\w])'
REG_BEGIN = '^(?:.*'+WILDCARD_SPACE+'+)?'
REG_END = '(?:'+WILDCARD_SPACE+'.*)?$'

#Compilation of Regexs to detect swears
swearWordsRegex = None

def setup(bot):
	# Check to ensure the DB exists
	if not bot.db:
		raise ConfigurationError("Database not set up, or unavailable.")
	
	# Create the table if needed
	bot.db.add_table('channel_moderation',[('name','TEXT'),('offense_date','INTEGER DEFAULT 0')],'name')

	# Check to see if offending user is in DB
		# If user is in db
			# get offense count
			# increment count
			# check if count is about SWEAR_LIMIT
			# If above swear limit the take action
		# If not in db
			# add user
			#set warning to 1	

for badword in BADWORDS:
        # skip single letter words
        if len(badword) < 2:
                continue

	#prepare the word
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
	bot.say('Please watch your language ' + trigger.nick + '!')


