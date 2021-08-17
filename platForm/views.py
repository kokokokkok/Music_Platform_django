import payjp
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import contentsForm, CommentForm  # contentsForm
from .models import contents, Comment



"""
class front(View):
    def get(self, request):
        context = {'message': 'hello world', }
        return render(request, 'hello.html', context)
front = front.as_view()
"""  # classの使い方がわからん


def front(request):
    musics = contents.objects.all()
    keyword = request.GET.get('keyword')  # 撃ち込まれた言葉を保持
    if keyword:  # keywordがhtmlのimputに撃ち込まれたら
        musics = musics.filter(Q(music_name__icontains=keyword))  # __icontainsとは部分一致のこと　
        # このQ（music_name__icontains=keyword) | Q(music_views__icontains=keyword）の様にモデルで定義した変数を追加すれば検索の範囲を広げることができる
        # if文で分岐させているので変数はmusicsでいい。検索されなければしっかりとすべてが表示されるから
        messages.success(request, format(keyword))
    # ここに　url　""　がが検索されたらif文をbreakするやつを書けば戻れる！

    return render(request, 'main/front.html', {'musics': musics})


def home(request):
    musics = contents.objects.all()
    keyword = request.GET.get('keyword')  # 撃ち込まれた言葉を保持
    if keyword:  # keywordがhtmlのimputに撃ち込まれたら
        musics = musics.filter(Q(music_name__icontains=keyword))  # __icontainsとは部分一致のこと　
        # このQ（music_name__icontains=keyword) | Q(music_views__icontains=keyword）の様にモデルで定義した変数を追加すれば検索の範囲を広げることができる
        # if文で分岐させているので変数はmusicsでいい。検索されなければしっかりとすべてが表示されるから
        messages.success(request, format(keyword))
    # ここに　url　""　がが検索されたらif文をbreakするやつを書けば戻れる！

    return render(request, 'main/home.html', {'musics': musics})


def plat_list(request):  # カテゴリのやつ
    posts = contents.objects.order_by('-published_date')
    return render(request, 'main/plat_list.html')


def mono_music(request, pk):
    post = get_object_or_404(contents, pk=pk)
    post.views += 1
    post.save()
    comment_list = Comment.objects.all()
    # comment_list = Comment.objects.filter('-published_date')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mono_music, pk=pk)  # {'form': form, 'post': post, 'comment_list': comment_list})
    else:
        form = CommentForm()
        return render(request, 'main/mono_musics.html', {'form': form, 'post': post, 'comment_list': comment_list})


@login_required
def upload_music(request):
    if request.method == 'POST':
        form = contentsForm(request.POST, request.FILES)  # fieldFileかImageFileを扱う場合request.FIlESが必要になる。その他は同じ
        if form.is_valid():  # formにあるすべてのものが入力されない限りTrueにならない
            form.save()
            return redirect('front')
        else:
            print("ere")
    else:
        form = contentsForm()
        return render(request, 'main/upload.html', {'form': form})


"""
def PayView(request):
    public_key = get_object_or_404() #?
    amount = request.POST.get("amount")
    payjp_token = request.POST.get("payjp-token")

    # トークンから顧客情報を生成
    customer = payjp.Customer.create(email="example@pay.jp", card=payjp_token)
    # 支払いを行う
    charge = payjp.Charge.create(
        amount=amount,
        currency="jpy",
        customer=customer.id,
        description="Django example charge",
    )

    context = {"public_key": "pk_test_e21be9eb8f6a5004b86cb288",  # 直接貼るのは本当はよくない
               "amount": amount, "customer": customer, "charge": charge,
               }

    return render(request, "main/payjp_test", {"public_key": "pk_test_e21be9eb8f6a5004b86cb288",  # 直接貼るのは本当はよくない
                                               "amount": amount, "customer": customer, "charge": charge,
                                               })
"""


class PayView(View):
    """
    use PAY.JP API
    """

    def get(self, request):
        # 公開鍵を渡す
        return render(
            request, "main/payjp_test.html", {"public_key": "pk_test_e21be9eb8f6a5004b86cb288"}
        )

    def post(self, request):
        amount = request.POST.get("amount")
        payjp_token = request.POST.get("payjp-token")

        # トークンから顧客情報を生成
        customer = payjp.Customer.create(email="example@pay.jp", card=payjp_token)
        # 支払いを行う
        charge = payjp.Charge.create(
            amount=amount,
            currency="jpy",
            customer=customer.id,
            description="Django example charge",
        )

        context = {"amount": amount, "customer": customer, "charge": charge}
        return render(request, "main/payjp_test.html", context)
