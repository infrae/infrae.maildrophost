## -*- coding: utf-8 -*-
############################################
## File : __init__.py
## Author : Sylvain Viollon
## Email : sylvain@infrae.com
## Creation Date : Tue Oct 23 09:44:38 2007 CEST
## Last modification : Tue Oct 23 10:26:54 2007 CEST
############################################

__author__ ="sylvain@infrae.com"
__format__ ="plaintext"
__version__ ="$Id$"

import os, re, shutil, tempfile, urllib2, urlparse
import setuptools

class Recipe:

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options
        self.location = os.path.join(
            self.buildout['buildout']['parts-directory'], self.name)
        self.product_location = os.path.join(self.location, 'MaildropHost')
        self.url = options['url']

    def install(self):
        """
        Install the maildrophost server
        """
        download_dir = self.buildout['buildout']['download-directory']

        if not os.path.isdir(download_dir):
            os.mkdir(download_dir)

        _, _, urlpath, _, _, _ = urlparse.urlparse(self.url)
        tmp = tempfile.mkdtemp('buildout-'+self.name)
        try:
            fname = os.path.join(download_dir, urlpath.split('/')[-1])
            if not os.path.exists(fname):
                f = open(fname, 'wb')
                try:
                    print self.url
                    f.write(urllib2.urlopen(self.url).read())
                except:
                    os.remove(fname)
                    raise zc.buildout.UserError(
                        "Failed to download URL %s: %s" % (self.url, str(e)))
                f.close()
                
            setuptools.archive_util.unpack_archive(fname, tmp)
            files = os.listdir(tmp)
            os.mkdir(self.location)
            shutil.move(os.path.join(tmp, files[0]), self.product_location)
        finally:
            shutil.rmtree(tmp)

        try:
            self._build_config()
            self._build_script()
        except:
            shutil.rmtree(self.location)
            raise

        return self.location

    def _build_config(self):
        """
        Create the config file for the maildrop server ;
        Create directory used by the maildrop server.
        """
        mail_dir = self.options.get('mail-dir',
                                    os.path.sep.join(('var', 'maildrop',)))
        mail_dir = os.path.join(self.buildout['buildout']['directory'],
                                mail_dir)


        if not os.path.exists(mail_dir):
            os.makedirs(mail_dir)

        config_option = dict(smtp_host=self.options.get('smtp_host', 'locahost'),
                             smtp_port=self.options.get('smtp_port', '25'),
                             maildrop_dir=mail_dir,
                             executable=self.buildout['buildout']['executable'])

        config_filename = os.path.join(self.product_location, 'config.py')
        config = open(config_filename, 'wb')
        config.write(maildrop_config_template % config_option)

                                       


    def _build_script(self):
        """
        Create the startup script in the bin directory.
        """


    def update(self):
        """
        Update the maildrophost server
        """




def uninstall(name, options):
    """
    Remove the maildrophost server.
    """
    shutil.rmtree(self.location)


maildrop_config_template="""
PYTHON="%(executable)s"
MAILDROP_HOME="%(maildrop_dir)s"
MAILDROP_VAR="%(maildrop_dir)s"

SMTP_HOST="%(smtp_host)s"
SMTP_PORT=%(smtp_port)s

MAILDROP_INTERVAL=120
DEBUG=0
DEBUG_RECEIVER=""

MAILDROP_BATCH=0
MAILDROP_TLS=0

MAILDROP_LOGIN=""
MAILDROP_PASSWORD=""

WAIT_INTERVAL=0.0
ADD_MESSAGEID=0
"""
