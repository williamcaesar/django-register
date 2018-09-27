from django_cron import CronJobBase, Schedule
from CI.container import DBEditor


class Register(CronJobBase):
    """Keep the repository updated."""

    RUN_EVERY_MINS = 3
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'register'

    def __init__(self):
        """Set atributes of the updater."""
        self.ssh_key = []

    def do(self):
        """Do bussines rules."""
        saver = DBEditor()
        saver.register()
        print('success')
