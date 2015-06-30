"""This file contains default indexers registered for all objects which are
indexed by portal_catalog.

Other files in this folder can contain more specific indexers to override these.
"""

from Acquisition._Acquisition import aq_base
from plone.indexer import indexer
from zope.interface import Interface

from bika.lims import logger

# Dates acquired from schema fields
from bika.lims.utils import get_transition_info


@indexer(Interface)
def BatchDate(instance):
    if hasattr(instance, 'getBatchDate'):
        return instance.getBatchDate()


@indexer(Interface)
def SamplingDate(instance):
    if hasattr(instance, 'getSamplingDate'):
        return instance.getSamplingDate()


@indexer(Interface)
def DisposalDate(instance):
    if hasattr(instance, 'getDisposalDate'):
        return instance.getDisposalDate()


@indexer(Interface)
def ExpiryDate(instance):
    if hasattr(instance, 'getExpiryDate'):
        return instance.getExpiryDate()


@indexer(Interface)
def DueDate(instance):
    if hasattr(instance, 'getDueDate'):
        return instance.getDueDate()


@indexer(Interface)
def DateOpened(instance):
    if hasattr(instance, 'getDateOpened'):
        return instance.getDateOpened()


# Dates acquired from workflow:

@indexer(Interface)
def DateReceived(instance):
    return get_transition_info(instance, 'recieve', 'time')


@indexer(Interface)
def DateDisposed(instance):
    return get_transition_info(instance, 'dispose', 'time')


@indexer(Interface)
def DateExpired(instance):
    return get_transition_info(instance, 'expire', 'time')


@indexer(Interface)
def DatePublished(instance):
    return get_transition_info(instance, 'publish', 'time')


@indexer(Interface)
def DateSampled(instance):
    return get_transition_info(instance, 'sample', 'time')


# assorted shared indexes:

@indexer(Interface)
def Priority(instance):
    if hasattr(instance, 'getPriority'):
        priority = instance.getPriority()
        if priority:
            return priority.getSortKey()


@indexer(Interface)
def ParentUID(instance):
    if hasattr(instance, 'aq_parent'):
        return getattr(aq_base(instance.aq_parent), 'UID', None)


@indexer(Interface)
def Fullname(instance):
    if hasattr(instance, 'getFullname'):
        return instance.getFullname()


@indexer(Interface)
def Username(instance):
    if hasattr(instance, 'getUsername'):
        return instance.getUsername()


@indexer(Interface)
def Keyword(instance):
    if hasattr(instance, 'getKeyword'):
        return instance.getKeyword()


# populate FieldIndex versions of these:

@indexer(Interface)
def description(instance):
    if hasattr(instance, 'Description'):
        return instance.Description()


@indexer(Interface)
def title(instance):
    if hasattr(instance, 'Title'):
        return instance.Title()


# two separate (redundant?) indexes

@indexer(Interface)
def ServiceTitle(instance):
    if hasattr(instance, 'getService'):
        return instance.getService().Title()


@indexer(Interface)
def ServiceUID(instance):
    if hasattr(instance, 'getService'):
        return instance.getService().UID()


# two separate (redundant?) indexes

@indexer(Interface)
def CategoryTitle(instance):
    if hasattr(instance, 'getCategory'):
        return instance.getCategory().Title()
    elif hasattr(instance, 'getAnalysisCategory'):
        return instance.getAnalysisCategory().Title()


@indexer(Interface)
def CategoryUID(instance):
    if hasattr(instance, 'getCategory'):
        return instance.getCategory().UID()
    elif hasattr(instance, 'getAnalysisCategory'):
        return instance.getAnalysisCategory().UID()


# two separate (redundant?) indexes

@indexer(Interface)
def SamplePointTitle(instance):
    if hasattr(instance, 'getSamplePoint'):
        return instance.getSamplePoint().Title()


@indexer(Interface)
def SamplePointUID(instance):
    if hasattr(instance, 'getSamplePoint'):
        return instance.getSamplePoint().UID()


# two separate (redundant?) indexes

@indexer(Interface)
def SampleTypeTitle(instance):
    if hasattr(instance, 'getSampleType'):
        return instance.getSampleType().Title()


@indexer(Interface)
def SampleTypeUID(instance):
    if hasattr(instance, 'getSampleType'):
        return instance.getSampleType().UID()

# redundant? (should be using a single KeywordIndex).

@indexer(Interface)
def Analyst(instance):
    if hasattr(instance, 'getAnalyst'):
        return instance.getAnalyst()

@indexer(Interface)
def Analysts(instance):
    if hasattr(instance, 'getAnalysts'):
        return instance.getAnalysts()

@indexer(Interface)
def ClientTitle(instance):
    if hasattr(instance, 'getClient'):
        client = instance.getClient()
        if client:
            return client.Title()

@indexer(Interface)
def ClientUID(instance):
    if hasattr(instance, 'getClient'):
        client = instance.getClient()
        if client:
            return client.UID()

@indexer(Interface)
def ClientOrderNumber(instance):
    if hasattr(instance, 'getClientOrderNumber'):
        return instance.getClientOrderNumber()

@indexer(Interface)
def ClientReference(instance):
    if hasattr(instance, 'getClientReference'):
        return instance.getClientReference()

@indexer(Interface)
def ClientSampleID(instance):
    if hasattr(instance, 'getClientSampleID'):
        return instance.getClientSampleID()

@indexer(Interface)
def ContactTitle(instance):
    if hasattr(instance, 'getContactTitle'):
        return instance.getContactTitle()
    elif hasattr(instance, 'Contact'):
        contact = instance.getContact()
        if contact:
            return contact.Title()

