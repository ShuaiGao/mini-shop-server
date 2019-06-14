# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
__author__ = 'Allen7D'

create_client = {
	"parameters": [
	{
		"name":"account",
		"in":"body",
		"description": '''用户注册''',
		"required":"true",
		"schema": {
				"id": "Client",
				"required": ["openid","nickname", "account", "secret", "type"],
				"properties": {
					"openid": {
						"type":"string",
						"description": "openid",
						"enum": ["1"],
						"default": "1"
					},
					"nickname": {
						"type":"string",
						"description": "昵称",
						"enum": ["冬瓜","西瓜","北瓜"],
						"default": "冬瓜"
					},
					"account": {
						"type":"string",
						"account": "用户名",
						"enum": ["9898@qq.com"],
						"default": "9898@qq.com"
					},
					"secret": {
						"type":"string",
						"description": "密码",
						"enum": ["123456"],
						"default": "123456"
					},
					"type": {
						"type":"integer",
						"description": "邮箱账号登录(type:100)\n小程序登录(type:200)\n微信扫码登录(type:201)",
						"enum": [100,200,201],
						"default": 100
					},
				}
			}

	}],
	"responses": {
		"200": {
			"description": "用户注册",
			"examples": {
				"data": {
					"token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU1MzE1OTE0MCwiZXhwIjoxNTU1NzUxMTQwfQ.eyJ1aWQiOjIsInR5cGUiOjEwMCwic2NvcGUiOiJVc2VyU2NvcGUifQ.5OHN-WF3ujKGcP3kT8lUbVZ-BIKFUgZLZL989X_ae-qjoxI1Sf7O7FRE10s9jk2I1ZRHdYfWdKY-TmSRmn0p-A"
				},
				"error_code": 0
			}
		}
	}
}
