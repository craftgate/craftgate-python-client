# setup.py
import io
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)


def read(relpath, encoding="utf-8"):
    with io.open(os.path.join(here, relpath), "r", encoding=encoding) as f:
        return f.read()


version_ns = {}
exec(read("_version.py"), version_ns)

setup(
    name="craftgate",
    version=version_ns["VERSION"],
    description="Python client for Craftgate API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Craftgate",
    author_email="dev@craftgate.io",
    url="https://github.com/craftgate/craftgate-python-client",
    license="MIT",
    keywords=["craftgate", "payments", "api", "client", "sdk"],
    packages=find_packages(include=["craftgate*"], exclude=["tests", "tests.*"]),
    py_modules=["_version"],
    package_data={"craftgate": ["py.typed"]},
    zip_safe=False,
    install_requires=[
        "requests>=2.20,<2.26; python_version < '3.6'",
        "requests>=2.20; python_version >= '3.6'",
        'typing_extensions<4; python_version < "3.8"',
    ],
    python_requires=">=3.5",
    extras_require={
        "dev": [
            "pytest>=6",
            "black==22.3.0; python_version >= '3.6'",
            "ruff; python_version >= '3.7'",
            "mypy; python_version >= '3.7'",
            "build",
            "twine",
        ]
    },
    project_urls={
        "Documentation": "https://developer.craftgate.io",
        "Source Code": "https://github.com/craftgate/craftgate-python-client",
        "Bug Tracker": "https://github.com/craftgate/craftgate-python-client/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
