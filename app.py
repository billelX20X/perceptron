from flask import Flask
import cv2
import numpy as np

app=Flask(__name__)


img=np.array(cv2.imread("im1.jpg",0))

@app.route('/')
def home():
       
         return "hello world"+str(img[1])
if __name__ =="__main__":
    app.run()

