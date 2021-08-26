from setuptools import setup

setup(
        name="markdown blog",
        version="0.1",
        long_description="Markdown blogging platform",
        packages=["mdblog"],
        zip_safe=False,
        include_package_data=True,
        install_requires=[
            "celery==5.1.2",
            "Flask==2.0.1",
            "Flask-SQLAlchemy==2.5.1",
            "Flask-WTF==0.15.1",
            "email-validator==1.1.3"
            ]
)