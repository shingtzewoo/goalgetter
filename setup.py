# https://click.palletsprojects.com/en/7.x/setuptools/#introduction

from setuptools import setup

setup(
    name='Goalgetter-CLI',
    version='1.0',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        goalgetter=cli.cli:cli
    ''',
)