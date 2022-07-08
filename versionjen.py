import jenkins
server = jenkins.Jenkins('http://18.117.236.74:8080', username='admin', password='11c86245b541f48a18c37aa7fa4c7db03e')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


nodes = get_nodes()
print(nodes)

server.create_node('slave1')
nodes = get_nodes()
print(nodes)
node_config = server.get_node_info('slave1')
print(node_config)

# create node with parameters
params = {
    'port': '22',
    'username': 'ec2-user',
    'credentialsId': 'hapro',
    'host': '3.12.155.135'
}
server.create_node(
    'slave1',
    nodeDescription='my test slave',
    remoteFS='/home/ec2-user/jenkins_home',
    labels='precise',
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH,
    launcher_params=params)
