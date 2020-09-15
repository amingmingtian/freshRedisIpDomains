import configparser

configLoader = configparser.ConfigParser()
configLoader.read("config.ini")
redis_cluster_nodes = configLoader.get('redis', 'cluster_nodes').encode('utf-8').split(',')
redis_password = configLoader.get('redis', 'password').encode()
http_3g_path = configLoader.get('data', 'path_3g').encode()
http_4g_path = configLoader.get('data', 'path_4g').encode()
http_3g_scheme = configLoader.get('data', 'scheme_3g').encode()
http_4g_scheme = configLoader.get('data', 'scheme_4g').encode()
target_scheme = configLoader.get('data', 'target_scheme').encode()
tb_ip_dn_host = configLoader.get('sql', 'tb_ip_dn_host').encode()
sql_count = configLoader.get('sql', 'sql_count').encode()
tb_ip_dn_count = configLoader.get('sql', 'tb_ip_dn_count').encode()
sql_max = configLoader.get('sql', 'sql_max').encode()

startup_nodes = [
    {"host": node.split(':')[0], "port": node.split(':')[1]}
    for node in redis_cluster_nodes
]
print startup_nodes
print redis_password
print redis_cluster_nodes
print http_3g_path
print http_4g_path
print http_3g_scheme
print http_4g_scheme
print target_scheme
print tb_ip_dn_count
print tb_ip_dn_host
print sql_max
print sql_count
