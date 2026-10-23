#!/bin/sh
# 使い方: src フォルダで  sh build_all.sh  → 5ページを生成し、公開用 index.html に反映します。
set -e
cd "$(dirname "$0")"
python3 lane55/render.py
python3 build_jax.py
python3 build_cho.py
python3 build_nasus.py
python3 build_gen.py
python3 build_items.py
python3 deploy.py
