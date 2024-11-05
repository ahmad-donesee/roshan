from django.contrib import admin

from .models import Dataset,Tags,Data,Information

@admin.register(Dataset)
class  DatasetAdmin(admin.ModelAdmin):
    list_display = ('author','name','created_at','edit_at')

@admin.register(Data)
class  DataAdmin(admin.ModelAdmin):
    list_display = ('relatedname','author','name','is_active','created_at','edit_at')

@admin.register(Tags)
class  TagsAdmin(admin.ModelAdmin):
    list_display = ('relatedname','author','name','is_active','created_at','edit_at')

@admin.register(Information)
class  InformationAdmin(admin.ModelAdmin):
    list_display = ('relatedname','author','name','is_active','created_at','edit_at')

