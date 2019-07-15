# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from flask_admin.contrib.sqla import ModelView
from app.libs.error_code import BannerMissException
from app.models.baner_item import BannerItem
from app.models.base import Base, db


from wtforms.fields import SelectField

__author__ = 'Allen7D'

class Banner(Base):
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	description = Column(String(255))
	_items = relationship('BannerItem', backref='author', lazy='dynamic')

	def keys(self):
		self.append('items')
		return self.fields

	@property
	def items(self):
		return self._items.all()

	@staticmethod
	def get_banner_by_id(id):
		with db.auto_check_empty(BannerMissException):
			return Banner.query.filter_by(id=id).first_or_404()

class BannerView(ModelView):
	column_exclude_list = ['delete_time', 'update_time', 'create_time', 'status']
	column_labels = {
		'name': u"名称",
		'description': u"描述",
		# 'topic_img_id':u"图标id",
		'image':u"图标"
	}
	form_overrides = dict(status=SelectField)
	form_args = dict(
        # Pass the choices to the `SelectField`
        status=dict(
            choices=[(0, 'waiting'), (1, 'in_progress'), (2, 'finished')]
        ))
	def __init__(self, session, **kwargs):
		# You can pass name add other parameters if you want to
		super(BannerView, self).__init__(Banner, session, **kwargs)
