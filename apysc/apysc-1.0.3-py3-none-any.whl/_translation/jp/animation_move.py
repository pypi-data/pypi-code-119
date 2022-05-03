"""This module is for the translation mapping data of the
following document:

Document file: animation_move.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_move interface':
    '# animation_move インターフェイス',

    'This page explains the `animation_move` method interface.':
    'このページでは`animation_move`メソッドのインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `animation_move` method interface creates an `AnimationMove` instance. You can animate the x and y coordinates with it.':  # noqa
    '`animation_move`メソッドのインターフェイスは`AnimationMove`クラスのインスタンスを生成します。そのインスタンスを使ってXとY座標に対してアニメーションを設定することができます。',  # noqa

    'This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle` class.':  # noqa
    'このインターフェイスは`Sprite`や`Rectangle`などの`DisplayObject`の各サブクラスに存在します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The following example sets the coordinates animation (from x=50, y=50 to x=100, y=100) with the `animation_move` method.':  # noqa
    '以下のコード例では`animation_move`のメソッドを使ってx=50, y=50の座標からx=100, y=100の座標へのアニメーションを設定しています。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    animation_move: ap.AnimationMove = e.this.target.animation_move(\n        x=50, y=50, duration=1000)\n    animation_move.animation_complete(on_animation_complete_2)\n    animation_move.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    animation_move: ap.AnimationMove = e.this.target.animation_move(\n        x=100, y=100, duration=1000)\n    animation_move.animation_complete(on_animation_complete_1)\n    animation_move.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(\n    x=100, y=100, duration=1000)\nanimation_move.animation_complete(on_animation_complete_1)\nanimation_move.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_move_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    animation_move: ap.AnimationMove = e.this.target.animation_move(\n        x=50, y=50, duration=1000)\n    animation_move.animation_complete(on_animation_complete_2)\n    animation_move.start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle],\n        options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    animation_move: ap.AnimationMove = e.this.target.animation_move(\n        x=100, y=100, duration=1000)\n    animation_move.animation_complete(on_animation_complete_1)\n    animation_move.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=200, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nanimation_move: ap.AnimationMove = rectangle.animation_move(\n    x=100, y=100, duration=1000)\nanimation_move.animation_complete(on_animation_complete_1)\nanimation_move.start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_move_basic_usage/\')\n```',  # noqa

    '## animation_move API':
    '## animation_move API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Set the x and y coordinates animation settings.<hr>':  # noqa
    '**[インターフェイス概要]** XとY座標に対するアニメーションを設定します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `x`: Int or int':
    '- `x`: Int or int',

    '  - Destination of the x-coordinate.':
    '  - 最終的なX座標。',

    '- `y`: Int or int':
    '- `y`: Int or int',

    '  - Destination of the y-coordinate.':
    '  - 最終的なY座標。',

    '- `duration`: Int or int, default 3000':
    '- `duration`: Int or int, default 3000',

    '  - Milliseconds before an animation ends.':
    '  - アニメーション完了までのミリ秒。',

    '- `delay`: Int or int, default 0':
    '- `delay`: Int or int, default 0',

    '  - Milliseconds before an animation starts.':
    '  - アニメーション開始までの遅延時間のミリ秒。',

    '- `easing`: Easing, default Easing.LINEAR':
    '- `easing`: Easing, default Easing.LINEAR',

    '  - Easing setting.':
    '  - イージング設定。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `animation_move`: AnimationMove':
    '- `animation_move`: AnimationMove',

    '  - Created animation setting instance.':
    '  - 生成されたアニメーションのインスタンス。',

    '<hr>':
    '<hr>',

    '**[Notes]**':
    '**[特記事項]**',

    'To start this animation, you need to call the `start` method of the returned instance.<hr>':  # noqa
    'アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=1)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_move(\n...     x=100, y=150,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> sprite.graphics.line_style(\n...     color=\'#fff\', thickness=1)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_move(\n...     x=100, y=150,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)':  # noqa
    '- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_duration.html)',  # noqa

    '- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)':  # noqa
    '- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_delay.html)',  # noqa

    '- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)':  # noqa
    '- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp_animation_return_value.html)',  # noqa

    '- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)':  # noqa
    '- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp_sequential_animation.html)',  # noqa

    '- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)':  # noqa
    '- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_animation_parallel.html)',  # noqa

    '- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '- [イージングのenum](https://simon-ritchie.github.io/apysc/jp_easing_enum.html)',  # noqa

}
