#python monitor/order_pass_rate.py -p r360,h5,58,normal.first -d now -a email -s marui@daixiaomi.com;Ma123456 -r marui@daixiaomi.com -t h5s_monitor_from_rules100
#python t.py -p r360,h5,58,normal.first -d now -a email -s marui@daixiaomi.com,Ma123456 -r marui@daixiaomi.com -t h5s_monitor_from_rules100
"""

import argparse
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.integers
print args.accumulate

print(args.accumulate(args.integers))
"""
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-p','--product')
parser.add_argument('-d','--date')
parser.add_argument('-a','--action')
parser.add_argument('-s','--sender')
parser.add_argument('-r','--receiver')
parser.add_argument('-t','--title')

args = parser.parse_args()
print args.product.split(',')
print args.title
