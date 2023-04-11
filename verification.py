#!/usr/bin/python3.7
import os
import glob

#Input
paths_list="/share/s3453g1/keysha/Development/ISR/output_median_year_filter_list.txt"

with open (paths_list,"r") as f:
        #read file line  by line saving in each line in the line variable
        for line in f:
            #take away \n
            line = line[:-1]
            #it takes the variable, lo divide en tab y lo guarda en elments en una lista
            elements = line.split("\t")

            # Program Variables
            results_output = "/share/s3453g1/keysha/Development/ISR/ISR_Program/output/prog_output_dir.txt"
            results_input = "/share/s3453g1/keysha/Development/ISR/ISR_Program/output/prog_input_dir.txt"

            # absolute path
            input_path= elements[0]
            output_path= elements[2]

            # getting listing
            input_files = glob.glob(os.path.join(input_path, "*"))
            output_files = glob.glob(os.path.join(output_path, "*"))
            
            # delete the output file if it exists
            if os.path.exists(results_output):
                os.remove(results_output)
                

            #Function to find missing or skipped files in the directory's
            def find_missing_numbers(arr):
                # Identify the range of numbers
                n = len(arr)
                min_num = min(arr)
                max_num = max(arr)
                
                # Create a set containing all numbers in the range
                full_list = list(range(min_num, max_num+1))
                # Iterate through the array and remove numbers found
                for num in arr:
                    full_list.remove(num)
                    
                summary = [min_num, max_num,full_list]
                # Return the missing numbers
                return summary
                #start of the input code
            input_identification = []
            input_ext = []


            # getting the input file name
            for file in input_files:
                input_filename = file.split("/")[-1]
                input_id = input_filename.split(".")[0]
                input_ext.append(input_filename.split(".")[-1])
                input_identification.append(input_id)
                input_identification = list(set(input_identification))
                    
            with open(results_input, "w") as file:
                file.write("Unique Input File Name: \n")
                for item in input_identification:
                    file.write(f'{item}\n') 


            ext_int = [int(x) for x in input_ext]
            extra_detail = find_missing_numbers(ext_int)

            with open(results_input, "a") as file:
                file.write("\n Extra Details: \n\n")
                file.write("Minimum number: " + str(extra_detail[0]) + "\n")
                file.write("Maximum number: " + str(extra_detail[1]) + "\n")
                file.write("Missing numbers: " + str(extra_detail[2]) + "\n")

            #start of the output code---------------------------

            output_extensions = {}
            for file in output_files:
                output_files = file.split(".")
                out_type = output_files[1] #file type
                time_ext = output_files[2] #time_ext
                profile_ext = output_files[3] #Ext 2
                # add profile extension to output_extensions[out_type][time_ext] as an append to list
                if out_type not in output_extensions:
                    output_extensions[out_type] = {}
                if time_ext not in output_extensions[out_type]:
                    output_extensions[out_type][time_ext] = []
                output_extensions[out_type][time_ext].append(profile_ext)
            
            out_type_list = list(output_extensions.keys())
            
            passed =True
            # has clppi
            # has toppi
            # is a length of 2
            if len(out_type_list) != 2:
                passed = False
            one_instance = False
            #verify that clppi is inside the variables of out_type_list
            for category in out_type_list:
                if "clppi" in category:
                    one_instance = True
            #if not in return false
            if not one_instance:
                passed = False
            one_instance = False
            #verify that toppi is inside the variables of out_type_list
            for category in out_type_list:
                if "toppi" in category:
                    one_instance = True
            #update the variable passed
            if not one_instance:
                passed = False
          #  if condition is met write to file
            if passed == False:
                with open(results_output, "a") as file:
                    file.write("\n Extra Details: \n\n")
                    file.write("File doesn't only have clppi and toppi. It contains: " + str(out_type_list))
                continue
                
            time_ext_list = list(output_extensions["toppi_1"].keys())
            time_ext_list = [int(x) for x in time_ext_list]
            results=find_missing_numbers(time_ext_list)
        #  find missing numbers
            if len(results[2]) != 0:
                with open(results_output, "a") as file:
                    file.write("\nTheres a missing numbers in Toppi: " + str(results))
            
            time_ext_list = list(output_extensions["clppi_1"].keys())
            time_ext_list = [int(x) for x in time_ext_list]
            results=find_missing_numbers(time_ext_list)
        # if theres a missing number
            if len(results[2]) != 0:
                with open(results_output, "a") as file:
                    file.write("\nTheres a missing numbers in Clppi: " + str(results))

# for each category in output_extensions
            for category in output_extensions.keys():
                ext_1_len = len(output_extensions[category].keys())
                last_i = ext_1_len - 1
                for i, ext1 in enumerate(output_extensions[category].keys()):
                    failed = False
                    ext2_list = output_extensions[category][ext1]
                    ext2_list = [int(x) for x in ext2_list]
                    results=find_missing_numbers(ext2_list)
                    if i == 0:
                        min_num = results[0]
                        max_num = results[1]
                    
                    breakpoint()
                    if len(results[2]) != 0:
                        with open(results_output, "a") as file:
                            file.write("\n\nTheres a missing numbers \n")
                            failed = True
                    elif (results[0] != min_num or results[1] != max_num) and i != last_i:
                        with open(results_output, "a") as file:
                            file.write("\n\nTheres a different mins and max than the rest \n")
                            file.write(f"first min and max: {min_num} {max_num} \n")
                            file.write(f"min and max found: {results[0]} {results[1]} \n")
                            failed = True
                    
                    if failed:
                        with open(results_output, "a") as file:
                            file.write(str(category)+ " " +str(ext1)+ str(results))
                    breakpoint()



