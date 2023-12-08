from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Issue
from .forms import IssueForm, DetailIssueForm, RegistrationForm, LoginForm


# Create your views here.
def index(request):
    return redirect('/issue_list')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('board:login')
    form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('board:issue_list')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def issue_list(request):
    user = request.user
    issue_lst = Issue.closed.filter(author=user)
    return render(request, 'issue_list.html', {'issues': issue_lst, 'user': user})


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required
def add_issue(request):
    issue = None
    issue_form = IssueForm(data=request.POST)
    if issue_form.is_valid() and request.method == 'POST':
        issue = issue_form.save(commit=False)
        issue.author = request.user
        issue.save()
    return render(request, 'new_issue.html', {'issue_form': issue_form, 'issue': issue})


@login_required
def issue_detail(request, year, month, day, slug):
    issue = get_object_or_404(Issue, slug=slug, created__year=year, created__month=month, created__day=day)
    detail_issue_form = DetailIssueForm(instance=issue, data=request.POST)
    if detail_issue_form.is_valid() and request.method == 'POST':
        issue.slug.title()
        issue.save()
    return render(request, 'issue_detail.html', {'issue': issue,
                                                 'detail_issue_form': detail_issue_form})


@login_required
def issue_delete(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    if request.method == 'POST':
        issue.delete()
    return redirect('board:issue_list')
