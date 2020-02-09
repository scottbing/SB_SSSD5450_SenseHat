from nytimesarticle import articleAPI
api = articleAPI('grzuX0voNRRIeU77q2BTHT1kdXNBt0zE')


articles = api.search( q = 'Obama',
     fq = {'headline':'Obama', 'source':['Reuters','AP', 'The New York Times']},
     begin_date = 20111231 )
