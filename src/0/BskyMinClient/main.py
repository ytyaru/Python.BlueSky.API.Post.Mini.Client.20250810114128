#!/usr/bin/env python3

import sys
from atproto import Client, client_utils
import csv

class User:
    def __init__(self, handle, app_pw, did=''):
        print(f'{handle} {app_pw} {did} {isinstance(did, str)} {not did}')
        if not isinstance(handle, str) and len(handle) < 1: raise ValueError(f'handleは一文字以上の文字列にしてください。: {handle}')
        if not isinstance(app_pw, str) and len(app_pw) < 1: raise ValueError(f'app_pwは一文字以上の文字列にしてください。: {app_pw}')
        if not (not did or (isinstance(did, str) and not did.startswith('did:plc:'))): raise ValueError(f'didは空文字かdid:plc:から始まる文字列にしてください。:{did}')
#        if (isinstance(did, str) and (0==len(did) or not did.startswith('did:plc:'))): raise ValueError(f'didは空文字かdid:plc:から始まる文字列にしてください。:{did}')
        self.__handle = handle
        self.__app_pw = app_pw
        self.__did = did
    @property
    def handle(self): return self.__handle
    @property
    def app_pw(self): return self.__app_pw
    @property
    def did(self): return self.__did
    def login(self):
        try:
            self.__client = Client(base_url='https://bsky.social')
            self.__client.login(self.handle, self.app_pw)
            if not self.did: self.__did = client.get_profile(self.handle).did
#        self.__did = client.get_profile(self.handle).did if self.did is None else self.did
        except Exception as e:
            print(f'ログインに失敗しました。/n{e}', file=sys.stderr)


#def main(handle, password) -> None:
def main() -> None:
    users = []
    with open('users.tsv', encoding='utf-8', newline='') as f:
        for cols in csv.reader(f, delimiter='\t'):
            try: users.append(User(*cols))
            except Exception as e: print(e, file=sys.stderr)

    print('TSV読込完了')
    for user in users:
        print(f'{user.handle} {user.app_pw} {user.did}')


#    client = Client(base_url='https://bsky.social')
#    client.login(handle, password)
#    print('ログイン成功！')

    # DID取得するため
#    profile = client.get_profile(client.me.handle)
#    print(profile)
#    print('DID:', profile.did)

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
    main()
    '''
    print(sys.argv)
    if len(sys.argv) < 3: 
        print("Error: BlueSkyユーザのハンドルとパスワードを引数に渡してください。", file=sys.stderr)
        sys.exit(1)
#    print(sys.argv[1], sys.argv[2])
    main(sys.argv[1], sys.argv[2])
    '''

