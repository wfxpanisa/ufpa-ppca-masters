#!/bin/bash

LD_PRELOAD=$2 $1 & export KPID=$!

sleep $3

if [[ $4 -gt 0 ]]
then
	kill -30 $KPID
	sleep $4
fi

kill -9 $KPID
