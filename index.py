from flask import render_template, request, redirect, url_for, session, flash
# from decorators import login_required
from config import app


@app.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    if request.method == 'GET':
        return render_template('index.html')



if __name__ == '__main__':
    app.run()