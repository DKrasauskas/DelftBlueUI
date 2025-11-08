module load 2025
module load 2024r1 openmpi
module load cmake/3.27.7

module list 2>&1 | awk '
/Currently Loaded Modules:/ {print "\033[1;34m" $0 "\033[0m"; next}
NF {print "\033[31m" $0 "\033[0m"}'
cd job/subjob1/OpenMP_exercises
ls -l
pwd
if cmake --version &> /dev/null; then
    mkdir -p build
    cd build
    export CC=mpicc
    export CXX=mpicxx
    export FC=mpifort
    cmake ..
    cmake --build .
else
    echo "Cmake Module not loaded / exiting"
fi