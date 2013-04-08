#!/bin/bash

# This script is used to execute various build activities

COMMAND=$1


function command.help() {
    echo -e "\nUSAGE:\n"
    echo -e "\nci-control <COMMAND>"
    echo -e "\nCommand is one of [help|update-python-env|run-unit-tests]\n"
}

function command.update-python-env() {
    echo "Updating virtual environment in ${VIRTUALENV_ACTIVATE}"
    bash -c "source ${VIRTUALENV_ACTIVATE} && pip install -r pip-requires.txt"
    echo -e "\nNow the dependencies look like this:\n"
    bash -c "source ${VIRTUALENV_ACTIVATE} && pip freeze"
}

function command.run-unit-tests() {
    cd ureport_project
    echo "Running the unit tests from [`pwd`]"
    cp /home/ureport/localsettings.py .
    rm -rf target/reports
    mkdir -p target/reports
    bash -c "source ${VIRTUALENV_ACTIVATE} && ./manage.py test --settings=ci_settings"
    LAST_COMMAND=$?
    tidy -xml -o target/reports/nosetests.xml target/reports/nosetests.xml
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

    VIRTUALENV_ACTIVATE="${UREPORT_VIRTUAL_ENV_HOME}/bin/activate"

}

function report.config() {
    
    echo "Running in     : [`pwd`]"

    echo "Virtual Env    : [${UREPORT_VIRTUAL_ENV_HOME}]"

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




