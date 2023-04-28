#!/usr/bin/python3.7

# example of multiprocessing using mp
from multiprocessing import Pool
import subprocess
# Importing the library
import psutil
import time
#RAM get toatal com puter ram 
total_RAM = psutil.virtual_memory().total
#estimated amount of ram consumed per process
RAM_per_process_GB = 30
#input text file
input_file_list_path = "inputs/sas_mp_input.txt"
def submit_tasks(command):
    return subprocess.run(command,shell=True)




if __name__ == '__main__':


    total_RAM_GB = total_RAM * 1e-9
    total_RAM_int = int(total_RAM_GB)
    max_ram_usage = total_RAM_int/2
    pool_size = max_ram_usage/RAM_per_process_GB
    pool_size_int = int(pool_size)
    estimated_RAM = RAM_per_process_GB*pool_size_int
    print("Max number of processes: " ,pool_size_int)
    print("Estimated RAM Usage: ", estimated_RAM, "GB")
    # Read a SAS_File List line by line
    # abre el path como read only y guarda en la variable "f"
    tasks = []
    with open (input_file_list_path,"r") as f:
        #read file line  by line saving in each line in the line variable
        for line in f:

            #take away \n
            line = line[:-1]
            #it takes the variable, lo divide en tab y lo guarda en elements en una lista
            elements = line.split("\t")
            # Command must be same as example
            # Hard coded exaple
            # ./rawr_execute_args.py -d /net/pkgserv/export/aoweb/datacatalog/utils/sasisrcatalog/2017/08/19/RAW -f t3188_20170819 -o /share/s3453g1/keysha/Development/ISR/server_distribution/batch2/test_output/0
            # Actual example
            # ./rawr_execute_args.py -d element[0] -f elements[1] -o element[2]
            command = f"python3.7 rawr_execute_args.py -d \"{elements[0]}\" -f \"{elements[1]}\" -o \"{elements[2]}\""
            
            tasks.append(command)

        
        # task_sublists = [tasks[i:i+pool_size_int] for i in range(0, len(tasks), pool_size_int)]



#create a for loop using tasks
     








#     total_RAM_GB = total_RAM * 1e-9
#     total_RAM_int = int(total_RAM_GB)
#     max_ram_usage = total_RAM_int/2
#     pool_size = max_ram_usage/RAM_per_process_GB
#     pool_size_int = int(pool_size)
#     estimated_RAM = RAM_per_process_GB*pool_size_int
#     print("Max number of processes: " ,pool_size_int)
#     print("Estimated RAM Usage: ", estimated_RAM, "GB")
#    # Getting % usage of virtual_memory ( 3rd field)
 
#     # args = ["ls", "ls"]
#     args = []
#     for i in range(pool_size_int):
#         args.append("sleep 20")

#     with Pool(pool_size_int) as p:
#         print(p.map(f, args))
    

