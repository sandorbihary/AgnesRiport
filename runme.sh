#!/bin/bash
set -x
source "/home/sanyi/agnesriport/venv/bin/activate"
wget --backups=1 --no-check-certificate https://covid.ourworldindata.org/data/owid-covid-data.csv


rm -f /bd-fs-mnt/kerasnfs/owid-covid-data.csv
cp owid-covid-data.csv /bd-fs-mnt/kerasnfs/owid-covid-data.csv

python covid.py
echo "sparkubmitdone" >> runs.txt

python charting.py

git add .
git commit -m "new stuff"
git push

#echo $(date) >> runs.txt
