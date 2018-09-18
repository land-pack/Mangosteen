import os
from fabric.api import run, cd, env, hosts, settings, sudo, local
from fabric.contrib.files import exists


hosts=os.environ['HOSTS'].split(',') or ['192.168.1.211']
hosts = [i for i in hosts if i]

env.hosts=hosts
env.password=os.environ['PASSWORD'] or 'mypassword'
env.user=os.environ['USER'] or 'frank'

registry_url = os.environ['REG_URL']
pro_name = 'Mangosteen'


def d_ps():
    run('docker ps')


def d_build():

    with cd('/data/code/'):
        if exists('{}-bak'.format(pro_name)):
            run('rm -rf {}'.format(pro_name))

        if exists(pro_name):
            run('mv {} {}-bak'.format(pro_name, pro_name))

        run('git clone https://github.com/land-pack/Mangosteen.git')

    with cd('/data/code/Mangosteen/demo'):
        run('docker build -t {}/demo .'.format(registry_url))
        run('docker push {}/demo'.format(registry_url))
