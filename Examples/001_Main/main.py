# main.py

import script1
import script2

def main():
    print("Running script 1:")
    script1.function1()

    print("Running script 2:")
    script2.function2()
    
    print(f"x is : {script1.x}")

if __name__ == "__main__":
    main()