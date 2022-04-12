from pydoc import source_synopsis
from django.db import models


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


class Material(models.Model):
    """_summary_"""

    class Usability(models.TextChoices):
        """_summary_"""
        EASY = "EASY"
        MEDIUM = "MEDIUM"
        HARD = "HARD"

    title = models.CharField(max_length=200)
    related_project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, null=True, blank=True
    )
    project_type = models.CharField(max_length=200, blank=True, null=True)
    materials_source = models.CharField(max_length=200, blank=True, null=True)
    usability_level = models.fields.CharField(
        max_length=50,
        choices=Usability.choices,
    )

    def __str__(self):
        return str(self.title)


class Project(models.Model):
    """_summary_"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    github_link = models.CharField(max_length=200, blank=True, null=True)
    website_link = models.CharField(max_length=200, blank=True, null=True)
    materials = models.ManyToManyField(Material, blank=True)

    def get_materials(self):
        """_summary_

        Args:
            self (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.materials.title()

    def __str__(self):
        return str(self.title)
