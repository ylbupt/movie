# -*- coding:utf-8 -*-
import os, sys, traceback
sys.path.append("../")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviesite.settings")
from django.conf import settings
from main.models import Movie,Imdb
from alignment.models import ImdbReview
import django.db.utils, django
django.setup()
def record_to_db(imdb, movie):
    try:
        a_review = ImdbReview.objects.get(imdbid=imdb, mid=movie)
    except ImdbReview.DoesNotExist:
        try:
            i = ImdbReview(imdbid=imdb, mid=movie)
            i.save()
            pass
        except django.db.utils.IntegrityError, e:
            print "imdbid %d to mid %d exist %s" % (imdb.pk, movie.mid, e)

if __name__ == "__main__":
    succ_item = 0
    imdbs = Imdb.objects.filter(douban_id=0)
    moives = Movie.objects.all()
    for imdb in imdbs:
        succ_flag = False
        ename_list = imdb.ename.strip().split('/')
        for i in range(0,len(ename_list)):
            ename_list[i] = ename_list[i].strip()

        for movie in moives:
            if movie.ename.strip() in ename_list:
                #print movie.cname + "\n" + imdb.ename + "\n\n"
                record_to_db(imdb=imdb, movie=movie)
                succ_flag = True
                break
        if succ_flag != True:
            print imdb.ename.encode("utf-8")
            pass
        else:
            succ_item = succ_item + 1
    print "[Obsever][success %d][fail %d]\n" % (succ_item,len(imdbs) - succ_item)
