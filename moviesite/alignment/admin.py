# -*- coding:utf-8 -*-
from django.contrib import admin
from alignment.models import LinkReview, ImdbReview

class LinkReviewAdmin(admin.ModelAdmin):
    list_display = ('linkid', 'mid', 'create_time')
    ordering = ('-create_time', )
    actions = ('link_review_pass', )

    def link_review_pass(self, request, queryset):
        #item_num = queryset.update(mid='11111')
        for review in queryset:
            link = review.linkid
            link.mid = review.mid.mid
            link.save()
            review.delete()
            self.message_user(request, "%s映射记录成功审核通过." % link)

    link_review_pass.short_description = "审核通过".decode("utf-8")

class ImdbReviewAdmin(admin.ModelAdmin):
    list_display = ('imdbid', 'mid', 'create_time')
    ordering = ('-create_time', )
    actions = ('imdb_review_pass', )

    def imdb_review_pass(self, request, queryset):
        for review in queryset:
            imdb = review.imdbid
            imdb.mid = review.mid.mid
            imdb.save()
            review.delete()
            self.message_user(request, "%s映射记录成功审核通过." % imdb)

    imdb_review_pass.short_description = "审核通过".decode("utf-8")

admin.site.register(LinkReview, LinkReviewAdmin)
admin.site.register(ImdbReview, ImdbReviewAdmin)
