from tkinter import *
width=384
height=484


def c_to_F():
    global frn,cel
    c = float(cel_enter.get())
    frn=((c*float(9/5))+float(32))
    frn_display=Label(win,text=frn,font=("Times",12),bg="brown",fg="white",borderwidth=8,relief=RAISED,width=18)
    frn_display.place(x=90,y=200)

def F_to_c():
    global frn,cel
    f = float(frn_enter.get())
    cel = float((f - float(32)) * float(5 / 9))
    cel_display=Label(win,text=cel,font=("Times",12),bg="brown",fg="white",borderwidth=8,relief=RAISED,width=18)
    cel_display.place(x=90,y=360)

def clr_botn():
    global frn,cel
    frn=""
    cel=""
    cel_enter.delete(0, END)
    frn_enter.delete(0, END)

    cel_display=Label(win,textvariable=cel,font=("Times",12),bg="brown",fg="white",borderwidth=8,relief=RAISED,width=18)
    cel_display.place(x=90,y=360)
    frn_display=Label(win,textvariable=frn,font=("Times",12),bg="brown",fg="white",borderwidth=8,relief=RAISED,width=18)
    frn_display.place(x=90,y=200)
win=Tk()
win.configure(bg="yellow")
win.geometry("%dx%d" % (width, height))
win.title("Tempreture Converter")
bg_image = PhotoImage(file="tc_3.png")
  
# Show image using label
label1 = Label( win, image = bg_image)
label1.place(x = 0, y = 0)
p1 = PhotoImage(file = 'SNDS.png')
win.iconphoto(False, p1)

cel_lbl=Label(win,text="Enter Tempreture(\u00b0C)",font=("Times",14),bg="black",fg="white",borderwidth=8,relief=RAISED)
cel_lbl.place(x=90,y=120)
cel_enter=Entry(win,cursor="ibeam",font=("Times",12),bg="orange",fg="black",borderwidth=8,relief=RAISED)
cel_enter.place(x=90,y=160)
frn_btn=Button(win,text="Convert",command=c_to_F,font=("Times",10),bg="brown",fg="white",borderwidth=8,relief=RAISED)
frn_btn.place(x=90,y=240)

cel_clr_btn=Button(win,text="Clear",command=clr_botn,font=("Times",10),bg="brown",fg="white",borderwidth=8,relief=RAISED)
cel_clr_btn.place(x=165,y=240)

frn_lbl=Label(win,text="Enter Tempreture(\u00b0F)",font=("Times",14),bg="black",fg="white",borderwidth=8,relief=RAISED)
frn_lbl.place(x=90,y=280)
frn_enter=Entry(win,cursor="ibeam",font=("Times",12),bg="orange",fg="black",borderwidth=8,relief=RAISED)
frn_enter.place(x=90,y=320)
cel_btn=Button(win,text="Convert",command=F_to_c,font=("Times",10),bg="brown",fg="white",borderwidth=8,relief=RAISED)
cel_btn.place(x=90,y=400)
frn_clr_btn=Button(win,text="Clear",command=clr_botn,font=("Times",10),bg="brown",fg="white",borderwidth=8,relief=RAISED)
frn_clr_btn.place(x=165,y=400)

exit_btn1=Button(win,text="Exit",command=win.destroy,font=("Times",10),bg="brown",fg="white",borderwidth=8,relief=RAISED)
exit_btn1.place(x=223,y=400)
exit_btn2=Button(win,text="Exit",command=win.destroy,font=("Times",10),bg="brown",fg="white",borderwidth=8,relief=RAISED)
exit_btn2.place(x=223,y=240)
win.mainloop()