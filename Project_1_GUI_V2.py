# Project_1_Converter
# Versin 2.0
# Dated on 12/8/2024
# Created By HK (Harshk Khandal) Hacker


#import
from tkinter import *
from tkinter import messagebox
from ctypes import windll
from tkinter import filedialog
from datetime import date
import webbrowser


windll.shcore.SetProcessDpiAwareness(1)      #Clear

#def()
def bindec():                                #binary to decimal
    bindec = txt_in.get('1.0',END)
    bindeclst2 = []
    bindeclst = bindec.split()

    for i in bindeclst:
        bindeclst2.append(int(i, 2))
        
    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)
    txt_out.insert(1.0,bindeclst2)
    txt_out.config(state=DISABLED)

def hexadec():                               #hexadecimal to decimal
    hexdec = txt_in.get(1.0,END)
    hexdeclst = list(hexdec.split())
    hexdeclst2=[]

    for i in hexdeclst:
        hexdeclst2.append(int(i, 16))

    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)    
    txt_out.insert(1.0,hexdeclst2)
    txt_out.config(state=DISABLED)

def decbin():                                #Decimal to binary
        decbin = txt_in.get(1.0,END)
        decbinlst2 = []
        decbinlst3 = []
        decbinlst = decbin.split()

        for i in decbinlst: 
            i = int(i)
            while i > 0:   
                decbinlst2.append(i%2)
                i = i//2

            decbinlst2.reverse()
            merge = ''.join(map(str, decbinlst2))
            decbinlst3.append(merge)
            decbinlst2=[]

        txt_out.config(state=NORMAL)
        txt_out.delete(1.0,END)    
        txt_out.insert(1.0,decbinlst3)
        txt_out.config(state=DISABLED)

def decoct():                                #Decimal to octal
    decoct = txt_in.get(1.0,END)
    decoctlst2 = []
    decoctlst3 = []
    decoctlst = decoct.split()

    for i in decoctlst: 
        i = int(i)
        while i > 0:   
            decoctlst2.append(i%8)
            i = i//8

        decoctlst2.reverse()
        merge = ''.join(map(str, decoctlst2))
        decoctlst3.append(merge)

        decoctlst2=[]

    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)    
    txt_out.insert(1.0,decoctlst3)
    txt_out.config(state=DISABLED)

def dechex():                                #Decimal to hexadecimal
    dechex = txt_in.get(1.0,END)
    dechexlst2 = []
    dechexlst3 = []
    dechexstr = ""
    dechexlst = dechex.split()

    for i in dechexlst: 
        i = int(i)
        while i > 0:   
            if i%16 <= 9:
                dechexlst2.append(i%16)
                
            if i%16 >= 9:
                match i%16:
                    case 10:
                        dechexlst2.append("A")
                    case 11:
                        dechexlst2.append("B")
                    case 12:
                        dechexlst2.append("C")
                    case 13:
                        dechexlst2.append("D")
                    case 14:
                        dechexlst2.append("E")
                    case 15:
                        dechexlst2.append("F")
            i = i//16

        merge = ''.join(map(str, dechexlst2))
        dechexlst3.append(merge)

        dechexlst2=[]

    for i in dechexlst3:
        dechexstr = dechexstr + i + " "
    
    dechexstr = dechexstr[::-1]

    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)    
    txt_out.insert(1.0,dechexstr)
    txt_out.config(state=DISABLED)

def decascii():                              #Decimal to ascii
    decascii = txt_in.get(1.0,END)

    decasciilst = []
    decasciilst2 = []
    decasciilst=decascii.split()

    for i in decasciilst:
        decasciilst2.append(chr(int(i)))

    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)    
    txt_out.insert(1.0,decasciilst2)
    txt_out.config(state=DISABLED)

def octdec():                                #octal to decimal
    octdec = txt_in.get(1.0,END)
    octdeclst2 = []
    octdeclst = octdec.split()

    for i in octdeclst:
        octdeclst2.append(int(i, 8))

    
    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)    
    txt_out.insert(1.0,octdeclst2)
    txt_out.config(state=DISABLED)

