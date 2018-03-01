#!/usr/bin/env bash

IP=$1
curl  --digest --user admin:a --cookie-jar cookies -k --basic https://$IP/api/authentication
SESSION_ID=`cat cookies | grep session_id | cut -f7`
curl https://$IP/api/transaction --request POST -k --cookie session_id=$SESSION_ID --data ''
rm -rf cookies
