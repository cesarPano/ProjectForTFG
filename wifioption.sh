echo "Script para el cambio del módulo wifi (std -> standard, hs -> hotspot):"

if [ "$1" = "std" ]; then
    mv /etc/wpa_supplicant/wpa_supplicant.confx /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null 2> /dev/null;
    /usr/bin/autohotspotN > /dev/null 2> /dev/null;
    echo Despues de hacer cambios, estas son las IPs que tienes:;
    hostname -I;
    exit 0;
fi

if [ "$1" = "hs" ]; then
    mv /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.confx > /dev/null 2> /dev/null;
    /usr/bin/autohotspotN > /dev/null 2> /dev/null;
    echo Despues de hacer cambios, estas son las IPs que tienes:;
    hostname -I;
    exit 0;
fi

echo Parece que tu argumento no vale
