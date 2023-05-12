#!/usr/bin/python3.7
import subprocess
import os
import multiprocessing as mp
import time

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

    # maximum number of processes to run in parallel
    max_processes = len(server_names)

    # create a pool of processes to run the jobs on
    pool = mp.Pool(processes=max_processes)


    running_processes = []
    i = 0
    for server_command in server_commands[:max_processes]:
        log_path=os.path.join(logs_base_dir, f"{server_names[i]}.txt")
        command = f"ssh -J remote.naic.edu {server_names[i]} -t 'cd {current_working_dir}; {server_command}' > {log_path}"
        #full command to be sent through the terminal
        new_processes = pool.apply_async(runCommand, args=(command))
        # Apply async the command, save result to variable
        running_processes.append(new_processes)
        # append variable to running_processes list
        i += 1




    for server_command in server_commands[max_processes:]:
        finished_process_position = checkFinished(running_processes)
        print("Process at index", finished_process_position, "finished!")
        i = finished_process_position
        log_path=os.path.join(logs_base_dir, f"{server_names[i]}.txt")
        command = f"ssh -J remote.naic.edu {server_names[i]} -t 'cd {current_working_dir}; {server_command}' >> {log_path}"
        new_processes = pool.apply_async(runCommand, args=(command,))
        running_processes[finished_process_position] = new_processes










# def main():
# #  Make exmaple of using .apply to run a process in parallel to another server, while when the server finishes the process, 
# # it will run another process on the same server
# # Use the .apply method and keep track of what each server is doing by using the object reutrned by .apply
#     # list of jobs to run
    
#     jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#     # maximum number of processes to run in parallel
#     max_processes = 5

#     # create a pool of processes to run the jobs on
#     pool = mp.Pool(processes=max_processes)

#     # submit the first batch of jobs to the pool
#     running_processes = [pool.apply_async(runJob, args=(job,)) for job in jobs[:max_processes]]


#     for job in jobs[max_processes:]:
#         finished_process_position = checkFinished(running_processes)
#         print("Process at index", finished_process_position, "finished!")
#         new_processes = pool.apply_async(runJob, args=(job,))
#         running_processes[finished_process_position] = new_processes


def checkFinished(running_processes):
    # Check until one of the processes has finished
    finished_process_found = False
    while finished_process_found == False:
        # Go through each process in the running_processes list and check if it is ready
        for idx, process in enumerate(running_processes):
            status = process.ready()
            if status == True:
                # if the process is ready, then we have found a finished process
                # break out of the for loop
                return idx
        time.sleep(1)


def runCommand(command):
#created to make the multiprocessing have only one parmeter
     subprocess.call(command, shell=True)
#execute the command through the shell


main()