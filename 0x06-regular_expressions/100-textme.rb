#!/usr/bin/env ruby
# output: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used
print ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:([0-1:-]+)\]/).join(',')
