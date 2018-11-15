import subprocess

location = "C:\Users\Joe_T\OneDrive\Desktop\New folder"

subprocess.Popen(r'explorer /select,' + location + "\en-US" )
