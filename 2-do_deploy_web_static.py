#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

import os
from fabric.api import *
from datetime import datetime

env.hosts = ['100.26.132.15', '100.25.118.3']
env.user = 'ubuntu'


def do_pack():
    """the function that packs all the necessary commands"""
    local('mkdir -p versions')

    archive = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    archive_name = f'web_static_{archive}.tgz'

    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return os.path.join('versions', archive_name)
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        new_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archived_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_version))
        run("sudo tar -xyz {} -C {}/".format(archived_file,
                                             new_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(new_version,
                                                new_version))
        run("sudo rm -rf {}/web_static".format(new_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_version))

        print("New version deployed!")
        return True

    return False
