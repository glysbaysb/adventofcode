counter = 0
for line in open('input'):
    e1, e2 = line.strip().split(',')
    e1_s, e1_e = e1.split('-')
    e2_s, e2_e = e2.split('-')

    if int(e1_s) <= int(e2_e) and int(e1_e) >= int(e2_s):
        counter = counter + 1
        print(line, "in")
    else:
        print(line, "not")
print(counter)


