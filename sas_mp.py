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
input_file_list_path = "/share/s3453g1/keysha/Development/ISR/server_distribution/batch2/ls_input.txt"
def submit_tasks(command):
    return subprocess.run(command,shell=True)




if __name__ == '__main__':

# echo 'Starts' prints "start to terminal"
# cd /share/jalvarad/SASCatalog/ cd is change directory to the path
# #      python3.7 rawr_execute_args.py -d "/net/pkgserv/export/aoweb/datacatalog/utils/sasisrcatalog/2016/11/28/RAW" -f "t1193_20161128" -o "/net/pkgserv/export/aoweb/datacatalog/utils/sasisrcatalog/2016/11/28/Output_Median"
# #nohup python3.7 rawr_execute_args.py -d "/net/pkgserv/export/aoweb/datacatalog/utils/sasisrcatalog/2018/09/21/RAW/" -f "t1193_20180921" -o "/net/pkgserv/export/aoweb/datacatalog/utils/sasisrcatalog/2018/09/21/Output/" > nohup1a.out > error1a.err &
# while IFS=$'\t' read -r -a myArray    a while is loop
# do
# echo "${myArray[0]}"
# echo "${myArray[1]}"
# echo "${myArray[2]}"
#   python3.7 rawr/rawr_execute_arg_jadiel.py -d "${myArray[0]}" -f "${myArray[1]}" -o "${myArray[2]}" 
# #   python3.7 rawr/rawr_execute_arg_jadiel.py -d /net/pkgserv/export/aoweb/datacatalog/utils/sasisrcatalog/2017/08/19/RAW/ -f t3188_20170819 -o /net/pkgserv/export/aoweb/datacatalog/utils/sasisrcatalog/2017/08/19/Output/

# done < SAS_FileList_Unique1_jadiel.txt
# echo 'Ends'
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
            breakpoint()
            #it takes the variable, lo divide en tab y lo guarda en elments en una lista
            elements = line.split("\t")
            command = line
            # command = f"python3.7 rawr_execute_args_jadiel.py -d \"{elements[0]}\" -f \"{elements[1]}\" -o \"{elements[2]}\""
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
    

