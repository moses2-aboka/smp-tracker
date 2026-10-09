import os
os.environ["FB_ACESS_TOKEN"] = "EAA Demo_token_never_hardcode_real_ones"
token = os.getenv("FB_ACESS_TOKEN")

fb_response = {
    "id" : "100044385041",
    "name" : "Amerix",
    "about" : "Reproductive health | Mens Health and welfare",
    "fan_count" : 284000,
    "followers_count" : 291500,
    "category" : "Health $ Welness Website",
    "link" : "https://www.facebook.com/amerix041"
}
name = fb_response["name"]
about = fb_response["about"]
fans = fb_response["fan_count"]
followers = fb_response["followers_count"]
page_link = fb_response["link"]

print("FACEBOOK PAGE DATA")
print(f"Page : {name}")
print(f"About : {about}")
print(f"Page likes : {fans:,}")
print(f"Followers : {followers:,}")
print(f"Link : {page_link}")
print()
print(f"Token loaded : {token[:12]}...(never log a live token)")
print()
print("Note: In production replace the mock response with :")
print("  response = requests.get(url,params={'acess_token':token,'fields':'...'})")
print("data = response.json()")
