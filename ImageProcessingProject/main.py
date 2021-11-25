from tkinter import *
from tkinter import filedialog,simpledialog,messagebox
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk
import os
import numpy as np
from skimage import io,color,filters,exposure
from skimage.util import img_as_ubyte
from skimage.transform import rotate,resize,swirl,rescale
from skimage.morphology import area_closing,area_opening,diameter_closing,diameter_opening,dilation,erosion,opening,closing,black_tophat,white_tophat
import matplotlib.pyplot as plt
image_type=None
img3 = img5 = img7 = img9 = img11 = img13 = img15 = img17 = img19 = img21 = img23 = img25 = img27 = img29 = img31 = img33 = img35 = img37 = img39 = img41 = img43 = img45 = img47 \
    = img49 = img51 = img53 = None
#if image_type == 3:
#    img_array = color.rgb2gray(img_asarray)
#else:
#    img_array = img_asarray
def load_image():
    global img_path,img_asarray,image_type, img, img1
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img_asarray = io.imread(img_path)
    image_type=len(img_asarray.shape)
    img = Image.fromarray(img_asarray)
    width, height = img.size
    img.thumbnail((width, height))
    canvas.delete("all")
    img1 = ImageTk.PhotoImage(img)
    canvas.create_image(300, 210, image=img1)
    canvas.image = img1

##Kümülatif toplam döndürmesi eklenecek
def rotate_image():
    global img2,img3
    rotate_angle=simpledialog.askfloat("Input", "Rotate Angle?")
    rotated_image= rotate(img_asarray,rotate_angle*-1)
    rotated_image = (rotated_image * 255).astype(np.uint8)
    img2 = Image.fromarray(rotated_image.astype('uint8'))
    width, height = img2.size
    img2.thumbnail((width, height))
    img3 = ImageTk.PhotoImage(img2)
    canvas.delete("all")
    canvas.create_image(300, 210, image=img3)
    canvas.image = img3

def resize_image():
    global img4, img5
    width, height = img.size
    img.thumbnail((width, height))
    new_width = simpledialog.askinteger("Input", "New Width?")
    new_height = int(new_width * height / width)
    resized_image = resize(img_asarray, (new_width,new_height),anti_aliasing=True)
    resized_image = (resized_image * 255).astype(np.uint8)
    img4 = Image.fromarray(resized_image.astype('uint8'))
    img5 = ImageTk.PhotoImage(img4)
    canvas.delete("all")
    canvas.create_image(300, 210, image=img5)
    canvas.image = img5

def crop_image():
    global img6, img7
    width, height = img.size
    img.thumbnail((width, height))
    x1 = simpledialog.askinteger("Input", "First X Coordinate?",minvalue=0,maxvalue=img.width-1)
    x2 = simpledialog.askinteger("Input", "Second X Coordinate?",minvalue=x1,maxvalue=img.width)
    y1 = simpledialog.askinteger("Input", "First Y Coordinate?",minvalue=0,maxvalue=img.height-1)
    y2 = simpledialog.askinteger("Input", "Second Y Coordinate?",minvalue=y1,maxvalue=img.height)
    img6 = img_asarray[x1:x2, y1:y2]
    img6 = Image.fromarray(img6)
    canvas.delete("all")
    img7 = ImageTk.PhotoImage(img6)
    canvas.create_image(300, 210, image=img7)
    canvas.image = img7

def swirl_image():#sabit sayilar degistirilebilir
    global img8, img9
    width, height = img.size
    img.thumbnail((width, height))
    swirled_image = swirl(img_asarray, rotation=0, strength=20, radius=180)
    swirled_image = (swirled_image * 255).astype(np.uint8)
    img8 = Image.fromarray(np.uint8(swirled_image))
    canvas.delete("all")
    img9 = ImageTk.PhotoImage(img8)
    canvas.create_image(300, 210, image=img9)
    canvas.image = img9

def rescale_image():
    global img10, img11
    width, height = img.size
    img.thumbnail((width, height))
    scale_rate = simpledialog.askfloat("Input", "Scale Rate")
    rescaled_image = rescale(img_asarray,scale_rate,anti_aliasing=True)
    rescaled_image = (rescaled_image * 255).astype(np.uint8)
    img10 = Image.fromarray(np.uint8(rescaled_image))
    canvas.delete("all")
    img11 = ImageTk.PhotoImage(img10)
    canvas.create_image(300, 210, image=img11)
    canvas.image = img11

