import json
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_file = os.path.join(project_root, 'jlpt-web', 'src', 'data', 'vocab.json')

    if not os.path.exists(data_file):
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        vocab = json.load(f)

    enrichment = {
        "N5_101": {"example_sentence": "毎朝、六時に起きます。", "example_reading": "まいあさ、ろくじにおきます。", "example_meaning_cn": "每天早上六点起床。", "example_meaning_en": "I wake up at six every morning."},
        "N5_102": {"example_sentence": "荷物を机に置きます。", "example_reading": "にもつをつくえにおきます。", "example_meaning_cn": "把行李放在桌子上。", "example_meaning_en": "I'll put the luggage on the desk."},
        "N5_103": {"example_sentence": "奥さんはお元気ですか。", "example_reading": "おくさんはおげんきですか。", "example_meaning_cn": "你夫人好吗？", "example_meaning_en": "Is your wife well?"},
        "N5_104": {"example_sentence": "お酒は二十歳から飲めます。", "example_reading": "おさけははたちからのめます。", "example_meaning_cn": "二十岁开始可以喝酒。", "example_meaning_en": "You can drink alcohol from the age of twenty."},
        "N5_105": {"example_sentence": "おじいさんはとても優しいです。", "example_reading": "おじいさんはとてもやさしいです。", "example_meaning_cn": "爷爷非常慈祥。", "example_meaning_en": "My grandfather is very kind."},
        "N5_106": {"example_sentence": "昨日、おじさんに会いました。", "example_reading": "きのう、おじさんにあいました。", "example_meaning_cn": "昨天见到了叔叔。", "example_meaning_en": "I met my uncle yesterday."},
        "N5_107": {"example_sentence": "教え方はとても上手です。", "example_reading": "おしえかたはとてもじょうずです。", "example_meaning_cn": "教法非常好。", "example_meaning_en": "The teaching method is very good."},
        "N5_108": {"example_sentence": "日本語を教えてください。", "example_reading": "にほんごをおしえてください。", "example_meaning_cn": "请教我日语。", "example_meaning_en": "Please teach me Japanese."},
        "N5_109": {"example_sentence": "おばあさんは料理が上手です。", "example_reading": "おばあさんはりょうりがじょうずです。", "example_meaning_cn": "奶奶拿手好菜。", "example_meaning_en": "My grandmother is good at cooking."},
        "N5_110": {"example_sentence": "おばさんは北海道に住んでいます。", "example_reading": "おばさんはほっかいどうにすんでいます。", "example_meaning_cn": "婶婶住在北海道。", "example_meaning_en": "My aunt lives in Hokkaido."},
        "N5_111": {"example_sentence": "お風呂に入ります。", "example_reading": "おふろにはいります。", "example_meaning_cn": "洗澡（泡澡）。", "example_meaning_en": "I'll take a bath."},
        "N5_112": {"example_sentence": "お弁当を買ってきました。", "example_reading": "おべんとうをかってきました。", "example_meaning_cn": "买便当回来了。", "example_meaning_en": "I bought a lunch box."},
        "N5_113": {"example_sentence": "お弁当箱を洗います。", "example_reading": "おべんとうばこをあらいます。", "example_meaning_cn": "洗便当盒。", "example_meaning_en": "I'll wash the lunch box."},
        "N5_114": {"example_sentence": "名前を覚えてください。", "example_reading": "なまえをおぼえてください。", "example_meaning_cn": "请记住名字。", "example_meaning_en": "Please remember the name."},
        "N5_115": {"example_sentence": "お巡りさんに道を聞きました。", "example_reading": "おまわりさんにみちをききました。", "example_meaning_cn": "向警察问了路。", "example_meaning_en": "I asked a police officer for directions."},
        "N5_116": {"example_sentence": "重い荷物を運びます。", "example_reading": "おもいにもつをはこびます。", "example_meaning_cn": "搬运沉重的行李。", "example_meaning_en": "I'll carry heavy luggage."},
        "N5_117": {"example_sentence": "この本は面白いです。", "example_reading": "このほんはおもしろいです。", "example_meaning_cn": "这本书很有趣。", "example_meaning_en": "This book is interesting."},
        "N5_118": {"example_sentence": "おやすみなさい。", "example_reading": "おやすみなさい。", "example_meaning_cn": "晚安。", "example_meaning_en": "Good night."},
        "N5_119": {"example_sentence": "プールで泳ぎます。", "example_reading": "プールでおよぎます。", "example_meaning_cn": "在泳池游泳。", "example_meaning_en": "I'll swim in the pool."},
        "N5_120": {"example_sentence": "駅で電車を降ります。", "example_reading": "えきででんしゃを降ります。", "example_meaning_cn": "在车站下电车。", "example_meaning_en": "I'll get off the train at the station."},
        "N5_121": {"example_sentence": "去年から日本語を勉強しています。", "example_reading": "きょねんからにほんごをべんきょうしています。", "example_meaning_cn": "从去年开始学习日语。", "example_meaning_en": "I've been studying Japanese since last year."},
        "N5_122": {"example_sentence": "会社員として働いています。", "example_reading": "かいしゃいんとしてはたらいています。", "example_meaning_cn": "作为公司员工工作。", "example_meaning_en": "I'm working as a company employee."},
        "N5_123": {"example_sentence": "学校へ行きます。", "example_reading": "がっこうへいきます。", "example_meaning_cn": "去学校。", "example_meaning_en": "I'm going to school."},
        "N5_124": {"example_sentence": "角を右に曲がります。", "example_reading": "かどをみぎにまがります。", "example_meaning_cn": "在拐角处向右拐。", "example_meaning_en": "Turn right at the corner."},
        "N5_125": {"example_sentence": "家内は料理が上手です。", "example_reading": "かないはりょうりがじょうずです。", "example_meaning_cn": "我太太拿手好菜。", "example_meaning_en": "My wife is good at cooking."},
        "N5_126": {"example_sentence": "バッグをカバンにかけます。", "example_reading": "バッグをカバンにかけます。", "example_meaning_cn": "把包挂在书包上。 ", "example_meaning_en": "I'll hang a bag on the bag."},
        "N5_127": {"example_sentence": "眼鏡をかけます。", "example_reading": "めがねをかけます。", "example_meaning_cn": "戴眼镜。", "example_meaning_en": "I'll put on glasses."},
        "N5_128": {"example_sentence": "机の上に鍵があります。", "example_reading": "つくえのうえにかぎがあります。", "example_meaning_cn": "桌子上有钥匙。", "example_meaning_en": "There is a key on the desk."},
        "N5_129": {"example_sentence": "家へ帰ります。", "example_reading": "いえにかえります。", "example_meaning_cn": "回家。", "example_meaning_en": "I'm going home."},
        "N5_130": {"example_sentence": "毎日、顔を洗います。", "example_reading": "まいにち、かおをあらいます。", "example_meaning_cn": "每天洗脸。", "example_meaning_en": "I wash my face every day."},
        "N5_131": {"example_sentence": "一ヶ月に三回映画を見ます。", "example_reading": "いっかげつにさんかいえいがをみます。", "example_meaning_cn": "一个月看三次电影。", "example_meaning_en": "I watch movies three times a month."},
        "N5_132": {"example_sentence": "階段を上ります。", "example_reading": "かいだんをのぼります。", "example_meaning_cn": "上楼梯。", "example_meaning_en": "I'll go up the stairs."},
        "N5_133": {"example_sentence": "スーパーで買い物をします。", "example_reading": "スーパーでかいものをします。", "example_meaning_cn": "在超市买东西。", "example_meaning_en": "I'm going shopping at the supermarket."},
        "N5_134": {"example_sentence": "本を買います。", "example_reading": "ほんをかいます。", "example_meaning_cn": "买书。", "example_meaning_en": "I'll buy a book."},
        "N5_135": {"example_sentence": "お返しはいりません。", "example_reading": "おかえしはいりません。", "example_meaning_cn": "不需要回礼（找零）。", "example_meaning_en": "No need for change (return gift)."},
        "N5_136": {"example_sentence": "傘を差します。", "example_reading": "かさをさします。", "example_meaning_cn": "打伞。", "example_meaning_en": "I'll open an umbrella."},
        "N5_137": {"example_sentence": "友達にお金を貸します。", "example_reading": "ともだちにおかねをかします。", "example_meaning_cn": "借钱给朋友。", "example_meaning_en": "I'll lend money to a friend."},
        "N5_138": {"example_sentence": "風が吹いています。", "example_reading": "かぜがふいています。", "example_meaning_cn": "起风了。", "example_meaning_en": "The wind is blowing."},
        "N5_139": {"example_sentence": "風邪を引きました。", "example_reading": "かぜをひきました。", "example_meaning_cn": "感冒了。", "example_meaning_en": "I caught a cold."},
        "N5_140": {"example_sentence": "家族は三人です。", "example_reading": "かぞくはさんにんです。", "example_meaning_cn": "家里有三个人。", "example_meaning_en": "There are three people in my family."},
        "N5_141": {"example_sentence": "片仮名を勉強します。", "example_reading": "かたかなをべんきょうします。", "example_meaning_cn": "学习片假名。", "example_meaning_en": "I'll study Katakana."},
        "N5_142": {"example_sentence": "一ヶ月ぐらい休みます。", "example_reading": "いっかげつぐらいやすみます。", "example_meaning_cn": "休息一个月左右。", "example_meaning_en": "I'll take a break for about a month."},
        "N5_143": {"example_sentence": "かっこいい靴を履いています。", "example_reading": "かっこいいくつをはいています。", "example_meaning_cn": "穿着很帅的鞋子。", "example_meaning_en": "I'm wearing cool shoes."},
        "N5_144": {"example_sentence": "学校までバスで行きます。", "example_reading": "がっこうまでバスでいきます。", "example_meaning_cn": "坐公交车去学校。", "example_meaning_en": "I'll go to school by bus."},
        "N5_145": {"example_sentence": "コップを学校に忘わすれました。", "example_reading": "コップをがっこうにわすれました。", "example_meaning_cn": "把杯子忘在学校了。", "example_meaning_en": "I forgot my cup at school."},
        "N5_146": {"example_sentence": "角の店でパンを買います。", "example_reading": "かどのみせでパンをかいます。", "example_meaning_cn": "在拐角处的店买面包。", "example_meaning_en": "I'll buy bread at the store on the corner."},
        "N5_147": {"example_sentence": "バッグをカバンに入れました。", "example_reading": "バッグをカバンにいれました。", "example_meaning_cn": "把小包放进大包里。 ", "example_meaning_en": "I put the small bag inside the bag."},
        "N5_148": {"example_sentence": "花瓶に花を飾ります。", "example_reading": "かびんにはなをかざります。", "example_meaning_cn": "在花瓶里插花。", "example_meaning_en": "Decorate the flowers in a vase."},
        "N5_149": {"example_sentence": "帽子を被ります。", "example_reading": "ぼうしをかぶります。", "example_meaning_cn": "戴帽子。", "example_meaning_en": "Put on a hat."},
        "N5_150": {"example_sentence": "火曜日、暇ですか。", "example_reading": "かようび、ひまですか。", "example_meaning_cn": "周二有空吗？", "example_meaning_en": "Are you free on Tuesday?"}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N5_150.")

if __name__ == "__main__":
    main()
