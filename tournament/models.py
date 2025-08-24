from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Player(models.Model):
    ROLE_CHOICES = [
        ('player', 'Player'),
        ('coach', 'Coach'),
    ]
    
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('unavailable', 'Unavailable'),
    ]
    
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=1200)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='player')
    availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES, default='available')
    profile_img = models.ImageField(upload_to='profiles/', blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)  # For coaches
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.role})"
    
    class Meta:
        ordering = ['-rating']

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    document = models.FileField(upload_to='tournaments/docs/', blank=True, null=True)
    image = models.ImageField(upload_to='tournaments/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tournament_detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date']

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_snippet(self):
        return self.content[:150] + "..." if len(self.content) > 150 else self.content
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "News"

class Message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.sender}"
    
    class Meta:
        ordering = ['-created_at']

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='admin_avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"