def hysteresis_thresholding():
    global img12, img13
    edges = filters.sobel(img_asarray)
    low = 0.1
    high = 0.4
    lowt = (edges > low).astype(int)
    hight = (edges > high).astype(int)
    filtered_image = filters.apply_hysteresis_threshold(edges, low, high)
    filtered_image = (filtered_image * 255).astype(np.uint8)
    img12 = Image.fromarray(np.uint8(filtered_image))
    canvas.delete("all")
    img13 = ImageTk.PhotoImage(img12)
    canvas.create_image(300, 210, image=img13)
    canvas.image = img13

def sobel_image():
    global img14, img15
    sobel_img=filters.sobel(img_asarray, mask=None, axis=1, mode='reflect', cval=5.0)
    sobel_img = (sobel_img * 255).astype(np.uint8)
    img14 = Image.fromarray(np.uint8(sobel_img))
    canvas.delete("all")
    img15 = ImageTk.PhotoImage(img14)
    canvas.create_image(300, 210, image=img15)
    canvas.image = img15

def hessian_image():
    global img16, img17
    hessian_img=filters.hessian(img_asarray)
    hessian_img = (hessian_img * 255).astype(np.uint8)
    img16 = Image.fromarray(np.uint8(hessian_img))
    canvas.delete("all")
    img17 = ImageTk.PhotoImage(img16)
    canvas.create_image(300, 210, image=img17)
    canvas.image = img17

def laplace_image():
    global img18, img19
    laplace_img=filters.laplace(img_asarray,ksize=3, mask=None)
    laplace_img = (laplace_img * 255).astype(np.uint8)
    img18 = Image.fromarray(np.uint8(laplace_img))
    canvas.delete("all")
    img19 = ImageTk.PhotoImage(img18)
    canvas.create_image(300, 210, image=img19)
    canvas.image = img19

def median_image():
    global img20, img21
    median_img=filters.median(img_asarray)
    median_img = (median_img * 255).astype(np.uint8)
    img20 = Image.fromarray(np.uint8(median_img))
    canvas.delete("all")
    img21 = ImageTk.PhotoImage(img20)
    canvas.create_image(300, 210, image=img21)
    canvas.image = img21

def meijering_image():
    global img22, img23
    meijering_img=filters.meijering(img_asarray,sigmas=range(1, 10, 2), alpha=None, black_ridges=True, mode='reflect', cval=0)
    meijering_img = (meijering_img * 255).astype(np.uint8)
    img22 = Image.fromarray(np.uint8(meijering_img))
    canvas.delete("all")
    img23 = ImageTk.PhotoImage(img22)
    canvas.create_image(300, 210, image=img23)
    canvas.image = img23

def sato_image():
    global img24, img25
    sato_img=filters.sato(img_asarray,sigmas=range(1, 10, 2), black_ridges=True, mode=None, cval=0)
    sato_img = (sato_img * 255).astype(np.uint8)
    img24 = Image.fromarray(np.uint8(sato_img))
    canvas.delete("all")
    img25 = ImageTk.PhotoImage(img24)
    canvas.create_image(300, 210, image=img25)
    canvas.image = img25

def scharr_image():
    global img26, img27
    scharr_img=filters.scharr(img_asarray,mask=None, axis=None, mode='reflect', cval=1.0)
    scharr_img = (scharr_img * 255).astype(np.uint8)
    img26 = Image.fromarray(np.uint8(scharr_img))
    canvas.delete("all")
    img27 = ImageTk.PhotoImage(img26)
    canvas.create_image(300, 210, image=img27)
    canvas.image = img27

def difference_of_gaussians_image():
    global img28, img29
    doga_img=filters.difference_of_gaussians(img_asarray, low_sigma=2, high_sigma=10, mode='nearest', cval=0, multichannel=False, truncate=4.0)
    doga_img = (doga_img * 255).astype(np.uint8)
    img28 = Image.fromarray(np.uint8(doga_img))
    canvas.delete("all")
    img29 = ImageTk.PhotoImage(img28)
    canvas.create_image(300, 210, image=img29)
    canvas.image = img29

def faridv_image():
    global img30, img31
    faridv_img=filters.farid_v(img_asarray,mask=None)
    faridv_img = (faridv_img * 255).astype(np.uint8)
    img30 = Image.fromarray(np.uint8(faridv_img))
    canvas.delete("all")
    img31 = ImageTk.PhotoImage(img30)
    canvas.create_image(300, 210, image=img31)
    canvas.image = img31

def rescale_intensity_img():
    global img32, img33
    low=simpledialog.askfloat("Input", "Low Pixel Input")  # Pixels with intensity smaller than this will be black
    high=simpledialog.askfloat("Input", "High Pixel Input")
    img_rescaled = exposure.rescale_intensity(img_asarray, in_range=(low, high))
    img32 = Image.fromarray(img_rescaled)
    canvas.delete("all")
    img33 = ImageTk.PhotoImage(img32)
    canvas.create_image(300, 210, image=img33)
    canvas.image = img33

