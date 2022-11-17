class request(object):
    def __init__(self):
        self.__count_of_failures = 0
        self.__sended_successfully = False

    def retry(self):
        if self.__sended_successfully or not self.__count_of_failures < 10:
            return False

        self.send()

        return self.retry()

    def send(self):
        self.__sended_successfully = True


print(request().if_more_than_ten_failures())
