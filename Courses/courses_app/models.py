from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)
    imgpath = models.CharField(max_length=64, default="", editable=False)

    def __str__(self):
        return str(self.name)

class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    logo = models.TextField()

    def __str__(self):
        return str(self.name)


class Branch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="Branches")
    latitude = models.TextField()
    longitude = models.TextField()
    address = models.TextField()

    def __str__(self):
        return str(self.address)

class ContactValue(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="Contacts")
    type = models.IntegerField()
    value = models.ForeignKey(ContactValue, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type)