def show_histogram():
    hist,histogram_of_img=exposure.histogram(img_as_ubyte(img_asarray), nbins=2)
    fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
    ax[0].imshow(img_asarray, cmap=plt.cm.gray)
    ax[0].axis('off')
    ax[1].plot(histogram_of_img,hist, lw=2)
    ax[1].set_title('Gray-level histogram')
    plt.show()

def equalize_histogram():
    global img34, img35
    equalized = exposure.equalize_hist(img_asarray, nbins=2)
    equalized = (equalized * 255).astype(np.uint8)
    img34 = Image.fromarray(equalized)
    canvas.delete("all")
    img35 = ImageTk.PhotoImage(img34)
    canvas.create_image(300, 210, image=img35)
    canvas.image = img35

def area_close():
    global img36, img37
    area_closed = area_closing(img_asarray, area_threshold=64, connectivity=1, parent=None, tree_traverser=None)
    area_closed = (area_closed * 255).astype(np.uint8)
    img36 = Image.fromarray(area_closed)
    canvas.delete("all")
    img37 = ImageTk.PhotoImage(img36)
    canvas.create_image(300, 210, image=img37)
    canvas.image = img37

def area_open():
    global img38, img39
    area_opened = area_opening(img_asarray, area_threshold=64, connectivity=1, parent=None, tree_traverser=None)
    area_opened = (area_opened * 255).astype(np.uint8)
    img38 = Image.fromarray(area_opened)
    canvas.delete("all")
    img39 = ImageTk.PhotoImage(img38)
    canvas.create_image(300, 210, image=img39)
    canvas.image = img39

def diameter_close():
    global img40, img41
    diameter_closed = diameter_closing(img_asarray, diameter_threshold=2, connectivity=1, parent=None, tree_traverser=None)
    diameter_closed = (diameter_closed * 255).astype(np.uint8)
    img40 = Image.fromarray(diameter_closed)
    canvas.delete("all")
    img41 = ImageTk.PhotoImage(img40)
    canvas.create_image(300, 210, image=img41)
    canvas.image = img41

def diameter_open():
    global img42, img43
    diameter_opened = diameter_opening(img_asarray, diameter_threshold=16, connectivity=1, parent=None, tree_traverser=None)
    diameter_opened = (diameter_opened * 255).astype(np.uint8)
    img42 = Image.fromarray(diameter_opened)
    canvas.delete("all")
    img43 = ImageTk.PhotoImage(img42)
    canvas.create_image(300, 210, image=img43)
    canvas.image = img43

def dilation_image():
    global img44, img45
    dilationed = dilation(img_asarray, selem=None, out=None, shift_x=False, shift_y=False)
    dilationed = (dilationed * 255).astype(np.uint8)
    img44 = Image.fromarray(dilationed)
    canvas.delete("all")
    img45 = ImageTk.PhotoImage(img44)
    canvas.create_image(300, 210, image=img45)
    canvas.image = img45

def erosion_image():
    global img46, img47
    erosioned = erosion(img_asarray, selem=None, out=None, shift_x=False, shift_y=False)
    erosioned = (erosioned * 255).astype(np.uint8)
    img46 = Image.fromarray(erosioned)
    canvas.delete("all")
    img47 = ImageTk.PhotoImage(img46)
    canvas.create_image(300, 210, image=img47)
    canvas.image = img47

def opened_image():
    global img48, img49
    opened = opening(img_asarray, selem=None, out=None)
    opened = (opened * 255).astype(np.uint8)
    img48 = Image.fromarray(opened)
    canvas.delete("all")
    img49 = ImageTk.PhotoImage(img48)
    canvas.create_image(300, 210, image=img49)
    canvas.image = img49

def closed_image():
    global img50, img51
    closed = closing(img_asarray, selem=None, out=None)
    closed = (closed * 255).astype(np.uint8)
    img50 = Image.fromarray(closed)
    canvas.delete("all")
    img51 = ImageTk.PhotoImage(img50)
    canvas.create_image(300, 210, image=img51)
    canvas.image = img51

def get_blacktophat():
    global img50, img51
    hatted = black_tophat(img_asarray, selem=None, out=None)
    hatted = (hatted * 255).astype(np.uint8)
    img50 = Image.fromarray(hatted)
    canvas.delete("all")
    img51 = ImageTk.PhotoImage(img50)
    canvas.create_image(300, 210, image=img51)
    canvas.image = img51

