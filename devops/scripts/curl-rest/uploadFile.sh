#!/usr/bin/env bash

if [ -z "$1" ]; then echo "please specify an address"; exit -1;
fi
if [ -z "$2" ]; then echo "please specify a filename"; exit -1;
fi
IP=$1
FILENAME=$2
SESSION_ID=`cat .session | grep session_id | cut -f7`
curl https://$IP/api/upload/plugins --request POST -k --cookie session_id=$SESSION_ID --upload-file $FILENAME -H "Expect:"
