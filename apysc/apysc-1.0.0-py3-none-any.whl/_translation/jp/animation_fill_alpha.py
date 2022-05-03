"""This module is for the translation mapping data of the
following document:

Document file: animation_fill_alpha.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# animation_fill_alpha interface':
    '# animation_fill_alpha インターフェイス',

    'This page explains the `animation_fill_alpha` method interface.':
    'このページでは`animation_fill_alpha`メソッドのインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    'The `animation_fill_alpha` method interface creates an `ap.AnimationFillAlpha` instance (animation setting instance and the  `AnimationBase` subclass). You can animate fill alpha (opacity) with it.':  # noqa
    '`animation_fill_alpha`メソッドのインターフェイスでは`AnimationBase`のサブクラスであり且つアニメーション設定を扱う`ap.AnimationFillAlpha`クラスのインスタンスを生成します。そのインスタンスを使って塗りの透明度のアニメーションを設定することができます。',  # noqa

    'This interface exists on a `GraphicsBase` subclass, such as the `Rectangle` or `Circle` class.':  # noqa
    'このインターフェイスは`Rectangle`や`Circle`クラスなどの`GraphicsBase`のサブクラスで存在します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The following example sets the fill alpha animation (from 1.0 to 0.0) with the `animation_fill_alpha` method:':  # noqa
    '以下の例では1.0～0.0の塗りの透明度のアニメーションを`animation_fill_alpha`メソッドで設定しています。',

    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_alpha(\n        alpha=1.0, duration=DURATION,\n    ).animation_complete(on_animation_complete_2).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_alpha(\n        alpha=0.0, duration=DURATION,\n    ).animation_complete(on_animation_complete_1).start()\n\n\nap.Stage(\n    stage_width=150, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_fill_alpha(\n    alpha=0.0, duration=DURATION,\n).animation_complete(on_animation_complete_1).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_fill_alpha_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_alpha(\n        alpha=1.0, duration=DURATION,\n    ).animation_complete(on_animation_complete_2).start()\n\n\ndef on_animation_complete_2(\n        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_alpha(\n        alpha=0.0, duration=DURATION,\n    ).animation_complete(on_animation_complete_1).start()\n\n\nap.Stage(\n    stage_width=150, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.animation_fill_alpha(\n    alpha=0.0, duration=DURATION,\n).animation_complete(on_animation_complete_1).start()\n\nap.save_overall_html(\n    dest_dir_path=\'./animation_fill_alpha_basic_usage/\')\n```',  # noqa

    '## animation_fill_alpha API':
    '## animation_fill_alpha API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Set the fill alpha (opacity) animation setting.<hr>':  # noqa
    '**[インターフェイス概要]** 塗りの透明度のアニメーションの設定を行います。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `alpha`: Number or float':
    '- `alpha`: Number or float',

    '  - The final alpha (opacity) of the animation.':
    '  - 透明度のアニメーションの最終値。',

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

    '- `animation_fill_alpha`: AnimationFillAlpha':
    '- `animation_fill_alpha`: AnimationFillAlpha',

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

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> circle: ap.Circle = sprite.graphics.draw_circle(\n...     x=100, y=100, radius=50)\n>>> _ = circle.animation_y(\n...     y=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> circle: ap.Circle = sprite.graphics.draw_circle(\n...     x=100, y=100, radius=50)\n>>> _ = circle.animation_y(\n...     y=100,\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)':  # noqa
    '- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/jp_animation_duration.html)',  # noqa

    '- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)':  # noqa
    '- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/jp_animation_return_value.html)',  # noqa

    '- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)':  # noqa
    '- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/jp_sequential_animation.html)',  # noqa

    '- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)':  # noqa
    '- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_animation_parallel.html)',  # noqa

    '- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)':  # noqa
    '- [イージングのenum](https://simon-ritchie.github.io/apysc/jp_easing_enum.html)',  # noqa

}
