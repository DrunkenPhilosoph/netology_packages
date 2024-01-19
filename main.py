from application.db.people import get_employees
from application.salary import calcualte_salary
import datetime

date_now = datetime.datetime.now()
print(date_now)

if __name__ == '__main__':
    print(calcualte_salary(3))
    print(get_employees(2))
