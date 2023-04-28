#!/usr/bin/python3.7

import glob
import os
import re

complete_list_path = "inputs/complete_list.txt"
output_file_path = "input/output_median_list.txt"
f = open(output_file_path, "w")

with open(complete_list_path) as file:
  for item in file:
    # if item has Output_Median, then print
    if "Output_Median" in item:
        f.write(item)
f.close()
output_file_path = "/share/s3453g1/keysha/Development/ISR/output_median_list.txt"
f = open(output_file_path, "r")

median_year_list_path= "/share/s3453g1/keysha/Development/ISR/median_year_filter_list.txt"
output_median_year_list_path= "/share/s3453g1/keysha/Development/ISR/output_median_year_filter_list.txt"
rej_output_median_year_list_path= "/share/s3453g1/keysha/Development/ISR/rej_output_median_year_filter_list.txt"

f2 = open(median_year_list_path, "w")

for item in f:
    # if item has Output_Median, then print
    if "2017" in item or "2018" in item or "2019" in item or "2020" in item or "2021" in item or "2022" in item:
        f2.write (item)
f.close()
f2.close()

# File contents: {input_path}   {Median_path}
# Where: Input path is the median path but RAW instead of Output_Median
#   The spacing is tab delimited
f = open(median_year_list_path, "r")
f2 = open(output_median_year_list_path, "w")
f3 = open(rej_output_median_year_list_path, "w")
for item in f:
  item = item.replace("\n","")
  raw_path = item.replace("Output_Median", "RAW")

  # get starting input filename
  p_name = glob.glob(os.path.join(raw_path, "*"))
  p_name = [item.replace(raw_path + "/", "").split(".")[0]for item in p_name]
  new_pname = ""
  fail = False

  

  project_names = []
  for item in p_name :
    project_names.append(item.split("_")[0])
    project_names = list(set(project_names))
  
  # if "/net/pkgserv/export/aoweb/datacatalog/utils/sasisrcatalog/2018/10/07/RAW" in raw_path:
  #   breakpoint()
  
  for name in p_name:
    if not name[0].isalpha():
      continue
  
    if not name[1].isnumeric() or not name[2].isnumeric() or not name[3].isnumeric():
      continue

    new_pname = name
  
  tab_input_output =  raw_path + "\t" + new_pname + "\t" + item + "\n"

  if len(project_names) != 1:
        fail = True
  for name in p_name:
    
    if 'test' in name:
      fail = True
      break
  if fail:
    # Add to rejected and continue
    f3.write(tab_input_output)
    continue
    
  if new_pname == "":
    # Add to rejected and continue
    f3.write(tab_input_output)
    continue

  if new_pname[0] == "t" or new_pname[0] == "T":
    f2.write(tab_input_output)
  else:
    # Add to rejected and continue
    f3.write(tab_input_output)