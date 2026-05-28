from django.contrib import admin
from .models import Contact, Skill, Project, Experience, Profile

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')
    
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'duration', 'description')
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('image','resume')
    