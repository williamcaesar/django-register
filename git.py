import os
import subprocess


class Git(object):
    """Manage the repository."""

    def __init__(self, url):
        """Set the absolute path."""
        # self.path = os.path.abspath()
        self.url = url

    def clone(self):
        """Clone the url repo on the destiny."""
        try:
            subprocess.check_call(['git', 'clone', self.url])
        except Exception as exc:
            raise(exc)

    def pull(self):
        """Pull the updates from remote."""
        print('pulling from git repository')
        os.popen('git pull')

    def print_repo(self):
        """Print repo."""
        print(self.url)
