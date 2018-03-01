#!/usr/bin/env bash

if [ -z "$1" ]; then echo "please specify an address"; exit -1;
fi
IP=$1
SESSION_ID=`cat .session | grep session_id | cut -f7`
curl https://$IP/api/transaction --request GET -k --cookie session_id=$SESSION_ID | jq ".body.status"
