from setuptools import setup, find_packages

version = '0.0.1'


setup(name='bit.content.checksum',
      version=version,
      description="Calculate and store a checksum for content",
      long_description=open("README.txt").read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Ryan Northey',
      author_email='ryan@3ca.org.uk',
      url='http://code.3ca.org.uk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bit', 'bit.content'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.annotation',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
