# ml_app/models.py

from django.db import models

class MLModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    trained_model_path = models.FileField(upload_to='ml_models/')
    training_data_path = models.FileField(upload_to='training_data/')
    evaluation_metrics = models.JSONField()

    def __str__(self):
        return self.name
