from django.db import models
from django.urls import reverse

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
    total_score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='FIRST')

    def __str__(self):
        return self.name


class Comment(models.Model):
    brother = models.CharField(max_length=100)
    comment = models.TextField(max_length=300)
    rushee = models.ForeignKey(Rushee, on_delete=models.CASCADE)

    def __str__(self):
        return "Comment for " + str(self.rushee.name)

    def get_absolute_url(self):
        return reverse("website:rushee_detail", kwargs={'pk': self.rushee.pk})
