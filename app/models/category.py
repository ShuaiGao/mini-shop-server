# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from app.models.image import Image

from app.libs.error_code import CategoryException
from app.models.base import Base, db

__author__ = 'Allen7D'

class Category(Base):
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	topic_img_id = Column(Integer, ForeignKey('image.id'))
	image = relationship('Image', foreign_keys=[topic_img_id])

	def keys(self):
		self.hide('topic_img_id').append('image')
		return self.fields

	@staticmethod
	def get_all_categories():
		return Category.query.all_or_404(e=CategoryException)


class CategoryView(ModelView):
	column_exclude_list = ['delete_time', 'update_time', 'create_time', 'status']
	#column_list = ('email', 'nickname', 'auth')
	column_labels = {
		'name': u"分类名称",
		# 'topic_img_id':u"图标id",
		'image':u"图标"
	}

	form_ajax_refs = {
		'topic_img_id': QueryAjaxModelLoader('topic_img_id', db.session, Image, fields=['id'], page_size=10)
	    # 'Image': {
	    #     'fields': ['topic_img_id'],
	    #     'page_size': 10
	    # }
	}
	#                form_ajax_refs = {
 #                    'user': QueryAjaxModelLoader('user', db.session, User, fields=['email'], page_size=10)
 #                }

	def __init__(self, session, **kwargs):
		# You can pass name add other parameters if you want to
		super(CategoryView, self).__init__(Category, session, **kwargs)

	# form_overrides = dict(auth=SelectField)
	# form_args = dict(
 #        # Pass the choices to the `SelectField`
 #        auth=dict(
 #            choices=[(1, '超级管理员'), (10, '普通管理员'), (100, '普通用户')]
 #        ))

