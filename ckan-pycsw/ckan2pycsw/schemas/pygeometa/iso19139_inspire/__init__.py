# =================================================================
# Adapt to ISO INSPIRE 19139 from Tom Kralidis code
# Copyright (c) 2022 Tom Kralidis
# =================================================================
# inbuilt libraries
import ast
import logging
import os
from typing import Union
from lxml import etree

# third-party libraries
from owslib.iso import CI_OnlineResource, CI_ResponsibleParty, MD_Metadata
from pygeometa.schemas.base import BaseOutputSchema

# custom functions
from model.template import render_j2_template


LOGGER = logging.getLogger(__name__)
THISDIR = os.path.dirname(os.path.realpath(__file__))


class ISO19139_inspireOutputSchema(BaseOutputSchema):
    """ISO 19139 - INSPIRE output schema"""

    def __init__(self):
        """
        Initialize object

        :returns: pygeometa.schemas.base.BaseOutputSchema
        """

        super().__init__('iso19139_inspire', 'xml', THISDIR)

    def write(self, mcf: dict, stringify: str = True, mappings_folder: str = 'ckan2pycsw/mappings/iso19139_inspire') -> Union[dict, str]:
        """
        Write outputschema to string buffer

        :param mcf: dict of MCF content model
        :param stringify: whether to return a string representation (default)
                          else native (dict, etree)

        :returns: `dict` or `str` of metadata in outputschema representation
        """

        LOGGER.debug('Writing INSPIRE ISO19139 metadata')
        #mappings_folder = f"{mappings_folder}/iso19139_inspire"
        if stringify:
            return render_j2_template(mcf=mcf, schema_type="pygeometa", template_dir=self.template_dir, mappings_folder=mappings_folder)

        return mcf

    def import_(self, metadata: str) -> dict:
        """
        Import metadata into MCF

        :param metadata: string of metadata content

        :returns: `dict` of MCF content
        """

        mcf = {
            'mcf': {
                'version': '1.0',
            },
            'metadata': {},
            'identification': {},
            'contact': {},
            'distribution': {}
        }

        LOGGER.debug('Parsing ISO metadata')
        try:
            m = MD_Metadata(etree.fromstring(metadata))
        except ValueError:
            m = MD_Metadata(etree.fromstring(bytes(metadata, 'utf-8')))

        LOGGER.debug('Setting metadata')
        mcf['metadata']['identifier'] = m.identifier

        mcf['metadata']['hierarchylevel'] = m.hierarchy
        mcf['metadata']['datestamp'] = m.datestamp

        LOGGER.debug('Setting identification')
        mcf['identification']['title'] = m.identification.title
        mcf['identification']['abstract'] = m.identification.abstract

        if m.identification.date:
            mcf['identification']['dates'] = {}
            for date_ in m.identification.date:
                mcf['identification']['dates'][date_.type] = date_.date

        if m.identification.keywords2:
            mcf['identification']['keywords'] = {}
            for count, value in enumerate(m.identification.keywords2):
                key = f'keywords-{count}'
                mcf['identification']['keywords'][key] = {
                    'type': value.type,
                    'keywords': value.keywords
                }
        mcf['identification']['topiccategory'] = m.identification.topiccategory  # noqa

        mcf['identification']['extents'] = {
            'spatial': [{
                'bbox': [
                    ast.literal_eval(m.identification.extent.boundingBox.minx),
                    ast.literal_eval(m.identification.extent.boundingBox.miny),
                    ast.literal_eval(m.identification.extent.boundingBox.maxx),
                    ast.literal_eval(m.identification.extent.boundingBox.maxy)
                ]
            }],
            'temporal': []
        }

        temp_extent = {}
        if m.identification.temporalextent_start:
            temp_extent['begin'] = m.identification.temporalextent_start
        if m.identification.temporalextent_end:
            temp_extent['end'] = m.identification.temporalextent_end

        mcf['identification']['extents']['temporal'].append(temp_extent)

        if m.identification.accessconstraints:
            mcf['identification']['accessconstraints'] = m.identification.accessconstraints[0]  # noqa

        mcf['identification']['status'] = m.identification.status

        LOGGER.debug('Setting contact')
        if m.contact:
            for c in m.contact:
                mcf['contact'].update(get_contact(c))

        if m.distribution.distributor:
            for d in m.distribution.distributor:
                mcf['contact'].update(get_contact(d.contact))

        LOGGER.debug('Setting distribution')
        if m.distribution:
            for count, value in enumerate(m.distribution.online):
                key = f'link-{count}'
                mcf['distribution'][key] = get_link(value)

        return mcf


def get_contact(contact: CI_ResponsibleParty) -> dict:
    """
    Generates an MCF contact from an OWSLib contact

    :param contact: OWSLib `CI_ResponsibleParty` object

    :returns: dict of MCF contact
    """

    mcf_contact = {contact.role: {}}

    cm_lookup = {
        'organization': 'organization',
        'individualname': 'name',
        'positionname': 'position',
        'phone': 'phone',
        'fax': 'fax',
        'address': 'address',
        'city': 'city',
        'administrativearea': 'region',
        'postalcode': 'postcode',
        'country': 'country',
        'email': 'email'
    }

    for key, value in cm_lookup.items():
        if hasattr(contact, value):
            mcf_contact[contact.role][key] = getattr(contact, value)

    if hasattr(contact.onlineresource, 'url'):
        mcf_contact[contact.role]['url'] = contact.onlineresource.url

    return mcf_contact


def get_link(link: CI_OnlineResource) -> dict:
    """
    Generates an MCF link from an OWSLib distribution URL

    :param contact: OWSLib `CI_OnlineResource` object

    :returns: dict of MCF link
    """

    mcf_link = {
        'url': link.url,
        'type': link.protocol,
        'name': link.name,
        'description': link.description,
        'function': link.function
    }

    return mcf_link
