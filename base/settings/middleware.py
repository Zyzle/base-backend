from __future__ import print_function

import random
import time

class LatencySimulator(object):
    def process_request(self, request):
        t = random.uniform(0, 4)
        time.sleep(t)

        return None
