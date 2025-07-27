import keyboard

FREE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', '*', '/', '(', ')', 'space','−','c',\
        '#']
SHIFT_KEYS = {'=': '+', '8': '*', '9': '(', '0': ')','3':'#'}
arr = []
is_shift = 0
cursor_ind = 0
keep_last = 0
last_ans = ''

#answer print_function
def print_ans(arr, cursor_ind):
    if('space' in arr):
        arr.remove('space')
    s = "".join(arr[:cursor_ind + 1])
    s = s.replace('−', '-')
    last_ans = ''

    try:
        ans = str(eval(s))
        last_ans = ans
        keyboard.write(ans)
    except:
        pass

    return(last_ans)

while True:
    event = keyboard.read_event()

    #add inline-debug
    if(len(arr)>0 and arr[-1] == '#'):
        if(len(arr)>1 and arr[-2] == 'c'):
            arr.clear()
            print('clear!')
            keyboard.send('backspace')
            keyboard.send('backspace')

    #programm keep all last 100 clicks on keyboard
    if len(arr) > 100:
        arr.pop(0)

    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'shift' or event.name == 'right shift':
            is_shift = 1
    elif event.event_type == keyboard.KEY_UP:
        match event.name:
            case 'delete' if len(arr) > cursor_ind:
                arr.pop(cursor_ind)
            case 'shift' | 'right shift':
                is_shift = 0
            case 'right':
                cursor_ind = min(len(arr), cursor_ind + 1)
            case 'left':
                cursor_ind = max(0, cursor_ind - 1)
            case 'backspace' if arr:
                arr.pop(cursor_ind - 1)
                cursor_ind = max(0, cursor_ind - 1)
            case name if name in SHIFT_KEYS and is_shift:

                if keep_last:
                    keep_last = 0
                    
                arr.insert(cursor_ind, SHIFT_KEYS[name])
                cursor_ind += 1
            case '=':
                last_ans = print_ans(arr, cursor_ind - 1)
                
                keep_last=1
                arr.clear()
                for i in range(len(last_ans)):
                    arr.append(last_ans[i])
                cursor_ind = len(arr)
                print(arr)
            case name if name in FREE:

                if keep_last:
                    if name =='space':
                        arr.clear()
                        cursor_ind =0
                        keep_last=0
                    else:
                        arr.insert(cursor_ind, name)
                        keep_last=0
                        cursor_ind +=1
                else:
                    arr.insert(cursor_ind, name)
                    cursor_ind +=1
                print(arr)
