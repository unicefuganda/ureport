#!/bin/bash


cat ureport_project/target/celery.pid | xargs -I {} kill -9 {}
