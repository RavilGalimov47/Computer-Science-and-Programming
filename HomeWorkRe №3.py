import re

text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!"

pattern_first = r'\b[0-1][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]\b'
pattern_second = r'\b[0-1][0-9]:[0-5][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]:[0-5][0-9]\b'

result = re.sub(pattern=f"{pattern_second}|{pattern_first}", string=text, repl="(TBD)")

print(result)