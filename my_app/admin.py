from django.contrib import admin
from my_app.models import  FilesModel,RolesModel,PermissionModel
# Register your models here.

admin.site.register(FilesModel)
admin.site.register(RolesModel)
admin.site.register(PermissionModel)