def asciidec():                              #ascii to decimal
    asciidec = txt_in.get(1.0,END)
    asciideclst = []
    asciideclst2 = []
    asciideclst=asciidec.split()

    for i in asciideclst:
        asciideclst2.append(ord(i))

    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)    
    txt_out.insert(1.0,asciideclst2)
    txt_out.config(state=DISABLED)

def morseencode():                           #Morse Encode
    moralp = txt_in.get(1.0,END)
    morlst=[]
    morstr=""
    moralp = list(moralp)

    for i in moralp:
        for j in i:
            match j:
                case "A" | "a":
                    morlst.append('01')
                case "B" | "b":
                    morlst.append('1000')
                case "C" | "c":
                    morlst.append('1010')
                case "D" | "d":
                    morlst.append('100')
                case "E" | "e":
                    morlst.append('0')
                case "F" | "f":
                    morlst.append('0010')
                case "G" | "g":
                    morlst.append('110')
                case "H" | "h":
                    morlst.append('0000')
                case "I" | "i":
                    morlst.append('00')
                case "J" | "j":
                    morlst.append('0111')
                case "K" | "k":
                    morlst.append('101')
                case "L" | "l":
                    morlst.append('0100')
                case "M" | "m":
                    morlst.append('11')
                case "N" | "n":
                    morlst.append('10')
                case "O" | "o":
                    morlst.append('111')
                case "P" | "p":
                    morlst.append('0110')
                case "Q" | "q":
                    morlst.append('1101')
                case "R" | "r":
                    morlst.append('010')
                case "S" | "s":
                    morlst.append('000')
                case "T" | "t":
                    morlst.append('1')
                case "U" | "u":
                    morlst.append('001')
                case "V" | "v":
                    morlst.append('0001')
                case "W" | "w":
                    morlst.append('011')
                case "X" | "x":
                    morlst.append('1001')
                case "Y" | "y":
                    morlst.append('1011')
                case "Z" | "z":
                    morlst.append('1100')
                case "0":
                    morlst.append('11111')
                case "1":
                    morlst.append('01111')
                case "2":
                    morlst.append('00111')
                case "3":
                    morlst.append('00011')
                case "4":
                    morlst.append('00001')
                case "5":
                    morlst.append('00000')
                case "6":
                    morlst.append('10000')
                case "7":
                    morlst.append('11000')
                case "8":
                    morlst.append('11100')
                case "9":
                    morlst.append('11110')
                case " ":
                    morlst.append('/')
                case ".":
                    morlst.append('010101')
                case ",":
                    morlst.append('110011')
                case ":":
                    morlst.append('111000')
                case "?":
                    morlst.append('001100')
                case "'":
                    morlst.append('011110')
                case "-":
                    morlst.append('100001')
                case "/":
                    morlst.append('10010')
                case "(":
                    morlst.append('10110')
                case ")":
                    morlst.append('101101')
                case "\"":
                    morlst.append('010010')
                case "=":
                    morlst.append('10001')
                case "+":
                    morlst.append('01010')
                case "@":
                    morlst.append('011010')
    for i in morlst:
        morstr = morstr + i
        morstr = morstr + " "
    
    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)    
    txt_out.insert(1.0,morstr)
    txt_out.config(state=DISABLED)
    
