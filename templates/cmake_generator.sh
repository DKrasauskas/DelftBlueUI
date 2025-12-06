#!/bin/bash
module load 2025
module load cuda/12.9
nvcc --version
module load cmake/3.30.5
cmake -S . -B cmake-build-debug2
cmake --build cmake-build-debug2 -j$(nproc)