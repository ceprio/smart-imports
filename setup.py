
import setuptools

setuptools.setup(
    name='smart_imports',
    version='0.1.0',
    description='automatic importing for Python modules',
    url='https://github.com/Tiendil/smart-imports',
    author='Aleksey Yeletsky <Tiendil>',
    author_email='a.eletsky@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',

        'Natural Language :: English',
        'Natural Language :: Russian'],
    keywords=['python', 'impot'],
    packages=setuptools.find_packages(),
    install_requires=[],

    include_package_data=True,
    test_suite = 'tests' )
