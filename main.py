import keyboard

FREE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', '*', '/', '(', ')', ' ']
SHIFT_KEYS = {'=': '+', '8': '*', '9': '(', '0': ')'}
arr = []
is_shift = 0
cursor_ind = 0


def print_ans(arr, cursor_ind):
    s = "".join(arr[:cursor_ind + 1])
    s = s.replace(' ', '')

    try:
        ans = str(eval(s))
        keyboard.write(ans)
    except:
        keyboard.write("wtf")

    print(s)


while True:
    event = keyboard.read_event()

    if len(arr) > 100:
        arr.pop(0)

    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'shift' or event.name == 'right shift':
            is_shift = 1
    elif event.event_type == keyboard.KEY_UP:
        match event.name:
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
                arr.insert(cursor_ind, SHIFT_KEYS[name])
                cursor_ind += 1
            case '=':
                print_ans(arr, cursor_ind - 1)
                arr.clear()
                cursor_ind = 0
            case name if name in FREE:
                arr.insert(cursor_ind, name)
                cursor_ind += 1
