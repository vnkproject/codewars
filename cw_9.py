import re


# def domain_name(url):
#     return url.replace('https://', '').replace('http://', '').replace('http://', '').replace('www.', '').split('.')[0]


# def domain_name(url):
#     return re.search("(//|www.)(\w+)[.]", url).group(2)


def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


if __name__ == "__main__":
    print(domain_name("http://github.com/carbonfive/raygun"))
    print(domain_name("http://www.zombie-bites.com"))
    print(domain_name("https://www.cnet.com"))
    print(domain_name("http://google.com"))
    print(domain_name("http://google.co.jp"))
    print(domain_name("www.xakep.ru"))
    print(domain_name("https://youtube.com"))