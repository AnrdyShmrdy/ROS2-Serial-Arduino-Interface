from setuptools import setup

package_name = 'serial_controller'

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
    maintainer='Andy Ponce',
    maintainer_email='andy.ponce@outlook.com',
    description='serial controller node',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'controller = serial_controller.serial_controller:main',
        ],
    },
)
