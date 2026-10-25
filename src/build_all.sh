#!/bin/sh
# 使い方: src フォルダで sh build_all.sh → 6ページを反映。ムンドは監査済み全文をコピーします。
set -e
cd "$(dirname "$0")"
python3 build_jax.py
python3 build_cho.py
python3 build_nasus.py
python3 build_gen.py
python3 build_items.py
python3 deploy.py
