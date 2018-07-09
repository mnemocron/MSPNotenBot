#!/bin/bash
cd /home/pi/workspace/MSPNotenBot
python msp-check.py -i /mnt/msp/E1811_Info/E1811_Info_HT/2-MSP\ Prüfungsergebnisse/ -s known.txt -r rules.json


# check if directory is still mounted
# else: reboot to trigger a VPN reconnect
sleep 20;
if [ -d "/mnt/msp/E1811_Info" ]; then
        # Control will enter here if $DIRECTORY exists.
        echo "connected"
else
        telegram-bot -u mnemocron -t "MSP Bot Pi\nlost VPN connection, rebooting" && reboot
        sudo reboot
fi

