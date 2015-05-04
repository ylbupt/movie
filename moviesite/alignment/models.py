from django.db import models
from main.models import Movie,Link,Imdb

# Create your models here.
class LinkReview(models.Model):
    #linkid = models.BigIntegerField() 
    #mid = models.BigIntegerField()
    linkid = models.ForeignKey(Link, db_column="linkid") 
    mid = models.ForeignKey(Movie, to_field="mid", db_column="mid") 
    create_time = models.DateTimeField() 
    def __unicode__(self):
        return u'%s -------> %s' % (self.linkid, self.mid)

class ImdbReview(models.Model):
    imdbid = models.ForeignKey(Imdb, db_column="imdbid") 
    mid = models.ForeignKey(Movie, to_field="mid", db_column="mid") 
    create_time = models.DateTimeField() 
    def __unicode__(self):
        return u'%s -------> %s' % (self.imdbid, self.mid)
