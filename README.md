# ODR Stream Router

A fairly primitive tool to route ODR zmq streams.

The aim of `odroute` is to achieve two goals:

 - Providing ways to handle a fallback for DAB+ streams generated with `odr-dabmod`.
   E.g. in the situation when running a dedicated encoder box in the studio, but in case of connection- or
   encoder-failure an automatic failover to a central encoder instance (encoding a webstream) is desired.
 - Providing way to distribute DAB+ streams through a single connection from an encoder to multiple MUXes.


## Installation

    pip install -e .

resp.

   pip install -e git+https://github.com/digris/odr-stream-router.git#egg=odr-stream-router


## Usage

    odroute run --help

#### Simple example:

Listen on ports *5001* and *5002* and output the active port to *tcp://localhost:9001* - switching
inputs after 0.4 seconds of 'inactivity/activity'.

`-i/--input` and `-o/--output` can both be specified multiple times.

The priority of the input ports is specified through the order. So in this example port *5001* is forwarded if
available, else packages from the socket on *5002* are used.

    odroute run -s 5001 -s 5002 -o tcp://localhost:9001 -d 0.5 -v debug