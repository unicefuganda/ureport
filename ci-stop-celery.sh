#!/bin/bash

echo "Killing celery deamon with pid `cat ureport_project/target/celery.pid`..."
cat ureport_project/target/celery.pid | xargs -I {} kill -9 {}
