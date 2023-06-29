from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label="제목")
    content = forms.CharField(label="내용", widget=forms.Textarea)
    writer = forms.CharField(label="작성자")