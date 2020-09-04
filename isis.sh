#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate isis3
input="commands.txt"
while IFS= read -r line
do
  $line
done < "$input"
