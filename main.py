import datetime
import sys
from salary import calculate_salary
#Временное добавление пути к модулю people в sys.path
sys.path.append('D:\\Олег\\0 Python\\script\\Phyton PROF\\DB')
import people


print('Бухгалтерия версия 8.3')
#текущие дата и время
now = datetime.datetime.now()
print(str(now))

calculate_salary()
people.get_employees()
