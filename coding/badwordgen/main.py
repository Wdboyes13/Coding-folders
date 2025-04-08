from words import words, slurs
import argparse
import random
parser = argparse.ArgumentParser(description='Generate random bad words')
parser.add_argument('--y', action='store_true', help='Enable slurs')
args = parser.parse_args()
if args.y:
    num = random.randrange(0, 19)
    if num > 11:
        print(slurs[num-12])
    else:
        print(words[num])
else:
    print(words[random.randrange(0, 11)])