def get_whitetophat():
    global img52, img53
    white_hatted = white_tophat(img_asarray, selem=None, out=None)
    white_hatted = (white_hatted * 255).astype(np.uint8)
    img52 = Image.fromarray(white_hatted)
    canvas.delete("all")
    img53 = ImageTk.PhotoImage(img52)
    canvas.create_image(300, 210, image=img53)
    canvas.image = img53

def save_image():
    ext = img_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG File","*.png"),("JPG File","*.jpg")])
    if file:
        if canvas.image==img1:
            img.save(file)
        elif canvas.image==img3:
            img2.save(file)
        elif canvas.image==img5:
            img4.save(file)
        elif canvas.image==img7:
            img6.save(file)
        elif canvas.image==img9:
            img8.save(file)
        elif canvas.image==img11:
            img10.save(file)
        elif canvas.image==img13:
            img12.save(file)
        elif canvas.image==img15:
            img14.save(file)
        elif canvas.image==img17:
            img16.save(file)
        elif canvas.image==img19:
            img18.save(file)
        elif canvas.image==img21:
            img20.save(file)
        elif canvas.image==img23:
            img22.save(file)
        elif canvas.image==img25:
            img24.save(file)
        elif canvas.image==img27:
            img26.save(file)
        elif canvas.image==img29:
            img28.save(file)
        elif canvas.image==img31:
            img30.save(file)
        elif canvas.image==img33:
            img32.save(file)
        elif canvas.image==img35:
            img34.save(file)
        elif canvas.image==img37:
            img36.save(file)
        elif canvas.image==img39:
            img38.save(file)
        elif canvas.image==img41:
            img40.save(file)
        elif canvas.image==img43:
            img42.save(file)
        elif canvas.image==img45:
            img44.save(file)
        elif canvas.image==img47:
            img46.save(file)
        elif canvas.image==img49:
            img48.save(file)
        elif canvas.image==img51:
            img50.save(file)
        elif canvas.image==img53:
            img52.save(file)

gui = Tk()
gui.title("Alperen's PhotoEditor")
gui.geometry("1280x720")
menu = Menu(gui)
gui.config(menu=menu)
filemenu = Menu(menu,tearoff=False)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Load',command=load_image)
filemenu.add_command(label='Save',command=save_image)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=gui.quit)

editmenu = Menu(menu,tearoff=False)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Crop',command=crop_image)
editmenu.add_command(label='Rescale',command=rescale_image)
editmenu.add_command(label='Resize',command=resize_image)
editmenu.add_command(label='Rotate',command=rotate_image)
editmenu.add_command(label='Swirl',command=swirl_image)

enhancementmenu = Menu(menu,tearoff=False)
menu.add_cascade(label='Enhancement', menu=enhancementmenu)
enhancementmenu.add_command(label='Doga',command=difference_of_gaussians_image)
enhancementmenu.add_command(label='FaridV',command=faridv_image)
enhancementmenu.add_command(label='Hessian',command=hessian_image)
enhancementmenu.add_command(label='Hysteresis Thresholding',command=hysteresis_thresholding)
enhancementmenu.add_command(label='Laplace',command=laplace_image)
enhancementmenu.add_command(label='Median',command=median_image)
enhancementmenu.add_command(label='Meijering',command=meijering_image)
enhancementmenu.add_command(label='Sato',command=sato_image)
enhancementmenu.add_command(label='Scharr',command=scharr_image)
enhancementmenu.add_command(label='Sobel',command=sobel_image)

menu.add_command(label='RI',command=rescale_intensity_img)

histogram_menu=Menu(menu,tearoff=False)
menu.add_cascade(label='Histograms', menu=histogram_menu)
histogram_menu.add_command(label='Histogram',command=show_histogram)
histogram_menu.add_command(label='Histogram Equalization',command=equalize_histogram)

morphological_menu=Menu(menu,tearoff=False)
menu.add_cascade(label='Morphology', menu=morphological_menu)
morphological_menu.add_command(label='Area Closing', command=area_close)
morphological_menu.add_command(label='Area Opening', command=area_open)
morphological_menu.add_command(label='Diameter Closing', command=diameter_close)
morphological_menu.add_command(label='Diameter Opening', command=diameter_open)
morphological_menu.add_command(label='Dilation', command=dilation_image)
morphological_menu.add_command(label='Erosion', command=erosion_image)
morphological_menu.add_command(label='Opening', command=opened_image)
morphological_menu.add_command(label='Closing', command=closed_image)
morphological_menu.add_command(label='Black TopHat', command=get_blacktophat)
morphological_menu.add_command(label='White TopHat', command=get_whitetophat)




canvas = Canvas(gui, width="1280", height="720", relief=RIDGE, bd=2)
canvas.place(x=0,y=0)


gui.mainloop()