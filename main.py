import keyboard
import pyperclip

FREE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', '*', '/', '(', ')', 'space','−','с','c',\
        '#','ctrl']
SHIFT_KEYS = {'=': '+', '8': '*', '9': '(', '0': ')','3':'#'}
tranq = {'Й':'Q','Ц':'W','У':'E','К':'R','Е':'T',
    'Н':'Y','Г':'U','Ш':'I','Щ':'O','З':'P',
    'Х':'{','Ъ':'}','Ф':'A','Ы':'S','В':'D',
    'А':'F','П':'G','Р':'H','О':'J','Л':'K',
    'Д':'L','Ж':':','Э':'"','Я':'Z','Ч':'X',
    'С':'C','М':'V','И':'B','Т':'N','Ь':'M',
    'Б':'<','Ю':'>','Ё':'~','й':'q','ц':'w',
    'у':'e','к':'r','е':'t','н':'y','г':'u',
    'ш':'i','щ':'o','з':'p','х':'[','ъ':']',
    'ф':'a','ы':'s','в':'d','а':'f','п':'g',
    'р':'h','о':'j','л':'k','д':'l','ж':';',
    'э':"'",'я':'z','ч':'x','с':'c','м':'v',
    'и':'b','т':'n','ь':'m','б':',','ю':'.',
    'ё':'`'}

arr = []
all = []
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
        if(len(arr)>1 and (arr[-2] == 'c' or arr[-2] == 'с')): 
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
        all.append(event.name)
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
                try:
                    arr.pop(cursor_ind - 1)
                except:
                    pass
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
            case 'ctrl':
                if(len(arr)>0 and arr[-1]=='ctrl'):
                    keyboard.send('shift + home,ctrl+c, backspace,alt+shift')
                    
                    text = pyperclip.paste()
                    
                    print(text)
                    for i in range(len(text)):
                        if(97 <= ord(text[i].lower()) <= 123):
                            keyboard.send(text[i].lower())
                        else:
                            if(text[i] in tranq):
                                keyboard.send(tranq[text[i]])
                            else:
                                keyboard.send(text[i])
                    arr.clear()
                else:
                    arr.insert(cursor_ind, 'ctrl')
                    
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
