# This file is part of curtin. See LICENSE file for copyright and license info.

from .releases import base_vm_classes as relbase
from .releases import centos_base_vm_classes as centos_relbase
from .test_network import (TestNetworkBaseTestsAbs,
                           CentosTestNetworkBasicAbs)


class TestNetworkStaticRoutesAbs(TestNetworkBaseTestsAbs):
    """ Static network routes testing with ipv4
    """
    conf_file = "examples/tests/network_static_routes.yaml"


class CentosTestNetworkStaticRoutesAbs(CentosTestNetworkBasicAbs):
    """ Static network routes testing with ipv4
    """
    conf_file = "examples/tests/network_static_routes.yaml"


class TrustyTestNetworkStaticRoutes(relbase.trusty,
                                    TestNetworkStaticRoutesAbs):
    __test__ = True


class TrustyHWEUTestNetworkStaticRoutes(relbase.trusty_hwe_u,
                                        TrustyTestNetworkStaticRoutes):
    # Working, off by default to save test suite runtime, covered by
    # TrustyTestNetworkStaticRoutes
    __test__ = False


class TrustyHWEVTestNetworkStaticRoutes(relbase.trusty_hwe_v,
                                        TrustyTestNetworkStaticRoutes):
    # Working, off by default to save test suite runtime, covered by
    # TrustyTestNetworkStaticRoutes
    __test__ = False


class TrustyHWEWTestNetworkStaticRoutes(relbase.trusty_hwe_w,
                                        TrustyTestNetworkStaticRoutes):
    # Working, off by default to save test suite runtime, covered by
    # TrustyTestNetworkStaticRoutes
    __test__ = False


class XenialTestNetworkStaticRoutes(relbase.xenial,
                                    TestNetworkStaticRoutesAbs):
    __test__ = True


class BionicTestNetworkStaticRoutes(relbase.bionic,
                                    TestNetworkStaticRoutesAbs):
    __test__ = True


class CosmicTestNetworkStaticRoutes(relbase.cosmic,
                                    TestNetworkStaticRoutesAbs):
    __test__ = True


class DiscoTestNetworkStaticRoutes(relbase.disco,
                                   TestNetworkStaticRoutesAbs):
    __test__ = True


class Centos66TestNetworkStaticRoutes(centos_relbase.centos66_xenial,
                                      CentosTestNetworkStaticRoutesAbs):
    __test__ = False


class Centos70TestNetworkStaticRoutes(centos_relbase.centos70_xenial,
                                      CentosTestNetworkStaticRoutesAbs):
    __test__ = False

# vi: ts=4 expandtab syntax=python
