
from tkinter import filedialog as fd

import cv2
from tkinter import *

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'


root =Tk()
root.title("OPTICAL CHARATER RECOGNITION")
root.geometry('700x500')



filenames=" "
def select_files():
    filetypes = (
        ('Images', '*.*'),
        ('All files', '*.*')
    )

    global filenames 
    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='C:/Users/nandy/OneDrive/Downloads',
        filetypes=filetypes)
    action()
temp=Label(root)
temp.pack()
mybutton=Button(root,text="Select image",command=select_files)
mybutton.pack()
temp2=Label(root)
temp2.pack()




#Extracting text

def action():
    global filenames
    filenames=str(filenames)
    
    filenames=filenames.strip('(')
    filenames=filenames.strip(')')
    filenames=filenames.strip(',')
    filenames=filenames.strip("'")
    img = cv2.imread(filenames)
    def ocr_core(img):
        final_text= pytesseract.image_to_string(img)
        return final_text 
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    def remove_noise (image):
        return cv2.medianBlur (image, 5)
    def thresholding (image):
        return cv2.threshold (image, 8, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img=get_grayscale (img)
    #cv2.imshow('Grayscale',img)
    '''img=thresholding (img)
    cv2.imshow('Thresholding',img)
    img =remove_noise(img)
    cv2.imshow('Remove Noise',img)'''
    extracted_text=ocr_core(img)
    print("\n\n"+extracted_text)
    extracted_text=str(extracted_text)
    extracted_text=extracted_text.strip("")
    txt_fl=open('extracted_text.txt','w')
    txt_fl.write(extracted_text)
    txt_fl.close()

    mylabel.configure(text=extracted_text,font=('arial',18,'bold'))


mylabel2=Label(root,text="Extracted Text",font=("Times new Roman",17,"bold"),bg='orange')
mylabel2.pack()
mylabel=Label(root,text="")
mylabel.pack()



root.mainloop()