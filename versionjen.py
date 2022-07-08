import jenkins
server = jenkins.Jenkins('http://18.117.236.74:8080', username='admin', password='11c86245b541f48a18c37aa7fa4c7db03e')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


nodes = server.get_nodes()
print(nodes)


server.create_node(
    'slave1',
    nodeDescription='my test slave',
    remoteFS='/home/ec2-user/jenkins_home',
    labels='precise',
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH)
