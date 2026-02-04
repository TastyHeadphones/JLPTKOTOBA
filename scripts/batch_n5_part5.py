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
        "N5_251": {"example_sentence": "空が青いです。", "example_reading": "そらがあおいです。", "example_meaning_cn": "天空是蓝色的。", "example_meaning_en": "The sky is blue."},
        "N5_252": {"example_sentence": "それ、いいですね。", "example_reading": "それ、いいですね。", "example_meaning_cn": "那个，很好呢。", "example_meaning_en": "That's good, isn't it?"},
        "N5_253": {"example_sentence": "それは何ですか。", "example_reading": "それはなんですか。", "example_meaning_cn": "那个是什么？", "example_meaning_en": "What is that?"},
        "N5_254": {"example_sentence": "外は雨が降っています。", "example_reading": "そとはあめがふっています。", "example_meaning_cn": "外面在下雨。", "example_meaning_en": "It's raining outside."},
        "N5_255": {"example_sentence": "大学まで一時間です。", "example_reading": "だいがくまでいちじかんです。", "example_meaning_cn": "到大学要一个小时。", "example_meaning_en": "It takes one hour to the university."},
        "N5_256": {"example_sentence": "大学校に行きます。", "example_reading": "だいがっこうにいきます。", "example_meaning_cn": "去大学。", "example_meaning_en": "I go to university."},
        "N5_257": {"example_sentence": "背が高いですね。", "example_reading": "せがたかいですね。", "example_meaning_cn": "个子很高呢。", "example_meaning_en": "You're tall, aren't you?"},
        "N5_258": {"example_sentence": "大好きです。 ", "example_reading": "だいすきです。", "example_meaning_cn": "非常喜欢。", "example_meaning_en": "I love it."},
        "N5_259": {"example_sentence": "大丈夫ですよ。", "example_reading": "だいじょうぶですよ。", "example_meaning_cn": "没关系哦。", "example_meaning_en": "It's okay."},
        "N5_260": {"example_sentence": "台所に母がいます。", "example_reading": "だいどころにははがいます。", "example_meaning_cn": "妈妈在厨房里。", "example_meaning_en": "My mother is in the kitchen."},
        "N5_261": {"example_sentence": "高い時計を買いました。", "example_reading": "たかいとけいをかいました。", "example_meaning_cn": "买了一只昂贵的手表。", "example_meaning_en": "I bought an expensive watch."},
        "N5_262": {"example_sentence": "荷物をたくさん持っています。", "example_reading": "よりもつをたくさんもっています。", "example_meaning_cn": "拿了很多行李。", "example_meaning_en": "I'm holding a lot of luggage."},
        "N5_263": {"example_sentence": "タクシーを呼びましょう。", "example_reading": "タクシーをよびましょう。", "example_meaning_cn": "叫出租车吧。", "example_meaning_en": "Let's call a taxi."},
        "N5_264": {"example_sentence": "パンを出してください。", "example_reading": "パンをだしてください。", "example_meaning_cn": "请把面包拿出来。", "example_meaning_en": "Please take out the bread."},
        "N5_265": {"example_sentence": "ただいま。", "example_reading": "ただいま。", "example_meaning_cn": "我回来了。", "example_meaning_en": "I'm back."},
        "N5_266": {"example_sentence": "あ、立ちましょう。", "example_reading": "あ、たちましょう。", "example_meaning_cn": "啊，站起来吧。", "example_meaning_en": "Oh, let's stand up."},
        "N5_267": {"example_sentence": "建物が古いです。", "example_reading": "たてものがふるいです。", "example_meaning_cn": "建筑很旧。", "example_meaning_en": "The building is old."},
        "N5_268": {"example_sentence": "楽しく遊びましょう。", "example_reading": "たのしくあそびましょう。", "example_meaning_cn": "愉快地玩吧。", "example_meaning_en": "Let's play happily."},
        "N5_269": {"example_sentence": "お願いします。", "example_reading": "おねがいします。", "example_meaning_cn": "拜托了。", "example_meaning_en": "Please."},
        "N5_270": {"example_sentence": "たばこを吸いますか。", "example_reading": "たばこをすいますか。", "example_meaning_cn": "抽烟吗？", "example_meaning_en": "Do you smoke?"},
        "N5_271": {"example_sentence": "卵を二個食べます。", "example_reading": "たまごをにこたべます。", "example_meaning_cn": "吃两个鸡蛋。", "example_meaning_en": "I eat two eggs."},
        "N5_272": {"example_sentence": "誰に会いましたか。", "example_reading": "だれにあいましたか。", "example_meaning_cn": "见到了谁？", "example_meaning_en": "Who did you meet?"},
        "N5_273": {"example_sentence": "誕生日はいつですか。", "example_reading": "たんじょうびはいつですか。", "example_meaning_cn": "生日是什么时候？", "example_meaning_en": "When is your birthday?"},
        "N5_274": {"example_sentence": "だんだん寒くなりました。", "example_reading": "だんだんさむくなりました。", "example_meaning_cn": "渐渐变冷了。", "example_meaning_en": "It gradually became colder."},
        "N5_275": {"example_sentence": "小さいカバンが欲しいです。", "example_reading": "ちいさいカバンがほしいです。", "example_meaning_cn": "想要个小包。", "example_meaning_en": "I want a small bag."},
        "N5_276": {"example_sentence": "近くに公園があります。", "example_reading": "ちかくにこうえんがあります。", "example_meaning_cn": "附近有公园。", "example_meaning_en": "There is a park nearby."},
        "N5_277": {"example_sentence": "地下鉄で帰ります。", "example_reading": "ちかてつでかえります。", "example_meaning_cn": "坐地铁回去。", "example_meaning_en": "I'll go back by subway."},
        "N5_278": {"example_sentence": "地図を見てください。", "example_reading": "ちずをみてください。", "example_meaning_cn": "请看地图。", "example_meaning_en": "Please look at the map."},
        "N5_279": {"example_sentence": "父は教師です。", "example_reading": "ちちはきょうしです。", "example_meaning_cn": "父亲是教师。", "example_meaning_en": "My father is a teacher."},
        "N5_280": {"example_sentence": "茶色い靴を履いています。", "example_reading": "ちゃいろいくつをはいています。", "example_meaning_cn": "穿着棕色的鞋子。", "example_meaning_en": "I'm wearing brown shoes."},
        "N5_281": {"example_sentence": "お茶を飲みましょう。", "example_reading": "おちゃをのみましょう。", "example_meaning_cn": "喝茶吧。", "example_meaning_en": "Let's drink tea."},
        "N5_282": {"example_sentence": "ちょうど十時です。", "example_reading": "ちょうどじゅうじです。", "example_meaning_cn": "正好十点。", "example_meaning_en": "It's exactly ten o'clock."},
        "N5_283": {"example_sentence": "ちょっと待ってください。", "example_reading": "ちょっとまってください。", "example_meaning_cn": "请等一下。", "example_meaning_en": "Please wait a moment."},
        "N5_284": {"example_sentence": "一ヶ月に一回旅行します。", "example_reading": "いっかげつにいっかいりょこうします。", "example_meaning_cn": "一个月旅行一次。", "example_meaning_en": "I travel once a month."},
        "N5_285": {"example_sentence": "一日中勉強しました。", "example_reading": "いちにちじゅうべんきょうしました。", "example_meaning_cn": "学了一整天。", "example_meaning_en": "I studied all day."},
        "N5_286": {"example_sentence": "使ってください。 ", "example_reading": "つかってください。", "example_meaning_cn": "请使用。", "example_meaning_en": "Please use it."},
        "N5_287": {"example_sentence": "疲れましたね。", "example_reading": "つかれましたね。", "example_meaning_cn": "累了吧。", "example_meaning_en": "You're tired, aren't you?"},
        "N5_288": {"example_sentence": "次のバスに乗ります。", "example_reading": "つぎのバスにのります。", "example_meaning_cn": "坐下一班公交。", "example_meaning_en": "I'll take the next bus."},
        "N5_289": {"example_sentence": "机を拭きます。", "example_reading": "つくえをふきます。", "example_meaning_cn": "擦桌子。", "example_meaning_en": "I'll wipe the desk."},
        "N5_290": {"example_sentence": "料理を作ります。", "example_reading": "りょうりをつくります。", "example_meaning_cn": "做饭。", "example_meaning_en": "I'll cook a meal."},
        "N5_291": {"example_sentence": "テレビをつけます。", "example_reading": "テレビをつけます。", "example_meaning_cn": "开电视。", "example_meaning_en": "I'll turn on the TV."},
        "N5_292": {"example_sentence": "勤めています。", "example_reading": "つとめています。", "example_meaning_cn": "正在工作（就职）。", "example_meaning_en": "I am employed."},
        "N5_293": {"example_sentence": "つまらない話です。", "example_reading": "つまらないはなしです。", "example_meaning_cn": "无聊的话。", "example_meaning_en": "It's a boring story."},
        "N5_294": {"example_sentence": "冷たい水が欲しいです。", "example_reading": "つめたいみずがほしいです。", "example_meaning_cn": "想要凉水。", "example_meaning_en": "I want some cold water."},
        "N5_295": {"example_sentence": "強い風が吹いています。", "example_reading": "つよいかぜがふいています。", "example_meaning_cn": "狂风大作。", "example_meaning_en": "A strong wind is blowing."},
        "N5_296": {"example_sentence": "手で食べます。", "example_reading": "てでたべます。", "example_meaning_cn": "用手吃。", "example_meaning_en": "I eat with my hands."},
        "N5_297": {"example_sentence": "テープを聞きます。", "example_reading": "テープをききます。", "example_meaning_cn": "听录音带。", "example_meaning_en": "I'll listen to the tape."},
        "N5_298": {"example_sentence": "テーブルを片付けます。", "example_reading": "テーブルをかたづけます。", "example_meaning_cn": "收拾桌子。", "example_meaning_en": "I'll clear the table."},
        "N5_299": {"example_sentence": "出かけます。", "example_reading": "でかけます。", "example_meaning_cn": "出门。", "example_meaning_en": "I'm going out."},
        "N5_300": {"example_sentence": "手紙を書きます。", "example_reading": "てがみをかきます。", "example_meaning_cn": "写信。", "example_meaning_en": "I'll write a letter."},
        "N5_301": {"example_sentence": "できるだけ早く来てください。", "example_reading": "できるだけはやくきてください。", "example_meaning_cn": "请尽可能早点过来。", "example_meaning_en": "Please come as soon as possible."},
        "N5_302": {"example_sentence": "出口はあちらです。", "example_reading": "でぐちはあちらです。", "example_meaning_cn": "出口在那边。", "example_meaning_en": "The exit is over there."},
        "N5_303": {"example_sentence": "テストがあります。", "example_reading": "テストがあります。", "example_meaning_cn": "有考试。", "example_meaning_en": "There is a test."},
        "N5_304": {"example_sentence": "では、また明日。", "example_reading": "では、またあした。", "example_meaning_cn": "那么，明天见。", "example_meaning_en": "Well then, see you tomorrow."},
        "N5_305": {"example_sentence": "デパートで買い物をしました。", "example_reading": "デパートでかいものをしました。", "example_meaning_cn": "在百货商店买东西了。", "example_meaning_en": "I went shopping at the department store."},
        "N5_306": {"example_sentence": "電気がつきました。", "example_reading": "でんきがつきました。", "example_meaning_cn": "灯亮了。", "example_meaning_en": "The light came on."},
        "N5_307": {"example_sentence": "電車で行きましょう。", "example_reading": "でんしゃでいきましょう。", "example_meaning_cn": "坐电车去吧。", "example_meaning_en": "Let's go by train."},
        "N5_308": {"example_sentence": "この料理は電話で注文できます。", "example_reading": "このりょうりはでんわでちゅうもんできます。", "example_meaning_cn": "这个菜可以用电话订。", "example_meaning_en": "You can order this dish over the phone."},
        "N5_309": {"example_sentence": "ドアを開けてください。", "example_reading": "ドアをあけてください。", "example_meaning_cn": "请开门。", "example_meaning_en": "Please open the door."},
        "N5_310": {"example_sentence": "トイレはどこですか。", "example_reading": "トイレはどこですか。", "example_meaning_cn": "厕所在哪儿？", "example_meaning_en": "Where is the toilet?"},
        "N5_311": {"example_sentence": "どういたしまして。", "example_reading": "どういたしまして。", "example_meaning_cn": "不客气。", "example_meaning_en": "You're welcome."},
        "N5_312": {"example_sentence": "どうぞ座ってください。", "example_reading": "どうぞすわってください。", "example_meaning_cn": "请坐。", "example_meaning_en": "Please have a seat."},
        "N5_313": {"example_sentence": "どうもありがとうございます。", "example_reading": "どうもありがとうございます。", "example_meaning_cn": "非常感谢。", "example_meaning_en": "Thank you very much."},
        "N5_314": {"example_sentence": "十円足りません。", "example_reading": "じゅうえんたりません。", "example_meaning_cn": "差十日元。", "example_meaning_en": "It's ten yen short."},
        "N5_315": {"example_sentence": "遠いですね。", "example_reading": "とおいですね。", "example_meaning_cn": "挺远的呢。", "example_meaning_en": "It's far, isn't it?"},
        "N5_316": {"example_sentence": "十日間休みます。", "example_reading": "とおかかんやすみます。", "example_meaning_cn": "休息十天。", "example_meaning_en": "I'll take a ten-day break."},
        "N5_317": {"example_sentence": "時々映画を見ます。", "example_reading": "ときどきえいがをみます。", "example_meaning_cn": "有时看电影。", "example_meaning_en": "I sometimes watch movies."},
        "N5_318": {"example_sentence": "時計を直します。", "example_reading": "とけいをなおします。", "example_meaning_cn": "修表。", "example_meaning_en": "I'll fix the watch."},
        "N5_319": {"example_sentence": "どこへ行きますか。", "example_reading": "どこへいきますか。", "example_meaning_cn": "去哪儿？", "example_meaning_en": "Where are you going?"},
        "N5_320": {"example_sentence": "床屋へ行きます。", "example_reading": "とこやへいきまります。", "example_meaning_cn": "去理发店。", "example_meaning_en": "I'm going to the barber shop."},
        "N5_321": {"example_sentence": "所持金を確認します。", "example_reading": "しょじきんをかくにんします。", "example_meaning_cn": "确认所持现金。", "example_meaning_en": "Check the cash on hand."},
        "N5_322": {"example_sentence": "図書館で勉強します。", "example_reading": "としょかんでべんきょうします。", "example_meaning_cn": "在图书馆学习。", "example_meaning_en": "I'll study at the library."},
        "N5_323": {"example_sentence": "どちらがいいですか。", "example_reading": "どちらがいいですか。", "example_meaning_cn": "哪个好？", "example_meaning_en": "Which one is better?"},
        "N5_324": {"example_sentence": "どっちが好きですか。", "example_reading": "どっちがすきですか。", "example_meaning_cn": "喜欢哪个？", "example_meaning_en": "Which one do you like?"},
        "N5_325": {"example_sentence": "とても寒いです。", "example_reading": "とてもさむいです。", "example_meaning_cn": "非常冷。", "example_meaning_en": "It's very cold."},
        "N5_326": {"example_sentence": "友達と遊びます。", "example_reading": "ともだちとあそびます。", "example_meaning_cn": "和朋友一起玩。", "example_meaning_en": "I'll play with a friend."},
        "N5_327": {"example_sentence": "土曜日、暇ですか。", "example_reading": "どようび、ひまですか。", "example_meaning_cn": "周六有空吗？", "example_meaning_en": "Are you free on Saturday?"},
        "N5_328": {"example_sentence": "鳥が飛んでいます。", "example_reading": "とりがとんでいます。", "example_meaning_cn": "鸟在飞。", "example_meaning_en": "Birds are flying."},
        "N5_329": {"example_sentence": "鶏肉が好きです。", "example_reading": "とりにくがすきです。", "example_meaning_cn": "喜欢吃鸡肉。", "example_meaning_en": "I like chicken meat."},
        "N5_330": {"example_sentence": "リンゴを取ってください。", "example_reading": "リンゴをとってください。", "example_meaning_cn": "请拿个苹果。", "example_meaning_en": "Please take an apple."},
        "N5_331": {"example_sentence": "写真を撮りましょう。", "example_reading": "しゃしんをとりましょう。", "example_meaning_cn": "拍照吧。", "example_meaning_en": "Let's take a photo."},
        "N5_332": {"example_sentence": "どれがあなたのですか。", "example_reading": "どれがあなたのですか。", "example_meaning_cn": "哪个是你的？", "example_meaning_en": "Which one is yours?"},
        "N5_333": {"example_sentence": "どんな音楽が好きですか。", "example_reading": "どんなおんがくがすきですか。", "example_meaning_cn": "喜欢什么样的音乐？", "example_meaning_en": "What kind of music do you like?"},
        "N5_334": {"example_sentence": "ナイフで切ります。", "example_reading": "ナイフできります。", "example_meaning_cn": "用小刀切。", "example_meaning_en": "I'll cut it with a knife."},
        "N5_335": {"example_sentence": "中に入りましょう。", "example_reading": "なかにはいりましょう。", "example_meaning_cn": "进到里面去吧。", "example_meaning_en": "Let's go inside."},
        "N5_336": {"example_sentence": "長いですね。", "example_reading": "ながいですね。", "example_meaning_cn": "挺长的呢。", "example_meaning_en": "It's long, isn't it?"},
        "N5_337": {"example_sentence": "夏休みが楽しみです。", "example_reading": "なつやすみがたのしみです。", "example_meaning_cn": "期待暑假。", "example_meaning_en": "I'm looking forward to summer vacation."},
        "N5_338": {"example_sentence": "何がありますか。", "example_reading": "なにがありますか。", "example_meaning_cn": "有什么？", "example_meaning_en": "What is there?"},
        "N5_339": {"example_sentence": "七時に起きます。", "example_reading": "ななじにおきます。", "example_meaning_cn": "七点起床。", "example_meaning_en": "I wake up at seven."},
        "N5_340": {"example_sentence": "七日後に行きます。", "example_reading": "なのかごにいきます。", "example_meaning_cn": "七天后去。", "example_meaning_en": "I'll go in seven days."},
        "N5_341": {"example_sentence": "名前を書いてください。", "example_reading": "なまえをかいてください。", "example_meaning_cn": "请写下名字。", "example_meaning_en": "Please write your name."},
        "N5_342": {"example_sentence": "習っています。", "example_reading": "ならっています。", "example_meaning_cn": "正在学习（拜师）。", "example_meaning_en": "I am learning."},
        "N5_343": {"example_sentence": "並んでください。", "example_reading": "ならんでください。", "example_meaning_cn": "请排队。", "example_meaning_en": "Please line up."},
        "N5_344": {"example_sentence": "日本は素晴らしい国です。", "example_reading": "にほんはすばらしいくにです。", "example_meaning_cn": "日本是个伟大的国家。", "example_meaning_en": "Japan is a wonderful country."},
        "N5_345": {"example_sentence": "毎日、お風呂に入ります。", "example_reading": "まいにち、おふろにはいります。", "example_meaning_cn": "每天泡澡。 ", "example_meaning_en": "I take a bath every day."},
        "N5_346": {"example_sentence": "荷物を送ります。", "example_reading": "よりもつをおくります。", "example_meaning_cn": "寄行李。", "example_meaning_en": "I'll send the luggage."},
        "N5_347": {"example_sentence": "肉を食べますか。", "example_reading": "にくをたべますか。", "example_meaning_cn": "吃肉吗？", "example_meaning_en": "Do you eat meat?"},
        "N5_348": {"example_sentence": "西のほうは山です。", "example_reading": "にしのはうはやまです。", "example_meaning_cn": "西边是山。", "example_meaning_en": "There are mountains to the west."},
        "N5_349": {"example_sentence": "日曜日、買い物に行きます。", "example_reading": "にちようび、かいものにいきます。", "example_meaning_cn": "周日去买东西。", "example_meaning_en": "I'm going shopping on Sunday."},
        "N5_350": {"example_sentence": "五日に行きます。", "example_reading": "いつかにいきます。", "example_meaning_cn": "五号去。", "example_meaning_en": "I'll go on the fifth."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N5_350.")

if __name__ == "__main__":
    main()
