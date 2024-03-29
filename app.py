from flask import Flask
import numpy

app=Flask(__name__)

@app.route('/')
def home():
    
         return "hello billel"
if __name__ =="__main__":
    app.run()

