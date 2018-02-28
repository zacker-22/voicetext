from PIL import Image
import numpy as np
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
def dirty_percentage(file_directory):


	pil_im = Image.open(file_directory)

	pil_imgray = pil_im.convert('LA')

	img = np.array(list(pil_imgray.getdata(band=0)), float)

	img.shape = (pil_imgray.size[1], pil_imgray.size[0])

	i=len(img)/2+10
	total_circle=0
	germs=0
	for i in range(len(img)):
	    for j in range(len(img[0])):
	        if img[i][j]>100:
	            total_circle+=1
	        if img[i][j]>132:
	            germs+=1
	            
	

	#print germs
	#print total_circle
	#print len(img)*len(img[0])
	return str(100.0*(germs/float(total_circle)))
	#plt.imshow(img, cmap="gray")
