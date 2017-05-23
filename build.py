MAX_BITS = 32


def print_binary(num):
    if num is None or num >= 1 or num <= 0:
        return 'ERROR'
    result = ['0', '.']
    fraction = 0.5
    while num:
        if num >= fraction:
            result.append('1')
            num -= fraction
        else:
            result.append('0')
        if len(result) > MAX_BITS:
            return 'ERROR'
        fraction /= 2
    return ''.join(result)
