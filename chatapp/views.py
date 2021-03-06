from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import Post,Follow
from .forms import PostForm,FollowForm
from django.contrib.auth.decorators import login_required

def top(request):
    try:
        fobjs = Follow.objects.filter(author=request.user)
        flists = []
        posts = []
        check = []
        for fobj in fobjs:
            a = fobj.follow
            flists.append(a)
            #二重フォロー対策
            for flist in flists:
                if flist not in check:
                    check.append(flist)
        for f in check:
<<<<<<< HEAD
             b = User.objects.get(username=f)
             posts.append(b)
=======
            try:
                b = User.objects.get(username=f)
                posts.append(b)
            except:
                pass
>>>>>>> 0bdc8184836a60da7f293558675947533a5139b7
        return render(request,'chatapp/top.html',{'posts':posts})
    except TypeError:
        return render(request,'chatapp/top.html',{})

<<<<<<< HEAD


=======
>>>>>>> 0bdc8184836a60da7f293558675947533a5139b7
@login_required
def chat(request,pk):
    #選んだユーザーの名前取得
    user = User.objects.values_list('username',flat=True).get(pk=pk)
    #選んだユーザーの情報受け取り>>templateでauthor指定に使う
    author = User.objects.get(pk=pk)
    #Postリクエストの時に新規登録
    if request.method == 'POST':
        form = PostForm(request.POST)
        #フォームチェックとユーザー設定
        if form.is_valid():
            chats = form.save(commit=False)
            #authorはユーザー情報がいるのでrequest.user
            chats.author = request.user
            #touserはCharFieldで設定しているのでユーザの文字列を取得(特殊)
            chats.touser = user
            chats.save()
            return redirect('chat',pk)
    #getメソッドの時の動き
    else:
        lists = Post.objects.all()
        form = PostForm()
    #lists(全メッセージ)>>テンプレートでそれぞれ指定して分解
    return render(request,'chatapp/chat.html',{'lists':lists,'form':form,'user':user,'author':author})

@login_required
def seach(request):
    if request.method == 'POST':
        form = FollowForm(request.POST)
        if form.is_valid():
            follow = form.save(commit=False)
            follow.author = request.user
            follow.save()
            return redirect('top')
    else:
        form = FollowForm()
    return render(request,'chatapp/seach.html',{'form':form})
