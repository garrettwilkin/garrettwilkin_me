from __future__ import with_statement
from fabric.api import *

env.hosts = ['hacktivate.org']
env.project_name = 'garrettwilkin.me'
env.user = 'machine'

@task
def test():
    env.remote_dir = '/var/www/test.garrettwilkin.me'

@task
def prod():
    env.remote_dir = '/var/www/'

@task
def init():
    with cd(env.remote_dir):
        run("git clone git@github.com:garrettwilkin/garrettwilkin_me.git")

@task
def deploy():
    local("git pull --rebase origin master")
    local("git push origin master")
    code_dir = env.remote_dir + '/garrettwilkin.me'
    with cd(code_dir):
        # TODO pull is probably not optimal for deploy. Perhaps fetch?
        # maybe a force option? No need to merge on the remote.
        run("git pull origin master")
    
