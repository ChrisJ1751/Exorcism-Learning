def is_armstrong_number(number):
    num_str = str(number)
    exponent = len(num_str)
    total_sum = 0
    for x in num_str:
        total_sum += int(x) ** exponent
    if total_sum == number:
        return True
    else:
        return False
    
