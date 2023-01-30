from setuptools import find_packages, setup

tests_require = [
    'pytest>=3.4.2',
    'pytest-cov>=2.6.0',
    'pytest-rerunfailures>10',
    'jupyter>=1.0.0,<2',
    'rundoc>=0.4.3,<0.5',
]
setup(
    name='modeval',
    packages=find_packages(include=['modeval']),
    version='0.0.1',
    description='Assess model quality',
    author='R-Palazzo',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require= tests_require,
    test_suite='tests',
)