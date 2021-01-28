import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import joblib
import pandas as pd 
import numpy as np 
import mglearn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model', methods = ['GET','POST'])
def model():    
    if request.method == 'GET':
        return render_template('model/model.html')

    else:
        gender = request.form.get('gender')
        major = request.form.get('major')
        edu_lev = request.form.get('edu_lev')
        re_exp = request.form.get('re_exp')
        last = request.form.get('last')
        comp_type = request.form.get('comp_type')
        comp_size = request.form.get('comp_size')
        exp = request.form.get('exp')
        city = request.form.get('city')
         
        print(gender,major,edu_lev,re_exp,last,comp_type,comp_size,exp,city)
        print(type(city))


        # if not(gender and major and edu_lev and re_exp and last and comp_type and comp_size and exp):
        #     return render_template('model.html')

        # turnover = Turn()
        # turnover.gender = gender
        # turnover.major = major
        # turnover.edu_lev = edu_lev
        # turnover.re_exp = re_exp
        # turnover.last = last
        # turnover.comp_type = comp_type
        # turnover.comp_size = comp_size
        # turnover.exp = exp
        
        # db.session.add(turnover)
        # db.session.commit()


        return render_template('/model/model.html', gender=gender ,major=major, 
                                edu_lev=edu_lev, re_exp=re_exp, last=last, comp_type=comp_type,
                                comp_size=comp_size,exp=exp,city=city)
    

if __name__ == '__main__':

    # basedir = os.path.abspath(os.path.dirname(__file__))
    # dbfile = os.path.join(basedir,'db.sqlite')

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    # app.config['SQLALCHEMY_COMMIT_ON_TEADDOWN'] = True # 사용자 요청의 끝에서 커밋을 한다는 의미 데이터 베이스에 저장을 하겠다.
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db.init_app(app)
    # db.app = app 

    # # db 생성
    # db.create_all()
    app.run(host='127.0.0.1', port=5000,debug=True)    
