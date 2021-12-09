#!/bin/bash
cd /home/pi/share/VPiBackglass
echo "starting"
lxterminal --working-directory='/home/pi/share/VPiBackglass' --command='python3 client.py' -t 'FX3'
echo "closing in 5 seconds"
sleep 5
exit
 

