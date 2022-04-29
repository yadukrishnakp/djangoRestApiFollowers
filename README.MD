## Django RestFramework

This is used to 
### * Create profile

http://localhost:8000/profile_details/

{
    "full_name": "nandu",
    "date_of_birth": "2000-10-11",
    "email": "nandu@gmail.com",
    "mobile_number": "+919605288163",
    "place": "calicut"
}


### * fetch all profiles
http://localhost:8000/profile_details/


### * fetch profile individually
http://localhost:8000/show_profile/1/


### * follow a profile
http://localhost:8000/follow_profile/1/1/

{
    "user_id":"1",
    "profile":"1",
    "follow_status":"follow"
}


### * unfollow a profile
http://localhost:8000/unfollow_profile/1/1/


### * find all the followers of a profile
http://localhost:8000/view_followers/1


### * find all profile a user following
http://localhost:8000/view_followings/1