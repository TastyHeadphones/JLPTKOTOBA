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
        "N1_201": {"example_sentence": "（（遺）い）た（た）い（い）を（を）安置（あんち）し（し）て（て）ください。", "example_reading": "いたいをあんちしてください。", "example_meaning_cn": "请安置遗体。", "example_meaning_en": "Please place the remains / corpse."},
        "N1_202": {"example_sentence": "（（至）いた）る（る）ところ（ところ）に（に）花（はな）が（が）咲い（さい）て（て）います。", "example_reading": "いたるところにはながさいています。", "example_meaning_cn": "到处（无所不在）都开着花。", "example_meaning_en": "Flowers are blooming everywhere."},
        "N1_203": {"example_sentence": "（（致）いた）し（し）か（か）た（た）あり（あり）ません。", "example_reading": "いたしかたありません。", "example_meaning_cn": "没办法（无可奈何）。", "example_meaning_en": "It can't be helped."},
        "N1_204": {"example_sentence": "（（意）い）た（た）ず（ず）ら（ら）し（し）ないで（で）ください。", "example_reading": "いたずらしないでください。", "example_meaning_cn": "请不要恶作剧（或徒然）。", "example_meaning_en": "Please don't play pranks / don't do it in vain."},
        "N1_205": {"example_sentence": "（（頂）いただ）き（き）を（を）極め（きわめ）ましょう。", "example_reading": "いただきをきわめましょう。", "example_meaning_cn": "登上顶峰吧。", "example_meaning_en": "Let's reach the summit."},
        "N1_206": {"example_sentence": "（（至）いた）る（る）まで（まで）待っ（まっ）て（て）ください。", "example_reading": "いたるまでまってください。", "example_meaning_cn": "请等他到（或达到）。", "example_meaning_en": "Please wait until it arrives/reaches."},
        "N1_207": {"example_sentence": "（（労）いたわ）っ（っ）て（て）ください。", "example_reading": "いたわってください。", "example_meaning_cn": "请慰劳（或体贴）。", "example_meaning_en": "Please be kind/show consideration."},
        "N1_208": {"example_sentence": "（（一）い）ち（ち）を（を）知っ（しっ）て（て）ください。", "example_reading": "いちをしってください。", "example_meaning_cn": "请知道其一（或位置）。", "example_meaning_en": "Please know one part/the position."},
        "N1_209": {"example_sentence": "（（一）い）ち（ち）が（が）い（い）に（に）は（は）言え（いえ）ません。", "example_reading": "いちがいにはいえません。", "example_meaning_cn": "不能一概而论。", "example_meaning_en": "I can't say for sure (categorically)."},
        "N1_210": {"example_sentence": "（（一）い）ち（ち）げ（げ）く（く）し（し）て（て）ください。", "example_reading": "いちげくしてください。", "example_meaning_cn": "请给出一击。", "example_meaning_en": "Please deliver a single blow."},
        "N1_211": {"example_sentence": "（（一）い）ち（ち）じ（じ）てき（てき）な（な）避難（ひなん）です。", "example_reading": "いちじてきなひなんです。", "example_meaning_cn": "一时的（暂时的）避难。", "example_meaning_en": "It's a temporary evacuation."},
        "N1_212": {"example_sentence": "（（一）い）ち（ち）じ（じ）ゅう（ゅう）を（を）話し（はなし）て（て）ください。", "example_reading": "いちじゅうをおなしてください。", "example_meaning_cn": "请说明始末（一重）。", "example_meaning_en": "Please explain the whole story."},
        "N1_213": {"example_sentence": "（（一）い）ち（ち）だ（だ）ん（ん）と（と）美しく（うつくしく）なり（なり）まし（し）た。", "example_reading": "いちだんとうつくしくなりました。", "example_meaning_cn": "更加（越发）美丽了。", "example_meaning_en": "It has become even more beautiful."},
        "N1_214": {"example_sentence": "（（一）い）ち（ち）ど（ど）に（に）来（き）ないで（で）ください。", "example_reading": "いちどにこないでください。", "example_meaning_cn": "请不要一下子（同时）都来。", "example_meaning_en": "Please don't all come at once."},
        "N1_215": {"example_sentence": "（（一）い）ち（ち）は（は）や（や）く（く）知らせ（しらせ）て（て）ください。", "example_reading": "いちはやくしらせてください。", "example_meaning_cn": "请第一时间通知我。", "example_meaning_en": "Please let me know as quickly as possible."},
        "N1_216": {"example_sentence": "（（一）い）ち（ち）め（め）ん（ん）に（に）雪（ゆき）が（が）積もっ（つもっ）て（て）います。", "example_reading": "いちめんにゆきがつもっています。", "example_meaning_cn": "满地（一面）都积了雪。", "example_meaning_en": "Snow is covering the entire surface."},
        "N1_217": {"example_sentence": "（（一）い）ち（ち）も（も）く（く）を（を）置き（おき）ます。", "example_reading": "いちもくをおきます。", "example_meaning_cn": "自愧不如（让出一筹）。", "example_meaning_en": "I take my hat off to them."},
        "N1_218": {"example_sentence": "（（一）い）ち（ち）よ（よ）う（う）に（に）並べ（ならべ）て（て）ください。", "example_reading": "いちようにならべてください。", "example_meaning_cn": "请整齐地（同样地）排列。", "example_meaning_en": "Please arrange them uniformly."},
        "N1_219": {"example_sentence": "（（一）い）ち（ち）り（り）つ（つ）に（に）決め（きめ）ないで（で）ください。", "example_reading": "いちりつにきめないでください。", "example_meaning_cn": "请不要一律确定。", "example_meaning_en": "Please don't decide it uniformly/indiscriminately."},
        "N1_220": {"example_sentence": "（（一）い）ち（ち）り（り）ん（ん）の（の）花（はな）を（を）飾り（かざり）ましょう。", "example_reading": "いちりんのはなをかざりましょう。", "example_meaning_cn": "装饰一朵花吧。", "example_meaning_en": "Let's decorate with a single flower."},
        "N1_221": {"example_sentence": "（（一）い）ち（ち）れ（れ）い（い）し（し）て（て）ください。", "example_reading": "いちれいしてください。", "example_meaning_cn": "请行个礼。", "example_meaning_en": "Please make a bow."},
        "N1_222": {"example_sentence": "（（著）いちじ）る（る）し（し）い（い）進歩（しんぽ）です。", "example_reading": "いちじるしいしんぽです。", "example_meaning_cn": "显著的进步。", "example_meaning_en": "It's a remarkable progress."},
        "N1_223": {"example_sentence": "（（一）い）っ（っ）か（か）を（を）支え（ささえ）ます。", "example_reading": "いっかをささえます。", "example_meaning_cn": "支撑一家（家庭）。", "example_meaning_en": "I support my family."},
        "N1_224": {"example_sentence": "（（一）い）っ（っ）か（か）つ（つ）し（し）て（て）ください。", "example_reading": "いっかつしてください。", "example_meaning_cn": "请一括（汇总）。", "example_meaning_en": "Please bundle/summarize it."},
        "N1_225": {"example_sentence": "（（一）い）っ（っ）き（き）に（に）飲み（のみ）ましょう。", "example_reading": "いっきにのみましょう。", "example_meaning_cn": "一口气全喝了吧。", "example_meaning_en": "Let's drink it all at once."},
        "N1_226": {"example_sentence": "（（一）い）っ（っ）き（き）ょ（ょ）に（に）解決（かいけつ）し（し）ましょう。", "example_reading": "いっきょにかいけつしましょう。", "example_meaning_cn": "一举解决吧。", "example_meaning_en": "Let's solve it at once."},
        "N1_227": {"example_sentence": "（（一）い）っ（っ）け（け）つ（つ）し（し）て（て）ください。", "example_reading": "いっけつしてください。", "example_meaning_cn": "请一决（决定）。", "example_meaning_en": "Please decide it finally."},
        "N1_228": {"example_sentence": "（（一）い）っ（っ）け（け）ん（ん）し（し）て（て）ください。", "example_reading": "いっけんしてください。", "example_meaning_cn": "请过目（看一眼）。", "example_meaning_en": "Please have a look/at a glance."},
        "N1_229": {"example_sentence": "（（一）い）っ（っ）さ（さ）い（い）話し（はなし）て（て）ください。", "example_reading": "いっさいおなしてください。", "example_meaning_cn": "请全部说完（一切）。", "example_meaning_en": "Please tell me everything."},
        "N1_230": {"example_sentence": "（（一）い）っ（っ）さ（さ）く（く）し（し）て（て）ください。", "example_reading": "いっさくしてください。", "example_meaning_cn": "请一作（创作）。", "example_meaning_en": "Please make one work/creation."},
        "N1_231": {"example_sentence": "（（一）い）っ（っ）し（し）ゅ（ゅ）ん（ん）の（の）出来事（できごと）でした。", "example_reading": "いっしゅんのできごとでした。", "example_meaning_cn": "这是瞬间发生的事。", "example_meaning_en": "It happened in an instant."},
        "N1_232": {"example_sentence": "（（一）い）っ（っ）し（し）ょ（ょ）に（に）頑張り（がんばり）ましょう。", "example_reading": "いっしょにがんばりましょう。", "example_meaning_cn": "一起努力吧。", "example_meaning_en": "Let's work hard together."},
        "N1_233": {"example_sentence": "（（一）い）っ（っ）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "いっしんしてください。", "example_meaning_cn": "请一心（或刷新）。", "example_meaning_en": "Please be wholehearted/renovate it."},
        "N1_234": {"example_sentence": "（（一）い）っ（っ）そ（そ）帰り（かえり）ましょうか。", "example_reading": "いっそかえりましょうか。", "example_meaning_cn": "索性（倒不如）回去吧。", "example_meaning_en": "Should we rather go home?"},
        "N1_235": {"example_sentence": "（（一）い）っ（っ）た（た）い（い）どう（どう）し（し）た（た）のです（です）か。", "example_reading": "いったいどうしたのですか。", "example_meaning_cn": "到底（究竟）怎么了呢？", "example_meaning_en": "What on earth happened?"},
        "N1_236": {"example_sentence": "（（一）い）っ（っ）た（た）ん（ん）休み（やすみ）ましょう。", "example_reading": "いったんやすみましょう。", "example_meaning_cn": "先（暂时）休息一下吧。", "example_meaning_en": "Let's take a temporary break."},
        "N1_237": {"example_sentence": "（（一）い）っ（っ）ち（ち）し（し）て（て）ください。", "example_reading": "いっちしてください。", "example_meaning_cn": "请一致（符合）。", "example_meaning_en": "Please agree/coincide."},
        "N1_238": {"example_sentence": "（（一）い）っ（っ）て（て）い（い）に（に）し（し）て（て）ください。", "example_reading": "いっていにしてください。", "example_meaning_cn": "请保持一定（固定）。", "example_meaning_en": "Please keep it constant."},
        "N1_239": {"example_sentence": "（（逸）いっ）て（て）ん（ん）し（し）て（て）ください。", "example_reading": "いってんしてください。", "example_meaning_cn": "请一转（转变）。", "example_meaning_en": "Please take a turn/change around."},
        "N1_240": {"example_sentence": "（（一）い）っ（っ）ぱ（ぱ）い（い）に（に）なり（なり）まし（し）た。", "example_reading": "いっぱいになりました。", "example_meaning_cn": "满了（充满了）。", "example_meaning_en": "It's full/packed."},
        "N1_241": {"example_sentence": "（（一）い）っ（っ）ぺ（へ）ん（ん）に（に）話し（はなし）て（て）ください。", "example_reading": "いっぺんにおなしてください。", "example_meaning_cn": "请一下子全说完。", "example_meaning_en": "Please tell me it all at once."},
        "N1_242": {"example_sentence": "（（一）い）っ（っ）ぽ（ぽ）う（う）てき（てき）な（な）話（はなし）です。", "example_reading": "いっぽうてきなはなしです。", "example_meaning_cn": "片面（单方面）的话。", "example_meaning_en": "It's a one-sided story."},
        "N1_243": {"example_sentence": "（（一）い）っ（っ）ぽ（ぽ）ん（ん）し（し）て（て）ください。", "example_reading": "いっぽんしてください。", "example_meaning_cn": "请一整（或一本/单纯）。", "example_meaning_en": "Please be single-minded/straightforward."},
        "N1_244": {"example_sentence": "（（何）いつ）も（も）ありがとうございます。", "example_reading": "いつもありがとうございます。", "example_meaning_cn": "一直（总是）谢谢你。", "example_meaning_en": "Thank you as always."},
        "N1_245": {"example_sentence": "（（何）いつ）か（か）また（また）会い（あい）ましょう。", "example_reading": "いつかまたあいましょう。", "example_meaning_cn": "哪天再见吧。", "example_meaning_en": "Let's meet again sometime."},
        "N1_246": {"example_sentence": "（（何）いつ）し（し）か（か）夜（よ）が（が）明け（あけ）まし（し）た。", "example_reading": "いつしかよがあけました。", "example_meaning_cn": "不知不觉中天亮了。", "example_meaning_en": "Day broke before I knew it."},
        "N1_247": {"example_sentence": "（（何）いつ）ま（ま）で（で）も（も）お（お）元気（げんき）で（で）。", "example_reading": "いつまでもおげんきで。", "example_meaning_cn": "祝你永远健康。", "example_meaning_en": "Stay healthy forever."},
        "N1_248": {"example_sentence": "（（何）いつ）も（も）の（の）場所（ばしょ）に（に）行き（いき）ましょう。", "example_reading": "いつものばしょにいきましょう。", "example_meaning_cn": "去老地方吧。", "example_meaning_en": "Let's go to the usual place."},
        "N1_249": {"example_sentence": "（（偽）いつわ）ら（ら）ない（ない）で（で）ください。", "example_reading": "いつわらないでください。", "example_meaning_cn": "请不要虚假（欺骗）。", "example_meaning_en": "Please don't lie/be false."},
        "N1_250": {"example_sentence": "（（営）いとな）ん（ん）で（て）ください。", "example_reading": "いとなんでください。", "example_meaning_cn": "请经营。", "example_meaning_en": "Please conduct/manage it."},
        "N1_251": {"example_sentence": "（（暇）いとま）を（を）告げ（つげ）て（て）ください。", "example_reading": "いとまをつげてください。", "example_meaning_cn": "请告辞（或退休）。", "example_meaning_en": "Please say goodbye/take your leave."},
        "N1_252": {"example_sentence": "（（暇）いとま）が（が）あり（あり）ません。", "example_reading": "いとまがありません。", "example_meaning_cn": "没有闲暇。", "example_meaning_en": "I have no leisure time."},
        "N1_253": {"example_sentence": "（（暇）いとま）ご（ご）い（い）し（し）て（て）ください。", "example_reading": "いとまごいしてください。", "example_meaning_cn": "请告别。", "example_meaning_en": "Please say farewell."},
        "N1_254": {"example_sentence": "（（異）い）な（な）る（る）意見（いけん）を（を）尊重（そんちょう）し（し）ましょう。", "example_reading": "いなるいけんをそんちょうしましょう。", "example_meaning_cn": "尊重不同的意见吧。", "example_meaning_en": "Let's respect differing opinions."},
        "N1_255": {"example_sentence": "（（言）い）な（な）い（い）で（で）ください。", "example_reading": "いないでください。", "example_meaning_cn": "请不要不在（或否认）。", "example_meaning_en": "Please don't be absent/don't deny."},
        "N1_256": {"example_sentence": "（（居）い）な（な）お（お）ら（ら）ないで（で）ください。", "example_reading": "いなおらないでください。", "example_meaning_cn": "请不要反咬一口（或改坐）。", "example_meaning_en": "Please don't turn on me / sit up straight."},
        "N1_257": {"example_sentence": "（（居）い）な（な）か（か）に（に）帰り（かえり）たい（たい）です。", "example_reading": "いなかにかえりたいです。", "example_meaning_cn": "想回乡下（田舍/居中）。", "example_meaning_en": "I want to go back to the countryside."},
        "N1_258": {"example_sentence": "（（往）い）な（な）さ（さ）ないで（で）ください。", "example_reading": "いなさないでください。", "example_meaning_cn": "请不要推诿（或闪开）。", "example_meaning_en": "Please don't dodge/deflect it."},
        "N1_259": {"example_sentence": "（（言）い）な（な）な（な）い（い）で（で）ください。", "example_reading": "いなななないでください。", "example_meaning_cn": "请不要嘶鸣（或推脱）。", "example_meaning_en": "Please don't neigh/refuse."},
        "N1_260": {"example_sentence": "（（居）い）な（な）ま（ま）せ（せ）て（て）ください。", "example_reading": "いなませてください。", "example_meaning_cn": "请在座（陪同）。", "example_meaning_en": "Please be present with me."},
        "N1_261": {"example_sentence": "（（否）いな）め（め）ませ（ませ）ん。", "example_reading": "いなめません。", "example_meaning_cn": "不容否认。", "example_meaning_en": "It cannot be denied."},
        "N1_262": {"example_sentence": "（（居）い）ね（ね）む（む）り（り）し（し）ないで（で）ください。", "example_reading": "いねむりしないでください。", "example_meaning_cn": "请不要打瞌睡。", "example_meaning_en": "Please don't nod off."},
        "N1_263": {"example_sentence": "（（威）い）は（は）く（く）し（し）ないで（で）ください。", "example_reading": "いはくしないでください。", "example_meaning_cn": "请不要威吓。", "example_meaning_en": "Please don't intimidate."},
        "N1_264": {"example_sentence": "（（威）い）ば（ば）ら（ら）ないで（で）ください。", "example_reading": "いばらないでください。", "example_meaning_cn": "请不要摆架子（自大）。", "example_meaning_en": "Please don't be haughty/boastful."},
        "N1_265": {"example_sentence": "（（違）い）は（は）ん（ん）し（し）ないで（で）ください。", "example_reading": "いはんしないでください。", "example_meaning_cn": "请不要违反。", "example_meaning_en": "Please don't violate/break it."},
        "N1_266": {"example_sentence": "（（威）い）ふ（ふ）う（う）に（に）打た（うた）れ（れ）まし（し）た。", "example_reading": "いふうにうたれました。", "example_meaning_cn": "被其威风（气派）所震撼。", "example_meaning_en": "I was struck by the majestic appearance."},
        "N1_267": {"example_sentence": "（（居）い）ま（ま）ど（ど）い（い）し（し）ないで（で）ください。", "example_reading": "いまどいしないでください。", "example_meaning_cn": "请不要逗留（或迷惑）。", "example_meaning_en": "Please don't linger/be confused here."},
        "N1_268": {"example_sentence": "（（今）いま）さ（さ）ら（ら）言わ（いわ）ないで（で）ください。", "example_reading": "いまさらいわないでください。", "example_meaning_cn": "事到如今（现在）请别说了。", "example_meaning_en": "Please don't say that at this late stage."},
        "N1_269": {"example_sentence": "（（今）いま）し（し）が（が）た（た）来（き）まし（し）た。", "example_reading": "いましがたきました。", "example_meaning_cn": "刚才来过。", "example_meaning_en": "I just arrived a moment ago."},
        "N1_270": {"example_sentence": "（（戒）いまし）め（め）て（て）ください。", "example_reading": "いましめてください。", "example_meaning_cn": "请警戒（或训诫）。", "example_meaning_en": "Please caution/admonish me."},
        "N1_271": {"example_sentence": "（（忌）い）み（み）嫌わ（きらわ）ない（ない）で（で）ください。", "example_reading": "いみきらわないでください。", "example_meaning_cn": "请不要忌嫌（厌恶）。", "example_meaning_en": "Please don't loathe/shun it."},
        "N1_272": {"example_sentence": "（（意）い）み（み）し（し）ん（ん）な（な）表情（ひょうじょう）です。", "example_reading": "いみしんなひょうじょうです。", "example_meaning_cn": "意味深长的脸。表情。", "example_meaning_en": "A meaningful/suggestive expression."},
        "N1_273": {"example_sentence": "（（卑）い）や（や）し（し）い（い）人（ひと）に（に）なら（なら）ないで（で）ください。", "example_reading": "いやしいひとにならないでください。", "example_meaning_cn": "请不要做卑贱（下流）的人。", "example_meaning_en": "Please don't be a base/mean person."},
        "N1_274": {"example_sentence": "（（負）い）や（や）な（な）こと（こと）を（を）思い出し（おもいだし）まし（し）た。", "example_reading": "いやなことをおもいだしました。", "example_meaning_cn": "想起了讨厌的事情（或胜负）。", "example_meaning_en": "I remembered something unpleasant."},
        "N1_275": {"example_sentence": "（（嫌）い）や（や）に（に）暑い（あつい）ですね。", "example_reading": "いやにあついですね。", "example_meaning_cn": "讨厌地（非常）热呢。", "example_meaning_en": "It's awfully hot, isn't it?"},
        "N1_276": {"example_sentence": "（（卑）い）や（や）し（し）め（め）ない（ない）で（で）ください。", "example_reading": "いやしめないでください。", "example_meaning_cn": "请不要轻视（卑视）。", "example_meaning_en": "Please don't despise/scorn me."},
        "N1_277": {"example_sentence": "（（癒）い）や（や）し（し）て（て）ください。", "example_reading": "いやってください。", "example_meaning_cn": "请治愈（安慰）。", "example_meaning_en": "Please heal/soothe me."},
        "N1_278": {"example_sentence": "（（嫌）い）や（や）が（が）ら（ら）せ（せ）を（を）し（し）ないで（で）ください。", "example_reading": "いやがらせをしないでください。", "example_meaning_cn": "请不要故意刁难（讨人嫌）。", "example_meaning_en": "Please don't harass/be malicious."},
        "N1_279": {"example_sentence": "（（意）い）よ（よ）う（う）に（に）なり（なり）たい（たい）です。", "example_reading": "いようになりたいです。", "example_meaning_cn": "想成就大业（或异样）。", "example_meaning_en": "I want to do something great / become strange."},
        "N1_280": {"example_sentence": "（（居）い）よ（よ）う（う）を（を）示し（しめし）て（て）ください。", "example_reading": "いようをしめしてください。", "example_meaning_cn": "请显示威容（庄重）。", "example_meaning_en": "Please show your majestic appearance."},
        "N1_281": {"example_sentence": "（（言）い）よ（よ）わ（わ）ないで（で）ください。", "example_reading": "いよわないでください。", "example_meaning_cn": "请不要（开口或归咎）。", "example_meaning_en": "Please don't say anything."},
        "N1_282": {"example_sentence": "（（意）い）よ（よ）よ（よ）頑張り（がんばり）ましょう。", "example_reading": "いよよがんばりましょう。", "example_meaning_cn": "更加地努力吧。", "example_meaning_en": "Let's work even harder."},
        "N1_283": {"example_sentence": "（（意）い）ら（ら）い（い）し（し）て（て）ください。", "example_reading": "いらいしてください。", "example_meaning_cn": "请委托（或以来）。", "example_meaning_en": "Please request it / since then."},
        "N1_284": {"example_sentence": "（（苛）いら）い（い）ら（ら）し（し）ないで（で）ください。", "example_reading": "いらいらしないでください。", "example_meaning_cn": "请不要焦躁。", "example_meaning_en": "Please don't be irritated."},
        "N1_285": {"example_sentence": "（（意）い）ら（ら）く（く）し（し）て（て）ください。", "example_reading": "いらくしてください。", "example_meaning_cn": "请使其在乐处（或安乐）。", "example_meaning_en": "Please find comfort / be at ease."},
        "N1_286": {"example_sentence": "（（意）い）ら（ら）し（し）ゃ（ゃ）っ（っ）て（て）ください。", "example_reading": "いらっしゃってください。", "example_meaning_cn": "请来（请去/请在）。", "example_meaning_en": "Please come/go/stay here (honorific)."},
        "N1_287": {"example_sentence": "（（射）い）り（り）つけ（つけ）ないで（で）ください。", "example_reading": "いりつけないでください。", "example_meaning_cn": "请不要（射中或纠缠）。", "example_meaning_en": "Please don't shoot it down / don't pester me."},
        "N1_288": {"example_sentence": "（（入）い）り（り）び（び）た（た）（（る）る）のは（は）良くない（よくない）です。", "example_reading": "いりびたるのはよくないです。", "example_meaning_cn": "老是泡在那儿（流连）不好。", "example_meaning_en": "It's not good to constantly stay somewhere."},
        "N1_289": {"example_sentence": "（（要）い）る（る）まで（まで）待っ（まっ）て（て）ください。", "example_reading": "いるまでまってください。", "example_meaning_cn": "请等他需要（或来到）。", "example_meaning_en": "Please wait until it's needed / it stays."},
        "N1_290": {"example_sentence": "（（居）い）る（る）場所（ばしょ）を（を）教えて（おしえて）ください。", "example_reading": "いるばしょをおしえてください。", "example_meaning_cn": "请告诉我所在地（身在何处）。", "example_meaning_en": "Please tell me where you are."},
        "N1_291": {"example_sentence": "（（射）い）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "いるのわてつだってください。", "example_meaning_cn": "请帮我射（或贴上）。", "example_meaning_en": "Please help me shoot it."},
        "N1_292": {"example_sentence": "（（意）い）れ（れ）い（い）し（し）て（て）ください。", "example_reading": "いれいしてください。", "example_meaning_cn": "请慰灵（或例外）。", "example_meaning_en": "Please perform a memorial / be exceptional."},
        "N1_293": {"example_sentence": "（（衣）い）れ（れ）じ（じ）（（物）もの）を（を）し（し）ないで（で）ください。", "example_reading": "いれじものをしないでください。", "example_meaning_cn": "请不要纹身。", "example_meaning_en": "Please don't get a tattoo."},
        "N1_294": {"example_sentence": "（（意）い）れ（れ）じ（じ）え（え）し（し）ないで（で）ください。", "example_reading": "いれじえしないでください。", "example_meaning_cn": "请不要出馊主意（指点）。", "example_meaning_en": "Please don't prompt / give bad advice."},
        "N1_295": {"example_sentence": "（（入）い）れ（れ）か（か）わ（わ）っ（っ）て（て）ください。", "example_reading": "いれかわってください。", "example_meaning_cn": "请调换（交替）。", "example_meaning_en": "Please swap / change places."},
        "N1_296": {"example_sentence": "（（入）い）れ（れ）こ（こ）ま（ま）ないで（で）ください。", "example_reading": "いれこまないでください。", "example_meaning_cn": "请不要着迷（或搬入）。", "example_meaning_en": "Please don't be obsessed / don't move things in."},
        "N1_297": {"example_sentence": "（（異）い）ろ（ろ）を（を）変え（かえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "いろをかえりましょう。", "example_meaning_cn": "换个颜色（或异性）吧。", "example_meaning_en": "Let's change the color."},
        "N1_298": {"example_sentence": "（（色）いろ）お（お）と（と）け（け）を（を）感じ（かんじ）ます。", "example_reading": "いろおとけをかんじます。", "example_meaning_cn": "感到好色（色欲）。", "example_meaning_en": "I feel some sexual appeal / lust."},
        "N1_299": {"example_sentence": "（（彩）いろど）り（り）を（を）添え（そえ）て（て）ください。", "example_reading": "いろどりをそえてください。", "example_meaning_cn": "请增添色彩。", "example_meaning_en": "Please add some color."},
        "N1_300": {"example_sentence": "（（色）いろ）め（め）か（か）さ（さ）ないで（で）ください。", "example_reading": "いろめかさないでください。", "example_meaning_cn": "请不要打扮得花枝招展。", "example_meaning_en": "Please don't dress up gaudily / be coquettish."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_300.")

if __name__ == "__main__":
    main()
