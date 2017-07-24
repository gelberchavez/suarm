# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
import click
from .cluster import *
from fabric.tasks import execute
from .tasks import Server, HOST

@click.group(chain=True)
def main():
    click.echo("main")


@main.command('nodes')
@click.option('--config', '-f', type=click.Path(), help='Config file "swarm.json"')
def nodes(config):
    click.echo('nodes')


@main.command('scale')
@click.option('--config', '-f', type=click.Path(), help='Config file "swarm.json"')
@click.option('--node', '-n', type=str, help='NodeID on Vultr')
@click.option('--plan', '-p', type=str, help='PlanID on Vultr')
def scale(config, node, plan):
    click.echo('scale')


@main.command('ssh-keygen')
@click.option('--config', '-f', type=click.Path(), help='Config file "swarm.json"')
def ssh_keygen(config):
    click.echo('ssh_keygen')
    register_sshkey()


@main.command('create')
@click.option('--config', '-f', type=click.Path(), help='Config file "swarm.json"')
def create(config):
    click.echo('create.......')
    create_cluster()


@main.command('delete')
@click.option('--config', '-f', type=click.Path(), help='Config file "swarm.json"')
def delete(config):
    click.echo('delete')
    destroy_cluster()


@main.command('increase')
@click.option('--config', '-f', type=click.Path(), help='Config file "swarm.json"')
@click.option('--replicas', '-r', type=int, help='NodeID on Vultr')
@click.option('--plan', '-p', type=str, help='PlanID on Vultr')
@click.option('--os', '-o', type=str, help='OSID on Vultr')
def increase(config, replicas, plan, os):
    click.echo('increase')


@main.command('set')
@click.option('--service', type=click.Choice(['dashboard', 'manager', 'worker']))
@click.option('--node', '-n', type=str, help='NodeID on Vultr')
def set(service, node):
    if service == 'dashboard':
        pass
    elif service == 'manager':
        pass
    elif service == 'worker':
        pass
    click.echo(service)


@main.command('loadbalancer')
@click.option('--config', '-f', type=click.Path(), help='Add load balancer')
@click.option('--zone', '-z', type=int, default=12, help='ZoneID on Vultr')
@click.option('--plan', '-p', type=int, default=201, help='PlanID on Vultr')
@click.option('--oss', '-o', type=int, default=215, help='OSID on Vultr')
def addlb(config, zone, plan, oss):
    click.echo('--> Adding Load balancer...')
    add_loadbalancer(zone=zone, plan=plan, oss=oss)

