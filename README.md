# Sophos XG v18 check RED status

## What it does

* Connect to the XG with SSH
* Grep red.log line and search for a line contains the number of disconnected RED device

## How to use:

Change this line:
`ssh.connect(sophos_host, username='admin', password='password', key_filename='/home/nagios/.ssh/sophosxg')`
to use either your sophos XG admin password or your own SSH private key

## to run:

`python sophos-check-red.py <sophos_xg_ip> `

