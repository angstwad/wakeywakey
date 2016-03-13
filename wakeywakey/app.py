# -*- coding: utf-8 -*-

# Copyright 2016 Paul Durivage <pauldurivage+github@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import sys
import time
from argparse import ArgumentParser

from slackclient import SlackClient


class WakeyWakey(object):
    def __init__(self, token):
        self.token = token
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = SlackClient(self.token)
        return self._client

    def set_auto(self):
        return self.client.api_call('users.setPresence', presence='auto')

    def set_active(self):
        return self.client.api_call('users.setActive')


def run_forever(args):
    wakey = WakeyWakey(args.token)
    while True:
        resp_auto = wakey.set_auto()
        resp_active = wakey.set_active()
        for n, r in (('Set Auto', resp_auto), ('Set Active', resp_active)):
            if r['ok'] is False:
                print("%s Error: %s" % (n, r['error']), file=sys.stderr)
        time.sleep(args.interval)


def run_once(args):
    wakey = WakeyWakey(args.token)
    resp_auto = wakey.set_auto()
    resp_active = wakey.set_active()
    for name, resp in (('Set Auto', resp_auto), ('Set Active', resp_active)):
        if resp['ok'] is False:
            print("%s Error: %s" % (name, resp['error']), file=sys.stderr)
            sys.exit(1)


def parse_args():
    parser = ArgumentParser(
        prog='wakeywakey',
        description="Continuously mark your Slack presence as active - never "
                    "appear away!"
    )
    parser.add_argument('token', help='Slack OAuth token')
    parser.add_argument(
        '--run-once', action='store_true',
        help='Sets user as active and exits.'
    )
    parser.add_argument(
        '-i', '--interval', default=300, type=int,
        help='Interval (seconds) at which Slack API is contacted. Default: 300'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.run_once:
        run_once(args)
    else:
        try:
            run_forever(args)
        except KeyboardInterrupt:
            raise SystemExit('\nExiting.')


if __name__ == '__main__':
    main()
