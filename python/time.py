import time 
def fast():
    """""""""
    print("I run Fast !")

def slow():
    """""""""
    time.sleep(0.1)
    print("I run Slow !")
def medium():
    """""""""
    time.sleep(0.5)
    print("I run Medium !")

def main():
    """""""""
    fast()
    slow()
    medium()
if __name__=="__main__":
    main()