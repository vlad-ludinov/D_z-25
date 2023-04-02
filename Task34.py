def count_syllable(phrase):
    count = 0
    for i in phrase:
        if i in vowels:
            count += 1
    return count
def count_rhythm(list_1):
    temp_list = list(map(count_syllable, list_1))
    for i in range(1,len(temp_list)):
        if temp_list[i-1] != temp_list[i]:
            return "Пам парам"  
    return "Парам пам-пам"

list_Vinny_Puh = input("Введите строку стихотворения: ").split()
print(list_Vinny_Puh)
vowels = "аоуиеёыэюя"
print(count_rhythm(list_Vinny_Puh))