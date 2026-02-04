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
        "N5_151": {"example_sentence": "体を大事にしてください。", "example_reading": "からだをだいじにしてください。", "example_meaning_cn": "请保重身体。", "example_meaning_en": "Please take care of your body."},
        "N5_152": {"example_sentence": "お金を借りました。", "example_reading": "おかねをかりました。", "example_meaning_cn": "借了钱。", "example_meaning_en": "I borrowed money."},
        "N5_153": {"example_sentence": "このスープは軽いです。", "example_reading": "このスープはかるいです。", "example_meaning_cn": "这个汤很清淡（轻）。", "example_meaning_en": "This soup is light."},
        "N5_154": {"example_sentence": "カレーライスは辛いです。", "example_reading": "カレーライスはからいです。", "example_meaning_cn": "咖喱饭很辣。", "example_meaning_en": "Curry rice is spicy."},
        "N5_155": {"example_sentence": "五キロぐらいあります。", "example_reading": "ごキロぐらいあります。", "example_meaning_cn": "大概有五公里（或五公斤）。", "example_meaning_en": "It's about five kilometers (or kilograms)."},
        "N5_156": {"example_sentence": "漢字を書いてください。", "example_reading": "かんじをかいてください。", "example_meaning_cn": "请写汉字。", "example_meaning_en": "Please write the Kanji."},
        "N5_157": {"example_sentence": "この本は簡単です。", "example_reading": "このほんはかんたんです。", "example_meaning_cn": "这本书很简单。", "example_meaning_en": "This book is easy."},
        "N5_158": {"example_sentence": "頑張ってください。 ", "example_reading": "がんばってください。", "example_meaning_cn": "请加油。", "example_meaning_en": "Please do your best."},
        "N5_159": {"example_sentence": "木に鳥がいます。", "example_reading": "きにとりがいます。", "example_meaning_cn": "树上有鸟。", "example_meaning_en": "There is a bird in the tree."},
        "N5_160": {"example_sentence": "黄色い花が咲いています。", "example_reading": "きいろいはながさいています。", "example_meaning_cn": "黄色的花正在开放。", "example_meaning_en": "Yellow flowers are blooming."},
        "N5_161": {"example_sentence": "黄色い車は珍しいです。", "example_reading": "きいろいくるまはめずらしいです。", "example_meaning_cn": "黄色的车很少见。", "example_meaning_en": "Yellow cars are rare."},
        "N5_162": {"example_sentence": "昨日は雨でした。", "example_reading": "きのうはあめでした。", "example_meaning_cn": "昨天是下雨天。", "example_meaning_en": "It was rainy yesterday."},
        "N5_163": {"example_sentence": "この服は汚いです。", "example_reading": "このふくはきたないです。", "example_meaning_cn": "这件衣服很脏。", "example_meaning_en": "This clothing is dirty."},
        "N5_164": {"example_sentence": "昨日の夜、何をしましたか。", "example_reading": "きのうのよる、なにをしましたか。", "example_meaning_cn": "昨天晚上做了什么？", "example_meaning_en": "What did you do last night?"},
        "N5_165": {"example_sentence": "切手を貼ってください。", "example_reading": "きってをはってください。", "example_meaning_cn": "请贴上邮票。", "example_meaning_en": "Please stick the stamp on."},
        "N5_166": {"example_sentence": "チケットを持っていますか。", "example_reading": "チケットをもっていますか。", "example_meaning_cn": "有票吗？", "example_meaning_en": "Do you have a ticket?"},
        "N5_167": {"example_sentence": "喫茶店で休みましょう。", "example_reading": "きっさてんでやすみましょう。", "example_meaning_cn": "在咖啡馆休息一下吧。", "example_meaning_en": "Let's take a break at a coffee shop."},
        "N5_168": {"example_sentence": "ジュースをください。", "example_reading": "ジュースをください。", "example_meaning_cn": "请给我果汁。", "example_meaning_en": "Please give me some juice."},
        "N5_169": {"example_sentence": "ギターを弾くのが上手です。", "example_reading": "ギターをひくのがじょうずです。", "example_meaning_cn": "擅长弹吉他。", "example_meaning_en": "I'm good at playing the guitar."},
        "N5_170": {"example_sentence": "去年、日本へ来ました。", "example_reading": "きょねん、にほんへきました。", "example_meaning_cn": "去年来到了日本。", "example_meaning_en": "I came to Japan last year."},
        "N5_171": {"example_sentence": "嫌いな食べ物は何ですか。", "example_reading": "きらいなたべものはなんですか。", "example_meaning_cn": "讨厌的食物是什么？", "example_meaning_en": "What food do you dislike?"},
        "N5_172": {"example_sentence": "爪を切ります。", "example_reading": "つめをきります。", "example_meaning_cn": "剪指甲。", "example_meaning_en": "I'll cut my nails."},
        "N5_173": {"example_sentence": "きれいな写真ですね。", "example_reading": "きれいなしゃしんですね。", "example_meaning_cn": "很漂亮的照片呢。", "example_meaning_en": "It's a beautiful photo, isn't it?"},
        "N5_174": {"example_sentence": "キロメートルで測ります。", "example_reading": "キロメートルではかります。", "example_meaning_cn": "用公里测量。", "example_meaning_en": "Measure in kilometers."},
        "N5_175": {"example_sentence": "銀行でお金を下ろします。", "example_reading": "ぎんこうでおかねをおろします。", "example_meaning_cn": "在银行取钱。", "example_meaning_en": "I'll withdraw money from the bank."},
        "N5_176": {"example_sentence": "金曜日にパーティーをします。", "example_reading": "きんようびにパーティーをします。", "example_meaning_cn": "周五举行派对。", "example_meaning_en": "We'll have a party on Friday."},
        "N5_177": {"example_sentence": "九時に寝ます。", "example_reading": "くじにねます。", "example_meaning_cn": "九点睡觉。", "example_meaning_en": "I sleep at nine."},
        "N5_178": {"example_sentence": "薬を飲みましたか。", "example_reading": "くすりをのみましたか。", "example_meaning_cn": "吃药了吗？", "example_meaning_en": "Did you take your medicine?"},
        "N5_179": {"example_sentence": "下を向いてください。", "example_reading": "したをむいてください。", "example_meaning_cn": "请向下看。", "example_meaning_en": "Please look down."},
        "N5_180": {"example_sentence": "果物を食べます。", "example_reading": "くだものをたべます。", "example_meaning_cn": "吃水果。", "example_meaning_en": "I eat fruit."},
        "N5_181": {"example_sentence": "口を開けてください。", "example_reading": "くちをあけてください。", "example_meaning_cn": "请张嘴。", "example_meaning_en": "Please open your mouth."},
        "N5_182": {"example_sentence": "新しい靴を買いました。", "example_reading": "あたらしいくつをかいました。", "example_meaning_cn": "买了一双新鞋。", "example_meaning_en": "I bought new shoes."},
        "N5_183": {"example_sentence": "靴下を履きます。", "example_reading": "くつしたをはきます。", "example_meaning_cn": "穿袜子。", "example_meaning_en": "I'll put on socks."},
        "N5_184": {"example_sentence": "私の国は寒いです。", "example_reading": "わたしのくにはさむいです。", "example_meaning_cn": "我的国家很冷。", "example_meaning_en": "My country is cold."},
        "N5_185": {"example_sentence": "窓を曇っています。", "example_reading": "まどをくもっています。", "example_meaning_cn": "窗户雾蒙蒙的（阴天）。", "example_meaning_en": "The window is cloudy (weather is cloudy)."},
        "N5_186": {"example_sentence": "外は暗いです。", "example_reading": "そとはくらいです。", "example_meaning_cn": "外面很暗。", "example_meaning_en": "It's dark outside."},
        "N5_187": {"example_sentence": "グラム単位で重さを量ります。", "example_reading": "グラムたんいでおもさをはかります。", "example_meaning_cn": "以克为单位称重。", "example_meaning_en": "Measure the weight in grams."},
        "N5_188": {"example_sentence": "この料理は来ますか。", "example_reading": "このりょうりはきますか。", "example_meaning_cn": "这个菜会上来吗？ ", "example_meaning_en": "Will this dish come?"},
        "N5_189": {"example_sentence": "車で行きましょう。", "example_reading": "くるまでいきましょう。", "example_meaning_cn": "开车去吧。", "example_meaning_en": "Let's go by car."},
        "N5_190": {"example_sentence": "黒いペンで書いてください。", "example_reading": "くろいペンでかいてください。", "example_meaning_cn": "请用黑笔写。", "example_meaning_en": "Please write with a black pen."},
        "N5_191": {"example_sentence": "黒いカバンを持っています。", "example_reading": "くろいカバンをもっています。", "example_meaning_cn": "拿个黑色的包。", "example_meaning_en": "I'm holding a black bag."},
        "N5_192": {"example_sentence": "警官に道を聞きました。", "example_reading": "けいかんにみちをききました。", "example_meaning_cn": "问了警察路。", "example_meaning_en": "I asked a police officer for directions."},
        "N5_193": {"example_sentence": "今朝、早く起きました。", "example_reading": "けさ、はやくおきました。", "example_meaning_cn": "今天早上起得很早。", "example_meaning_en": "I woke up early this morning."},
        "N5_194": {"example_sentence": "テレビを消します。", "example_reading": "テレビをけします。", "example_meaning_cn": "关电视。", "example_meaning_en": "I'll turn off the TV."},
        "N5_195": {"example_sentence": "この景色は素晴らしいです。", "example_reading": "このけしきはすばらしいです。", "example_meaning_cn": "这景色太棒了。", "example_meaning_en": "This scenery is wonderful."},
        "N5_196": {"example_sentence": "消しゴムを貸してください。", "example_reading": "けしゴムをかしてください。", "example_meaning_cn": "请借我橡皮擦。", "example_meaning_en": "Please lend me an eraser."},
        "N5_197": {"example_sentence": "結婚おめでとうございます。", "example_reading": "けっこんおめでとうございます。", "example_meaning_cn": "新婚快乐。", "example_meaning_en": "Congratulations on your marriage."},
        "N5_198": {"example_sentence": "月曜日は忙しいです。", "example_reading": "げつようびはいそがしいです。", "example_meaning_cn": "周一很忙。", "example_meaning_en": "Mondays are busy."},
        "N5_199": {"example_sentence": "玄関で靴を脱ぎます。", "example_reading": "げんかんでくつをぬぎます。", "example_meaning_cn": "在玄关脱鞋。", "example_meaning_en": "Take off your shoes at the entrance."},
        "N5_200": {"example_sentence": "元気で頑張りましょう。", "example_reading": "げんきでがんばりましょう。", "example_meaning_cn": "精神抖擞地加油吧。", "example_meaning_en": "Let's do our best with health and energy."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N5_200.")

if __name__ == "__main__":
    main()
