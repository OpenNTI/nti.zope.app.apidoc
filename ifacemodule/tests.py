##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Tests for the Interface Documentation Module

$Id: tests.py,v 1.1 2004/02/19 20:46:41 philikon Exp $
"""
import unittest
from zope.app import zapi
from zope.app.interfaces.traversing import IContainmentRoot
from zope.app.location import LocationProxy
from zope.app.tests import placelesssetup
from zope.interface import implements
from zope.app.apidoc.ifacemodule import IInterfaceModule
from zope.app.apidoc.interfaces import IDocumentationModule
from zope.testing.doctestunit import DocTestSuite


def setUp():
    placelesssetup.setUp()
    service = zapi.getService(None, 'Interfaces')
    service.provideInterface(None, IDocumentationModule)
    service.provideInterface('IInterfaceModule', IInterfaceModule)

def tearDown():
    placelesssetup.tearDown()


class Root:
    implements(IContainmentRoot)

    __parent__ = None
    __name__ = ''

def rootLocation(obj, name):
    return LocationProxy(obj, Root(), name)
    
def test_suite():
    return unittest.TestSuite((
        DocTestSuite('zope.app.apidoc.ifacemodule'),
        DocTestSuite('zope.app.apidoc.ifacemodule.menu'),
        ))

if __name__ == '__main__':
    unittest.main()
