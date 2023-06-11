#!/bin/bash

for (( i=40000;i<=41000;i++ ))
do

curl --url "https://api.github.com/repos/apache/spark/issues/$i/comments" --header "Authorization: Bearer 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" --header "X-GitHub-Api-Version: 2022-11-28" > "comment_$i.json"
echo "comment $i is done!\n"

done