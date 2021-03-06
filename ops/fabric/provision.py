import json

from fabric.api import *
from pprintpp import pprint as out
from fabric.contrib.project import rsync_project
from utils import *


@task(default=True)
@hosts()
def provision(role=False):
    state = get_state()

    if (not role) or (role == 'dev'):

        env.hosts = ["localhost"]
        env.host = ["localhost"]
        env.host_string = ["localhost"]
        env.stages = [state.dev]

        local("sudo salt-call state.highstate --config-dir='/project/ops/salt/config/dev' pillar='"+json.dumps(state)+"' -l debug")

    elif role == 'web':
        state = get_state()

        server = state.services.public_ips.web.address

        env.user = state.web.admin.user
        env.hosts = [server]
        env.host = server
        env.host_string = server

        env.key_filename = 'ops/keys/admin.pem'

        user = state.web.admin.user
        group = state.web.admin.group

        run("curl -L https://github.com/everysquare/formula/archive/4541430110542004b9fc311f5620155d0932e88b.tar.gz -o /tmp/formula.tar.gz")

        md5 = run("md5sum /tmp/formula.tar.gz | awk '{ print $1 }'").strip()
        if md5 != "0beb7ce48459da2ed6888542ec109727":
            sys.exit()

        run("tar xvf /tmp/formula.tar.gz -C /srv --strip-components=1")

        with settings(warn_only=True):
            check_for_salt = run("which salt-call")
            if check_for_salt.return_code != 0:
                # Install Salt
                run("cd /tmp && wget https://github.com/saltstack/salt-bootstrap/archive/v2015.08.06.tar.gz -q")

                md5 = run("cd /tmp && md5sum v2015.08.06.tar.gz | awk '{ print $1 }'").strip()
                if md5 != "60110888b0af976640259dea5f9b6727":
                    sys.exit()

                run("cd /tmp && tar -xvf v2015.08.06.tar.gz")
                run("cd /tmp && sudo sh salt-bootstrap-2015.08.06/bootstrap-salt.sh -P -p python-dev -p python-pip -p python-git -p unzip")

        # Get the files where they need to be before provisioning
        sudo("mkdir -p /salt")
        sudo("chown -R "+user+":"+group+" /salt")
        rsync_project("/salt/", "./ops/salt/")

        # Provision the machine
        state['role'] = 'web'
        sudo("salt-call state.highstate --config-dir='/salt/config/web' pillar='"+json.dumps(state)+"' -l debug")

