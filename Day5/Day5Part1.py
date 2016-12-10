import hashlib
m = hashlib.md5()

doorId = 'ojvtpuvg'
doorId = 'abc3231929'

count = 0
internalCount = 0

while count < 8:
    item = doorId + str(internalCount)
    hsh = hashlib.md5(item).hexdigest()
    internalCount = internalCount + 1

    if (hsh.startswith('00000')):
        print hsh


        print hsh[5], hsh[6]
        count = count + 1