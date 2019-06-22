# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/26.
"""
from app.libs.swagger_filed import IntegerPathFiled

__author__ = 'Allen7D'


get_config_value = {
	"parameters": ["mallName"],
	"responses": {
		"200": {
			"description": "请求成功",
			"examples": {
				"data": {
					"description": "首页轮播图",
					"id": 1,
					"items": [
						{
							"id": 1,
							"img_url": "0.0.0.0:8080/static/images/banner-4a.png",
							"key_word": "6",
							"type": 1
						}
					],
					"name": "首页置顶"
				},
				"error_code": 0,
				"msg": "成功"
			}
		},
		'404': {
			"description": "请求失败",
			"examples": {
				"error_code": 4000,
				"msg": "请求的Banner不存在",
				"request_url": "GET /v1/banner/100"
			}
		}
	}
}
