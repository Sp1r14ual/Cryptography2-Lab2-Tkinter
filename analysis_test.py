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


def run_analytics():
    seq = open("key.txt").read()

    print(check_balance(seq))
    print(check_cyclicity(seq))
    print(check_correlation(seq))
