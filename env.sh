# file: env.sh
#
# invoke with:
#   source env.sh
#
# sets up MDSplus environment and adds this directory to MDS_PATH and PYTHONPATH
#
export MDSPLUS_DIR=/data/home/jas/mdsplus-cmake/build/amazonlinux2/cmake/usr-local-mdsplus/
source $MDSPLUS_DIR/setup.sh
# Get absolute path 
MDSQUARTZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
export MDS_PATH="$MDSQUARTZ;$MDS_PATH"
export PYTHONPATH=$MDSQUARTZ:$PYTHONPATH

