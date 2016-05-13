# -*- coding: utf-8 -*-
from django.contrib import admin
import models

#from django.contrib.auth.models import User 
#user=User.objects.create_superuser('admin','zhuliang06@baidu.com','admin')
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','age','sex')   #列表显示
    search_fields=('name',)             #搜索
    list_filter = ('type',)             #过滤器
    date_hierarchy = 'birth'            #日期型字段进行层次划分。
    ordering = ('-birth','age')         #对出生日期降序排列，对年级升序
    fields = ('name','sex','age','birth','type')    #自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性
           
#admin.site.register(Person,AuthorAdmin)

admin.site.register(models.BlogPost, models.BlogPostAdmin)