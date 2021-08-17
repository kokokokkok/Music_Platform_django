from django.conf.urls.static import static
from django.urls import re_path
from . import views
from django.urls import path, include

# このプロジェクトのurl.pyで認証の処理プログラムを読んでいるので、このアプリのviewを呼び出す必要がないのでここにも認証のurlはいらない。
# その代わりtemplatesの中に"registration"というディレクトリの中に"login.html"と"logged_out.html"という決められた名前のhtmlを作りそこにつなげてくれる

urlpatterns = [
    # re_path(r'^') 現状どう使えばいいのかわからない （ヒント：正規表現とurl）
    path('', views.front, name='front'),
    path('home', views.home, name='home'),
    path('ras_music', views.plat_list, name='plat_list'),  # home
    path('<int:pk>', views.mono_music, name='mono_music'),
    path('upload', views.upload_music, name='upload_music'),
    path('pay', views.PayView.as_view(), name="pay_test"),
    # path('pay', views.payjp_test, name='pay_test'),
]
