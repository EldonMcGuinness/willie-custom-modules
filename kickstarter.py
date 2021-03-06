"""
kickstarter.py - Willie module to search for kickstarter projects
Copyright 2013, Eldon McGuinness

http://willie.dftba.net
"""

from willie import module, web
import json, time, re

def google_ajax(query):
    """Search using AjaxSearch, and return its JSON."""
    uri = 'http://ajax.googleapis.com/ajax/services/search/web'
    args = '?v=1.0&safe=off&q=site:kickstarter.com/projects/+' + web.quote(query)
    bytes = web.get(uri + args)
    return json.loads(bytes)


def google_search(query):
    results = google_ajax(query)
    try:
        return results['responseData']['results'][0]['unescapedUrl']
    except IndexError:
        return None
    except TypeError:
        return False

@module.commands('kickstarter')
@module.example('.kickstarter read only memories')
def g(bot, trigger):
    """Attempts to find the given Kickstarter title"""
    query = trigger.group(2)
    if not query:
        return bot.reply('What title are you looking for?')
    uri = google_search(query)
    if uri:
        bot.say('[ Kickstarter: %s | %s ]' % (query.lower().capitalize(),uri))
        bot.memory['last_seen_url'][trigger.sender] = uri
    elif uri is False:
        bot.reply("Query could not be complete, please try again.")
    else:
        bot.reply("No results found for '%s'." % query)	
