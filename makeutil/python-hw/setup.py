from pathlib import Path
from setuptools import setup

HERE = Path(__file__).parent

readme_path = HERE / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else "FOSSDEV python-hw example package."

setup(
    name="fossdev-makeutil",
    version="0.1.0",
    description="Example utilities for FOSSDEV homework with make (module examples in src/)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asutenshi/fossdev/tree/feature/makeutil-pypi-release/makeutil/python-hw",
    author="Asu Tenshi",
    author_email="you@example.com",
    py_modules=["app", "calc", "example", "service"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests",
        "numpy",
        "fastapi",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/asutenshi/fossdev/tree/feature/makeutil-pypi-release/makeutil/python-hw",
    },
)
