#!/usr/bin/env ruby
# accepts one argument and pass it to a regular
# expression matching method
print ARGV[0].scan(/^[A-Z]$/).join
