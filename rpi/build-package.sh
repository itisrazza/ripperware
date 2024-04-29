#!/bin/bash

#
# Build the RipperWare app 
#

section() {
    echo -e "\e[1m\e[34m==> $1\e[0m"
}

fatal() {
    echo "FATAL! $1" >&2
    exit 1
}

# recreate the work folder
section "Preparing work directory"
rm -rf rpi/work
mkdir -p rpi/work
mkdir -p rpi/out

# copy the app files into
section "Copying code"
cp -r app rpi/work/app
cp -r assets rpi/work/assets

# write out the version meta
echo "$(date +%y%m%d)-$(git rev-parse --short=6 HEAD)" > rpi/work/assets/version

# remove pycache
find rpi/work/app -name __pycache__ -exec rm -r '{}' ';'

# prepare venv
section "Preparing virtual environment"
python3 -m venv rpi/work/venv || fatal "Failed to create virtual environment"
rpi/work/venv/bin/pip install -r requirements.txt || fatal "Failed to package dependencies"

# build archive
section "Compressing release"
cd rpi/work
tar cf ../out/ripperware-"$(cat assets/version)".tar.gz *
cd -

# copy to site
section "Preparing website"
cp rpi/work/assets/version site/version.txt
cp rpi/out/*.tar.gz site
