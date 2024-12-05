# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()  # Приводим текст к нижнему регистру
    letter_counts = {}
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_counts):
    total_letters = sum(letter_counts.values())  # Общее количество букв
    frequency = {}
    for letter, count in letter_counts.items():
        frequency[letter] = round(count / total_letters, 2)  # Округляем частоту до двух знаков
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
# Подсчёт букв
letter_counts = count_letters(main_str)

# Вычисление частоты
letter_frequency = calculate_frequency(letter_counts)

# Сортировка и вывод результатов
sorted_letter_frequency = sorted(letter_frequency.items())

# Выводим в столбик буквы и их частоту
for letter, freq in sorted_letter_frequency:
    print(f"{letter}: {freq}")

