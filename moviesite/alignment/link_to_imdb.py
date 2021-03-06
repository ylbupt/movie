# -*- coding:utf-8 -*-
import os, sys, traceback
sys.path.append("../")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviesite.settings")
from django.conf import settings
from main.models import Movie,Link
from alignment.models import LinkReview
import django.db.utils, django
django.setup()
def record_to_db(link, movie):
    try:
        a_review = LinkReview.objects.get(linkid=link, mid=movie)
    except LinkReview.DoesNotExist:
        try:
            l = LinkReview(linkid=link, mid=movie)
            l.save()
            pass
        except django.db.utils.IntegrityError, e:
            print "linkid %d to mid %d exist %s" % (link.pk, movie.mid, e)

def record_auto_pass(link, movie):
    try:
        link.mid = movie.mid
        link.save()
        print "auto pass linkid %d to mid %d success!" % (link.pk, movie.mid)
    except Exception, e:
        print "auto pass linkid %d to mid %d failed! %s" % (link.pk, movie.mid, e)

if __name__ == "__main__":
    succ_item = 0
    auto_succ_item = 0
    links = Link.objects.filter(mid=0)
    moives = Movie.objects.all()
    for link in links:
        succ_flag = False
        auto_succ_flag = False
        cname_list = link.cname.strip().split('/')
        for i in range(0,len(cname_list)):
            cname_list[i] = cname_list[i].strip()
        ename_list = link.ename.strip().split('/')
        for i in range(0,len(ename_list)):
            ename_list[i] = ename_list[i].strip()
        title_list = link.title.strip().replace('[',' ').replace(']',' ').replace('【'.decode("utf-8"),' ').replace('】'.decode("utf-8"),' ').replace('/',' ').split()

        for movie in moives:
            if movie.cname.strip() in cname_list:
                #print movie.cname + "\n" + link.title + "\n\n"
                record_auto_pass(link=link, movie=movie)
                auto_succ_flag = True
                break
            elif movie.ename.strip() in ename_list:
                #print movie.cname + "\n" + link.title + "\n\n"
                record_auto_pass(link=link, movie=movie)
                auto_succ_flag = True
                break
            elif movie.cname.strip() in title_list:
                #print movie.cname + "\n" + link.title + "\n\n"
                record_auto_pass(link=link, movie=movie)
                auto_succ_flag = True
                break
            elif link.cname.find(movie.cname.strip()) != -1:
                #print movie.cname + "\n" + link.title + "\n\n"
                record_to_db(link=link, movie=movie)
                succ_flag = True
                break
            elif link.title.find(movie.cname.strip()) != -1:
                #print movie.cname + "\n" + link.title + "\n\n"
                record_to_db(link=link, movie=movie)
                succ_flag = True
                break
            elif link.title.lower().find(movie.ename.strip().lower()) != -1:
                #print movie.cname + "\n" + link.title + "\n\n"
                record_to_db(link=link, movie=movie)
                succ_flag = True
                break
        if succ_flag == True:
            succ_item = succ_item + 1
        if auto_succ_flag == True:
            auto_succ_item = auto_succ_item + 1
        else:
            print link.title.encode("utf-8")
            pass
    print "[Obsever][auto success %d][success %d][fail %d]\n" % (auto_item, succ_item,len(links) - succ_item - auto_item)
