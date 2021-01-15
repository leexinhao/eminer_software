# -*- mode: python ; coding: utf-8 -*-

import os
import importlib
block_cipher = None


a = Analysis(['test.py',
        'C:\\Users\\dell\\Desktop\\eminer_software_release\\T1_codes\\T1_AutoEncoder.py',
        'C:\\Users\\dell\\Desktop\\eminer_software_release\\T1_codes\\T1_Canopy.py',
        'C:\\Users\\dell\\Desktop\\eminer_software_release\\T1_codes\\T1_DataDrawer.py',
        'C:\\Users\\dell\\Desktop\\eminer_software_release\\T1_codes\\T1_DataReader.py',
        'C:\\Users\\dell\\Desktop\\eminer_software_release\\T2_codes\\T2_code\\S2SGRU.py',
        'C:\\Users\\dell\\Desktop\\eminer_software_release\\T2_codes\\T2_code\\T2_draw.py'
        ],
             pathex=['C:\\Users\\dell\\Desktop\\eminer_software_release'],
             binaries=[(os.path.join(os.path.dirname(importlib.import_module('tensorflow').__file__),
                              "lite/experimental/microfrontend/python/ops/_audio_microfrontend_op.so"),
                 "tensorflow/lite/experimental/microfrontend/python/ops/")],
             datas=[],
             hiddenimports=['matplotlib'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['zmq'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='test',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False,
          icon='Lightning.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=['.'],
               name='test')
