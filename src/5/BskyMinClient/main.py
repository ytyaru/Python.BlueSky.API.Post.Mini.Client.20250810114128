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
    page.title = 'BlueSky 投稿'
    page.window.width = 500
    page.window.height = 380
    page.fonts = {"JapaneseFont": "/home/pi/.fonts/NotoSansJP-Regular.otf"}
    page.theme = ft.Theme(font_family="JapaneseFont")  # Default app font

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
        value="""Python + Flet で BlueSkyに投稿します。

https://github.com/ytyaru/Python.BlueSky.API.Post.Mini.Client.20250810114128

#BlueSky #Python #Flet #プログラミング""",
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
            client.send_post(post_content.value)
            result.color = 'green'
            result.value = '投稿成功！'
            page.update()
        except Exception as e:
            result.color = 'red'
            result.value = '投稿失敗orz'
            page.update()
            return
    post_button = ft.OutlinedButton("投稿する", on_click=button_clicked, data=post_content.value)

    cnt_btn_row = ft.Row(spacing=0, controls=[count, post_button ])
    page.add(cnt_btn_row)

    result = ft.Text(value='', color='red', size=32)
    page.add(result)

    def set_focus_on_load(e):
        handleDD.focus()
        page.update()
    page.on_load = set_focus_on_load

    change_count()
    page.update()


if __name__ == '__main__':
    ft.app(target=main)

