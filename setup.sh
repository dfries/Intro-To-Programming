#!/bin/bash
cd $(dirname $0)
echo "resetting back to the last commit and removing all new files"
timeout=5
git clean -ndx
git status |grep :
echo "resetting in $timeout seconds, Control-C to interrupt"
sleep 5 || exit 0
echo "resetting"
git reset --hard
git clean -fdx
