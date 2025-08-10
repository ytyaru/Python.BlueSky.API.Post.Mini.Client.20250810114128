[ja](./README.md)

# BlueSky.API.Post.Mini.Client

Implement the minimum client to post BlueSky in Python.

![first][]
![select_handle][]
![over_300][]
![eye_catch][]
![failed][]

[first]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/first.png?raw=true
[select_handle]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/select_handle.png?raw=true
[over_300]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/over_300.png?raw=true
[eye_catch]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/eye_catch.png?raw=true
[failed]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/failed.png?raw=true

# Features

* Build: [Python][]
* BlueSky API: [atproto][]
* GUI: [Flet][]

[Python]:https://www.python.org/
[atproto]:https://github.com/MarshalX/atproto
[Flet]:https://flet.dev/

<!--

# DEMO

* [demo](https://ytyaru.github.io/Python.BlueSky.API.Post.Mini.Client.20250810114128/)

![img](https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/blob/master/doc/0.png?raw=true)

-->

# Requirement

* <time datetime="2025-08-10T11:40:49+09:00">2025-08-10</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspberry Pi OS](https://ja.wikipedia.org/wiki/Raspbian) Debian 12 bookworm 2025-05-13
* bash 5.2.15(1)-release
* Python 3.11.2

<!--* [Raspberry Pi OS](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2020-08-20 <small>[setup](http://ytyaru.hatenablog.com/entry/2020/10/06/111111)</small>-->

```sh
$ uname -a
Linux raspberrypi 6.12.34+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.12.34-1+rpt1~bookworm (2025-06-26) aarch64 GNU/Linux
```

# Installation

```sh
REPO=Python.BlueSky.API.Post.Mini.Client.20250810114128
git clone https://github.com/ytyaru/$REPO
cd $REPO
source src/5/mkvenv.sh
cd BskyMinClient
python main.py
```

# Startup

```sh
cd $REPO
source src/5/mkvenv.sh
python main.py
```

# Note

* Only plain text posts are allowed (the following are not supported):
    * Rich text
        * URL links
        * Tags
        * Mentions
    * Link cards
    * Images and videos
    * Threads

# Author

ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![BlueSky](http://www.google.com/s2/favicons?domain=bsky.app)](https://bsky.app/profile/ytyaru.bsky.social "BlueSky")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# License

This software is CC0 licensed.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.en)

