# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/16 22:02
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""


class CPMelBaseException(Exception): pass
class CPMelException(CPMelBaseException): pass


class RefException(CPMelBaseException): pass


class ArgConvException(CPMelBaseException): pass


class ArgConvTypeException(ArgConvException): pass
