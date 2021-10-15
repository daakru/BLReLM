import PyInstaller.__main__
from os import system
import fileinput
import re

# PyInstaller.__main__.run([
#     'blrevive_loadout_manager.py',
#     '--clean',
#     '--onefile',
#     '--windowed',
#     '--add-data=resource;resource',
#     '--add-data=data;data',
#     '--add-data=helpers_pyinstaller.py;.',
#     '--add-data=__WXFB_BLR_LMGR.py;.',
#     '--add-data=blrevive_gear.py;.',
#     '--add-data=bitmap_panel.py;.',
#     '--add-data=blrevive_toolkit.py;.',
#     '--add-data=writable_string_object.py;.',
#     '--splash=resource/images/splash.png'
# ])


def make_specfile():
    options = [
        '--onefile',
        '--windowed',
        '--hidden-import=wso.py;.',
        '--add-data=helpers_pyinstaller.py;.',
        '--add-data=ue3_config_reader.py;.',
        '--add-data=__WXFB_BLR_LMGR.py;.',
        '--add-data=blrevive_gear.py;.',
        '--add-data=bitmap_panel.py;.',
        '--add-data=blrevive_toolkit.py;.',
        '--add-data=resource/FoxGame;FoxGame',
        '--add-data=resource/images;images',
        '--add-data=resource/fonts;fonts',
        '--add-data=data;data',
        '--splash=resource/images/BLReLM_splash.png',
        '--icon=resource/images/BLReLM.ico'
    ]

    excluded_modules = [
        'IPython',
        'jedi',
        'parso',
        'zmq',
        'difflib',
        'distutils',
        'lib2to3',
        'pkg_resources',
        'PIL',
        'pygments',
        'setuptools',
        'sqlite3',
        'sysconfig',
        'wcwidth',
        'xml',
        '_tkinter',
        'pythoncom',
        'pywintypes',
        'pandas.io.formats.style',
        'win32com'
    ]

    # required_modules = [
    #     'wx.xrc',
    #     'encodings',
    #     'numpy',
    #     'numpy._pytesttester',
    #     'pandas',
    #     'pytz',
    #     'pickle',
    #     'heapq',
    #     'multiprocessing.util'
    # ]

    # pyoptimize = 'set PYTHONOPTIMIZE=1 && '
    pyoptimize = ''
    excstr = ' '.join([f'--exclude-module {m}' for m in excluded_modules])
    optstr = ' '.join(options)
    command = 'pyi-makespec'
    file = 'blrevive_loadout_manager.py'
    cmdstr = f'{pyoptimize}{command} {optstr} {excstr} {file}'
    system(cmdstr)


def patch_specfile(filename='blrevive_loadout_manager.spec'):
    def handle_target_block(target, line):
        if target == 'splash':
            # Handle splash filepath
            # <splash = Splash('resource/images/BLReLM_splash.png',\r\n>
            if line.startswith('splash'):
                return line  # comment out to modify
                pattern = '\'.*\''
                replace = '\'resource/images/splash.png\''
                res_str = re.sub(pattern, replace, line)
                return res_str

            # Handle splash 'binaries'
            # </indent><binaries=a.binaries,\r\n>
            elif line.strip().startswith('binaries'):
                return line  # comment out to modify
                # Implement modifications here

            # Handle splash 'datas'
            # </indent><datas=a.datas,\r\n>
            elif line.strip().startswith('datas'):
                return line  # comment out to modify
                # Implement modifications here

            # Handle splash 'text_pos'
            # </indent><text_pos=None,\r\n>
            elif line.strip().startswith('text_pos'):
                # return line  # comment out to modify
                # Implement modifications here
                pattern = '= *[^,]*'
                replace = '=(104, 190)'  # 62
                res_str = re.sub(pattern, replace, line)
                return res_str

            # Handle splash 'text_size'
            # </indent><text_size=12,\r\n>
            elif line.strip().startswith('text_size'):
                # return line  # comment out to modify
                # Implement modifications here
                pattern = '= *[^,]*'
                replace = '=8'
                res_str = re.sub(pattern, replace, line)

                indentation = line.split('t')[0]
                extra_lines = indentation + 'text_color=\'white\',\n'
                extra_lines += indentation + 'max_img_size=(640, 192),\n'

                return res_str + extra_lines

            # Handle splash 'minify_script'
            # </indent><minify_script=True)\r\n>
            elif line.strip().startswith('minify_script'):
                return line  # comment out to modify
                # Implement modifications here

        return line

    in_target_block = False
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as fi:
        for line in fi:
            if not in_target_block:
                if line.startswith('splash'):
                    in_target_block = 'splash'
                rep = handle_target_block(in_target_block, line)
                if rep is not None:
                    print(rep, end='')
            elif in_target_block == 'splash':
                rep = handle_target_block(in_target_block, line)
                if rep is not None:
                    print(rep, end='')
                if line.endswith(')\r\n'):
                    in_target_block = False
                    return


def build_exec(clean=False):
    # optstr = ''
    # command = 'pyinstaller'
    # specfile = 'blrevive_loadout_manager.spec'
    # if clean:
    #     optstr += ' --clean'
    # cmdstr = f'set PYTHONOPTIMIZE=1 && {command}{optstr} {specfile}'
    # system(cmdstr)
    if clean:
        PyInstaller.__main__.run([
            'blrevive_loadout_manager.spec',
            '--clean'
        ])
    else:
        PyInstaller.__main__.run([
            'blrevive_loadout_manager.spec'
        ])


if __name__ == '__main__':
    make_specfile()
    patch_specfile()
    build_exec(True)
