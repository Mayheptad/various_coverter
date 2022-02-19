

from tkinter import Tk, Button, Label, Entry

window = Tk()
window.title('Miles to Kilometer Converter')
window.config(padx=20, pady=20)

FONT = ('arial', 12, 'bold')


def handle_calc():
    if mile_input_box.get() != '' and mile_input_box.get() != ' ':
        result['text'] = round(float(mile_input_box.get()) * 1.609)


is_equal_to = Label(text='is equal to', font=FONT)
is_equal_to.grid(column=0, row=1)

mile_input_box = Entry(width=20)
mile_input_box.grid(column=1, row=0)

miles = Label(text='Miles', font=FONT, padx=20)
miles.grid(column=2, row=0)

result = Label(text=0, font=FONT)
result.grid(column=1, row=1)

km = Label(text='Km', font=FONT)
km.grid(column=2, row=1)

calc_btn = Button(text='Calculate', command=handle_calc)
calc_btn.grid(column=1, row=2)


# top_title = Label(text='Mile to Km Converter', font=('arial', 24, 'bold'))
# top_title.grid(column=0, row=0)
#
#
# def handle_click():
#     top_title['text'] = 'New Value'
#     top_title['text'] = text_input.get()
#
#
# button = Button(text='click me', command=handle_click)
# button.grid(column=1, row=1)
#
# text_input = Entry(width=10)
# text_input.grid(column=3, row=2)
#
# sample_label = Label(text='new button', font=('arial', 24, 'bold'))
# sample_label.grid(column=2, row=0)


window.mainloop()
