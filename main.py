from application.db.people import get_employees
from application.salary import calcualte_salary
import datetime

date_now = datetime.datetime.now()
print(date_now)

def main():
    print(calcualte_salary(2))
    print(get_employees('Тествич'))

if __name__ == '__main__':
    main()
