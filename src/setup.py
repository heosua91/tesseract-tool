from setuptools import setup

setup(
    name='TesseractOCRTool',
    version='1.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tocrtool=cli:cli
    ''',
)