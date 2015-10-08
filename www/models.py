#!usr/bin/env python
# -*- coding:utf-8 -*-

'''
第一,根据Model 创建了三个表web app 需要的三个表User Blog Comment

第二,操作数据库之前,先要初始化数据库

mysql -u root -p < schema.sql
第三,编写访问数据库的测试代码,此时,我们就可以通过操作类来操作数据库了(通过orm.py).
'''

import time,uuid

from transwarp.db import next_id
from transwarp.orm import Model,StringFielf,BooleanField,TextField

class User(Model):
	__table__ = 'users'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(50')
	email = StringField(updatable=False,ddl='varchar(50')
	password =StringField(ddl='varchar(50)')
	admin = BooleanField()
	name = StringField(ddl='varchar(50)')
	image = StringFiel(ddl='varchar(500)')
	created_at = FloatField(updatable=False, default=time.time)

class Blog(Model):
	__table__ = 'blogs'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(updatable=False, ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(updatable=False, default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(updatable=False, ddl='varchar(50)')
    user_id = StringField(updatable=False, ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(updatable=False, default=time.time)