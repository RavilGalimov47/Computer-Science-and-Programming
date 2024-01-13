import re

pattern_first = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"
pattern_second = r"[АВЕКМНОРСТУХ]{2}\d{2}\d{2,3}"

text = "С227НА777 КУ22777 Т22В7477 М227К19У9 С227НА777".split()

for i in text:
    if re.fullmatch(pattern_first, i):
        print(f"Частный | {i}")
    elif re.fullmatch(pattern_second, i):
        print(f"Такси | {i}")
    else:
        print(f"Не номер | {i}")