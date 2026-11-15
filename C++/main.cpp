#include <iostream>
#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

#ifdef _WIN32
#include <windows.h>
#endif

bool prefix_check(const std::string& code) {
    int prefix = std::stoi(code.substr(0, 3));
    
    static const std::vector<std::pair<int,int>> ranges = {
        {0, 19}, {30, 39}, {60, 139}, {300, 379},
        {380, 380}, {383, 383}, {385, 385}, {387, 387},
        {389, 389}, {400, 440}, {450, 459}, {460, 469},
        {470, 470}, {471, 471}, {474, 474}, {475, 475},
        {476, 476}, {477, 477}, {478, 478}, {479, 479},
        {480, 480}, {481, 481}, {482, 482}, {484, 484},
        {485, 485}, {486, 486}, {487, 487}, {488, 488},
        {489, 489}, {490, 499}, {500, 509}, {520, 521},
        {528, 528}, {529, 529}, {530, 530}, {531, 531},
        {535, 535}, {539, 539}, {540, 549}, {560, 560},
        {569, 569}, {570, 579}, {590, 590}, {594, 594},
        {599, 599}, {600, 601}, {603, 603}, {604, 604},
        {608, 608}, {609, 609}, {611, 611}, {613, 613},
        {615, 615}, {616, 616}, {617, 617}, {618, 618},
        {619, 619}, {621, 621}, {622, 622}, {624, 624},
        {625, 625}, {626, 626}, {627, 627}, {628, 628},
        {629, 629}, {640, 649}, {690, 699}, {700, 709},
        {729, 729}, {730, 739}, {740, 740}, {741, 741},
        {742, 742}, {743, 743}, {744, 744}, {745, 745},
        {746, 746}, {750, 750}, {754, 755}, {759, 759},
        {760, 769}, {770, 770}, {773, 773}, {775, 775},
        {777, 777}, {779, 779}, {780, 780}, {784, 784},
        {786, 786}, {789, 790}, {800, 839}
    };
    
    for (const auto& r : ranges) {
        if (prefix >= r.first && prefix <= r.second)
            return true;
    }
    return false;
}

bool modulo10_check(const std::string& code) {
    int sum = 0;
    for (int i = 0; i < 12; i++) {
        int digit = code[i] - '0';
        if (i % 2 == 0)
            sum += digit;
        else
            sum += digit * 3;
    }
    int check_digit = (10 - (sum % 10)) % 10;
    return (code[12] - '0') == check_digit;
}

std::string barcode_check(const std::string& image_path) {
    (void)image_path; // путь пока не используется (имитация анализа)
    std::vector<std::string> verdict;
    
    std::cout << "Имитация анализа изображения(пока не добавлено)..." << std::endl;
    
    std::string code;
    std::cout << "Введите цифры со штрих-кода >> ";
    std::getline(std::cin, code);
    
    auto is_all_digits = [](const std::string& s) {
        if (s.empty()) return false;
        for (char c : s)
            if (!std::isdigit(static_cast<unsigned char>(c)))
                return false;
        return true;
    };
    
    while (!is_all_digits(code)) {
        std::cout << "Введите только цифры >> ";
        std::getline(std::cin, code);
    }
    
    while (code.length() != 13) {
        std::cout << "Штрих-код EAN-13 должен содержать только 13 символов!" << std::endl;
        std::cout << "Введите цифры со штрих-кода >> ";
        std::getline(std::cin, code);
        while (!is_all_digits(code)) {
            std::cout << "Введите только цифры >> ";
            std::getline(std::cin, code);
        }
    }
    
    if (prefix_check(code))
        verdict.push_back("Префикс страны валиден");
    else
        verdict.push_back("Префикс страны невалиден");
    
    if (modulo10_check(code))
        verdict.push_back("Контрольная цифра валидна");
    else
        verdict.push_back("Контрольная цифра невалидна");
    
    std::string result;
    for (size_t i = 0; i < verdict.size(); i++) {
        if (i > 0) result += "\n";
        result += verdict[i];
    }
    return result;
}

int main() {
#ifdef _WIN32
    SetConsoleOutputCP(65001);
    SetConsoleCP(65001);
#endif
    std::cout << "Вас приветствует программа CVBarcode" << std::endl;
    while (true) {
        std::cout << "Введите путь к изображению штрих-кода(для выхода напишите exit) >> ";
        std::string image_path;
        std::getline(std::cin, image_path);
        
        if (image_path == "exit")
            break;
        
        std::cout << barcode_check(image_path) << std::endl;
    }
    
    return 0;
}