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
        "N2_301": {"example_sentence": "（（降）お）り（（曲）ま）ってください。", "example_reading": "おりまがってください。", "example_meaning_cn": "请下（楼或车）后转弯。", "example_meaning_en": "Please get off and turn."},
        "N2_302": {"example_sentence": "（（愚）おろ）かな（な）こと（こと）を（を）し（し）まし（し）た。", "example_reading": "おろかなことをしました。", "example_meaning_cn": "做了愚蠢的事情。", "example_meaning_en": "I did something foolish."},
        "N2_303": {"example_sentence": "（（疎）おろそ）か（か）に（に）し（し）ないで（で）ください。", "example_reading": "おろそかにしないでください。", "example_meaning_cn": "请不要疏忽（或马虎）。", "example_meaning_en": "Please don't neglect/ignore it."},
        "N2_304": {"example_sentence": "（（卸）おろ）し（し）売り（うり）をし（し）て（て）います。", "example_reading": "おろしうりをしています。", "example_meaning_cn": "正在搞批发。", "example_meaning_en": "I'm doing wholesale."},
        "N2_305": {"example_sentence": "おん（（恩）おん）を（を）返し（かえし）ましょう。", "example_reading": "おんをかえしましょう。", "example_meaning_cn": "报恩吧。", "example_meaning_en": "Let's repay the kindness/debt of gratitude."},
        "N2_306": {"example_sentence": "おん（（音）おん）き（き）ょう（ょう）が（が）いい（いい）ですね。", "example_reading": "おんきょうがいいですね。", "example_meaning_cn": "音响（效果）真好呢。", "example_meaning_en": "The acoustics are good, aren't they?"},
        "N2_307": {"example_sentence": "おん（（温）おん）け（け）い（い）を（を）受け（うけ）て（て）います。", "example_reading": "おんけいをうけています。", "example_meaning_cn": "受到了恩惠（惠及）。", "example_meaning_en": "I'm receiving the benefits/grace."},
        "N2_308": {"example_sentence": "おん（（温）おん）し（し）つ（つ）で（で）育て（そだて）まし（し）た。", "example_reading": "おんしつでそだてました。", "example_meaning_cn": "在温室里培育的。", "example_meaning_en": "Grown in a greenhouse."},
        "N2_309": {"example_sentence": "おん（（音）おん）せ（せ）い（い）が（が）聞こえ（きこえ）ません。", "example_reading": "おんせいがきこえません。", "example_meaning_cn": "听不到声音（音频）。", "example_meaning_en": "I can't hear the voice/audio."},
        "N2_310": {"example_sentence": "おん（（温）おん）せん（せん）に（に）入り（はいり）ましょう。", "example_reading": "おんせんにはいりましょう。", "example_meaning_cn": "泡温泉吧。", "example_meaning_en": "Let's go into the hot spring."},
        "N2_311": {"example_sentence": "おん（（温）おん）たい（たい）の（の）気候（きこう）です。", "example_reading": "おんたいのきこうです。", "example_meaning_cn": "温带气候。", "example_meaning_en": "It's a temperate climate."},
        "N2_312": {"example_sentence": "おん（（御）おん）ち（ち）な（な）ん（ん）ですか。", "example_reading": "おんちなんですか。", "example_meaning_cn": "是音痴（五音不全）吗？", "example_meaning_en": "Are you tone-deaf?"},
        "N2_313": {"example_sentence": "おん（（温）おん）ど（ど）を（を）上げ（あげ）て（て）ください。", "example_reading": "おんどをあげてください。", "example_meaning_cn": "请调高温度。", "example_meaning_en": "Please raise the temperature."},
        "N2_314": {"example_sentence": "おん（（女）おんな）の（の）人（ひと）は（は）あちら（あちら）です。", "example_reading": "おんなのひとわあちらです。", "example_meaning_cn": "女性在那边。", "example_meaning_en": "The women are over there."},
        "N2_315": {"example_sentence": "（（蚊）か）に（に）刺さ（さ）れ（れ）まし（し）た。", "example_reading": "かにさされました。", "example_meaning_cn": "被蚊子叮了。", "example_meaning_en": "I was bitten by a mosquito."},
        "N2_316": {"example_sentence": "か（（可）か）と（と）し（し）て（て）ください。", "example_reading": "かとしてください。", "example_meaning_cn": "请视为可以（通过）。", "example_meaning_en": "Please consider it acceptable/possible."},
        "N2_317": {"example_sentence": "（（課）か）の（の）人（ひと）に（に）聞い（きい）て（て）ください。", "example_reading": "かのひとにきいてください。", "example_meaning_cn": "请问那个科（部门）的人。", "example_meaning_en": "Please ask someone in that department/section."},
        "N2_318": {"example_sentence": "（（何）か）い（い）を（を）数え（かぞえ）て（て）ください。", "example_reading": "かいをかぞえてください。", "example_meaning_cn": "请数一下回数（次数）。", "example_meaning_en": "Please count the times/rounds."},
        "N2_319": {"example_sentence": "（（害）がい）は（は）あり（あり）ません。", "example_reading": "がいわありません。", "example_meaning_cn": "没有害处。", "example_meaning_en": "There is no harm."},
        "N2_320": {"example_sentence": "がい（（外）がい）か（か）を（を）両替（りょうがえ）し（し）ます。", "example_reading": "がいかをりょうがえします。", "example_meaning_cn": "兑换外币。", "example_meaning_en": "Exchanging foreign currency."},
        "N2_321": {"example_sentence": "がい（（海）がい）き（き）ょう（ょう）を（を）調べ（しらべ）て（て）ください。", "example_reading": "がいきょうをしらべてください。", "example_meaning_cn": "请查询概况。", "example_meaning_en": "Please check the general situation/overview."},
        "N2_322": {"example_sentence": "がい（（外）がい）こ（こ）く（く）へ（へ）行き（いき）たい（たい）です。", "example_reading": "がいこくへいきたいです。", "example_meaning_cn": "想去外国。", "example_meaning_en": "I want to go to a foreign country."},
        "N2_323": {"example_sentence": "がい（（外）がい）し（し）ゅ（ゅ）つ（つ）し（し）て（て）い（い）ます。", "example_reading": "がいしゅつしています。", "example_meaning_cn": "正在外出。", "example_meaning_en": "I'm out/away."},
        "N2_324": {"example_sentence": "がい（（概）がい）せ（せ）つ（つ）を（を）話し（はなし）て（て）ください。", "example_reading": "がいせつをななしてください。", "example_meaning_cn": "请说一下概论。", "example_meaning_en": "Please give an overview/outline."},
        "N2_325": {"example_sentence": "がい（（外）がい）そう（そう）が（が）綺麗（きれい）ですね。", "example_reading": "がいそうがきれいですね。", "example_meaning_cn": "外装真漂亮呢。", "example_meaning_en": "The exterior is beautiful, isn't it?"},
        "N2_326": {"example_sentence": "がい（（該）がい）とう（とう）し（し）て（て）います。", "example_reading": "がいとうしています。", "example_meaning_cn": "符合项（该当）。", "example_meaning_en": "It falls under/corresponds to it."},
        "N2_327": {"example_sentence": "がい（（街）がい）とう（とう）で（で）演説（えんぜつ）し（し）ます。", "example_reading": "がいとうでえんぜつします。", "example_meaning_cn": "在街头演说。", "example_meaning_en": "Giving a speech on the street."},
        "N2_328": {"example_sentence": "がい（（外）がい）らい（らい）語（ご）を（を）使い（つかい）ます。", "example_reading": "がいらいごをつかいます。", "example_meaning_cn": "使用外来语。", "example_meaning_en": "Using loanwords."},
        "N2_329": {"example_sentence": "がい（（概）がい）ろ（ろ）ん（ん）を（を）読み（よみ）まし（し）た。", "example_reading": "がいろんをよみました。", "example_meaning_cn": "读了概论。", "example_meaning_en": "I read the introduction/outline."},
        "N2_330": {"example_sentence": "（（飼）か）って（て）ください。", "example_reading": "かってください。", "example_meaning_cn": "请饲养。", "example_meaning_en": "Please raise/keep it as a pet."},
        "N2_331": {"example_sentence": "（（返）かえ）して（て）ください。", "example_reading": "かえしてください。", "example_meaning_cn": "请还给我。", "example_meaning_en": "Please return it."},
        "N2_332": {"example_sentence": "（（代）か）え（え）て（て）ください。", "example_reading": "かえてください。", "example_meaning_cn": "请更换（或代替）。", "example_meaning_en": "Please replace/substitute it."},
        "N2_333": {"example_sentence": "（（省）かえり）み（み）て（て）ください。", "example_reading": "かえりみてください。", "example_meaning_cn": "请反省（回首）。", "example_meaning_en": "Please look back/reflect on it."},
        "N2_334": {"example_sentence": "（（顧）かえり）み（み）て（て）ください。", "example_reading": "かえりみてください。", "example_meaning_cn": "请顾及（或照顾）。", "example_meaning_en": "Please take into account/look back."},
        "N2_335": {"example_sentence": "（（変）か）え（え）て（て）ください。", "example_reading": "かえてください。", "example_meaning_cn": "请改变。", "example_meaning_en": "Please change it."},
        "N2_336": {"example_sentence": "（（掲）かか）げて（て）ください。", "example_reading": "かかげてください。", "example_meaning_cn": "请高举（或悬挂）。", "example_meaning_en": "Please hold high/hoist it."},
        "N2_337": {"example_sentence": "（（踵）かかと）を（を）揃え（そろえ）て（て）ください。", "example_reading": "かかとをそろえてください。", "example_meaning_cn": "请并拢脚后跟。", "example_meaning_en": "Please put your heels together."},
        "N2_338": {"example_sentence": "（（係）かか）り（り）の（の）人（ひと）に（に）聞い（きい）て（て）ください。", "example_reading": "かかりのひとにきいてください。", "example_meaning_cn": "请问负责人。", "example_meaning_en": "Please ask the person in charge."},
        "N2_339": {"example_sentence": "（（拘）かか）わ（わ）ら（ら）ず（ず）やって（て）ください。", "example_reading": "かかわらずやってください。", "example_meaning_cn": "不管怎样请做下去。", "example_meaning_en": "Please do it regardless."},
        "N2_340": {"example_sentence": "（（関）かか）わ（わ）ら（ら）ない（ない）で（で）ください。", "example_reading": "かかわらないでください。", "example_meaning_cn": "请不要扯上关系（干预）。", "example_meaning_en": "Please don't get involved."},
        "N2_341": {"example_sentence": "（（書）か）き（き）こ（こ）み（み）を（を）し（し）て（て）ください。", "example_reading": "かきこみをしてください。", "example_meaning_cn": "请留言（或写入）。", "example_meaning_en": "Please post/write a comment."},
        "N2_342": {"example_sentence": "（（書）か）き（き）とり（とり）を（を）し（し）ます。", "example_reading": "かきとりをします。", "example_meaning_cn": "做听写。", "example_meaning_en": "Doing dictation."},
        "N2_343": {"example_sentence": "（（書）か）き（き）ね（ね）を（を）越え（こえ）て（て）ください。", "example_reading": "かきねをこえてください。", "example_meaning_cn": "跨过篱笆（或隔阂）。", "example_meaning_en": "Cross the fence/barrier."},
        "N2_344": {"example_sentence": "（（欠）か）き（き）ま（ま）わ（わ）さ（さ）ないで（で）ください。", "example_reading": "かきまわさないでください。", "example_meaning_cn": "请不要搅乱（或搅拌）。", "example_meaning_en": "Please don't stir/mess it up."},
        "N2_345": {"example_sentence": "（（欠）か）き（き）混ぜ（まぜ）て（て）ください。", "example_reading": "かきまぜてください。", "example_meaning_cn": "请搅拌均匀。", "example_meaning_en": "Please stir/mix it."},
        "N2_346": {"example_sentence": "（（書）か）き（き）も（も）の（の）を（を）し（し）て（て）います。", "example_reading": "かきものをしています。", "example_meaning_cn": "正在写字。", "example_meaning_en": "I'm doing some writing."},
        "N2_347": {"example_sentence": "（（欠）か）く（く）べ（べ）から（ら）ざ（ざ）る（る）存在（そんざい）です。", "example_reading": "かくべからざるそんざいです。", "example_meaning_cn": "不可或缺的存在。", "example_meaning_en": "An indispensable existence."},
        "N2_348": {"example_sentence": "かく（（角）かく）を（を）曲がっ（まがっ）て（て）ください。", "example_reading": "かどをまがってください。", "example_meaning_cn": "请拐角（弯）。", "example_meaning_en": "Please turn the corner."},
        "N2_349": {"example_sentence": "（（額）がく）を（を）飾っ（かざっ）て（て）ください。", "example_reading": "がくをかざってください。", "example_meaning_cn": "请装饰画框（额）。", "example_meaning_en": "Please decorate with a frame."},
        "N2_350": {"example_sentence": "（（格）かく）が（が）違い（ちがい）ますね。", "example_reading": "かくがちがいますね。", "example_meaning_cn": "档次（格调）不同呢。", "example_meaning_en": "It's in a different class, isn't it?"},
        "N2_351": {"example_sentence": "（（核）かく）を（を）守り（まもり）ましょう。", "example_reading": "かくをまもりましょう。", "example_meaning_cn": "守护核心（或核能安全）吧。", "example_meaning_en": "Let's protect the core."},
        "N2_352": {"example_sentence": "（（確）かく）しん（しん）を（を）突い（つい）て（て）ください。", "example_reading": "かくしんをついてください。", "example_meaning_cn": "击中核心（要点）。", "example_meaning_en": "Please hit the core/point."},
        "N2_353": {"example_sentence": "（（確）かく）じ（じ）つ（つ）に（に）やっ（やっ）て（て）ください。", "example_reading": "かくじつにやってください。", "example_meaning_cn": "请确确实实地做。", "example_meaning_en": "Please do it for sure."},
        "N2_354": {"example_sentence": "（（学）がく）し（し）ゃ（ゃ）になり（なり）たい（たい）です。", "example_reading": "がくしゃになりたいです。", "example_meaning_cn": "想成为学者。", "example_meaning_en": "I want to become a scholar."},
        "N2_355": {"example_sentence": "（（学）がく）し（し）ゅう（ゅう）し（し）て（て）ください。", "example_reading": "がくしゅうしてください。", "example_meaning_cn": "请学习。", "example_meaning_en": "Please learn/study."},
        "N2_356": {"example_sentence": "（（格）かく）し（し）ゅ（ゅ）の（の）イベント（いべんと）があり（あり）ます。", "example_reading": "かくしゅのいべんとがあります。", "example_meaning_cn": "有各种各样的活动。", "example_meaning_en": "There are various types of events."},
        "N2_357": {"example_sentence": "（（格）かく）じ（じ）に（に）任せ（まかせ）ます。", "example_reading": "かくじにまかせます。", "example_meaning_cn": "由各自负责。", "example_meaning_en": "I'll leave it to each individual."},
        "N2_358": {"example_sentence": "（（拡）かく）じ（じ）ゅう（ゅう）し（し）て（て）ください。", "example_reading": "かくじゅうしてください。", "example_meaning_cn": "请扩充。", "example_meaning_en": "Please expand/augment it."},
        "N2_359": {"example_sentence": "（（客）かく）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "かくしんしてください。", "example_meaning_cn": "请格新（改革）。", "example_meaning_en": "Please innovate."},
        "N2_360": {"example_sentence": "（（各）かく）ち（ち）を（を）旅（たび）し（し）ます。", "example_reading": "かくちをたびします。", "example_meaning_cn": "周游各地。", "example_meaning_en": "I'll travel to various places."},
        "N2_361": {"example_sentence": "（（拡）かく）だい（だい）し（し）て（て）ください。", "example_reading": "かくだいしてください。", "example_meaning_cn": "请放大（扩张）。", "example_meaning_en": "Please enlarge/expand it."},
        "N2_362": {"example_sentence": "（（確）かく）に（に）ん（ん）し（し）て（て）ください。", "example_reading": "かくにんしてください。", "example_meaning_cn": "请确认。", "example_meaning_en": "Please confirm."},
        "N2_363": {"example_sentence": "（（学）がく）ふ（ふ）を（を）読ん（よん）で（て）ください。", "example_reading": "がくふをよんでください。", "example_meaning_cn": "请看乐谱。", "example_meaning_en": "Please read the musical score."},
        "N2_364": {"example_sentence": "（（確）かく）ほ（ほ）し（し）て（て）ください。", "example_reading": "かくほしてください。", "example_meaning_cn": "请确保。", "example_meaning_en": "Please secure/guarantee it."},
        "N2_365": {"example_sentence": "（（格）かく）め（め）い（い）を（を）起こし（おこし）ましょう。", "example_reading": "かくめいをおこしましょう。", "example_meaning_cn": "发起革命吧。", "example_meaning_en": "Let's start a revolution."},
        "N2_366": {"example_sentence": "（（確）かく）り（り）つ（つ）し（し）て（て）ください。", "example_reading": "かくりつしてください。", "example_meaning_cn": "请确立。", "example_meaning_en": "Please establish it."},
        "N2_367": {"example_sentence": "（（学）がく）り（り）ょ（ょ）く（く）を（を）高め（たかめ）て（て）ください。", "example_reading": "がくりょくをたかめてください。", "example_meaning_cn": "请提高学力。", "example_meaning_en": "Please improve your academic ability."},
        "N2_368": {"example_sentence": "（（欠）か）け（け）て（て）いますか。", "example_reading": "かけていますか。", "example_meaning_cn": "有缺口（或不够）吗？", "example_meaning_en": "Is something lacking/chipped?"},
        "N2_369": {"example_sentence": "（（賭）か）け（け）て（て）み（み）ましょう。", "example_reading": "かけてみましょう。", "example_meaning_cn": "赌一把吧。", "example_meaning_en": "Let's bet/risk it."},
        "N2_370": {"example_sentence": "（（懸）か）け（け）て（て）ください。", "example_reading": "かけてください。", "example_meaning_cn": "请悬挂（或打电话）。", "example_meaning_en": "Please hang/call it."},
        "N2_371": {"example_sentence": "（（駆）か）け（け）あ（あ）が（が）って（て）ください。", "example_reading": "かけあがってください。", "example_meaning_cn": "请跑上去。", "example_meaning_en": "Please run up."},
        "N2_372": {"example_sentence": "（（欠）か）け（け）が（が）え（え）の（の）ない（ない）存在（そんざい）。", "example_reading": "かけがえのないそんざい。", "example_meaning_cn": "无可替代的存在。", "example_meaning_en": "An irreplaceable existence."},
        "N2_373": {"example_sentence": "（（駆）か）け（け）っこ（っこ）し（し）ましょう。", "example_reading": "かけっこしましょう。", "example_meaning_cn": "赛跑吧。", "example_meaning_en": "Let's have a race."},
        "N2_374": {"example_sentence": "（（可）か）け（け）つ（つ）され（され）まし（し）た。", "example_reading": "かけつされました。", "example_meaning_cn": "通过（决议）了。", "example_meaning_en": "It was passed/approved."},
        "N2_375": {"example_sentence": "（（加）か）げ（げ）ん（ん）し（し）て（て）ください。", "example_reading": "かげんしてください。", "example_meaning_cn": "请斟酌（或加减）。", "example_meaning_en": "Please adjust/moderate it."},
        "N2_376": {"example_sentence": "（（過）か）こ（こ）を（を）振り返ら（ふりかえら）ないで（で）ください。", "example_reading": "かこをふりかえらないでください。", "example_meaning_cn": "请不要回首过去。", "example_meaning_en": "Please don't look back at the past."},
        "N2_377": {"example_sentence": "（（籠）かご）に（に）入れ（いれ）て（て）ください。", "example_reading": "かごにいれてください。", "example_meaning_cn": "请放入篮子里。", "example_meaning_en": "Please put it in the basket."},
        "N2_378": {"example_sentence": "かこ（（火）かこ）を（を）囲み（かこみ）ましょう。", "example_reading": "かこをかこみましょう。", "example_meaning_cn": "围着火堆吧。", "example_meaning_en": "Let's gather around the fire."},
        "N2_379": {"example_sentence": "（（過）か）ご（ご）に（に）させ（させ）ないで（で）ください。", "example_reading": "かごにさせないでください。", "example_meaning_cn": "请不要让他（她）犯错。", "example_meaning_en": "Please don't let them make a mistake."},
        "N2_380": {"example_sentence": "（（重）かさ）ね（ね）て（て）ください。", "example_reading": "かさねてください。", "example_meaning_cn": "请叠加。", "example_meaning_en": "Please overlap/stack them."},
        "N2_381": {"example_sentence": "（（飾）かざ）り（り）を（を）し（し）て（て）ください。", "example_reading": "かざりをしてください。", "example_meaning_cn": "请装饰。", "example_meaning_en": "Please decorate it."},
        "N2_382": {"example_sentence": "（（火）か）ざ（ざ）ん（ん）が（が）爆ぜ（はぜ）まし（し）た。", "example_reading": "かざんがはぜました。", "example_meaning_cn": "火山爆发了。", "example_meaning_en": "The volcano erupted."},
        "N2_383": {"example_sentence": "（（貸）か）し（し）て（て）ください。", "example_reading": "かしてください。", "example_meaning_cn": "请借给我。", "example_meaning_en": "Please lend it to me."},
        "N2_384": {"example_sentence": "（（可）か）し（し）し（し）て（て）ください。", "example_reading": "かししてください。", "example_meaning_cn": "请写下来（可视化）。", "example_meaning_en": "Please visualize/write it down."},
        "N2_385": {"example_sentence": "（（過）か）し（し）つ（つ）は（は）あり（あり）ません。", "example_reading": "かしつわありません。", "example_meaning_cn": "没有过失。", "example_meaning_en": "There was no negligence/fault."},
        "N2_386": {"example_sentence": "（（歌）か）しゅ（しゅ）になり（なり）たい（たい）です。", "example_reading": "かしゅになりたいです。", "example_meaning_cn": "想成为歌手。", "example_meaning_en": "I want to become a singer."},
        "N2_387": {"example_sentence": "（（箇）か）じ（じ）ょ（ょ）う（う）書き（がき）に（に）し（し）て（て）ください。", "example_reading": "かじょうがきにしてください。", "example_meaning_cn": "请列举（分条写）。", "example_meaning_en": "Please list them item by item."},
        "N2_388": {"example_sentence": "（（過）か）じ（じ）ょ（ょ）う（う）摂取（せっしゅ）し（し）ないで（で）ください。", "example_reading": "かじょうせっしゅしないでください。", "example_meaning_cn": "请不要过量摄取。", "example_meaning_en": "Please don't over-consume it."},
        "N2_389": {"example_sentence": "かす（（微）かす）かな（な）声（こえ）が（が）聞こえ（きこえ）ます。", "example_reading": "かすかなこえがきこえます。", "example_meaning_cn": "听到微弱的声音。", "example_meaning_en": "I hear a faint voice."},
        "N2_390": {"example_sentence": "（（霞）かす）ん（ん）で（て）います。", "example_reading": "かすんでいます。", "example_meaning_cn": "朦朦胧胧（有霞光）的。", "example_meaning_en": "It's misty/hazy."},
        "N2_391": {"example_sentence": "（（擦）かす）り（り）傷（きず）です。", "example_reading": "かすりきずです。", "example_meaning_cn": "擦伤。", "example_meaning_en": "It's a scratch."},
        "N2_392": {"example_sentence": "（（火）か）せい（せい）に（に）行き（いき）たい（たい）です。", "example_reading": "かせいにいきたいです。", "example_meaning_cn": "想去火星。", "example_meaning_en": "I want to go to Mars."},
        "N2_393": {"example_sentence": "（（稼）かせ）いで（て）ください。", "example_reading": "かせいでください。", "example_meaning_cn": "请赚钱（或赚取）。", "example_meaning_en": "Please earn money."},
        "N2_394": {"example_sentence": "（（課）か）せ（せ）られ（られ）た（た）仕事（しごと）です。", "example_reading": "かせられたしごとです。", "example_meaning_cn": "被指派（课）的工作。", "example_meaning_en": "The task assigned to me."},
        "N2_395": {"example_sentence": "（（固）かた）めて（て）ください。", "example_reading": "かためてください。", "example_meaning_cn": "请固化（或加固）。", "example_meaning_en": "Please solidify/harden it."},
        "N2_396": {"example_sentence": "（（偏）かたよ）らないで（で）ください。", "example_reading": "かたよらないでください。", "example_meaning_cn": "请不要偏颇（或不偏食）。", "example_meaning_en": "Please don't be biased."},
        "N2_397": {"example_sentence": "（（語）かた）って（て）ください。", "example_reading": "かたってください。", "example_meaning_cn": "请讲述。", "example_meaning_en": "Please tell/narrate."},
        "N2_398": {"example_sentence": "（（担）かつ）いで（て）ください。", "example_reading": "かついでください。", "example_meaning_cn": "请扛着（或欺骗）。", "example_meaning_en": "Please shoulder/carry it."},
        "N2_399": {"example_sentence": "（（活）かつ）き（き）があり（あり）ますね。", "example_reading": "かっきがありますね。", "example_meaning_cn": "真有活力（活泼）呢。", "example_meaning_en": "How lively/animated it is."},
        "N2_400": {"example_sentence": "（（活）かく）し（し）て（て）ください。", "example_reading": "かくしてください。", "example_meaning_cn": "请隐藏（或掩饰）。", "example_meaning_en": "Please hide/conceal it."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_400.")

if __name__ == "__main__":
    main()
