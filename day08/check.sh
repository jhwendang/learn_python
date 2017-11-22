#/bin/sh
device=$1
item=$2
ps -ef | grep '/usr/bin/iostat -dxkt 1 3' | grep -v grep > /dev/null
if [ $? -ne 0  ]
   then /usr/bin/iostat -dxkt 1 3 > /data/logs/zabbix/iostat_output 2>/dev/null
fi
case $item in
        rrqm)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b"|tail -1|awk '{print $2}'
            ;;
        wrqm)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b"|tail -1|awk '{print $3}'
            ;;
          rps)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b"|tail -1|awk '{print $4}'
            ;;
          wps)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b" |tail -1|awk '{print $5}'
            ;;
        rKBps)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b" |tail -1|awk '{print $6}'
            ;;
        wKBps)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b" |tail -1|awk '{print $7}'
            ;;
    avgrq-sz)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b" |tail -1|awk '{print $8}'
            ;;
    avgqu-sz)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b" |tail -1|awk '{print $9}'
            ;;
        await)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b" |tail -1|awk '{print $10}'
            ;;
        svctm)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b" |tail -1|awk '{print $11}'
            ;;
        util)
            /usr/bin/tail -n20 /data/logs/zabbix/iostat_output |grep "\b$device\b" |tail -1|awk '{print $12}'
            ;;
esac
