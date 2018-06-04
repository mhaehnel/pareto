#!/usr/bin/env python3
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

def _better_aspect(row1,row2,aspect):
    if aspect[0] == '>':
        return float(row1[aspect[1:]]) >= float(row2[aspect[1:]])
    else:
        return float(row1[aspect[1:]]) <= float(row2[aspect[1:]])

def paretoOptimize(data,aspects):
    """
    Calculate the pareto frontier from data

    @param data:    The data to process as a list of dicts. All elements of the list need to have the columns refered to by the aspects.
    @aspects:       A list of strings that denote a sign (> or < for maximize or minimize) immediately followed by the dict key that this optimization should be applied for
    @return:        A list of dicts containing only those list entries from data that lie on the pareto frontier
    @rtype:         list(dict())
    """

    if (len(aspects) < 2):
        print("Need at least two fields to build paretofront!");
        sys.exit(-1)

    if any([x[0] not in ['>','<'] for x in aspects]):
        print("Aspects must indicate minimization (<) or maximization (>) before name")
        sys.exit(-2)
    
    better = lambda row1,row2 : all([_better_aspect(row1,row2,aspect) for aspect in aspects])

    pareto = list()
    for r in data:
            for d in data:
                if d != r and better(d,r): break
            else:
                pareto.append(r)
    return pareto                

