from django.shortcuts import render, get_object_or_404
from .models import Landmark, Comment
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


def landmark_list(request):
    lm = Landmark.objects.all()
    return render(request, 'sights/landmark/list.html', {'landmarks': lm})


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
            # сохраняем комментарий в базе данных
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'sights/landmark/detail.html', {'landmark': landmark,
                                                           'comments': comments,
                                                           'new_comment': new_comment,
                                                           'comment_form': comment_form})


class LandmarkListView(ListView):
    queryset = Landmark.objects.all()
    context_object_name = 'landmarks'
    paginate_by = 3
    template_name = 'sights/landmark/list.html'
