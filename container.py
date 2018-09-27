from CI.models import Container
import socket
import os


class DBEditor(object):
    """Edit container database."""

    def __init__(self):
        self.hostname = socket.gethostname()
        self.key_path = '{}/.ssh/id_rsa.pub'.format(os.environ['HOME'])
        print(' hostname: {}\n key path: {}'.format(
            self.hostname, self.key_path))

    def register(self):
        """Register a new container on database."""
        container = Container.objects.all().filter(name=self.hostname)
        if len(container) < 1:
            new_container = Container()
            new_container.name = self.hostname
            # check if the ssh key exists
            print('entra no if')
            if os.path.isfile(self.key_path):
                print('the key already exists')
            else:
                os.popen("ssh-keygen -f ~/.ssh/id_rsa -t rsa -N ''")

            ssh_key = open(self.key_path)
            ssh_key = ssh_key.readlines()
            print('the key is: {}'.format(ssh_key))
            new_container.ssh_key = ssh_key
            try:
                new_container.save()
                print('saved')
            except Exception as exc:
                raise(exc)
        else:
            print('the container already exists')
