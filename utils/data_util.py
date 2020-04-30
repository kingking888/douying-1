
#
def pack_user(user):
    user_info = {}

    uid = user.get('uid')  # 用户ID
    short_id = user.get('short_id')  # 抖音id
    unique_id = user.get('unique_id')
    nickname = user.get('nickname')  # 昵称

    # 这里需要进行非空判断,有些没有值会覆盖之前的
    if uid and uid != "0":
        user_info['uid'] = uid
    if short_id and short_id != '0':
        user_info['short_id'] = short_id
    if unique_id and unique_id != '0':
        user_info['unique_id'] = unique_id
    if nickname:  # 昵称
        user_info['nike'] = nickname
    # 0 male 1 female 2 unset
    if user.get('gender'):  # 性别
        user_info['gender'] = user['gender']
    if user.get('birthday'):  # 生日
        user_info['birthday'] = user['birthday']

    if user.get('status'):
        user_info['status'] = user['status']
    if user.get('region'):
        user_info['region'] = user['region']

    # 作品数量
    if user.get('aweme_count'):
        user_info['aweme_count'] = user['aweme_count']
    # 获赞数量
    if user.get('total_favorited'):
        user_info['total_favorited'] = user['total_favorited']
    # 关注数量
    if user.get('following_count'):
        user_info['following_count'] = user['following_count']
    # 粉丝数量
    if user.get('follower_count'):
        user_info['follower_count'] = user['follower_count']
    # 签名
    if user.get('signature'):
        user_info['signature'] = user.get('signature')
    # 学校
    if user.get('school_name'):
        user_info['school_name'] = user.get('school_name')
    # 地区
    if user.get('area'):
        user_info['district'] = user.get('district')
    # 位置
    if user.get('location'):
        user_info['location'] = user.get('location')
    # 省份
    if user.get('province'):
        user_info['province'] = user.get('province')

    # 国家
    if user.get('country'):
        user_info['country'] = user.get('country')
    # 城市
    if user.get('city'):  #
        user_info['city'] = user.get('city')
    if user.get('twitter_name'):  #
        user_info['twitter_name'] = user.get('twitter_name')
    # 头像
    if user.get('avatar_medium') and len(user.get('avatar_medium').get("url_list")) > 0:
        user_info['head_icon'] = user.get('avatar_medium').get("url_list")[0]

    followers_detail = user.get('followers_detail')
    if followers_detail:
        for v in followers_detail:
            if v['app_name'] == 'aweme':
                user_info['fans_count'] = user.get('fans_count')  # 粉丝数量
                break

    return user_info

def pack_video(data):
    info = {'vid':data['aweme_id'],'uid':data.get('uid'),'create_time':data.get('create_time'),'title':data.get('desc')}

    statistics = data.get('statistics')
    if statistics:
        info['comment_count'] = statistics.get('comment_count')
        info['upcount'] = statistics.get('digg_count')
        info['download_count'] = statistics.get('download_count')
        info['forward_count'] = statistics.get('forward_count')

    return info

def pack_comment(data):
    info = {}
    info['cid'] = data['cid']
    info['vid'] = data['aweme_id']
    info['uid'] = data['user']['uid']
    info['reply_id'] = data['reply_id']
    info['content'] = data['text']
    info['createtime'] = data['create_time']  #
    info['digg_count'] = data['digg_count']  # 评论点赞数量
    return info
def pack_comment_1(data):
    comments = [pack_comment(data)]

    reply_comment = data.get('reply_comment')
    if reply_comment:
        for v in reply_comment:
            comments.append(pack_comment(v))

    return comments