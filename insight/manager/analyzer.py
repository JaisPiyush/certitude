"""
 Analyzer
 API for analyzing user activity in relation with hobbies
 API will receive signals from actions such as create , view, love, share, comment or follow
 API can manage hobby_map and primary hobby of user for personalized experience
"""

from insight.models import Hobby, Post, Account


WEIGHT_VIEW: float = 0.25
WEIGHT_LOVE: float = 0.50
WEIGHT_COMMENT: float = 0.65
WEIGHT_SAVE: float = 0.80
WEIGHT_SHARE: float = 0.85
WEIGHT_CREATE: float = 0.90
WEIGHT_FOLLOWING: float = 0.45
WEIGHT_FRIEND: float = 0.85


class Analyzer:

    def __init__(self, user: Account):
        self.user = user
    
    """
      Inject hobby into hobby map increasing weight 
      update primary_hobby and primary_hobby_weight
    """    

    @staticmethod
    def max_in_map(map, default,value):
        maximum = [default,value]
        for key in map.keys():
            if map[key] > maximum[1]:
                maximum = [key,map[key]]
        return maximum
    
    def analyze(self, post:Post, weight: float):
        post_hobby_code_name = post.hobby.code_name
        post_hobby_weight = post.hobby.weight

        if post_hobby_code_name in self.user.hobby_map:
            self.user.hobby_map[post_hobby_code_name] += weight
        else:
            self.user.hobby_map[post_hobby_code_name] = weight
        
        if not self.user.primary_hobby:
            self.user.primary_hobby = post_hobby_code_name
            self.user.primary_weight = post_hobby_weight
        self.user.primary_hobby, self.user.primary_weight = self.max_in_map(self.user.hobby_map, self.user.primary_hobby, self.user.primary_weight)
        self.user.save()
        
    def analyze_create_post(self, post: Post):
       self.analyze(post,WEIGHT_CREATE)
    