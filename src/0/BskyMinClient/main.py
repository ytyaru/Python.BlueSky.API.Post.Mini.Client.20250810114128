#!/usr/bin/env python3

import sys
from atproto import Client, client_utils

def main(handle, password) -> None:
    client = Client(base_url='https://bsky.social')
    client.login(handle, password)
    print('ログイン成功！')

    # DID取得するため
    profile = client.get_profile(client.me.handle)
    print('DID:', profile.did)
    '''
    text_builder = client_utils.TextBuilder()
    text_builder.text('APIで投稿してみる。\n改行確認。\n\nPythonライブラリatprotoで実行した。\n\n')
    text_builder.text('タグの挿入。実際の値はblueskyだが以下別の表記にしてみた。\n')
    text_builder.tag('#ブルスカ', 'bluesky')
    text_builder.text(' ')
    text_builder.text('\nハッシュ記号のないタグも挿入できるか試す。\n')
    text_builder.text(' ')
    text_builder.tag('BlueSky', 'bluesky')
    text_builder.text(' \n\n')
    #text_builder.mention('私自身へのメンション', 'did:plc:ffttrlkbljhdeoypveptm4sj')
    text_builder.mention('私自身へのメンション', profile.did) # 'did:plc:ffttrlkbljhdeoypveptm4sj'

    text_builder.text(' ')
    text_builder.link('私のはてなブログ', 'https://ytyaru.hatenablog.com/')
    text_builder.text('へのリンク。通常はURL文字列だが任意テキストで表示されたはず。')

    client.send_post(text_builder)
    print('ポスト成功！')
    '''


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 3: 
        print("Error: BlueSkyユーザのハンドルとパスワードを引数に渡してください。", file=sys.stderr)
        sys.exit(1)
#    print(sys.argv[1], sys.argv[2])
    main(sys.argv[1], sys.argv[2])

