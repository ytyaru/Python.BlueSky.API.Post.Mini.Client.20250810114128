#!/usr/bin/env python3
import flet as ft
import sys
from atproto import Client, client_utils
import csv
from typing import NamedTuple

class User(NamedTuple):
    handle: str
    app_pw: str
    did: str

def valid_user(user):
    print(user)
    if not isinstance(user.handle, str) and len(user.handle) < 1:
        print(f'handleは一文字以上の文字列にしてください。: {user.handle}', file=sys.stderr)
        return False
    if not isinstance(user.app_pw, str) and len(user.app_pw) < 1:
        print(f'app_pwは一文字以上の文字列にしてください。: {user.app_pw}', file=sys.stderr)
        return False
    if (user.did.startswith('did:plc:') or user.did):
        print(f'didは空文字かdid:plc:から始まる文字列にしてください。:{user.did}', file=sys.stderr)
        return False
    return True


def main(page: ft.Page):
    # https://flet.dev/docs/cookbook/fonts/
    page.fonts = {"JapaneseFont": "/home/pi/.fonts/NotoSansJP-Regular.otf"}
#    page.fonts = {"JapaneseFont": "/home/pi/.fonts/NotoSansJP-VariableFont_wght.ttf"}
    page.theme = ft.Theme(font_family="JapaneseFont")  # Default app font
    #page.add(ft.Text("こんにちは", font_family="JapaneseFont"))
#    page.add(ft.Text("Hello World !!"))
#    page.add(ft.Text("こんにちは/n世界！", font_family="JapaneseFont", size=64, weight=ft.FontWeight.BOLD))
    page.add(ft.Text("BlueSky 投稿", font_family="JapaneseFont", size=64, weight=ft.FontWeight.BOLD))

    users = []
    with open('users.tsv', encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader) # 一行目を読み飛ばす
        for d in map(User._make, reader):
            if valid_user(d):
                users.append(d)
    print('TSV読込完了')
    for user in users:
        print(f'{user.handle} {user.app_pw} {user.did}')

    # Text Control 生成
#    t = ft.Text(value="BlueSky 投稿", color="green")
    # ページのコントロールリストに Control を追加
#    page.controls.append(t)

    '''
    list_view = ft.ListView(
        controls=[ft.Text(f"{user.handle}") for user in users],
        height=300,  # スクロール可能な高さを設定
    )
    page.add(list_view)
    '''


    def dropdown_changed(e):
        print(e)
        e.control.color = e.control.value
        page.update()
    dd = ft.Dropdown(
        editable=True,
        label="handles",
        options=[ft.DropdownOption(key=user.handle, content=ft.Text(f"{user.handle}")) for user in users],
        on_change=dropdown_changed,
    )
    page.add(dd)



    def textfield_changed(e):
#        t.value = e.control.value
#        print(e.control.value)
#        page.update()
#        encoded_value = e.control.value.encode('utf-8', 'ignore').decode('utf-8')
#        txt_出力.value = encoded_value # エンコードされた値を表示
#        e.control.value = e.control.value.encode('utf-8', 'ignore').decode('utf-8')
#        e.control.value = ft.Text(e.control.value, font_family="JapaneseFont", size=16, weight=ft.FontWeight.BOLD)
        print(e.control.value)
        print(ft.Text(e.control.value, font_family="JapaneseFont"))
        page.update()

    tf = ft.TextField(
        label=ft.Text("投稿内容", font_family="JapaneseFont", size=16, weight=ft.FontWeight.BOLD),
#        value=ft.Text("UIから入力すると日本語が文字化けする。文字が豆腐になる。", font_family="JapaneseFont", size=16, weight=ft.FontWeight.BOLD),
        value="UIから入力すると日本語が文字化けする。文字が豆腐になる。",
        multiline=True,
        min_lines=1,
#        max_lines=5,
        on_change=textfield_changed,
#        font_family="JapaneseFont",
    )
    page.add(tf)

    # ページを更新
    page.update()

"""
def main() -> None:
    users = []
    with open('users.tsv', encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader) # 一行目を読み飛ばす
        for d in map(User._make, reader):
            if valid_user(d):
                users.append(d)
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
"""


if __name__ == '__main__':
    ft.app(target=main)

#    main()
    '''
    print(sys.argv)
    if len(sys.argv) < 3: 
        print("Error: BlueSkyユーザのハンドルとパスワードを引数に渡してください。", file=sys.stderr)
        sys.exit(1)
#    print(sys.argv[1], sys.argv[2])
    main(sys.argv[1], sys.argv[2])
    '''

