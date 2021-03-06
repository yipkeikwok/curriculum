from setuptools import setup

""" This is used to setup the web application. Be careful when altering """

setup(name='mwsu_curriculum',
      version='2020.0.dev1',
      description='Curriculum definitions and utilities for MWSU Computer Science',
      url='https://github.com/mwsu-csmp/curriculum',
      author='MWSU Computer Science Department',
      author_email='csmp@missouriwestern.edu',
      license='GPL',
      packages=['mwsu_curriculum'],  
      package_dir={'mwsu_curriculum': 'mwsu_curriculum'}, 
      package_data={'mwsu_curriculum': ['syllabi/*/*.xml', \
                                        'schedules/*.xml', \
                                        'programs/*/*.xml', \
                                        'schema/*.xsd', \
                                        'transformations/*.xsl', \
                                        'rosters/*.xml', \
                                        'standards/*.xml']},
      zip_safe=False)
