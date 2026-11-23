from barcode_checker import *
def main():
    while True:
        print("==== Программа проверки штрих-кодов EAN-13 ====")
        print("===== Для выхода напишите: exit ===============\n")
        print("Укажите путь к файлу с изображением штрих-кода:")
        need_check = input("Если файла нет - нажмите Enter ")
        print("Распознание изображений пока не реализовано...")
        if need_check == "exit":
            break
        barcode_string = input("Введите цифры со штрих кода >> ")
        print(ean13_verdict(barcode_string))

if __name__ == '__main__':
    main()
