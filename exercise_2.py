import urllib2
import json
import datetime

#vriskei thn shmerinh hmeromhnia
cur_date = datetime.datetime.now()

#listes ari8mwn 
nums = []
ari8moi = []

#elegxos an oi ari8moi pou dinei o xrhsths anhkoun stous epitreptous tou kino
for i in range(1,81):
    ari8moi.append(i)
for j in range(1,11):
    while True:
        x = int(input('Dwste ton ' + str(j) + 'o ari8mo (apo to 1 ews to 80):'))
        if x in ari8moi and x not in nums:
            break
    nums.append(x)
    #an o ari8mos pou dinei o xrhsths den anhkei sto pedio tou kino h einai o
    #idios me kapoion prohgoumeno tote 8a zhth8ei apo ton xrhsth na 3ana eisagei
    #sth 8esh tou enan egkuro ari8mo

#dhmiourgeia synarthshs gia thn euresh twn nikhthriwn ari8mwn   
def compare_lists(l0, l2): 
    s = 0
    for i in l0:
        if i in l2:
            s += 1
    return s

epityxies = []
dates = []
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    #pairnei ta dedomena apo to web service twn klhrwsewn
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    drawlist= data['draws']['draw']

    apo = 0
    #gia ka8e klhrwsh stis sugkekrimenes meres
    for d in drawlist:
        tmp = d['results']
        #sugrinei ta apotelesmata me th lista tou xrhsth kai vriskei tis "x" epityxies
        x = (compare_lists(nums, tmp))
        if x > 4:
            apo += 1

    epityxies.append(apo)
    dates.append(date_str)

#h hmera me tis perissoteres epityxies
win_hmera = dates[epityxies.index(max(epityxies))]
#emfanish ths hmeras me tis perissoteres epityxies
print('Stis ' + win_hmera +' o xrhsths 8a eixe tis perissoteres epituxies!')
