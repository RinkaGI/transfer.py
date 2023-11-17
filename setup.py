from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='transferpy',
    packages=['transferpy'],
    version='1.0',
    description='Use transfer.sh in python',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='RinkaDev',
    author_email='rinkadevoficial@gmail.com',
    url='https://github.com/RinkaGI/transfer.py',
    download_url='https://github.com/RinkaGI/transfer.py/tarball/1.0',
    keywords=['transfer', 'upload', 'cloud'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)