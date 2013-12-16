try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(
    name = "grocerytrends",
    version = "0.1",
    author = "Jacob Hooey",
    author_email = "jacob@pompouspanda.com",
    description = ("A Python application that takes your grocery receipts "
                                "and analyses that data to give you trends"),
    license = "BSD",
    keywords = "finances trending personal",
    url = "https://github.com/jhooey/grocery-cart-trends",
    packages = ['grocerytrends', 'tests'],
    classifiers =
        [
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        ],
    )
