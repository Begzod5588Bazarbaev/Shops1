from django.forms import ModelForm
from .models import Post

class PostsForm(ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'image1',
            'image2',
            'image3',
            'inf',
            'rubric'
        )