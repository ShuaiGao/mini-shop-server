# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
"""
import os.path as op
from flask_admin import Admin, BaseView, expose
from flask import render_template, redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import form
from app.models.base import db
from app.models.user import User
from app.models.banner import Banner
from app.models.user_address import UserAddress
from app.models.product import Product


__author__ = 'Allen7D'


from wtforms.fields import SelectField

class BannerView(ModelView):
	form_overrides = dict(status=SelectField)
	form_args = dict(
        # Pass the choices to the `SelectField`
        status=dict(
            choices=[(0, 'waiting'), (1, 'in_progress'), (2, 'finished')]
        ))



# class MyView(BaseView):
# 	@expose('/')
# 	def index(self):
# 		return self.render("admin.html")

class MyView(ModelView):
	# Disable model creation
	# can_create = False

	# Override displayed fields
	column_list = ('email', 'nickname', 'auth')
	column_labels = {
		'email': u"邮件",
		'nickname':u"头像",
		'auth':u"权限"
	}
	form_extra_fields = {
	'auth':form.Select2Field('权限',choices=[('1','权限1'),('2','权限2')])
	}

	# form_overrides = dict(auth=SelectField)
	# form_args = dict(
 #        # Pass the choices to the `SelectField`
 #        auth=dict(
 #            choices=[(1, '超级管理员'), (10, '普通管理员'), (100, '普通用户')]
 #        ))

	def __init__(self, session, **kwargs):
		# You can pass name add other parameters if you want to
		super(MyView, self).__init__(User, session, **kwargs)


def CreateAdminView(admin):
	path = op.join(op.dirname(__file__), u'../static')
	admin.add_view(FileAdmin(path, u'/static', name = 'Static Files'))
	# admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
	# admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
	# admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))
	# admin.add_view(MyView(name="hello"))
	
	admin.add_view(BannerView(Banner, db.session, name=u'轮播图'))
	admin.add_view(MyView(db.session, name=u'用户管理'))
	admin.add_view(ModelView(UserAddress, db.session, name=u'地址管理'))
	admin.add_view(ModelView(Product, db.session, name=u'商品管理'))