#!/bin/bash
#This bash script can be used to download and compile opensees both on Ubuntu and Debian.

cd
HOME=$PWD
sudo apt -y install git
git clone https://github.com/OpenSees/OpenSees.git
sudo apt -y install make
sudo apt -y install tcl8.6
sudo apt -y install tcl8.6-dev
sudo apt -y install gcc
sudo apt -y install g++
sudo apt -y install gfortran
sudo apt -y install python3-dev
mkdir -p bin
mkdir -p lib
cd OpenSees/
cp ./MAKES/Makefile.def.EC2-UBUNTU ./Makefile.def
sed -i 's,'^HOME.*$','HOME="$HOME"','  Makefile.def
make
echo
echo
echo
echo
echo
echo 'Finished successfully! The binary file is in ~/bin/'
