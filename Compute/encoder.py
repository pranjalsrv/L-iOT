import cv2

image_bw = []

def encoder(file_path):
    global image_bw
    im_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    (thresh, image_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = 127
    image_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
    print(image_bw.tolist())
    #file1 = open("myfile.txt","w")
    print(' '.join(image_bw.tolist()))


def decoder(image_arr):
    cv2.imshow('windowname', image_arr)

encoder('input_image.jpg')
#print(image_bw)d
decoder(image_bw)



