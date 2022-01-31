from tkinter import *

FONT_SIZE = 36

app = Tk()
app.title('Scuba Dive Decompression Reader')
app.config()
app.attributes('-fullscreen', True)
app.resizable(False, False)

app.bind("<Escape>", lambda event: app.destroy())

label = Label(app, text='你', font=('Helvetica', FONT_SIZE))
label.pack(side='left')
label.update()
print('CN letter width:', label.winfo_width())

label = Label(app, text='。', font=('Helvetica', FONT_SIZE))
label.pack(side='left')
label.update()
print('CN operator width:', label.winfo_width())

label = Label(app, text='a', font=('Helvetica', FONT_SIZE))
label.pack(side='left')
label.update()
print('EN letter width:', label.winfo_width())

label = Label(app, text='!', font=('Helvetica', FONT_SIZE))
label.pack(side='left')
label.update()
print('EN operator width:', label.winfo_width())

label = Label(app, text='1', font=('Helvetica', FONT_SIZE))
label.pack(side='left')
label.update()
print('Number width:', label.winfo_width())
print('Number height:', label.winfo_height())

label = Label(app, text='111111111111111111', font=('Helvetica', FONT_SIZE), wraplength=199)
label.pack(fill='both')
label.update()
print('Two lines of Number height:', label.winfo_height())

app.mainloop()