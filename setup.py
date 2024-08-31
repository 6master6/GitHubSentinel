from setuptools import setup, find_packages

setup(
    name="GitHubSentinel",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "PyYAML",
        "schedule"
    ],
    entry_points={
        "console_scripts": [
            "github-sentinel=src.main:main",
        ]
    },
)
