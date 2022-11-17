class request(object):
    def __init__(self):
        self.__count_of_failures = 0
        self.__sended_successfully = False

    def if_more_than_ten_failures(self):
        return self.__count_of_failures >= 10

    def can_retry(self):
        if self.if_more_than_ten_failures():
            return False
        else:
            return True

    def retry(self):
        if self.__sended_successfully or not self.can_retry():
            return False

        self.send()

        return self.retry()

    def send(self):
        self.__sended_successfully = True


print(request().if_more_than_ten_failures())
