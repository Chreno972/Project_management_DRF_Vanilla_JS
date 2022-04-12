from rest_framework import serializers
from .models import Task, Project, Material


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


class ProjectListSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        """_summary_
        """
        model = Project
        fields = ('id', 'title', 'state',)

class ProjectDetailSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        """_summary_
        """
        model = Project
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    """summary
    """

    class Meta:
        """summary
        """
        model = Material
        fields = '__all__'
