from flask import Flask, request
import os
import shutil

app = Flask(__name__)

@app.route("/")
def hello():

    name = request.args.get('name', type = str)

    newpath = r'C:\new_folder' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    src = r'D:\Projects\face-recognition\test_images\{}'
    shutil.copy2(src.format(name), r'C:\new_folder')
    return name


if __name__ == "__main__":
    app.run(debug=True)