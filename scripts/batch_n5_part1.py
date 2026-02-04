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

    # Batch 1: N5 (Partial) - Words N5_14 to N5_100 (approx)
    # I'll provide a mapping of ID to data
    enrichment = {
        "N5_14": {
            "example_sentence": "窓を開けると、部屋が明るくなりました。",
            "example_reading": "まどをあけると、へやがあかるくなりました。",
            "example_meaning_cn": "打开窗户后，房间变得明亮了。",
            "example_meaning_en": "The room became bright after opening the window."
        },
        "N5_15": {
            "example_sentence": "暑いので、窓を開けます。",
            "example_reading": "あついので、まどをあけます。",
            "example_meaning_cn": "因为热，所以我打开窗户。",
            "example_meaning_en": "I'll open the window because it's hot."
        },
        "N5_16": {
            "example_sentence": "誕生日にプレゼントをあげました。",
            "example_reading": "たんじょうびにプレゼントをあげました。",
            "example_meaning_cn": "生日那天送了礼物。",
            "example_meaning_en": "I gave a present on the birthday."
        },
        "N5_17": {
            "example_sentence": "朝、公園を散歩します。",
            "example_reading": "あさ、こうえんをさんぽします。",
            "example_meaning_cn": "早上在公园散步。",
            "example_meaning_en": "I take a walk in the park in the morning."
        },
        "N5_18": {
            "example_sentence": "あさって、日本へ行きます。",
            "example_reading": "あさって、にほんへいきます。",
            "example_meaning_cn": "后天去日本。",
            "example_meaning_en": "I'm going to Japan the day after tomorrow."
        },
        "N5_19": {
            "example_sentence": "足が痛いので、あまり歩けません。",
            "example_reading": "あしがいたいので、あまりあるけません。",
            "example_meaning_cn": "因为脚疼，所以不太能走路。",
            "example_meaning_en": "My feet hurt, so I can't walk much."
        },
        "N5_20": {
            "example_sentence": "明日、何をしますか。",
            "example_reading": "あした、なにをしますか。",
            "example_meaning_cn": "明天要做什么？",
            "example_meaning_en": "What are you doing tomorrow?"
        },
        "N5_21": {
            "example_sentence": "あそこにきれいな花が咲いています。",
            "example_reading": "あそこにきれいなはながさいています。",
            "example_meaning_cn": "那里开着漂亮的花。",
            "example_meaning_en": "Beautiful flowers are blooming over there."
        },
        "N5_22": {
            "example_sentence": "昨日、友達と遊びました。",
            "example_reading": "きのう、ともだちとあそびました。",
            "example_meaning_cn": "昨天和朋友一起玩了。",
            "example_meaning_en": "I played with my friend yesterday."
        },
        "N5_23": {
            "example_sentence": "今日は暖かいですね。",
            "example_reading": "きょうはあたたかいですね。",
            "example_meaning_cn": "今天很温暖。 ",
            "example_meaning_en": "It's warm today, isn't it?"
        },
        "N5_24": {
            "example_sentence": "新しいカバンを買いました。",
            "example_reading": "あたらしいカバンをかいました。",
            "example_meaning_cn": "买了一个新书包。",
            "example_meaning_en": "I bought a new bag."
        },
        "N5_25": {
            "example_sentence": "あちらの部屋へどうぞ。",
            "example_reading": "あちらのへやへどうぞ。",
            "example_meaning_cn": "请到那边的房间。",
            "example_meaning_en": "Please go to that room over there."
        },
        "N5_26": {
            "example_sentence": "今日はとても暑いですね。",
            "example_reading": "きょうはとてもあついですね。",
            "example_meaning_cn": "今天非常热呢。",
            "example_meaning_en": "It's very hot today, isn't it?"
        },
        "N5_27": {
            "example_sentence": "トイレはあっちです。",
            "example_reading": "トイレはあっちです。",
            "example_meaning_cn": "厕所在那边。",
            "example_meaning_en": "The toilet is over there."
        },
        "N5_28": {
            "example_sentence": "あとで電話します。",
            "example_reading": "あとででんわします。",
            "example_meaning_cn": "待会给你打电话。",
            "example_meaning_en": "I'll call you later."
        },
        "N5_29": {
            "example_sentence": "私の兄はエンジニアです。",
            "example_reading": "わたしのあにはエンジニアです。",
            "example_meaning_cn": "我哥哥是工程师。",
            "example_meaning_en": "My older brother is an engineer."
        },
        "N5_30": {
            "example_sentence": "私の姉は看護師です。",
            "example_reading": "わたしのあねはかんごしです。",
            "example_meaning_cn": "我姐姐是护士。",
            "example_meaning_en": "My older sister is a nurse."
        },
        "N5_31": {
            "example_sentence": "あの人は誰ですか。",
            "example_reading": "あのひとはだれですか。",
            "example_meaning_cn": "那个人是谁？",
            "example_meaning_en": "Who is that person?"
        },
        "N5_32": {
            "example_sentence": "毎朝、シャワーを浴びます。",
            "example_reading": "まいあさ、シャワーをあびます。",
            "example_meaning_cn": "每天早上冲澡。",
            "example_meaning_en": "I take a shower every morning."
        },
        "N5_33": {
            "example_sentence": "この川は危ないです。",
            "example_reading": "このかわはあぶないです。",
            "example_meaning_cn": "这条河很危险。",
            "example_meaning_en": "This river is dangerous."
        },
        "N5_34": {
            "example_sentence": "お酒はあまり飲みません。",
            "example_reading": "おさけはあまりのみません。",
            "example_meaning_cn": "不怎么喝酒。",
            "example_meaning_en": "I don't drink alcohol much."
        },
        "N5_35": {
            "example_sentence": "雨が降っています。",
            "example_reading": "あめがふっています。",
            "example_meaning_cn": "下雨了。",
            "example_meaning_en": "It is raining."
        },
        "N5_36": {
            "example_sentence": "彼はアメリカ人です。",
            "example_reading": "かれはアメリカじんです。",
            "example_meaning_cn": "他是美国人。",
            "example_meaning_en": "He is American."
        },
        "N5_37": {
            "example_sentence": "手を洗ってから、食べます。",
            "example_reading": "てをあらってから、たべます。",
            "example_meaning_cn": "洗手后再吃。",
            "example_meaning_en": "I eat after washing my hands."
        },
        "N5_38": {
            "example_sentence": "机の上に本があります。",
            "example_reading": "つくえのうえにほんがあります。",
            "example_meaning_cn": "桌子上有书。",
            "example_meaning_en": "There is a book on the desk."
        },
        "N5_39": {
            "example_sentence": "ここから駅まで歩いて行きます。",
            "example_reading": "ここからえきまであるいていきます。",
            "example_meaning_cn": "从这里走路去车站。",
            "example_meaning_en": "I'll walk from here to the station."
        },
        "N5_40": {
            "example_sentence": "毎日、30分歩きます。",
            "example_reading": "まいにち、さんじゅっぷんあるきます。",
            "example_meaning_cn": "每天走30分钟。",
            "example_meaning_en": "I walk for 30 minutes every day."
        },
        "N5_41": {
            "example_sentence": "コンビニでアルバイトをしています。",
            "example_reading": "コンビニでアルバイトをしています。",
            "example_meaning_cn": "在便利店打工。",
            "example_meaning_en": "I'm working part-time at a convenience store."
        },
        "N5_42": {
            "example_sentence": "あれは何ですか。",
            "example_reading": "あれはなんですか。",
            "example_meaning_cn": "那个是什么？",
            "example_meaning_en": "What is that?"
        },
        "N5_43": {
            "example_sentence": "このドラマはいいですね。",
            "example_reading": "このドラマはいいですね。",
            "example_meaning_cn": "这个连续剧很好呢。",
            "example_meaning_en": "This drama is good, isn't it?"
        },
        "N5_44": {
            "example_sentence": "いいえ、違います。",
            "example_reading": "いいえ、ちがいます。",
            "example_meaning_cn": "不，不是。",
            "example_meaning_en": "No, that's not right."
        },
        "N5_45": {
            "example_sentence": "先生、質問があります。 ",
            "example_reading": "せんせい、しつもんがあります。",
            "example_meaning_cn": "老师，我有问题。",
            "example_meaning_en": "Teacher, I have a question."
        },
        "N5_46": {
            "example_sentence": "私の家は学校の近くです。",
            "example_reading": "わたしのいえはがっこうのちかくです。",
            "example_meaning_cn": "我的家在学校附近。",
            "example_meaning_en": "My house is near the school."
        },
        "N5_47": {
            "example_sentence": "いかがですか。 ",
            "example_reading": "いかがですか。",
            "example_meaning_cn": "怎么样？",
            "example_meaning_en": "How is it?"
        },
        "N5_48": {
            "example_sentence": "デパートへ行きます。",
            "example_reading": "デパートへいきます。",
            "example_meaning_cn": "去百货商店。",
            "example_meaning_en": "I'm going to the department store."
        },
        "N5_49": {
            "example_sentence": "お子さんはおいくつですか。",
            "example_reading": "おこさんはおいくつですか。",
            "example_meaning_cn": "你的孩子多大了？",
            "example_meaning_en": "How old is your child?"
        },
        "N5_50": {
            "example_sentence": "リンゴをいくつ買いましたか。",
            "example_reading": "リンゴをいくつかいましたか。",
            "example_meaning_cn": "买了几个苹果？",
            "example_meaning_en": "How many apples did you buy?"
        },
        "N5_51": {
            "example_sentence": "このペンはいくらですか。",
            "example_reading": "このペンはいくらですか。",
            "example_meaning_cn": "这支笔多少钱？",
            "example_meaning_en": "How much is this pen?"
        },
        "N5_52": {
            "example_sentence": "病気なので、医者に行きます。",
            "example_reading": "びょうきなので、いしゃにいきます。",
            "example_meaning_cn": "因为生病了，所以去看医生。",
            "example_meaning_en": "I'm sick, so I'm going to the doctor."
        },
        "N5_53": {
            "example_sentence": "いすに座ってください。",
            "example_reading": "いすにすわってください。",
            "example_meaning_cn": "请坐在椅子上。",
            "example_meaning_en": "Please sit on the chair."
        },
        "N5_54": {
            "example_sentence": "仕事が忙しいです。",
            "example_reading": "しごとがいそがしいです。",
            "example_meaning_cn": "工作很忙。",
            "example_meaning_en": "I'm busy with work."
        },
        "N5_55": {
            "example_sentence": "時間がありませんから、急ぎましょう。",
            "example_reading": "じかんがありませんから、いそぎましょう。",
            "example_meaning_cn": "没时间了，赶快吧。",
            "example_meaning_en": "We don't have time, so let's hurry."
        },
        "N5_56": {
            "example_sentence": "お腹が痛いです。",
            "example_reading": "おなかがいたいです。",
            "example_meaning_cn": "肚子疼。",
            "example_meaning_en": "My stomach hurts."
        }
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated {len(enrichment)} more items.")

if __name__ == "__main__":
    main()
