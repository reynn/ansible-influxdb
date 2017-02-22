influxdb
========

[![Build Status](https://travis-ci.org/kbrebanov/ansible-influxdb.svg?branch=master)](https://travis-ci.org/kbrebanov/ansible-influxdb)

Installs and configures InfluxDB.

Requirements
------------

This role requires Ansible 1.9 or higher.

Role Variables
--------------

| Name                                             | Default                | Description                                                                                                                                                |
|:-------------------------------------------------|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| influxdb_version                                 | 1.0.2                  | Version of InfluxDB to install                                                                                                                             |
| influxdb_hostname                                | ''                     | Use this option to manually set the hostname                                                                                                               |
| influxdb_reporting_disabled                      | false                  | When enabled, InfluxDB will report usage data every 24 hours to usage.influxdata.com                                                                       |
| influxdb_meta_dir                                | /var/lib/influxdb/meta | Where the metadata/raft database is stored                                                                                                                 |
| influxdb_meta_retention_autocreate               | true                   |                                                                                                                                                            |
| influxdb_meta_logging_enabled                    | true                   | If log messages are printed for the meta service                                                                                                           |
| influxdb_meta_pprof_enabled                      | false                  |                                                                                                                                                            |
| influxdb_meta_lease_duration                     | 1m0s                   | The default duration for leases                                                                                                                            |
| influxdb_data_enabled                            | true                   | Controls if this node holds time series data shards in the cluster                                                                                         |
| influxdb_data_dir                                | /var/lib/influxdb/data |                                                                                                                                                            |
| influxdb_data_wal_dir                            | /var/lib/influxdb/wal  |                                                                                                                                                            |
| influxdb_data_wal_logging_enabled                | true                   | If log messages are printed for the storage engine                                                                                                         |
| influxdb_data_trace_logging_enabled              | false                  | Trace logging provides more verbose output around the tsm engine. Turning this on can provide more useful output for debugging tsm engine issues           |
| influxdb_data_query_log_enabled                  | true                   | Whether queries should be logged before execution. Very useful for troubleshooting, but will log any sensitive data contained within a query               |
| influxdb_data_cache_max_memory_size              | 524288000              | Maximum size a shard's cache can reach before it starts rejecting writes                                                                                   |
| influxdb_data_cache_snapshot_memory_size         | 26214400               | Size at which the engine will snapshot the cache and write it to a TSM file, freeing up memory                                                             |
| influxdb_data_cache_snapshot_write_cold_duration | 1h                     | Length of time at which the engine will snapshot the cache and write it to a new TSM file if the shard hans't received writes or deletes                   |
| influxdb_data_compact_min_file_count             | 3                      | Minimum number of TSM files that need to exist before a compaction cycle will run                                                                          |
| influxdb_data_compact_full_write_cold_duration   | 24h                    | Duration at which the engine will compact all TSM files in a shard if it hasn't received a write or delete                                                 |
| influxdb_data_max_points_per_block               | 1000                   | Maximum number of points in an encoded block in a TSM file. Larger numbers may yield better compression but could incur a perfomance penalty when querying |
| influxdb_coordinator_write_timeout               | 10s                    |                                                                                                                                                            |
| influxdb_coordinator_max_concurrent_queries      | 0                      |                                                                                                                                                            |
| influxdb_coordinator_query_timeout               | 0                      |                                                                                                                                                            |
| influxdb_coordinator_log_queries_after           | 0                      |                                                                                                                                                            |
| influxdb_coordinator_max_select_point            | 0                      |                                                                                                                                                            |
| influxdb_coordinator_max_select_series           | 0                      |                                                                                                                                                            |
| influxdb_coordinator_max_select_buckets          | 0                      |                                                                                                                                                            |
| influxdb_retention_enabled                       | true                   |                                                                                                                                                            |
| influxdb_retention_check_interval                | 30m                    |                                                                                                                                                            |
| influxdb_shard_precreation_enabled               | true                   |                                                                                                                                                            |
| influxdb_shard_precreation_check_interval        | 10m                    |                                                                                                                                                            |
| influxdb_shard_precreation_advance_period        | 30m                    |                                                                                                                                                            |
| influxdb_monitor_store_enabled                   | true                   | Whether to record statistics internally                                                                                                                    |
| influxdb_monitor_store_database                  | _internal              | The destination database for recorded statistics                                                                                                           |
| influxdb_monitor_store_interval                  | 10s                    | The interval at which to record statistics                                                                                                                 |
| influxdb_admin_enabled                           | true                   |                                                                                                                                                            |
| influxdb_admin_bind_address                      | ":8083"                |                                                                                                                                                            |
| influxdb_admin_https_enabled                     | false                  |                                                                                                                                                            |
| influxdb_admin_https_certificate                 | /etc/ssl/influxdb.pem  |                                                                                                                                                            |
| influxdb_http_enabled                            | true                   |                                                                                                                                                            |
| influxdb_http_bind_address                       | ":8086"                |                                                                                                                                                            |
| influxdb_http_auth_enabled                       | false                  |                                                                                                                                                            |
| influxdb_http_log_enabled                        | true                   |                                                                                                                                                            |
| influxdb_http_write_tracing                      | false                  |                                                                                                                                                            |
| influxdb_http_pprof_enabled                      | false                  |                                                                                                                                                            |
| influxdb_http_https_enabled                      | false                  |                                                                                                                                                            |
| influxdb_http_https_certificate                  | /etc/ssl/influxdb.pem  |                                                                                                                                                            |
| influxdb_http_https_private_key                  | ''                     | Use a separate private key location                                                                                                                        |
| influxdb_http_max_row_limit                      | 10000                  |                                                                                                                                                            |
| influxdb_http_realm                              | InfluxDB               |                                                                                                                                                            |
| influxdb_subscriber_enabled                      | true                   |                                                                                                                                                            |
| influxdb_subscriber_http_timeout                 | 30s                    |                                                                                                                                                            |
| influxdb_graphite_enabled                        | false                  |                                                                                                                                                            |
| influxdb_graphite_database                       | graphite               |                                                                                                                                                            |
| influxdb_graphite_bind_address                   | ":2003"                |                                                                                                                                                            |
| influxdb_graphite_protocol                       | tcp                    |                                                                                                                                                            |
| influxdb_graphite_consistency_level              | one                    |                                                                                                                                                            |
| influxdb_graphite_batch_size                     | 5000                   |                                                                                                                                                            |
| influxdb_graphite_batch_pending                  | 10                     |                                                                                                                                                            |
| influxdb_graphite_batch_timeout                  | 1s                     |                                                                                                                                                            |
| influxdb_graphite_udp_read_buffer                | 0                      |                                                                                                                                                            |
| influxdb_graphite_separator                      | .                      |                                                                                                                                                            |
| influxdb_graphite_tags                           | []                     |                                                                                                                                                            |
| influxdb_graphite_templates                      | []                     |                                                                                                                                                            |
| influxdb_collectd_enabled                        | false                  |                                                                                                                                                            |
| influxdb_collectd_bind_address                   | ''                     |                                                                                                                                                            |
| influxdb_collectd_database                       | ''                     |                                                                                                                                                            |
| influxdb_collectd_typesdb                        | ''                     |                                                                                                                                                            |
| influxdb_collectd_batch_size                     | 1000                   |                                                                                                                                                            |
| influxdb_collectd_batch_pending                  | 5                      |                                                                                                                                                            |
| influxdb_collectd_batch_timeout                  | 1s                     |                                                                                                                                                            |
| influxdb_collectd_read_buffer                    | 0                      |                                                                                                                                                            |
| influxdb_opentsdb_enabled                        | false                  |                                                                                                                                                            |
| influxdb_opentsdb_bind_address                   | ":4242"                |                                                                                                                                                            |
| influxdb_opentsdb_database                       | opentsdb               |                                                                                                                                                            |
| influxdb_opentsdb_retention_policy               | ''                     |                                                                                                                                                            |
| influxdb_opentsdb_consistency_level              | one                    |                                                                                                                                                            |
| influxdb_opentsdb_tls_enabled                    | false                  |                                                                                                                                                            |
| influxdb_opentsdb_certificate                    | ''                     |                                                                                                                                                            |
| influxdb_opentsdb_log_point_errors               | true                   |                                                                                                                                                            |
| influxdb_opentsdb_batch_size                     | 1000                   |                                                                                                                                                            |
| influxdb_opentsdb_batch_pending                  | 5                      |                                                                                                                                                            |
| influxdb_opentsdb_batch_timeout                  | 1s                     |                                                                                                                                                            |
| influxdb_udp_enabled                             | false                  |                                                                                                                                                            |
| influxdb_udp_bind_address                        | ''                     |                                                                                                                                                            |
| influxdb_udp_database                            | udp                    |                                                                                                                                                            |
| influxdb_udp_retention_policy                    | ''                     |                                                                                                                                                            |
| influxdb_udp_batch_size                          | 1000                   |                                                                                                                                                            |
| influxdb_udp_batch_pending                       | 5                      |                                                                                                                                                            |
| influxdb_udp_batch_timeout                       | 1s                     |                                                                                                                                                            |
| influxdb_udp_read_buffer                         | 0                      |                                                                                                                                                            |
| influxdb_udp_payload_size                        | 65536                  |                                                                                                                                                            |
| influxdb_continuous_queries_log_enabled          | true                   |                                                                                                                                                            |
| influxdb_continuous_queries_enabled              | true                   |                                                                                                                                                            |
| influxdb_continuous_queries_run_interval         | 1s                     |                                                                                                                                                            |

Dependencies
------------

None

Example Playbook
----------------

Install InfluxDB
```yaml
- hosts: all
  roles:
    - kbrebanov.influxdb
```

License
-------

BSD

Author Information
------------------

Kevin Brebanov
