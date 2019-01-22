import os
from var import env
from zipfile import ZipFile


def get_files(path):
    list_files = os.listdir(path)
    return [os.path.normpath(path + '/' + file) for file in list_files if not file in env.exclude_file]


def get_pic_file(list_files):
    pic_file = [file for file in list_files if '.png' in file
                or '.jpg' in file
                or '.jpeg' in file
                or '.bmp' in file]
    assert len(pic_file) == 1
    return os.path.realpath(pic_file.pop(0))


def get_zip_file(list_files):
    zip_file = [file for file in list_files if '.zip' in file]
    assert len(zip_file) == 1
    return os.path.realpath(zip_file.pop(0))


def get_name_from_path(path):
    if path[-1] == "\\" or path[-1] == "/":
        path = path[0: len(path)-1]
    return os.path.basename(path)


def get_path_files(path):

    if path[-1] != "/":
        path = path + "/"
    # path = os.path.normpath(path)
    print(path)
    file_path = []
    for root, dicrectory, files in os.walk(path):
        for file in files:
            file_path.append(root + file)
    return file_path


def create_zip_file(path):
    name = get_name_from_path(path)
    path_zip_file = os.path.join(path, f"{name}.zip")
    list_files = get_path_files(path)
    print(list_files)
    with ZipFile(path_zip_file, "w") as w:
        for file in list_files:
            w.write(file)
    print("######WRITE FILE ZIP SUCCESS#######")


def make_zip_to_post(path):
    list_files = get_files(path)
    zip_file = get_zip_file(list_files)
    # get file_name
    zip_name = get_name_file(zip_file)
    zip_info = (zip_name, open(zip_file, "rb"), 'application/zip')

    zip_tuple = (env.zip_field_name, zip_info)
    return zip_tuple


def make_pic_to_post(path):
    list_files = get_files(path)
    pic_file = get_pic_file(list_files)
    # get content-type
    mimme_type = make_mimme_type(pic_file)
    pic_name = get_name_file(pic_file)
    pic_info = (pic_name, open(pic_file, "rb"), mimme_type)

    pic_tuple = (env.image_field_name, pic_info)
    return pic_tuple


def get_pic_name(path):
    list_files = get_files(path)
    pic_file = get_pic_file(list_files)

    pic_name = get_name_file(pic_file)
    return pic_name


def get_zip_name(path):
    list_files = get_files(path)
    zip_file = get_zip_file(list_files)

    zip_name = get_name_file(zip_file)
    return zip_name


def make_mimme_type(image):
    extensive = os.path.splitext(image)[1]
    extensive = extensive.replace(".", "")
    return "image/{0}".format(extensive)


def get_name_file(file):
    shortname = os.path.split(file)[0]
    return shortname


def make_data(path, _token, category_id):
    name = get_name_from_path(path)
    pic_name = get_pic_name(path)
    zip_name = get_zip_name(path)

    return {
                "user_id": 1,
                "delete_img": "",
                "pic": 1,
                "title": name,
                "category_id": category_id,
                "pic_url": pic_name,
                "file_zip": zip_name,
                "body": name,
                "link_url": name,
                "tags": "",
                "_token":  _token
            }


# >>> url = 'https://httpbin.org/post'
# >>> multiple_files = [
#         ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
#         ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
# >>> r = requests.post(url, files=multiple_files)
# >>> r.text

try:
    pass
    # listfile = get_files("./Blank-rectangle-pink-roses-frame-on-pink-and-white-background")
    # print(get_pic_file(listfile))
    # create_zip_file("./Blank-rectangle-pink-roses-frame-on-pink-and-white-background")
    # make_zip_to_post("C:\\Users\\titihacker\\Desktop\\all_ninja_media\\downloadApi\\upload-website\\download\\vectores\\Blank-rectangle-pink-roses-frame-on-pink-and-white-background")
except Exception as e:
    print("#####EXCEPTION####")
    print(e)
"""user_id=1&delete_img=&pic=1&title=tesst_upload&category_id=2&pic_url=63860.jpg&file_zip=Blank-rectangle-pink-roses-frame-on-pink-and-white-background.zip&body=aaaa&link_url=aa&tags=aaaa&_token=oqnbNaAY31x1hVUmkDvceaEYgPJECKik8XKNvmyy"""
