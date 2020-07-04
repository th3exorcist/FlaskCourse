from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip()
        for req
        in open(filename).readlines()
    ]
setup(
    name ="iPudim",
    version = "0.1.0", #major, minor, patch
    description = "Delivery food",
    packages = ['iPudim'], #find_packages()
    include_package_data=True,
    install_requeries=["flask"],

)
