import jenkins
server = jenkins.Jenkins('http://18.117.236.74:8080', username='admin', password='11c86245b541f48a18c37aa7fa4c7db03e')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


nodes = server.get_nodes()
print(nodes)

server.delete_node('slave22')

params = {
    'port': '22',
    'username': 'ec2-user',
    'credentialsId': 'hapro',
    'host': '3.135.213.219'
}
server.create_node(
    'slave22',
    nodeDescription='my test slave',
    remoteFS='/home/ec2-user/jenkins_home',
    labels='precise',
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH,
    launcher_params=params)
