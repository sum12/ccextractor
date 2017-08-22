import ccextractor as cc
import ccx_to_python_g608 as g608
import python_srt_generator as srt_generator
import time
import os
import subprocess
##
#help_string to be included in the documentation
#it is the help string for telling what kind of output the user wants to STDOUT 
#the redirection of output to STDOUT can be changed easily to whatsoever usage the user wants to put in.
##
help_string = """
    Case is the value that would give the desired output.
    case = 0 --> print start_time,end_time,text,color,font
    case = 1 --> print start_time,end_time,text
    case = 2 --> print start_time,end_time,color
    case = 3 --> print start_time,end_time,font
    case = 4 --> print start_time,end_time,text,color
    case = 5 --> print start_time,end_time,text,font
    case = 6 --> print start_time,end_time,color,font
    """
text,font,color = [],[],[]
filename = " "
srt_counter = " "
def generate_output_srt(line):
    global text,font,color
    global filename, srt_counter
    if "filename:" in line:
        filename = str(str(line.split(":")[1]).split("\n")[0])
        #check for an alternative to wipe the output file in python
        with open(filename,'wb+') as fh:
            fh.write("")
            fh.flush()
            os.fsync(fh)
    elif "srt_counter-" in line:
        srt_counter = str(line.split("-")[1])
        with open(filename,'ab+') as fh:
            fh.write(srt_counter)
            fh.flush()
            os.fsync(fh)
    elif "start_time" in line:
        with open(filename,'ab+') as fh:
                data = line.split("-")
                end_time = str(data[-1].split("\n")[0])
                start_time = str(data[1].split("\t")[0])
                fh.write(start_time)
                fh.write(" --> ")
                fh.write(end_time)
                fh.write("\n")
                fh.flush()
                os.fsync(fh)

    elif "***END OF FRAME***" in line:
        data = {}
        data['text'] = text
        data['font'] = font
        data['color'] = color
        srt_generator.generate_output_srt(filename, data)
        text,font,color = [],[],[]
    else:
        g608.g608_grid_former(line,text,color,font)



