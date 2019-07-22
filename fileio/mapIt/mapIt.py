import webbrowser, sys
from Tkinter import Tk




your_clipboard=Tk().clipboard_get()
your_cmdline=sys.argv[1]
your_address=" "
(your_address=your_cmdline) if sys.argv[1] else  (your_address=your_clipboard)

baseurl=f"https://www.google.com/maps/place/{your_address}"
