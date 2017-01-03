input = '01111001100111011'
length = 272

#input = '10000'
#length = 20

ex1 = '1'
ex2 = '0'
ex3 = '11111'
ex4 = '111100001010'

def Build_Data(item):
    a = item
    b = a[:]
    b = b[::-1]

    stack = []
    for c in b:
        if c is '0':
            stack.append('1')
        elif c is '1':
            stack.append('0')

    answer = a + '0' + ''.join(stack)
    return answer

def make_check_sum(data):
    output = []
    i = 0
    while i < len(data) - 1:
        if data[i] == data[i+1]:
            output.append('1')
        else:
            output.append('0')
        i += 2

    return output

firstPart = Build_Data(input)
while len(firstPart) < length:
    firstPart = Build_Data(firstPart)

disk = firstPart[:length]

chk = make_check_sum(disk)
while len(chk) % 2 == 0:
    chk = make_check_sum(chk)

print ''.join(chk)
