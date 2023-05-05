#!/usr/bin/python3.7
import subprocess

command = "ssh remote.naic.edu -t hostname"
subprocess.call(command, shell=True)