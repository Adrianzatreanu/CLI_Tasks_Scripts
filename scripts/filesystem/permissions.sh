#!/bin/bash

filename="lady_godiva"

if [ -f $filename ]; then
	res=$(ls -l | grep lady_godiva | cut -f 1 -d' ')
	real="-rw-r-xrw-"

	if [ "$res" == "$real" ]; then
		exit 0
	else
		exit 1
	fi
else
	exit 1
fi
