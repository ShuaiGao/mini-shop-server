# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/19.
"""
from flask import render_template, redirect, url_for
from . import web

__author__ = 'Allen7D'


# @web.route('/', defaults={'path': ''})
# @web.route('/<path:path>')
@web.route('/api')
def index():
    '''默认跳转的 API 文档'''
    return redirect('/apidocs/#/')
    # return render_template("index.html")

@web.route('/doc')
def doc():
    '''跳转'''
    return redirect(url_for('web.index'))


@web.route('/home/')
def home_home():
    data = {
    	'title': "今嗨旅遊",
    }
    return render_template("home.html", **data)

@web.route('/')
def home():
    data = {
    	'title': "今嗨旅遊",
    	"companyName":"今嗨旅游",
    }
    return render_template("home.html", **data)

