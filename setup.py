from distutils.core import setup

setup(name='verfcoderecognizer',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='http://www.python.org/sigs/distutils-sig/',
      include_package_data = True,
      packages=['verfcoderecognizer'],
      data_files=[('Lib\\site-packages\\verfcoderecognizer\\YYU', ['YYU\VCR.dll'])]
      )
