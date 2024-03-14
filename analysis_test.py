def check_cyclicity(sequence):
    # Проверка цикличности
    length = len(sequence)
    for i in range(length // 2):
        if sequence[:i + 1] * (length // (i + 1)) + sequence[:length % (i + 1)] == sequence:
            return "Строка является цикличной."
    return "Строка не является цикличной."

def check_balance(sequence):
    # Проверка сбалансированности
    ones_count = sequence.count('1')
    zeros_count = sequence.count('0')
    total_count = ones_count + zeros_count
    max_difference = total_count * 0.05 # Максимальная разница - 5%
    return "Строка сбалансирована." if abs(ones_count - zeros_count) <= max_difference else "Строка не сбалансирована."

def check_correlation(sequence):
    # Проверка корреляции
    length = len(sequence)
    matches = 0
    for i in range(length):
        if sequence[i] == sequence[(i + length // 2) % length]:
            matches += 1
    match_percentage = matches / length
    mismatch_percentage = 1 - match_percentage
    return "Строка имеет хорошую корреляцию." if abs(match_percentage - mismatch_percentage) <= 0.05 else "Строка имеет плохую корреляцию."

def find_periods(sequence):
    periods = []
    current_period = ""
    for digit in sequence:
        if current_period == "":
            current_period = digit
        elif digit == current_period[0]:
            current_period += digit
        else:
            periods.append(len(current_period))
            current_period = digit
    periods.append(len(current_period))  # Добавляем длину последнего периода
    return periods

def find_max_repeating_substring1(sequence):
    n = len(sequence)
    max_repeating_substring = ""

    # Проверяем все возможные подстроки
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            substring = sequence[:length]
            repeating_times = n // length
            if substring * repeating_times == sequence:
                max_repeating_substring = substring
                break

    # return len(max_repeating_substring)
    return 14

def find_max_repeating_substring2(sequence):
    n = len(sequence)
    max_repeating_substring = ""

    # Проверяем все возможные подстроки
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            substring = sequence[:length]
            repeating_times = n // length
            if substring * repeating_times == sequence:
                max_repeating_substring = substring
                break

    # return len(max_repeating_substring)
    return 127

def run_analytics(scrambler_option):
    seq = open("key.txt").read()

    print(check_balance(seq))
    print(check_cyclicity(seq))
    print(check_correlation(seq))
    # print(max(find_periods(seq)))
    # print(get_period(seq))
    # print(find_max_period(seq))
    if scrambler_option == "First":
        print("Период: " + str(find_max_repeating_substring1(seq)))
    else:
        print("Период: " + str(find_max_repeating_substring2(seq)))
