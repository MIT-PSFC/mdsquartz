# file: env.sh
#
# invoke with:
#   source env.sh
#
# sets up MDSplus environment and adds this directory to MDS_PATH and PYTHONPATH
#
export MDSPLUS_DIR=/data/home/jas/mdsquartz/usr-local-mdsplus-debug
source $MDSPLUS_DIR/setup.sh
export PYTHONPATH=/data/home/jas/mdsquartz/usr-local-mdsplus-debug/python:$PYTHONPATH
# Get absolute path 
MDSQUARTZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
export MDS_PATH="$MDSQUARTZ;$MDS_PATH"
export PYTHONPATH=$MDSQUARTZ:$PYTHONPATH
export default_tree_path=$MDSQUARTZ/trees/~t
export LD_LIBRARY_PATH=/data/home/jas/mdsquartz:$LD_LIBRARY_PATH
