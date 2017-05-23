##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Class representation for code browser
"""

__docformat__ = 'restructuredtext'

from inspect import ismethod, ismethoddescriptor

from zope.interface import implementer, implementedBy
from zope.security.checker import getCheckerForInstancesOf
from zope.location.interfaces import ILocation

from zope.app.apidoc.classregistry import classRegistry
from zope.app.apidoc.utilities import getInterfaceForAttribute
from zope.app.apidoc.utilities import getPublicAttributes
from zope.app.apidoc.codemodule.interfaces import IClassDocumentation


@implementer(ILocation, IClassDocumentation)
class Class(object):
    """This class represents a class declared in the module."""

    def __init__(self, module, name, klass):
        self.__parent__ = module
        self.__name__ = name
        self.__klass = klass

        # Setup interfaces that are implemented by this class.
        self.__interfaces = tuple(implementedBy(klass))
        self.__all_ifaces = tuple(implementedBy(klass).flattened())

        # Register the class with the global class registry.
        classRegistry[self.getPath()] = klass

    def getPath(self):
        """See IClassDocumentation."""
        return self.__parent__.getPath() + '.' + self.__name__

    def getDocString(self):
        """See IClassDocumentation."""
        return self.__klass.__doc__

    def getBases(self):
        """See IClassDocumentation."""
        return self.__klass.__bases__

    def getKnownSubclasses(self):
        """See IClassDocumentation."""
        return [k for n, k in classRegistry.getSubclassesOf(self.__klass)]

    def getInterfaces(self):
        """See IClassDocumentation."""
        return self.__interfaces

    def _iterAllAttributes(self):
        for name in getPublicAttributes(self.__klass):
            iface = getInterfaceForAttribute(
                    name, self.__all_ifaces, asPath=False)
            yield name, getattr(self.__klass, name), iface

    if str is bytes:
        # Python 2
        def _ismethod(self, obj):
            return ismethod(obj)
    else:
        # On Python 3, there is no unbound method.
        # we treat everything that's callable as a method.
        # The corner case is where we bind a C
        # function to an attribute; it's not *technically* a method,
        # but it acts just like a @staticmethod, so it works out
        # the same
        _ismethod = callable

    def getAttributes(self):
        """See IClassDocumentation."""
        return [(name, obj, iface)
                for name, obj, iface in self._iterAllAttributes()
                if not self._ismethod(obj) and not ismethoddescriptor(obj)]

    def getMethods(self):
        """See IClassDocumentation."""
        return [(name, obj, iface)
                for name, obj, iface in self._iterAllAttributes()
                if self._ismethod(obj)]

    def getMethodDescriptors(self):
        return [(name, obj, iface)
                for name, obj, iface in self._iterAllAttributes()
                if ismethoddescriptor(obj)]

    def getSecurityChecker(self):
        """See IClassDocumentation."""
        return getCheckerForInstancesOf(self.__klass)

    def getConstructor(self):
        """See IClassDocumentation."""
        init = getattr(self.__klass, '__init__', None)
        if callable(init):
            return init
