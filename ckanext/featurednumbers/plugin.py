import db
import actions
import ckan.model as model
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.dictization.model_dictize as md
from random import randrange

from ckan.lib.dictization import table_dictize



def get_featured_number():
    '''Returns a number, a description and the associated dataset.'''
    N = db.Featurednumbers.count()
    r = randrange(1, 8)
    return db.Featurednumbers.get(id_fn=r)

class FeaturednumbersPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'featurednumbers')

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'featurednumbers_get_featured_number': get_featured_number}


