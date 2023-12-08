#!/usr/bin/python3
"""2. Deploy archive!"""
from fabric.api import *
import datetime
import os
env.hosts = ['3.90.84.83', '54.162.104.87']


def do_pack():
    """generates a .tgz archive from the contents"""
    local("mkdir -p versions")
    x = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + x + '.tgz'
    r = local(f"tar -cvzf versions/{archive_name} web_static")

    if r.failed:
        return None
    else:
        archive_path = os.path.join("versions", archive_name)
        print("web_static packed: {} -> {}Bytes".
              format(archive_path, os.path.getsize(archive_path)))
        return archive_path


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""

    if not os.path.exists(archive_path):
        return False
    try:
        src = archive_path[9:-4]
        root = "/data/web_static/releases"
        put(archive_path, "/tmp")
        run(f"mkdir -p {root}/{src}")
        run(f"tar -xzf /tmp/{src}.tgz -C {root}/{src}")
        run(f"rm /tmp/{src}.tgz")
        run(f"mv {root}/{src}/web_static/* {root}/{src}/")
        run(f"rm -rf {root}/{src}/web_static ")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {root}/{src} /data/web_static/current")
        return True

    except Exception:
        return False
