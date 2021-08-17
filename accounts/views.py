from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User


class SignUpView(generic.CreateView):  # 新規登録もusercreateformというクラスをdjangoが提供しているので簡単
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
