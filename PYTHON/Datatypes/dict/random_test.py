data = {
    "count": 25,
    "next": "/api/v3/projects/?limit=10&offset=10",
    "previous": None,
    "results": [{
        "id": 12345,
        "name": "Pip",
        "slug": "pip",
        "created": "2010-10-23T18:12:31+00:00",
        "modified": "2018-12-11T07:21:11+00:00",
        "language": {
            "code": "en",
            "name": "English"
        },
        "programming_language": {
            "code": "py",
            "name": "Python"
        },
        "repository": {
            "url": "https://github.com/pypa/pip",
            "type": "git"
        },
        "default_version": "stable",
        "default_branch": "master",
        "subproject_of": None,
        "translation_of": None,
        "urls": {
            "documentation": "http://pip.pypa.io/en/stable/",
            "home": "https://pip.pypa.io/"
        },
        "tags": [
            "distutils",
            "easy_install",
            "egg",
            "setuptools",
            "virtualenv"
        ],
        "users": [
            {
                "username": "dstufft"
            }
        ],
        "active_versions": {
            "stable": "{VERSION}",
            "latest": "{VERSION}",
            "19.0.2": "{VERSION}"
        },
        "_links": {
            "_self": "/api/v3/projects/pip/",
            "versions": "/api/v3/projects/pip/versions/",
            "builds": "/api/v3/projects/pip/builds/",
            "subprojects": "/api/v3/projects/pip/subprojects/",
            "superproject": "/api/v3/projects/pip/superproject/",
            "redirects": "/api/v3/projects/pip/redirects/",
            "translations": "/api/v3/projects/pip/translations/"
        }
    }]
}

for version in data['results'][0]['_links'].values():
    print(version)



