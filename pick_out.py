import os

#get all files in current directory
files = os.listdir('.')

#initialize lists
images =[]
texts = []

#extract files 
for f in files:
    if f.endswith('.jpg'):
        images.append(f)
    else:
        texts.append(f)

#remove specific files in list
texts.remove('classes.txt')
texts.remove('pick_out.py')

#if there is no equivalent text file, delete the image file.
for i in range(0, len(images)): #loop for images list
    text_file = images[i][0:13]+'.txt' #declare equivalent text file for image
    if_exists = os.path.isfile(text_file)#if it's not exist text file
    if not if_exists:
        os.remove(images[i]) #remove that image file
        
