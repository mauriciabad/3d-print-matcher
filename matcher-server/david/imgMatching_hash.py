from PIL import Image, ImageFilter
import imagehash
import os
import matplotlib.pyplot as plt

def find_similar_images(currImage, DBpath, hashfunc = imagehash.average_hash):
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or f.endswith(".svg")
    
    if(is_image(currImage)):
        image_filenames = []
        for userpath in DBpath:
            image_filenames += [os.path.join(userpath, path) for path in os.listdir(userpath) if is_image(path)]
        
        results = {}


        img1=Image.open(currImage)
        for y in image_filenames:
            img2=Image.open(y)

            #Make both images same size
            if img1.width<img2.width:
                img2=img2.resize((img1.width,img1.height))
            else:
                img1=img1.resize((img2.width,img2.height))


            img1=img1.filter(ImageFilter.BoxBlur(radius=3))
            img2=img2.filter(ImageFilter.BoxBlur(radius=3))

            #print(y,"phash",imagehash.phash(img1)-imagehash.phash(img2))
            #print(y,"ahash",imagehash.average_hash(img1)-imagehash.average_hash(img2))
            #print(y,"dhash",imagehash.dhash(img1)-imagehash.dhash(img2))
            #print(y,"whash",imagehash.whash(img1)-imagehash.whash(img2))            
            #print(y,"colorhash",imagehash.colorhash(img1)-imagehash.colorhash(img2))

            phashvalue=imagehash.phash(img1)-imagehash.phash(img2)
            ahashvalue=imagehash.average_hash(img1)-imagehash.average_hash(img2)
            totalaccuracy=phashvalue+ahashvalue

            results[y] = totalaccuracy

        return sorted([(k,results[k]) for k in results], key = lambda x: x[1])


foto = "foto_botella.jpg"
print(find_similar_images(foto,["."]))