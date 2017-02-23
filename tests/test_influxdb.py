import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_influxdb_is_installed(Package):
    influxdb = Package("influxdb")
    assert influxdb.is_installed
    assert influxdb.version.startswith('1.2.0')


def test_influxdb_config_file(File):
    config = File('/etc/influxdb/influxdb.conf')
    assert config.user == "root"
    assert config.group == "influxdb"
    assert config.mode == 0o644


def test_influxdb_enabled_and_running(Service):
    influxdb = Service("influxdb")
    assert influxdb.is_running
    assert influxdb.is_enabled
