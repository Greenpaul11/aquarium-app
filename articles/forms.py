from django import forms
from .models import ArticleComment

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['comment']
    
    def clean(self):
        data = self.cleaned_data
        comment = data.get('comment')
        q_s = ArticleComment.objects.all().filter(comment__icontains=comment)
        if q_s.exists():
            self.add_error("comment", f'Comment like this already exists')
        return data