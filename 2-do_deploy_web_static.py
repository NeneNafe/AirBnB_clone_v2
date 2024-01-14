#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

import os
from fabric.api import local, put, env, run, sudo
from datetime import datetime

env.hosts = ['100.26.132.15', '100.25.118.3']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """distributes an archive to webservers"""
    if not os.path.exists(archive_path):
        return False

    basename = os.path.basename(archive_path)
    rem_archive_path = f"/tmp/{basename}"

    try:
        put(archive_path, rem_archive_path)
        x_archive = "/data/web_static/releases/{}".format(
            os.path.splitext(basename)[0]
        )
        run(f"mkdir -p {x_archive}")
        run("tar -xzf {} -C {} --strip-components=1".format(
            rem_archive_path, x_archive
            ))
        run(f"rm -f {rem_archive_path}")
        symlink = "/data/web_static/current"
        run(f"rm -rf {symlink}")
        run(f"ln -s {x_archive}/ {symlink}")
    except Exception:
        return False

    return True
