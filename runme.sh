#!/bin/bash
#spark-submit covid.py
python charting.py
git add *.png
git commit -m "new stuff"
git push
