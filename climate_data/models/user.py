import uuid
from djongo import models

class UserEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=14)

    def __str__(self):
        return (
            f"UserEntity [ID: {self.id},
            First Name: {self.first_name},
            Last Name: {self.last_name},
            Location: {self.location},
            Username: {self.username},
            Password: {self.password}]"
        )

