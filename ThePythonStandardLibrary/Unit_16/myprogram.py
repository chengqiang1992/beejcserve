import argparse


# 16.4.2.1. prog参数
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

# parser = argparse.ArgumentParser(prog='myprogram')
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()
# parser.print()

# parser = argparse.ArgumentParser(prog='myprogram')
# parser.add_argument('--foo', help='foo of the %(prog)s program')
# args = parser.parse_args()
# parser.print()


# 16.4.2.2. usage参数
# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
# parser.print_help()

parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
parser.print_help()
