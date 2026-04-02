from django.forms import ModelForm, Form, forms

from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'date')