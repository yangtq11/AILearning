#!/bin/bash
cd ~/yousanAI/baishen
for i in ~/yousanAI/baishen/*
do
	echo "Hello, $i"
done
count=`ls -l|grep '^-'|wc -l`
echo "====file_count:$count===="
