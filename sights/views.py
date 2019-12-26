from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Landmark, Comment, ProposedLandmark
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, LoginForm, ProposedLandmarkForm, FindForm
from account.models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated succesfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'sights/landmark/login.html', {'form': form})


def landmark_list(request):
    if request.method == 'POST':
        find_form = FindForm(data=request.POST)
        if find_form.is_valid():
            cd = find_form.cleaned_data
            lm = Landmark.objects.filter(name__icontains=cd['name'],
                                         information__icontains=cd['information'],
                                         type__icontains=cd['type'],
                                         address__icontains=cd['address'])

        else:
            lm = Landmark.objects.all()
    else:
        lm = Landmark.objects.all()
    find_form = FindForm()
    paginate_by = 3
    return render(request, 'sights/landmark/list.html', {'landmarks': lm,
                                                         'find_form': find_form,
                                                         'paginate_by': paginate_by})


def landmark_detail(request, name):
    landmark = get_object_or_404(Landmark, name=name)
    # список активных комментариев данной статьи
    comments = landmark.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # пользователь отправил комментарий
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # создаём комментарий, но пока не сохраняем в базе
            new_comment = comment_form.save(commit=False)
            # привязываем комментарий к текущей статье
            new_comment.landmark = landmark
            # привязываем комментарий к текущему пользователю
            curr_user = Profile.objects.get(user=request.user)
            new_comment.profile = curr_user
            # сохраняем комментарий в базе данных
            new_comment.save()
    elif request.user.is_authenticated:
        comment_form = CommentForm()
    else:
        comment_form = None
    return render(request, 'sights/landmark/detail.html', {'landmark': landmark,
                                                           'comments': comments,
                                                           'new_comment': new_comment,
                                                           'comment_form': comment_form})


def landmark_propose(request):
    new_propose = None
    if request.method == 'POST':
        # пользователь отправил форму
        propose_form = ProposedLandmarkForm(data=request.POST)
        if propose_form.is_valid():
            # создаём достопримечательность, но пока не сохраняем в базе
            new_propose = propose_form.save(commit=False)
            # привязываем достопримечательность к текущему пользователю
            curr_user = Profile.objects.get(user=request.user)
            new_propose.author = curr_user
            # сохраняем достопримечательность в базе данных
            new_propose.save()
    elif request.user.is_authenticated:
        propose_form = ProposedLandmarkForm()
    else:
        propose_form = None
    return render(request, 'sights/landmark/propose.html', {'new_propose': new_propose,
                                                            'propose_form': propose_form})




class LandmarkListView(ListView):
    queryset = Landmark.objects.filter(information__contains='ghb')
    context_object_name = 'landmarks'
    paginate_by = 3
    template_name = 'sights/landmark/list.html'
