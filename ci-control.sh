#!/bin/bash

# This script is used to execute various build activities

COMMAND=$1


function command.help() {
    echo -e "\nUSAGE:\n"
    echo -e "\nci-control <COMMAND>"
    echo -e "\nCommand is [help|update-python-env|run-server|run-unit-tests|run-functional-tests] or one of many others.\n"
}

function command.update-python-env() {
    echo "Updating virtual environment in ${VIRTUALENV_ACTIVATE}"
    bash -c "source ${VIRTUALENV_ACTIVATE} && pip install -r pip-requires.txt"
    echo -e "\nNow the dependencies look like this:\n"
    bash -c "source ${VIRTUALENV_ACTIVATE} && pip freeze"
}

function command.syncdb() {
    echo "Syncing a db, make sure you create an empty one first!"

    cd ureport_project
    bash -c "source ${VIRTUALENV_ACTIVATE} && ./manage.py syncdb --noinput --verbosity=1 --settings=${UREPORT_SETTINGS_FILE}"   
    cd ..
}

function command.migratedb() {
    echo "Migrating a db, make sure you create an empty one first!"

    cd ureport_project

    bash -c "source ${VIRTUALENV_ACTIVATE} && ./manage.py migrate --noinput --verbosity=1 --settings=${UREPORT_SETTINGS_FILE}"

    cd ..
}

function command.init-db() {
    command.syncdb
    command.migratedb
}

function command.shell-celery() {    
    bash -c "source ${VIRTUALENV_ACTIVATE} && ./ci-start-celery.sh ${UREPORT_SETTINGS_FILE}"   

    cd ureport_project
    
    echo "Running the python shell from [`pwd`]"
    bash -c "source ${VIRTUALENV_ACTIVATE} && ./manage.py shell_plus --settings=${UREPORT_SETTINGS_FILE}"

    cd ..

    bash -c "source ${VIRTUALENV_ACTIVATE} && ./ci-stop-celery.sh"   
}

function command.run-server() {
    bash -c "source ${VIRTUALENV_ACTIVATE} && ./ci-start-celery.sh ci_settings"   

    cd ureport_project
    
    echo "Running the python shell from [`pwd`]"
    bash -c "source ${VIRTUALENV_ACTIVATE} && ./manage.py runserver --settings=${UREPORT_SETTINGS_FILE}"

    cd ..

    bash -c "source ${VIRTUALENV_ACTIVATE} && ./ci-stop-celery.sh"       
}

function command.create-superuser() {
    cd ureport_project
    
    echo "Running the python shell from [`pwd`]"
    bash -c "source ${VIRTUALENV_ACTIVATE} && ./manage.py createsuperuser --settings=${UREPORT_SETTINGS_FILE}"

    cd ..
}


function command.run-unit-tests() {
    local NOSE_TEST_REPORT="target/reports/unit-test/nosetests.ureport.xml"

    cd ureport_project
    echo "Running the unit tests from [`pwd`]"
    rm -rf target/reports/unit-test
    mkdir -p target/reports/unit-test/coverage
    bash -c "source ${VIRTUALENV_ACTIVATE} && ./manage.py test --noinput --settings=${UREPORT_SETTINGS_FILE}"
    LAST_COMMAND=$?
    tidy -xml -o ${NOSE_TEST_REPORT} ${NOSE_TEST_REPORT}

    cat ${NOSE_TEST_REPORT} | sed 's_name\=\"nosetests\"_name\=\"unit-tests.ureport\"_'> ${NOSE_TEST_REPORT}.replaced
    mv ${NOSE_TEST_REPORT} ${NOSE_TEST_REPORT}.before
    mv ${NOSE_TEST_REPORT}.replaced ${NOSE_TEST_REPORT}

    cd ..
    ant -f ci-reports.xml


    if [[ `uname` == "Darwin" ]]; then
        open ureport_project/target/reports/unit-test/html/index.html
        open ureport_project/target/reports/unit-test/coverage/index.html 
    else
        echo "To see the reports: open ureport_project/target/reports/unit-test/html/index.html"
        echo "To see the reports: open ureport_project/target/reports/unit-test/coverage/index.html "
    fi

}

function set-test-server-url() {
    TEST_SERVER_IPADDRESS=$1
    awk "/TEST_SERVER_URL/ { \$3=\"\\\"http://${TEST_SERVER_IPADDRESS}\\\"\";print;next; } 1" ureport_project/ci_settings.py > tmp_settings && mv tmp_settings ureport_project/ci_settings.py
}

function command.run-functional-tests-against() {
    set-test-server-url $1
    RUN_ON_DEV_BOX=$2
    run-functional-tests $RUN_ON_DEV_BOX $3
}

function command.run-functional-tests-against-ci() {
    IPADDRESS=$(knife search node ci-dev-appserver -a ipaddress | awk '/ipaddress/ {print $2;}')
    set-test-server-url $IPADDRESS
    RUN_ON_DEV_BOX=$1
    run-functional-tests $RUN_ON_DEV_BOX
}

function command.run-functional-tests() {
    RUN_ON_DEV_BOX=$1
    run-functional-tests $RUN_ON_DEV_BOX
}

