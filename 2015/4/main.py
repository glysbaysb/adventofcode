import hashlib

key = 'iwrupvqb'

for i in range(1, 1024*1025):
    hashed = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()
    if hashed[0:5] == '00000':
        print(i)
        break
