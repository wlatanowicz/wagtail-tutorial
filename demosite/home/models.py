from django.db import models
from wagtail.core import blocks

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.api import APIField
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    api_fields = [
        APIField('body'),
    ]


class AnotherPage(Page):
    sf_body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('person', blocks.StructBlock([
            ('first_name', blocks.CharBlock()),
            ('surname', blocks.CharBlock()),
            ('photo', ImageChooserBlock(required=False)),
            ('biography', blocks.RichTextBlock()),
        ], icon='user'))
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sf_body'),
    ]

    api_fields = [
        APIField('sf_body'),
    ]
