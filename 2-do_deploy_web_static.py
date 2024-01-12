#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

import os
from fabric.api import put, run, env
from datetime import datetime

env.hosts = ['100.26.132.15', '100.25.118.3']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    try:
        if not os.path.exists(archive_path):
            return False

        # upload archive
        put(archive_path, '/tmp/')

        # extract archive dir
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove the uploaded archive from the web server
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # this moves the contents into host web static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # Remove extraneous web static dir
        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
            .format(timestamp))

        # delete existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish sym link
        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))

        # return True on success
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
