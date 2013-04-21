#!/bin/bash

SETTINGS_FILE=$1

VIRTUALENV_ACTIVATE="${UREPORT_VIRTUAL_ENV_HOME}/bin/activate"

cd ureport_project

echo "Starting server deamon with ${SETTINGS_FILE}.py running in [`pwd`]"


if [ ! -d "target" ]; then
    mkdir target
fi

echo -e "\nStarting Server...\n" > target/ureport-server.log

#      --plugin-dir=/usr/lib/uwsgi  \
#      --plugins=python \
#       --env DJANGO_SETTINGS_MODULE=ci_settings \

DJANGO_SETTINGS_MODULE=ci_settings

uwsgi --chdir="${UREPORT_HOME}/ureport_project" \
      --master --pidfile=target/server.pid \
      --module=wsgi_app \
      --socket=0.0.0.0:8001 \
      --vacuum \
      --virtualenv=${UREPORT_VIRTUAL_ENV_HOME} \
      --daemonize=target/ureport-server.log 
     


#echo $! > target/server.pid

cd ..
