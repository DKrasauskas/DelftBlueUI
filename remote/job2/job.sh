#!/bin/bash
module avail >> modules.txt
nvidia-smi >> output.txt
#nvidia-smi --query-gpu=name,uuid,driver_version,memory.total,memory.free,memory.used,temperature.gpu,utilization.gpu,utilization.memory,pstate,clocks.gr,clocks.sm,clocks.mem,clocks.video --format=csv >> output.csv