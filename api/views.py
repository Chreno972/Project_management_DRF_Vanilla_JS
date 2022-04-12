from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, ProjectListSerializer, ProjectDetailSerializer, MaterialSerializer

from .models import Task, Project, Material


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-detail/<str:the_id>/",
        "Create": "/task-create/",
        "Update": "/task-update/<str:the_id>/",
        "Delete": "/task-delete/<str:the_id>/",
        "Projects_List": "/project-list/",
        "Projects_Detail View": "/project-detail/<str:the_id>/",
        "Projects_Create": "/project-create/",
        "Projects_Update": "/project-update/<str:the_id>/",
        "Projects_Delete": "/project-delete/<str:the_id>/",
        "Materials_List": "/material-list/",
        "Materials_Detail View": "/material-detail/<str:the_id>/",
        "Materials_Create": "/material-create/",
        "Materials_Update": "/material-update/<str:the_id>/",
        "Materials_Delete": "/material-delete/<str:the_id>/",
    }

    return Response(api_urls)


@api_view(["GET"])
def task_list(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    tasks = Task.objects.all().order_by("-id")
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def task_detail(request, the_id):
    """_summary_

    Args:
        request (_type_): _description_
        the_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    tasks = Task.objects.get(id=the_id)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def task_create(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def task_update(request, the_id):
    """_summary_

    Args:
        request (_type_): _description_
        the_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    task = Task.objects.get(id=the_id)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def task_delete(request, the_id):
    """_summary_

    Args:
        request (_type_): _description_
        the_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    task = Task.objects.get(id=the_id)
    task.delete()

    return Response("Item succsesfully delete!")


# Projects


@api_view(["GET"])
def projectList(request):
    projects = Project.objects.all().order_by("-id")
    serializer = ProjectListSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def projectDetail(request, the_id):
    projects = Project.objects.get(id=the_id)
    serializer = ProjectDetailSerializer(projects, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def projectCreate(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def projectUpdate(request, the_id):
    project = Project.objects.get(id=the_id)
    serializer = ProjectSerializer(instance=project, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def projectDelete(request, the_id):
    project = Project.objects.get(id=the_id)
    project.delete()

    return Response("Item succsesfully delete!")
    


# Materials


@api_view(["GET"])
def materialList(request):
    materials = Material.objects.all().order_by("-id")
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def materialDetail(request, the_id):
    materials = Material.objects.get(id=the_id)
    serializer = MaterialSerializer(materials, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def materialCreate(request):
    serializer = MaterialSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def materialUpdate(request, the_id):
    material = Material.objects.get(id=the_id)
    serializer = MaterialSerializer(instance=material, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def materialDelete(request, the_id):
    material = Material.objects.get(id=the_id)
    material.delete()

    return Response("Item succsesfully delete!")