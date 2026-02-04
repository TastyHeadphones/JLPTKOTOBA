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
        "N4_601": {"example_sentence": "に（似）たようなものですね。", "example_reading": "にたようなものですね。", "example_meaning_cn": "差不多（类似）的东西呢。", "example_meaning_en": "It's something similar, isn't it?"},
        "N4_602": {"example_sentence": "に（握）ってください。", "example_reading": "にぎってください。", "example_meaning_cn": "请握住（或握寿司）。", "example_meaning_en": "Please grasp it (or make sushi)."},
        "N4_603": {"example_sentence": "にぎ（賑）やかですね。", "example_reading": "にぎやかですね。", "example_meaning_cn": "真够热闹的呢。", "example_meaning_en": "It's lively, isn't it?"},
        "N4_604": {"example_sentence": "に（肉）を食べましよう。", "example_reading": "にくをたべましょう。", "example_meaning_cn": "吃肉吧。", "example_meaning_en": "Let's eat meat."},
        "N4_605": {"example_sentence": "に（逃）げてください！", "example_reading": "にげてください！", "example_meaning_cn": "快逃吧！", "example_meaning_en": "Please run away!"},
        "N4_606": {"example_sentence": "にっき（日記）を書きます。", "example_reading": "にっきをかきます。", "example_meaning_cn": "写日记。", "example_meaning_en": "I'll write a diary."},
        "N4_607": {"example_sentence": "に（荷）物（もつ）を運びます。", "example_reading": "にもつをはこびます。", "example_meaning_cn": "搬运行李。", "example_meaning_en": "I'll carry the luggage."},
        "N4_608": {"example_sentence": "にゅう（入場）場してください。", "example_reading": "にゅうじょうしてください。", "example_meaning_cn": "请入场。", "example_meaning_en": "Please enter the venue."},
        "N4_609": {"example_sentence": "にゅう（入院）院しました。", "example_reading": "にゅういんしました。", "example_meaning_cn": "住院了。", "example_meaning_en": "I was hospitalized."},
        "N4_610": {"example_sentence": "にゅう（入学）学おめでとう！", "example_reading": "にゅうがくおめでとう！", "example_meaning_cn": "入学快乐！", "example_meaning_en": "Congratulations on your school entrance!"},
        "N4_611": {"example_sentence": "に（煮）てください。", "example_reading": "にてください。", "example_meaning_cn": "请煮（或炖）一下。", "example_meaning_en": "Please boil/stew it."},
        "N4_612": {"example_sentence": "にわ（庭）で遊びます。", "example_reading": "にわであそびます。", "example_meaning_cn": "在院子里玩。", "example_meaning_en": "I'll play in the garden."},
        "N4_613": {"example_sentence": "に（抜）いてください。", "example_reading": "ぬいてください。", "example_meaning_cn": "请拔出来（或超过）。", "example_meaning_en": "Please pull it out/exceed."},
        "N4_614": {"example_sentence": "ぬ（脱）いでください。", "example_reading": "ぬいでください。", "example_meaning_cn": "请脱掉（衣服/鞋）。", "example_meaning_en": "Please take off (your clothes/shoes)."},
        "N4_615": {"example_sentence": "ぬ（塗）ってください。", "example_reading": "ぬってください。", "example_meaning_cn": "请涂抹。", "example_meaning_en": "Please apply/paint it on."},
        "N4_616": {"example_sentence": "ぬ（濡）れていますね。", "example_reading": "ぬれていますね。", "example_meaning_cn": "湿了呢。", "example_meaning_en": "It's wet, isn't it?"},
        "N4_617": {"example_sentence": "ね（根）っこが深いです。", "example_reading": "ねっこがふかいです。", "example_meaning_cn": "根扎得很深。", "example_meaning_en": "The roots are deep."},
        "N4_618": {"example_sentence": "ね（寝）てください。", "example_reading": "ねてください。", "example_meaning_cn": "请睡觉。", "example_meaning_en": "Please sleep."},
        "N4_619": {"example_sentence": "ねだん（値段）はいくらですか。", "example_reading": "ねだんはいくらですか。", "example_meaning_cn": "价格是多少？", "example_meaning_en": "How much is the price?"},
        "N4_620": {"example_sentence": "ねつ（熱）がありますか。", "example_reading": "ねつがありますか。", "example_meaning_cn": "发烧了吗？", "example_meaning_en": "Do you have a fever?"},
        "N4_621": {"example_sentence": "ね（寝）坊しました。", "example_reading": "ねぼうしました。", "example_meaning_cn": "起晚了。", "example_meaning_en": "I overslept."},
        "N4_622": {"example_sentence": "ね（猫）がいます。", "example_reading": "ねこがいます。", "example_meaning_cn": "有猫。", "example_meaning_en": "There is a cat."},
        "N4_623": {"example_sentence": "ねむ（眠）いですか。", "example_reading": "ねむいですか。", "example_meaning_cn": "困了吗？", "example_meaning_en": "Are you sleepy?"},
        "N4_624": {"example_sentence": "ねむ（眠）ってください。", "example_reading": "ねむってください。", "example_meaning_cn": "请入睡。", "example_meaning_en": "Please go to sleep."},
        "N4_625": {"example_sentence": "ね（練）ってください。", "example_reading": "ねってください。", "example_meaning_cn": "请揉捏（或构思）。", "example_meaning_en": "Please knead/elaborate."},
        "N4_626": {"example_sentence": "ねん（年度）度末です。", "example_reading": "ねんどまつです。", "example_meaning_cn": "是年度末。", "example_meaning_en": "It's the end of the fiscal year."},
        "N4_627": {"example_sentence": "ね（年）齢（れい）を聞いてください。", "example_reading": "ねんれいをきいてください。", "example_meaning_cn": "请问一下年龄。", "example_meaning_en": "Please ask the age."},
        "N4_628": {"example_sentence": "の（野）原で遊びます。", "example_reading": "のはらであそびます。", "example_meaning_cn": "在原野玩耍。", "example_meaning_en": "I'll play in the field."},
        "N4_629": {"example_sentence": "の（能）力が高いです。", "example_reading": "のうりょくがたかいです。", "example_meaning_cn": "能力很高。", "example_meaning_en": "The ability is high."},
        "N4_630": {"example_sentence": "の（残）されてしまいました。", "example_reading": "のこされてしまいました。", "example_meaning_cn": "被留下了。", "example_meaning_en": "I was left behind."},
        "N4_631": {"example_sentence": "の（残）りはありません。", "example_reading": "のこりはありません。", "example_meaning_cn": "没有剩余。", "example_meaning_en": "There is nothing left."},
        "N4_632": {"example_sentence": "の（載）せてください。", "example_reading": "のせてください。", "example_meaning_cn": "请放上（或刊载）。", "example_meaning_en": "Please place it on/publish it."},
        "N4_633": {"example_sentence": "のど（喉）が痛いです。", "example_reading": "のどがいたいです。", "example_meaning_cn": "嗓子疼。", "example_meaning_en": "My throat hurts."},
        "N4_634": {"example_sentence": "のり（乗）り換えてください。", "example_reading": "のりかえてください。", "example_meaning_cn": "请换乘。", "example_meaning_en": "Please transfer."},
        "N4_635": {"example_sentence": "の（飲）みましょう。", "example_reading": "のみましょう。", "example_meaning_cn": "喝吧。", "example_meaning_en": "Let's drink."},
        "N4_636": {"example_sentence": "の（乗）りましょう。", "example_reading": "のりましょう。", "example_meaning_cn": "上（车）吧。", "example_meaning_en": "Let's get on."},
        "N4_637": {"example_sentence": "は（歯）を磨いてください。", "example_reading": "はをみがいてください。", "example_meaning_cn": "请刷牙。", "example_meaning_en": "Please brush your teeth."},
        "N4_638": {"example_sentence": "パーティー（ぱーてぃー）に行きます。", "example_reading": "パーティーにいきます。", "example_meaning_cn": "去参加派对。", "example_meaning_en": "I'm going to a party."},
        "N4_639": {"example_sentence": "はい（はい）。 ", "example_reading": "はい。", "example_meaning_cn": "是的。 ", "example_meaning_en": "Yes."},
        "N4_640": {"example_sentence": "はい（拝）見します。", "example_reading": "はいけんします。", "example_meaning_cn": "拜读（或看，谦指）。", "example_meaning_en": "I will see/read (humble)."},
        "N4_641": {"example_sentence": "はい（歯医者）医者さんに行きます。", "example_reading": "はいしゃさんにいきます。", "example_meaning_cn": "去看牙医。", "example_meaning_en": "I'm going to the dentist."},
        "N4_642": {"example_sentence": "はい（入）ってください。", "example_reading": "はいってください。", "example_meaning_cn": "请进。", "example_meaning_en": "Please come in."},
        "N4_643": {"example_sentence": "はく（履）いてください。", "example_reading": "はいてください。", "example_meaning_cn": "请穿上（下装/鞋袜）。", "example_meaning_en": "Please put them on."},
        "N4_644": {"example_sentence": "はく（吐）かないでください。", "example_reading": "はかないでください。", "example_meaning_cn": "请不要呕吐（或说出）。", "example_meaning_en": "Please don't vomit/spit it out."},
        "N4_645": {"example_sentence": "は（葉）がきれいに紅葉しました。", "example_reading": "はがきれいにこうようしました。", "example_meaning_cn": "叶子红得很漂亮。", "example_meaning_en": "The leaves have turned red beautifully."},
        "N4_646": {"example_sentence": "はき（掃）いてください。", "example_reading": "はいてください。", "example_meaning_cn": "请清扫。", "example_meaning_en": "Please sweep."},
        "N4_647": {"example_sentence": "はこ（箱）に入れてください。", "example_reading": "はこにいれてください。", "example_meaning_cn": "请放进盒子里。", "example_meaning_en": "Please put it in the box."},
        "N4_648": {"example_sentence": "はこ（運）んでください。", "example_reading": "はこんでください。", "example_meaning_cn": "请搬运。", "example_meaning_en": "Please carry it."},
        "N4_649": {"example_sentence": "はさ（鋏）みで切ります。", "example_reading": "はさみできります。", "example_meaning_cn": "用剪刀剪。", "example_meaning_en": "I'll cut it with scissors."},
        "N4_650": {"example_sentence": "はじ（始）めてください。", "example_reading": "はじめてください。", "example_meaning_cn": "请开始。", "example_meaning_en": "Please start."},
        "N4_651": {"example_sentence": "はじ（始）まりましたね。", "example_reading": "はじまりましたね。", "example_meaning_cn": "开始了呢。", "example_meaning_en": "It has started, hasn't it?"},
        "N4_652": {"example_sentence": "はず（外）してください。", "example_reading": "はずしてください。", "example_meaning_cn": "请解开（或摘掉）。", "example_meaning_en": "Please remove/unfasten it."},
        "N4_653": {"example_sentence": "はず（恥）ずかしいですね。", "example_reading": "はずかしいですね。", "example_meaning_cn": "很不好意思呢。", "example_meaning_en": "It's embarrassing, isn't it?"},
        "N4_654": {"example_sentence": "はた（旗）を振ります。", "example_reading": "はたをふります。", "example_meaning_cn": "挥旗。", "example_meaning_en": "I'll wave the flag."},
        "N4_655": {"example_sentence": "はだ（肌）がきれいです。", "example_reading": "はだがきれいです。", "example_meaning_cn": "皮肤很好。", "example_meaning_en": "The skin is beautiful."},
        "N4_656": {"example_sentence": "はたら（働）いてください。", "example_reading": "はたらいてください。", "example_meaning_cn": "请工作。", "example_meaning_en": "Please work."},
        "N4_657": {"example_sentence": "はち（八）時に集まります。", "example_reading": "はちじにあつまります。", "example_meaning_cn": "八点集合。", "example_meaning_en": "Gather at eight."},
        "N4_658": {"example_sentence": "はつ（発）見しました！", "example_reading": "はっけんしました！", "example_meaning_cn": "发现了！", "example_meaning_en": "Discovered!"},
        "N4_659": {"example_sentence": "はな（鼻）が痛いです。", "example_reading": "はながいたいです。", "example_meaning_cn": "鼻子疼。", "example_meaning_en": "My nose hurts."},
        "N4_660": {"example_sentence": "はな（花）が咲いています。", "example_reading": "はながさいています。", "example_meaning_cn": "花开了。", "example_meaning_en": "Flowers are blooming."},
        "N4_661": {"example_sentence": "はな（話）してください。", "example_reading": "はなしてください。", "example_meaning_cn": "请说话。", "example_meaning_en": "Please speak."},
        "N4_662": {"example_sentence": "はな（離）してください。", "example_reading": "はなしてください。", "example_meaning_cn": "请松开（或保持距离）。", "example_meaning_en": "Please let go/keep a distance."},
        "N4_663": {"example_sentence": "はな（放）してください。", "example_reading": "はなしてください。", "example_meaning_cn": "请释放。", "example_meaning_en": "Please release."},
        "N4_664": {"example_sentence": "はな（離）れてください。", "example_reading": "はなれてください。", "example_meaning_cn": "请离开一点。", "example_meaning_en": "Please move away."},
        "N4_665": {"example_sentence": "はな（鼻）水が出ます。", "example_reading": "はなみずがでます。", "example_meaning_cn": "流鼻涕。", "example_meaning_en": "I have a runny nose."},
        "N4_666": {"example_sentence": "はは（母）は料理が上手です。", "example_reading": "はははりょうりがじょうずです。", "example_meaning_cn": "我母亲擅长做菜。", "example_meaning_en": "My mother is good at cooking."},
        "N4_667": {"example_sentence": "は（早）く来てください。", "example_reading": "はやくきてください。", "example_meaning_cn": "请早点来。", "example_meaning_en": "Please come early."},
        "N4_668": {"example_sentence": "はら（払）ってください。", "example_reading": "はらってください。", "example_meaning_cn": "请付钱。", "example_meaning_en": "Please pay."},
        "N4_669": {"example_sentence": "は（晴）れましたね。", "example_reading": "はれましたね。", "example_meaning_cn": "天晴了呢。", "example_meaning_en": "It cleared up, didn't it?"},
        "N4_670": {"example_sentence": "は（貼）ってください。", "example_reading": "はってください。", "example_meaning_cn": "请粘贴。", "example_meaning_en": "Please stick/paste it."},
        "N4_671": {"example_sentence": "は（張）ってください。", "example_reading": "はってください。", "example_meaning_cn": "请张开（或拉紧）。", "example_meaning_en": "Please spread/stretch it."},
        "N4_672": {"example_sentence": "ばん（番）組を見ています。", "example_reading": "ばんぐみをみています。", "example_meaning_cn": "正在看节目。", "example_meaning_en": "I'm watching a program."},
        "N4_673": {"example_sentence": "はん（反対）対ですか。", "example_reading": "はんたいですか。", "example_meaning_cn": "反对吗？", "example_meaning_en": "Are you against it?"},
        "N4_674": {"example_sentence": "はん（飯）を食べましょう。", "example_reading": "はんをたべましょう。", "example_meaning_cn": "吃饭吧。", "example_meaning_en": "Let's eat rice/meal."},
        "N4_675": {"example_sentence": "はん（半分）分に分けてください。", "example_reading": "はんぶんにわけてください。", "example_meaning_cn": "请分成两半。", "example_meaning_en": "Please divide it in half."},
        "N4_676": {"example_sentence": "ひ（日）が沈みます。", "example_reading": "ひがしずみます。", "example_meaning_cn": "太阳落山了。", "example_meaning_en": "The sun is setting."},
        "N4_677": {"example_sentence": "ひ（火）を消してください。", "example_reading": "ひをけしてください。", "example_meaning_cn": "请熄火。", "example_meaning_en": "Please put out the fire."},
        "N4_678": {"example_sentence": "ピアノ（ぴあの）を弾きます。", "example_reading": "ピアノをひきます。", "example_meaning_cn": "弹钢琴。", "example_meaning_en": "I'll play the piano."},
        "N4_679": {"example_sentence": "ひ（冷）やしてください。", "example_reading": "ひやしてください。", "example_meaning_cn": "请冷藏（或弄冷）。", "example_meaning_en": "Please cool it down."},
        "N4_680": {"example_sentence": "ひ（光）っていますね。", "example_reading": "ひかっていますね。", "example_meaning_cn": "正在发光呢。", "example_meaning_en": "It's shining, isn't it?"},
        "N4_681": {"example_sentence": "ひ（引）いてください。", "example_reading": "ひいてください。", "example_meaning_cn": "请拉（或查字典）。", "example_meaning_en": "Please pull (or look up)."},
        "N4_682": {"example_sentence": "ひ（弾）いてください。", "example_reading": "ひいてください。", "example_meaning_cn": "请演奏（琴）。", "example_meaning_en": "Please play (a string instrument)."},
        "N4_683": {"example_sentence": "ひく（低）いですね。 ", "example_reading": "ひくいですね。", "example_meaning_cn": "挺矮的呢。", "example_meaning_en": "It's low/short, isn't it?"},
        "N4_684": {"example_sentence": "ひこうき（飛行機）に乗ります。", "example_reading": "ひこうきにのります。", "example_meaning_cn": "坐飞机。", "example_meaning_en": "I'll take the plane."},
        "N4_685": {"example_sentence": "ひざ（膝）が痛いです。", "example_reading": "ひざがいたいです。", "example_meaning_cn": "膝盖疼。", "example_meaning_en": "My knee hurts."},
        "N4_686": {"example_sentence": "ひだり（左）を見てください。", "example_reading": "ひだりをみてください。", "example_meaning_cn": "请看左边。", "example_meaning_en": "Please look to the left."},
        "N4_687": {"example_sentence": "びっくり（びっくり）しました。", "example_reading": "びっくりしました。", "example_meaning_cn": "吓了一跳。", "example_meaning_en": "I was startled."},
        "N4_688": {"example_sentence": "ひつよう（必要）なものがあります。", "example_reading": "ひつようなものがあります。", "example_meaning_cn": "有需要的东西。", "example_meaning_en": "There's something I need."},
        "N4_689": {"example_sentence": "ひ（一）人（り）で来ました。", "example_reading": "ひとりできました。", "example_meaning_cn": "一个人来的。", "example_meaning_en": "I came alone."},
        "N4_690": {"example_sentence": "ひま（暇）ですか。 ", "example_reading": "ひまですか。", "example_meaning_cn": "有空吗？", "example_meaning_en": "Are you free?"},
        "N4_691": {"example_sentence": "ひ（百）円玉をください。", "example_reading": "ひゃくえんだまをください。", "example_meaning_cn": "请给我一百日元硬币。", "example_meaning_en": "Please give me a 100-yen coin."},
        "N4_692": {"example_sentence": "びょう（病院）院へ行きます。", "example_reading": "びょういんへいきます。", "example_meaning_cn": "去医院。", "example_meaning_en": "I'm going to the hospital."},
        "N4_693": {"example_sentence": "びょう（病気）気になりました。", "example_reading": "びょうきになりました。", "example_meaning_cn": "生病了。", "example_meaning_en": "I got sick."},
        "N4_694": {"example_sentence": "ひ（昼）休みです。", "example_reading": "ひるやすみです。", "example_meaning_cn": "午休时间。", "example_meaning_en": "It's lunch break."},
        "N4_695": {"example_sentence": "ひろ（広）いですね。 ", "example_reading": "ひろいですね。", "example_meaning_cn": "真够宽敞（或大）的呢。", "example_meaning_en": "It's wide/spacious, isn't it?"},
        "N4_696": {"example_sentence": "ひろ（拾）ってください。", "example_reading": "ひろってください。", "example_meaning_cn": "请捡起来。", "example_meaning_en": "Please pick it up."},
        "N4_697": {"example_sentence": "ふ（吹）いてください。", "example_reading": "ふいてください。", "example_meaning_cn": "请吹一下（或擦一下）。", "example_meaning_en": "Please blow (or wipe)."},
        "N4_698": {"example_sentence": "ぶ（部）屋に入ってください。", "example_reading": "へやにはいってください。", "example_meaning_cn": "请进屋。", "example_meaning_en": "Please enter the room."},
        "N4_699": {"example_sentence": "ふ（増）えてきました。", "example_reading": "ふえてきました。", "example_meaning_cn": "增加了。", "example_meaning_en": "It has increased."},
        "N4_700": {"example_sentence": "ふ（深）いですね。 ", "example_reading": "ふかいですね。", "example_meaning_cn": "挺深的呢。", "example_meaning_en": "It's deep, isn't it?"},
        "N4_701": {"example_sentence": "ふく（服）を着てください。", "example_reading": "ふくをきてください。", "example_meaning_cn": "请穿衣服。", "example_meaning_en": "Please put on clothes."},
        "N4_702": {"example_sentence": "ふく（複）習しましょう。", "example_reading": "ふくしゅうしましょう。", "example_meaning_cn": "复习吧。", "example_meaning_en": "Let's review."},
        "N4_703": {"example_sentence": "ぶた（豚）肉を食べましょう。", "example_reading": "ぶたにくをたべましょう。", "example_meaning_cn": "吃猪肉吧。", "example_meaning_en": "Let's eat pork."},
        "N4_704": {"example_sentence": "ふ（二）日（か）目に会いましょう。", "example_reading": "ふつかにあいましょう。", "example_meaning_cn": "第二天见吧（或二号见吧）。", "example_meaning_en": "Let's meet on the 2nd (of the month)."},
        "N4_705": {"example_sentence": "ぶつ（物）理学を学びます。", "example_reading": "ぶつりがくをまなびます。", "example_meaning_cn": "学习物理学。", "example_meaning_en": "I study physics."},
        "N4_706": {"example_sentence": "ふね（船）に乗ります。", "example_reading": "ふねにのります。", "example_meaning_cn": "坐船。", "example_meaning_en": "I'll get on a boat."},
        "N4_707": {"example_sentence": "ふ（踏）んでしまいました。", "example_reading": "ふんでしまいました。", "example_meaning_cn": "踩到了。", "example_meaning_en": "I stepped on it."},
        "N4_708": {"example_sentence": "ふり（降り）始めました。", "example_reading": "ふりはじめました。", "example_meaning_cn": "开始下（雨/雪）了。", "example_meaning_en": "It started raining/snowing."},
        "N4_709": {"example_sentence": "ふ（降）ってください。 ", "example_reading": "ふってください。", "example_meaning_cn": "请下（雨）或请挥（手）。 ", "example_meaning_en": "Please rain/wave."},
        "N4_710": {"example_sentence": "プレゼント（ぷれぜんと）をあげます。", "example_reading": "プレゼントをあげます。", "example_meaning_cn": "送礼物。", "example_meaning_en": "I'll give a present."},
        "N4_711": {"example_sentence": "ふ（文化）化が違います。", "example_reading": "ぶんかがちがいます。", "example_meaning_cn": "文化不同。", "example_meaning_en": "The culture is different."},
        "N4_712": {"example_sentence": "ふん（文学）学が好きです。", "example_reading": "ぶんがくがすきです。", "example_meaning_cn": "喜欢文学。", "example_meaning_en": "I like literature."},
        "N4_713": {"example_sentence": "ぶん（文章）章を読んでください。", "example_reading": "ぶんしょうをよんでください。", "example_meaning_cn": "请读文章。", "example_meaning_en": "Please read the sentence/text."},
        "N4_714": {"example_sentence": "ふん（文法）法を学びます。", "example_reading": "ぶんぽうをまなびます。", "example_meaning_cn": "学习语法。", "example_meaning_en": "I study grammar."},
        "N4_715": {"example_sentence": "へ（部屋）屋を掃除してください。", "example_reading": "へやをそうじしてください。", "example_meaning_cn": "请打扫房间。", "example_meaning_en": "Please clean the room."},
        "N4_716": {"example_sentence": "へ（下手）手くそですね。", "example_reading": "へたくそですね。", "example_meaning_cn": "真够差劲的呢（太笨了）。", "example_meaning_en": "You're really bad at it, aren't you?"},
        "N4_717": {"example_sentence": "べ（勉強）勉強しましょう。", "example_reading": "べんきょうしましょう。", "example_meaning_cn": "学习吧。", "example_meaning_en": "Let's study."},
        "N4_718": {"example_sentence": "べん（便利）利ですね。", "example_reading": "べんりですね。", "example_meaning_cn": "挺方便的呢。", "example_meaning_en": "It's convenient, isn't it?"},
        "N4_719": {"example_sentence": "ほ（方）向を教えてください。", "example_reading": "ほうこうをおしえてください。", "example_meaning_cn": "请告诉方向。", "example_meaning_en": "Please tell me the direction."},
        "N4_720": {"example_sentence": "ぼう（帽子）子を被ります。", "example_reading": "ぼうしをかぶります。", "example_meaning_cn": "戴帽子。", "example_meaning_en": "I'll put on a hat."},
        "N4_721": {"example_sentence": "ほう（報道）道されました。", "example_reading": "ほうどうされました。", "example_meaning_cn": "被报道了。", "example_meaning_en": "It was reported."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N4_721. N4 level enrichment COMPLETE.")

if __name__ == "__main__":
    main()
