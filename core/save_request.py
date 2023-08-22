import os


def save_request_to_file(user_id: int, request: str):
    folder_path = f'requests/{user_id}'
    os.makedirs(folder_path, exist_ok=True)
    file_path = f'{folder_path}/{user_id}_request.txt'
    with open(file_path, 'a') as file:
        file.write(request + '\n')