def morsedecode():                           #Morse Decode
    morsede=txt_in.get(1.0,END)

    mordelst=list(morsede.split())
    mordelst2=[]
    mordestr=""
    
    for i in mordelst:
        match i:
            case '01':
                mordelst2.append('a')

            case '1000':
                mordelst2.append('b')
            
            case '1010':
                mordelst2.append('c')

            case '100':
                mordelst2.append('d')

            case '0':
                mordelst2.append('e')

            case '0010':
                mordelst2.append('f')

            case '110':
                mordelst2.append('g')

            case '0000':
                mordelst2.append('h')

            case '00':
                mordelst2.append('i')

            case '0111':
                mordelst2.append('j')

            case '101':
                mordelst2.append('k')

            case '0100':
                mordelst2.append('l')
            
            case '11':
                mordelst2.append('m')

            case '10':
                mordelst2.append('n')

            case '111':
                mordelst2.append('o')

            case '0110':
                mordelst2.append('p')

            case '1101':
                mordelst2.append('q')

            case '010':
                mordelst2.append('r')

            case '000':
                mordelst2.append('s')

            case '1':
                mordelst2.append('t')

            case '001':
                mordelst2.append('u')

            case '0001':
                mordelst2.append('v')

            case '011':
                mordelst2.append('w')

            case '1001':
                mordelst2.append('x')

            case '1011':
                mordelst2.append('y')

            case '1100':
                mordelst2.append('z')

            case '11111':
                mordelst2.append('0')

            case '01111':
                mordelst2.append('1')

            case '00111':
                mordelst2.append('2')

            case '00011':
                mordelst2.append('3')

            case '00001':
                mordelst2.append('4')

            case '00000':
                mordelst2.append('5')

            case '10000':
                mordelst2.append('6')

            case '11000':
                mordelst2.append('7')

            case '11100':
                mordelst2.append('8')

            case '11110':
                mordelst2.append('9')

            case '010101':
                mordelst2.append('.')

            case '110011':
                mordelst2.append(',')

            case '111000':
                mordelst2.append(':')

            case '001100':
                mordelst2.append('?')

            case '011110':
                mordelst2.append('\'')

            case '100001':
                mordelst2.append('-')

            case '10010':
                mordelst2.append('/')

            case '101101':
                mordelst2.append(')')

            case '10110':
                mordelst2.append('(')

            case '010010':
                mordelst2.append('"')

            case '10001':
                mordelst2.append('=')

            case '01010':
                mordelst2.append('+')

            case '011010':
                mordelst2.append('@')

            case '/':
                mordelst2.append(' ')

            case _ :
                print("Invalid Morse. Please Enter a Correct one.")

    
    

    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)    
    txt_out.insert(1.0,mordestr.join(mordelst2))
    txt_out.config(state=DISABLED)

def proceed():                               #Submit Button
    if choice.get() == 1:
        decbin()
    elif choice.get() == 2 :
        decoct()
    elif choice.get() == 3 :
        dechex()
    elif choice.get() == 4 :
        decascii()
    elif choice.get() == 5 :
        bindec()
    elif choice.get() == 6 :
        octdec()
    elif choice.get() == 7 :
        hexadec()
    elif choice.get() == 8 :
        asciidec()
    elif choice.get() == 9 :
        morseencode()
    elif choice.get() == 10 :
        morsedecode()
    else:
        print("error")

def about():                                 #About Button
    def webpre():
        webbrowser.open_new_tab("https://github.com/Hk-Hacker-Harsh/Converter")

    def webnew():
        webbrowser.open_new_tab("https://github.com/Hk-Hacker-Harsh/Converter_v2")

    def webx():
        webbrowser.open_new_tab("https://x.com/Hk__Hacker")

    def webgh():
        webbrowser.open_new_tab("https://github.com/Hk-Hacker-Harsh")

    def weblt():
        webbrowser.open_new_tab("https://linktr.ee/Hk.Hacker")


    aboutwin= Toplevel()
    aboutwin.geometry("720x350")
    aboutwin.resizable(0,0)
    aboutwin.config(bg='#f6e947')
    aboutwin.title("About Developer")

    Label(aboutwin, text=f"Created By: HK (Harsh Khandal) Hacker\n", font=("",13,"bold","italic"), bg='#f6e947').place(x=15,y=15)
    Label(aboutwin, text="Project: Project 1 Converter (GUI Revised Version)\nVersion: 2.0\nDated On: 12 August 2024\n\nPrevious Version: \n\nThis Version (Feedback): ", font=("",12,""),bg="#f6e947", justify=LEFT).place(x=19,y=65)
    Button(aboutwin,text="Previous Version Link", font=("",9,""),command=webpre).place(x=235,y=170)
    Button(aboutwin,text="This Version Link", font=("",9,""),command=webnew).place(x=315,y=225)

    Button(aboutwin, text="Twitter(X)", font=("",9,""),command=webx).place(x=180,y=320,anchor=CENTER)
    Button(aboutwin, text="Github", font=("",9,""),command=webgh).place(x=360,y=320, anchor=CENTER)
    Button(aboutwin, text="Linktr.ee", font=("",9,""),command=weblt).place(x=540,y=320, anchor=CENTER)

