import setuptools

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "special2text"

setuptools.setup(
    name="special2text",  # Replace with your own PyPI username(id)
    version="0.1.0",
    license="MIT",
    author="Tanat",
    author_email="shrbwjd05@naver.com",
    description="special2text is a package that converts special characters to nomal text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KR-korcen/korcen",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "special2text=special2text.special2text:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Source': 'https://github.com/KR-korcen/korcen',
        'Tracker': 'https://github.com/KR-korcen/korcen/issues',
    },
)
