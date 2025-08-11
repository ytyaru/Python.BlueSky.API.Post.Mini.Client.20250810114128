#!/usr/bin/env python3
import flet as ft
import sys
from atproto import Client, client_utils
import csv
from typing import NamedTuple
import re
import requests

def get_did(handle):
    r = requests.get('https://bsky.social/xrpc/com.atproto.identity.resolveHandle', params={'handle':handle})
    print(r)
    return r.json()['did']

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

class Content(NamedTuple):
    start: int      # 開始位置
    end: int        # 終了位置
    kind: str       # client_utils.TextBuilder()のメソッド名すなわちlink,mention,tag,textのいずれか
    text: str       # 表示名 client_utils.TextBuilder.link(表示名, 値)
    value: str      # 値     

class UrlBuilder: # https://
    def build(self, text):
        contents = []
        for pattern in [re.compile(s, re.I | re.M | re.U) for s in [r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+']]:
            for match in re.finditer(pattern, text):
                s = match.start()
                e = match.end()
                t = match.string[s:e]
                contents.append(Content(s, e, 'link', t, t))
        return contents

class TagBuilder: #tag
    def build(self, text):
        contents = []
        for pattern in [re.compile(s, re.I | re.M | re.U) for s in [r'#[^# \t\n]+']]:
            for match in re.finditer(pattern, text):
                s = match.start()
                e = match.end()
                t = match.string[s:e]
                contents.append(Content(s, e, 'tag', t, t[1:]))
        return contents

class MentionBuilder: # @handle
    def build(self, text):
        contents = []
        for pattern in [re.compile(s, re.I | re.M | re.U) for s in [r'@[^# \t\n]+']]:
            for match in re.finditer(pattern, text):
                s = match.start()
                e = match.end()
                t = match.string[s:e]
                # メンションの値にはDIDを渡せとドキュメンには書いてあるが、ハンドルでも成功か試してみる。
                # https://atproto.blue/en/latest/atproto/atproto_client.utils.text_builder.html#atproto_client.utils.text_builder.TextBuilder.mention
                # 次のようなエラー応答が返ってきた。やはりハンドルはダメでDIDであるべきのようだ。
                # status_code=400, error='InvalidRequest', 
                # message='Invalid app.bsky.feed.post record: Record/facets/0/features/0/did must be a valid did'
                contents.append(Content(s, e, 'mention', t, get_did(t[1:])))
#                contents.append(Content(s, e, 'mention', t, t[1:]))
        return contents


class ContentBuilder:
    def __init__(self): self.__builder = client_utils.TextBuilder()
    @property
    def builder(self): return self.__builder
    def build(self, text):
        contents = []
        for b in [UrlBuilder(), TagBuilder(), MentionBuilder()]: contents.extend(b.build(text))
        contents = sorted(contents, key=lambda c: c.start)
        contents = self.__text(text, contents)
        for c in contents: print(f'{c.start},{c.end} {c.kind} {c.text} {c.value}')
        return self.__build(contents)
    def __text(self, text, contents):
        if 0 == len(contents): return [Content(0, len(text), 'text', text, text)]
        else:
            s = 0
            for c in contents:
                if s < c.start:
                    contents.append(Content(s, c.start, 'text', text[s:c.start], text[s:c.start]))
                    s = c.end
            if s < len(text):
                contents.append(Content(s, len(text), 'text', text[s:len(text)], text[s:len(text)]))
            return sorted(contents, key=lambda c: c.start)

    def __build(self, contents):
        self.__builder = client_utils.TextBuilder()
        for c in contents:
            match c.kind:
                case 'link' | 'tag' | 'mention' | 'text':
                    (getattr(self.__builder, c.kind))(*([c.text] if 'text' == c.kind else [c.text, c.value]))
                case _: print(f'指定されたContent.kindは未定義のため無視します。:{c.kind}', file=sys.stderr)
        print(self.__builder.build_facets())
        print(self.__builder.build_text())
        return self.__builder

def main(page: ft.Page):
    page.title = 'BlueSky 投稿'
    page.window.width = 500
    page.window.height = 380
    page.fonts = {"JapaneseFont": "/home/pi/.fonts/NotoSansJP-Regular.otf"}
    page.theme = ft.Theme(font_family="JapaneseFont")  # Default app font
    users = []
    builder = ContentBuilder()

    with open('users.tsv', encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader) # 一行目を読み飛ばす
        for d in map(User._make, reader):
            if valid_user(d):
                users.append(d)
    print('TSV読込完了')
    for user in users:
        print(f'{user.handle} {user.app_pw} {user.did}')

    def dropdown_changed(e):
        post_button.disabled = True if handleDD.value is None else False or True if count.value < 0 else False
        post_content.focus()
        print(e.control.value)
        page.update()
    handleDD = ft.Dropdown(
        editable=True,
        label="handles",
        options=[ft.DropdownOption(key=user.handle, content=ft.Text(f"{user.handle}")) for user in users],
        on_change=dropdown_changed,
        value=users[0].handle,
    )
    page.add(handleDD)

    def change_count():
        count.value = 300 - len(post_content.value)
        count.color = 'red' if count.value < 0 else 'green'
        post_button.disabled = True if handleDD.value is None else False or True if count.value < 0 else False
        print(f"{count.value} {count.color}")
        page.update()

    def textfield_changed(e):
        change_count()
    post_content = ft.TextField(
        label=ft.Text("投稿内容", size=16, weight=ft.FontWeight.BOLD),
        value="""これは Python + Flet で BlueSky に投稿したものである。

リッチテキストに対応したのでURL、タグ、メンションはリンク化するはず。

https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128

文中 https://github.com/ytyaru にURL。

メンション @ytyaru.bsky.social も効くはず。

#BlueSky #atproto #Python #Flet #プログラミング""",
        multiline=True,
        min_lines=7,
        max_lines=7,
        on_change=textfield_changed,
    )
    page.add(post_content)

    count = ft.Text('300', color='green', weight=ft.FontWeight.BOLD)

    def button_clicked(e):
        print(users)
        print(handleDD.value)
        user = list(filter(lambda u: u.handle == handleDD.value, users))[0]
        print(user)

        '''
        # デバッグ
        print(builder)
        print(post_content.value)
        print(builder.build(post_content.value))
        '''
        try:
            client = Client(base_url='https://bsky.social')
            client.login(user.handle, user.app_pw)
            result.color = 'green'
            result.value = 'ログイン成功！'
            page.update()
        except Exception as e:
            result.color = 'red'
            result.value = 'ログイン失敗orz'
            page.update()
            return
        try:
            client.send_post(builder.build(post_content.value))
            result.color = 'green'
            result.value = '投稿成功！'
            page.update()
        except Exception as e:
            result.color = 'red'
            result.value = '投稿失敗orz/n{e.error}¥n{e.message}'
            print(f'投稿失敗。:{e}')
            page.update()
            return
    post_button = ft.OutlinedButton("投稿する", on_click=button_clicked, data=post_content.value)

    cnt_btn_row = ft.Row(spacing=0, controls=[count, post_button ])
    page.add(cnt_btn_row)

    result = ft.Text(value='', color='red', size=32)
    page.add(result)

    def set_focus_on_load(e):
#        handleDD.focus()
        post_content.focus()
        page.update()
    page.on_load = set_focus_on_load

    change_count()
    post_content.focus()
    page.update()


if __name__ == '__main__':
    ft.app(target=main)

