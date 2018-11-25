# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import Login_Form, Post_Form, Add_User_Form
from .models import User, Permission, Post


from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def Login(request):

    posts = Post.objects.filter(published=True)

    login_form = Login_Form()
    context = {'login_form': login_form, 'posts': posts}

    return render(request, 'login.html', context)


def Show_Post(request, post_id):
    post = Post.objects.filter(published=False).filter(pk =post_id )
    context = {'post': post}
    return render(request, 'post.html', context)


def Home(request):

    posts = Post.objects.filter(published=True)

    if request.session.get('member_id') :
        m_id = request.session.get('member_id')
        return render(request, 'home.html', context={})

    else:
        return HttpResponseRedirect('/')

def Panel(request):


    if request.session.get('member_id') :
        m_id = request.session.get('member_id')

        us = User.objects.get(id=m_id)
        permis = us.permission.all()


        if us.permission.filter(permi_type='View'):
            posts = Post.objects.filter(published=False)
            context = {'permis': permis, 'posts': posts}
        else:
            context = {'permis': permis}


        return render(request, 'panel.html', context)

    else:
        return HttpResponseRedirect('/')



def create(request):

    if request.session.get('member_id') :
        m_id = request.session.get('member_id')

        us = User.objects.get(id=m_id)
        permis = us.permission.all()

        if us.permission.filter(permi_type='Create'):
            post_form =Post_Form()
            context = {'post_form': post_form, 'permis': permis}

        else:
            msg = "You don't have Permission to view the unpublished posts"

            context = {'msg': msg, 'permis': permis}


        return render(request, 'create.html', context)

    else:
        return HttpResponseRedirect('/')



def update(request):
    if request.session.get('member_id') :
        m_id = request.session.get('member_id')

        us = User.objects.get(id=m_id)
        permis = us.permission.all()


        if us.permission.filter(permi_type='Update'):
            posts = Post.objects.all()
            context = {'permis': permis, 'posts': posts}
        else:
            context = {'permis': permis}


        return render(request, 'update.html', context)

    else:
        return HttpResponseRedirect('/')



def update_post(request,post_id):

    if request.session.get('member_id') :
        m_id = request.session.get('member_id')

        us = User.objects.get(id=m_id)
        permis = us.permission.all()

        post = Post.objects.get(pk=post_id)

        if us.permission.filter(permi_type='Create'):

            post_form = Post_Form(initial={'title': post.title, 'body': post.body})

            context = {'post_form': post_form, 'permis': permis}

        else:
            msg = "You don't have Permission to view the unpublished posts"

            context = {'msg': msg, 'permis': permis}


        return render(request, 'create.html', context)

    else:
        return HttpResponseRedirect('/')


def save_publish_post(request):

    m_id = request.session.get('member_id')
    use = User.objects.get(id=m_id)

    if request.method == 'POST':

        if 'Save' in request.POST:

            post_form = Post_Form(request.POST)

            if post_form.is_valid():
                obj = post_form.save(commit=False)
                obj.author = use.user_name
                post_form.save()

                messages.success(request, 'Post successfully saved.')
                return HttpResponseRedirect('/panel/create')

            else:
                messages.success(request, 'Post Not saved.')
                return HttpResponseRedirect('/panel/create')


        elif 'Publish' in request.POST:

            post_form = Post_Form(request.POST)

            if post_form.is_valid():

                obj = post_form.save(commit=False)
                obj.author = use.user_name
                obj.published = True
                post_form.save()
                messages.success(request, 'Post successfully published.')
                return HttpResponseRedirect('/panel/publish')

            else:
                messages.success(request, 'Post not published.')
                return HttpResponseRedirect('/panel/create')






def delete_page(request):
    if request.session.get('member_id') :
        m_id = request.session.get('member_id')

        us = User.objects.get(id=m_id)
        permis = us.permission.all()

        if us.permission.filter(permi_type='Delete'):
            posts = Post.objects.all()
            context = {'permis': permis, 'posts': posts}
        else:
            context = {'permis': permis}


        return render(request, 'delete.html', context)

    else:
        return HttpResponseRedirect('panel/')


def delete_post(request, post_id):
    post = Post.objects.filter(pk =post_id )
    post.delete()
    messages.success(request, 'Post successfully deleted.')

    return HttpResponseRedirect('/panel/delete')


def publish(request):
    posts = Post.objects.filter(published=False)


    if request.session.get('member_id') :
        m_id = request.session.get('member_id')

        us = User.objects.get(id=m_id)
        permis = us.permission.all()

        if us.permission.filter(permi_type='Delete'):
            posts = Post.objects.all()
            context = {'permis': permis, 'posts': posts}
        else:
            context = {'permis': permis}

        return render(request, 'publish.html', context)

    else:
        return HttpResponseRedirect('panel/')



def publish_post(request, post_id):
    post = Post.objects.get(pk =post_id )
    post.published = True
    post.save()
    messages.success(request, 'Post successfully published.')
    return HttpResponseRedirect('/panel/publish')


def Recommend(request):
    posts = Post.objects.filter(published=True)


    if request.session.get('member_id') :
        m_id = request.session.get('member_id')


        us = User.objects.get(id=m_id)
        permis = us.permission.all()

        if us.permission.filter(permi_type='Recommend'):

            context = {'permis': permis, 'posts': posts}
        else:
            context = {'permis': permis}


        return render(request, 'recommend.html', context)

    else:
        return HttpResponseRedirect('/')


def recommend_post(request, post_id):
    if request.session.get('member_id') :
        m_id = request.session.get('member_id')

        post = Post.objects.get(pk=post_id)

        if post.recommended == False :
            post.recommended = True
        else:
            post.recommended = False

        post.save()

        return HttpResponseRedirect('/panel/recommend')

    else:
        return HttpResponseRedirect('/')



def Show_Recommended(request):
    posts = Post.objects.filter(recommended=True)

    return render(request, 'login.html', context={'posts':posts})



def Add_User(request):


    if request.session.get('member_id') :
        m_id = request.session.get('member_id')

        us = User.objects.get(id=m_id)
        permis = us.permission.all()

        if us.permission.filter(permi_type='Create'):
            add_user_form = Add_User_Form()
            context = {'add_user_form': add_user_form, 'permis': permis}

        else:
            msg = "You don't have Permission to view the unpublished posts"

            context = {'msg': msg, 'permis': permis}


        return render(request, 'add_user.html', context)

    else:
        return HttpResponseRedirect('/')


def Submit_Add_User(request):

    m_id = request.session.get('member_id')
    use = User.objects.get(id=m_id)

    if request.method == 'POST':

        if 'Add User' in request.POST:

            add_user_form = Add_User_Form(request.POST)

            if add_user_form.is_valid():

                add_user_form.save()

                messages.success(request, 'User successfully saved.')
                return HttpResponseRedirect('/panel/add user')

            else:
                messages.success(request, 'User Not saved.')
                return HttpResponseRedirect('/panel/add user')


def login(request):

    if request.method == 'POST':

        if 'Login' in request.POST:

            login_form = Login_Form(request.POST)

            m = User.objects.get(user_name=request.POST['user_name'])
            if m.user_pass == request.POST['user_pass']:
                request.session['member_id'] = m.id
                request.session['member_name'] = m.user_name

                return HttpResponseRedirect('/')

            else:
                return HttpResponse("Your username and password didn't match.")


def logout(request):
    try:
        #del request.session['member_id']
        request.session.flush()
    except KeyError:
        pass
    return HttpResponseRedirect('/')