#http://stackoverflow.com/questions/6183276/how-do-i-run-selenium-in-xvfb
function run-functional-tests() {
    RUN_ON_DEV_BOX=$1
    FUNCT_FILE=$2
    local NOSE_TEST_REPORT="target/reports/functional-test/nosetests.ureport.xml"

    # Making it possible to run a specific functional test at a time
    #local FUNCTIONAL_TEST_FILE="`pwd`/ureport_project/rapidsms_ureport/ureport/tests/functional/funct_*.py"
    if [[ -z "$FUNCT_FILE" ]]
    then
        local FUNCTIONAL_TEST_FILE="`pwd`/ureport_project/rapidsms_ureport/ureport/tests/functional/funct_*.py"
    else
        local FUNCTIONAL_TEST_FILE="`pwd`/ureport_project/rapidsms_ureport/ureport/tests/functional/$2"
    fi
    
    cd ureport_project
    echo "Running the functional tests from [${FUNCTIONAL_TEST_FILE}]"
    rm -rf target/reports/functional-test
    mkdir -p target/reports/functional-test
    rm -rf target/reports/functional-test/screenshots
    mkdir -p target/reports/functional-test/screenshots
   
    #Do not recreate database on each test run
    export REUSE_DB="1"
 
    if [[ "$RUN_ON_DEV_BOX" == "local" ]]; then
   	bash -c "source ${VIRTUALENV_ACTIVATE} &&  ./manage.py test ${FUNCTIONAL_TEST_FILE} --noinput --verbosity=2 --settings=functional_test_settings"
    else
	bash -c "source ${VIRTUALENV_ACTIVATE} && DISPLAY=:1 xvfb-run ./manage.py test ${FUNCTIONAL_TEST_FILE} --noinput --verbosity=2 --settings=functional_test_settings"
    fi
 
    LAST_COMMAND=$?

    tidy -xml -o ${NOSE_TEST_REPORT} ${NOSE_TEST_REPORT}

    cat ${NOSE_TEST_REPORT} | sed 's_name\=\"nosetests\"_name\=\"functional-tests.ureport\"_'> ${NOSE_TEST_REPORT}.replaced
    mv ${NOSE_TEST_REPORT} ${NOSE_TEST_REPORT}.before
    mv ${NOSE_TEST_REPORT}.replaced ${NOSE_TEST_REPORT}

    cd ..
    ant -f ci-reports.xml report-functional-tests


    if [[ "$RUN_ON_DEV_BOX" == "local" ]]; then
			  echo "Disabled the printing of lines"
        #open ureport_project/target/reports/functional-test/html/index.html
        #open ureport_project/target/reports/functional-test/coverage/index.html 
    else
        echo "To see the reports: open ureport_project/target/reports/functional-test/html/index.html"
        echo "To see the reports: open ureport_project/target/reports/functional-test/coverage/index.html "
    fi
    

}


function setVar() {
    local varName=$1
    local value=$2 
    eval "${varName}=${value}"
}

function defaultArg() {
    local argvalue=$1
    local argname=$2
    local default=$3
       
    if [ -z ${argvalue} ]; then
        setVar ${argname} ${default}
    else
        setVar ${argname} ${argvalue}
    fi
}

function defaultEnv() {
    local envname=$1
    local default=$2    
    eval "local currentValue=\"\${${envname}}\""
         
    if [ -z ${currentValue} ]; then
        echo -e "No environment variable called [${envname}] set, defaulting to [${default}]\n"
        setVar ${envname} ${default}        
    fi      
}


function title() {
    local message=$1
    echo -e "\n--- ${message}\n"
}

function title.done() {
    title "Done."
}

function executeCommandFunction() {
    local COMMAND=$1
    local COMMAND_FUNCTION=$2
    shift
    shift
    local ARGUMENTS=$*
    FUNCTION_EXISTS=$(type "$COMMAND_FUNCTION" 2> /dev/null | grep "is a function")
    if [ -z "$FUNCTION_EXISTS" ] ; then
        echo "Unknown command [$COMMAND]"
	command.help
	exit -1
    fi
    eval $COMMAND_FUNCTION $ARGUMENTS
}

function processCommand() {
    local COMMAND=$1
    shift
    local ARGUMENTS=$*

    echo -e "Executing command [$COMMAND] with arguments [$ARGUMENTS]\n"

    executeCommandFunction $COMMAND "command.$COMMAND" $ARGUMENTS

    echo -e " "
}

function init() {   
    echo -e "\n-----------------------------------------------------------------------------"
    echo -e "CI-Control Script"
    echo "-----------------------------------------------------------------------------"
    CURRENT_DIR=`pwd`
    LAST_COMMAND=0
    defaultEnv "UREPORT_VIRTUAL_ENV_HOME" "/home/ureport/virtualenv/ureport"
    defaultEnv "UREPORT_SETTINGS_FILE" "ci_settings"

    VIRTUALENV_ACTIVATE="${UREPORT_VIRTUAL_ENV_HOME}/bin/activate"

}

function report.config() {
    
    echo "Running in     : [`pwd`]"

    echo "Virtual Env    : [${UREPORT_VIRTUAL_ENV_HOME}]"
    echo "Settings FIle  : [${UREPORT_SETTINGS_FILE}]"

    echo "Args           : [$*]"
    echo "Command        : [${COMMAND}]"
    echo "-----------------------------------------------------------------------------"
}

function report.completed() {
    #type man strftime to see full list of date formatting options.
    CURRENT_DATE=$(date "+%a %d %b %Y")
    CURRENT_TIME=$(date "+%H:%M:%S")
    echo "-----------------------------------------------------------------------------"
    echo "CI-Control Complete at $CURRENT_TIME on $CURRENT_DATE.CI Exiting with [${LAST_COMMAND}]"
    echo -e "-----------------------------------------------------------------------------\n"

}

function exit.with.last.command.status() {
    if [ ${LAST_COMMAND} == 0 ]; then
        echo "Last command was successful"
    fi
    
    exit ${LAST_COMMAND}
}

init
report.config $*
processCommand $*
report.completed
exit.with.last.command.status




