from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).resolve().parent

# Попытка загрузить README.md для long_description (twine проверяет рендеринг)
readme_path = here / "README.md"
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")
    long_description_content_type = "text/markdown"
else:
    long_description = "Short package description."
    long_description_content_type = "text/plain"

setup(
    name="ndfl-soft-dev",
    version="0.0.0",
    description="Краткое описание вашего пакета ndfl",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author="Your Name",
    author_email="you@example.com",
    url="https://example.org/ndfl",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="ndfl example",
    install_requires=[],
    project_urls={
        "Source": "https://example.org/ndfl/source",
        "Tracker": "https://example.org/ndfl/issues",
    },
)
