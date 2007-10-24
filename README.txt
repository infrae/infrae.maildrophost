infrae.maildrophost
===================

``infrae.maildrophost`` is used to install MaildropHost for Zope, and
prepare a maildrophost server. Use::


  [buildout]
  parts = maildrophost
  

  [maildrophost]
  recipe = infrae.maildrophost
  smtp_host = localhost
  smtp_port = 25


This will install MaildropHost, create configurtion files for the deamon,
and put a start/stop script in the ``bin`` directory of the buildout tree.


