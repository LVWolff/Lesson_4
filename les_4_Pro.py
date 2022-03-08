import datetime
from google_drive_downloader import GoogleDriveDownloader as gdd

def download_file(id, path):
    gdd.download_file_from_google_drive(file_id=id,
                                    dest_path='./'+path)

def fun_list_data(path):

    list_data = []

    with open(path) as file:
        for line in file:
            list_data.append(line.split(' - ')[0])

    return list_data


id = '1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8'
path = 'log.txt'

download_file(id, path)
list_data = fun_list_data(path)
print(list_data)

new_list_data = sorted(list_data)
print(new_list_data)
print("Самая поздняя дата/время записи в логе:", new_list_data[0])

# # реализация через конвертацию строки в дата время - лишнее
# def fun_str_dattime(date_time_str):
#     return datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S,%f')
# new_list_data = sorted(list(map(fun_str_dattime, list_data)))
# print(new_list_data)

