#!/bin/bash

RESOLUTION=${1}
SDIR=${2}
TDIR=${3}
PWD=`dirname ${0}`

set -x

if [ $# -lt 3 ]
then
	print "$0" [resolution] [SourceDIR] [TargetDIR]
	exit 1
fi

rm -rf ${TDIR}
cp -r ${SDIR} ${TDIR}
cd ${TDIR}

for img in `ls *.jpg`
do
	#convert -resize ${1}! ${img} new_${img} &
	mogrify -resize ${1}! ${img} &
done
