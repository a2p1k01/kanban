from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('issue_list', views.issue_list, name='issue_list'),
    path('<int:year>/'
         '<int:month>/'
         '<int:day>/'
         '<slug:slug>/', views.issue_detail, name='issue_detail'),
    path('issue_delete/<int:issue_id>', views.issue_delete, name='issue_delete'),
    path('add_issue', views.add_issue, name='add_issue'),
]

