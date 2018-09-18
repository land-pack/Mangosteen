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
git_url = 'https://github.com/land-pack/Mangosteen.git'
pro_path = '/Mangosteen/demo'


def d_ps():
    run('docker ps')


def d_build():

    with cd('/data/code/'):
        if exists('{}-bak'.format(pro_name)):
            run('rm -rf {}'.format(pro_name))

        if exists(pro_name):
            run('mv {} {}-bak'.format(pro_name, pro_name))

        run('git clone {}'.format(git_url))

    with cd('/data/code{}'.format(pro_path)):
        run('docker build --build-arg registry_url=192.168.1.1/ak/base -t {}/demo .'.format(registry_url))
        run('docker push {}/demo'.format(registry_url))
