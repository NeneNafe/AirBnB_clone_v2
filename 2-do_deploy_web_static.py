#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

import os
from fabric.api import put, run, env
from datetime import datetime

env.hosts = ['100.26.132.15', '100.25.118.3']
enx.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        # extract archive data
        archive_dt = os.path.basename(archive_path)[:-4]
        run('mkdir -p /data/web_static/releases/{}'.format(archive_dt))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            os.path.basename(archive_path), archive_dt))

        # remove the uploaded archive from the web server
        run('rm /tmp/{}'.format(os.path.basename(archive_path)))

        # this moves the contents to a new folder
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(archive_dt, archive_dt))

        # Remove the old symbolic link
        run('rm -rf /data/web_static/current')

        # Cresting a new symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_dt))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
