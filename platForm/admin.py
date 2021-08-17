from django.contrib import admin
from .models import contents

# モデルから定義された編集、管理したいものを渡してもらっている。

admin.site.register(contents)

