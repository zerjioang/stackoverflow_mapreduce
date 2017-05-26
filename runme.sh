#!/bin/bash

echo "Removing previous files..."
#rm *.7z
#rm -rf ./out
echo "Installing required dependencies.."
sudo yum install p7zip
echo "Downloading exercise dataset..."
python2 ./downloader.py
echo "Extracting data..."
7za e $(ls *.7z) -o./out
echo "MOST ACTIVE USERS "
echo "User ID	Post number"
cat ./out/Posts.xml | python2 ./mapper.py | sort | python2 ./reducer.py | sort --key 2 --numeric-sort --reverse | head -n 10
echo "Top 10 most active users on"
echo "StackOverflow selected category"

