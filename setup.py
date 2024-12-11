from setuptools import setup, find_packages

setup(
    name='erasing_concepts_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        'torch',
        'diffusers',
        'transformers',
        'Pillow',
        'matplotlib',
        'numpy',
        'tqdm',
        'PyYAML',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A project to erase specific concepts from diffusion models.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/erasing_concepts_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
