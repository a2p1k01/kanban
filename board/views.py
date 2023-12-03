from django.shortcuts import render, redirect, get_object_or_404
from .models import Issue
from .forms import IssueForm, DetailIssueForm


# Create your views here.
def index(request):
    return redirect('/issue_list')


def issue_list(request):
    issue_lst = Issue.closed.all()
    return render(request, 'issue_list.html', {'issues': issue_lst})


def add_issue(request):
    issue = None
    issue_form = IssueForm(data=request.POST)
    if issue_form.is_valid() and request.method == 'POST':
        issue = issue_form.save(commit=False)
        issue.save()
    return render(request, 'new_issue.html', {'issue_form': issue_form, 'issue': issue})


def issue_detail(request, year, month, day, slug):
    issue = get_object_or_404(Issue, slug=slug, created__year=year, created__month=month, created__day=day)
    detail_issue_form = DetailIssueForm(instance=issue, data=request.POST)
    if detail_issue_form.is_valid() and request.method == 'POST':
        issue.slug.title()
        issue.save()
    return render(request, 'issue_detail.html', {'issue': issue,
                                                 'detail_issue_form': detail_issue_form})


def issue_delete(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    if request.method == 'POST':
        issue.delete()
    return redirect('board:issue_list')
