import tkinter as tk 
windoew = tk.Tk()


etn_name = tk.Entry(
    master=windoew,
    width=30,
)

def show_resutl():
    farenhit=etn_name.get()
    try:
        result=((int(farenhit)-32))* 5.9
    except:
        result=((float(farenhit)-32))* 5.9

    lbl_result['text'] =result


lbl_farenhit = tk.Label(
    master=windoew,
    text='farenhit : ',
    height=5,
)



lbl_celicus = tk.Label(
    master=windoew,
    text='celicus',
)

btn_clc = tk.Button(
    master=windoew,
    text='calc',
    command=show_resutl,
    width=5,
)
lbl_result =tk.Label(
    master=windoew,
    text='0',
)
lbl_farenhit.grid(row=0,column=0)
etn_name.grid(row=0,column=1)
btn_clc.grid(row=0,column=2)
lbl_celicus.grid(row=1,column=0)
lbl_result.grid(row=1,column=1)
windoew.mainloop()