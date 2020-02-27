from datetime import date
#getting current date from user#
today= date.today()
print("Today's date is:",today)
give_date=input("Please enter a date in DD/MM/YYYY: ") 
d= give_date.split("/")
y= int(d[2])
m= int(d[1])
dt= int(d[0])
print(y,m,dt)
newdate= date(year= y, month=m , day=dt)
df = abs(today - newdate) #get absolute difference between current and given date
days_difference = df.days #to print only the days 
hours_difference= days_difference * 24 #turning days to hours
secs_difference= hours_difference * 60 #turning hours to seconds
print("The difference between the date given and current date is:",days_difference," in days",hours_difference,"in hours", secs_difference,"in seconds")

#find how many days the month has#
if (m==2):
    if (y%400==0 or (y%4== 0 and y%100!=0)): #if month is February check if year is leap year
        print("The given month has 29 days")
    else:
        print("The given month has 28 days")
        
if(m==1 or (m>2 and m<=7)): #if month is number between 1 and 7-but not 2-odd months have 31 days even have 30
    if(m%2==0):
        print("The given month has 30 days")
    else:
        print("The given month has 31 days")
        
elif(m>=8 and m<=12): #if month is a number between 8 and 12 odd months have 30 days and even have 31 days
    if(m%2==0):
        print("The given month has 31 days")
    else:
        print("The given month has 30 days")