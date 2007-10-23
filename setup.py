from setuptools import setup, find_packages

name = "infrae.maildrophost"
setup(name = name,
      version = "0.1",
      author = "Sylvain Viollon",
      author_email = "sylvain@infrae.com",
      description = "Install and setup maildrophost server",
      long_description = """
      Recipe to download, install MaildropHost Zope product,
      create and configure a maildrop host server in the buildout tree.
      """,
      license = "ZPL 2.1",
      keywords = "buildout",
      classifiers = ["Framework :: Buildout",
                     ],
      url = 'http://www.python.org/pypi/'+name,

      packages = find_packages(),
      namespace_packages = ['infrae'],
      install_requires = ['zc.buildout', 'setuptools'],
      entry_points = {'zc.buildout':
                      ['default = %s:Recipe' % name]},
    )
