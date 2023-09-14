def cal_total(value, tax):
    total_value = value * (1 + tax / 100)

    return total_value

print(cal_total(1000, 10))
