# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['healthone.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('password_gen.py', '.'),
        ('response_function.py', '.'),
        ('file_io.py', '.'),
        ('crypt.py', '.'),
    ],
    hiddenimports=['cryptography.fernet'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['test', 'unittest', 'pdb', 'doctest'],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='healthone',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # 可以在这里添加图标文件路径
)
