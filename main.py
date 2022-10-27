from logging import PercentStyle


print("Введите не больше 5 чисел через пробел. Эти числа не должны быть больше 10")
def main():
    try:
        global PER
        PER = list(map(int, input().split(" ")))
        print(PER)
    
    except ValueError:
        print("Вы ввели не число!")
        main()

main()
if len(PER) > 5:
    print("Введите не больше 5 чисел!")

i = 0
leng = len(PER)
for i in range(0,leng):
    if PER[i] > 10:
        print("Введите числа которые не превышают заданное число")
        main()

STR_PER = map(str,PercentStyle)
FILE = open("txt.txt", "a")
for index in STR_PER:
    FILE.write(index + ' ')
FILE.write('\n')
FILE.close()
