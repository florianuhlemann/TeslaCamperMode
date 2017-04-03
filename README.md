# TeslaCamperMode
Python / PHP script for Tesla Model S / Model X to keep the HVAC system powered on.

## Installation Guide
1) Edit ./camper/command.php and change password to your desired password. This doesn't need to be extremely secure, as it is only to prevent free access to the start / stop command.
2) Place the content of the folder "camper" onto your webserver. Note the location of it. (i.e. if it's /var/www/html/camper/command.php use this for the next step)
3) Modify camperMode.py to change the file location according to your location from step 2. It is in line 29. (i.e. /var/www/tesla/camper/is_currently_heating)