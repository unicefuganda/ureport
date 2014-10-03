#from setuptools import setup, find_packages
from setuptools import find_packages
from distutils.core import setup

setup(
    name='ureport',
    version='1.0',
    license="BSD",

    install_requires = [
        "django",
        "django-nose",
        'django-uni-form',
        "djtables",
        "django-extensions",
        "python-dateutil",
         "djappsettings",
        'xlrd',
        'psycopg2',
        'django-mptt', 'requests',
    ],

    dependency_links = [],

    scripts = [],

    description='Ureport deployment repository for ureport.ug',
    long_description=open('README').read(),
    author='UNICEF Uganda',
    author_email='mossplix@gmail.com',

    url='http://github.com/unicefuganda/ureport',
    download_url='http://github.com/unicefuganda/ureport/downloads',

    include_package_data=True,

    packages=find_packages(),
    package_data={'ureport':['templates/*/*.html','templates/*/*/*.html','static/*/*']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
