#!/bin/bash
#SBATCH --job-name="job3" 
#SBATCH --partition=gpu
#SBATCH --cpus-per-task=1 
#SBATCH --gpus-per-task=1
#SBATCH --time=00:1:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1G

srun job.sh