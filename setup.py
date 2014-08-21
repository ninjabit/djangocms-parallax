from setuptools import setup, find_packages
import io


def read(*filenames, **kwargs):
    """
    From http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
    """
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


setup(
    name="djangocms-parallax",
    version='0.1.1',
    description=read('DESCRIPTION.md'),
    long_description=read('README.md'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, django-cms, plugin, parallax, jquery',
    author='Olle Vidner',
    author_email='olle@vidner.se',
    url="https://github.com/ovidner/djangocms-parallax",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
        'South',
        'django-cms>=3.0.0',
        'django-sekizai'
    ],
)
