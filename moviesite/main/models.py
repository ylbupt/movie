from django.db import models

# Create your models here.
class Movie(models.Model):
    mid = models.BigIntegerField(unique=True,db_index=True)
    pic_url = models.URLField()
    cname = models.CharField(max_length=100)
    ename = models.CharField(max_length=100)
    actors = models.TextField()
    actors_links = models.TextField()
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    runtime = models.CharField(max_length=100)

    channel  = models.IntegerField(default=0)
    date = models.BigIntegerField() 
    rate = models.IntegerField() 
    votes = models.BigIntegerField() 
    imdb_id = models.BigIntegerField()
    imdb_link  = models.URLField()
    imdb_box  = models.IntegerField()
    imdb_rate  = models.IntegerField()
    comment_link = models.URLField()
    douban_link = models.URLField()
    comment_link = models.URLField()
    summary = models.TextField()
    found_date = models.BigIntegerField()
    links = []
    def __unicode__(self):
        return u'%s %s' % (self.mid, self.cname)

class Imdb(models.Model):
    mid = models.BigIntegerField(unique=True,db_index=True)
    douban_id = models.BigIntegerField(default=0) 
    url = models.URLField()
    pic_url = models.URLField()
    ename = models.CharField(max_length=100)
    actors = models.TextField()
    actors_links = models.TextField()
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    runtime = models.CharField(max_length=100)
    date = models.BigIntegerField() 
    rate = models.IntegerField(default=0) 
    votes = models.BigIntegerField(default=0) 
    box  = models.IntegerField(default=0)
    found_date = models.BigIntegerField()
    def __unicode__(self):
        return u'%s %s' % (self.mid, self.ename)

class Link(models.Model):
    #mid = models.ForeignKey('Movie')
    mid = models.BigIntegerField(db_index=True)
    urlmd5 = models.CharField(max_length=32,db_index=True,unique=True)
    url = models.URLField()
    title = models.CharField(max_length=255)
    cname = models.CharField(max_length=100)
    ename = models.CharField(max_length=100)
    actors = models.TextField()
    director = models.CharField(max_length=100)
    date = models.BigIntegerField(default=0) 
    content = models.CharField(max_length=1000)
    found_date = models.BigIntegerField()
    def __unicode__(self):
        return u'%s %s' % (self.pk, self.title)

