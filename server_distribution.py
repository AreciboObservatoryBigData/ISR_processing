#!/usr/bin/python3.7
import subprocess
import os
import multiprocessing as mp

current_working_dir = os.getcwd()
#grab the current working directory from where the program is running
input_path_file = "inputs/server_distribution_testing.txt"
logs_base_dir = "outputs/logs"


server_names = ["gpuserv0", "gpuserv1", "gpuserv3", "gpuserv4", "gpuserv5"]

def main():
    with open (input_path_file,"r") as f:
        #read file line  by line saving in each line in the line variable
        server_commands =[]
        for line in f:
            line = line[:-1]
            #remove last element from the line variable which is the new line char
            elements = line.split("\t")
           #separate the elements by the tab character and save them in the list elements 
            server_command = f"python3.7 rawr_execute_args.py -d \"{elements[0]}\" -f \"{elements[1]}\" -o \"{elements[2]}\""
            #create command with current data inside elements list
            server_commands.append(server_command)
            #save command to list of commands
  
    server_submission_commands = []
    i = 0
    pool = mp.Pool()

    for server_command in server_commands:
        #  append to server_command_list of server[i] if not enough elements
        if len(server_submission_commands) < len(server_names):
            #if not enoughcommands for each server, append and continue for
            log_path=os.path.join(logs_base_dir, f"{server_names[i]}.txt")
            command = f"ssh -J remote.naic.edu {server_names[i]} -t 'cd {current_working_dir}; {server_command}' > {log_path}"
            #full command to be sent through the terminal
            server_submission_commands.append(command)
            #save command to list
            i+=1
        else:
            print(f"Submited commands :" + len(server_submission_commands))
            pool.map(run_command, server_submission_commands)
            server_submission_commands=[]
            #reset the command list
            log_path=os.path.join(logs_base_dir, f"{server_names[i]}.txt")
            command = f"ssh -J remote.naic.edu {server_names[i]} -t 'cd {current_working_dir}; {server_command}'> {log_path}" 
            server_submission_commands.append(command)
            #save current the running command to list
            i=1           





def run_command(command):
#created to make the multiprocessing have only one parmeter
     subprocess.call(command, shell=True)
#execute the command through the shell
main()