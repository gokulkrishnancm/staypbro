#!/usr/bin/python3

from sys import argv
from os import system, path
import subprocess

def main():
    if (len(argv) != 2):
        print("Usage ./staypbro.py <file.c>")
        return False

    c_file = argv[1]
    exe_file = 'debug'
    gdb_file = 'tmp'

    C99(c_file)
    gdb(exe_file)
    parser(gdb_file)
    
    subprocess.Popen(['rm', exe_file, gdb_file])
    return True

def C99(file):
    exe = subprocess.Popen(['gcc', '-g', file, '-o', 'debug'],\
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stderr = exe.communicate()
    if stderr is None:
        print(stderr)
        return False
    return True

def gdb(file):
    command = "echo run | gdb ./{} > tmp".format(file)
    system(command)
    if (path.exists('tmp')):
        return True
    print("[!] Error running gdb")
    return False

def parser(gdb_file):
    with open(gdb_file) as file:
        whole_file =  file.readlines()
        print("[!] Segmentation fault might probably be at line...")
        print(whole_file[20], end='')

if __name__ == "__main__":
    main()
