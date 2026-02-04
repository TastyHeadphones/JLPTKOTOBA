import json
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_file = os.path.join(project_root, 'jlpt-web', 'src', 'data', 'vocab.json')

    if not os.path.exists(data_file):
        print("Data file not found.")
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        vocab = json.load(f)

    # High-quality data for the first batch of N5 words
    seed_data = {
        "N5_0": {
            "example_sentence": "夏休みにアイスクリームをたくさん食べました。",
            "example_reading": "なつやすみにアイスクリームをたくさんたべました。",
            "example_meaning_cn": "暑假吃了很多冰淇淋。",
            "example_meaning_en": "I ate a lot of ice cream during summer vacation."
        },
        "N5_1": {
            "example_sentence": "授業と授業の間に、少し休みます。",
            "example_reading": "じゅぎょうとじゅぎょうのあいだに、すこしやすみます。",
            "example_meaning_cn": "课与课之间稍作休息。",
            "example_meaning_en": "I take a short break between classes."
        },
        "N5_2": {
            "example_sentence": "明日、駅で友達に会います。",
            "example_reading": "あした、えきでともだちにあいます。",
            "example_meaning_cn": "明天，我要在车站和朋友见面。",
            "example_meaning_en": "I will meet my friend at the station tomorrow."
        },
        "N5_3": {
            "example_sentence": "私の好きな色は青です。",
            "example_reading": "わたしのすきないろはあおです。",
            "example_meaning_cn": "我喜欢的颜色是蓝色。",
            "example_meaning_en": "My favorite color is blue."
        },
        "N5_4": {
            "example_sentence": "あそこに青い服を着た人がいます。",
            "example_reading": "あそこにあおいふくをきたひとがいます。",
            "example_meaning_cn": "那里有一个穿着蓝色衣服的人。",
            "example_meaning_en": "There is a person wearing blue clothes over there."
        },
        "N5_5": {
            "example_sentence": "信号が赤になりました。",
            "example_reading": "しんごうがあかになりました。",
            "example_meaning_cn": "信号灯变红了。",
            "example_meaning_en": "The traffic light turned red."
        },
        "N5_6": {
            "example_sentence": "公園に赤い花が咲いています。",
            "example_reading": "こうえんにあかいはながさいています。",
            "example_meaning_cn": "公园里开着红色的花。",
            "example_meaning_en": "Red flowers are blooming in the park."
        },
        "N5_7": {
            "example_sentence": "田中さんはいつも明るい人です。",
            "example_reading": "たなかさんはいつもあかるいひとです。",
            "example_meaning_cn": "田中先生一直是个开朗的人。",
            "example_meaning_en": "Mr. Tanaka is always a cheerful person."
        },
        "N5_8": {
            "example_sentence": "暑いので、窓を開けます。",
            "example_reading": "あついので、まどをあけます。",
            "example_meaning_cn": "太热了，我把窗户打开。",
            "example_meaning_en": "It's hot, so I'll open the window."
        },
        "N5_9": {
            "example_sentence": "誕生日にプレゼントをあげました。",
            "example_reading": "たんじょうびにプレゼントをあげました。",
            "example_meaning_cn": "生日那天给了礼物。",
            "example_meaning_en": "I gave a present for the birthday."
        },
        "N5_10": {
            "example_sentence": "朝、早く起きました。",
            "example_reading": "あさ、はやくおきました。",
            "example_meaning_cn": "早晨起得很早。",
            "example_meaning_en": "I woke up early in the morning."
        },
        "N5_11": {
            "example_sentence": "学校はあさってから始まります。",
            "example_reading": "がっこうはあさってからはじまります。",
            "example_meaning_cn": "后天开始开学。",
            "example_meaning_en": "School starts the day after tomorrow."
        },
        "N5_12": {
            "example_sentence": "たくさん歩いたので、足が痛いです。",
            "example_reading": "たくさんあるいたので、あしがいたいです。",
            "example_meaning_cn": "走得太多，脚疼。",
            "example_meaning_en": "My feet hurt because I walked a lot."
        },
        "N5_13": {
            "example_sentence": "明日、一緒に映画を見ませんか。",
            "example_reading": "あした、いっしょにえいがをみませんか。",
            "example_meaning_cn": "明天一起看电影吗？",
            "example_meaning_en": "Would you like to watch a movie together tomorrow?"
        }
    }

    for item in vocab:
        item_id = item.get('id')
        if item_id in seed_data:
            item.update(seed_data[item_id])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated {len(seed_data)} items with real sentences.")

if __name__ == "__main__":
    main()
