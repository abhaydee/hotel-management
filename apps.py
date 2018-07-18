from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('slide1.jinja2')
    #with sql.connect("sqldb.db") as con:
        #cur = con.cursor()
        #cur.execute("drop table employees")

@app.route('/rooms/')
def rooms():
    return render_template('rooms.jinja2')

@app.route('/rooms/addrooms/' , methods=['GET','POST'])
def addrooms():
    if request.method == 'POST':
        roomno = request.form['roomno']
        type = request.form['type']
        defaultval=10000
        price=defaultval*int(type)
        switcher={
            3:"Presidential Suite",
            2:"Extended Villa",
            1.5:"Executive Suite",
            1:"PentHouse Suite",
            0.5:"Wood Cabin "
        }
        suitename=switcher.get(int(type),0.5)
        if roomno.strip() is "" and type.strip() is "" :
            return render_template('addroom.jinja2', error="Enter all fields properly")
        else:
            try:
                with sql.connect("sqldb.db") as con:
                    cur = con.cursor()
                    cur.execute("create table if not exists rooms (roomno INT , type TEXT , status BOOLEAN , guestno INT DEFAULT NULL,price INT)")
                    cur.execute("INSERT INTO rooms (roomno,type,status,guestno,price) VALUES (?,?,?,?,?)", (roomno,suitename,"Yes","NULL",price))
                    con.commit()
                    msg = "Record saved successfully"
            except:
                con.rollback()
                msg = "Error in inserting record"
            finally:
                con.close()
                return render_template("addroom.jinja2", msg=msg)
    return render_template('addroom.jinja2')

@app.route('/rooms/lstroom/')
def lstrooms():
    with sql.connect("sqldb.db") as con:
        cur = con.cursor()
        cur.execute("select * from rooms")
        roomlist = cur.fetchall()
    return render_template('lstroom.jinja2',roomlist=roomlist)


@app.route('/booking/' , methods = ['GET','POST'])
def booking():
    if request.method == 'POST':
        #bookingno = request.form['bookingno']
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        guestname = request.form['guestname']
        roomno = request.form['roomno']
        phone = request.form['phone']
        address = request.form['address']
        if  roomno.strip() is "" and phone.strip() is "":
            return render_template('addemp.jinja2', error="Enter all fields properly")
        else:
            try:
                with sql.connect("sqldb.db") as con:
                    cur = con.cursor()
                    print("beginning table creation")
                    cur.execute("create table if not exists booking (bookingno INTEGER primary key autoincrement, checkin DATE , checkout DATE)")
                    print("table1 created")
                    cur.execute("create table if not exists guest (guestno INTEGER primary key autoincrement,guestname TEXT, bookingno INT default NULL,phone INT,address TEXT,foreign key(bookingno) references booking(bookingno))")
                    print("tables created")
                    cur.execute("select * from booking")
                    curobject= cur.fetchall()
                    print("select statement")
                    print(str(curobject))
                    print(type(curobject))
                    bookingno = len(curobject)
                    print(bookingno)
                    cur.execute("INSERT INTO booking (checkin,checkout) VALUES (?,?)", (checkin,checkout))
                    print("1st insert finished")
                    cur.execute("INSERT INTO guest (guestname,phone,address) VALUES (?,?,?)", (guestname,phone,address))
                    print("@nd insert finished")
                    cur.execute("UPDATE guest set bookingno = {0} where guestno = {0}".format(bookingno))
                    print("1st update finished")
                    cur.execute("UPDATE rooms set guestno = {0} where roomno = {1}".format(bookingno,roomno))
                    print("2nd update finished")
                    con.commit()
                    msg = "Record saved successfully"
            except:
                con.rollback()
                msg = "Error in inserting record"
            finally:
                con.close()
                return render_template("booking.jinja2", msg=msg)
    return render_template('booking.jinja2')

@app.route('/guests/')
def guests():
    with sql.connect("sqldb.db") as con:
        cur = con.cursor()
        cur.execute("select * from guest")
        guestlist = cur.fetchall()
    return render_template('guests.jinja2',guestlist=guestlist)

@app.route('/employees/')
def employees():
    return render_template('lstemp.jinja2')

@app.route('/employees/addemp/' ,methods =['GET','POST'])
def addemp():
    if request.method == 'POST':
        emp_id = request.form['empid']
        emp_name = request.form['empname']
        emp_age =   request.form['empage']
        emp_des = request.form['empdes']
        emp_phone = request.form['empphone']
        emp_address = request.form['empaddress']
        if emp_id.strip() is "" and emp_name.strip() is "" and emp_phone.strip() is "":
            return render_template('addemp.jinja2', error="Enter all fields properly")
        else:
            try:
                with sql.connect("sqldb.db") as con:
                    cur = con.cursor()
                    cur.execute("create table if not exists employees (emp_id INT , emp_name TEXT , emp_age INT , emp_des TEXT , emp_phone INT ,emp_address TEXT)")
                    cur.execute("INSERT INTO employees (emp_id,emp_name,emp_age,emp_des,emp_phone,emp_address) VALUES (?,?,?,?,?,?)", (emp_id,emp_name, emp_age, emp_des, emp_phone,emp_address))
                    con.commit()
                    msg = "Record saved successfully"
            except:
                con.rollback()
                msg = "Error in inserting record"
            finally:
                con.close()
                return render_template("addemp.jinja2", msg=msg)
    return render_template('addemp.jinja2')

@app.route('/employees/lstemp/')
def lstemp():
    with sql.connect("sqldb.db") as con:
        cur = con.cursor()
        cur.execute("select * from employees")
        emplist = cur.fetchall()
    return render_template('mgemp.jinja2',emplist=emplist)

@app.route('/<string:post_id>')  #eg - /post/2 returns 2 to post_id
def error1(post_id):
    return render_template('404.jinja2',message=f'{post_id} was not found')

@app.route('/<string:post_id>/')  #eg - /post/2 returns 2 to post_id
def error2(post_id):
    return render_template('404.jinja2',message=f'{post_id} was not found')


app.run(debug=True)
