# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# import default django-user model
from django.contrib.auth.models import User

# import signals
from django.db.models.signals import post_save

# Create your models here.

	# function to define directory of profile pictures
def profile_picture_directory( instance, filename ):
	# 'users/uploads/account_pic/%Y-%m-%d/'
	path = 'users/account_images/user_{0}/{1}'.format( instance.user.id, filename )
	return path

# model[ profile ]: get extra information to be added to the default User-model
class ProfileModel( models.Model ):
	user = models.OneToOneField( User, primary_key=True,
	                            on_delete=models.CASCADE, related_name='user' )
	pic = models.ImageField( upload_to=profile_picture_directory,
	                        blank=True, default='', max_length=300,
	                        verbose_name='Profile Picture' )

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

	bio = models.TextField(  default='', blank=True, max_length=140,
	verbose_name='Biography' )

	def save( self, *args, **kwargs ):
			# do something
		if self.pic.name and len(self.pic.name) > 0:
			

			orginal_filename = self.pic.name
			orginal_filename = orginal_filename.lower()
			orginal_filename = orginal_filename.split('.')
			extension = orginal_filename[1]

			user_id = self.user.id

			user_name = self.user.username
			user_name = user_name.upper()

			mpya_filename = '{0}-{1}.{2}'.format( user_id, user_name, extension )

			self.pic.name = mpya_filename
			#print( '\n\tNew filename: {0} .**'.format( self.pic.name ) )
		else:
			#print('\tNo Filename present yet')
			pass

			# call the 'real' save() method
		super().save( *args, **kwargs )

	def _save_FIELD_file( self, field, filename, raw_contents, save=True ):
		filename = '{0}_{1}_{2}'.format( self.user.id, self.user.username, filename )
		print( '\tNew Image Name: \n\t -> {0} * *'.format(filename)  )
		super( ProfileModel, self )._save_FIELD_file( field, filename, raw_contents, save )
		# NB!! function not working - check on it

# :: ensures that ProfileModel-object is created, when a User-model-object is created
def create_account( sender, **kwargs ):
	user = kwargs[ "instance" ]
	if kwargs["created"]:
		ProfileModel.objects.get_or_create( user=user )
		user_account = ProfileModel( user=user )
		user_account.save()

post_save.connect( create_account, sender=User )
