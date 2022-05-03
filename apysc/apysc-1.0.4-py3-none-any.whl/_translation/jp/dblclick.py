"""This module is for the translation mapping data of the
following document:

Document file: dblclick.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# dblclick interface':
    '# dblclick インターフェイス',

    'This page explains the `dblclick` (double-click) interface.':
    'このページでは`dblclick` (double-click)のインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `dblclick` interface binds the double-click event to any `DisplayObject` instance (e.g., `Sprite`\\, `Rectangle`\\, and so on). If you double-click on that instance, this interface calls the registered handler function.':  # noqa
    '`dblclick`インターフェイスは`Sprite`や`Rectangle`などの任意の`DisplayObject`のサブクラスのインスタンスへダブルクリック時のイベントを設定します。もし登録したインスタンス上でダブルクリックした場合、登録されているハンドラの関数などが呼び出されます。',  # noqa

    '## See also':
    '## 関連資料',

    'The following page describes the basic mouse event interfaces.':
    '以下のページでは基本的なマウスイベントの各インターフェイスについて説明しています。',

    '- [Basic mouse event interfaces](mouse_event_basic.md)':
    '- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)',

    '## Basic usage of the dblclick interface':
    '## dblclick インターフェイスの基本的な使い方',

    'Each `DisplayObject` instance has the `dblclick` method, and you can bind handlers by that.':  # noqa
    '`DisplayObject`のサブクラスの各インスタンスは`dblclick`メソッドを持っており、それを使ってハンドラを登録することができます。',  # noqa

    'The following example binds the double-click event handler to the rectangle. If you double-click on that instance, the rectangle color changes from cyan to magenta.':  # noqa
    '以下のコード例では四角に対してダブルクリック時のハンドラを登録しています。対象の四角のインスタンスをダブルクリックすると四角の色はシアンからマゼンタに変化します。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when double-clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.dblclick(on_double_click)\n\nap.save_overall_html(\n    dest_dir_path=\'./dblclick_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when double-clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.dblclick(on_double_click)\n\nap.save_overall_html(\n    dest_dir_path=\'./dblclick_basic_usage/\')\n```',  # noqa

    '## Basic usage of the unbind_dblclick interfaces':
    '## unbind_dblclick の各インターフェイスの基本的な使い方',

    'The `unbind_dblclick` interface can remove the single binding double-click event from a `DisplayObject` instance. The `unbind_dblclick_all` interface removes all double-click events.':  # noqa
    '`unbind_dblclick`インターフェイスは`DisplayObject`のサブクラスの任意のインスタンスからダブルクリックイベントのハンドラの設定を取り除きます。また、`unbind_dblclick_all`インターフェイスは対象のインスタンスに設定されているダブルクリックのハンドラ設定を全て取り除きます。',  # noqa

    'The following example removes the double click event by the `unbind_dblclick` method. If you double-click the rectangle, nothing happens.':  # noqa
    '以下のコード例では`unbind_dblclick`メソッドでダブルクリックのイベント設定を取り除いているため、四角をダブルクリックしても何も起きません。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when double-clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.dblclick(on_double_click)\nrectangle.unbind_dblclick(on_double_click)\n\nap.save_overall_html(\n    dest_dir_path=\'./unbind_dblclick_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when double-clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.dblclick(on_double_click)\nrectangle.unbind_dblclick(on_double_click)\n\nap.save_overall_html(\n    dest_dir_path=\'./unbind_dblclick_basic_usage/\')\n```',  # noqa

    '## dblclick API':
    '## dblclick API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Add a double-click event listener setting.<hr>':  # noqa
    '**[インターフェイス概要]** ダブルクリック時のイベント設定を追加します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - Callable that would be called when double-clicking this instance.':
    '  - このインスタンスをダブルクリックした際に呼ばれる関数やメソッドのハンドラ。',

    '- `options`: dict or None, default None':
    '- `options`: dict or None, default None',

    '  - Optional arguments dictionary to be passed to a handler.':
    '  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `name`: str':
    '- `name`: str',

    '  - Handler\'s name.':
    '  - ハンドラ名。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '- [ハンドラのoptions引数の型について](https://simon-ritchie.github.io/apysc/jp_about_handler_options_type.html)',  # noqa

    '## unbind_dblclick API':
    '## unbind_dblclick API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind a specified handler\'s double click event.<hr>':  # noqa
    '**[インターフェイス概要]** 指定されたハンドラのダブルクリック時のイベント設定を取り除きます。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `handler`: _Handler':
    '- `handler`: _Handler',

    '  - Unbinding target Callable.':
    '  - イベント設定を取り除く対象の関数やメソッドなど。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_dblclick(on_double_click)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_dblclick(on_double_click)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```',  # noqa

    '## unbind_dblclick_all API':
    '## unbind_dblclick_all API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Unbind all double click events.<hr>':
    '**[インターフェイス概要]** 全てのダブルクリック時のイベント設定を取り除きます。<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_dblclick_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_dblclick_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```',  # noqa

}
