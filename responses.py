"""
responses.py - Willie Anti-Swearing Module
Copyright 2013, Eldon McGuinness

http://willie.dftba.net
"""

#  TODO Build a regex to represent the bots name

from willie import module
import random

@module.rule('(?:.*\s)?gamestick(?:s)?.*')
def gamestick_response (bot, trigger):
	responses = [
		'%s, how dare you mention that toy in here!',
		'%s, I put away toys like that when I grew up.',
		'%s, I\'d rather be playing OUYA that talking about that',
		'%s, gamewho?'
	]
        bot.say(random.choice(responses) % trigger.nick)

@module.rule('^ouya$')
def ouya_response (bot, trigger):
	responses = [
		'Let the revolution begin!'
	]
        bot.say(random.choice(responses))

@module.rule('^(?:who is the)?\s*Doctor\s*$')
def doctor_response (bot, trigger):
	responses = [
		'Doctor Who?'
	]
        bot.say(random.choice(responses))

@module.rule('^(?:hi|hey|hello|what\'s? up)[^\d\w]*$')
@module.rule('^(?:how\'?s it going,?|hello|hey|hi|what\'?s? up) (?:guys|all|gals|fellas|peoples|everyone|everybody?)')
@module.rule('^(?:how\'?s it going,?|hello|hey|hi|what\'?s? up) (?:Lain_Iwakura|Lain Iwakura)')
def greetings_response (bot, trigger):
	responses = [
		'How\'s it going %s',
		'Hello %s.',
		'Greeetings, %s.',
		'%s is in the his-oussseeeee!',
		'Hi %s, overlord of all things OUYA and surpreme ruler of the universe.'

	]
	bot.say(random.choice(responses) % trigger.nick)

# Insert reply for when people appologive to bot
#@module.rule('^(?:how\'?s it going,?|hello|hey|hi|what\'?s? up) (?:Lain_Iwakura|Lain Iwakura)')
#def greetings_response (bot, trigger):
#	responses = [
#		'How\'s it going %s',
#	]
#	bot.say(random.choice(responses) % trigger.nick)
