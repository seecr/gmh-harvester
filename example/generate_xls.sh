#!/bin/bash
#

source /etc/seecr/metastreams/config

python create_xls.py \
    --state-path=${STATEDIR} \
    --log-path=${LOGDIR} \
    --data-path=${DATADIR} \
    --domain_id=kb-acc \
    --target-path=./x

