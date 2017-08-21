import ccextractor as cc
import api_support
import sys,os
import api_testing as tester

output_formats = ['.srt','.ass','.ssa','.webvtt','.sami','.txt','.original','.python','.py']
args_list = sys.argv[1:]
args_count = len(args_list)
if args_count>1:
    print "wrong usage"
    exit(0)
directory = args_list[0]
if not os.path.isdir(directory):
    print "error: path given is not a directory"
    exit(0)
for item in os.listdir(directory):
    ext = os.path.splitext(item)[1]
    if ext not in output_formats:
        print item
