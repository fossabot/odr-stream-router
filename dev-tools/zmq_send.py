#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import time
import zmq

@click.command()
@click.option('--output', '-o', 'output', required=True)
def send(output):

    zmq_ctx = zmq.Context()

    c = zmq_ctx.socket(zmq.PUB)
    c.connect(output)

    while True:

        frame = (output).encode()
        c.send(frame, zmq.NOBLOCK)
        time.sleep(0.1)


if __name__ == '__main__':
    send()
