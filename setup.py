from setuptools import setup

setup(
    name="lan",
    version='0.0.1',
    description="Lan(懒)是一套测试框架 .",
    long_description="Lan(懒)是一套测试框架 .",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
    ],
    keywords='lan python test',
    author='BIJ',
    author_email='bobofpl@gmail.com',
    url='https://github.com/bbfpl/Lan',
    license='MIT',
    packages=['core', 'core.commands'],
    entry_points=dict(console_scripts=['lan=core.cli:main']),
    install_requires=[
        'requests'
    ],
    zip_safe=False)
