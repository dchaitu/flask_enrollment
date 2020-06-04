from apps import app,db
from flask import render_template,request,json,Response
from apps.models import User,Course,Enrollment
courseData = [
    {"courseID": "1111", "title": "PHP 111", "description": "Intro to PHP", "credits": "3", "term": "Fall, Spring"},
    {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": "4",
     "term": "Spring"},
    {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": "3",
     "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": "3",
                       "term": "Fall, Spring"},
    {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": "4",
     "term": "Fall"}]

@app.route("/")
#@app.route('/index')
def index():
    return render_template("index.html",index=True,login=False)
#
@app.route('/courses/')
@app.route('/courses/<term>')
def courses(term="Spring 2019"):
    return render_template("courses.html",courseData=courseData,courses=True,login=False,term=term)

@app.route('/register')
def register():
    return render_template("register.html",register=True,login=False)
@app.route('/login')
def login():
    return render_template("login.html",log=True,login=False)

@app.route('/enrollment',methods=['GET','POST'])
def enrollment():
    id = request.args.get('courseID')#id = request.forms['courseID']
    title = request.args.get('title')#forms work for both get and post
    term = request.args.get('term')
    return render_template("enrollment.html",enrollment=True,data={"id":id,"title":title,"term":term})

@app.route('/api/')
@app.route('/api/<id>')
def api(id=None):
    if id==None:
        jdata = courseData
    else:
        jdata = courseData[int(id)]

    return Response(json.dumps(jdata),mimetype="application/json")



@app.route('/user')
def user():
    User(user_id=1,first_name="Chaitanya",last_name="Dokara",email="cdokara@gmail.com",password="abc1234").save()
    User(user_id=2, first_name="Lokesh", last_name="Dokara", email="lokeshdokara@gmail.com", password="lok1234").save()
    users = User.objects.all()
    return render_template("users.html",users=users)