#!/bin/bash

# download the issues or comments using Github API

for (( i=40000;i<=42000;i++ ))
do

curl --url "https://api.github.com/repos/apache/spark/issues/$i" --header "Authorization: Bearer $GithubToken" --header "X-GitHub-Api-Version: 2022-11-28" > "issue_$i.json"
echo "comment $i is done!\n"

done
