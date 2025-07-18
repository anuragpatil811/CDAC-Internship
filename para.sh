#!/bin/bash

echo "Running 4 Monte Carlo simulations in parallel (2 threads each)..."

for i in {1..4}

do

    ./pi <<< 100000000 &

done

wait

echo "All 4 simulations completed."



