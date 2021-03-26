from django.urls import path

from . import views

urlpatterns = [
    path('get_student/', views.get_all_students, name='get_all_students'),
    path('get_student/<int:pk>',views.get_student, name='get_student'),
    path('branch/list',views.BranchViewSets.list, name='branch_list'),
    path('branch/retrieve/<int:pk>', views.BranchViewSets.retrieve, name='branch_retrieve'),
    path('branch/create', views.BranchViewSets.create, name='branch_create'),
    path('branch/update/<int:pk>', views.BranchViewSets.update, name='branch_update'),
    path('branch/destroy/<int:pk>', views.BranchViewSets.destroy, name='branch_destroy'),
]