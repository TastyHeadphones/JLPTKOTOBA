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
        "N1_101": {"example_sentence": "（（改）あらた）め（め）て（て）話し（はなし）て（て）ください。", "example_reading": "あらためておなしてください。", "example_meaning_cn": "请重申（正式谈话）。", "example_meaning_en": "Please state it again (formally)."},
        "N1_102": {"example_sentence": "（（良）あ）ら（ら）わ（わ）し（し）て（て）ください。", "example_reading": "あらわしてください。", "example_meaning_cn": "请表现（表达）出来。", "example_meaning_en": "Please express it."},
        "N1_103": {"example_sentence": "（（現）あらわ）れ（れ）て（て）ください。", "example_reading": "あらわれてください。", "example_meaning_cn": "请出现（显现）。", "example_meaning_en": "Please appear."},
        "N1_104": {"example_sentence": "（（有）あ）る（る）が（が）まま（まま）の（の）姿（すがた）です。", "example_reading": "あるがままのすがたです。", "example_meaning_cn": "本色（原样）。", "example_meaning_en": "It's the way it is/as it is."},
        "N1_105": {"example_sentence": "（（在）あ）る（る）ま（ま）じ（じ）き（き）態度（たいど）です。", "example_reading": "あるまじきたいどです。", "example_meaning_cn": "不应有的（不当）态度。", "example_meaning_en": "An inappropriate/unbecoming attitude."},
        "N1_106": {"example_sentence": "（（在）あ）る（る）ま（ま）じ（じ）い（い）事（こと）を（を）し（し）ない（ない）で（で）ください。", "example_reading": "あるまじいことわしないでください。", "example_meaning_cn": "请不要做不该做的事。", "example_meaning_en": "Please don't do anything improper."},
        "N1_107": {"example_sentence": "（（歩）ある）き（き）ま（ま）わ（わ）ら（ら）ないで（で）ください。", "example_reading": "あるきまわらないでください。", "example_meaning_cn": "请不要走来走去。", "example_meaning_en": "Please don't walk around."},
        "N1_108": {"example_sentence": "（（安）あん）い（い）な（な）考え（かんがえ）は（は）避け（さけ）ましょう。", "example_reading": "あんいなかんがえわさけましょう。", "example_meaning_cn": "避开轻率（简易）的想法吧。", "example_meaning_en": "Let's avoid easy/naive thinking."},
        "N1_109": {"example_sentence": "（（案）あん）が（が）い（い）面白い（おもしろい）です。", "example_reading": "あんがいおもしろいです。", "example_meaning_cn": "出乎意料（意外）地有趣。", "example_meaning_en": "It's unexpectedly interesting."},
        "N1_110": {"example_sentence": "（（暗）あん）き（き）し（し）て（て）ください。", "example_reading": "あんきしてください。", "example_meaning_cn": "请背诵（默记）。", "example_meaning_en": "Please memorize it."},
        "N1_111": {"example_sentence": "（（暗）あん）こ（こ）う（う）に（に）し（し）て（て）ください。", "example_reading": "あんこうにしてください。", "example_meaning_cn": "请使其在暗处（或暗号）。", "example_meaning_en": "Please keep it in the dark/use a code."},
        "N1_112": {"example_sentence": "（（暗）あん）さ（さ）つ（つ）し（し）ないで（で）ください！ ", "example_reading": "あんさつしないでください！", "example_meaning_cn": "请不要暗杀！", "example_meaning_en": "Please don't assassinate!"},
        "N1_113": {"example_sentence": "（（案）あん）じ（じ）て（て）ください。", "example_reading": "あんじてください。", "example_meaning_cn": "请担心（或构思）。", "example_meaning_en": "Please worry/contrive it."},
        "N1_114": {"example_sentence": "（（暗）あん）し（し）して（て）ください。", "example_reading": "あんししてください。", "example_meaning_cn": "请放心（或暗示）。", "example_meaning_en": "Please rest assured/be reassured."},
        "N1_115": {"example_sentence": "（（安）あん）じ（じ）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "あんじょうしてください。", "example_meaning_cn": "请妥善处理（或乘马）。", "example_meaning_en": "Please manage it well/ride a horse."},
        "N1_116": {"example_sentence": "（（多）あん）ず（ず）る（る）より（より）産む（うむ）が（が）易し（やすし）です。", "example_reading": "あんずるよりうむがやすしです。", "example_meaning_cn": "忧虑不如实践（车到山前必有路）。", "example_meaning_en": "It's easier to do than to worry about it."},
        "N1_117": {"example_sentence": "（（案）あん）せ（せ）い（い）に（に）し（し）て（て）ください。", "example_reading": "あんせいにしてください。", "example_meaning_cn": "请静养（安静）。", "example_meaning_en": "Please rest quietly."},
        "N1_118": {"example_sentence": "（（案）あん）ぜ（ぜ）ん（ん）を（を）確認（かくにん）し（し）てください。", "example_reading": "あんぜんをかくにんしてください。", "example_meaning_cn": "请确认安全。", "example_meaning_en": "Please confirm the safety."},
        "N1_119": {"example_sentence": "（（案）あん）な（な）い（い）し（し）て（て）ください。", "example_reading": "あんないしてください。", "example_meaning_cn": "请引导（带路）。", "example_meaning_en": "Please guide me."},
        "N1_120": {"example_sentence": "（（暗）あん）に（に）伝え（つたえ）て（て）ください。", "example_reading": "あんにたえてください。", "example_meaning_cn": "请暗中传达（暗示）。", "example_meaning_en": "Please convey it implicitly."},
        "N1_121": {"example_sentence": "（（安）あん）の（の）ん（ん）な（な）日々（ひび）です。", "example_reading": "あんのんなひびです。", "example_meaning_cn": "安稳（和平）的日子。", "example_meaning_en": "Peaceful/quiet days."},
        "N1_122": {"example_sentence": "（（暗）あん）む（む）に（に）なり（なり）そう（そう）です。", "example_reading": "あんむになりそうです。", "example_meaning_cn": "好像要变暗（或大雾）。", "example_meaning_en": "It seems to be getting dark/foggy."},
        "N1_123": {"example_sentence": "（（案）あん）も（も）ん（ん）し（し）て（て）ください。", "example_reading": "あんもんしてください。", "example_meaning_cn": "请起草（或暗算）。", "example_meaning_en": "Please draft it/calculate mentally."},
        "N1_124": {"example_sentence": "（（暗）あん）り（り）に（に）話し（はなし）て（て）ください。", "example_reading": "あんりにおなしてください。", "example_meaning_cn": "请私下（或暗中）谈话。", "example_meaning_en": "Please talk privately/implicitly."},
        "N1_125": {"example_sentence": "（（威）い）を（を）張っ（はっ）て（て）ください。", "example_reading": "いをはってください。", "example_meaning_cn": "请威风凛凛（张威）。", "example_meaning_en": "Please put on airs/exert authority."},
        "N1_126": {"example_sentence": "（（意）い）を（を）決し（けっし）て（て）ください。", "example_reading": "いをけっしてください。", "example_meaning_cn": "请下定决心。", "example_meaning_en": "Please make up your mind."},
        "N1_127": {"example_sentence": "（（胃）い）が（が）痛い（いたい）です。", "example_reading": "いがいたいです。", "example_meaning_cn": "胃疼。", "example_meaning_en": "My stomach hurts."},
        "N1_128": {"example_sentence": "（（委）い）い（い）し（し）ないで（で）ください。", "example_reading": "いいしないでください。", "example_meaning_cn": "请不要推诿（或委托）。", "example_meaning_en": "Please don't delegate/shirk."},
        "N1_129": {"example_sentence": "（（言）い）い（い）当て（あて）て（て）ください。", "example_reading": "いいあててください。", "example_meaning_cn": "请猜中。", "example_meaning_en": "Please guess correctly."},
        "N1_130": {"example_sentence": "（（言）い）い（い）合わ（あわ）せ（せ）て（て）ください。", "example_reading": "いいあわせてください。", "example_meaning_cn": "请约好（商定）。", "example_meaning_en": "Please arrange/agree beforehand."},
        "N1_131": {"example_sentence": "（（言）い）い（い）お（お）こ（こ）し（し）て（て）ください。", "example_reading": "いいおこしてください。", "example_meaning_cn": "请传话（或寄信）。", "example_meaning_en": "Please send word/a letter."},
        "N1_132": {"example_sentence": "（（言）い）い（い）か（か）え（え）て（て）ください。", "example_reading": "いいかえてください。", "example_meaning_cn": "请换句话说。", "example_meaning_en": "Please rephrase it."},
        "N1_133": {"example_sentence": "（（言）い）い（い）か（か）け（け）ない（ない）で（で）ください。", "example_reading": "いいかけないでください。", "example_meaning_cn": "请不要（开口或归咎）。", "example_meaning_en": "Please don't (start to say/accuse)."},
        "N1_134": {"example_sentence": "（（言）い）い（い）か（か）げ（げ）ん（ん）に（に）し（し）て（て）ください。", "example_reading": "いいかげんにしてください。", "example_meaning_cn": "请适可而止。", "example_meaning_en": "Please stop it/don't be irresponsible."},
        "N1_135": {"example_sentence": "（（言）い）い（い）き（き）か（か）せ（せ）て（て）ください。", "example_reading": "いいきかせてください。", "example_meaning_cn": "请劝导（说服）。", "example_meaning_en": "Please reason with/persuade me."},
        "N1_136": {"example_sentence": "（（言）い）い（い）き（き）っ（っ）て（て）ください。", "example_reading": "いいきってください。", "example_meaning_cn": "请断言（或说尽）。", "example_meaning_en": "Please state definitely/finish saying."},
        "N1_137": {"example_sentence": "（（言）い）い（い）く（く）る（る）め（め）ない（ない）で（で）ください。", "example_reading": "いいくるめないでください。", "example_meaning_cn": "请不要巧辩（哄骗）。", "example_meaning_en": "Please don't quibble/deceive with words."},
        "N1_138": {"example_sentence": "（（言）い）い（い）し（し）ぶ（ぶ）ら（ら）ないで（で）ください。", "example_reading": "いいしぶらないでください。", "example_meaning_cn": "请不要吞吞吐吐。", "example_meaning_en": "Please don't hesitate to say it."},
        "N1_139": {"example_sentence": "（（言）い）い（い）すぎ（すぎ）ないで（で）ください。", "example_reading": "いいすぎないでください。", "example_meaning_cn": "请不要失言（说得过火）。", "example_meaning_en": "Please don't overstate/say too much."},
        "N1_140": {"example_sentence": "（（言）い）い（い）そ（そ）こ（こ）な（な）わ（わ）ないで（で）ください。", "example_reading": "いいそこなわないでください。", "example_meaning_cn": "请不要说错（或漏说）。", "example_meaning_en": "Please don't misspeak/omit saying it."},
        "N1_141": {"example_sentence": "（（言）い）い（い）た（た）い（い）こと（こと）を（を）言っ（いっ）て（て）ください。", "example_reading": "いいたいことをいってください。", "example_meaning_cn": "请说出想说的话。", "example_meaning_en": "Please say what you want to say."},
        "N1_142": {"example_sentence": "（（言）い）い（い）た（た）て（て）て（て）ください。", "example_reading": "いいたててください。", "example_meaning_cn": "请宣扬（或强调）。", "example_meaning_en": "Please advocate/assert."},
        "N1_143": {"example_sentence": "（（言）い）い（い）つ（つ）け（け）に（に）し（し）ない（ない）で（で）ください。", "example_reading": "いいつけにしないでください。", "example_meaning_cn": "请不要告状（或嘱咐）。", "example_meaning_en": "Please don't tell on me/order me."},
        "N1_144": {"example_sentence": "（（言）い）い（い）つ（つ）た（た）え（え）を（を）信じ（しんじ）ます。", "example_reading": "いいつたえをきんじます。", "example_meaning_cn": "相信传说（言传）。", "example_meaning_en": "I believe in the tradition/legend."},
        "N1_145": {"example_sentence": "（（言）い）い（い）つ（つ）な（な）ぎ（ぎ）して（て）ください。", "example_reading": "いいつなぎしてください。", "example_meaning_cn": "请传话（或联系）。", "example_meaning_en": "Please pass on the word."},
        "N1_146": {"example_sentence": "（（言）い）い（い）つ（つ）の（の）れ（れ）ないで（で）ください。", "example_reading": "いいつのれないでください。", "example_meaning_cn": "请不要激烈争论（或加剧）。", "example_meaning_en": "Please don't argue fiercely."},
        "N1_147": {"example_sentence": "（（言）い）い（い）とお（とお）し（し）て（て）ください。", "example_reading": "いいとおしてください。", "example_meaning_cn": "请坚持说到底。", "example_meaning_en": "Please stick to your word/say it through."},
        "N1_148": {"example_sentence": "（（言）い）い（い）な（な）り（り）に（に）なら（なら）ないで（で）ください。", "example_reading": "いいなりにならないでください。", "example_meaning_cn": "请不要唯命是从。", "example_meaning_en": "Please don't be a yes-man."},
        "N1_149": {"example_sentence": "（（言）い）い（イ）に（に）くい（くい）こと（こと）を（を）話し（はなし）て（て）ください。", "example_reading": "いいにくいことをおなしてください。", "example_meaning_cn": "请把难言之隐（难说的话）说出来。", "example_meaning_en": "Please say what's hard to say."},
        "N1_150": {"example_sentence": "（（言）い）い（い）のか（のか）さ（さ）ないで（で）ください。", "example_reading": "いいのかさないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying/let it pass)."},
        "N1_151": {"example_sentence": "（（言）い）い（い）は（は）り（り）ま（ま）しょ（しょ）う（う）。", "example_reading": "いいはりましょう。", "example_meaning_cn": "坚持已见吧。", "example_meaning_en": "Let's insist on it."},
        "N1_152": {"example_sentence": "（（言）い）い（い）ふ（ふ）ら（ら）さ（さ）ないで（で）ください。", "example_reading": "いいふらさないでください。", "example_meaning_cn": "请不要到处宣扬。", "example_meaning_en": "Please don't spread rumors."},
        "N1_153": {"example_sentence": "（（言）い）い（い）ま（ま）か（か）せ（せ）て（て）ください。", "example_reading": "いいまかせてください。", "example_meaning_cn": "请把对方驳倒。", "example_meaning_en": "Please talk them down/refute them."},
        "N1_154": {"example_sentence": "（（言）い）い（い）も（も）ら（ら）さ（さ）ないで（で）ください。", "example_reading": "いいもらさないでください。", "example_meaning_cn": "请不要漏掉（或泄密）。", "example_meaning_en": "Please don't omit anything/leak it."},
        "N1_155": {"example_sentence": "（（言）い）い（い）よ（よ）う（う）が（が）あり（あり）ません。", "example_reading": "いいようがありません。", "example_meaning_cn": "无法用言语表达（无话可说）。", "example_meaning_en": "It's beyond words."},
        "N1_156": {"example_sentence": "（（言）い）い（い）わ（わ）け（け）を（を）し（し）ないで（で）ください。", "example_reading": "いいわけをしないでください。", "example_meaning_cn": "请不要辩解。", "example_meaning_en": "Please don't make excuses."},
        "N1_157": {"example_sentence": "（（家）い）え（え）に（に）帰り（かえり）ましょう。", "example_reading": "いえにかえりましょう。", "example_meaning_cn": "回家吧。", "example_meaning_en": "Let's go home."},
        "N1_158": {"example_sentence": "（（否）い）え（え）、（え）そう（そう）では（は）あり（あり）ません。", "example_reading": "いえそうわありません。", "example_meaning_cn": "不，不是那样。", "example_meaning_en": "No, that's not it."},
        "N1_159": {"example_sentence": "（（言）い）え（え）よ（よ）う（う）の（の）ない（ない）美しさ（うつくしさ）です。", "example_reading": "いえようのないうつくしさです。", "example_meaning_cn": "无法言喻的美丽。", "example_meaning_en": "Unspeakable beauty."},
        "N1_160": {"example_sentence": "（（位）い）か（か）を（を）正し（ただし）て（て）ください。", "example_reading": "いかをただしてください。", "example_meaning_cn": "请端正位置（或威严）。", "example_meaning_en": "Please adjust your position/dignity."},
        "N1_161": {"example_sentence": "（（意）い）が（が）い（い）な（な）結果（けっか）です。", "example_reading": "いがいなけっかです。", "example_meaning_cn": "意外的结果。", "example_meaning_en": "An unexpected result."},
        "N1_162": {"example_sentence": "（（怒）いか）ら（ら）せ（せ）ないで（で）ください。", "example_reading": "いからせないでください。", "example_meaning_cn": "请不要让我生气。", "example_meaning_en": "Please don't make me angry."},
        "N1_163": {"example_sentence": "（（怒）いか）り（り）を（を）静め（しずめ）て（て）ください。", "example_reading": "いかりをしずめてください。", "example_meaning_cn": "请平息怒火。", "example_meaning_en": "Please calm your anger."},
        "N1_164": {"example_sentence": "（（錨）いかり）を（を）おろ（おろ）し（し）て（て）ください。", "example_reading": "いかりをおろしてください。", "example_meaning_cn": "请抛锚。", "example_meaning_en": "Please drop the anchor."},
        "N1_165": {"example_sentence": "（（活）いか）し（し）て（て）ください。", "example_reading": "いかしてください。", "example_meaning_cn": "请使其发挥作用（活）。", "example_meaning_en": "Please make use of it/keep it alive."},
        "N1_166": {"example_sentence": "（（如何）いか）に（に）もし（し）て（て）ください。", "example_reading": "いかにもしてください。", "example_meaning_cn": "无论如何请照办。", "example_meaning_en": "Please do it by all means."},
        "N1_167": {"example_sentence": "（（如何）いか）な（な）る（る）時（とき）も（も）頑張り（がんばり）ましょう。", "example_reading": "いかなるときもがんばりましょう。", "example_meaning_cn": "无论何时都努力吧。", "example_meaning_en": "Let's work hard whatever the time."},
        "N1_168": {"example_sentence": "（（如何）いか）に（に）も（も）その（その）通り（とおり）です。", "example_reading": "いかしもそのとおりです。", "example_meaning_cn": "确实如此。", "example_meaning_en": "Indeed, that's right."},
        "N1_169": {"example_sentence": "（（怒）いか）め（め）し（し）い（い）門（もん）です。", "example_reading": "いかめしいもんです。", "example_meaning_cn": "庄严（威严）的大门。", "example_meaning_en": "A solemn/stately gate."},
        "N1_170": {"example_sentence": "（（行）い）か（か）ら（ら）せ（せ）て（て）ください。", "example_reading": "いからせてください。", "example_meaning_cn": "请让我走。", "example_meaning_en": "Please let me go."},
        "N1_171": {"example_sentence": "（（粋）いき）な（な）計らい（はからい）ですね。", "example_reading": "いきなはからいですね。", "example_reading": "いきなはからいですね。", "example_meaning_cn": "真是漂亮（潇洒）的处理呢。", "example_meaning_en": "That's a stylish/chic arrangement."},
        "N1_172": {"example_sentence": "（（意）いき）ぎ（ぎ）れ（れ）し（し）ないで（で）ください。", "example_reading": "いきぎれしないでください。", "example_meaning_cn": "请不要气喘吁吁。", "example_meaning_en": "Please don't run out of breath."},
        "N1_173": {"example_sentence": "（（行）い）き（き）こ（こ）み（み）を（を）話し（はなし）て（て）ください。", "example_reading": "いきこみをおなしてください。", "example_meaning_cn": "请说说你的干劲。", "example_meaning_en": "Please tell me about your enthusiasm."},
        "N1_174": {"example_sentence": "（（行）い）き（き）さ（さ）つ（つ）を（を）説明（せつめい）し（し）て（て）ください。", "example_reading": "いきさつをせつめいしてください。", "example_meaning_cn": "请说明缘由（经过）。", "example_meaning_en": "Please explain the circumstances."},
        "N1_175": {"example_sentence": "（（意）いき）じ（じ）を（を）張ら（はら）ないで（で）ください。", "example_reading": "いきじをはらないでください。", "example_meaning_cn": "请不要意气用事（张狂）。", "example_meaning_en": "Please don't be stubborn/show off your spirit."},
        "N1_176": {"example_sentence": "（（行）い）き（き）ず（ず）ま（ま）ら（ら）ないで（で）ください。", "example_reading": "いきずまらないでください。", "example_meaning_cn": "请不要走投无路（或停滞）。", "example_meaning_en": "Please don't come to a deadlock."},
        "N1_177": {"example_sentence": "（（行）い）き（き）とど（とど）い（い）て（て）いますね。", "example_reading": "いきとどいていますね。", "example_meaning_cn": "真是无微不至（周到）呢。", "example_meaning_en": "It's very well-attended/thorough."},
        "N1_178": {"example_sentence": "（（息）いき）ど（ど）お（お）り（り）を（を）感じ（かんじ）ます。", "example_reading": "いきどおりをかんじます。", "example_meaning_cn": "感到愤慨。", "example_meaning_en": "I feel resentment/indignation."},
        "N1_179": {"example_sentence": "（（行）い）き（き）な（な）り（り）来（き）ないで（で）ください。", "example_reading": "いきなりこないでください。", "example_meaning_cn": "请不要突然（唐突）过来。", "example_meaning_en": "Please don't come suddenly."},
        "N1_180": {"example_sentence": "（（意）いき）の（の）き（き）を（を）し（し）て（て）ください。", "example_reading": "いきのきをしてください。", "example_meaning_cn": "请松口气（或换气）。", "example_meaning_en": "Please take a breather."},
        "N1_181": {"example_sentence": "（（活）いき）い（い）き（き）し（し）て（て）いますね。", "example_reading": "いきいきしていますね。", "example_meaning_cn": "真有活力（生机勃勃）呢。", "example_meaning_en": "You're very lively/vibrant."},
        "N1_182": {"example_sentence": "（（育）いく）じ（じ）に（に）励ん（はげん）で（て）ください。", "example_reading": "いくじにはげんでください。", "example_meaning_cn": "请致力于育儿。", "example_meaning_en": "Please devote yourself to childcare."},
        "N1_183": {"example_sentence": "（（幾）いく）た（た）の（の）困難（こんなん）を（を）乗り越え（のりこえ）まし（し）た。", "example_reading": "いくたのこんなんをのりこえました。", "example_meaning_cn": "克服了许多（无数）困难。", "example_meaning_en": "I overcame many difficulties."},
        "N1_184": {"example_sentence": "（（幾）いく）ば（ば）く（く）も（も）なく（なく）終わり（おわり）まし（し）た。", "example_reading": "いくばくもなくおわりました。", "example_meaning_cn": "没过多久（为时不多）就结束了。", "example_meaning_en": "It ended before long."},
        "N1_185": {"example_sentence": "（（意）い）く（く）れ（れ）ないで（で）ください。", "example_reading": "いくれないでください。", "example_meaning_cn": "请不要意气（或任性）。", "example_meaning_en": "Please don't be stubborn."},
        "N1_186": {"example_sentence": "（（生）い）け（け）け（け）し（し）い（い）嘘（うそ）です。", "example_reading": "いけけしいうそです。", "example_meaning_cn": "无耻（可恶）的谎言。", "example_meaning_en": "A brazen/shameless lie."},
        "N1_187": {"example_sentence": "（（生）い）け（け）す（す）（（花）はな）を（を）飾っ（かざっ）て（て）ください。", "example_reading": "いけすはなをかざってください。", "example_meaning_cn": "请装饰插花（生花）。", "example_meaning_en": "Please decorate with flower arrangement."},
        "N1_188": {"example_sentence": "（（意）い）け（け）つ（つ）し（し）ないで（で）ください。", "example_reading": "いけつしないでください。", "example_meaning_cn": "请不要（拒决或裁决）。", "example_meaning_en": "Please don't (reject/decide)."},
        "N1_189": {"example_sentence": "（（意）い）げ（げ）ん（ん）を（を）保っ（たもっ）て（て）ください。", "example_reading": "いげんをたもってください。", "example_meaning_cn": "请保持威严（尊严）。", "example_meaning_en": "Please maintain your dignity."},
        "N1_190": {"example_sentence": "（（言）い）ご（ご）に（に）耳（みみ）を（来）さ（さ）せ（せ）て（て）ください。", "example_reading": "いごにみみをきさせてください。", "example_meaning_cn": "请让我听听遗言（后话）。", "example_meaning_en": "Please let me hear the final words."},
        "N1_191": {"example_sentence": "（（囲）い）ご（ご）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "いごをたのしみましょう。", "example_meaning_cn": "下围棋吧。", "example_meaning_en": "Let's enjoy a game of Go."},
        "N1_192": {"example_sentence": "（（意）い）ざ（ざ）出陣（しゅつじん）し（し）ましょう。", "example_reading": "いざしゅつじんしましょう。", "example_meaning_cn": "那就（一旦）出阵吧。", "example_meaning_en": "Now, let's go to battle."},
        "N1_193": {"example_sentence": "（（意）い）じ（じ）し（し）て（て）ください。", "example_reading": "いじしてください。", "example_meaning_cn": "请维持。", "example_meaning_en": "Please maintain/preserve it."},
        "N1_194": {"example_sentence": "（（意）い）し（し）き（き）を（を）はっきり（はっきり）させ（さ）せ（せ）て（て）ください。", "example_reading": "いしきをはっきりさせてください。", "example_meaning_cn": "请保持意识清醒。", "example_meaning_en": "Please keep your consciousness clear."},
        "N1_195": {"example_sentence": "（（衣）い）し（し）ょ（ょ）く（く）し（し）て（て）ください。", "example_reading": "いしょくしてください。", "example_meaning_cn": "请移植（或衣食）。", "example_meaning_en": "Please transplant/clothe and feed."},
        "N1_196": {"example_sentence": "（（意）い）じ（じ）わ（わ）る（る）し（し）ないで（で）ください。", "example_reading": "いじわるしないでください。", "example_meaning_cn": "请不要使坏。", "example_meaning_en": "Please don't be mean."},
        "N1_197": {"example_sentence": "（（意）い）す（す）い（い）し（し）ないで（で）ください。", "example_reading": "いすいしないでください。", "example_meaning_cn": "请不要打瞌睡（微睡）。", "example_meaning_en": "Please don't doze off."},
        "N1_198": {"example_sentence": "（（泉）いずみ）が（が）湧い（わい）て（て）います。", "example_reading": "いずみがわいています。", "example_meaning_cn": "泉水正在涌出。", "example_meaning_en": "The spring is bubbling up."},
        "N1_199": {"example_sentence": "（（依然）いぜん）として（とて）変わり（かわり）ませ（ませ）ん。", "example_reading": "いぜんととしてかわりません。", "example_meaning_cn": "依然没有变化。", "example_meaning_en": "It remains unchanged as before."},
        "N1_200": {"example_sentence": "（（急）いそ）が（が）せ（せ）て（て）すみません。", "example_reading": "いそがせてすみません。", "example_meaning_cn": "催促你真抱歉。", "example_meaning_en": "I'm sorry to rush you."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_200.")

if __name__ == "__main__":
    main()
