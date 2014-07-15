from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    name = models.CharField(_(u"Name"), max_length=140)


class Blog(models.Model):
    name = models.CharField(_(u"Name"), max_length=140)


class Post(models.Model):
    author = models.ForeignKey(
        Author,
        verbose_name=_('Author'),
    )
    blog = models.ForeignKey(
        Blog,
        verbose_name=_('Blog'),
    )
    name = models.CharField(_(u"Name"), max_length=140)
    content = models.TextField(_("Content"))
