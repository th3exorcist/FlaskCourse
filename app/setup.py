from setuptools import setup

setup(
    name ="iPudim",
    version = "0.0.1", #major, minor, patch
    description = "Delivery food",
    packages = ['iPudim'], #find_packages()
    include_package_data=True,
    install_requeries=["flask"],

)