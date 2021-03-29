from django.urls import path, include

from . import views
from .routers import router

urlpatterns = [
    path('get_student/', views.get_all_students, name='get_all_students'),
    path('get_student/<int:pk>',views.get_student, name='get_student'),
    path('',include(router.urls)),
    # path('branch/retrieve/<int:pk>', views.BranchViewSets.retrieve, name='branch_retrieve'),
    # path('branch/create', views.BranchViewSets.create, name='branch_create'),
    # path('branch/update/<int:pk>', views.BranchViewSets.update, name='branch_update'),
    # path('branch/destroy/<int:pk>', views.BranchViewSets.destroy, name='branch_destroy'),
]