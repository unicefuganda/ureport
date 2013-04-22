#!/bin/bash

echo -e "\n----------------------------------------------------------------------"

echo "Initialising virtual env from [${UREPORT_VIRTUAL_ENV_HOME}]..."

source "${UREPORT_VIRTUAL_ENV_HOME}/bin/activate"

echo -e " "
pip freeze | grep nose

if [[ -z "${UREPORT_HOME}" ]]; then
    echo -e "\nERROR: You must specify UREPORT_HOME as a bash environment variable (points to root of the repo) \n"
    exit -1
fi


echo -e "\n----------------------------------------------------------------------"

echo -e "\nUREPORT_HOME is [${UREPORT_HOME}]"

echo -e "\n----------------------------------------------------------------------\n"

bash -c "cd ${UREPORT_HOME}; ./ci-start-celery.sh ci_settings"  
sleep 2 # Just wait for celery to come up - find a better way to do this!


echo -e "\n----------------------------------------------------------------------"
echo "Going to run the functional tests..."


if [ ! -d "target/reports/functional-test" ]; then 
    mkdir -p target/reports/functional-test
fi

echo -e "----------------------------------------------------------------------"

PYTHONPATH="fixtures:${PYTHONPATH}"

NOSE_ARGS="--with-xunit --xunit-file=target/reports/functional-test/nosetests.ureport.xml"
NOSE_ARGS="${NOSE_ARGS} --verbosity=2"

./nose-wrapper.py ${NOSE_ARGS} scenarios

TEST_SUCCESS=$?

echo -e "----------------------------------------------------------------------\n"

bash -c "cd ${UREPORT_HOME}; ./ci-stop-celery.sh" 

echo -e "\n----------------------------------------------------------------------"

