from django.db import models 
 
 
class Todo(models.Model): 
    todo = models.CharField('ToDo', max_length=100, blank=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)
    
    def __str__(self):
        return self.todo