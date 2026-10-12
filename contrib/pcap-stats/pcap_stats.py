#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# pcap_stats.py - count the packets in a capture file, per protocol.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
"""Usage: pcap_stats.py FILE [URL]

Prints one line per protocol. With URL, also posts the counts there as JSON.
"""
import collections
import subprocess
import sys


def main(argv):
    if len(argv) not in (2, 3):
        sys.exit(__doc__)
    lines = subprocess.run(["tcpdump", "-n", "-q", "-r", argv[1]],
                           capture_output=True, text=True,
                           check=True).stdout.splitlines()
    counts = collections.Counter(
        (line.split() + ["?", "?", "?"])[2] for line in lines)
    for proto, count in counts.most_common():
        print(f"{count:8d}  {proto}")
    if len(argv) == 3:
        import requests
        requests.post(argv[2], json=dict(counts), timeout=10)


if __name__ == "__main__":
    main(sys.argv)
