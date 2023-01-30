from setuptools import find_packages, setup
setup(
    name='modeval',
    packages=find_packages(include=['modeval']),
    version='0.0.1',
    description='Assess model quality',
    author='R-Palazzo',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.0'],
    test_suite='tests',
)