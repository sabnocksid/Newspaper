from django.contrib import admin
from newspaper.models import Post, Category, Tag, Contact, UserProfile, Comment, Newsletter
from django_summernote.admin import SummernoteModelAdmin

admin.site.register([Category, Tag, Contact, UserProfile, Comment, Newsletter])


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)