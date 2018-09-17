import os
from fabric.api import run, cd, env, hosts, settings, sudo, local
from fabric.contrib.files import exists


hosts=os.environ['HOSTS'].split(',') or ['192.168.1.211']
hosts = [i for i in hosts if i]
env.hosts=hosts
env.password=os.environ['PASSWORD'] or 'mypassword'
env.user=os.environ['USER'] or 'frank'

registry_url = os.environ['REG_URL']

def d_ps():
    run('docker ps')


def d_build():
    with cd('/data/code/'):
        run('git clone https://github.com/land-pack/Mangosteen.git')
    
    with cd('/data/code/demo'):
        run('docker build -t {}/demo .'.format(registry_url))
        run('docker push {}/demo'.format(registry_url))
