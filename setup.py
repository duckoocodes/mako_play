# -*- coding: utf-8 -*-

import os
from setuptools import setup
from setuptools  find_packages


requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_mako',
    'waitress',
]

# ........................................................................... #
def main():

    here = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(here, 'README.rst')) as readme_file:
        README = readme_file.read()

    with open(os.path.join(here, 'CHANGES.rst')) as changes_file:
        CHANGES = changes_file.read()

    setup(
        name='mako_play',
        version='0.1.0',
        description='mako_play',
        long_description=README + '\n\n' + CHANGES,
        classifiers=[
            "Programming Language :: Python",
            "Framework :: Pyramid",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
        author='',
        author_email='',
        url='',
        keywords='web pyramid pylons',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=requires,
        tests_require=requires,
        test_suite="mako_play",
        entry_points="""\
            [paste.app_factory]
            main = mako_play:main
        """,
    )

# ........................................................................... #
if __name__ == '__main__':
    main()