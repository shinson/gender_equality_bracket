from django.db import models
from django.utils.encoding import smart_unicode

class Nickname(models.Model):
	abbrev = models.CharField(max_length=25, default = 'None')
	
	def __unicode__(self):
		return smart_unicode(self.abbrev)


class Team(models.Model):
	name = models.CharField(max_length=150, default = 'None')
	abbrev = models.ForeignKey(Nickname)
	def __unicode__(self):
		return smart_unicode(self.name)
		

class TeamStat(models.Model):
	name = models.ForeignKey(Team)
	EAST = 'East'
	WEST = 'West'
	SOUTH = 'South'
	MIDWEST = 'Midwest'
	region_choices = (
		(EAST, 'East'), 
		(WEST,  'West'), 
		(SOUTH, 'South'),
		(MIDWEST, 'Midwest'),
	)
	region = models.CharField(max_length=7, choices=region_choices, default = 'West')
	abbrev = models.ForeignKey(Nickname)
	rank = models.IntegerField(max_length=5, null=False, blank=False)
	magic_no = models.FloatField(max_length=5, null=False, blank=False)
	female_bb_rate = models.IntegerField(max_length=5, null=False, blank=False)
	male_bb_rate = models.IntegerField(max_length=5, null=False, blank=False)
	female_grad_rate = models.IntegerField(max_length=5, null=False, blank=False)
	male_grad_rate= models.IntegerField(max_length=5, null=False, blank=False)
	female_stem_rate= models.FloatField(max_length=5, null=False, blank=False)
	male_stem_rate= models.FloatField(max_length=5, null=False, blank=False)
	female_admin_rate= models.IntegerField(max_length=5, null=False, blank=False)
	male_admin_rate= models.IntegerField(max_length=5, null=False, blank=False)
	
	def __unicode__(self):
		return smart_unicode(self.name)
	
	
