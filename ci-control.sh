#!/bin/bash

COMMAND=$1


function command.help() {
    echo -e "\nUSAGE:\n"
    echo -e "\nci-control <COMMAND>"
    echo -e "\nCommand is one of [help|update-python-env|run-unit-tests]\n"
}

function command.update-python-env() {
    echo "Going to update the virtual env"
}

function command.run-unit-tests() {
    echo "Running the unit tests"
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
    CURRENT_DIR=`pwd`
}

function report.config() {
    echo -e "\n-----------------------------------------------------------------------------"
    echo -e "CI Control Script"
    echo "-----------------------------------------------------------------------------"
    echo "Running in     : [`pwd`]"
    echo "Command        : [${COMMAND}]"
    echo "Args           : [$*]"
    echo "-----------------------------------------------------------------------------"
}

function report.completed() {
    #type man strftime to see full list of date formatting options.
    CURRENT_DATE=$(date "+%a %d %b %Y")
    CURRENT_TIME=$(date "+%H:%M:%S")
    echo "-----------------------------------------------------------------------------"
    echo "CI-Control Complete at $CURRENT_TIME on $CURRENT_DATE.CI "
    echo -e "-----------------------------------------------------------------------------\n"

}

init
report.config $*
processCommand $*
report.completed





