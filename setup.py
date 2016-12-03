from setuptools import setup

import easyquant

long_desc = """
easyquant
===============

* easyquant


"""

setup(
        name='easyquant',
        description='quant framework  for China Stock Trade',
        long_description = long_desc,
        author='shidenggui',
        author_email='longlyshidenggui@gmail.com',
        license='BSD',
        url='https://github.com/shidenggui/easyquant',
        keywords='China stock trade',
        install_requires=[
            'requests',
            'logbook',
            'anyjson',
            'aiohttp',
            'easytrader',
            'easyquotation',
        ],
        classifiers=['Development Status :: 4 - Beta',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.2',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'License :: OSI Approved :: BSD License'],
        packages=['easyquant', 'easyquant.easydealutils', 'easyquant.log_handler', 'easyquant.push_engine', 'easyquant.strategy'],
        package_data={'': ['*.jar', '*.json','*.conf']}
)

