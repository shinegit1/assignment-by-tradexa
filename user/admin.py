from django.contrib import admin
from user.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =['id','user','text','created_at','updated_at']
