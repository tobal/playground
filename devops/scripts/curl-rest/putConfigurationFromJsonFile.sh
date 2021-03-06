#!/usr/bin/env bash

if [ -z "$1" ]; then echo "please specify an address"; exit -1;
fi
if [ -z "$2" ]; then echo "please specify endpoint, at least a '/'"; exit -1;
fi
if [ -z "$3" ]; then echo "please specify JSON filename"; exit -1;
fi
IP=$1
ENDPOINT=$2
FILENAME=$3
SESSION_ID=`cat .session | grep session_id | cut -f7`
curl https://$IP/api/configuration$ENDPOINT --request PUT -k --cookie session_id=$SESSION_ID --data @$FILENAME --header "Content-Type: application/json"
