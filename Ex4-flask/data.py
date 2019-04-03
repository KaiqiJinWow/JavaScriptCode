from flask import Flask, flash, redirect, render_template, request,jsonify
from flask import make_response
import pandas as pd
from page_utils import Pagination
import csv




app = Flask(__name__)
@app.route('/')
def test():
    datas=pd.read_csv('data/countriesData.csv',sep=',',engine='python')
    datas = datas.rename(columns={'2010[YR2010]':'2010','2011[YR2011]':'2011','2012[YR2012]':'2012','2013[YR2013]':'2013','2014[YR2014]':'2014'})
    datas.dropna(axis=0, how='any', inplace=True)
    li = datas
    pager_obj = Pagination(request.args.get("page", 1), len(li), request.path, request.args, per_page_count=5)
    print(request.path)
    print(request.args)
    index_list = li[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template("FrontEndData.html", datas=index_list, html=html)
@app.route('/' , methods=['POST'] )
def addItem():
	
    CountryName = request.form['CountryName'] if request.form['CountryName']!='' else '..'
    SeriesName = request.form['SeriesName'] if request.form['SeriesName']!='' else '..'
    Y2010 = request.form['2010'] if request.form['2010']!='' else '..'
    Y2011 = request.form['2011'] if request.form['2011']!='' else '..'
    Y2012 = request.form['2012'] if request.form['2012']!='' else '..'
    Y2013 = request.form['2013'] if request.form['2013']!='' else '..'
    Y2014 = request.form['2014'] if request.form['2014']!='' else '..'
    s = CountryName + ',..,' + SeriesName + ',..,' +Y2010+','+Y2011+','+Y2012+','+Y2013+','+Y2014+'\n'
    print("Y20134 is ")
    print(Y2014)
    f = open("data/countriesData.csv","r")
    contents = f.readlines()
    f.close()
    contents.insert(1, s)
    f = open("data/countriesData.csv","w")
    contents ="".join(contents)
    f.write(contents)
    f.close()
    datas1=pd.read_csv('data/countriesData.csv',sep=',',engine='python')
    datas1 = datas1.rename(columns={'2010[YR2010]':'2010','2011[YR2011]':'2011','2012[YR2012]':'2012','2013[YR2013]':'2013','2014[YR2014]':'2014'})

    datas1.dropna(axis=0, how='any', inplace=True)
    li = datas1
    pager_obj = Pagination(request.args.get("page", 1), len(li), request.path, request.args, per_page_count=5)
    print(request.path)
    print(request.args)
    index_list = li[0:5]
    html = pager_obj.page_html()
    return render_template("FrontEndData.html", datas=index_list, html=html)

if __name__ == "__main__":
    app.run(debug=True)