#!/usr/bin/env bash

for x in LASTTENFUZ_*; do y=$RANDOM.html; cat ./part_1 >> $y; cat $x >> $y; echo "</div>" >> $y; cat ./part_2 >> $y; mv $y ./tries/; done
