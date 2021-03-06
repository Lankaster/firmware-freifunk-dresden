#!/bin/sh

export TITLE="Infos: Status"

. /usr/share/libubox/jshn.sh
. /usr/lib/www/page-pre.sh


cat<<EOF
<h2>$TITLE</h2>
<br>
<fieldset class="bubble">
<legend>Allgemeines</legend>
<table>
<tr><th>Knoten-IP-Adresse:</th><td><a href="https://$_ddmesh_ip/">$_ddmesh_ip</a></td></td></tr>
<tr><th>Internet-Gateway:</th><td><a href="https://$INET_GW/">$INET_GW</a></td></td></tr>
<tr><th>Nameserver:</th><td>$(grep nameserver /tmp/resolv.conf.auto | sed 's#nameserver##g')</td></tr>
<tr><th>Ger&auml;telaufzeit:</th><td>$(uptime)</td></tr>
<tr><th>System:</th><td>$(uname -m) $(cat /proc/cpuinfo | sed -n '/system type/s#system[ 	]*type[ 	]*:##p')</td></tr>
<tr><th>Ger&auml;teinfo:</th><td>$device_model - $(cat /proc/cpuinfo | sed -n '/system type/s#.*:[ 	]*##p') [$(cat /tmp/sysinfo/board_name)]</td></tr>
<tr><th>Firmware-Version:</th><td>Freifunk Dresden Edition $(cat /etc/version) / $DISTRIB_DESCRIPTION</td></tr>
<tr><th>Freier Speicher:</th><td>$(cat /proc/meminfo | grep MemFree | cut -d':' -f2) von $(cat /proc/meminfo | grep MemTotal | cut -d':' -f2)</td></tr>
</table>
</fieldset>
EOF

. /usr/lib/www/page-post.sh
