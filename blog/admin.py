from django.contrib import admin
from .models import BlogPost, Topic, Blogger, Comment

#admin.site.register(BlogPost)
admin.site.register(Topic)
#admin.site.register(Blogger)
#admin.site.register(Comment)

#Define the admin class
@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'bio') 

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'post_date', 'display_topic')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blogpost', 'post_date', 'comment', 'commenter')
    list_filter = ['post_date']
    
    
