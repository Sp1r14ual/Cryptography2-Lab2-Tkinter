from random import randint

shift_register = None
def lfsr1():
    ''' f(x)=x^8 + x^7 + x^6 + x^3 + x^2 + 1 '''
    global shift_register
    feedback_bit = ((shift_register >> 7) ^ (shift_register >> 6) ^ (shift_register >> 5) ^ (shift_register >> 2) ^ (
                shift_register >> 1) ^ 1) & 0x01
    shift_register = (shift_register >> 1) | (feedback_bit << 7)
    return shift_register & 0x01

def lfsr2():
    ''' f(x) = x^8 + x^5 + x^3 + x^2 + 1 '''
    global shift_register
    feedback_bit = ((shift_register >> 7) ^ (shift_register >> 4) ^ (shift_register >> 2) ^ (
                shift_register >> 1) ^ 1) & 0x01
    shift_register = (shift_register >> 1) | (feedback_bit << 7)
    return shift_register & 0x01

def generate_init_state(length):
    result = str()
    for i in range(length):
        result += str(randint(0, 1))
    return int(result, base=2)

def get_gamma(length, scrambler_choice):
    global shift_register
    result = str()
    shift_register = generate_init_state(length)
    if scrambler_choice == "First":
        for i in range(length):
            result += str(lfsr1())
    else:
        for i in range(length):
            result += str(lfsr2())

    return result