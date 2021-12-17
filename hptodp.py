import tkinter as tk

def hp_to_dp():
	hp = hp_input.get()
	dp = (float(hp) * 131.2)
	lbl_result['text'] = f'One Horsepower = ~131 Duckpower\nYour {hp}hp vehicle has {dp:.0f}dp.'

window = tk.Tk()
window.title('Horsepower Converter')
window.resizable(width=False, height=False)

hp_entry = tk.Frame(master=window)
hp_input = tk.Entry(master=hp_entry, width=10)
lbl_hp = tk.Label(master=hp_entry, text=' Horsepower')

hp_input.grid(row=0, column=0, sticky='e')
lbl_hp.grid(row=0, column=1, sticky='w')

btn_convert = tk.Button(master=window, text='Convert', command=hp_to_dp)
lbl_result = tk.Label(master=window, text=' Duckpower')

hp_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
