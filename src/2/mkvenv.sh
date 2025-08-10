#!/usr/bin/env bash
#Pythonの仮想環境を作成して依存ライブラリをインストールしファイルに書き出して仮想環境をアクティベートする
# 定義
VENV_NAME=BskyMinClient;
VENV_ACT="./$VENV_NAME/bin/activate";
function moveThis() { cd "$(dirname "$BASH_SOURCE[0]")"; }
#function exist() { [ -d "./$VENV_NAME/bin" ] && return 0 || return 1; }
function exist() { [ -f "$VENV_ACT" ] && return 0 || return 1; }
function addx() { chmod +x "$VENV_ACT"; }
function make() { addx; python -m venv "$VENV_NAME"; }
function activate() { source "$VENV_ACT"; }
function install() { pip install atproto; pip install flet;}
function freeze() { pip freeze > requirements.txt; }

# 実行
moveThis
#	[ exist -eq 0 ] || { make; activate; install; freeze; echo '環境構築完了！'; };
exist
[ $? -eq 0 ] && activate || {
	make;
	activate;
	source "$VENV_ACT";
	echo 'アクティベート';
	install;
	freeze;
	echo '環境構築完了！';
}
cd "$VENV_NAME"

