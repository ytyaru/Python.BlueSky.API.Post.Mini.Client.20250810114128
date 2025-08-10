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
function install() {  }
function installAtproto() {pip install atproto;}
function installFlet() {
	# Fletを使うにはLinuxの場合以下コマンドが必要。
	sudo apt update -y
	sudo apt install -y libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools
	sudo apt install -y libmpv-dev libmpv2
	# 以下のようなエラーが出た。libmpv.so.1 が参照できないらしい。
	# error while loading shared libraries: libmpv.so.1: cannot open shared object file: No such file or directory
	# dpkg-query -L libmpv-dev でパスを確認してみる。libmpv.soはあったので、これをリネームしたリンクを作る。場所はmain.pyがあるディレクトリ。
	sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so "./$VENV_NAME/libmpv.so.1";
	# Fletをインストールする
	pip install flet;
}
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

