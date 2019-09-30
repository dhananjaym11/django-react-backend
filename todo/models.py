from django.db import models

# Create your models here.
class Todo(models.Model):
      name = models.CharField(max_length=30)
      age = models.CharField(max_length=10)

      def _str_(self):
        return self.name