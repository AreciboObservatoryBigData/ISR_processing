#!/usr/bin/python3.7


import os
import sys, getopt
import csv
import shutil

# Import rawr from directory
#################################
# Define rawr path
rawr_path = "/home/isradar/python/pydt3"
# Save current working directory
cwd = os.getcwd()
# Change to directory where rawr.py is
os.chdir(rawr_path)
# Add path to rawr.py
sys.path.insert(0, rawr_path)
# import rawr
import rawr
# Change everything back
os.chdir(cwd)
sys.path.pop(0)


#################################


def main(argv):
    print(argv)

    try:
        opts, args = getopt.getopt(argv, "d:f:o:")
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-d":
            i_dir = arg
            print("Input: " + arg)
        if opt == "-f":
            i_file = arg
            print("File: " + arg)
        if opt == "-o":
            o_dir = arg
            print("Output: " + arg)

    # Count number of file with same name
    names = []
    files = next(os.walk(i_dir))[2]
    names += [f.split(".", 1)[0] for f in files if i_file in f] # add those without extensions
    for name in set(names): # for each unique name-
        fileCount = names.count(name)
        print("{} - Total files found: {}".format(name, names.count(name)))

    # Define parameter dictionary
    thisPD = {}
    # Parameters for reading input
    input = {}
    input['startingfile'] = 0
    input['channel'] = 1     # compute data from this fifo (sampler pair)
    # Parameters for writing results
    output = {}

    ############
    input['inputdir'] = '/share/aserv01/aeron'
    input['filename'] = 't3380_20190829'
    output['outdir'] = '/share/aoweb/datacatalog/utils/sasisrcatalog/2019/08/29/Output'

    input['inputdir'] = i_dir
    input['filename'] = i_file
    output['outdir'] = o_dir
    ############

    thisPD['input'] = input
    thisPD['output'] = output
    # Parameters for computing mracf
    mra = {}
    mra['mrantoacc'] = 2000
    mra['mrachtoallow'] = 1
    thisPD['mra'] = mra
    # Parameters for computing topside
    top = {}
    top['topntoacc'] = 1000
    top['topchtoallow'] = 2
    thisPD['top'] = top
    # Parameters for computing clp
    clp = {}
    clp['clpntoacc'] = 2000
    clp['clpchtoallow'] = 1
    thisPD['clp'] = clp
    # Parameters for computing pwr
    pwr = {}
    pwr['pwrntoacc'] = 2000
    pwr['pwrchtoallow'] = 1
    thisPD['pwr'] = pwr
    thisPD['fileCount'] = fileCount

    # Call RAWR script used by SAS team
 
    rdat = rawr.rawr(thisPD);


    rdat.readandcompute();
    
    # Use current file being processed to create folder for archive
    destFolder = o_dir + i_file
    destFolderClppi = o_dir + i_file + "/clppi"
    destFolderToppi = o_dir + i_file + "/toppi"
    
    print ("Dest Folder: " + destFolder)
    print ("Dest Folder clppi: " + destFolderClppi)
    print ("Dest Folder toppi: " + destFolderToppi)
    
    # Check if folder exists, if not, create
    isExist = os.path.exists(destFolder)
    isExistClppi = os.path.exists(destFolderClppi)
    isExistToppi = os.path.exists(destFolderToppi)
    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(destFolder)
      
    # Look at the Output folder and move files according to clppi/toppi
    files2 = next(os.walk(destFolder))[2]
    # Check for clppi files
    clppis += [f.split(".", 1)[0] for f in files if ".clppi_" in f]
    toppis += [f.split(".", 1)[0] for f in files if ".toppi_" in f]
    # Move clppi files
    for clppi in clppis:
        shutil.move(o_dir + clppi, destFolder + clppi)
        print ("Moved: " + o_dir + clppi + " to " + destFolder + clppi)
    # Move toppi files
    for toppi in toppis:
        shutil.move(o_dir + toppi, destFolder + toppi)
        print ("Moved: " + o_dir + toppi + " to " + destFolder + toppi)



if __name__ == "__main__":
   main(sys.argv[1:])