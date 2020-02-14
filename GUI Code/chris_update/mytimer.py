from time import sleep, time
def countdown(n) :
    while n > 0:
        sleep(1)
        if n % 10 == 0:
            print n
        n = n - 1
    if n ==0:
        print('BLAST OFF!')
countdown(10)