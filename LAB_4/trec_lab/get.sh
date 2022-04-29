#!/bin/bash
# this file gets all the res files for each value of k and b
for k in 1.2 1.5 1.5 2.0
do
        for b in 0.75 0.0 1.0 0.75
        do
                wget -O res_8.$k"."$b".txt" http://clueweb.adaptcentre.ie/IRModelGenerator/res.8.BM25.$k"."$b
        done
done
~    