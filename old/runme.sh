#!/bin/bash
set -x
wget --backups=1 --no-check-certificate https://covid.ourworldindata.org/data/owid-covid-data.csv


hdfs dfs -rm owid-covid-data.csv
hdfs dfs -put owid-covid-data.csv

spark-submit covid.py
echo "sparsubmitdone" >> runs.txt

python charting.py

git add .
git commit -m "new stuff"
git push

echo $(date) >> runs.txt
