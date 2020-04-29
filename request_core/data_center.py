class DataCenter:
    def __init__(self):

        # 视频的评论数据
        self.dicComment = dict()
        self.comment_aweme_ids   = []

        # def append(id,data):





dataCenter = DataCenter()


url ='/aweme/v1/general/search/single/?version_code=10.8.0&js_sdk_version=1.60.0.7&app_name=aweme&vid=C3280B93-939F-4871-829A-2CE82573A38E&app_version=10.8.0&device_id=47727489130&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=af97844c55cf7d97cb6d136560a91f4a2b9602c3&cdid=BAA59DF8-9502-4940-B6E8-3AC16B08F1B3&os_api=18&ac=WIFI&os_version=12.0&device_platform=iphone&build_number=108013&iid=641747431465901&device_type=iPhone9,1&is_vcd=1&idfa=726A4A57-7910-4297-BD80-3C90CD8064C1&client_width=375&keyword=%E5%87%8F%E8%82%A5&disable_synthesis=0&sort_type=0&is_filter_search=0&count=20&longitude=116.424467&single_filter_aladdin=0&is_pull_refresh=0&latitude=39.908067&multi_mod=0&epidemic_card_type=2&query_correct_type=1&mac_address=02%3A00%3A00%3A00%3A00%3A00&offset=0&search_source=search_history&dynamic_type=1&publish_time=0&hot_search=0'

print(url.rfind("?"))