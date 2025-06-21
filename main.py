import keyboard
import time

arr = []
free = ['1','2','3','4','5','6','7','8','9','0','-','+','*','/','(',')',' ']
cursor_ind = 0
is_shift = 0

def print_ans(arr):
    s = ""
    for i in range(len(arr)-1,-1,-1):
        if(arr[i] in free):
            s = arr[i] + s
        else:
            break

    s = s.replace(' ','')

    try:
        ans = str(eval(s))
        keyboard.write(ans)
    except:
        keyboard.write("wtf")

    print(s)

while True:
    event = keyboard.read_event()

    if(event.name == 'shift' and event.event_type == keyboard.KEY_DOWN):
        is_shift = 1
    
    if(event.name == 'shift' and event.event_type == keyboard.KEY_UP):
        is_shift = 0

    
    elif(event.event_type == keyboard.KEY_UP):

        if(event.name == '−'):
            arr.insert(cursor_ind, '-')
            cursor_ind+=1
        elif(event.name == 'left'):
            cursor_ind -=1
        elif(event.name == 'right'):
            cursor_ind += 1
        elif(event.name == 'backspace'):
            try:
                arr.pop(cursor_ind-1)
            except:
                continue
            cursor_ind -=1
            cursor_ind = max(0,cursor_ind)
        elif event.name != 'shift':
            if(is_shift):
                if(event.name == '8'):
                    arr.insert(cursor_ind, '*')
                    cursor_ind+=1
                elif(event.name == '='):
                    arr.insert(cursor_ind, '+')
                    cursor_ind+=1
                elif(event.name == '9'):
                    arr.insert(cursor_ind, '(')
                    cursor_ind+=1
                    arr.insert(cursor_ind, ')')
                elif(event.name == '0'):
                    if(arr[cursor_ind] != ')'):
                        arr.insert(cursor_ind, ')')
                    cursor_ind+=1
                print(arr)
            else:
                arr.insert(cursor_ind, event.name)
                cursor_ind += 1
                if(arr[-1] == '='):
                    arr.pop(-1)
                    print_ans(arr)
                    arr.clear()
                    cursor_ind = 0
        
        
