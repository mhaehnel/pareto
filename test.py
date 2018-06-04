#!/usr/bin/env python3

import csv, sys, argparse

from pareto import paretoOptimize

parser = argparse.ArgumentParser(description='Extract pareto front');
parser.add_argument('-f',required=True)
parser.add_argument('fields', metavar='fields', nargs='+')
args = parser.parse_args()

with open(args.f, newline='') as f:
    reader = csv.DictReader(f)
    pareto = paretoOptimize([row for row in reader],args.fields)
    print(','.join(pareto[0].keys()))
    for r in pareto:
        print(','.join(r.values()))

