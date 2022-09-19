import datetime
import sys
# импорт пакета p1
sys.path.append('D:\\Олег\\0 Python\\script\\Phyton PROF')
import p1 as package_1
# импорт пакета p2
sys.path.append('D:\\Олег\\0 Python\\script\\Phyton PROF\\DB')
import p2 as package_2


print('Бухгалтерия версия 8.3')
#текущие дата и время
now = datetime.datetime.now()
print(str(now))

package_1.calculate_salary()
package_2.g()


#print(dir(package_1))
#print(dir(package_2))