from Acquisition import aq_inner
from Acquisition import aq_parent
from bika.lims.permissions import *
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName
from zExceptions import BadRequest


def upgrade(tool):
    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup
    typestool = getToolByName(portal, 'portal_types')

    # update affected tools
    setup.runImportStepFromProfile('profile-bika.lims:default', 'typeinfo')
    setup.runImportStepFromProfile('profile-bika.lims:default', 'workflow')

    # Add the SupplyOrderFolder /supplyorders
    try:
        typestool.constructContent(type_name="SupplyOrderFolder",
                               container=portal,
                               id='supplyorders',
                               title='Supply Orders')
        obj = portal['supplyorders']
        obj.unmarkCreationFlag()
        obj.reindexObject()
    except BadRequest:
        # folder already exists
        pass

    # /supplyorders folder permissions
    mp = portal.supplyorders.manage_permission
    mp(permissions.ListFolderContents, ['Manager', 'LabManager', 'LabClerk', ], 0)
    mp(permissions.View, ['Manager', 'LabManager', 'LabClerk'], 0)
    mp('Access contents information', ['Manager', 'LabManager', 'LabClerk'], 0)
    portal.supplyorders.reindexObject()

    return True