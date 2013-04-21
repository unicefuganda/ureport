#!/bin/bash

echo -e "\nStopping celery...\n" > ureport_project/target/celery.log

echo "Killing celery deamon with pid `cat ureport_project/target/celery.pid`..."

cat ureport_project/target/celery.pid | xargs -I {} kill -9 {}

echo -e "\nCelery stopped." > ureport_project/target/celery.log
