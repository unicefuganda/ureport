#!/bin/bash

SETTINGS_FILE=$1

if [[ -z "${SETTINGS_FILE}" ]]; then
    echo "You must pass in a settings file to run with, e.g. 'ci_settings'"
    exit -1
fi

VIRTUALENV_ACTIVATE="${UREPORT_VIRTUAL_ENV_HOME}/bin/activate"

cd ureport_project

echo "Starting server deamon with settings [${SETTINGS_FILE}.py] running in [`pwd`]"


if [ ! -d "target" ]; then
    mkdir target
fi

echo -e "\nStarting Server...\n" > target/ureport-server.log

#      --plugin-dir=/usr/lib/uwsgi  \
#      --plugins=python \
#       --env DJANGO_SETTINGS_MODULE=ci_settings \
# --chdir=${UREPORT_HOME}/ureport_project \

# http://projects.unbit.it/uwsgi/wiki/Example - Good list of different ways to start uwsgi

uwsgi --master \
      --pp .. \
      --pidfile=target/server.pid \
      --env="DJANGO_SETTINGS_MODULE=ureport_project.${SETTINGS_FILE}" \
      --module=wsgi_app \
      --socket=0.0.0.0:8001 \
      --vacuum \
      --virtualenv=${UREPORT_VIRTUAL_ENV_HOME} \
      -w django_wsgi \
      --daemonize=target/ureport-server.log 
     


#echo $! > target/server.pid

cd ..
