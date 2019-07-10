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
        ("FIRST", "1"),
        ("SECOND", "2"),
        ("BID_ROOM", "BID"),
        ("ACCEPTED", "A"),
        ("HOLDING", "H"),
        ("DENIED", "D"),
    ]
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True)
    grade = models.CharField(max_length=2, choices=GRADES)
    phone_number = models.IntegerField(default=0)
    brothers_known = models.CharField(max_length=300, blank=True, null=True)
    total_score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS)
