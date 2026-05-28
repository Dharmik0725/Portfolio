from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Creative Tools'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='frontend')

    def __str__(self):
        return f"{self.name} ({self.category})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Requires Pillow (pip install Pillow)
    image = models.ImageField(upload_to='projects/', blank=True, null=True) 
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"
    

class Profile(models.Model):
    # This will store the image in media/profile/
    image = models.ImageField(upload_to='profile/')
    
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, help_text="Upload your PDF resume here.")
    
    def __str__(self):
        return "My Profile"