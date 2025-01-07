# from locust import HttpUser, TaskSet, task, between

# class GamingTasks(TaskSet):
#     @task(2)
#     def get_gaming_home(self):
#         self.client.get("/gaming/")

#     @task(1)
#     def post_gaming_data(self):
#         self.client.post("/gaming/", json={"data": "test"})

# class VideoStreamingTasks(TaskSet):
#     @task(2)
#     def get_video_streaming_home(self):
#         self.client.get("/")

#     @task(1)
#     def post_video_streaming_data(self):
#         self.client.post("/", json={"data": "test"})

# class GamingUser(HttpUser):
#     tasks = [GamingTasks]
#     wait_time = between(1, 5)

# class VideoStreamingUser(HttpUser):
#     tasks = [VideoStreamingTasks]
#     wait_time = between(1, 5)

# from locust import HttpUser, TaskSet, task, between

# class GamingTasks(TaskSet):
#     @task(2)
#     def get_gaming_home(self):
#         self.client.get("/gaming/")

#     @task(1)
#     def post_gaming_data(self):
#         self.client.post("/gaming/", json={"data": "test"})

# class VideoStreamingTasks(TaskSet):
#     @task(2)
#     def get_video_streaming_home(self):
#         self.client.get("/")

#     @task(1)
#     def post_video_streaming_data(self):
#         self.client.post("/", json={"data": "test"})

# class CombinedTasks(TaskSet):
#     tasks = {GamingTasks: 1, VideoStreamingTasks: 1}

# class CombinedUser(HttpUser):
#     tasks = [CombinedTasks]
#     wait_time = between(1, 5)

from locust import HttpUser, TaskSet, task, between

class GamingTasks(TaskSet):
    @task(2)
    def get_gaming_home(self):
        self.client.get("/gaming/")

    @task(1)
    def post_gaming_data(self):
        self.client.post("/gaming/", json={"data": "test"})

class VideoStreamingTasks(TaskSet):
    @task(2)
    def get_video_streaming_home(self):
        self.client.get("/video_streaming/")

    @task(1)
    def post_video_streaming_data(self):
        self.client.post("/video_streaming/", json={"data": "test"})

class CombinedTasks(TaskSet):
    tasks = {GamingTasks: 1, VideoStreamingTasks: 1}

class CombinedUser(HttpUser):
    tasks = [CombinedTasks]
    wait_time = between(1, 5)