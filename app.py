#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request, render_template
from werkzeug.utils import secure_filename
import speech_recognition as sr


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        print(file)
        filename = secure_filename(file.filename)
        file.save("static/" + filename)
        a = sr.AudioFile("static/" + filename)
        with a as source:
            a = sr.Recognizer().record(source)
        res = sr.Recognizer().recognize_google(a)
        return render_template("index.html", result=res)
    else:
        return render_template("index.html", result="2")


# In[4]:


if __name__ == "__main__":
    app.run()


# In[ ]:




