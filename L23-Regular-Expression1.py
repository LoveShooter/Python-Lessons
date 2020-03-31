import re

mytext = "Vasya aaaaaaa 1972, Kolya -19727777: Olesya 1981, aaaa@mail.com" \
         "bbbbbbbb@mail.com, Petya ggggggg, 1992, ccccccc@yahoo.com,  " \
         "dddddddd@mail.com, vasya@yandex.ru, hello hello, Misha #43 1984, " \
         "Vladimir 1977, Irina, 2001, annnnnn@gov.gov, trollolo@yandex.ru, " \
         "ooooooooooooo@hotmail.com, ggggg@gov.gov, tutututut@giv.hot"

"""
\d = Any Digit 0-9
\D = Any non Digit a-z
\w = Any Alphabet symbol [A-Z, a-z]
\W = Any Non Aplhabet symbol
\s = breakspace
\S = Non breakspace

[0-9]{3}
[A-Z][a-z]+
\w+\.w+     

"""

textlookfor = r"[A-Z][a-z]+"
allresults = re.findall(textlookfor, mytext)


print(allresults)


