# -*- coding: utf-8 -*-
from django.db import models
#from djorm_pgarray.fields import ArrayField # http://www.niwi.be/2012/10/07/postgresql-array-fields-with-django/
import uuid
import datetime
def make_uuid():
    return str(uuid.uuid4())


class Metadata(models.Model):
    LAYER_TYPES = (
        ('WMS', 'Web Map Service'),
        ('WMST', 'Web Map TileService'),
        ('WMSC', 'WMS-C'),
    )
    FEATURES_TYPES = (
        ('SS', 'SpatialSuite'),
        ('GS10', 'Geoserver WFS 1.0'),

    )
    fileidentifier = models.CharField(max_length=36, primary_key=True, default=make_uuid, editable=False)
    title = models.CharField('Ressourcetitel',max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    abstract = models.TextField('Ressourceresumé',max_length=10000,null=True, blank=True)
    purpose  = models.CharField('Ressourceformål',max_length=200,null=True, blank=True)
    type = models.CharField('Ressourcetype',max_length=200,null=True, blank=True)
    language = models.CharField(max_length=3,null=True, blank=True, default='dan')
    topiccategorycode = models.CharField('Emnekategori',max_length=200,null=True, blank=True)
    descriptivekeywords = models.CharField('Nøgleord',max_length=200,null=True, blank=True)
    responsibleparty_organisationname = models.CharField('Organisation',max_length=200,null=True, blank=True)
    responsibleparty_individualname = models.CharField('Kontaktperson',max_length=200,null=True, blank=True)
    responsibleparty_positionname = models.CharField('Position',max_length=200,null=True, blank=True)
    contactinfo_telephone = models.CharField('Telefon',max_length=200,null=True, blank=True)
    address_deliverypoint = models.CharField('Adresse',max_length=200,null=True, blank=True)
    address_city = models.CharField('By',max_length=200,null=True, blank=True)
    address_postalcode = models.CharField('Postnummer',max_length=200,null=True, blank=True)
    address_country = models.CharField(max_length=36, default='Denmark', editable=False)
    electronicmailaddress = models.EmailField('e-mail',max_length=200)
    created = models.DateTimeField('Oprettet', default=datetime.datetime.now) # maybe datetime.datetime.now as default ?
    updated = models.DateTimeField('Opdateret',auto_now=False)
    beginposition = models.DateField('gældende fra')
    endposition = models.DateField('gældende til')
    accessconstraints = models.TextField('Betingelser for adgang og brug',max_length=200,null=True, blank=True)
    useconstraints = models.TextField('Begrænsninger på offentlig adgang',max_length=200,null=True, blank=True)
   # otherconstraints = models.CharField(max_length=200,null=True, blank=True)
    search_string = models.CharField(max_length=100000,null=True, blank=True)
    class Meta:
        ordering = ['title']
        
        verbose_name = "metadata"
        verbose_name_plural = "metadatasæt"
    def __unicode__(self):
        return self.title