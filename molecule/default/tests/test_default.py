import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_httpd_package(host):
    httpd_pkg = host.package('httpd')

    assert httpd_pkg.is_installed


def test_httpd_service(host):
    httpd_svc = host.service('httpd')

    assert httpd_svc.is_enabled
    assert httpd_svc.is_running


def test_socket_listening(host):
    socket = host.socket('tcp://0.0.0.0:80')

    assert socket.is_listening


def test_command_output(host):
    command = host.run('apachectl graceful')

    assert command.rc == 0
