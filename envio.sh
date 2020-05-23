#!/bin/bash

TOKEN="1069120953:AAF4Ckcgu93ATG5RTsHaEHzGIR6uoq8wZqo"
ID="705071120"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

MENSAJE="La raspberry PI-Hole, PiVPN y Amule server se acaba de encender."
MENSAJE2="Conecxion a la Raspberry por ssh con la IP $(echo $SSH_CLIENT | awk '{ print $1}')."

curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE"
curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE2"

