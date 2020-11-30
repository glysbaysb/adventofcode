cnt = 0
for line in open('input'):
    vowels = (line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')) >= 3
    double = ("aa" in line or "bb" in line or "cc" in line or "dd" in line or  "ee" in line or "ff" in line or "gg" in line or\
            "hh" in line or "ii" in line or "jj" in line or "kk" in line or "ll" in line or "mm" in line or\
            "nn" in line or "oo" in line or "pp" in line or "qq" in line or "rr" in line or "ss" in line or\
            "tt" in line or "uu" in line or "vv" in line or "ww" in line or "xx" in line or "yy" in line or\
            "zz" in line)
    naughty = not ("ab" in line or "cd" in line or "pq" in line or "xy" in line)

    if vowels and double and naughty:
        cnt = cnt + 1

print(cnt)
