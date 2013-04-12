#!/bin/bash
cd ureport_project

echo "Starting celery deamon with celery_test_settings.py..."

mkdir target
nohup ./manage.py celeryd --settings=celery_test_settings --verbosity=2 > target/celery.log &

echo $! > target/celery.pid

cd ..
