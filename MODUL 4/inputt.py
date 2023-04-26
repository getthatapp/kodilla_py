import sys

def customized_hello(first_name, last_name, gender):
    print("Hello %s %s %s!" % (first_name, last_name, gender))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    gender = sys.argv[3]
#    print(sys.argv)
customized_hello(first_name, last_name, gender)