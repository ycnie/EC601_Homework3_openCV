import numpy as np
import cv2

source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
#print(source_img)
temp = cv2.imread('template_img.jpg',0) # read image in grayscale
#print(temp)

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0;
    var_t = 0;
    location = [0, 0];
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------ 
    mean_t = np.mean(temp)
    var_t = np.var(temp) 
    max_corr = 0;
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0;
            var_s = 0;
            corr = 0;
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------ 
            mean_s = np.mean(src[i:i+temp.shape[0], j:j+temp.shape[1]])
            var_s = np.var(src[i:i+temp.shape[0], j:j+temp.shape[1]])
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            #print("mean_s:", mean_s, "mean_t:", mean_t)
            #print("var_s: ", var_s, "var_t: ", var_t)
            #print("i, j ", i, j)
            #print("temp.shape:", temp.shape,"src.shape: ", src.shape)
            for k in np.arange(i, i + temp.shape[0]):
                #print("k: ", k)
                #print("temp.shape[0]", temp.shape[0])
                for v in np.arange(j, j + temp.shape[1]):
                    #print("v: ", v)
                    #print("src:",v,k,src[k,v])
                    #print("i:", i, "j: ", j)
                    #print("temp",k-i,v-j,temp[k-i,v-j])
                    corr += (src[k,v] - mean_s) * (temp[k-i,v-j] - mean_t)
            corr /= (var_s * var_t * temp.shape[0] * temp.shape[1])
            print(corr)
            if corr > max_corr:
                max_corr = corr;
                location = [i, j];
                print(location)
    return location

# load source and template images
#source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
#temp = cv2.imread('template.jpg',0) # read image in grayscale
location = TemplateMatching(source_img, temp, 15);
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------ 
cv2.rectangle(match_img, (location[1],location[0]), (location[1]+temp.shape[1], location[0]+temp.shape[0]), (0,0,255), 2)
# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------ 
cv2.imwrite('match_img.png', match_img)

# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()