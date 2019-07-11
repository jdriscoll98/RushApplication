from django.db import models

# This will contain all the information about the rushee  #

class Rushee(models.Model):
    GRADES = [
        ("FRESHMAN", "FR"),
        ("SOPHOMORE", "SO"),
        ("JUNIOR", "JR"),
        ("SENIOR", "SR"),
        ]

    STATUS = [
        ("FIRST", "Main Floor"),
        ("SECOND", "Upstairs"),
        ("ACCEPTED", "Accepted"),
        ("HOLDING", "Holding"),
        ("DENIED", "Denied"),
    ]
    name = models.CharField(max_length=100, unique=True)
    grade = models.CharField(max_length=100, choices=GRADES)
    phone_number = models.IntegerField()
    currently_talking_to = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(max_length=500, blank=True, null=True)
    total_score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.name
