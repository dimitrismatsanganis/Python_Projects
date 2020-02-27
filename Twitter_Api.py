import tweepy
 
consumer_key='JnTatNhKI2VQdOC8NmmoFZEZm'
consumer_secret='hNSqbPWZzuuWPiQAIA8vEPQzIEhJUG46m1SomBRwOhOVE5kAR1'
access_token='742835108852469760-EitPUsd50qhtOOHIHl96TUZerKVJpVN'
access_token_secret='yQbSAdi7VZmIQSEtz3bNS35mFYRwp7cEiS0AbGk4hudnS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

#eisodos tou logariasmou apo ton xrhsth
name=raw_input('Dwse to Twitter username pou 8eleis: ')

#euresh twn tweets 
statuses = api.user_timeline(screen_name = name, count = 10, tweet_mode='extended')
allstatuses = [s.full_text for s in statuses]
allstatuses = [s.replace(s,s+' ') for s in allstatuses]

text=''
#vriskei ta keimena twn 10 teleutaiwn tweets tou xrhsth
for status in allstatuses:
	text+="".join([status])
	
#xwrizei tis le3eis (8a xwrizontai me keno,ka8ws yparxei to .split())
sepwords = text.lower().split()

#dhmiourgeia listas me tis monadikes le3eis
listwords = []
for w in sepwords:
  if w not in listwords:
    listwords.append(w)

#dhmiourgeia listas me tis syxnthtes twn le3ewn
freqs = []
#gia ka8e le3h sth lista twn monadikwn le3ewn
for lw in listwords:
  #mhdenizei thn syxnothta
  fr = 0 
  #gia ka8e le3h apo th lista twn monadikwn le3ewn (sepwords) isoutai me mia monadikh le3h
  for w in sepwords:    
    if w == lw:
      #au3anei thn syxnothta ths monadikhs le3hs
      fr=fr+ 1
  #pros8etei sth lista twn syxnothtwn    
  freqs.append((fr, lw))
#katatassei tis syxnothtes kata f8inousa seira
freqs.sort()           
freqs.reverse()         
#ektypwnei thn prwth le3h
c, w = freqs[0]
#ektypwsh twn apotelesmatwn
print 'H le3h pou xrhsimopoih8hke perissotero sta teleutaia 10 tweets tou xrhsth,',name,',einai h e3hs: '
print '( %s ) h opoia xrhsimopoih8hke synolika : %s fores.' % (w, c)
