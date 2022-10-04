import datetime
import PackageDB.people
from PackageBUCH.salary import calculate_salary

if __name__ == '__main__':
    
    now = datetime.datetime.now()
    print(now)
    
    calculate_salary()
    PackageDB.people.get_employees()
    