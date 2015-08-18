def fizzbuzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        print "FizzBuzz"
    elif (num % 3 == 0):
        print "Fizz"
    elif (num % 5 == 0):
        print "Buzz"
    else:
        print num

def main():
    for num in range(100):
        fizzbuzz(num+1)
    
    

if __name__ == '__main__':
    main()
    