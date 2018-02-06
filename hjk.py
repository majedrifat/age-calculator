#list={'a':6,'b':'tmi','c':True}


#for i,v in list.items():
   # print(v)
from datetime import datetime, date

print("Your date of birth (dd mm yyyy)")
date_of_birth = datetime.strptime(input("dd mm yy"), "%d %m %Y")

def age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = age(date_of_birth)

print(age)