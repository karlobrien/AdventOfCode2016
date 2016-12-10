import hashlib

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

doorId = 'ojvtpuvg'
#doorId = 'abc3231929'

count = 0
internalCount = 0
firstResult = set()
while count < 8:
    item = doorId + str(internalCount)
    hsh = hashlib.md5(item).hexdigest()
    internalCount = internalCount + 1

    validHash = hsh.startswith('00000')
    if validHash:
        posCheck = is_number(hsh[5])
        # check if digit
        # check if between 0 and 7
        if posCheck:
            pos = float(hsh[5])
            if (pos >= 0 and pos <= 7):
                if (pos not in firstResult):
                    firstResult.add(pos)
                    count = count + 1
                    print 'Position: ', hsh[5]
                    print 'Char:', hsh[6]