# Generated by Django 2.0.8 on 2018-09-11 20:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('sf_body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('person', wagtail.core.blocks.StructBlock([('first_name', wagtail.core.blocks.CharBlock()), ('surname', wagtail.core.blocks.CharBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('biography', wagtail.core.blocks.RichTextBlock())], icon='user'))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
