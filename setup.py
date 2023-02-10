from setuptools import setup
from age_dijkstra import VERSION 

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name             = 'apache-age-dijkstra',
    version          = VERSION.VERSION,
    description      = 'Dijkstra shortest path algorithm using apache age graph database',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author           = 'Moontasir Mahmood',
    author_email     = 'moontasir042@gmail.com',
    url              = 'https://github.com/Munmud/apache-age-dijkstra',
    license          = 'Apache2.0',
    install_requires = [ 'apache-age-python'],
    packages         = ['age_dijkstra',],
    keywords         = ['Graph Database', 'Apache AGE', 'PostgreSQL','Shotrtest path', 'Dijkstra'],
    python_requires  = '>=3.9',
    classifiers      = [
        'Programming Language :: Python :: 3.9'
    ]
)