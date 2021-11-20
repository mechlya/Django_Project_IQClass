from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
# Create your models here.

def image_upload(instance, filename):
    imagename, extenstion = filename.split(".")
    return "course-list/%s.%s"%(instance.id, extenstion)


SKILL_CHOICES = (
    ('Beginner ', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
   
)

CERTIFICATE_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
   
)



class Course(models.Model): # Table 

    
    title = models.CharField(max_length= 100)  # column 
    description = models.TextField(max_length= 2000)
    details = models.TextField(max_length= 2000)
    published_at =  models.DateTimeField(auto_now= True)
    price_previou = models.IntegerField(default=1)
    price_now = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null= True)

    #Add 
    days = models.IntegerField(default=1)
    duration = models.IntegerField(default=1)
    certification = models.CharField(max_length=15, choices = CERTIFICATE_CHOICES)
    skill = models.CharField(max_length=15, choices = SKILL_CHOICES)
    when = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course,self).save(*args, **kwargs)

    def __str__(self):
    	return self.title

class Category( models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name