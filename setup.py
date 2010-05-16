from distutils.core import setup

setup(
    name='FormAlchemy2',
    version='0.1dev',
    description='FormAlchemy2 generates forms, validates and stores input data'
                'to your favorite backend.',
    author='Alexandre Conrad',
    author_email='alexandre conrad gmail com',
    url='http://formalchemy.org',
    packages=['formalchemy2', ],
    license='MIT License',
    long_description=open('README').read(),
)
