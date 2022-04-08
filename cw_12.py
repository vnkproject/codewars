# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
# # HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
# # You can find some examples in the test fixtures.

def make_readable(seconds):
    h = seconds//3600
    m = (seconds - h*3600)//60
    s = seconds - h*3600 - m*60
    result = ""
    for i in [h, m, s]:
        if (i > 0) and (i < 10):
            i = f'0{i}'
        elif i > 0:
            i = f'{i}'
        else:
            i = '00'
        result += f':{i}' if result else f'{i}'

    print(result)

#THE BEST
# make_readable=lambda s:f'{s//3600:02}:{s//60%60:02}:{s%60:02}'


if __name__ == "__main__":
    make_readable(0)
    make_readable(5)
    make_readable(60)
    make_readable(86399)
    make_readable(359999)
