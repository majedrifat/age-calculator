from _datetime import datetime, date

print("Your date of birth (dd mm yyyy)")
date_of_birth = datetime.strptime(input("dd mm yy\n"), "%d %m %Y")

def age(born):
    today = date.today()
    if today.day < born.day and today.month < born.month:
        tod=13 -born.month
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day)) ,tod

ag = age(date_of_birth)


print("your age: yy mm" )
print(ag)
