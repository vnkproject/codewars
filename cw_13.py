# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of
# seconds, in a human-friendly way.
# # The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration
# is expressed as a combination of years, days, hours, minutes and seconds.

def format_duration(s):
    if not s:
        return 'now'
    d = dict(zip(['years', 'days', 'hours', 'minutes', 'seconds'], [s//31536000, s//86400%365, s//3600%24, s//60%60, s%60]))
    r, count = "", 0
    for key, value in d.items():
        if value > 0:
            r += f"{value} {key if value>1 else key[:-1]}, "
            count += 1
    r = r[:-2]
    return f"{r[:r.rfind(', ')]} and {r[r.rfind(', ')+2:]}" if count > 1 else r


# THE BEST
# def format_duration(s):
#     dt = []
#     for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
#         s, m = divmod(s, b)
#         if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
#     return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'

if __name__ == "__main__":
    print(format_duration(1))
    print(format_duration(62))
    print(format_duration(120))
    print(format_duration(3600))
    print(format_duration(97000))
    print(format_duration(0))