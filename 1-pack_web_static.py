#!/usr/bin/python3
"""1. Compress before sending"""
from fabric.api import local
import datetime
import os


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
