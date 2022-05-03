import os
import sys
from .__config__ import _ask, QproConfig, QproDefaultConsole

if sys.platform.startswith('win'):
    is_win = True
    dir_char = '\\'
else:
    is_win = False
    dir_char = '/'

user_root = os.path.expanduser('~')
_qpro_config = QproConfig(user_root + dir_char + '.qprorc', os.path.exists(user_root + dir_char + '.qprorc'))

try:
    import QuickStart_Rhy
    qs_flag = True
except:
    qs_flag = False

user_lang = _qpro_config.select('default_language')
user_pip = _qpro_config.select('default_pip')
QproErrorString = '[bold red][ERRO]' if user_lang != 'zh' else '[bold red][错误]'
QproInfoString = '[bold cyan][INFO]' if user_lang != 'zh' else '[bold cyan][提示]'
QproWarnString = '[bold yellow][WARN]' if user_lang != 'zh' else '[bold yellow][警告]'
name = 'QuickProject'
configure_name = 'project_configure.json'


def __latest_filename(filename):
    import os

    cur = os.getcwd()
    rec = cur
    while cur != dir_char:
        if os.path.exists(filename):
            os.chdir(rec)
            return os.path.abspath(cur + dir_char + filename)
        os.chdir('..')
        last = cur
        cur = os.getcwd()
        if cur == last:
            break
    os.chdir(rec)
    return ''


if ' '.join(sys.argv[:2]) != 'Qpro -init':
    rt_dir = os.path.dirname(__latest_filename(configure_name)) + dir_char
    if rt_dir == dir_char:
        rt_dir = os.path.abspath('.') + dir_char
else:
    rt_dir = os.path.abspath('.')
project_configure_path = rt_dir + configure_name


def __sub_path(path, isExist=True):
    if not os.path.exists(path) and isExist:
        return ''
    abs_path = os.path.abspath(path)
    return abs_path.replace(rt_dir, '') if abs_path.startswith(rt_dir) else ''


def requirePackage(pname: str, module: str = "", real_name: str = "", not_exit: bool = True, not_ask: bool = False, set_pip: str = user_pip):
    """
    获取本机上的python第三方库

    :param pname: 库名
    :param module: 待引入的模块名，可缺省
    :param real_name: 用于 pip3 install 的名字
    :param not_exit: 安装后不退出
    :return: 库或模块的地址
    """
    try:
        exec(f'from {pname} import {module}' if module else f"import {pname}")
    except (ModuleNotFoundError, ImportError):
        if not_ask:
            return None
        confirm = _ask({
            'type': 'confirm',
            'name': 'install',
            'message': f"""Qs require {pname + (' -> ' + module if module else '')}, confirm to install?  
  Qs 依赖 {pname + (' -> ' + module if module else '')}, 是否确认安装?""",
            'default': True})
        if confirm:
            os.system(f'{set_pip} install {pname if not real_name else real_name} -U')
            if not_exit:
                exec(f'from {pname} import {module}' if module else f"import {pname}")
            else:
                QproDefaultConsole.print(QproInfoString, f'just run again: "{" ".join(sys.argv)}"' if user_lang != 'zh' else f'请重新运行: "{" ".join(sys.argv)}"')
                exit(0)
        else:
            exit(-1)
    finally:
        return eval(f'{module if module else pname}')


class SshProtocol:
    @staticmethod
    def post_folder(user, domain, target, port, srcPath, dstPath):
        if user:
            status = os.system(
                'scp -P %s -r %s %s' % (port, srcPath, user + '@\\[' + domain + '\\]:' + target + dstPath))
        else:
            status = os.system('scp -P %s -r %s %s' % (port, srcPath, '\\[' + domain + '\\]:' + target + dstPath))
        return status

    @staticmethod
    def post_file(user, domain, target, port, srcPath, dstPath):
        if user:
            status = os.system('scp -P %s %s %s' % (port, srcPath, user + '@\\[' + domain + '\\]:' + target + dstPath))
        else:
            status = os.system('scp -P %s %s %s' % (port, srcPath, '\\[' + domain + '\\]:' + target + dstPath))
        return status

    @staticmethod
    def post_all_in_folder(user, domain, target, port, dstPath):
        if user:
            status = os.system('scp -P %s -r * %s' % (port, user + '@\\[' + domain + '\\]:' + target + dstPath))
        else:
            status = os.system('scp -P %s -r * %s' % (port, '\\[' + domain + '\\]:' + target + dstPath))
        return status

    @staticmethod
    def get_file_or_folder(user, domain, target, port, srcPath, dstPath):
        if user:
            return os.system('scp -P %s -r %s %s' % (port, user + '@\\[' + domain + '\\]:' + target + srcPath, dstPath))
        else:
            return os.system('scp -P %s -r %s %s' % (port, '\\[' + domain + '\\]:' + target + srcPath, dstPath))

    @staticmethod
    def command(user, domain, target, port, command):
        if user:
            return os.system(
                'ssh -p {port} {user}@{domain} "cd {target} ; {command}"'.format(
                    port=port, user=user, domain=domain, target=target, command=command
                )
            )
        else:
            return os.system(
                'ssh -p {port} {domain} "cd {target} ; {command}"'.format(
                    port=port, domain=domain, target=target, command=command
                )
            )

    @staticmethod
    def ssh(user, domain, target, port, dstPath):
        if user:
            return os.system(
                "ssh -p {port} -t {user}@{domain} 'cd {aim} ; exec $SHELL -l'".format(
                    port=port, user=user, domain=domain, aim=target + dstPath
                )
            )
        else:
            return os.system(
                "ssh -p {port} -t {domain} 'cd {aim} ; exec $SHELL -l'".format(
                    port=port, domain=domain, aim=target + dstPath
                )
            )


def menu_output(menu):
    from rich.table import Table, Column
    from rich.box import SIMPLE

    tb = Table(*[Column('Parameter', justify='full', style='bold yellow'),
                 Column('Description', justify='right', style='bold cyan')],
               show_edge=False, show_header=False, row_styles=['none', 'dim'], box=SIMPLE, pad_edge=False,
               title='[bold underline] {title}[dim]Author: RhythmLian\n'.format(title=menu['title']))
    for line in menu['lines']:
        tb.add_row((menu['prefix'] + ' ' if line[0].startswith('-') else '') + line[0], line[1])
    QproDefaultConsole.print(tb, justify='center')
    QproDefaultConsole.print(
        '\nDOC:' if user_lang != 'zh' else '\n文档:', 'https://rhythmlian.cn/2020/02/14/QuickProject/', justify='center'
    )


def get_config(without_output: bool = False):
    config_path = __latest_filename('project_configure.json')
    config = {}
    if config_path:
        import json
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        if not without_output:
            QproDefaultConsole.print(
                QproErrorString,
                "No file named: project_configure.json\n May you need run:\"Qpro -init\" first!"
                if user_lang != 'zh' else
                "没有文件: project_configure.json\n可能你需要先运行: \"Qpro -init\"!"
            )
        exit(0)
    return config


def get_server_target(st=None):
    try:
        if not st:
            config = get_config()['server_target']
            ls, port = config[0].split(':'), config[1]
        else:
            ls, port = st[0].split(':'), st[1]
    except IndexError:
        QproDefaultConsole.print(QproErrorString, 'Didn\'t set server_target!' if user_lang != 'zh' else '未配置远程映射!')
        exit(0)
    else:
        if len(ls) > 2:
            server = ':'.join(ls[:8])
            target = ':'.join(ls[8:])
        else:
            server, target = ls
        return server, target, port