def enable():
    R1.config(state=NORMAL)
    R2.config(state=NORMAL)
    R3.config(state=NORMAL)
    R4.config(state=NORMAL)
    R5.config(state=NORMAL)
    R6.config(state=NORMAL)
    R7.config(state=NORMAL)
    R8.config(state=NORMAL)
    R9.config(state=NORMAL)
    R10.config(state=NORMAL)

def disable():
    R1.config(state=DISABLED, disabledforeground="#313131")
    R2.config(state=DISABLED, disabledforeground="#313131")
    R3.config(state=DISABLED, disabledforeground="#313131")
    R4.config(state=DISABLED, disabledforeground="#313131")
    R5.config(state=DISABLED, disabledforeground="#313131")
    R6.config(state=DISABLED, disabledforeground="#313131")
    R7.config(state=DISABLED, disabledforeground="#313131")
    R8.config(state=DISABLED, disabledforeground="#313131")
    R9.config(state=DISABLED, disabledforeground="#313131")
    R10.config(state=DISABLED, disabledforeground="#313131")

def choose():                                #Submit Button
    txt=""
    if choice.get() == 1 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="Decimal to Binary", font=("",12,"bold","underline","italic"),bg=color).place(x=125,y=25)
        txt="Decimal to Binary"
        Label(hk2,text="This Mode is used to Convert\nDecimal to Binary.\n\nInput should be in Decimal\n Numerical Integer(ex:123)\nform and prgram converts\nit into Binary(ex:10011010010)\nform.", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)
    
    elif choice.get() == 2 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="Decimal to Octal", font=("",12,"bold","underline","italic"),bg=color).place(x=130,y=25)
        txt="Decimal to Octal"
        Label(hk2,text="This Mode is used to Convert\nDecimal to Octal.\n\nInput should be in Decimal\nNumerical Integer(ex:123)\nform and prgram converts\nit into Octal(ex:173) form.", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)

    elif choice.get() == 3 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="Decimal to HexaDecimal", font=("",12,"bold","underline","italic"),bg=color).place(x=90,y=25)
        txt="Decimal to HexaDecimal"
        Label(hk2,text="This Mode is used to Convert Decimal\nto HexaDecimal.\n\nInput should be in Decimal\nNumerical Integer(ex:123)\nform and prgram converts\nit into HexaDecimal(ex:10011010010)\nform.\n\nUse Captial letters to Represent Characters\n(A,B,C,D,E,F).", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)

    elif choice.get() == 4 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="Decimal to ASCII", font=("",12,"bold","underline","italic"),bg=color).place(x=125,y=25)
        txt="Decimal to ASCII"
        Label(hk2,text="This Mode is used to Convert\nDecimal to ASCII.\n\nInput should be in Decimal\nNumerical Integer(ex:65)\nform and prgram converts\nit into ASCII(ex:A) form.", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)

    elif choice.get() == 5 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="Binary to Decimal", font=("",12,"bold","underline","italic"),bg=color).place(x=125,y=25)
        txt="Binary to Decimal"
        Label(hk2,text="This Mode is used to Convert\nBinary to Decimal.\n\nInput should be in Binary(ex:1101)\nform and prgram converts\nit into Decimal(ex:13) form.", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)

    elif choice.get() == 6 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="Octal to Decimal", font=("",12,"bold","underline","italic"),bg=color).place(x=130,y=25)
        txt="Octal to Decimal"
        Label(hk2,text="This Mode is used to Convert\nOctal to Decimal.\n\nInput should be in Octal(ex:173)\nform and prgram converts\nit into Decimal(ex:123) form.", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)

    elif choice.get() == 7 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="HexaDecimal to Decimal", font=("",12,"bold","underline","italic"),bg=color).place(x=85,y=25)
        txt="HexaDecimal to Decimal"
        Label(hk2,text="This Mode is used to Convert\nHexaDecimal to Decimal.\n\nInput should be in HexaDecimal(ex:AD)\nform and prgram converts\nit into Decimal(ex:173) form.", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)
        
    elif choice.get() == 8 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="ASCII to Decimal", font=("",12,"bold","underline","italic"),bg=color).place(x=125,y=25)
        txt="ASCII to Decimal"
        Label(hk2,text="This Mode is used to Convert\nASCII to Decimal.\n\nInput should be in ASCII(ex:a)\nform and prgram converts\nit into Decimal(ex:97) form.\n\nCharacters should be Space\nSeparated.", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)
        
    elif choice.get() == 9 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="Morse Encode", font=("",12,"bold","underline","italic"),bg=color).place(x=142,y=25)
        txt="Morse Encode"
        Label(hk2,text="This Mode is used to Convert Text\nto Morse or to create Morse Code.\n\nInput should be in Characters\n(Text)(ex:h) form and prgram\nconverts or encodes it into\nMorse(ex:0000) Code.\n\nInput should be in Sentence\nform(ex:Python is Language).\n\nOutput will be in 0s(represents .)\n,1s(represents -) and\n/s(represents Spaces).", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)
    elif choice.get() == 10 :
        But2.config(state=NORMAL)
        But3.config(state=NORMAL)
        But5.config(state=NORMAL)
        txt_in.config(bg="#FFFFFF", state=NORMAL)
        But1.config(state=DISABLED)
        disable()
        hk2=Toplevel()
        hk2.geometry("450x540")
        hk2.resizable(0,0)
        hk2.config(bg=color)
        hk2.title("Instructions")
        Label(hk2,text="Morse Decode", font=("",12,"bold","underline","italic"),bg=color).place(x=142,y=25)
        txt="Morse Decode"
        Label(hk2,text="This Mode is used to Convert Morse\nto Text or to Decode Morse Code.\n\nInput should be in 0s\n(represents .), 1s(represents -)\nand /s(represents Spaces)and\nprgram converts or decodes\nit into Characters(Text)\n(ex:0000) form.\n\nInput should be in Morse form\n(ex:0000 00/ 1 0000 0 010 0).\n\nOutput will be in Text(ex:hi there)", bg=color, font=("",11,"")).place(x=225,y=270,anchor=CENTER)

    else:
        messagebox.showwarning(title="Didn't Selected Anything?", message="Please select any of the above options to continue.")

    global lab
    lab=Label(hk,text=txt, font=("",15,"bold","underline","italic"),bg=color)
    lab.place(x=630,y=38.5,anchor=CENTER)

