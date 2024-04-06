import instaloader

iid=input("Enter any Instagram's ID:")

insta=instaloader.Instaloader()
#insta.download_profile(iid,profile_pic_only=True)
insta.download_profile(iid,profile_pic_only=False)
print("Profile download successfully!")
