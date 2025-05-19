from django.db import models

class Handbook(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=20, default='1.0.0')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Folder(models.Model):
    handbook = models.ForeignKey(Handbook, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    level = models.PositiveIntegerField(default=1)
    path = models.CharField(max_length=255, blank=True)
    order_num = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Document(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file_url = models.URLField()
    file_size = models.IntegerField(default=0)
    file_type = models.CharField(max_length=50, default='pdf')
    version = models.CharField(max_length=20, default='1.0.0')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
