from flask import Flask
import numpy
import cv2

app=Flask(__name__)

@app.route('/')
def home():
    
         return "hello billel"
if __name__ =="__main__":
    app.run()

