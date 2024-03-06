import sys
import os
import subprocess
import psutil
import time

def Fleisch(hammelfleisch):
    try:
        process = subprocess.Popen(hammelfleisch, creationflags=subprocess.CREATE_NO_WINDOW)
        print("Started", process.pid)
        return process
    except Exception as e:
        print("???:", e)
        return None

def ok(process, hammelfleisch):
    while True:
        if process.poll() is not None:  
            print("Closed")
            process = Fleisch(hammelfleisch)

def monitor():
    LOLIPOP = "C:LOL.pid"
    if os.path.exists(LOLIPOP):
        with open(LOLIPOP, "r") as f:
            old_pid = int(f.read().strip())
            if psutil.pid_exists(old_pid):
                print("other process running", old_pid)
                sys.exit(1)
    with open(LOLIPOP, "w") as f:
        f.write(str(os.getpid()))

if __name__ == "__main__":
    monitor()

    if len(sys.argv) < 2:
        print("Hide A Cheat or A Software")
        print("CONFIG:")
        print("ARGUMENTS: FILE.EXE")
        time.sleep(3)
        os.system("cls")
        sys.exit(1)

    hammelfleisch = sys.argv[1:]

    bushaltestel = Fleisch(hammelfleisch)

    if bushaltestel is not None:
        ok(bushaltestel, hammelfleisch)
    else:
        print("???")
