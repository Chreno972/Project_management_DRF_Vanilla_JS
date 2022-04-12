from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.task_list, name="task-list"),
    path('task-detail/<str:the_id>/', views.task_detail, name="task-detail"),
    path('task-create/', views.task_create, name="task-create"),
    path('task-update/<str:the_id>/', views.task_update, name="task-update"),
    path('task-delete/<str:the_id>/', views.task_delete, name="task-delete"),

    path(
        'project-list/',
        views.projectList,
        name="project-list"
    ),
    path(
        'project-detail/<str:the_id>/',
        views.projectDetail,
        name="project-detail"
    ),
    path(
        'project-create/',
        views.projectCreate,
        name="project-create"
    ),
    path(
        'project-update/<str:the_id>/',
        views.projectUpdate,
        name="project-update"
    ),
    path(
        'project-delete/<str:the_id>/',
        views.projectDelete,
        name="project-delete"
    ),

    path(
        'material-list/',
        views.materialList,
        name="material-list"
    ),
    path(
        'material-detail/<str:the_id>/',
        views.materialDetail,
        name="material-detail"
    ),
    path(
        'material-create/',
        views.materialCreate,
        name="material-create"
    ),
    path(
        'material-update/<str:the_id>/',
        views.materialUpdate,
        name="material-update"
    ),
    path(
        'material-delete/<str:the_id>/',
        views.materialDelete,
        name="material-delete"
    ),
]
