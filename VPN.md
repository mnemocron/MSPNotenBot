# VPN Addressen

---


### `mount-msp-drive.sh`

```bash
#!/bin/bash

sudo umount /mnt/msp
# \\fs.edu.ds.fhnw.ch\data\HT\E1811_Info\E1811_Info_HT\2-MSP Prüfungsergebnisse
sudo mount -t cifs -o user=name.nachname,domain=edu.ds.fhnw.ch,password=`cat /home/pi/passwort.txt` //fsemu18.edu.ds.fhnw.ch/E_18_Data11\$ /mnt/msp
```


---

### Cronjob

```bash
*/15 * * * * /home/pi/scripts/cronjob.sh >> /home/pi/scripts/msp.log
```
