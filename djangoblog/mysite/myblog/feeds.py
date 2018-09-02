from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post


class LatestPostFeed(Feed):
    title = "Latest Posts"
    link = "/latest/feed/"
    description = "Newest posts."

    def items(self):
        return Post.objects.all().order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
       return self.link