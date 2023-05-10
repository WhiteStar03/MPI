import random

# 
# DATA SET 1 (1000 random numbers in range 0 - )
# 
def gen1(file):
    f = open(file,'a')

    for i in range(1000):
        rnd = random.randint(0, 100000)
        f.write(str(rnd)+' ')

    f.flush()
    f.close()

# 
# DATA SET 2 (1000 random numbers in range 0 , 9)
# 
def gen2(file):
    f = open(file,'a')  

    for i in range(1000):
        rnd = i % 10
        f.write(str(rnd)+' ')

    f.flush()
    f.close()

# 
# DATA SET 3 (1000 numbers ascending then descending)
# 
def gen3(file):
    f = open(file,'a')  
    dec = 1000
    for i in range(1000):
        if i >= (1000/2):
            rnd = dec
            dec = dec - 1
        else:
            rnd = i
        f.write(str(rnd)+' ')

    f.flush()
    f.close()

# 
# DATA SET 4 (1000 decreasing order )
# 
def gen4(file):
    f = open(file,'a')  
    for i in range(1000,0,-1):
        f.write(str(i)+' ')

    f.flush()
    f.close()

# 
# DATA SET 5 (1000 alternating order min, max)
# 
def gen5(file):
    f = open(file,'a')  
    for i,j in zip(range(0,500),range(500,0,-1)):
        f.write(str(i)+' ')
        f.write(str(j)+' ')

    f.flush()
    f.close()

# 
# DATA SET 6 (1000 sorted)
def gen6(file):
    f = open(file,'a')  
    for i in range(0,1000): 
        f.write(str(i)+' ')

    f.flush()
    f.close()


# 
# MAIN
if __name__ == '__main__':

    name = "smalldata"
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


