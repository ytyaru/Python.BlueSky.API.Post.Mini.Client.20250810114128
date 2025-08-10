# ライブラリ Flet を使用する

* https://qiita.com/ForestMountain1234/items/bc709c3599ee86e2a0dd
* https://qiita.com/NasuPanda/items/48849d7f925784d6b6a0

　尚、Linuxの場合は以下でパッケージを追加する必要が合った。

* https://flet.dev/docs/publish/linux/#prerequisites

```sh
sudo apt install -y libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools
```
```sh
sudo apt update
sudo apt install libmpv-dev libmpv2
sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
```
```sh
sudo apt install -y libmpv-dev mpv
```

　Fletを使用したコードを実行すると以下エラーが出た。インストールしたはずのlibmpvが参照できていない。

```sh
$ ./main.py 
/home/pi/.flet/bin/flet-0.28.3/flet/flet: error while loading shared libraries: libmpv.so.1: cannot open shared object file: No such file or directory
```

　気になるのは`libmpv.so.1`というヘンテコな名前だ。

　とりあえずインストールしたパッケージのパス一覧を見てみる。

```sh
$ dpkg-query -L libmpv-dev
/.
/usr
/usr/include
/usr/include/mpv
/usr/include/mpv/client.h
/usr/include/mpv/render.h
/usr/include/mpv/render_gl.h
/usr/include/mpv/stream_cb.h
/usr/lib
/usr/lib/aarch64-linux-gnu
/usr/lib/aarch64-linux-gnu/pkgconfig
/usr/lib/aarch64-linux-gnu/pkgconfig/mpv.pc
/usr/share
/usr/share/doc
/usr/share/doc/libmpv-dev
/usr/share/doc/libmpv-dev/changelog.Debian.gz
/usr/share/doc/libmpv-dev/changelog.gz
/usr/share/doc/libmpv-dev/copyright
/usr/lib/aarch64-linux-gnu/libmpv.so
```

　`libmpv.so`という名前であって`libmpv.so.1`などという妙な名前ではない。

　ならFletが参照するヘンテコな名前のシンボリックリンクを作ってやればいいか。

```sh
sudo ln -s /usr/lib/aarch64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
```
```sh
ln: シンボリックリンク '/usr/lib/libmpv.so.1' の作成に失敗しました: ファイルが存在します
```

　え、あるんかい！

```sh
$ cd /usr/lib
$ ls | grep libmpv.so.1
libmpv.so.1
```

　あるやん。

　でもFletはそれを参照しやがらないってことかな？

　参照して？

　Fletがどこを参照しているか知らないが、とりあえず`main.py`があるディレクトリにリンクを作ってみる。

```sh
sudo ln -s /usr/lib/aarch64-linux-gnu/libmpv.so ./libmpv.so.1
```

　動いた。やれやれ。でも文字化けしてる……。

　日本語はフォントを指定しないと使えない的な話かな？



* https://stackoverflow.com/questions/78007193/error-while-loading-shared-libraries-libmpv-so-1-cannot-open-shared-object-fil
