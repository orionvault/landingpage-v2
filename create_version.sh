#!/usr/bin/env bash

function get_git_version() {
    git rev-parse --short HEAD
}

GIT_VERSION=$(get_git_version)_$(date +%s)
VERSION_DIR="./versions/ov_$GIT_VERSION"

mkdir "$VERSION_DIR"
cp -r ./src/*.html ./src/vendor ./src/img ./src/js ./src/css ./src/files "$VERSION_DIR"

echo "Created new version $GIT_VERSION in $VERSION_DIR"

rm -d dist
ln -sf "$VERSION_DIR" ./dist 

echo "Created symlink to dist from newly created version"
echo "DONE."
