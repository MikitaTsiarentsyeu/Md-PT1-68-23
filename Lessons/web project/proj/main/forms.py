from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPostFreeForm(forms.Form):

    title = forms.CharField(max_length=200, label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'test_form'}), label="Content")
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label="Post Type")
    image = forms.ImageField(label="Main image")

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        
        return title
    
    def clean_post_type(self):
        if self.cleaned_data['post_type'] == "c":

            if '(c)' not in self.cleaned_data['title']:
                raise ValidationError("The title of a copyright post should contain (c)")
            
        return self.cleaned_data['post_type']



class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_type', 'image')
        labels = {'title':"Title", 'content':"Content", 'posts_type':"Post type", 'image':"Image"}
        widgets = {'content':forms.Textarea(attrs={'class':'test_form'})}

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        
        return title
    
    def clean_post_type(self):
        if self.cleaned_data['post_type'] == "c":

            if '(c)' not in self.cleaned_data['title']:
                raise ValidationError("The title of a copyright post should contain (c)")
            
        return self.cleaned_data['post_type']
