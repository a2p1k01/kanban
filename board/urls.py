from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('issue_list', views.issue_list, name='issue_list'),
    path('add_issue', views.add_issue, name='add_issue'),
    path('issue_update/<int:issue_id>/<int:action_id>', views.issue_update, name='issue_update'),
]