def reset():                                 #Reset Button
    But2.config(state=DISABLED)
    But3.config(state=DISABLED)
    But5.config(state=DISABLED)
    But1.config(state=NORMAL)
    txt_in.delete(1.0,END)
    txt_in.config(state=DISABLED, bg='#d8d8d8')
    txt_out.config(state=NORMAL)
    txt_out.delete(1.0,END)
    txt_out.config(state=DISABLED)
    choice.set(0)
    enable()
    lab.destroy()
    
def fileout():                               #Save to file
    if choice.get() == 1:
        mode = "Decimal to Binary"
    elif choice.get() == 2:
        mode = "Decimal to Octal"
    elif choice.get() == 3:
        mode = "Decimal to Hexadecimal"
    elif choice.get() == 4:
        mode = "Decimal to ASCII"
    elif choice.get() == 5:
        mode = "Binary to Decimal"
    elif choice.get() == 6:
        mode = "Octal to Decimal"
    elif choice.get() == 7:
        mode = "Hexadecimal to Decimal"
    elif choice.get() == 8:
        mode = "ASCII to Decimal"
    elif choice.get() == 9:
        mode = "Morse Encode"
    elif choice.get() == 10:
        mode = "Morse Decode"
    else:
        pass

    text=f'Project_1_Converter.py\nCreated By Hk (Harsh Khandal) Hacker\nDated on : {str(date.today().strftime("%d-%m-%Y"))}\nMode Used : {mode}\n\nInput: {txt_in.get(1.0,END)}\nOutput: {txt_out.get(1.0,END)}\n\nThank You...'
    path=filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text File (*.txt)",".txt")])
    file=open(path.name, "w")
    file.write(text)
    file.close()


