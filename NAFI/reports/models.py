from django.db import models

class ReportType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Report(models.Model):
    title = models.CharField(max_length=255)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
