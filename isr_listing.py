#!/usr/bin/python3.7
import glob
import os
import re

def main():
  complete_list_path = "inputs/complete_dir_list.txt"
  output_file_path = "temp/output_median_list.txt"
  f = open(output_file_path, "w")

  with open(complete_list_path) as file:
    for item in file:
      # if item has Output_Median, then print
      if "Output_Median" in item:
          f.write(item)
  f.close()
  f = open(output_file_path, "r")



  median_year_list_path= "temp/output_median_year_filter_list.txt"
  output_median_year_list_path= "inputs/median_year_filter_list.txt"
  rej_output_median_year_list_path= "outputs/rej_output_median_year_filter_list.txt"



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
  for median_path in f:
    median_path = median_path.replace("\n","")
    raw_path = median_path.replace("Output_Median", "RAW")

    # get starting input filename
    # get all files in raw path
    p_names = glob.glob(os.path.join(raw_path, "*"))
    # get only the basename, without the complete path
    # List comprehension
    p_names = [os.path.basename(item)for item in p_names]
    # equivalent to
    # i=0
    # for item in p_names:
    # p_names[i] = os.path.basename(item)
    # i+=1

    

    results = criterias(p_names)

    if results[0] ==False:
      new_pname = results[1][0]
    else:
      new_pname = str(results[1])

    tab_input_output =  raw_path + "\t" + new_pname + "\t" + median_path + "\n"
  
    if results[0]==False:
      f2.write(tab_input_output)
    else:
      f3.write(tab_input_output)


  os.remove(output_file_path)
  os.remove(median_year_list_path)




def criterias(p_names):
  fail = False
  unique_filenames_no_ext = list(set([name.split(".")[0] for name in p_names]))
  if len(unique_filenames_no_ext) > 1:
    fail = True
  # return if test in the string
  elif "test" in unique_filenames_no_ext[0]:
    fail = True
  elif "hf" in unique_filenames_no_ext[0]:
    fail = True
  else:
    fail = False
  
  return [fail, unique_filenames_no_ext]
  


main()