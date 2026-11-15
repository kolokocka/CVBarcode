all_countries_path = [
    *range(0, 20),
    *range(30, 40),
    *range(60, 140),
    *range(300, 380),
    *range(380, 381),
    *range(383, 384),
    *range(385, 386),
    *range(387, 388),
    *range(389, 390),
    *range(400, 441),
    *range(450, 460),
    *range(460, 470),
    *range(470, 471),
    *range(471, 472),
    *range(474, 475),
    *range(475, 476),
    *range(476, 477),
    *range(477, 478),
    *range(478, 479),
    *range(479, 480),
    *range(480, 481),
    *range(481, 482),
    *range(482, 483),
    *range(484, 485),
    *range(485, 486),
    *range(486, 487),
    *range(487, 488),
    *range(488, 489),
    *range(489, 490),
    *range(490, 500),
    *range(500, 510),
    *range(520, 522),
    *range(528, 529),
    *range(529, 530),
    *range(530, 531),
    *range(531, 532),
    *range(535, 536),
    *range(539, 540),
    *range(540, 550),
    *range(560, 561),
    *range(569, 570),
    *range(570, 580),
    *range(590, 591),
    *range(594, 595),
    *range(599, 600),
    *range(600, 602),
    *range(603, 604),
    *range(604, 605),
    *range(608, 609),
    *range(609, 610),
    *range(611, 612),
    *range(613, 614),
    *range(615, 616),
    *range(616, 617),
    *range(617, 618),
    *range(618, 619),
    *range(619, 620),
    *range(621, 622),
    *range(622, 623),
    *range(624, 625),
    *range(625, 626),
    *range(626, 627),
    *range(627, 628),
    *range(628, 629),
    *range(629, 630),
    *range(640, 650),
    *range(690, 700),
    *range(700, 710),
    *range(729, 730),
    *range(730, 740),
    *range(740, 741),
    *range(741, 742),
    *range(742, 743),
    *range(743, 744),
    *range(744, 745),
    *range(745, 746),
    *range(746, 747),
    *range(750, 751),
    *range(754, 756),
    *range(759, 760),
    *range(760, 770),
    *range(770, 771),
    *range(773, 774),
    *range(775, 776),
    *range(777, 778),
    *range(779, 780),
    *range(780, 781),
    *range(784, 785),
    *range(786, 787),
    *range(789, 791),
    *range(800, 840),
]

def prefix_check(image_path) -> bool:
    image_path = str(image_path);
    prefix = int(image_path[:3]);
    if prefix in all_countries_path:
        return True;
    else:
        return False;

def modulo10_check(image_path: str) -> bool:
    nums = image_path[::-1]
    true_sum = (int(nums[1]) + int(nums[3]) + int(nums[5]) + int(nums[7]) + int(nums[9]) + int(nums[11])) * 3
    false_sum = int(nums[2]) + int(nums[4]) + int(nums[6]) + int(nums[8]) + int(nums[10]) + int(nums[12])
    total_sum = true_sum + false_sum
    check_digit = ((int(total_sum) + 9) // 10) * 10 - int(total_sum)
    
    if int(image_path[-1]) == check_digit:
        return True
    else:
        return False

def verdict_compile(verdict) -> str:
    return verdict[0] + "\n" + verdict[1];

def barcode_check(image_path: str) -> str:
    verdict = []

    print("Имитация анализа изображения(пока не добавлено)...");
    image_path = input("Введите цифры со штрих-кода >> ");

    while not image_path.isdigit():
        image_path = input("Введите только цифры >> ");
    
    while not len(image_path) == 13:
        print("Штрих-код EAN-13 должен содержать только 13 символов!");
        image_path = input("Введите цифры со штрих-кода >> ");
 
    if prefix_check(image_path):
        verdict.append("Префикс страны валиден");
    else:
        verdict.append("Префикс страны невалиден");
    
    if modulo10_check(image_path):
        verdict.append("Контрольная цифра валидна");
    else:
        verdict.append("Контрольная цифра невалидна");
    
    return verdict_compile(verdict);