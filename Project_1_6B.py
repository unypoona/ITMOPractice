'''Изучить в https://pythontutor.com/ пример square root вычисления квадратного корня 						и понять почему продолжаются вычисления? И когда они заканчиваются?						тренировочное
Контрольные задания по итогам каждого модуля												Project 1_6B	6B'''

import os
import logging
import datetime

def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def read_file_with_encoding(file_path, encodings=['utf-8', 'cp1251']):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read(), encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Cannot decode file {file_path} with any of the provided encodings.")


def copy_csv_files(file_list, source_directory, destination_directory):
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
    combined_filename = os.path.join(destination_directory, f"{current_time}_copy_content.txt")
    any_files_copied = False

    for filename in file_list:
        source_file = os.path.join(source_directory, filename)
        try:
            content, encoding_used = read_file_with_encoding(source_file)
            if not any_files_copied:
                with open(combined_filename, 'w', encoding='utf-8') as combined_file:
                    combined_file.write(content + '\n')
                any_files_copied = True
            else:
                with open(combined_filename, 'a', encoding='utf-8') as combined_file:
                    combined_file.write(content + '\n')
            logging.info(f"Successfully copied: {filename}")
        except FileNotFoundError:
            logging.error(f"File not found: {filename}")
        except UnicodeDecodeError:
            logging.error(f"Error copying file {filename}: cannot decode with provided encodings")
        except Exception as e:
            logging.error(f"Error copying file {filename}: {str(e)}")

    if not any_files_copied:
        logging.info("No files were found to copy, combined file was not created.")


if __name__ == "__main__":

    file_list = ["file1.csv", "input.csv", "bikes.csv"]

    source_directory = ""
    destination_directory = ""
    log_file = "copy_log.log"

    # Setup logging
    setup_logging(log_file)

    # Copy files
    copy_csv_files(file_list, source_directory, destination_directory)