#!/bin/bash

echo -e "\nStopping server...\n" > ureport_project/target/ureport-server.log

echo "Killing server deamon with pid `cat ureport_project/target/server.pid`..."

cat ureport_project/target/server.pid | xargs -I {} kill -9 {}

echo -e "\nServer stopped." > ureport_project/target/ureport-server.log
