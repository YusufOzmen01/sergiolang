from cpu import CPU
from memory import Memory
import time
import sys
import os

def argError(line, var, type):
    print("ArgumentError: Argument cannot be empty.\nException at line {}\nExpected: {} as {}\n".format(line, var, type))


memory = Memory(8192)    # 8KD (8192 Data)
cpu = CPU(memory,100000) # 100KP (Kilo Processing)

debug = False

try:
    if sys.argv[1] == "--verbose":
        debug = True
        try:
            fi = sys.argv[2]
        except:
            print("""
            sergiolang usage : main.py filename [--verbose]
    
            --verbose : Enables verbose mode.
            --help, -h : Shows this menu.
    
            """)
            sys.exit()
    else:
        fi = sys.argv[1]
    try:
        if sys.argv[2] == "--verbose":
            debug = True
        else:
            print("""
            sergiolang usage : main.py filename [--verbose]
    
            --verbose : Enables verbose mode.
            --help, -h : Shows this menu.
    
            """)
            sys.exit()
            
        
    except:
        pass
    
    if fi == "--help" or fi == "-h":
        print("""
        sergiolang usage : main.py filename [--verbose]
    
        --verbose : Enables verbose mode.
        --help, -h : Shows this menu.
    
        """)
        sys.exit()
except:
    print("""
    sergiolang usage : main.py filename [--verbose]
    
    --verbose : Enables verbose mode.
    --help, -h : Shows this menu.
    
    """)
    sys.exit()


fi = fi.replace(';','')


file = open(fi,'r')
lines = file.readlines()

curLine = 0

for line in lines:
    curLine = curLine + 1
    if debug:
        print("FILE: Reading line " + str(curLine))
        print("FILE: Line is " + line)
    for instruction in cpu.instructions:
        time.sleep(1000 / cpu.clockSpeed)
        if debug:
            print("CPU: " + line.split()[0] + " is being compared with selected instruction " + instruction[0])
        if len(line.split()) == 0:
            pass
        elif line.split()[0] == instruction[0]:
            f = instruction[2](line.split())
            try:
                time.sleep(1000 / cpu.clockSpeed)
                if debug:
                    print("CPU: Argument " + line.split()[1] + " used to execute instruction " + instruction[0])
                    if f == True:
                        print("MEMORY: Applied " + str(memory.applied_memory) + " data into address " + line.split()[1] + ". " + str(memory.capacityLeft()) + " bytes free.")
                    elif f == 2:
                        print('abs cannot continue. Variables used are not number.')
                break
            except:
                argError(curLine,instruction[1],instruction[3])
        time.sleep(1000/cpu.clockSpeed)
