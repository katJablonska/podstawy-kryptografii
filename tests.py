from collections import Counter

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            bits = file.read().strip()
            return bits
    except FileNotFoundError:
        print("File nont found.")
        return False

def single_bit_test(bits):
    ones_count = bits.count('1')
    return 9725 < ones_count < 10275

def long_series_test(bits):
    threshold = 26
    current_length = 0
    previous_bit = None

    for bit in bits:
        if bit == previous_bit:
            current_length += 1
        else:
            current_length = 1
        if current_length >= threshold:
            return False
        previous_bit = bit
    return True

def series_test(bits):
    lengths = [0] * 7
    current_length = 1
    current_bit = bits[0]

    for bit in bits[1:]:
        if bit == current_bit:
            current_length += 1
        else:
            if current_length > 6:
                lengths[6] += 1
            else:
                lengths[current_length - 1] += 1
            current_length = 1
            current_bit = bit

    if current_length > 6:
        lengths[6] += 1
    else:
        lengths[current_length - 1] += 1

    return (2315 <= lengths[0] <= 2685 and
            1114 <= lengths[1] <= 1386 and
            527 <= lengths[2] <= 723 and
            240 <= lengths[3] <= 384 and
            103 <= lengths[4] <= 209 and
            103 <= lengths[5] <= 209 and
            103 <= lengths[6] <= 209)

def poker_test(bits):
    num_groups = 5000
    groups = [bits[i:i+4] for i in range(0, len(bits), 4)]
    group_counts = Counter(groups)

    val = sum(count ** 2 for count in group_counts.values())
    test_value = 16 / num_groups * val - 5000
    return 2.16 < test_value < 46.17

bits = read_file("output.txt")

print("Passed single bit test: " + str(single_bit_test(bits)))
print("Passed long series test: " + str(long_series_test(bits)))
print("Passed series test: " + str(series_test(bits)))
print("Passed poker test: " + str(poker_test(bits)))




