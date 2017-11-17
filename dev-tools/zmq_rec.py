#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import zmq

from zmq.eventloop import ioloop
from zmq.eventloop.zmqstream import ZMQStream

@click.command()
@click.option('--port', '-p', 'port', required=True)
def rec(port):

    zmq_ctx = zmq.Context()

    s = zmq_ctx.socket(zmq.SUB)
    s.bind('tcp://*:{port}'.format(port=port))
    s.setsockopt(zmq.SUBSCRIBE, b"")


    stream = ZMQStream(s)

    stream.on_recv_stream(rec_frame)

    ioloop.IOLoop.instance().start()

    while True:
        pass


def rec_frame(stream, msg, *args, **kwargs):
    print(msg[0])


if __name__ == '__main__':
    rec()
