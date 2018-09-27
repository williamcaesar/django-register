from django_cron import CronJobBase, Schedule
import os


class Updater(CronJobBase):
    """Keep the repository updated."""

    RUN_EVERY_MINS = 3
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'update check'

    def __init__(self):
        """Set atributes of the updater."""

    def do(self):
        """Do bussines rules."""
        os.popen('git pull')
        print('success')
