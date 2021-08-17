from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Model, IntegerField
from django.utils import timezone
from django.conf import settings
from django.db import models


class contents(models.Model):  # models.Modelはdjangoにデータベースに保存するべきだと伝えている。　# 下の5行がプロパティ（状態）を表している
    music_name = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=20)
    author_comment = models.CharField(max_length=100)

    music_category = ((1, 'rock'), (2, 'hophop'), (3, "vacaloid"))

    category_name = models.IntegerField(choices=music_category, default='SOME STRING')  # defaultがいるないとエラーになる

    """
    music_img = models.ImageField(
        upload_to='uploads/img',
        verbose_name='添付画像ファイル',
        validators=[FileExtensionValidator(['png', 'jpeg'])],
    )
    """
    music_main = models.FileField(  # このImageFieldとFileFieldは本質的にデータを入力時に作るのではなくアップロードなので他とは違う対応になる
        default=None,
        upload_to='uploads/sound',
        verbose_name='添付音声ファイル',
        validators=[FileExtensionValidator(['mp3', 'mp4', 'acc', ])],
    )

    def publish(self):  # 下の２つのメソッド（命令）を定義している　   ここでは何をしている？
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.music_name


class Comment(models.Model):
    # post = models.ForeignKey( on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    # slug = models.SlugField(null=True, blank=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def publish(self):  # 下の２つのメソッド（命令）を定義している　   ここでは何をしている？
        self.published_date = timezone.now()
        self.save()