color="#f95555"
framecol="#50aff0"

#code
hk = Tk()                                  #window
hk.geometry('1040x540')
hk.resizable(0,0)                          #resize off
hk.title("Project_1_Converter")
hk.config(bg=color)
img= PhotoImage(file='img.png')
hk.iconphoto(True, img)



frame=Frame(hk, bg=framecol, height=988, width=235, relief="groove", bd=4)
frame.place(x=0,y=0)


mode_label= Label(frame, text="Modes", font=('Comic Sans MS',19,"bold","italic","underline"), bg=framecol)
mode_label.place(x=52.5,y=10)

choice = IntVar()

from_dec= Label(frame, text=">> From Decimal", font=('',11,"bold"), bg=framecol)
from_dec.place(x=15, y=75)

R1 = Radiobutton(frame, text="Binary", variable=choice, value=1, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R1.place(x=35,y=105)

R2 = Radiobutton(frame, text="Octal", variable=choice, value=2, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R2.place(x=35,y=135)

R3 = Radiobutton(frame, text="Hexadecimal", variable=choice, value=3, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R3.place(x=35,y=165)

R4 = Radiobutton(frame, text="ASCII", variable=choice, value=4, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R4.place(x=35,y=195)


to_dec= Label(frame, text=">> To Decimal", font=('',11,"bold"), bg=framecol)
to_dec.place(x=15, y=235)


R5 = Radiobutton(frame, text="Binary", variable=choice, value=5, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R5.place(x=35,y=265)

R6 = Radiobutton(frame, text="Octal", variable=choice, value=6, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R6.place(x=35,y=295)

R7 = Radiobutton(frame, text="Hexadecimal", variable=choice, value=7, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R7.place(x=35,y=325)

R8 = Radiobutton(frame, text="ASCII", variable=choice, value=8, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R8.place(x=35,y=355)


morse= Label(frame, text=">> Morse", font=('',11,"bold"), bg=framecol)
morse.place(x=15, y=395)


R9 = Radiobutton(frame, text="Encode", variable=choice, value=9, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R9.place(x=35,y=425)

R10 = Radiobutton(frame, text="Decode", variable=choice, value=10, bg=framecol, activebackground=framecol ,activeforeground="#000000", fg="#000000", font=("",10,""))
R10.place(x=35,y=455)


txt_in= Text(hk, font=('',12,''), height=12,width=28, state=DISABLED, bg="#d8d8d8",padx=10, pady=10)
txt_in.place(x=240,y=77)

txt_out= Text(hk, font=('',12,''), height=12,width=28, bg="#d8d8d8", padx=10, pady=10)
txt_out.config(state=DISABLED)
txt_out.place(x=640,y=77)


But1 = Button(frame, text="Submit", font=("",9,"bold"), command=choose)
But1.place(x=35, y= 490)

But2 = Button(frame, text="Reset",font=("",9,"bold"),command=reset, state=DISABLED)
But2.place(x=120,y=490)

But3 = Button(hk, text="Proceed",font=("",9,""),command=proceed, state=DISABLED)
But3.place(x=591.5,y=432.5)

But4 = Button(hk, text="About Me", font=("",9,""),command=about)
But4.place(x=940,y=497)

But5 = Button(hk, text="Save to File", font=("",9,""), command=fileout, state=DISABLED)
But5.place(x=577.5,y=475)

Label(hk, text="Input", font=("",12,"bold","italic"), bg="#529eff",height=1, width=6, relief="ridge", bd=5).place(x=240,y=77,anchor='sw')
Label(hk, text="Output", font=("",12,"bold","italic"), bg="#529eff",height=1, width=6, relief="ridge", bd=5).place(x=1026,y=77,anchor='se')

hk.mainloop()

# Project_1_Converter
# Versin 2.0
# Dated on 12/8/2024
# Created By HK (Harshk Khandal) Hacker