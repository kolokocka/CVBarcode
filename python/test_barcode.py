from barcode_checker import *
    
def main():
    Test1   = "4601234567893" #Базовый префикс РФ (460)
    Test2   = "4691234567894" #Верхняя граница префикса
    Test3   = "0123456789012" #Префикс с ведущим нулем
    Test4   = "4006381333450" #Стандартный европейский префикс
    Test5   = "6901234567892" #Азиатский префикс
    Test6   = "9781234567897" #Специальный префикс для книг
    Test7   = "5012345678900" #Префикс 50
    Test8   = "0123456789012" #Префикс с ведущим нулем
    Test9   = "0000000000000" #Минимально возможный индекс
    Test10  = "9990000000005" #Максимально возможный префикс
    Test11  = "460123456789"  #Код короче 13 знаков
    Test12  = "46012345678934"#Код длиннее 13 знаков
    Test13  = "46012345678A3" #В коде присутствуют не цифры
    Test14  = ""  #Пустая строка
    Test15  = "4601234567894" #Ошибка контрольной суммы

    print("=========== Тестирование программы штрих-кодов EAN-13 ===========")
    print("==================== Начало тестирования:  ======================\n")
    print(f"Ввод: {Test1}")
    print(ean13_verdict(Test1))
    print(f"Ввод: {Test2}")
    print(ean13_verdict(Test2))
    print(f"Ввод: {Test3}")
    print(ean13_verdict(Test3))
    print(f"Ввод: {Test4}")
    print(ean13_verdict(Test4))
    print(f"Ввод: {Test5}")
    print(ean13_verdict(Test5))
    print(f"Ввод: {Test6}")
    print(ean13_verdict(Test6))
    print(f"Ввод: {Test7}")
    print(ean13_verdict(Test7))
    print(f"Ввод: {Test8}")
    print(ean13_verdict(Test8))
    print(f"Ввод: {Test9}")
    print(ean13_verdict(Test9))
    print(f"Ввод: {Test10}")
    print(ean13_verdict(Test10))
    print(f"Ввод: {Test11}")
    print(ean13_verdict(Test11))
    print(f"Ввод: {Test12}")
    print(ean13_verdict(Test12))
    print(f"Ввод: {Test13}")
    print(ean13_verdict(Test13))
    print(f"Ввод: {Test14}")
    print(ean13_verdict(Test14))
    print(f"Ввод: {Test15}")
    print(ean13_verdict(Test15))

if __name__ == '__main__':
    main()
