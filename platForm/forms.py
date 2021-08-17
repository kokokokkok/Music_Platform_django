from django import forms

from .models import contents, Comment


# formsではadminで使う編集フォームを簡単に作れる！

class contentsForm(forms.ModelForm):
    class Meta:
        model = contents
        fields = ('music_main', 'music_name', 'category_name', 'author', 'author_comment')
        # 'music_img')'music_main'がfieldfileなので少しviewの処理が変わる


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
