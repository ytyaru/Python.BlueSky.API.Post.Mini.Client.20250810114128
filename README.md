[ja](./README.ja.md)

# BlueSky.API.Post.Mini.Client

Implement the minimum client to post BlueSky in Python.

<!--

# DEMO

* [demo](https://ytyaru.github.io/Python.BlueSky.API.Post.Mini.Client.20250810114128/)

![img](https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/blob/master/doc/0.png?raw=true)

# Features

* sales point

-->

# Requirement

* <time datetime="20250810114049">20250810114049</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspberry Pi OS](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2020-08-20 <small>[setup](http://ytyaru.hatenablog.com/entry/2020/10/06/111111)</small>
* bash 5.2.15(1)-release
* 

<!-- * environment: python2: コマンドが見つかりません
 -->

```sh
$ uname -a

```

# Installation

```sh
REPO=Python.BlueSky.API.Post.Mini.Client.20250810114128
git clone https://github.com/ytyaru/$REPO
cd $REPO
source src/0/mkvenv.sh
cd BskyMinClient
python main.py
```

## anyenv

```sh
git clone https://github.com/anyenv/anyenv ~/.anyenv
echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(anyenv init -)"' >> ~/.bash_profile
anyenv install --init -y
```

## pyenv

```sh
anyenv install pyenv
exec $SHELL -l
```

## python

```sh
sudo apt install -y libsqlite3-dev libbz2-dev libncurses5-dev libgdbm-dev liblzma-dev libssl-dev tcl-dev tk-dev libreadline-dev
```

```sh
pyenv install -l
```
```sh
pyenv install 3.10.5
```


## this works

```sh
git clone https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128Python.BlueSky.API.Post.Mini.Client.20250810114128
cd Python.BlueSky.API.Post.Mini.Client.20250810114128/src
```

# Usage

## run

```sh
./run.py
```

## unit test

```sh
./test.py
```

<!--

# Note

* important point

-->

# Author

ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![twitter](http://www.google.com/s2/favicons?domain=twitter.com)](https://twitter.com/ytyaru1 "twitter")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# License

This software is CC0 licensed.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.en)

