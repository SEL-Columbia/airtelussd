from setuptools import setup, find_packages

version = '0.0'

setup(name='airtelussd',
      version=version,
      description="",
      long_description="""\
      """,
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='airtelussd',
      install_requires=[
          # -*- Extra requirements: -*-
          'PasteDeploy',
          'pastescript',
          'Werkzeug',
          'pyramid',
          'webtest',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = airtelussd:main


      [paste.filter_app_factory]
      debugger = airtelussd.middleware:make_werkzeug_debugger
      """,
#      paster_plugins=['pyramid']
      )
