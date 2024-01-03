This repo contains samples and ideas of code to access Quartz data from MDSplus.

Main Function:
   `getquartz.py`
which uses
   `usecs_from_strings.py`

Example usage:
```
_sig = getquartz("885c9dd7-24b1-4789-b4b2-f309f093be28", "finj.in_chan_1", "2023-09-21T22:39:00")
Build_Signal(Set_Range(60001,1.932707713435569D0 /*** etc. ***/), *, Set_Range(60001,0D0 /*** etc. ***/))
dim_of(_sig)[0:10]
[0D0,.9999359999999999D0,2.000128D0,3.000064D0,4D0,5.000192D0,6.000128D0,7.000064D0,8D0,8.999936D0,9.999872D0]
```

Now we need to figure out where to get
 - guid
 - signal names
 - time range
 - zero time

We can then construct trees with
 - tagged nodes holding
   - guid
   - time range
   - zero time
 - any hierarchy we want with leaves:
   - signal - the answer MDSplus Signal
   - signal:qname - the quartz name (could be hard coded into the signal node's expression)

We could then think about:
 - writing something that uses quartz data discovery to generate trees
 - or (possibly) make `plugable, virtual, tree hierarchies` with functions for
   - `parent_of()`
   - `child_of()`
   - `member_of()`
   - `sibling_of()`

To use need to:
```
export MDSPLUS_DIR=/data/home/jas/mdsplus-cmake/build/amazonlinux2/cmake/usr-local-mdsplus/
source $MDSPLUS_DIR/setup.sh
export MDS_PATH="{this-dir};$MDS_PATH"
export PYTHONPATH={this-dir}:$PYTHONPATH
```
and create a findable link to the libpython3.10.so

```
ln -s /idea_apps/Linux/spack/opt/spack/linux-amzn2-zen2/gcc-12.2.0/python-3.10.10-5ag7selmv6gnigvfda23jdfiuzu6mk77/lib/libpython3.10.so.1.0 /data/home/jas/mdsplus-cmake/build/amazonlinux2/cmake/usr-local-mdsplus/lib/libpython3.10.so
```
or possibly add `/idea_apps/Linux/spack/opt/spack/linux-amzn2-zen2/gcc-12.2.0/python-3.10.10-5ag7selmv6gnigvfda23jdfiuzu6mk77/lib` to `LD_LIBRARY_PATH`

