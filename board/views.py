from django.shortcuts import render, redirect, get_object_or_404
from .models import Issue
from .forms import IssueForm


# Create your views here.
def index(request):
    return redirect('/issue_list')


def issue_list(request):
    issue_lst = Issue.closed.all()
    return render(request, 'issue_list.html', {'issues': issue_lst})


def issue_update(request, issue_id, action_id):
    issue = get_object_or_404(Issue, id=issue_id)
    match action_id:
        case 1:
            issue.status = Issue.Status.BUG
        case 2:
            issue.status = Issue.Status.WORK
        case 3:
            issue.status = Issue.Status.DONE
    issue.save()
    if action_id == 4:
        issue.delete()
    return redirect('board:issue_list')


def add_issue(request):
    issue = None
    issue_form = IssueForm(data=request.POST)
    if issue_form.is_valid():
        issue = issue_form.save(commit=False)
        issue.save()
    return render(request, 'new_issue.html', {'issue_form': issue_form, 'issue': issue})
