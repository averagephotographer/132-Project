# import Tkinter as tk
# import time

# class Clock():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.label = tk.Label(text="", font=('Helvetica', 48), fg='red')
#         self.label.pack()
#         self.update_clock()
#         self.root.mainloop()

#     def update_clock(self):
#         now = time.strftime("%H:%M:%S")
#         self.label.configure(text=now)
#         self.root.after(1000, self.update_clock)

# app=Clock()

import Tkinter as tk

class Clock(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.clock = tk.Label(self, text="", width=10)
        self.clock.pack()
        self.remaining = 0
        self.countdown(240)

        self.over = False

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.clock.configure(text="time's up!")
            self.over = True
        else:
            self.clock.configure(text="%d:%d" % (int(self.remaining / 60), (self.remaining - int(self.remaining / 60) * 60 )))
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

c = Clock()
c.mainloop()