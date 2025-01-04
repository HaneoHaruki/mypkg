from setuptools import setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Haruki Haneo',
    maintainer_email='s23C1111TB@s.chibakoudai.jp',
    description='robosyssample',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'weatherpublisher = mypkg.weatherpublisher:main',
            'listener = mypkg.listener:main',
        ],
    },
)
