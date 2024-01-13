import re

text = "Он --- серо-буро-малиновая редиска!! >>>:-> А не кот.www.kot.ru"

result = re.findall(pattern="([\b|!|.e]*[А-ЯЁа-яё]+|[\b|!|.]*w{3}.[A-Za-z]+.ru)", string=text)

print(len(result))