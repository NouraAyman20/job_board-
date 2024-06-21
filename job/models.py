from collections import UserDict
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
JOB_TYPE =(
  ('Full Time' , 'full time'),
  ('Part Time' , 'part time'),
)

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s/%s.%s"%(instance.id,instance.id, extension)

class Job(models.Model) :
  owner =models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
  title=models.CharField(max_length=100)
  job_type =models.CharField(max_length=100 , choices=JOB_TYPE ,default='Full Time')  
  desciption = models.TextField(max_length=1000 ,default='' ) 
  published_at = models.DateTimeField(auto_now=True)
  vacancy = models.IntegerField(default=0)
  salary=models.IntegerField(default=0) 
  experience =models.IntegerField(default=1)
  Category =models.ForeignKey('Category' ,on_delete=models.CASCADE)
  image = models.ImageField(upload_to=image_upload)
  slug = models.SlugField(unique=True, blank=True, null=True)
  
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Job, self).save(*args, **kwargs)
  
  def __str__(self):
    return self.title
   
class  Category(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self):
      return self.name 
    
    
    
class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=200, blank=True, null=True)
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
  
  
  
       
    
  
  
  