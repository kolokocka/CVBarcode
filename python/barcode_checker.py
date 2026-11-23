all_countries_path = [
    (0, 19, "США / Канада"),
    (30, 39, "Франция"),
    (40, 49, "Германия"),
    (50, 59, "Великобритания"),
    (60, 69, "Финляндия"),
    (70, 79, "Норвегия"),
    (80, 89, "Италия"),
    (90, 99, "Австрия"),
    (300, 379, "Франция"),
    (400, 440, "Германия"),
    (450, 459, "Япония"),
    (460, 469, "Россия"),
    (471, 471, "Тайвань"),
    (489, 489, "Гонконг"),
    (500, 509, "Великобритания"),
    (540, 549, "Бельгия / Люксембург"),
    (560, 560, "Португалия"),
    (690, 699, "Китай"),
    (760, 769, "Швейцария"),
    (800, 839, "Италия"),
    (840, 849, "Испания"),
    (870, 879, "Нидерланды"),
    (880, 880, "Южная Корея"),
    (890, 890, "Индия"),
    (930, 939, "Австралия"),
    (940, 949, "Новая Зеландия"),
    (978, 979, "Книги (ISBN)"),
    (980, 980, "Возвратные квитанции"),
    (981, 984, "Купонные валюты"),
    (990, 999, "Купоны")
]
countries = [""] * 1000
for start, end, country in all_countries_path:
    for i in range(start, end + 1):
        countries[i] = country

def prefix_check(user_input):
    prefix = int(user_input[:3])
    country = ""
    if countries[prefix] != "":
        country = countries[prefix]
    return country

def modulo10_check(user_input) -> bool:
    nums = user_input[::-1]
    even_sum = (int(nums[1]) + int(nums[3]) + int(nums[5]) + int(nums[7]) + int(nums[9]) + int(nums[11])) * 3
    odd_sum = int(nums[2]) + int(nums[4]) + int(nums[6]) + int(nums[8]) + int(nums[10]) + int(nums[12])
    total_sum = even_sum + odd_sum
    check_digit = ((total_sum + 9) // 10) * 10 - int(total_sum) # Хитрый способ округления вверх
    
    return int(user_input[-1]) == check_digit
    


def decode_barcode_from_image(image_path): # str
    """
    Заглушка. В реальности анализируем картинку и возвращаем строку цифр.
    Сейчас просто просим ввести код вручную.
    """
    print(f"[Имитация] Анализ изображения: {image_path}")
    # Здесь мог бы быть наш код с OpenCV
    user_input = input("Введите 13 цифр, изображенных на штрих-коде: ")
    return user_input
''' #Первая версия без префикса страны
def ean13_valid(barcode): #bool
    length = len(barcode)
    if not barcode.isdigit() or length != 13:
        #print('!', length)
        return False # Получен неверный код
    digits = []
    check_digit = int(barcode[-1])
    for i in range(length - 1):
        digits += [int(barcode[i])]

    total = 0
    for i in range(length - 1):
        if i % 2 == 1:
            total += digits[i]
        else:
            total += digits[i] * 3
    nearest10 = (total + 9) // 10 * 10 # Хитрый способ округления вверхъ
    calc_check_digit = nearest10 - total
        
    return check_digit == calc_check_digit
'''
def ean13_verdict(barcode) -> str:
    verdict = []
    length = len(barcode)
    if not barcode.isdigit():
        return "Штрих-код должен содержать только цифры\n"
    
    if length != 13:
        return "Штрих-код должен содержать 13 цифр\n"

    if prefix_check(barcode) != "":
        verdict.append("Префикс страны валиден, " + prefix_check(barcode))
    else:
        verdict.append("Префикс страны невалиден")
    
    if modulo10_check(barcode):
        verdict.append("Контрольная цифра валидна")
    else:
        verdict.append("Контрольная цифра невалидна")
    
    return verdict[0] + "\n" + verdict[1] + "\n"
