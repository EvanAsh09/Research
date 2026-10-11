from django.db import models


class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ("Towels", "Towels"),
        ("Toiletries", "Toiletries"),
        ("Sheets", "New Sheets"),
        ("Cleaning", "Room Cleaning"),
        ("Room Service", "Room Service"),
    ]

    STATUS_CHOICES = [
        ("Received", "Received"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    guest_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    request_type = models.CharField(max_length=30, choices=REQUEST_TYPES)
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Received",
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_number} - {self.request_type}"