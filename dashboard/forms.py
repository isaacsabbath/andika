from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = ["title", "content", "featured_image", "published"]
