# -*- coding: utf-8 -*-
import logging
import sys

import click
import click_log

from router import StreamRouter

__version__ = '0.0.1'

logger = logging.getLogger(__name__)


@click.group()
@click_log.simple_verbosity_option()
@click_log.init(__name__)
def cli():
    pass


@cli.command()
@click_log.simple_verbosity_option()
@click.option('--source', '-s', 'sources', type=int, multiple=True, required=True,
              help='The source ports for incoming connections. Can (and likely will) be given multiple times')
@click.option('--output', '-o', 'outputs', multiple=True, required=True,
              help='Destinations to route to, in the form of: tcp://<hostnam>:<port>. Can be given multiple times')
@click.option('--delay', '-d', default=0.5,
              help='Delay until to fallback to secondary streams')
def run(sources, outputs, delay):
    logger.info('Source ports: %s' % ', '.join(map(str, sources)))
    logger.info('Destinations: %s' % ', '.join(outputs))

    while True:

        r = StreamRouter(sources, outputs, delay)

        try:
            r.connect()
            r.run()
        except KeyboardInterrupt:
            logger.info('Ctrl-c received! Stop router')
            r.stop()
            sys.exit()
