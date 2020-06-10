if [ -z "$1" ]
then
    echo No hay argumentos
    echo el uso adecuado es ./limpiacron.sh palabra
    echo y todas las lineas con palabra seran eliminadas
else
    grep -v $1 /var/spool/cron/crontabs/root > efimero
    chmod 600 efimero
    chown root:crontab efimero
    cp efimero /var/spool/cron/crontabs/root
    rm efimero
fi
