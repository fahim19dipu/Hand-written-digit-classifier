# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:12:11 2016

@author: fahim
"""

def main_function(path):
    
    from PIL import Image, ImageFilter
    from matplotlib import pyplot as plt
    """
    #REMOVES SHADOWs AND NOMALIZES THE IMAGE
    """
    def remove_shadow(path):
        import cv2
        import numpy as np
        from matplotlib import pyplot as plt
        
        img = cv2.imread(path, -1)
        
        rgb_planes = cv2.split(img)
        
        result_planes = []
        result_norm_planes = []
        for plane in rgb_planes:
            dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
            bg_img = cv2.medianBlur(dilated_img, 21)
            diff_img = 255 - cv2.absdiff(plane, bg_img)
            #norm_img = cv2.normalize(diff_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)  
            norm_img = cv2.normalize(diff_img, None)
            result_planes.append(diff_img)
            result_norm_planes.append(norm_img)
        
        result = cv2.merge(result_planes)
        result_norm = cv2.merge(result_norm_planes)
        
        cv2.imwrite('shadows_out.png', result)
        ###############################################
        
        img = cv2.imread('shadows_out.png',0)
        img = cv2.medianBlur(img,5)
        
        ret,th1 = cv2.threshold(img,220,255,cv2.THRESH_BINARY)
        #th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\cv2.THRESH_BINARY,11,2)
        #th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\cv2.THRESH_BINARY,11,2)
        #images = [img, th1, th2, th3]
        
        cv2.imwrite('formated.png', th1)
    """
    #CONVERT THE IMAGE IN RESULATION 28x28
    """
    def imageprepare(argv):
        """
        This function returns the pixel values.
        The imput is a png file location.
        """
        im = Image.open(argv).convert('L')
        width = float(im.size[0])
        height = float(im.size[1])
        newImage = Image.new('L', (28, 28), (255))  # creates white canvas of 28x28 pixels
    
        if width > height:  # check which dimension is bigger
            # Width is bigger. Width becomes 20 pixels.
            nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
            if (nheight == 0):  # rare case but minimum is 1 pixel
                nheight = 1
                # resize and sharpen
            img = im.resize((20, nheight), Image.ANTIALIAS)#.filter(ImageFilter.SHARPEN)
            wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
            newImage.paste(img, (4, wtop))  # paste resized image on white canvas
        else:
            # Height is bigger. Heigth becomes 20 pixels.
            nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
            if (nwidth == 0):  # rare case but minimum is 1 pixel
                nwidth = 1
                # resize and sharpen
            img = im.resize((nwidth, 20), Image.ANTIALIAS)#.filter(ImageFilter.SHARPEN)
            wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
            newImage.paste(img, (wleft, 4))  # paste resized image on white canvas
            print(newImage)
            
        newImage.save("sample.jpg")
        
        tv = list(newImage.getdata())  # get pixel values
    
        # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
        tva = [(255 - x) * 1.0 / 255.0 for x in tv]
        #print(tva)
        
        return tva
            
    
        
        #print(tva)
        
        #return tva
    """
    #CROP ANY UNNCESSARY WHITE SPACE
    """
    def crop_image(imageFile):
        
        image = Image.open(imageFile).convert('L')
        print('processing ' + imageFile)
        rgbim = image.convert('RGB')
    
        w, h = rgbim.size
        #print((w,h))
        first_pixel=(256,256)
        last_pixel=(-1, -1)
    
        mpixel=255
        
        for i in range(w):
            for j in range(h):
                px = rgbim.getpixel((i, j))
                mpixel = min(mpixel, px[0])
                if px[0]<90: 
                    first_pixel=(min(first_pixel[0], i), min(first_pixel[1], j))
                    last_pixel=(max(last_pixel[0], i), max(last_pixel[1], j))
    
        threshold=mpixel+80
        #print(threshold)          
        #print(first_pixel)
        #print(last_pixel)
        nw = last_pixel[0]-first_pixel[0]
        nh = last_pixel[1]-first_pixel[1]
        nrgbim = Image.new('RGB', (nw,nh))
        
        for i in range(nw):
            for j in range(nh):
                if rgbim.getpixel((i+first_pixel[0], j+first_pixel[1]))[0]<threshold:
                    nrgbim.putpixel((i, j), (0, 0, 0))            
                else:
                    nrgbim.putpixel((i, j), (255, 255, 255))
                #nrgbim.putpixel((i,j), rgbim.getpixel((i+first_pixel[0], j+first_pixel[1])))
        
        
        nrgbim.save('cropped_processed_image.png')	
        image.close()
        rgbim.close()    
        nrgbim.close()
    """  
    #REGULAR MEDIAN FILTER [UNSED]
    
    def median_filter(data, filter_size):
        temp = []
        indexer = filter_size // 2
        data_final = []
        data_final = numpy.zeros((len(data),len(data[0])))
        for i in range(len(data)):
    
            for j in range(len(data[0])):
    
                for z in range(filter_size):
                    if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(data[i + z - indexer][j + k - indexer])
    
                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []
        return data_final
        
    def create_array(filename):
        crop_image(filename)
    #medfilter(path)
        x=[imageprepare('./cropped_processed_image.png')]
        newArr=[[0 for d in range(28)] for y in range(28)]
        k = 0
        for i in range(28):
            for j in range(28):
                newArr[i][j]=x[0][k]
                k=k+1
        return newArr
    """
      
    ###########################################################
    #from keras.models import Sequential
    #from keras.layers import Dense
    #from keras.models import model_from_json
    import numpy
    #import os
    from tensorflow import keras
    #from tensorflow.keras import layers
    #from keras.models import load_model
    """LOADING THE TRAINNED MODEL AS new_model"""
    #new_model = keras.models.load_model('path_to_my_model.h5')
    new_model = keras.models.load_model('myCNN.h5')
    new_model.summary()
    
    
    import numpy 
    
    
    """
    img = Image.open('shadows_out.png').convert("L")
   
    arr = numpy.array(img)
    removed_noise = median_filter(arr, 1) 
    img = Image.fromarray(removed_noise)
    #img.show()
    img = img.convert("L")
    img.save("noiseless_image.png")
    """
  #  crop_image(path)    
    
    remove_shadow(path)
    #from matplotlib import pyplot as plt
    #plt.imshow("formated.png",cmap='gray')
        
    crop_image( 'formated.png')
    #from matplotlib import pyplot as plt
    #plt.imshow("cropped_processed_image.png",cmap='gray')
        
    
   
    
    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    x = [imageprepare('cropped_processed_image.png')]
    newArr=[[0 for d in range(28)] for y in range(28)]
    k = 0
    for i in range(28):
        for j in range(28):
            newArr[i][j]=x[0][k]
            k=k+1
     
    #from matplotlib import pyplot as plt
    #plt.imshow(newArr,cmap='binary')
    
    import numpy as np
    newArr= np.asarray(newArr)
    from numpy import newaxis
    newArr = newArr[...,newaxis]
    newArr.shape
    newArr = newArr.reshape((1,newArr.shape[0], newArr.shape[1], 1))
    newArr.shape
    
    predictions = new_model.predict(newArr)
    print(predictions)
    print(np.argmax(predictions))
    return np.argmax(predictions)