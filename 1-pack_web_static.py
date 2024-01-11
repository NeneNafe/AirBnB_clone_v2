#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo"""


import os
from datetime import datetime
from fabric.api import local


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
