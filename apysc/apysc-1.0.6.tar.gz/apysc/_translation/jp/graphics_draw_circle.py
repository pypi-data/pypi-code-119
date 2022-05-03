"""This module is for the translation mapping data of the
following document:

Document file: graphics_draw_circle.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Graphics draw_circle interface':
    '# Graphics クラスの draw_circle インターフェイス',

    'This page explains the `Graphics` class `draw_circle` method interface.':  # noqa
    'このページでは`Graphics`クラスの`draw_circle`メソッドのインターフェイスについて説明します。',

    '## What interface is this?':
    '## インターフェイス概要',

    '`draw_circle` interface draws the vector circle graphics.':
    '`draw_circle`インターフェイスはベクターグラフィックスの円を描画します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The `draw_circle` interface has the `x`\\, `y`\\, and `radius` arguments.':  # noqa
    '`draw_circle`インターフェイスは`x`と`y`、そして`radius`引数を持っています。',

    'The `x` and `y` arguments are the circle center coordinates, and the `radius` argument determines the circle size. The width and height become twice the `radius` value.':  # noqa
    '`x`と`y`引数は円の中央座標となります。`radius`引数は円の半径となります、幅と高さは`radius`引数の2倍の値になります。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=350,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan color and draw the circle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_circle(x=100, y=100, radius=50)\n\n# Set the dotted-line style and draw the circle.\nsprite.graphics.begin_fill(color=\'\')\nsprite.graphics.line_style(\n    color=\'#fff\', thickness=3, dot_setting=ap.LineDotSetting(dot_size=3))\nsprite.graphics.draw_circle(x=250, y=100, radius=50)\n\n# Draw the inner circle.\nsprite.graphics.draw_circle(x=250, y=100, radius=25)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_circle_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=350,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Set the cyan color and draw the circle.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_circle(x=100, y=100, radius=50)\n\n# Set the dotted-line style and draw the circle.\nsprite.graphics.begin_fill(color=\'\')\nsprite.graphics.line_style(\n    color=\'#fff\', thickness=3, dot_setting=ap.LineDotSetting(dot_size=3))\nsprite.graphics.draw_circle(x=250, y=100, radius=50)\n\n# Draw the inner circle.\nsprite.graphics.draw_circle(x=250, y=100, radius=25)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_circle_basic_usage/\')\n```',  # noqa

    '## Return value':
    '## 返却値',

    'The return value of the `draw_circle` interface is the instance of the `Circle` class.':  # noqa
    '`draw_circle`インターフェイスの返却値は`Circle`クラスのインスタンスとなります。',

    'It has the `radius` attribute or other basic interfaces and you can change these settings.':  # noqa
    'このインスタンスは`radius`属性や他の基本的な各インターフェイスを持っており生成後に値を更新することができます。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=400,\n    stage_height=400,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the small radius circle.\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=200, y=200, radius=25)\n\n# Update circle radius to become the bigger one.\ncircle.radius = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_circle_return_value/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=400,\n    stage_height=400,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw the small radius circle.\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=200, y=200, radius=25)\n\n# Update circle radius to become the bigger one.\ncircle.radius = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'graphics_draw_circle_return_value/\')\n```',  # noqa

    '## draw_circle API':
    '## draw_circle API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Draw a circle vector graphics.<hr>':
    '**[インターフェイス概要]** 円のベクターグラフィックスを描画します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `x`: Int or int':
    '- `x`: Int or int',

    '  - X-coordinate of the circle center.':
    '  - 円の中心のX座標。',

    '- `y`: Int or int':
    '- `y`: Int or int',

    '  - Y-coordinate of the circle center.':
    '  - 円の中心のY座標。',

    '- `radius`: Int or int':
    '- `radius`: Int or int',

    '  - Circle radius.':
    '  - 円の半径。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `circle`: Circle':
    '- `circle`: Circle',

    '  - Created circle graphics instance.':
    '  - 生成された円のグラフィックスのインスタンス。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> circle: ap.Circle = sprite.graphics.draw_circle(\n...     x=100, y=100, radius=50)\n>>> circle.x\nInt(100)\n\n>>> circle.y\nInt(100)\n\n>>> circle.radius\nInt(50)\n\n>>> circle.fill_color\nString(\'#00aaff\')\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> circle: ap.Circle = sprite.graphics.draw_circle(\n...     x=100, y=100, radius=50)\n>>> circle.x\nInt(100)\n\n>>> circle.y\nInt(100)\n\n>>> circle.radius\nInt(50)\n\n>>> circle.fill_color\nString(\'#00aaff\')\n```',  # noqa

}
