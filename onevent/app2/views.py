from django.shortcuts import render, get_object_or_404


# Create your views here.
from app1.models import Events
from app2.forms import CommentForm


def post_detail(request, slug):
    template_name = 'app1/events/event_live.html'
    post = get_object_or_404(Events, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
