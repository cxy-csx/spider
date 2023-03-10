import json
import requests
import execjs

# 全局配置
# 抓取数据开始索引
cursor_score = 0

with open('xhs.js', 'r', encoding='utf-8') as fp:
    ctx = execjs.compile(fp.read())


def get_web_session():
    activate_url = '/api/sns/web/v1/login/activate'
    res = ctx.call('sign', activate_url, {})
    cookies = {

        'webId': '0ae757010bf1d1df7429b122477dd0a5',

    }

    headers = {

        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'xhsTrackerId=e2053e4f-6653-4375-8297-8b2dcbb6c36f; xhsTrackerId.sig=pdgIhQKCUtvObtlUPhqX6evGG-hN_WWr-j9gSbjfCEQ; extra_exp_ids=h5_230301_origin,h5_1208_exp3,h5_1130_exp2,ios_wx_launch_open_app_exp,h5_video_ui_exp3,wx_launch_open_app_duration_origin,ques_exp2; extra_exp_ids.sig=Q1dfhDzyOJMTIgN9UUlWPpFwcvW7sck8r5UTIC8y1iI; webBuild=1.2.1; xsecappid=xhs-pc-web; a1=186c0a154eakh980byyf9y9fvithlykqvuyn5ilta50000275006; webId=0ae757010bf1d1df7429b122477dd0a6; websectiga=f3d8eaee8a8c63016320d94a1bd00562d516a5417bc43a032a80cbf70f07d5c0; sec_poison_id=33ac7dec-cc76-4d0d-8387-50b7a7111952',
        'origin': 'https://www.xiaohongshu.com',

        'referer': 'https://www.xiaohongshu.com/',

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',

        'x-s': res['X-s'],
        'x-t': res['X-t'],
    }

    json_data = {}

    response = requests.post(
        'https://edith.xiaohongshu.com/api/sns/web/v1/login/activate',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.json()


res = get_web_session()
cookies = {

    'web_session': res['data']['session']

}
while True:
    def get_params(data):
        url = '/api/sns/web/v1/homefeed'

        with open('xhs2.js', 'r', encoding='utf-8') as fp:
            return ctx.call('sign', url, data)


    json_data = {"cursor_score": cursor_score, "num": 12, "refresh_type": 3, "note_index": 94,
                 "unread_begin_note_id": "",
                 "unread_end_note_id": "", "unread_note_count": 0, "category": "homefeed_recommend"}

    res = get_params(json_data)
    print(res)

    headers = {

        'content-type': 'application/json;charset=UTF-8',

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',

        'x-s': res['X-s'],
        'x-t': res['X-t'],
    }

    response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
                             data=json.dumps(json_data, separators=(',', ':')))

    print(json.dumps(response.json(), ensure_ascii=False))
    cursor_score += 12
    # break
