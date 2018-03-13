#!/usr/bin/env bash

set -e

DIRNAME=output
mkdir $DIRNAME
cd $DIRNAME
mkdir certs private
chmod 700 private
echo 01 > serial
touch index.txt

openssl req -x509 -config ../openssl.cnf -newkey rsa:2048 -days 365 -out cacert.pem -outform PEM -subj /CN=ChangeMe/ -nodes

openssl genrsa -out server_key.pem 2048
openssl req -new -key server_key.pem -out server_req.pem -outform PEM -subj /CN=changeme_hostname/O=server/ -nodes
openssl ca -config ../openssl.cnf -in server_req.pem -out server_cert.pem -notext -batch -extensions server_ca_extensions
