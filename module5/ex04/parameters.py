#!/usr/bin/env python3
import sys

# sys.argv[1:] -> dosya adı hariç tüm argümanlar
param_count = len(sys.argv) - 1

print(f"Number of parameters: {param_count}.")
