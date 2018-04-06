#!/bin/bash
#echo $WORKON_HOME
if [ $1 ]
then
  env_path=$1
else
  env_path=django_test
fi
echo $env_path
source ~/.bashrc
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv  $env_path
echo home=$WORKON_HOME/$env_path >> uwsgi_django_test.ini
pip install -r requirements.txt