from PIL import Image
import numpy

grayscale91=[' ','`', '.', '-', "'", ':', '_', ',', '^', '=', ';', '>', '<', '+', '!', 'r', 'c', '*', '/', 'z', '?', 's', 'L', 'T', 'v', ')', 'J', '7', '(', '|', 'F', 'i', '{', 'C', '}', 'f', 'I', '3', '1', 't', 'l', 'u', '[', 'n', 'e', 'o', 'Z', '5', 'Y', 'x', 'j', 'y', 'a', ']', '2', 'E', 'S', 'w', 'q', 'k', 'P', '6', 'h', '9', 'd', '4', 'V', 'p', 'O', 'G', 'b', 'U', 'A', 'K', 'X', 'H', 'm', '8', 'R', 'D', '#', '$', 'B', 'g', '0', 'M', 'N', 'W', 'Q', '%', '&', '@']
grayscaleCharBrightness91=[0.0751, 0.0829, 0.0848, 0.1227, 0.1403, 0.1559, 0.185, 0.2183, 0.2417, 0.2571, 0.2852, 0.2902, 0.2919, 0.3099, 0.3192, 0.3232, 0.3294, 0.3384, 0.3609, 0.3619, 0.3667, 0.3737, 0.3747, 0.3838, 0.3921, 0.396, 0.3984, 0.3993, 0.4075, 0.4091, 0.4101, 0.42, 0.423, 0.4247, 0.4274, 0.4293, 0.4328, 0.4382, 0.4385, 0.442, 0.4473, 0.4477, 0.4503, 0.4562, 0.458, 0.461, 0.4638, 0.4667, 0.4686, 0.4693, 0.4703, 0.4833, 0.4881, 0.4944, 0.4953, 0.4992, 0.5509, 0.5567, 0.5569, 0.5591, 0.5602, 0.5602, 0.565, 0.5776, 0.5777, 0.5818, 0.587, 0.5972, 0.5999, 0.6043, 0.6049, 0.6093, 0.6099, 0.6465, 0.6561, 0.6595, 0.6631, 0.6714, 0.6759, 0.6809, 0.6816, 0.6925, 0.7039, 0.7086, 0.7235, 0.7302, 0.7332, 0.7602, 0.7834, 0.8037]
grayscale10=[' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
grayscaleCharBrightness10=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
braileeDots = [
    (0x01, 0x08),
    (0x02, 0x10),
    (0x04, 0x20),
    (0x40, 0x80)
]

def loadImage(path):
    try:
        return Image.open(path, mode="r", formats=None)
    except:
        return False
    
def resizeImage(image, console, charset):
    imageSize=[]
    consoleSize=[]
    printSize=[0,0]
    imageSize=image.size
    consoleSize=console.size
    aspectRatio=imageSize[0]/imageSize[1]
    printSize[1]=consoleSize[1]-1
    printSize[0]=int(printSize[1]*aspectRatio)
    printSize[0]=2*printSize[0]
    if printSize[0]>=consoleSize[0]:
        printSize[0]=consoleSize[0]-1
        printSize[1]=int(printSize[0]*aspectRatio)
        printSize[1]=int(0.5*printSize[0])
    if charset=="braille":
        printSize[0]=printSize[0]*2
        printSize[1]=printSize[1]*4
    resizedImage=image.resize(printSize)
    return numpy.asarray(resizedImage, dtype="int16")

def imgToAsciiBig(imageArray):
    imageShape=imageArray[:,:,0].shape
    asciiImage=numpy.zeros(imageShape, dtype=str)
    i,j=0,0
    for rows in imageArray:
        for col in rows:
            pixelBrightness=(col[0]+col[1]+col[2])/765
            asciiImage[i][j]=getAsciiCharBig(pixelBrightness)
            j=j+1
        i=i+1
        j=0
    return asciiImage

def imgToAsciiSmall(imageArray):
    imageShape=imageArray[:,:,0].shape
    asciiImage=numpy.zeros(imageShape, dtype=str)
    i,j=0,0
    for rows in imageArray:
        for col in rows:
            pixelBrightness=(col[0]+col[1]+col[2])/765
            asciiImage[i][j]=getAsciiCharSmall(pixelBrightness)
            j=j+1
        i=i+1
        j=0
    return asciiImage

def imgToAsciiBraille(imageArray, threshold=150):
    imageShape=imageArray[:,:,0].shape
    brailleImage=numpy.zeros((imageShape[0]//4, imageShape[1]//2), dtype=str) 
    pixelRGB=numpy.zeros((imageShape[0]//4, imageShape[1]//2, 3), dtype="int16") 
    i,j=0,0
    for y in range(0,imageShape[0],4):
        for x in range(0,imageShape[1],2):
            brailleImage[i][j], pixelRGB[i][j][0], pixelRGB[i][j][1], pixelRGB[i][j][2]=getBrailleChar(x,y,imageArray,threshold)
            j=j+1
        i=i+1
        j=0
    return brailleImage, pixelRGB
            
def getAsciiCharBig(brightness):
    for i in range(len(grayscaleCharBrightness91)-1):
        if brightness>grayscaleCharBrightness91[i] and brightness<grayscaleCharBrightness91[i+1]:
            return grayscale91[i]
    return '@'

def getAsciiCharSmall(brightness):
    for i in range(len(grayscaleCharBrightness10)-1):
        if brightness>grayscaleCharBrightness10[i] and brightness<grayscaleCharBrightness10[i+1]:
            return grayscale10[i]
    return '@'
    
def getBrailleChar(x,y,imageArray, threshold):
    brailleOffset = 0x2800
    pixelRGB=numpy.zeros((4,2,3), dtype="int16")
    for dy in range(4):
        for dx in range(2):
            pixelBrightness=(imageArray[y+dy][x+dx][0]+imageArray[y+dy][x+dx][1]+imageArray[y+dy][x+dx][2])/3
            pixelRGB[dy][dx][0]=imageArray[y+dy][x+dx][0]
            pixelRGB[dy][dx][1]=imageArray[y+dy][x+dx][1]
            pixelRGB[dy][dx][2]=imageArray[y+dy][x+dx][2]
            if pixelBrightness>threshold:
                brailleOffset=brailleOffset+braileeDots[dy][dx]
    averageRed=numpy.mean(pixelRGB[:,:,0])
    averageBlue=numpy.mean(pixelRGB[:,:,1])
    averageGreen=numpy.mean(pixelRGB[:,:,2])
    return chr(brailleOffset), averageRed, averageBlue, averageGreen

def ditherImage(imageArray):
    if numpy.ma.size(imageArray, 2)>3:
        imageArray=imageArray[:,:,:3]
    tempImage=Image.fromarray(imageArray.astype("uint8"), mode="RGB")
    tempImage=tempImage.convert("P",dither=Image.Dither.FLOYDSTEINBERG)
    tempImage=tempImage.convert("RGB")
    imageArray=numpy.asarray(tempImage, dtype="int16")
    return imageArray