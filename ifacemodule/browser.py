##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
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
"""Interface Details View

$Id$
"""
__docformat__ = 'restructuredtext'
from zope.interface import Interface

from zope.publisher.interfaces import IRequest
from zope.publisher.interfaces.browser import ILayer
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.publisher.interfaces.xmlrpc import IXMLRPCRequest
from zope.publisher.interfaces.http import IHTTPRequest
from zope.publisher.interfaces.ftp import IFTPRequest
from zope.security.proxy import removeSecurityProxy
from zope.proxy import removeAllProxies

from zope.app import zapi
from zope.app.publisher.browser import BrowserView

from zope.app.apidoc.utilities import getPythonPath, renderText
from zope.app.apidoc.apidoc import APIDocumentation
from zope.app.apidoc import classregistry
from zope.app.apidoc import interface, component, presentation

def findAPIDocumentationRoot(obj, request):
    if zapi.isinstance(obj, APIDocumentation):
        return zapi.absoluteURL(obj, request)
    return findAPIDocumentationRoot(zapi.getParent(obj), request)

class InterfaceDetails(BrowserView):
    """View class for an Interface."""

    def __init__(self, context, request):
        super(InterfaceDetails, self).__init__(context, request)
        self._prepareViews()
        try:
            self.apidocRoot = findAPIDocumentationRoot(context, request)
        except TypeError:
            # Probably context without location; it's a test
            self.apidocRoot = ''

    def getId(self):
        """Return the id of the field as it is defined for the interface
        utility.

        Example::

          >>> from tests import getInterfaceDetails
          >>> details = getInterfaceDetails()
          >>> details.getId()
          'IFoo'
        """
        return zapi.name(self.context)

    def getDoc(self):
        r"""Return the main documentation string of the interface.

        Example::

          >>> from tests import getInterfaceDetails
          >>> details = getInterfaceDetails()
          >>> details.getDoc()[:55]
          u'<div class="document">\n<p>This is the Foo interface</p>'
        """
        # We must remove all proxies here, so that we get the context's
        # __module__ attribute. If we only remove security proxies, the
        # location proxy's module will be returned.
        return renderText(self.context.__doc__,
                          removeSecurityProxy(self.context).__module__)

    def getBases(self):
        """Get all bases of this class

        Example::

          >>> from tests import getInterfaceDetails
          >>> details = getInterfaceDetails()
          >>> details.getBases()
          ['zope.interface.Interface']
        """
        return [getPythonPath(base) for base in self.context.__bases__]

    def getTypes(self):
        """Return a list of interface types that are specified for this
        interface."""
        # We have to really, really remove all proxies, since self.context (an
        # interface) is usually security proxied and location proxied. To get
        # the types, we need all proxies gone, otherwise the proxies'
        # interfaces are picked up as well. 
        iface = removeAllProxies(self.context)
        return [{'name': type.getName(),
                 'path': getPythonPath(type)}
                for type in interface.getInterfaceTypes(iface)]
    
    def getAttributes(self):
        """Return a list of attributes in the order they were specified."""
        # The `Interface` and `Attribute` class have no security declarations,
        # so that we are not able to access any API methods on proxied
        # objects. If we only remove security proxies, the location proxy's
        # module will be returned.
        iface = removeAllProxies(self.context)
        return [interface.getAttributeInfoDictionary(attr)
                for name, attr in interface.getAttributes(iface)]

    def getMethods(self):
        """Return a list of methods in the order they were specified."""
        # The `Interface` class have no security declarations, so that we are
        # not able to access any API methods on proxied objects. If we only
        # remove security proxies, the location proxy's module will be
        # returned.
        iface = removeAllProxies(self.context)
        return [interface.getMethodInfoDictionary(method)
                for name, method in interface.getMethods(iface)]

    def getFields(self):
        r"""Return a list of fields in required + alphabetical order.

        The required attributes are listed first, then the optional
        attributes."""
        # The `Interface` class have no security declarations, so that we are
        # not able to access any API methods on proxied objects.  If we only
        # remove security proxies, the location proxy's module will be
        # returned.
        iface = removeAllProxies(self.context)
        # Make sure that the required fields are shown first
        sorter = lambda x, y: cmp((not x[1].required, x[0].lower()),
                                  (not y[1].required, y[0].lower()))
        return [interface.getFieldInfoDictionary(field)
                for name, field in interface.getFieldsInOrder(iface, sorter)]

    def getSpecificRequiredAdapters(self):
        """Get adapters where this interface is required."""
        # Must remove security and location proxies, so that we have access to
        # the API methods and class representation.
        iface = removeAllProxies(self.context)
        regs = component.getRequiredAdapters(iface)
        regs = component.filterAdapterRegistrations(
            regs, iface,
            level=component.SPECIFIC_INTERFACE_LEVEL)
        regs = [component.getAdapterInfoDictionary(reg)
                  for reg in regs]
        return regs

    def getExtendedRequiredAdapters(self):
        """Get adapters where this interface is required."""
        # Must remove security and location proxies, so that we have access to
        # the API methods and class representation.
        iface = removeAllProxies(self.context)
        regs = component.getRequiredAdapters(iface)
        regs = component.filterAdapterRegistrations(
            regs, iface,
            level=component.EXTENDED_INTERFACE_LEVEL)
        regs = [component.getAdapterInfoDictionary(reg)
                  for reg in regs]
        return regs

    def getGenericRequiredAdapters(self):
        """Get adapters where this interface is required."""
        # Must remove security and location proxies, so that we have access to
        # the API methods and class representation.
        iface = removeAllProxies(self.context)
        regs = component.getRequiredAdapters(iface)
        regs = tuple(component.filterAdapterRegistrations(
            regs, iface,
            level=component.GENERIC_INTERFACE_LEVEL))
        return [component.getAdapterInfoDictionary(reg)
                for reg in regs]
        
    def getProvidedAdapters(self):
        """Get adapters where this interface is provided."""
        # Must remove security and location proxies, so that we have access to
        # the API methods and class representation.
        regs = component.getProvidedAdapters(removeAllProxies(self.context))
        return [component.getAdapterInfoDictionary(reg)
                for reg in regs]

    def getClasses(self):
        """Get the classes that implement this interface.

        Example::

          >>> from zope.app.apidoc.tests import pprint
          >>> from tests import getInterfaceDetails
          >>> details = getInterfaceDetails()

          >>> classes = details.getClasses()
          >>> pprint(classes)
          [[('path', 'zope.app.apidoc.ifacemodule.tests.Foo'),
            ('url', 'zope/app/apidoc/ifacemodule/tests/Foo')]]
        """
        # Must remove security and location proxies, so that we have access to
        # the API methods and class representation.
        iface = removeAllProxies(self.context)
        classes = classregistry.classRegistry.getClassesThatImplement(iface)
        return [{'path': path, 'url': path.replace('.', '/')}
                for path, klass in classes]

    def getFactories(self):
        """Return the factories, who will provide objects implementing this
        interface."""
        # Must remove security and location proxies, so that we have access to
        # the API methods and class representation.
        regs = component.getFactories(removeAllProxies(self.context))
        return [component.getFactoryInfoDictionary(reg)
                for reg in regs]

    def getUtilities(self):
        """Return all utilities that provide this interface."""
        # Must remove security and location proxies, so that we have access to
        # the API methods and class representation.
        regs = component.getUtilities(removeAllProxies(self.context))
        return [component.getUtilityInfoDictionary(reg)
                for reg in regs]


    def _prepareViews(self):
        self.httpViews = []
        self.browserViews = []
        self.ftpViews = []
        self.xmlrpcViews = []
        self.otherViews = []

        for reg in presentation.getViews(removeAllProxies(self.context)):
            type = presentation.getPresentationType(reg.required[-1])
            info = presentation.getViewInfoDictionary(reg)

            if type is IBrowserRequest:
                self.browserViews.append(info)
            elif type is IXMLRPCRequest:
                self.xmlrpcViews.append(info)
            elif type is IHTTPRequest:
                self.httpViews.append(info)
            elif type is IFTPRequest:
                self.ftpViews.append(info)
            else:
                self.otherViews.append(info)

        sort_function = lambda x, y: cmp(x['name'], y['name']) 
        self.httpViews.sort(sort_function)
        self.browserViews.sort(sort_function)
        self.ftpViews.sort(sort_function)
        self.xmlrpcViews.sort(sort_function)
        self.otherViews.sort(sort_function)
