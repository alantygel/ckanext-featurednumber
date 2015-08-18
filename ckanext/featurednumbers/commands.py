import ckan.plugins as p
import paste.script
import db
import logging

from ckan.lib.cli import CkanCommand

from ckan import model

log = logging.getLogger(__name__)

class FeaturedNumbersCommands(CkanCommand):
    """
    ckanext-featurednumbers commands:
    Usage::
        paster featurednumbers migrate
    """
    summary = __doc__.split('\n')[0]
    usage = __doc__

    parser = paste.script.command.Command.standard_parser(verbose=True)
    parser.add_option('-c', '--config', dest='config',
        default='production.ini', help='Config file to use.')

    def command(self):
        if not len(self.args):
            print self.__doc__
            return

        cmd = self.args[0]
        self._load_config()

        if cmd == 'migrate':
            self._migrate()
        else:
            print self.__doc__

    def _migrate(self):
        if not db.featurednumbers_table.exists():
            db.featurednumbers_table.create()
            log.info('Featured Numbers table created')
        else:
            log.warning('Featured Numbers table already exists')
            print 'Featured Numbers table already exists'
