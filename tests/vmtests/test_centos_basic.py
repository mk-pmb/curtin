from . import VMBaseClass
from .releases import centos_base_vm_classes as relbase
from .test_network import TestNetworkBaseTestsAbs

import textwrap


# FIXME: should eventually be integrated with the real TestBasic
class CentosTestBasicAbs(VMBaseClass):
    __test__ = False
    conf_file = "examples/tests/centos_basic.yaml"
    extra_kern_args = "BOOTIF=eth0-52:54:00:12:34:00"
    collect_scripts = [textwrap.dedent(
        """
        cd OUTPUT_COLLECT_D
        cat /etc/fstab > fstab
        rpm -qa | cat >rpm_qa
        # selinux is FUN!
        ifconfig -a | cat >ifconfig_a
        ip a | cat >ip_a
        netstat -rn | cat >netstat_rn
        echo $PIPESTATUS | cat >netstat_pipestatus
        cp -a /etc/sysconfig/network-scripts .
        cp -a /var/log/messages .
        cp -a /var/log/cloud-init* .
        cp -a /var/lib/cloud ./var_lib_cloud
        cp -a /run/cloud-init ./run_cloud-init
        python2 -c 'from cloudinit import util; \
                    print(util.subp(["netstat", "-rn"]))'
        """)]
    fstab_expected = {
        'LABEL=cloudimg-rootfs': '/',
    }

    def test_dname(self):
        pass

    def test_interfacesd_eth0_removed(self):
        pass

    def test_output_files_exist(self):
        self.output_files_exist(["fstab"])


# FIXME: this naming scheme needs to be replaced
class Centos70FromXenialTestBasic(relbase.centos70fromxenial,
                                  CentosTestBasicAbs):
    __test__ = True


class Centos66FromXenialTestBasic(relbase.centos66fromxenial,
                                  CentosTestBasicAbs):
    __test__ = False
    # FIXME: test is disabled because the grub config script in target
    #        specifies drive using hd(1,0) syntax, which breaks when the
    #        installation medium is removed. other than this, the install works


class CentosTestBasicNetworkAbs(TestNetworkBaseTestsAbs):
    conf_file = "examples/tests/centos_basic.yaml"
    extra_kern_args = "BOOTIF=eth0-52:54:00:12:34:00"
    collect_scripts = TestNetworkBaseTestsAbs.collect_scripts + [
        textwrap.dedent("""
            cd OUTPUT_COLLECT_D
            cp -a /etc/sysconfig/network-scripts .
            cp -a /var/log/cloud-init* .
            cp -a /var/lib/cloud ./var_lib_cloud
            cp -a /run/cloud-init ./run_cloud-init
        """)]

    def test_etc_network_interfaces(self):
        pass

    def test_etc_resolvconf(self):
        pass


class Centos70BasicNetworkFromXenialTestBasic(relbase.centos70fromxenial,
                                              CentosTestBasicNetworkAbs):
    __test__ = True
