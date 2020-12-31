import pyyoutube
from twitchbot import Command
import json

# this loads the super secret api keys
with open('configs/api_keys.json') as f:
    api_keys = json.load(f)
    API_KEY = api_keys['youtube_api']

# command
@Command('song', aliases=['yt', 'youtube', 'music', 'tune'])
async def cmd_function(msg, *args):
    if api_keys["youtube_api"] == "":
        print("[BOT] !song command: missing api key for 'youtube_api'")
        return

    # function that writes into videos.json
    def get_video_info():
        api = pyyoutube.Api(api_key=API_KEY)

        playlist_item_res = api.get_playlist_items(
            playlist_id="PLb_KV6iCoxINp2vwdz9ZHJO7aPF_WrEat", count=1
        )

        videos = []
        for item in playlist_item_res.items:
            video_id = item.contentDetails.videoId
            video_res = api.get_video_by_id(video_id=video_id)
            videos = video_res.items
        return videos

    def processor():
        videos = get_video_info()
        print(videos)

        with open("videos.json", "w+") as f:
            for video in videos:
                f.write(video.to_json())
                f.write("\n")

    processor()


    with open('videos.json') as f:
        video_info = json.load(f)
        video_id_for_url = video_info['id']
        video_title = video_info['snippet']['title']



    await msg.reply(f'currently playing: {video_title}, youtu.be/{video_id_for_url} lisare1Hiss')
