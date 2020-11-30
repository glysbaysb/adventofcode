import hashlib

key = 'iwrupvqb'

for i in range(1, 1024*1025*100):
    hashed = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()
    if hashed[0:6] == '000000':
        print(i)
        break
