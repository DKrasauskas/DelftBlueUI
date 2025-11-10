#!/bin/bash
#SBATCH --job-name="MyJobs"
#SBATCH --partition=gpu
#SBATCH --time=00:01:00
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1G

srun bash ./job.sh