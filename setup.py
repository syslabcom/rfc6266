from setuptools import setup

setup(
    author='Gabriel de Perthuis',
    author_email='g2p.code+rfc6266@gmail.com',
    description='Parse and generate Content-Disposition headers',
    url='https://github.com/g2p/rfc6266',
    keywords='rfc6266 Content-Disposition http attachments',
    name='rfc6266',
    version='0.0.4',  # semver
    license='GNU LGPL',
    platforms='OS-independent',
    py_modules=['rfc6266', 'test_rfc6266'],
    install_requires=['LEPL'],
    long_description=open('README').read(),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Topic :: Internet :: WWW/HTTP',
    ],
)

