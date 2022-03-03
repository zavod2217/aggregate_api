from concurrent.futures import ThreadPoolExecutor, as_completed


class Thread:
    def __init__(self, func, params, thread_count=1, max_workers=1):
        self.func = func
        self.params = params
        self.thread_count = thread_count
        self.max_worker = max_workers
        self.results = []

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_worker) as pool:
            results = [pool.submit(self.func, self.params) for i in range(self.thread_count)]
            for future in as_completed(results):
                res = future.result()
                self.results.append(res)
        return self.results
