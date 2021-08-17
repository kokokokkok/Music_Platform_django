from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # ここの'admin/'を変えておかないと簡単に管理サイトのurlを特定される。
    path('', include('platForm.urls')),  # ここでappのurlとつなげる。
    path('accounts/', include('django.contrib.auth.urls')),  # ここは認証のdjangoが提供しているviewの処理につないでいる。よってこれだけで認証の新規登録以外は完了する。
    # templatesの中に"registration"というディレクトリの中に"login.html"と"logged_out.html"という決められたhtmlを作りそこにつなげてくれる
    path('accounts/', include('accounts.urls')),  # アカウント新規登録のアプリへつなげている

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
