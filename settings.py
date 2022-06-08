TEST = True

""" name1 """
Test_TOKEN = 'token'
folder_path_test = ''
""" name2 """
TOKEN = 'token'
folder_path = ''

URL = ''


def test():
    if TEST is True:
        return Test_TOKEN
    elif TEST is False:
        return TOKEN


def folder():
    if TEST is True:
        return folder_path_test
    elif TEST is False:
        return folder_path

