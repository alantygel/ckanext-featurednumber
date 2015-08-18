
=============
ckanext-featurednumbers
=============

Featured Numbers is a very simple plugin that displays a custom number (or a fact) on CKAN's front page and links it to the corresponding dataset, for example:

805 million people were suffering from chronic undernourishment in 2012-2014 (link to UNO data)

You can register several numbers, with associated description, unit, specify if the unit comes before or after the number (U$1000 or 1000km), and add a link to a dataset from where this fact comes from.

The main motivation was the perception that such numbers call people's attentionand incentivates the search and use of data.

------------
Requirements
------------

* CKAN 2.0+

------------
Installation
------------

To install ckanext-featurednumbers:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-featurednumbers Python package into your virtual environment::

     pip install ckanext-featurednumbers

3. Add ``featurednumbers`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.featurednumbers.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install ckanext-featurednumbers for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/alantygel/ckanext-featurednumbers.git
    cd ckanext-featurednumbers
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.featurednumbers --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-featurednumbers on PyPI
---------------------------------

ckanext-featurednumbers should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-featurednumbers. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-featurednumbers
----------------------------------------

ckanext-featurednumbers is availabe on PyPI as https://pypi.python.org/pypi/ckanext-featurednumbers.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
