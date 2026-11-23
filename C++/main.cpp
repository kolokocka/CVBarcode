#include <iostream>
#include <string>

#ifdef _WIN32
#include <windows.h>
#endif

// Все проверки из barcode_checker.py находятся прямо в этом файле.
// Никаких собственных заголовков, модулей или внешних библиотек не требуется.

struct PrefixRange {
    int first;
    int last;
    const char* description;
};

std::string prefix_check(const std::string& barcode) {
    // Та же таблица диапазонов, что в исходном barcode_checker.py.
    static const PrefixRange ranges[] = {
        {0, 19, "США / Канада"},
        {30, 39, "Франция"},
        {40, 49, "Германия"},
        {50, 59, "Великобритания"},
        {60, 69, "Финляндия"},
        {70, 79, "Норвегия"},
        {80, 89, "Италия"},
        {90, 99, "Австрия"},
        {300, 379, "Франция"},
        {400, 440, "Германия"},
        {450, 459, "Япония"},
        {460, 469, "Россия"},
        {471, 471, "Тайвань"},
        {489, 489, "Гонконг"},
        {500, 509, "Великобритания"},
        {540, 549, "Бельгия / Люксембург"},
        {560, 560, "Португалия"},
        {690, 699, "Китай"},
        {760, 769, "Швейцария"},
        {800, 839, "Италия"},
        {840, 849, "Испания"},
        {870, 879, "Нидерланды"},
        {880, 880, "Южная Корея"},
        {890, 890, "Индия"},
        {930, 939, "Австралия"},
        {940, 949, "Новая Зеландия"},
        {978, 979, "Книги (ISBN)"},
        {980, 980, "Возвратные квитанции"},
        {981, 984, "Купонные валюты"},
        {990, 999, "Купоны"}
    };

    const int prefix = (barcode[0] - '0') * 100
                     + (barcode[1] - '0') * 10
                     + (barcode[2] - '0');

    for (const PrefixRange& range : ranges) {
        if (prefix >= range.first && prefix <= range.last) {
            return range.description;
        }
    }
    return "";
}

bool modulo10_check(const std::string& barcode) {
    // Для EAN-13 первые 12 цифр складываются с весами 1, 3, 1, 3, ...
    int total_sum = 0;
    for (int i = 0; i < 12; ++i) {
        const int digit = barcode[i] - '0';
        total_sum += (i % 2 == 0) ? digit : digit * 3;
    }
    const int check_digit = (10 - total_sum % 10) % 10;
    return (barcode[12] - '0') == check_digit;
}

// Как и в Python-оригинале, это только имитация распознавания картинки.
// Настоящего чтения штрих-кода с изображения исходный проект не содержал.
std::string decode_barcode_from_image(const std::string& image_path) {
    std::cout << "[Имитация] Анализ изображения: " << image_path << '\n';
    std::cout << "Введите 13 цифр, изображенных на штрих-коде: ";
    std::string barcode;
    std::getline(std::cin, barcode);
    return barcode;
}

std::string ean13_verdict(const std::string& barcode) {
    // Пустая строка, как и в Python, считается вводом без цифр.
    if (barcode.empty()) {
        return "Штрих-код должен содержать только цифры\n";
    }
    for (char symbol : barcode) {
        if (symbol < '0' || symbol > '9') {
            return "Штрих-код должен содержать только цифры\n";
        }
    }
    if (barcode.size() != 13) {
        return "Штрих-код должен содержать 13 цифр\n";
    }

    const std::string country = prefix_check(barcode);
    std::string verdict;
    if (!country.empty()) {
        verdict = "Префикс страны валиден, " + country + "\n";
    } else {
        verdict = "Префикс страны невалиден\n";
    }

    if (modulo10_check(barcode)) {
        verdict += "Контрольная цифра валидна\n";
    } else {
        verdict += "Контрольная цифра невалидна\n";
    }
    return verdict;
}

void setup_console_utf8() {
#ifdef _WIN32
    // Вывод русских букв в стандартной консоли Windows.
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
#endif
}

int main() {
    setup_console_utf8();

    while (true) {
        std::cout << "==== Программа проверки штрих-кодов EAN-13 ====\n";
        std::cout << "===== Для выхода напишите: exit ===============\n\n";
        std::cout << "Укажите путь к файлу с изображением штрих-кода:\n";
        std::cout << "Если файла нет - нажмите Enter ";

        std::string need_check;
        if (!std::getline(std::cin, need_check)) {
            break;
        }
        if (need_check == "exit") {
            break;
        }
        std::cout << "Распознание изображений пока не реализовано...\n";

        std::cout << "Введите цифры со штрих кода >> ";
        std::string barcode_string;
        if (!std::getline(std::cin, barcode_string)) {
            break;
        }
        std::cout << ean13_verdict(barcode_string) << '\n';
    }
    return 0;
}
