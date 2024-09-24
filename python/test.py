# import json

# class ContentItem:
#     def __init__(self, content, author):
#         self.content = content
#         self.author = author
#         self.comments = []
#         self.likes = 0

#     def add_comment(self, comment_content, commenter):
#         new_comment = Comment(comment_content, commenter)
#         self.comments.append(new_comment)

# class Post(ContentItem):
#     def like_post(self):
#         self.likes += 1

#     def add_comment(self, comment_content, commenter):
#         new_comment = Comment(comment_content, commenter)
#         self.comments.append(new_comment)

# class Comment(ContentItem):
#     pass

# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.posts = []
#         self.friends = []

#     def add_post(self, post_content):
#         new_post = Post(post_content, self.name)
#         self.posts.append(new_post)

#     def login(self, username, password):
#         # Implementation

#     def register(self, username, password, bio=""):
#         # Implementation

#     def send_friend_request(self, to_user):
#         # Implementation

#     def accept_friend_request(self, friend):
#         # Implementation

#     def decline_friend_request(self, friend):
#         # Implementation

#     def view_friend_requests(self):
#         # Implementation

#     def send_message(self, to_user, message):
#         # Implementation

#     def view_inbox(self):
#         # Implementation

#     def delete_user(self):
#         # Implementation

#     def block_user(self):
#         # Implementation

#     def view_platform_stats(self):
#         # Implementation

# class DataManager:
#     def __init__(self):
#         self.users = self.load_data()

#     def load_data(self):
#         try:
#             with open("data.json", "r") as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             return {}

#     def save_data(self):
#         with open("data.json", "w") as file:
#             json.dump(self.users, file, indent=4)

# # Usage
# data_manager = DataManager()
# user1 = User("Alice", "alice@example.com", "password123")
# user2 = User("Bob", "bob@example.com", "password456")

# user1.add_post("Hello, this is my first post.")
# user1.posts[0].like_post()
# user1.posts[0].add_comment("Nice post!", "Charlie")

# user1.send_friend_request("Bob")

# data_manager.users[user1.email] = user1.__dict__
# data_manager.users[user2.email] = user2.__dict__

# data_manager.save_data()