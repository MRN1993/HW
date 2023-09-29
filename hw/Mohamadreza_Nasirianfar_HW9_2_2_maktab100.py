import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-g', '--user_input', nargs='+')
args = parser.parse_args()

sum = 0 

for num  in args.user_input:
    sum += int(num)

print(sum/len(args.user_input))