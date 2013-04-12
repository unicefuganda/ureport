#!/bin/bash
cd ureport_project

nohup ./manage.py celeryd --settings=celery_test_settings --verbosity=2 > target/celery.log &

echo $! > target/celery.pid
