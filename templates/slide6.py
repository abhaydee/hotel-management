#!C:/Python34/python.exe
import cgi, cgitb
import sys
#from iterable import chain
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()
hotel= "tipton"
qrytable = form.getvalue('choice')

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
    if qrytable == "list" :
        cursor.execute(("select * from hotels where hotelname = '%s'" ) % hotel)
        res=cursor.fetchall()
        print("""<table align="center" border=1 cellpadding=10><tr><th>Hotel id</th><th>Hotel Name </th><th>Stars</th></tr>""")

        for i in range(0,len(res)):
            print('<tr><td>')
            print(res[i][0])
            print('</td><td>')
            print(res[i][1])
            print('</td><td>')
            print(res[i][2])
            print('</td></tr>')
        print("</table>")

    elif qrytable == "restaurant" :
        cursor.execute(("select hotelname,rid,type,ratings from hotels h,restaurant r where hotelname = '%s' and h.hotelid = r.hotelid ") % hotel )
        res=cursor.fetchall()
        print("""<table align="center" border=1 cellpadding=10><tr><th>Hotel Name</th><th>Rid </th><th>Type</th><th>Rating</th></tr>""")

        for i in range(0,len(res)):
            print('<tr><td>')
            print(res[i][0])
            print('</td><td>')
            print(res[i][1])
            print('</td><td>')
            print(res[i][2])
            print('</td><td>')
            print(res[i][3])
            print('</td></tr>')
        print("</table>")

    elif qrytable == "rooms" :
        cursor.execute(("select hotelname,roomid,type,cost,ac,status,beds from hotels h,rooms r where hotelname = '%s' and h.hotelid = r.hotelid ") % hotel )
        res=cursor.fetchall()
        print("""<table  align="center" border=1 cellpadding=10><tr><th>Hotel Name</th><th>Roomid </th><th>Type</th><th>Cost</th><th>A/C</th><th>Available</th><th>No of Beds</th></tr>""")

        for i in range(0,len(res)):
            print('<tr><td>')
            print(res[i][0])
            print('</td><td>')
            print(res[i][1])
            print('</td><td>')
            print(res[i][2])
            print('</td><td>')
            print(res[i][3])
            print('</td><td>')
            print(res[i][4])
            print('</td><td>')
            print(res[i][5])
            print('</td><td>')
            print(res[i][6])
            print('</td></tr>')
        print("</table>")

    elif qrytable == "facilities" :
        cursor.execute(("select hotelname,name from hotels h,facilities r where hotelname = '%s' and h.hotelid = r.hotelid ") % hotel )
        res=cursor.fetchall()
        print("""<table align="center" border=1 cellpadding=10><tr><th>Hotel name</th><th>facility name </th></tr>""")
        flag =1
        for i in range(0,len(res)):
            print('<tr><td>')
            print(res[i][0])
            print('</td><td>')
            print(res[i][1])
            print('</td></tr>')
        print("</table>")

    elif qrytable == "location" :
        cursor.execute(("select hotelname,pin,street,city from hotels h,location r where hotelname = '%s' and h.hotelid = r.hotelid ") % hotel )
        res=cursor.fetchall()
        print("""<table align="center" border=1 cellpadding=10><tr><th>Hotel name</th><th>pin</th><th>street</th><th>city</th></tr>""")

        for i in range(0,len(res)):
            print('<tr><td>')
            print(res[i][0])
            print('</td><td>')
            print(res[i][1])
            print('</td><td>')
            print(res[i][2])
            print('</td><td>')
            print(res[i][3])
            print('</td></tr>')
        print("</table>")




def home():
    print("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Tipton</title>
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <link href="style/main.css" rel="stylesheet" type="text/css" media="screen" />
    <link href="style/animate.css" rel="stylesheet" >
    </head>
    <body background="hotel12.jpg">

        <div class ="supreme">
          <div class ="animated slideInDown">
            <img src="tipton.png" width="600" height= 399 border=0 alt="">
        </div>
        <div class = "animated fadeIn">
            <h1 name ="heading" class="hd" id="tre"> Tipton </h1>
            <a href = "slide1.py" style="float:left"><button><-- Back</button></a>
        </div>
        <form action ="slide6.py" method="get">
        <div class ="col-3">
          Options : <input type = "radio" name ="choice" value ="list"/>Star ratings
          <input type = "radio" name ="choice" value="restaurant"/>Restaurant
          <input type = "radio" name ="choice" value = "rooms"/>Rooms
          <input type = "radio" name ="choice" value="facilities"/>Facilities
          <input type = "radio" name ="choice" value = "location"/>Location
        </div>

        <div class ="col-4">
            <input type ="submit" value ="QUERY"/>
        </div>
        </div>
        </form>""")
    hotels(config)
    print ("""</body>
            </html>""")

home()
