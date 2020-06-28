#!/bin/bash
for d in Unprocessed/ ; do (cd "$d" && for d in ./*/ ; do (cd "$d" &&  chmod +x Allrun && ./Allrun && cp -r "$PWD" ../../Processed ); done ); done
