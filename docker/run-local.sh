#!/bin/bash
if [ -z "$1" ]
  then
    echo "    Must provide the absolute path to the local directory where hubmapconsortium/documentation was cloned."; echo "    Like ./runlocal.sh /users/myuser/projects/hubmap/documentation"; exit 1;
fi

if [ ! -d "$1" ]
  then
    echo "$1 must be a valid directory"; exit 1;
fi

if [[   "$1" != /* ]]
then
    echo "$1 is not an absolute path."; exit 1;
fi

if [[ "$1" == */ ]]
then
    S_DOC_DIR=`echo "$1" | rev | cut -c2- | rev`;
else
    S_DOC_DIR="$1";
    
fi

if [ ! -d "$S_DOC_DIR/docs" ]
  then
    echo "docs directory expected, but not found at $S_DOC_DIR/docs";  exit 1;
fi

docker run -it -p4000:4000 -v $S_DOC_DIR:/software-docs github-pages-server_local:latest
