from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=40, verbose_name='ИМЯ')

    last_name = models.CharField(max_length=60, blank=True)
    age = models.PositiveSmallIntegerField(null=True)
    email = models.EmailField(primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} -> {self.name}'

class ToDo(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='todos')
    task = models.TextField()

    def __str__(self):
        return self.task
class Category(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        Tag
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.title} ... {self.body}'
