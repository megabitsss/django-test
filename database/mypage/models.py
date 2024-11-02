from django.db import models

# Create your models here.
class creativereser(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    event_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_id} {self.name} {self.event_date}"
    
class peerone(models.Model):
    student_id_peer1 = models.IntegerField()
    name_peer1 = models.CharField(max_length=100)
    event_date_peer1 = models.DateTimeField()

    def __str__(self):
        return f"{self.student_id_peer1} {self.name_peer1} {self.event_date_peer1}"