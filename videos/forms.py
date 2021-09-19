from .models import Comment, Video
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        labels = {
            "content":"Type your comment here",
        }

class VideoForm(ModelForm):    
    class Meta:
        model = Video
        fields = ['video','thumbnail','title','description']