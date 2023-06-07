from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Theme(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a theme (e.g. Entertainment)')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class subtheme_I(models.Model):
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class subtheme_V(models.Model):
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class subtheme_A(models.Model):
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Image(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    url = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE) 
    subtheme = models.ForeignKey(subtheme_I,on_delete=models.CASCADE)
    caption = models.TextField(max_length=1000, help_text='Enter a caption to be displayed with the image')
    caption_french = models.TextField(max_length=1000,blank=True, default='', help_text='Enter a caption to be displayed with the image')


class Video(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    url = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    subtheme = models.ForeignKey(subtheme_V,on_delete=models.CASCADE)
    caption = models.TextField(max_length=1000, help_text='Enter a caption to be displayed with the image')
    caption_french = models.TextField(max_length=1000,blank=True, default='', help_text='Enter a caption to be displayed with the image')

class Audio(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    url = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    subtheme = models.ForeignKey(subtheme_A,on_delete=models.CASCADE)
    caption = models.TextField(max_length=1000, help_text='Enter a caption to be displayed with the image')
    caption_french = models.TextField(max_length=1000,blank=True, default='', help_text='Enter a caption to be displayed with the image')




# Create your models here.
