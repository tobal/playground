#!/usr/bin/env bash
echo "This will run a stand-alone version of Druid"
set +u
shopt -s xpg_echo
shopt -s expand_aliases
trap "exit 1" 1 2 3 15

SCRIPT_DIR=`dirname $0`
DRUID_DIR=$1

if [[ ! -d "${DRUID_DIR}/lib" ]]; then
  echo "No druid library found"
  exit 2
fi

CURR_DIR=`pwd`
cd ${SCRIPT_DIR}
SCRIPT_DIR=`pwd`
cd ${CURR_DIR}

[ -d /tmp/example ]  &&  echo "Cleaning up from previous run.."  &&  /bin/rm -fr /tmp/example

SPEC_FILE="${SCRIPT_DIR}/mean_deviation/randoms_realtime.spec"

EXAMPLE_LOC=$(dirname $SPEC_FILE)

#  start process
JAVA_ARGS="-Xmx512m -Duser.timezone=UTC -Dfile.encoding=UTF-8"
JAVA_ARGS="${JAVA_ARGS} -Ddruid.realtime.specFile=${SPEC_FILE}"

DRUID_CP=${EXAMPLE_LOC}
#For a pull
DRUID_CP=${SCRIPT_DIR}/../config/realtime:${DRUID_CP}
#For the kit
DRUID_CP=${DRUID_CP}:${SCRIPT_DIR}/config/_common
DRUID_CP=${DRUID_CP}:${SCRIPT_DIR}/config/realtime
DRUID_CP=${DRUID_CP}:${DRUID_DIR}/lib/*

echo "Running command:"

(set -x; java ${JAVA_ARGS} -classpath ${DRUID_CP}  io.druid.cli.Main example realtime)
