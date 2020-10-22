from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment_content',]
        widgets = {
            'comment_content': forms.Textarea(attrs={'id':'com_cont_form',
                                                        'placeholder':'Napisz tu swój komentarz...',
                                                        'rows':10,
                                                   }),
            'author': forms.TextInput(attrs={'id':'com_auth_form', 'placeholder':'Twój nick...'
            })    
        }
        