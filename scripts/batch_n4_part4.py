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
        "N4_451": {"example_sentence": "せわ（世話）になりました。", "example_reading": "せわになりました。", "example_meaning_cn": "承蒙关照了。", "example_meaning_en": "Thank you for your help/kindness."},
        "N4_452": {"example_sentence": "ぜん（全部）部でいくらですか。", "example_reading": "ぜんぶでいくらですか。", "example_meaning_cn": "全部加起来多少钱？", "example_meaning_en": "How much is it in total?"},
        "N4_453": {"example_sentence": "せん（先生）生、質問があります。", "example_reading": "せんせい、しつもんがあります。", "example_meaning_cn": "老师，我有个问题。", "example_meaning_en": "Teacher, I have a question."},
        "N4_454": {"example_sentence": "ぜん（全国）国を旅します。", "example_reading": "ぜんこくをたびします。", "example_meaning_cn": "周游全国。", "example_meaning_en": "I'll travel across the country."},
        "N4_455": {"example_sentence": "せん（専門）門は何ですか。", "example_reading": "せんもんはなんですか。", "example_meaning_cn": "你的专业是什么？", "example_meaning_en": "What is your specialty?"},
        "N4_456": {"example_sentence": "せん（洗濯）濯をしましょう。", "example_reading": "せんたくをしましょう。", "example_meaning_cn": "洗衣服吧。", "example_meaning_en": "Let's do the laundry."},
        "N4_457": {"example_sentence": "ぜん（全然）然わかりません。", "example_reading": "ぜんぜんわかりません。", "example_meaning_cn": "完全不明白。", "example_meaning_en": "I don't understand it at all."},
        "N4_458": {"example_sentence": "せん（先日）日はありがとうございました。", "example_reading": "せんじつはありがとうございました。", "example_meaning_cn": "前几天真是谢谢您了。", "example_meaning_en": "Thank you for the other day."},
        "N4_459": {"example_sentence": "ぜん（前方）方に注意してください。", "example_reading": "ぜんぽうにちゅういしてください。", "example_meaning_cn": "请注意前方。", "example_meaning_en": "Please be careful of what's ahead."},
        "N4_460": {"example_sentence": "せい（政治）治に興味があります。", "example_reading": "せいじにきょうみがあります。", "example_meaning_cn": "对政治感兴趣。", "example_meaning_en": "I'm interested in politics."},
        "N4_461": {"example_sentence": "そう（掃除）除をしましょう。", "example_reading": "そうじをしましょう。", "example_meaning_cn": "大扫除（打扫）吧。", "example_meaning_en": "Let's do the cleaning."},
        "N4_462": {"example_sentence": "そう（相談）談に乗ってください。", "example_reading": "そうだんにのってください。", "example_meaning_cn": "请听听我的商量（或给予建议）。", "example_meaning_en": "Please give me some advice."},
        "N4_463": {"example_sentence": "そう（送別）別会を開きます。", "example_reading": "そうべつかいをひらきます。", "example_meaning_cn": "举行送别会。", "example_meaning_en": "We'll hold a farewell party."},
        "N4_464": {"example_sentence": "そ（外）に出ましょう。", "example_reading": "そとにでましょう。", "example_meaning_cn": "去外面吧。", "example_meaning_en": "Let's go outside."},
        "N4_465": {"example_sentence": "ソフト（そふと）ウェアを作ります。", "example_reading": "ソフトウェアをつくります。", "example_meaning_cn": "制作软件。", "example_meaning_en": "I make software."},
        "N4_466": {"example_sentence": "そ（空）が青いですね。", "example_reading": "そらがあおいいですね。", "example_meaning_cn": "天空真蓝呢。", "example_meaning_en": "The sky is blue, isn't it?"},
        "N4_467": {"example_sentence": "それ（それ）からどうなりましたか。", "example_reading": "それからどうなりましたか。", "example_meaning_cn": "那之后怎么样了？", "example_meaning_en": "What happened after that?"},
        "N4_468": {"example_sentence": "そ（育）てるのが大変です。", "example_reading": "そだてるのがたいへんです。", "example_meaning_cn": "抚养（或培育）很辛苦。", "example_meaning_en": "Raising/nuturing is hard."},
        "N4_469": {"example_sentence": "そつ（卒業）業しました！", "example_reading": "そつぎょうしました！", "example_meaning_cn": "毕业了！", "example_meaning_en": "Graduated!"},
        "N4_470": {"example_sentence": "その（その）理由を教えてください。", "example_reading": "そのりゆうをおしえてください。", "example_meaning_cn": "请告诉我那个理由。", "example_meaning_en": "Please tell me the reason for that."},
        "N4_471": {"example_sentence": "そふ（祖父）は元気です。", "example_reading": "そふはげんきです。", "example_meaning_cn": "祖父身体很好。", "example_meaning_en": "My grandfather is well."},
        "N4_472": {"example_sentence": "そぼ（祖母）も元気です。", "example_reading": "そぼはげんきです。", "example_meaning_cn": "祖母身体也很好。", "example_meaning_en": "My grandmother is also well."},
        "N4_473": {"example_sentence": "そ（染）めてください。", "example_reading": "そめてください。", "example_meaning_cn": "请染色（或染发）。", "example_meaning_en": "Please dye it."},
        "N4_474": {"example_sentence": "そ（反）っていますね。", "example_reading": "そっていますね。", "example_meaning_cn": "翘起来（或弯曲）了呢。", "example_meaning_en": "It's warped/curved, isn't it?"},
        "N4_475": {"example_sentence": "たい（台風）風が来ます。", "example_reading": "たいふうがきます。", "example_meaning_cn": "台风要来了。", "example_meaning_en": "A typhoon is coming."},
        "N4_476": {"example_sentence": "だい（大学）学に通っています。", "example_reading": "だいがくにかよっています。", "example_meaning_cn": "正在上大学。", "example_meaning_en": "I'm attending university."},
        "N4_477": {"example_sentence": "たい（大使）館へ行きます。", "example_reading": "たいしかんへいきます。", "example_meaning_cn": "去大使馆。", "example_meaning_en": "I'm going to the embassy."},
        "N4_478": {"example_sentence": "だい（台所）所を掃除します。", "example_reading": "だいどころをそうじします。", "example_meaning_cn": "打扫厨房。", "example_meaning_en": "I'll clean the kitchen."},
        "N4_479": {"example_sentence": "たい（体重）重が増えました。", "example_reading": "たいじゅうがふえました。", "example_meaning_cn": "体重增加了。", "example_meaning_en": "I've gained weight."},
        "N4_480": {"example_sentence": "たい（大切）切にしてください。", "example_reading": "たいせつにしてください。", "example_meaning_cn": "请珍惜（或保重）。", "example_meaning_en": "Please take good care of it/keep it precious."},
        "N4_481": {"example_sentence": "だい（大体）体わかりました。", "example_reading": "だいたいわかりました。", "example_meaning_cn": "大概明白了。", "example_meaning_en": "I basically understood."},
        "N4_482": {"example_sentence": "だい（大統領）統領に会いました。", "example_reading": "だいとうりょうにあいました。", "example_meaning_cn": "见到了总统。", "example_meaning_en": "I met the president."},
        "N4_483": {"example_sentence": "たい（大変）変ですね。", "example_reading": "たいへんですね。", "example_meaning_cn": "真够辛苦（或够受）的呢。", "example_meaning_en": "That's tough, isn't it?"},
        "N4_484": {"example_sentence": "たお（倒）れそうです。", "example_reading": "たおれそうです。", "example_meaning_cn": "快要倒下了。", "example_meaning_en": "It looks like it's going to fall/collapse."},
        "N4_485": {"example_sentence": "たかい（高い）ですね。", "example_reading": "たかいですね。", "example_meaning_cn": "挺贵的呢（或挺高的）。", "example_meaning_en": "It's expensive/high, isn't it?"},
        "N4_486": {"example_sentence": "タクシー（たくしー）に乗ります。", "example_reading": "タクシーにのります。", "example_meaning_cn": "坐出租车。", "example_meaning_en": "I'll take a taxi."},
        "N4_487": {"example_sentence": "だ（出）してください。", "example_reading": "だしてください。", "example_meaning_cn": "请拿出来。", "example_meaning_en": "Please take it out."},
        "N4_488": {"example_sentence": "た（助）けてください！", "example_reading": "たすけてください！", "example_meaning_cn": "救命（或请帮帮我）！", "example_meaning_en": "Please help me!"},
        "N4_489": {"example_sentence": "ただ（只）（無料）ですか。", "example_reading": "ただですか。", "example_meaning_cn": "是免费的吗？", "example_meaning_en": "Is it free?"},
        "N4_490": {"example_sentence": "たた（畳）みの上に座ります。", "example_reading": "たたみのうえにすわります。", "example_meaning_cn": "坐在榻榻米上。", "example_meaning_en": "I sit on the tatami."},
        "N4_491": {"example_sentence": "ただ（正）しい答えです。", "example_reading": "ただしいこたえです。", "example_meaning_cn": "正确答案。", "example_meaning_en": "Correct answer."},
        "N4_492": {"example_sentence": "たた（戦）っています。", "example_reading": "たたかっています。", "example_meaning_cn": "正在战斗。", "example_meaning_en": "They are fighting."},
        "N4_493": {"example_sentence": "たた（叩）かないでください。", "example_reading": "たたかないでください。", "example_meaning_cn": "请不要敲打。", "example_meaning_en": "Please don't hit/clap."},
        "N4_494": {"example_sentence": "た（建）ててください。", "example_reading": "たててください。", "example_meaning_cn": "请建造。", "example_meaning_en": "Please build it."},
        "N4_495": {"example_sentence": "たと（例）えばこういう事です。", "example_reading": "たとえばこういうことです。", "example_meaning_cn": "例如是这样的事。", "example_meaning_en": "For example, it's like this."},
        "N4_496": {"example_sentence": "たな（棚）に置いてください。", "example_reading": "たなにおいてください。", "example_meaning_cn": "请放在架子上。", "example_meaning_en": "Please put it on the shelf."},
        "N4_497": {"example_sentence": "たのみ（頼み）があります。", "example_reading": "たのみがあります。", "example_meaning_cn": "有个请求。", "example_meaning_en": "I have a request."},
        "N4_498": {"example_sentence": "たばこ（たばこ）を吸いますか。", "example_reading": "たばこをすいますか。", "example_meaning_cn": "抽烟吗？", "example_meaning_en": "Do you smoke?"},
        "N4_499": {"example_sentence": "た（食）べましよう。", "example_reading": "たべましょう。", "example_meaning_cn": "吃吧。", "example_meaning_en": "Let's eat."},
        "N4_500": {"example_sentence": "たま（玉）が転がっています。", "example_reading": "たまがころがっています。", "example_meaning_cn": "球（或玉）正在滚动。", "example_meaning_en": "A ball is rolling."},
        "N4_501": {"example_sentence": "たま（偶）に会います。", "example_reading": "たまにあいます。", "example_meaning_cn": "偶尔见面。", "example_meaning_en": "I meet them occasionally."},
        "N4_502": {"example_sentence": "たまご（卵）を食べます。", "example_reading": "たまごをたべます。", "example_meaning_cn": "吃鸡蛋。", "example_meaning_en": "I'll eat an egg."},
        "N4_503": {"example_sentence": "ため（為）に頑張ります。", "example_reading": "ためにがんばります。", "example_meaning_cn": "为了(目标)而加油。", "example_meaning_en": "I'll do my best for (the goal)."},
        "N4_504": {"example_sentence": "だ（誰）れが来ますか。", "example_reading": "だれがきますか。", "example_meaning_cn": "谁来？", "example_meaning_en": "Who is coming?"},
        "N4_505": {"example_sentence": "たん（誕生）誕生日おめでとう！", "example_reading": "たんじょうびおめでとう！", "example_meaning_cn": "生日快乐！", "example_meaning_en": "Happy birthday!"},
        "N4_506": {"example_sentence": "だん（男性）性ですか。", "example_reading": "だんせいですか。", "example_meaning_cn": "是男性吗？", "example_meaning_en": "Is it a male?"},
        "N4_507": {"example_sentence": "ち（地）球を守りましょう。", "example_reading": "ちきゅうをまもりましょう。", "example_meaning_cn": "保护地球吧。", "example_meaning_en": "Let's protect the Earth."},
        "N4_508": {"example_sentence": "ち（違）いますね。", "example_reading": "ちがいますね。", "example_meaning_cn": "不一样呢（或不对呢）。", "example_meaning_en": "It's different, isn't it?"},
        "N4_509": {"example_sentence": "ちか（地下）鉄に乗ります。", "example_reading": "ちかてつにのります。", "example_meaning_cn": "坐地铁。", "example_meaning_en": "I'll take the subway."},
        "N4_510": {"example_sentence": "ちか（近）くに来てください。", "example_reading": "ちかくにきてください。", "example_meaning_cn": "请靠近点。", "example_meaning_en": "Please come closer."},
        "N4_511": {"example_sentence": "ちこ（遅刻）刻しないでください。", "example_reading": "ちこくしないでください。", "example_meaning_cn": "请不要迟到。", "example_meaning_en": "Please don't be late."},
        "N4_512": {"example_sentence": "ち（知）識が豊富です。", "example_reading": "ちしきがほうふです。", "example_meaning_cn": "知识丰富。", "example_meaning_en": "I have extensive knowledge."},
        "N4_513": {"example_sentence": "ち（地）図を見てください。", "example_reading": "ちずをみてください。", "example_meaning_cn": "请看地图。", "example_meaning_en": "Please look at the map."},
        "N4_514": {"example_sentence": "ち（血）が出ています。", "example_reading": "ちがでています。", "example_meaning_cn": "流血了。", "example_meaning_en": "It's bleeding."},
        "N4_515": {"example_sentence": "ちゃ（茶）色ですね。", "example_reading": "ちゃいろですね。", "example_meaning_cn": "是茶色（棕色）呢。", "example_meaning_en": "It's brown, isn't it?"},
        "N4_516": {"example_sentence": "ちゅう（注意）意してください。", "example_reading": "ちゅういしてください。", "example_meaning_cn": "请注意。", "example_meaning_en": "Please be careful."},
        "N4_517": {"example_sentence": "ちゅう（中学校）学校へ行きます。", "example_reading": "ちゅうがっこうへいきます。", "example_meaning_cn": "去初中。", "example_meaning_en": "I'm going to middle school."},
        "N4_518": {"example_sentence": "ちゅう（注射）射が怖いです。", "example_reading": "ちゅうしゃがこわいです。", "example_meaning_cn": "怕打针。", "example_meaning_en": "I'm afraid of injections."},
        "N4_519": {"example_sentence": "ちゅう（駐車場）車場はこちらです。", "example_reading": "ちゅうしゃじょうはこちらです。", "example_meaning_cn": "停车场在这边。", "example_meaning_en": "The parking lot is over here."},
        "N4_520": {"example_sentence": "ちゅう（昼食）食を食べましょう。", "example_reading": "ちゅうしょくをたべましょう。", "example_meaning_cn": "吃午饭吧。", "example_meaning_en": "Let's eat lunch."},
        "N4_521": {"example_sentence": "ちょっと（ちょっと）待ってください。", "example_reading": "ちょっとまってください。", "example_meaning_cn": "请等一下。", "example_meaning_en": "Please wait a moment."},
        "N4_522": {"example_sentence": "つ（使）ってください。", "example_reading": "つかってください。", "example_meaning_cn": "请使用。", "example_meaning_en": "Please use it."},
        "N4_523": {"example_sentence": "つか（捕）まえました！", "example_reading": "つかまえました！", "example_meaning_cn": "逮住了！", "example_meaning_en": "Caught it!"},
        "N4_524": {"example_sentence": "つか（疲）れましたか。", "example_reading": "つかれましたか。", "example_meaning_cn": "累了吗？", "example_meaning_en": "Are you tired?"},
        "N4_525": {"example_sentence": "つ（着）きましたか。", "example_reading": "つきましたか。", "example_meaning_cn": "到了吗？", "example_meaning_en": "Did you arrive?"},
        "N4_526": {"example_sentence": "つ（次）は誰ですか。", "example_reading": "つぎはだれですか。", "example_meaning_cn": "下一个是谁？", "example_meaning_en": "Who is next?"},
        "N4_527": {"example_sentence": "つく（机）の上に置いてください。", "example_reading": "つくえのうえにおいてください。", "example_meaning_cn": "请放在桌上。", "example_meaning_en": "Please put it on the desk."},
        "N4_528": {"example_sentence": "つく（作）ってください。", "example_reading": "つくってください。", "example_meaning_cn": "请制作。", "example_meaning_en": "Please make it."},
        "N4_529": {"example_sentence": "つ（付）けてください。", "example_reading": "つけてください。", "example_meaning_cn": "请附加上（或涂上）。", "example_meaning_en": "Please attach/put it on."},
        "N4_530": {"example_sentence": "つ（点）けてください。", "example_reading": "つけてください。", "example_meaning_cn": "请点亮（或开灯）。", "example_meaning_en": "Please turn it on."},
        "N4_531": {"example_sentence": "つ（伝）えてください。", "example_reading": "つたえてください。", "example_meaning_cn": "请转告。", "example_meaning_en": "Please convey the message."},
        "N4_532": {"example_sentence": "ずっと（ずっと）大好きです。", "example_reading": "ずっとだいすきです。", "example_meaning_cn": "一直最喜欢你。", "example_meaning_en": "I'll always love you."},
        "N4_533": {"example_sentence": "つ（包）んでください。", "example_reading": "つつんでください。", "example_meaning_cn": "请包起来。", "example_meaning_en": "Please wrap it up."},
        "N4_534": {"example_sentence": "つと（勤）めています。", "example_reading": "つとめています。", "example_meaning_cn": "正在任职（或工作）。", "example_meaning_en": "I am employed (at)."},
        "N4_535": {"example_sentence": "つな（繋）いでいてください。", "example_reading": "つないでいてください。", "example_meaning_cn": "请保持连接（或牵手）。", "example_meaning_en": "Please keep it connected/hold hands."},
        "N4_536": {"example_sentence": "つよい（強い）ですね。", "example_reading": "つよいですね。", "example_meaning_cn": "挺强的呢。", "example_meaning_en": "It's strong, isn't it?"},
        "N4_537": {"example_sentence": "つ（連）れて行ってください。", "example_reading": "つれていってください。", "example_meaning_cn": "请带我一起去。", "example_meaning_en": "Please take me with you."},
        "N4_538": {"example_sentence": "て（手）を洗ってください。", "example_reading": "てをあらってください。", "example_meaning_cn": "请洗手。", "example_meaning_en": "Please wash your hands."},
        "N4_539": {"example_sentence": "てい（丁寧）寧に話しましょう。", "example_reading": "ていねいにはなしましょう。", "example_meaning_cn": "礼貌地说话吧。", "example_meaning_en": "Let's speak politely."},
        "N4_540": {"example_sentence": "て（出）てください。", "example_reading": "でてください。", "example_meaning_cn": "请出去（或出席）。", "example_meaning_en": "Please go out/attend."},
        "N4_541": {"example_sentence": "て（手）传ってください。", "example_reading": "てつだってください。", "example_meaning_cn": "请帮帮我。", "example_meaning_en": "Please help me."},
        "N4_542": {"example_sentence": "てつ（鉄道）道を使います。", "example_reading": "てつどうをつかいます。", "example_meaning_cn": "使用铁路（交通）。", "example_meaning_en": "I use the railway."},
        "N4_543": {"example_sentence": "テキスト（てきすと）を読んでください。", "example_reading": "テキストをよんでください。", "example_meaning_cn": "请读课文。", "example_meaning_en": "Please read the text."},
        "N4_544": {"example_sentence": "てがみ（手紙）を書きます。", "example_reading": "てがみをかきます。", "example_meaning_cn": "写信。", "example_meaning_en": "I'll write a letter."},
        "N4_545": {"example_sentence": "でき（出来）ました！", "example_reading": "できました！", "example_meaning_cn": "做好了（或完成了）！", "example_meaning_en": "It's done!"},
        "N4_546": {"example_sentence": "てぐち（出口）はあちらです。", "example_reading": "でぐちはあちらです。", "example_meaning_cn": "出口在那边。", "example_meaning_en": "The exit is over there."},
        "N4_547": {"example_sentence": "テスト（てすと）があります。", "example_reading": "テストがあります。", "example_meaning_cn": "有考试。", "example_meaning_en": "There is a test."},
        "N4_548": {"example_sentence": "で（出）てください。", "example_reading": "でてください。", "example_meaning_cn": "请接（电话）或请出来。", "example_meaning_en": "Please answer/come out."},
        "N4_549": {"example_sentence": "て（手）伝いましょうか。", "example_reading": "てつだいましょうか。", "example_meaning_cn": "需要我帮忙吗？", "example_meaning_en": "Shall I help you?"},
        "N4_550": {"example_sentence": "てぶくろ（手袋）をはめます。", "example_reading": "てぶくろをはめます。", "example_meaning_cn": "戴上手套。", "example_meaning_en": "I'll put on gloves."},
        "N4_551": {"example_sentence": "て（寺）院を訪ねます。", "example_reading": "じいんをたずねます。", "example_meaning_cn": "拜访寺庙。", "example_meaning_en": "I'll visit the temple."},
        "N4_552": {"example_sentence": "てん（点）数を聞いてください。", "example_reading": "てんすうをきいてください。", "example_meaning_cn": "请报一下分数。", "example_meaning_en": "Please tell me the score."},
        "N4_553": {"example_sentence": "てん（店）員さんは親切です。", "example_reading": "てんいんさんはしんせつです。", "example_meaning_cn": "店员很亲切。", "example_meaning_en": "The shop staff are kind."},
        "N4_554": {"example_sentence": "てん（天気）気予報を見てください。", "example_reading": "てんきよほうをみてください。", "example_meaning_cn": "请看天气报。", "example_meaning_en": "Please watch the weather forecast."},
        "N4_555": {"example_sentence": "てん（電車）车に乗ります。", "example_reading": "でんしゃにのります。", "example_meaning_cn": "坐电车。", "example_meaning_en": "I'll take the train."},
        "N4_556": {"example_sentence": "てん（電話）话してください。", "example_reading": "でんわしてください。", "example_meaning_cn": "请打电话。", "example_meaning_en": "Please make a call."},
        "N4_557": {"example_sentence": "と（戸）を闭めてください。", "example_reading": "とをしめてください。", "example_meaning_cn": "请关门。", "example_meaning_en": "Please close the door."},
        "N4_558": {"example_sentence": "ど（度）忘れしました。", "example_reading": "どわすれしました。", "example_meaning_cn": "突然想不起来了。", "example_meaning_en": "I suddenly forgot."},
        "N4_559": {"example_sentence": "とい（問）い答えてください。", "example_reading": "といにこたえてください。", "example_meaning_cn": "请回答提问。", "example_meaning_en": "Please answer the question."},
        "N4_600": {"example_sentence": "に（似）合っていますね。", "example_reading": "にあっていますね。", "example_meaning_cn": "挺适合（你）的呢。", "example_meaning_en": "It suits you well, doesn't it?"}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N4_600.")

if __name__ == "__main__":
    main()
