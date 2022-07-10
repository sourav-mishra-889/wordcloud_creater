from wordcloud import *
from wordcloud import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import os
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


root = Tk()

root.title('Wordcloud Creater')
root.geometry("800x800") 
root.maxsize(800,800)

photo_frame = Frame(root,width = 120, borderwidth=6, relief=SUNKEN) #creating frame for inserting banner

image1=Image.open("banner.png")

photo1=ImageTk.PhotoImage(image1)

photo_label1=Label(photo_frame,image=photo1)
photo_label1.pack()

photo_frame.pack(side = LEFT,fill=Y)

workspace = Frame(root)
workspace.pack(side=LEFT, fill = BOTH)

buttons = Frame(workspace)
buttons.pack(side=BOTTOM, fill=X)

feature = Frame(workspace,width=75)
feature.pack(fill=Y)

#creating label to select a text file
label = Label(workspace, text=""" Select a text file: """, padx=25, pady=35, font=("Georgia 14")).pack()


#creating function to select text file
def select_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select an text file",
                                               filetypes=(("text file", "*.txt"), ("All files", "*.")))
    
    if root.filename != "":
        label2.config(text = root.filename)
        file_name = root.filename
        root.clipboard_append(file_name)
        return file_name
    else:
        label2.config(text = "Please select a txt file")

#creating labels to show file path and size of selected file in KB
label2 = Label(workspace,width= 75, text=" File Path", borderwidth=6, padx=40, pady=10, bg="white", font=("Georgia 10"), relief=SUNKEN)
label3 = Label(workspace, width = 75, text="", padx=10, pady=10, font=("Georgia 12"))
def upload():
    global file_path
    global filename

    file_path = str(select_file())
    filename = str(os.path.basename(file_path))

    with open(file_path) as file:
        str1 = 'Selected `{}` ({:.2f} kB)'.format(filename, len(file.read()) / 2 **10)
    label3.config(text = str1)

label2.pack()
label3.pack()

select_button = Button(workspace, text="SELECT FILE", borderwidth=4, command=upload, relief = RAISED).pack(pady=2)

#adding label to select back ground color
label4 = Label(feature, text="""Select image Back ground :
colour""", padx=5, pady=5, font=("Georgia 13")).grid(row=0,column=0, pady=15)

n = StringVar() 
Background_color = ttk.Combobox(feature,state="readonly", width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list for taking input background color for image 
Background_color['values'] = (' Black',  
                          ' Blue', 
                          ' Green', 
                          ' Orange', 
                          ' Red',
                          ' White', 
                          ' Yellow')
                
Background_color.grid(row=0,column=1, pady = 23)
Background_color.current(5)

#adding label to select font color
label5 = Label(feature, text="""Select image font :
colour""", padx=5, pady=5, font=("Georgia 13")).grid(row=1,column=0, pady=15)

m = StringVar() 
font_color = ttk.Combobox(feature,state="readonly", width = 27,  
                            textvariable = m) 
  
# Adding combobox drop down list 
font_color['values'] = ('Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'Dark2',
'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PRGn', 'Paired', 'Pastel1', 'Pastel2', 'PiYG', 'PuBu',
'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Set1', 'Set2',
'Set3', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone',
'brg', 'bwr', 'cividis', 'cool', 'coolwarm', 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray',
'gist_heat', 'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 'gray', 'hot',
'hsv', 'inferno', 'jet', 'magma', 'nipy_spectral', 'ocean', 'pink', 'plasma', 'prism', 'rainbow', 'seismic',
'spring', 'summer', 'tab10', 'tab20', 'tab20b', 'tab20c', 'terrain', 'turbo', 'twilight', 'twilight_shifted',
 'viridis','winter')
                
font_color.grid(row =1,column=1, pady = 23)
font_color.current(0)

label9 = Label(feature, text="""Select shape: """, padx=5, pady=5, font=("Georgia 13")).grid(row=2,column=0, pady=15)

k = StringVar() 
masks = ttk.Combobox(feature,state="readonly", width = 27,  
                            textvariable = k)
  
# Adding combobox drop down list 
masks['values'] = ('cloud','girl','india-map','leaf','love-sign',
'shuit-cap','twitter-sign','winebottle','wine-glass')
                
masks.grid(row =2,column=1, pady = 23)
masks.current(0)

#close button to close the main window
close_button = Button(buttons, text="CLOSE", borderwidth=4, padx=20, command=root.quit, relief = RAISED)
close_button.pack(padx=5, pady= 5, side=RIGHT, anchor='nw')

#creting function to determine the frequencies of usable words for word cloud
def calculate_frequencies(file_contents):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    f = list(file_contents.split(" "))
    frequencies = {}
    
    for i in f:
        if i in punctuations:
            continue
        elif i in uninteresting_words:
            continue
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i]=1


    # adding mask to word cloud
    mask = masks.get()+'-mask.png'
    Path = os.path.realpath(mask)
    my_mask = np.array(Image.open(Path))
    
    wordcloud = WordCloud(mask=my_mask, colormap=font_color.get().strip()+"_r", background_color=Background_color.get().lower().strip()).generate(file_contents)
    wordcloud.generate_from_frequencies(frequencies)
    return wordcloud

#creating function to open next window to view word cloud
def nextwindow():
    with open(file_path) as file:
        if file_path!="":
            myimage = calculate_frequencies(file.read())
            plt.figure() 
            plt.imshow(myimage, interpolation = None)
            plt.axis('off')
            plt.show()

#creating function to submit the values to create word cloud
submit_button = Button(buttons, text="SUBMIT", borderwidth=4, padx=20, command=nextwindow, relief = RAISED ).pack(pady=5, side=RIGHT, anchor='nw')

root.mainloop()
