#!/bin/bash
echo Please Enter UI file name:
read var
pyuic5 -x "$var" -o "C:/Repo Proyecto 4/UI.py"
