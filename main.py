import keyboard
import time

arr = []

while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_UP and event.name == '=' and arr[-1] != '+':
        s = ""
        for i in range(len(arr)):
            s += arr[i]

        #print(s)
        arr.clear()
        try:
            ans = str(eval(s))
            
            for i in range(len(ans)):
                arr.append(ans[i])

                if(ans[i] == '-'):
                    keyboard.send(74)
                elif(ans[i] == '0'):
                    keyboard.send(11)
                else:
                    keyboard.send(int(ans[i]) + 1)
        except:
            keyboard.send('shift + 7')
        
        #arr.pop(-1)
        #print(eval(s))
        print(s)
        
        
    elif(keyboard.is_pressed('shift + =')):
        arr.append('+')
    elif(keyboard.is_pressed('shift + 8')):
        arr.append('*')
    elif(event.event_type == keyboard.KEY_DOWN):
        #print(event.name)
        if(event.name in ['0','1','2','3','4','5','6','7','8','9','−','/']):
            if(event.name == '−'):
                arr.append('-')
            else:
                arr.append(event.name)
        elif(event.name == 'space' or event.name == 'backspace'):
            arr.clear()
        
        
