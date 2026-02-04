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
        "N5_57": {"example_sentence": "イタリア料理が好きです。", "example_reading": "イタリアりょうりがすきです。", "example_meaning_cn": "喜欢意大利菜。", "example_meaning_en": "I like Italian food."},
        "N5_58": {"example_sentence": "クラスで一番背が高いです。", "example_reading": "クラスでいちばんせがたかいです。", "example_meaning_cn": "在班里个子最高。", "example_meaning_en": "He is the tallest in the class."},
        "N5_59": {"example_sentence": "いつ日本へ来ましたか。", "example_reading": "いつにほんへきましたか。", "example_meaning_cn": "什么时候来日本的？", "example_meaning_en": "When did you come to Japan?"},
        "N5_60": {"example_sentence": "一緒に帰りましょう。", "example_reading": "いっしょにかえりましょう。", "example_meaning_cn": "一起回去吧。", "example_meaning_en": "Let's go home together."},
        "N5_61": {"example_sentence": "いつも朝ご飯を食べますか。", "example_reading": "いつもあさごはんをたべますか。", "example_meaning_cn": "总是吃早饭吗？", "example_meaning_en": "Do you always eat breakfast?"},
        "N5_62": {"example_sentence": "私の家には犬が二匹います。", "example_reading": "わたしのいえにはいぬがにひきいます。", "example_meaning_cn": "我家有两条狗。", "example_meaning_en": "I have two dogs at my house."},
        "N5_63": {"example_sentence": "今、何時ですか。", "example_reading": "いま、なんじですか。", "example_meaning_cn": "现在几点？", "example_meaning_en": "What time is it now?"},
        "N5_64": {"example_sentence": "今から勉強します。", "example_reading": "いまからべんきょうします。", "example_meaning_cn": "现在开始学习。", "example_meaning_en": "I'm going to study from now."},
        "N5_65": {"example_sentence": "教室にテレビがあります。", "example_reading": "きょうしつにテレビがあります。", "example_meaning_cn": "教室里有电视。", "example_meaning_en": "There is a TV in the classroom."},
        "N5_66": {"example_sentence": "妹は高校生です。", "example_reading": "いもうとはこうこうせいです。", "example_meaning_cn": "妹妹是高中生。", "example_meaning_en": "My younger sister is a high school student."},
        "N5_67": {"example_sentence": "妹さんはお元気ですか。", "example_reading": "いもうとさんはおげんきですか。", "example_meaning_cn": "你妹妹好吗？", "example_meaning_en": "Is your younger sister well?"},
        "N5_68": {"example_sentence": "入り口はこちらです。", "example_reading": "いりぐちはこちらです。", "example_meaning_cn": "入口在这边。", "example_meaning_en": "The entrance is here."},
        "N5_69": {"example_sentence": "このバッグにいりますか。", "example_reading": "このバッグにいりますか。", "example_meaning_cn": "需要这个包吗？", "example_meaning_en": "Do you need this bag?"},
        "N5_70": {"example_sentence": "コーヒーに砂糖を入れます。", "example_reading": "コーヒーにさとうをいれます。", "example_meaning_cn": "在咖啡里加糖。", "example_meaning_en": "I put sugar in the coffee."},
        "N5_71": {"example_sentence": "いろいろお世話になりました。", "example_reading": "いろいろおせわになりました。", "example_meaning_cn": "承蒙多方照顾。", "example_meaning_en": "Thank you for everything."},
        "N5_72": {"example_sentence": "インターネットで調べます。", "example_reading": "インターネットでしらべます。", "example_meaning_cn": "在网上查一下。", "example_meaning_en": "I'll look it up on the internet."},
        "N5_73": {"example_sentence": "夜、インターネットをします。", "example_reading": "よる、インターネットをします。", "example_meaning_cn": "晚上上网。", "example_meaning_en": "I surf the internet at night."},
        "N5_74": {"example_sentence": "山の上に雪があります。", "example_reading": "やまのうえにゆきがあります。", "example_meaning_cn": "山上山上有雪。", "example_meaning_en": "There is snow on top of the mountain."},
        "N5_75": {"example_sentence": "銀行はデパートの後ろです。", "example_reading": "ぎんこうはデパートのうしろです。", "example_meaning_cn": "银行在百货商店后面。", "example_meaning_en": "The bank is behind the department store."},
        "N5_76": {"example_sentence": "歌を歌うのが好きです。", "example_reading": "うたをうたうのがすきです。", "example_meaning_cn": "喜欢唱歌。", "example_meaning_en": "I like singing songs."},
        "N5_77": {"example_sentence": "みんなで歌いましょう。", "example_reading": "みんなでうたいましょう。", "example_meaning_cn": "大家一起唱吧。", "example_meaning_en": "Let's all sing together."},
        "N5_78": {"example_sentence": "うちへ帰りましょう。", "example_reading": "うちへかえりましょう。", "example_meaning_cn": "回家吧。", "example_meaning_en": "Let's go home."},
        "N5_79": {"example_sentence": "去年の三月に生まれました。", "example_reading": "きょねんのさんがつにうまれました。", "example_meaning_cn": "去年三月出生的。", "example_meaning_en": "I was born in March last year."},
        "N5_80": {"example_sentence": "海へ泳ぎに行きます。", "example_reading": "うみへおよぎにいきます。", "example_meaning_cn": "去海边游泳。", "example_meaning_en": "I'm going to the sea to swim."},
        "N5_81": {"example_sentence": "写真の裏に名前を書きます。", "example_reading": "しゃしんのうらになまえをかきます。", "example_meaning_cn": "在照片后面写名字。", "example_meaning_en": "Write your name on the back of the photo."},
        "N5_82": {"example_sentence": "野菜を売っています。", "example_reading": "やさいをうっています。", "example_meaning_cn": "正在卖蔬菜。", "example_meaning_en": "Selling vegetables."},
        "N5_83": {"example_sentence": "隣の部屋がうるさいです。", "example_reading": "となりのへやがうるさいです。", "example_meaning_cn": "隔壁房间很吵。", "example_meaning_en": "The next room is noisy."},
        "N5_84": {"example_sentence": "プレゼントをもらって嬉しいです。", "example_reading": "プレゼントをもらってうれしいです。", "example_meaning_cn": "收到礼物很高兴。", "example_meaning_en": "I'm happy to receive a present."},
        "N5_85": {"example_sentence": "うん、わかった。", "example_reading": "うん、わかった。", "example_meaning_cn": "嗯，知道了。", "example_meaning_en": "Yeah, I got it."},
        "N5_86": {"example_sentence": "絵を描くのが得意です。", "example_reading": "えをかくのがとくいです。", "example_meaning_cn": "擅长画画。", "example_meaning_en": "I'm good at drawing pictures."},
        "N5_87": {"example_sentence": "週末に映画を見ます。", "example_reading": "しゅうまつにえいがをみます。", "example_meaning_cn": "周末看电影。", "example_meaning_en": "I'll watch a movie this weekend."},
        "N5_88": {"example_sentence": "駅の近くに映画館があります。", "example_reading": "えきのちかくにえいがかんがあります。", "example_meaning_cn": "车站附近有电影院。", "example_meaning_en": "There is a movie theater near the station."},
        "N5_89": {"example_sentence": "英語を勉強しています。", "example_reading": "えいごをべんきょうしています。", "example_meaning_cn": "正在学习英语。", "example_meaning_en": "I'm studying English."},
        "N5_90": {"example_sentence": "ええ、いいですよ。", "example_reading": "ええ、いいですよ。", "example_meaning_cn": "是的，可以哦。", "example_meaning_en": "Yes, that's fine."},
        "N5_91": {"example_sentence": "駅までタクシーで行きます。", "example_reading": "えきまでタクシーでいきます。", "example_meaning_cn": "坐出租车去车站。", "example_meaning_en": "I'll go to the station by taxi."},
        "N5_92": {"example_sentence": "駅前で待ち合わせましょう。", "example_reading": "えきまえでまちあわせましょう。", "example_meaning_cn": "在车站前等吧。", "example_meaning_en": "Let's meet in front of the station."},
        "N5_93": {"example_sentence": "えんぴつで書いてください。", "example_reading": "えんぴつでかいてください。", "example_meaning_cn": "请用铅笔写。", "example_meaning_en": "Please write with a pencil."},
        "N5_94": {"example_sentence": "このお菓子はおいしいです。", "example_reading": "このおかしはおいしいです。", "example_meaning_cn": "这个点心挺好吃的。", "example_meaning_en": "This sweet is delicious."},
        "N5_95": {"example_sentence": "人が多いですね。", "example_reading": "ひとがおおいですね。", "example_meaning_cn": "人很多呢。", "example_meaning_en": "There are many people, aren't there?"},
        "N5_96": {"example_sentence": "大きい声で言ってください。", "example_reading": "おおきいこえでいってください。", "example_meaning_cn": "请大声说。", "example_meaning_en": "Please say it in a loud voice."},
        "N5_97": {"example_sentence": "駅におおぜいの人がいます。", "example_reading": "えきにおおぜいのひとがいます。", "example_meaning_cn": "车站里有很多人。", "example_meaning_en": "There are a lot of people at the station."},
        "N5_98": {"example_sentence": "お母さんはお元気ですか。", "example_reading": "おかあさんはおげんきですか。", "example_meaning_cn": "你母亲身体好吗？", "example_meaning_en": "Is your mother healthy?"},
        "N5_99": {"example_sentence": "甘いお菓子が好きです。", "example_reading": "あまいおかしがすきです。", "example_meaning_cn": "喜欢甜食。", "example_meaning_en": "I like sweet snacks."},
        "N5_100": {"example_sentence": "お金を払います。", "example_reading": "おかねをはらいます。", "example_meaning_cn": "付钱。", "example_meaning_en": "I'll pay the money."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N5_100.")

if __name__ == "__main__":
    main()
