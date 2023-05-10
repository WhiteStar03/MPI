import random

# 
# DATA SET 1 (10mil random numbers in range 0 - )
# 
def gen1(file):
    f = open(file,'a')

    for i in range(10000000):
        rnd = random.randint(0, 100000)
        f.write(str(rnd)+' ')

    f.flush()
    f.close()

# 
# DATA SET 2 (10mil random numbers in range 0 - 9)
# 
def gen2(file):
    f = open(file,'a')  

    for i in range(10000000):
        rnd = i % 10
        f.write(str(rnd)+' ')

    f.flush()
    f.close()

# 
# DATA SET 3 (10mil numbers ascending them descending)
# 
def gen3(file):
    f = open(file,'a')  
    dec = 500000
    for i in range(10000000):
        if i >= (10000000/2):
            rnd = dec
            dec = dec - 1
        else:
            rnd = i
        f.write(str(rnd)+' ')

    f.flush()
    f.close()

# 
# DATA SET 4 (10mil decreasing order numbers)
# 
def gen4(file):
    f = open(file,'a')  
    for i in range(10000000,0,-1):
        f.write(str(i)+' ')

    f.flush()
    f.close()

# 
# DATA SET 5 (10mil alternating order min, max, min+1, max-1 ...)
# 
def gen5(file):
    f = open(file,'a')  
    for i,j in zip(range(0,5000000),range(5000000,0,-1)):
        f.write(str(i)+' ')
        f.write(str(j)+' ')

    f.flush()
    f.close()

# 
# DATA SET 6 (10mil sorted)
def gen6(file):
    f = open(file,'a')  
    for i in range(0,10000000): 
        f.write(str(i)+' ')

    f.flush()
    f.close()


# 
# MAIN
if __name__ == '__main__':

    name = "bigdata"
    ext = ".txt"
    print ('[*] Test 1')
    file = name + "1" + ext
    gen1(file)
    print ('[*] Test 2')
    file = name + "2" + ext
    gen2(file)
    print ('[*] Test 3')
    file = name + "3" + ext
    gen3(file)
    print ('[*] Test 4')
    file = name + "4" + ext
    gen4(file)
    print ('[*] Test 5')
    file = name + "5" + ext
    gen5(file)
    print ('[*] Test 6')
    file = name + "6" + ext
    gen6(file)


