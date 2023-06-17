
from instabot import Bot
my_bot=Bot()

# login
my_bot.login(username="your username",password="your account password")
# to follow someone
my_bot.follow("account you want to follow")
# to follow multiple user
my_bot.follow("username ","username")
# to unfollow someone but need to run rhis after 1 hr
my_bot.unfollow_non_followers()
# upload image
my_bot.upload_photo("clock.png",caption="first post")
my_bot.upload_story_photo("clock.png")

# to send the msg
my_bot.send_message("hello","username")


# to like the post| amount is for howmany post you want to like it count from the bottom
try:
    my_bot.like_user("username",amount=51)
except Exception:
    print(Exception)   


# for commenting on post
# we need userid that is given by  username
try:
    user_id=my_bot.get_user_id_from_username("username")
# now from user id we can have the media id
    media_id=my_bot.get_last_user_medias(user_id,1)
# to coment on post we need media id which acheive by above code
    my_bot.comment(media_id[0],"amazing content")
except Exception:
    print(Exception)


# to get list of followers and following
follower_list=my_bot.get_user_followers("your username")
following_list=my_bot.get_user_following("your username")
# to get one by one list of followers
for count, each_follower in enumarate(follower_list):
    if count>4:
        continue
    
    print(my_bot.get_username_from_user_id(each_follower))

for count1, each_follow in enumarate(following_list):
      if count>4:
        continue
    
      print(my_bot.get_username_from_user_id(each_follower))


my_bot.logout()   