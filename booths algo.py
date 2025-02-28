def binary(n, bits):
    if n >= 0:
        return format(n, f'0{bits}b')
    else:
        return format((1 << bits) + n, f'0{bits}b')

def add_binary(a, b, bits):
    result = int(a, 2) + int(b, 2)
    return binary(result, bits)[-bits:]

def twos_complement(value, bits):
    return binary(-int(value, 2), bits)

def arithmetic_shift_right(A, Q, Q_1):
    combined = A + Q + Q_1
    shifted = combined[0] + combined[:-1]
    return shifted[:len(A)], shifted[len(A):-1], shifted[-1]

def booth_algorithm(multiplicand, multiplier, bits=8):
    A = '0' * bits
    Q = binary(multiplier, bits)
    M = binary(multiplicand, bits)
    M_neg = twos_complement(M, bits)
    Q_1 = '0'

    print(f"Initial values: A = {A}, Q = {Q}, Q-1 = {Q_1}, M = {M}, -M = {M_neg}")
    
    for step in range(bits):
        print(f"\nStep {step + 1}:")
        if Q[-1] + Q_1 == '10':
            A = add_binary(A, M_neg, bits)
            print(f"A = A - M -> {A}")
        elif Q[-1] + Q_1 == '01':
            A = add_binary(A, M, bits)
            print(f"A = A + M -> {A}")
        
        A, Q, Q_1 = arithmetic_shift_right(A, Q, Q_1)
        print(f"After shift: A = {A}, Q = {Q}, Q-1 = {Q_1}")
    
    result = A + Q
    print(f"\nFinal result in binary: {result}")
    print(f"Final result in decimal: {int(result, 2) if result[0] == '0' else int(result, 2) - (1 << (2 * bits))}")

if __name__ == "__main__":
    multiplicand = int(input("Enter multiplicand (M): "))
    multiplier = int(input("Enter multiplier(Q): "))
    booth_algorithm(multiplicand, multiplier)
