import datetime

#lista me ta onomata twn hmerwn sta Ellhnika
days = ['Deutera','Trith','Tetarth','Pempth','Paraskeuh','Sabbato','Kuriakh']
#lista me ta onomata twn mhnwn sta Ellhnika
months = ['Ianouario','Febrouario','Martio','Aprilio','Maio','Iounio','Ioulio','Augousto','Septembrio','Oktobrio','Noembrio','Dekembrio']
#vriskei to onoma ths shmerinhs hmeras(px: Deutera...)
name_day = datetime.datetime.today().weekday()
#vriskei thn twrinh hmeromhnia
day = datetime.datetime.today().day
#vriskei ton twrino mhna
month = datetime.datetime.today().month
#vriskei to twrino etos
year = datetime.datetime.today().year
#ektypwsh twn twrinwn stoixeiwn
print('Shmera exoume '+str(day)+', hmera '+days[name_day]+', mhna '+months[month-1]+', kai etos '+str(year)) 

sum = 0
#gia ta epomena 10 xronia poses meres tautizontai
for i in range(year+1, year+11):
    if datetime.datetime(i, month, day).weekday() == name_day:
        #au3hsh tou "sum" an yparxei allh mera pou na plhrei ta krithria
        sum +=1                                                 
#e3odos tou apotelesmatos pou anaferei poses idies meres 8a upar3oun sta epomena 10 xronia
print('Gia ta epomena 10 xronia 8a tuxei '+str(sum)+' fora/es na einai '+days[name_day]+' stis '+str(day)+' gia ton mhna '+months[month-1])
#sto "months[month-1]" to "month-1" uparxei ka8ws,px: h lista "months" exei ws 0 stoixeio ton Ianouario enw
#to "month" pairnei times apo to 1 ews to 12,kai o Ianouarios einai to 1, ara gia na ektypw8ei to swsto
#onoma tou mhna ,kai oxi tou epomenou tou, prepei na afairesoume 1 apo to "month"
