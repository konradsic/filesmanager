from setuptools import setup

version = "0.0.1"
with open("requirements.txt", mode="r") as f:
    requirements = [req.strip("\n ") for req in f.readlines()]

with open("README.md", mode="r") as readme_file:
    long_description = readme_file.read()

packages = [
    "pyfiles"
]

setup(
    name="filesmanager",
    author="konradsic",
    url='https://github.com/konradsic/filemanager',
    project_urls = {
        "Issues and bugs": "https://github.com/konradsic/filemanager/issues"
    },
    version=version,
    packages=packages,
    license='MIT',
    description='A python package allowing users to easly manipulate and download files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    keywords = ["python", "files", "pyfiles", "file manipulation", "file", "filemanager"],
    python_requires='>=3.7.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Desktop Environment :: File Managers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)
