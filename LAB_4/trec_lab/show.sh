#!/bin/bash
# this file gives us the map values for each file
for k in 1.2 1.5 1.5 2.0
do
        for b in 0.75 0.0 1.0 0.75
        do
                echo "k = "$k "b = "$b
                trec_eval qrels.trec678.adhoc res_8.$k"."$b".txt"| grep "^map"
        done
done
~                