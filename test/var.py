import os


WORKINGDIR = os.getcwd()


class env:
    base_url = "http://vectorpng.com"
    login = "{0}/login".format(base_url)
    upload = "{0}/post".format(base_url)

    exclude_file = [
        "page",
        "dock_fotos.txt",
        "dock_vectores.txt",
        "dock_psd.txt",
        ".git",
        "__pycache__"
    ]

    image_field_name = "pic_url"

    zip_field_name = "file_zip"

    download_dir = "{0}/download/".format(WORKINGDIR)


class path:
    files = "{0}/files/".format(WORKINGDIR)


class test:
    path_dir = "{0}/download/vectores".format(WORKINGDIR)
