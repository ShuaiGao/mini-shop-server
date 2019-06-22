# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.validators.params import IDMustBePositiveInt
from app.api_docs import config as api_doc
from flask import request
__author__ = 'Allen7D'

api = RedPrint(name='config', description='应用配置', api_doc=api_doc)


mallConfig = {
	"mallName":u"酒店商城"
}


@api.route('/get-value/<string:key>', methods=['GET'])
@api.doc()
def get_config_value(key):
	print("======================================")
	print(key)
	return Success({key:mallConfig.get(key, "")})


@api.route('/get-value', methods=['GET'])
@api.doc()
def get_config_value_1():
	print("======================================")
	key = "no"
	key = request.args.get('key')
	print(key)
	return Success({key:mallConfig.get(key, "")})




@api.route('/hello', methods=['GET'])
@api.doc()
def get_config_hello():
	print("======================================")
	print("hello")
	return Success({"name":"huhao"})
