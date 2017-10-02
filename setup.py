from setuptools import setup, find_packages

setup(name='soccer_strategy',
      version='0.0.1',
      description='A visual demonstration for soccer strategy',
      author='Thanh Vu',
      author_email='',
      url='https://github.com/thanhvu262/soccer-plan',
      license='MIT',
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 3.5',
      ],
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      python_requires='>=3.4',
     )
