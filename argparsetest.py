import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help = "echo the string you put here")
print parser.parse_args()
args = parser.parse_args()
print args.echo