#!C:/Python34/python.exe
import cgi, cgitb
import sys
#from iterable import chain
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()

print("Content-type:text/html\r\n\r\n")
if __name__ == '__main__':

    config = {
               'host': '127.0.0.1',
               'port': 3306,
               'database': 'project',
               'user': 'root',
               'password': '',
               'charset': 'utf8',
               'use_unicode': True,
               'get_warnings': True,
               }

def hotels(config):
    db = mysql.connector.Connect(**config)
    cursor = db.cursor()
    cursor.execute(("select * from hotels "))
    res=cursor.fetchall()
    print("""<table align="center" border=1 cellpadding=10><tr><th>Hotel id</th><th>hotel name</th><th>stars</th></tr>""")
    for i in range(0,len(res)):
        print('<tr><td>')
        print(res[i][0])
        print('</td><td>')
        if i==0:
            print('<a href="slide2.py">')
            print(res[i][1])
            print('</a>')
        elif i==1:
            print('<a href="slide3.py">')
            print(res[i][1])
            print('</a>')
        elif i==2:
            print('<a href="slide4.py">')
            print(res[i][1])
            print('</a>')
        elif i==3:
            print('<a href="slide5.py">')
            print(res[i][1])
            print('</a>')
        elif i==4:
            print('<a href="slide6.py">')
            print(res[i][1])
            print('</a>')
        else :
            print(res[i][1])
        print('</td><td>')
        print(res[i][2])
        print('</td></tr>')
    print("</table></div></div>")


def home():
    print("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Hotels</title>
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <link href="style/main.css" rel="stylesheet" type="text/css" media="screen" />
    <link href="style/animate.css" rel="stylesheet" >
    <script src = "js/wow.min.js"></script>
    <script>
        new WOW().init();
    </script>

    </head>
    <body background = "hotel12.jpg">
    <div class ="supreme">
    <form action ="testing.py" method="get">
        <div class ="wow animated fadeInDown" data-wow-delay = "1s" >
            <img src="hotels-6.png" width= 1200 height= 500 border=0 alt="">
        </div>
        <div class = "col-2">
        <div>
         <div>
            <audio controls autoplay ><source src = "End - Credits.mp3" type = "audio/mp3" ></audio>
         </div>
       </form>
       <div class="wow fadeIn animated " data-wow-delay = "6s">
      """)
    hotels(config)
    print ("""
            </body>
            </html>""")

home()
