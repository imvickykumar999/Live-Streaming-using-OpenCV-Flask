
def move():
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (338, 170)
    mouse.click(Button.left, 2)

move()
