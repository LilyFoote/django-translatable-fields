from setuptools import setup, find_packages


install_requires = (
    'django-hstore>=1.3,<1.4',
    'langcodes>=1.0,<1.1',
)

extras_require = {
    'rest': [
        'djangorestframework-hstore>=1.1,<1.2',
    ],
}


classifiers = (
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Internationalization',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
)


setup(
    name='django-translatable-fields',
    packages=find_packages(),
    include_package_data=True,
    version='0.0.0',
    description='',
    author='Incuna',
    author_email='admin@incuna.com',
    url='',
    install_requires=install_requires,
    extras_require=extras_require,
    license='MIT',
    classifiers=classifiers,
    zip_safe=False,
)
