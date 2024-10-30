import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--variable", dest="variable")
args = parser.parse_args()

print('variable = ' + str(args.variable))