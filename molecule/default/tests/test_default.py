import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_repo(host):
    if host.system_info.distribution == 'debian':
        r = host.file('/etc/apt/sources.list.d/litespeed.list')
    elif host.system_info.distribution == 'centos':
        r = host.file('/etc/yum.repos.d/litespeed.repo')

    assert r.exists
