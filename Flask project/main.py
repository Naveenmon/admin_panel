from flask import *
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="codyb"
app.config['MYSQL_CURSORCLASS']="DictCursor"
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login')
def logout():
    return  render_template('login.html')
@app.route('/au')
def adduser1():
    return  render_template('adduser.html')
@app.route('/ab')
def addbooks1():
    return  render_template('addbooks.html')
@app.route('/at')
def addtransaction1():
    return  render_template('addtransaction.html')
@app.route('/ai')
def addissues1():
    return  render_template('addissues.html')
@app.route('/ei')
def editissues1():
    return  render_template('editissues.html')
#edit user
@app.route('/ei/<string:id>',methods=['GET','POST'])
def editissue(id):
    con = mysql.connection.cursor()
    con.execute("select * from issues where Issue_Id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('editissues.html',id=r)
#edit user
@app.route('/eu/<string:id>',methods=['GET','POST'])
def edituser(id):
    con = mysql.connection.cursor()
    con.execute("select * from users where User_id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('edituser.html',id=r)
@app.route('/eb/<string:id>',methods=['GET','POST'])
def editbooks(id):
    con = mysql.connection.cursor()
    con.execute("select * from books where Book_id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('editbooks.html',id=r)
@app.route('/et/<string:id>',methods=['GET','POST'])
def edittransaction(id):
    con = mysql.connection.cursor()
    con.execute("select * from transaction where Transaction_Id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('edittransaction.html',id=r)

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/dash')
def dash():
    con = mysql.connection.cursor()
    con.execute("select * from users;")
    r = len(con.fetchall())
    con.execute("select * from books;")
    v = len(con.fetchall())
    con.execute("select * from transaction")
    w = len(con.fetchall())
    con.close()
    return render_template('dash.html',data=r,data1=v,data2=w)
@app.route('/user')
def user():
    con=mysql.connection.cursor()
    con.execute("select * from users;")
    r=con.fetchall()
    con.close()
    return render_template('Users.html',data=r)
@app.route('/book')
def book():
    con = mysql.connection.cursor()
    con.execute("select * from books;")
    r = con.fetchall()
    con.close()
    return render_template('book.html',data=r)
@app.route('/transaction')
def trans():
    con = mysql.connection.cursor()
    con.execute("select * from Transaction;")
    r = con.fetchall()
    con.close()
    return render_template('transaction.html',data=r)
@app.route('/issuebook')
def issue():
    con = mysql.connection.cursor()
    con.execute("select * from issues;")
    r = con.fetchall()
    con.close()
    return render_template('issued.html',data=r)
@app.route('/deletetrans/<string:id>',methods=['GET','POST'])
def deletetrans(id):
    con=mysql.connection.cursor()
    con.execute("delete from Transaction where Transaction_Id=%s",id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for('trans'))
@app.route('/deletebooks/<string:id>',methods=['GET','POST'])
def deletebooks(id):
    con=mysql.connection.cursor()
    con.execute("delete from Books where Book_id=%s",id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for('book'))
@app.route('/deleteissue/<string:id>',methods=['GET','POST'])
def deleteissue(id):
    con=mysql.connection.cursor()
    con.execute("delete from Issues where Issue_Id=%s",id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for('issuebook'))
@app.route('/deleteuser/<string:id>',methods=['GET','POST'])
def deleteuser(id):
    con=mysql.connection.cursor()
    con.execute("delete from Users where User_Id=%s",id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for('user'))
#LOGIN PROCESS
@app.route('/ulogin',methods=['GET','POST'])
def ulogin():
    if request.method=="POST":
        uname=request.form['uname']
        pas=request.form['upass']
        con = mysql.connection.cursor()
        con.execute("select * from users where User_Name=%s and Password=%s;",[uname,pas])
        r = len(con.fetchall())
        con.close()
        if r==1:
            return redirect(url_for('dash'))
        else:
            flash("Invalid usname or password")
            return redirect(url_for('home'))
@app.route('/adduser',methods=['GET','POST'])
def adduser():
    if request.method=="POST":
        id = request.form['uid']
        name = request.form['uname']
        email=request.form['uemail']
        pas=request.form['password']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO users(User_id,User_Name,User_Email,Password) values (%s,%s,%s,%s);",(id,name,email,pas))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('user'))
@app.route('/addissues',methods=['GET','POST'])
def addissues():
    if request.method=="POST":
        id = request.form['uid']
        ename = request.form['uname']
        bookname=request.form['book']
        issuedate=request.form['idate']
        expdate=request.form['edate']
        retdate=request.form['rdate']
        con = mysql.connection.cursor()
        con.execute("insert into issues (Issue_Id,User_Name,Book_Name,Issue_Date,Exp_Return_Date,Return_Date) values (%s,%s,%s,%s,%s,%s);",(id,ename,bookname,issuedate,expdate,retdate))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('issue'))
@app.route('/addbook1',methods=['GET','POST'])
def addbook1():
    if request.method=="POST":
        id = request.form['bid']
        name = request.form['bname']
        auth=request.form['author']
        qun=request.form['quantity']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO books(Book_id,Book_Name,Author,Quantity) values (%s,%s,%s,%s);",(id,name,auth,qun))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('book'))
@app.route('/addtransaction',methods=['GET','POST'])
def addtransaction():
    if request.method=="POST":
        id = request.form['uid']
        name = request.form['uname']
        auth=request.form['bname']
        qun=request.form['due']
        st = request.form['status']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO transaction(Transaction_Id,User_Name,Book_Name,Due,Status) values (%s,%s,%s,%s,%s);",(id,name,auth,qun,st))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('trans'))
#edit user
@app.route('/edituser1/<string:id>',methods=['GET','POST'])
def edituser1(id):
    con = mysql.connection.cursor()
    con.execute("select * from users where User_id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('edituser.html',id=r)
#update user
@app.route('/updateuser',methods=['GET','POST'])
def updateuser():
    if request.method=="POST":
        id = request.form['uid']
        name = request.form['uname']
        email = request.form['uemail']
        pas = request.form['password']
        con = mysql.connection.cursor()
        con.execute("update users set User_id=%s,User_Name=%s,User_Email=%s,Password=%s where User_id=%s;",(id,name,email,pas,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('user'))
#update book
@app.route('/updatebook',methods=['GET','POST'])
def updatebook():
    if request.method=="POST":
        id = request.form['bid']
        name = request.form['bname']
        auth = request.form['author']
        qun = request.form['quantity']
        con = mysql.connection.cursor()
        con.execute("update books set Book_id=%s,Book_Name=%s,Author=%s,Quantity=%s where Book_id=%s;",(id,name,auth,qun,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('book'))
#update issue
@app.route('/updateissue',methods=['GET','POST'])
def updateissue():
    if request.method=="POST":
        id = request.form['uid']
        uname = request.form['uname']
        bname = request.form['bname']
        idate = request.form['idate']
        edate = request.form['edate']
        rdate = request.form['rdate']
        con = mysql.connection.cursor()
        con.execute("update issues set Issue_Id=%s,User_Name=%s,Book_Name=%s,Issue_date=%s,Exp_Return_Date=%s,Return_Date=%s where Issue_Id=%s;",(id,uname,bname,idate,edate,rdate,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('issue'))
#update trans
@app.route('/updatetrans',methods=['GET','POST'])
def updatetrans():
    if request.method=="POST":
        id = request.form['uid']
        uname = request.form['uname']
        bname = request.form['bname']
        due = request.form['due']
        st = request.form['status']
        con = mysql.connection.cursor()
        con.execute("update transaction set Transaction_Id=%s,User_Name=%s,Book_Name=%s,Due=%s,Status=%s where Transaction_Id=%s;",(id,uname,bname,due,st,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('trans'))
if __name__=='__main__':
    app.secret_key='d1234'
    app.run(debug=True)