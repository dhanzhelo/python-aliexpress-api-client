try:
    import multiprocessing
except ImportError:
    pass


from setuptools import setup

setup(
    name='aliexpress-api-client',
    version='0.1.0',
    description='AliExpress API Client',
    url='https://github.com/kronas/python-aliexpress-api-client',
        
    author='Kronas',
    author_email='kronas.sw@gmail.com',
    license='MIT',

    packages=['aliexpress_api_client'],

    install_requires=[],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    zip_safe=False,
)
