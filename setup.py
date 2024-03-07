from setuptools import find_packages, setup

setup(
    name='django_databricks',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django package for database connection with Databricks.',
    long_description='A Django package for database connection with Databricks.',
    url='https://github.com/ChanduArepalli/django_databricks',
    author='Chandu Arepalli',
    author_email='chandumanikumar4@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)