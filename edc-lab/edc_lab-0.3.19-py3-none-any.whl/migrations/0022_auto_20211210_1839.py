# Generated by Django 3.2.9 on 2021-12-10 15:39

from django.db import migrations
import edc_lab.models.aliquot
import edc_lab.models.box
import edc_lab.models.box_item
import edc_lab.models.box_type
import edc_lab.models.manifest.manifest
import edc_lab.models.order
import edc_lab.models.panel
import edc_lab.models.result
import edc_lab.models.result_item
import edc_sites.models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_lab', '0021_auto_20200513_0034'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='aliquot',
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_lab.models.aliquot.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='box',
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_lab.models.box.BoxManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='boxitem',
            managers=[
                ('objects', edc_lab.models.box_item.BoxItemManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='boxtype',
            managers=[
                ('objects', edc_lab.models.box_type.BoxTypeManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='manifest',
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_lab.models.manifest.manifest.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='order',
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_lab.models.order.OrderManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='panel',
            managers=[
                ('objects', edc_lab.models.panel.PanelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='result',
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_lab.models.result.ResultManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='resultitem',
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_lab.models.result_item.ResultItemManager()),
            ],
        ),
    ]
