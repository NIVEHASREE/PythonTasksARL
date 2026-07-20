try:
    with open("index.txt") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found error")


# custom exception
class FileManagementException(Exception):
    pass


class Files:
    def open_file(self, file_name):
        try:
            with open(file_name) as file:
                content = file.read()
            return content
        except:
            raise FileManagementException("file not found")


file_obj = Files()
try:
    print(file_obj.open_file("temp_file.txt"))
    print(file_obj.open_file("index.txt"))
except FileManagementException as e:
    print(e)
finally:
    print("File operations are completed")


# logging
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")
print(logging.getLogger(__name__))


class FileManagementException(Exception):
    pass


class Files:
    def open_file(self, file_name):
        try:
            with open(file_name) as file:
                content = file.read()
            return content
        except:
            logging.error("file not found")


file_obj = Files()
try:
    logging.info(file_obj.open_file("temp_file.txt"))
    logging.info(file_obj.open_file("index.txt"))
except FileManagementException as e:
    logging.exception("Couldnt open the file")
finally:
    logging.info("File operations are completed")
