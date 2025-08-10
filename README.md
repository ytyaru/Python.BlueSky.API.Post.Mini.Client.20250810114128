[en](./README.en.md)

# BlueSky.API.Post.Mini.Client

　BlueSky投稿する最小クライアントをPythonで仮実装する。

![first][]
![select_handle][]
![over_300][]
![eye_catch][]
![failed][]

[first]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/memo/first.png?raw=true
[select_handle]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/memo/select_handle.png?raw=true
[over_300]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/memo/over_300.png?raw=true
[eye_catch]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/memo/eye_catch.png?raw=true
[failed]:https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/raw/master/memo/failed.png?raw=true

# 特徴

* Build: [Python][]
* BlueSky API: [atproto][]
* GUI: [Flet][]

[Python]:https://www.python.org/
[atproto]:https://github.com/MarshalX/atproto
[Flet]:https://flet.dev/

<!--

# デモ

* [demo](https://ytyaru.github.io/Python.BlueSky.API.Post.Mini.Client.20250810114128/)

![img](https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128/blob/master/doc/0.png?raw=true)

-->

# 開発環境

* <time datetime="2025-08-10T11:40:49+09:00">2025-08-10</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspberry Pi OS](https://ja.wikipedia.org/wiki/Raspbian) Debian 12 bookworm 2025-05-13
* bash 5.2.15(1)-release
* Python 3.11.2

```sh
$ uname -a
Linux raspberrypi 6.12.34+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.12.34-1+rpt1~bookworm (2025-06-26) aarch64 GNU/Linux
```

# インストール

```sh
REPO=Python.BlueSky.API.Post.Mini.Client.20250810114128
git clone https://github.com/ytyaru/$REPO
cd $REPO
source src/5/mkvenv.sh
cd BskyMinClient
python main.py
```

# GUI起動

```sh
cd $REPO
source src/5/mkvenv.sh
python main.py
```

　`mkvenv.sh`はインストール済みなら仮想環境をアクティベートする。これはライブラリの参照に必要なので必須の操作。（一々手動でsourceしなくちゃいけないから面倒極まりない。`source`の代わりに`.`と表記して省略できるが焼け石に水）


# 注意

* プレーンテキスト投稿しかできません（次のようなことができません）
    * リッチテキスト
        * URLリンク
        * タグ
        * メンション
    * リンクカード
    * 画像、動画
    * スレッド

# 著者

　ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![BlueSky](http://www.google.com/s2/favicons?domain=bsky.app)](https://bsky.app/profile/ytyaru.bsky.social "BlueSky")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# ライセンス

　このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

