#! /bin/bash

cpu=$(cat /sys/class/thermal/thermal_zone0/temp)
gpu=$(/opt/vc/bin/vcgencmd measure_temp | cut -c6-7)

clear
echo
echo
echo " ---------------------------------------------------"
echo "|"
echo "| $(date +'Son las %H:%M horas del %A %d de %B')"
echo "|"
echo " ---------------------------------------------------"
echo "|"
echo "| Temp. de la CPU/GPU .... $(($cpu/1000)) ºC / $gpu ºC"
echo "|"
echo " ---------------------------------------------------"
echo "|"
echo "| Home de 'pi' ........... $(du /home/pi -h | tail -n1)"
echo "|"
echo " ---------------------------------------------------"
echo "|"
echo "| Memoria RAM ............ $(free -mth | cut -c15-20,39-45 | tail -n1)"
echo "|"
echo " ---------------------------------------------------"
echo "|"
echo "| Tarjeta microSD ........ $(df -h | grep root | cut -c18-23,32-35)"
echo "|"
echo " ---------------------------------------------------"
echo "|"
echo "| Tu ip (wifi) ........... $(ip a | grep "inet 19" | cut -c10-25)"
echo "|"
echo " ---------------------------------------------------"
echo
echo
