import python-jenkins
print jenkins.__file__

server = python-jenkins.Jenkins('http://18.117.236.74:8080', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
