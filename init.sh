#!/bin/bash
#echo $WORKON_HOME
a=`which virtualenvwrapper.sh`
if [ -z $a ]
then
  sudo apt-get install uwsgi -y && sudo apt-get install python-pip && sudo pip install virtualenv virtualenvwrapper
fi
b=`grep WORKON_HOME ~/.bashrc`
flag=0
if [ -z "${b}" ]
then
  WORKON_HOME=$HOME/Envs
  export WORKON_HOME=${WORKON_HOME}
  echo "export WORKON_HOME=${WORKON_HOME}">>$HOME/.bashrc
  flag=1
	if [ ! -e $WORKON_HOME ]
	then
	  mkdir -p $WORKON_HOME
	fi
fi
if [ ! $WORKON_HOME ]
then
  a=`grep WORKON_HOME ~/.bashrc | awk -F '=' '{print $2}'`
  if [ $a ]
  then
    WORKON_HOME=$a
  else
    WORKON_HOME=$HOME/Envs
  fi
  export WORKON_HOME=${WORKON_HOME}
fi
c=`grep virtualenvwrapper.sh ~/.bashrc`
if [ -z "${c}" ]
then
  echo "source /usr/local/bin/virtualenvwrapper.sh">>$HOME/.bashrc
  flag=1
fi
if [ $flag -eq 1 ]
then
  echo "please run source ~/.bashrc"
  source ~/.bashrc
fi

echo "over"
#echo $WORKON_HOME
#source /usr/local/bin/virtualenvwrapper.sh
#echo $env_path
#mkvirtualenv  $env_path
#pip install -r r.txt
