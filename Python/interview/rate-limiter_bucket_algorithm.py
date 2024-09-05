from threading import Lock, Timer, Thread
import time
from random import randint

MAX_BUCKET_SIZE = 5
DEFAULT_REFILL_RATE = 2
DEFAULT_REFILL_INTERVAL = 5


class RateLimiter:
    buckets = 0

    def __init__(
            self,
            max_tokens=MAX_BUCKET_SIZE,
            rate=DEFAULT_REFILL_RATE,
            interval=DEFAULT_REFILL_INTERVAL,
            token="__TOKEN__"
    ):
        print(
            f"Rate-limiter bucket with a max-size of {max_tokens} Tokens created. \n"
            f"Token-creation happens at a rate of {rate} tokens every {interval}s. \n"
            f"----- Starting Logs -----")

        self.__lock = Lock()
        self.__max_tokens = max_tokens
        self.__rate = rate
        self.__interval = interval
        self.__token = token
        self.__bucket = [token] * max_tokens
        RateLimiter.buckets += 1
        self.__init_bucket()

    # Private methods

    def __init_bucket(self):
        self.__set_interval(self.__add_token, self.__interval)

    def __set_interval(self, func, sec):
        def func_wrapper():
            self.__set_interval(func, sec)
            func()

        t = Timer(sec, func_wrapper)
        t.start()
        return t

    def __add_token(self):
        with self.__lock:
            self.__bucket = self.__bucket + self.__generate_tokens()
            if len(self.__bucket) > self.__max_tokens:
                self.__bucket = self.__bucket[:self.__max_tokens]
            print(f"{"-" * 5} Bucket filled to {len(self.__bucket)} tokens {"-" * 5}")

    def __generate_tokens(self):
        # possibly generate tokens with patterns
        return [self.__token] * self.__rate

    def __token_available(self, request_tokens=1) -> bool:
        with self.__lock:
            if len(self.__bucket) >= request_tokens:
                if request_tokens == 1:
                    self.__bucket.pop()
                else:
                    self.__bucket = self.__bucket[:-2]
                return True
            return False

    # Public API

    def request_token(self):
        if self.__token_available():
            print(f"SUCCESS: {self.__token} granted", end="")
            return self.__token
        print("FAILED: Rate-limit reached.", end="")
        return None

    def available_tokens(self):
        with self.__lock:
            return len(self.__bucket)


def main():
    bucket = RateLimiter()

    while True:
        time_till_next_request = randint(1, 10) / 10 * 4
        time.sleep(time_till_next_request)
        bucket.request_token()
        print(f" ({bucket.available_tokens()} left)")


if __name__ == "__main__":
    main()
