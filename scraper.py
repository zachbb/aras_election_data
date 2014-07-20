###################################################################################
# Twitter API scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2


QUERY = '#prochoice OR #prolife'
RESULTS_PER_PAGE = '15'
LANGUAGE = 'en'
NUM_PAGES = 1 

for page in range(1, NUM_PAGES+1):
    base_url = 'https://api.twitter.com/1.1/search.json?q=%s&&rpp=%s&lang=%s&page=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            data['from_user_id'] = result['from_user_id']
            data['created_at'] = result['created_at']
            print data['from_user'], data['text']
            scraperwiki.sqlite.save(["id"], data) 
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        
    
