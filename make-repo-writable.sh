#!/bin/bash

echo -e "\nWARNING! Going to make all your submodules writeable!!!\n"

function make.submodule.writeable() {
    local repo=$1
    local install_path=$3

    cd ${install_path}
    
    echo "in [`pwd`] ..."
    git remote remove origin
    git remote add origin ${repo}

    cd -

}

function make.submodules.writeable() {
    local branch=$1
    echo -e "\nInstalling the submodules on branch [${branch}] now...\n"

    make.submodule.writeable "git@github.com:unicefuganda/django-eav.git" "${branch}" "ureport_project/django_eav"
    make.submodule.writeable "git@github.com:unicefuganda/django-taggit.git" "${branch}" "ureport_project/django_taggit"
    make.submodule.writeable "git@github.com:unicefuganda/monitor_src.git" "${branch}" "ureport_project/qos_monitor"

    make.submodule.writeable "git@github.com:unicefuganda/rapidsms.git" "${branch}" "ureport_project/rapidsms"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-auth.git" "${branch}" "ureport_project/rapidsms_auth"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-contact.git" "${branch}" "ureport_project/rapidsms_contact"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-generic.git" "${branch}" "ureport_project/rapidsms_generic"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-geoserver.git" "${branch}" "ureport_project/rapidsms_geoserver"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-httprouter.git" "${branch}" "ureport_project/rapidsms_httprouter_src"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-message-classifier.git" "${branch}" "ureport_project/rapidsms_message_classifier"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-polls.git" "${branch}" "ureport_project/rapidsms_polls"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-script.git" "${branch}" "ureport_project/rapidsms_script"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-tracking.git" "${branch}" "ureport_project/rapidsms_tracking"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-uganda-common.git" "${branch}" "ureport_project/rapidsms_uganda_common"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-uganda-ussd.git" "${branch}" "ureport_project/rapidsms_uganda_ussd"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-unregister.git" "${branch}" "ureport_project/rapidsms_unregister"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-ureport.git" "${branch}" "ureport_project/rapidsms_ureport"
    make.submodule.writeable "git@github.com:unicefuganda/rapidsms-xforms.git" "${branch}" "ureport_project/rapidsms_xforms_src"


    echo -e "\nDone.\n"
}

read -r -p "Are you sure? [Y/n] " response
case $response in
    [yY][eE][sS]|[yY])         
        make.submodules.writeable
        ;;
    *)
        echo -e "\nOk, don't worry, nothing happened.\n"
        ;;
esac

git submodule status
