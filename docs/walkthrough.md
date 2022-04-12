# Walkthrough

## Sommaire

[Terminer les settings](#terminer-les-settings)

[Enregistrer les modèles](#on-enregistre-un-model)


[Enregistrer l'admin](#on-enregistre-l'admin)

[Enregistrer le serializer](#on-enregistre-le-serializer)

[Enregistrer les vues](#on-enregistre-les-vues)
> [Vue d'ensemble de l'api](#vue-d'ensemble-de-l'api)
> [Liste et détail des taches](#liste-et-détail-des-taches)
> [Création des taches](#permettre-la-création-de-taches)
> [Update des taches](#permettre-l'update-de-tache)
> [Suppression des taches](#permettre-la-suppression-de-tache)

[Création des Urls](#on-crée-les-urls)

[App Frontend](#créer-l'app-frontend)
> [Ajouter l'app dans settings](#ajouter-l'app-dans-settings)
> [Créer la vue](#créer-la-vue-app-frontend)
> [Créer les url](#créer-les-urls-app-frontend)


---
---

[top](#sommaire)
## terminer les settings
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api.apps.ApiConfig',

    'rest_framework',
]
ROOT_URLCONF = 'todo_drf.urls'
WSGI_APPLICATION = 'todo_drf.wsgi.application'
STATIC_URL = '/static/'
```

---
---

[top](#sommaire)
## on enregistre un model
<!-- models.py -->
```python
class Task(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    related_project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return str(self.title)
```

---
---

[top](#sommaire)
## On enregistre l'admin
<!-- admin.py -->
```python
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'related_project')
```

**Les tasks dans l'admin django**
<img src="images/admin_task_view.PNG" alt="image des instances de task">

---
---

[top](#sommaire)
## On enregistre le serializer
<!-- serializers.py -->

```python
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        """_summary_
        """
        model = Task
        fields = '__all__'
```

---
---

## On enregistre les vues
<!-- views.py -->

[top](#sommaire)
### Vue d'ensemble de l'api
```python
"""On importe api_view, le serializer et le model"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


"""
le décorateur api_view sert à afficher
les endpoints de l'API depuis l'url 
http://127.0.0.1:8000/api/
"""
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-detail/<str:the_id>/",
        "Create": "/task-create/",
        "Update": "/task-update/<str:the_id>/",
        "Delete": "/task-delete/<str:the_id>/",
    }

    return Response(api_urls)
```

**L'overview**
<img src="images/apiOverview.PNG" alt="apiOverview">

---

[top](#sommaire)
### Liste et détail des taches
```python
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
```

---

[top](#sommaire)
### Permettre la création de taches

```python
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
```

---

[top](#sommaire)
### Permettre l'update de tache

```python
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
```

---

[top](#sommaire)
### Permettre la suppression de tache

```python
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
```

---
---

[top](#sommaire)
## On crée les URLS
<!-- urls.py -->

```python
# Dans le dossier qui contient settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Puis dans le dossier de l'app concernée
from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.task_list, name="task-list"),
    path('task-detail/<str:the_id>/', views.task_detail, name="task-detail"),
    path('task-create/', views.task_create, name="task-create"),
    path('task-update/<str:the_id>/', views.task_update, name="task-update"),
    path('task-delete/<str:the_id>/', views.task_delete, name="task-delete"),
]
```

**Endpoint http://127.0.0.1:8000/api/task-list/**
<img src="images/task_list.PNG" alt="apiOverview">


**Endpoint http://127.0.0.1:8000/api/task-detail/2/**
<img src="images/task-detail.PNG" alt="taskdetail">

---
---

[top](#sommaire)
## Créer l'app Frontend

`py manage.py startapp frontend`
Cette nouvelle app va récupérer les données, à partir de l'Api et nous allons y référencer les urls pour la visualisation

### Ajouter l'app dans settings

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api.apps.ApiConfig',
    'frontend.apps.FrontendConfig',

    'rest_framework',
]
```

---

[top](#sommaire)
### Créer la vue app frontend

```python
from django.shortcuts import render


def list(request):
    return render(request, "frontend/list.html")
```

---

[top](#sommaire)
### Créer les urls app frontend

```python
"""Depuis dossier racine urls.py"""
path('', include('frontend.urls')),

"""Depuis dossier frontend urls.py"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.list, name="list"),
]
```

---
---


[top](#sommaire)
## Mise en place du gabarit

```html

```
