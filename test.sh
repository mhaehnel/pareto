#!/usr/bin/env sh
./test.py  -f demo.csv '<p_pkg' '>tps' | 
    gnuplot -e "set key bottom right; set terminal dumb ansi; set datafile separator comma; plot 'demo.csv' u 'tps':'p_pkg' t 'raw', '<cat' u 'tps':'p_pkg' t 'pareto'"

