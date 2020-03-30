from pynput.mouse import Listener
def click(x,y,button,pressed):
    print("Mouse is Clicked at (",x,",",y,")","with",button)


with Listener(on_click=click) as listener:
    listener.join()

