#!/bin/sh

#export DISPLAY=:0

# get rid of the cursor so we don't see it when videos are running
#setterm -cursor off
#setterm -blank poke --term linux </dev/tty1


cd /
cd home/pi

# set here the path to the directory containing your videos
VIDEOPATH="usbdrv/vids" 

# you can normally leave this alone
SERVICE="omxplayer"

#unclutter

#setterm -cursor off

# now for our infinite loop!
while true; do
        if ps ax | grep -v grep | grep $SERVICE > /dev/null
        then
        sleep 1;
else
        for entry in $VIDEOPATH/*
        do
 #               clear
                omxplayer -b $entry > /dev/null
#		setterm -cursor off
        done
fi
done

