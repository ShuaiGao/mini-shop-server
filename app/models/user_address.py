# -*- coding: utf-8 -*-
"""
  Created by Allen7D on 2018/6/25.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from flask_admin.contrib.sqla import ModelView

from app.models.base import Base

__author__ = 'Allen7D'

class UserAddress(Base):
	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	name =  Column(String(30), nullable=False)
	mobile =  Column(String(20), nullable=False)
	country =  Column(String(20))
	province =  Column(String(20))
	city =  Column(String(20))
	detail =  Column(String(100)) # 具体体制

	def keys(self):
		# return ['id', 'email', 'nickname', 'auth', 'user_address']
		self.hide('id', 'user_id' )
		return self.fields


class UserAddressView(ModelView):
	column_exclude_list = ['delete_time', 'update_time', 'create_time', 'status']
	#column_list = ('email', 'nickname', 'auth')
	column_labels = {
		'user_id': u"玩家id",
		'name': u"分类名称",
		'mobile': u"手机号",
		'country': u"城市",
		'province':u"省（市、自治区）",
		'city':u"市",
		'detail':u"详细地址",
		'image':u"图标"
	}

	def __init__(self, session, **kwargs):
		# You can pass name add other parameters if you want to
		super(UserAddressView, self).__init__(UserAddress, session, **kwargs)
