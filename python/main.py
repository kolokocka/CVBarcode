from barcode_checker import *

def main():
    while True:
        image_path = input("Введите путь к изображению штрих-кода(для выхода напишите exit) >> ");
        if image_path == "exit":
            break;
        print(barcode_check(image_path));

if __name__ == "__main__":
    print("Вас приветствует программа CVBarcode")
    main();