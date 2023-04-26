import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename='logfile.txt')

def print_maturity(age):
    if age >= 18:
        logging.info('Adult!')
    else:
        logging.info('Not adult!!!')

if __name__ == '__main__':
    logging.debug('The program was called with these parameters %s' % sys.argv[1:])
    logging.debug('The first parameter is %s' % sys.argv[1])
    age = int(sys.argv[1])
    print_maturity(age)


