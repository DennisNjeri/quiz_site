from __future__ import unicode_literals

from django.db import models




# Create your models here.
def study( instance, filename ):
	
	path = 'study/'.format( filename )
	return path
class PdfResources( models.Model ):
	
	pdf = models.FileField( upload_to=study,
	                        blank=True, default='', max_length=300,
	                        verbose_name='pdf_file' )

	ONE = 'ONE'
	TWO = 'TWO'
	THREE = 'THREE'
	FOUR = 'FOUR'
	FIVE = 'FIVE'
	SIX = 'SIX'
	SEVEN = 'SEVEN'
	EIGHT ='EIGHT'
	COLOR_CHOICES = (
	                 (ONE,'ONE'),
	                 (TWO,'TWO'),
	                 (THREE,'THREE'),
	                 (FOUR,'FOUR'),
	                 (FIVE,'FIVE'),
	                 (SIX, 'SIX'),
	                 (SEVEN,'SEVEN'),
	                 (EIGHT,'EIGHT')
	                 )

	Class = models.CharField( help_text='Enter the current class you are in',
	                                choices=COLOR_CHOICES, default=EIGHT, max_length=255 )

	subject = models.CharField(help_text='Enter the subject of the book',  default='', blank=True, max_length=140
	 )


	class Meta:
		db_table = "PdfResources"

class EResources( models.Model ):
	
	pdf = models.FileField(  )

	ONE = 'ONE'
	TWO = 'TWO'
	THREE = 'THREE'
	FOUR = 'FOUR'
	FIVE = 'FIVE'
	SIX = 'SIX'
	SEVEN = 'SEVEN'
	EIGHT ='EIGHT'
	COLOR_CHOICES = (
	                 (ONE,'ONE'),
	                 (TWO,'TWO'),
	                 (THREE,'THREE'),
	                 (FOUR,'FOUR'),
	                 (FIVE,'FIVE'),
	                 (SIX, 'SIX'),
	                 (SEVEN,'SEVEN'),
	                 (EIGHT,'EIGHT')
	                 )

	Class = models.CharField( help_text='Enter the current class you are in',
	                                choices=COLOR_CHOICES, default=EIGHT, max_length=255 )

	subject = models.CharField(help_text='Enter the subject of the book',  default='', blank=True, max_length=140
	 )


	class Meta:
		db_table = "EResources"