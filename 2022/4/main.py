counter = 0
for line in open('input'):
    e1, e2 = line.strip().split(',')
    e1_s, e1_e = e1.split('-')
    e2_s, e2_e = e2.split('-')

    if int(e1_s) >= int(e2_s) and int(e1_e) <= int(e2_e):
        counter = counter + 1
        print(line, "in")
    elif int(e2_s) >= int(e1_s) and int(e2_e) <= int(e1_e):
        counter = counter + 1
        print(line, "in")
    else:
        print(line, "not")
print(counter)


