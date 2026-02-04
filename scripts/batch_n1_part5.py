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
        "N1_401": {"example_sentence": "（（売）う）り（り）さ（さ）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "うりさらわないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_402": {"example_sentence": "（（売）う）り（り）つ（つ）く（く）し（し）て（て）ください。", "example_reading": "うりつくしてください。", "example_meaning_cn": "请卖尽（或售完）。", "example_meaning_en": "Please sell it all off / sell out."},
        "N1_403": {"example_sentence": "（（売）う）り（り）つ（つ）け（け）て（て）ください。", "example_reading": "うりつけてください。", "example_meaning_cn": "请强行卖给（或推销）。", "example_meaning_en": "Please force a sale / push it on me."},
        "N1_404": {"example_sentence": "（（売）う）り（り）と（と）ば（ば）し（し）て（て）ください。", "example_reading": "うりとばしてください。", "example_meaning_cn": "请卖掉（甩卖）。", "example_meaning_en": "Please sell it off / dump it."},
        "N1_405": {"example_sentence": "（（売）う）り（り）も（も）の（の）に（に）し（し）ましょ（しょ）う（う）。", "example_reading": "うりものにしましょう。", "example_meaning_cn": "拿去卖（作为商品）吧。", "example_meaning_en": "Let's put it up for sale."},
        "N1_406": {"example_sentence": "（（売）う）り（り）わ（わ）た（た）し（し）て（て）ください。", "example_reading": "うりわたしてください。", "example_meaning_cn": "请转卖（或交付）。", "example_meaning_en": "Please sell and deliver / transfer it."},
        "N1_407": {"example_sentence": "（（潤）うる）お（お）い（い）を（を）与え（あたえ）て（て）ください。", "example_reading": "うるおいをあたえてください。", "example_meaning_cn": "请给予滋润（或利益）。", "example_meaning_en": "Please provide moisture / enrichment."},
        "N1_408": {"example_sentence": "（（潤）うる）お（お）し（し）て（て）ください。", "example_reading": "うるおしてください。", "example_meaning_cn": "请使其滋润。", "example_meaning_en": "Please moisten / soak it."},
        "N1_409": {"example_sentence": "（（潤）うる）お（お）ん（ん）で（て）ください。", "example_reading": "うるおんでください。", "example_meaning_cn": "请润湿（或受惠）。", "example_meaning_en": "Please be moistened / benefit from it."},
        "N1_410": {"example_sentence": "（（煩）うるさ）い（い）です。", "example_reading": "うるさいです。", "example_meaning_cn": "太吵了。", "example_meaning_en": "It's noisy / annoying."},
        "N1_411": {"example_sentence": "（（浮）う）わ（わ）つ（つ）か（か）ないで（で）ください。", "example_reading": "うわつかないでください。", "example_meaning_cn": "请不要轻浮。", "example_meaning_en": "Please don't be fickle / flighty."},
        "N1_412": {"example_sentence": "（（噂）うわさ）を（を）し（し）ないで（で）ください。", "example_reading": "うわさをしないでください。", "example_meaning_cn": "请不要传流言。", "example_meaning_en": "Please don't gossip."},
        "N1_413": {"example_sentence": "（（浮）う）わ（わ）き（き）し（し）ないで（で）ください。", "example_reading": "うわきしないでください。", "example_meaning_cn": "请不要见异思迁（花心）。", "example_meaning_en": "Please don't be unfaithful / have an affair."},
        "N1_414": {"example_sentence": "（（噂）うわさ）ば（ば）な（な）し（し）を（を）やめ（やめ）ましょ（しょ）う（う）。", "example_reading": "うわさばなしをやめましょう。", "example_meaning_cn": "停止说闲话吧。", "example_meaning_en": "Let's stop the gossip / idle talk."},
        "N1_415": {"example_sentence": "（（噂）うわさ）を（を）振りまか（ふりまか）ないで（で）ください。", "example_reading": "うわさをふりまかないでください。", "example_meaning_cn": "请不要散播谣言。", "example_meaning_en": "Please don't spread rumors."},
        "N1_416": {"example_sentence": "（（植）う）わ（わ）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "うわらわないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_417": {"example_sentence": "（（産）う）ん（ん）で（て）ください。", "example_reading": "うんでください。", "example_meaning_cn": "请生产（或分娩）。", "example_meaning_en": "Please give birth / produce it."},
        "N1_418": {"example_sentence": "（（運）うん）が（が）いい（いい）ですね。", "example_reading": "うんがいいですね。", "example_meaning_cn": "运气真好呢。", "example_meaning_en": "You're lucky."},
        "N1_419": {"example_sentence": "（（云）うん）ぬ（ぬ）ん（ん）言わ（いわ）ないで（で）ください。", "example_reading": "うんぬんいわないでください。", "example_meaning_cn": "请不要多说（云云）。", "example_meaning_en": "Please don't make various comments."},
        "N1_420": {"example_sentence": "（（運）うん）ぱ（ぱ）ん（ん）し（し）て（て）ください。", "example_reading": "うんぱんしてください。", "example_meaning_cn": "请搬运。", "example_meaning_en": "Please transport it."},
        "N1_421": {"example_sentence": "（（動）え）い（い）が（が）を（を）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "えいがをみましょう。", "example_meaning_cn": "看电影吧。", "example_meaning_en": "Let's watch a movie."},
        "N1_422": {"example_sentence": "（（永）えい）き（き）ゅ（ゅ）う（う）に（に）愛し（あいし）て（て）ください。", "example_reading": "えいきゅうにあいしてください。", "example_meaning_cn": "请永远爱我。", "example_meaning_en": "Please love me forever."},
        "N1_423": {"example_sentence": "（（影）えい）き（き）ょ（ょ）う（う）を（を）受け（うけ）ないで（で）ください。", "example_reading": "えいきょうをうけないでください。", "example_meaning_cn": "请不要受影响。", "example_meaning_en": "Please don't be influenced."},
        "N1_424": {"example_sentence": "（（営）えい）ぎ（ぎ）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "えいぎょうしてください。", "example_meaning_cn": "请营业（经营）。", "example_meaning_en": "Please do business / operate."},
        "N1_425": {"example_sentence": "（（影）えい）さ（さ）つ（つ）し（し）ないで（で）ください。", "example_reading": "えいさつしないでください。", "example_meaning_cn": "请不要印（印刷）。", "example_meaning_en": "Please don't print it."},
        "N1_426": {"example_sentence": "（（衛）えい）せ（せ）い（い）を（を）保っ（たもっ）て（て）ください。", "example_reading": "えいせいをたもってください。", "example_meaning_cn": "请保持卫生。", "example_meaning_en": "Please maintain hygiene."},
        "N1_427": {"example_sentence": "（（影）えい）ぞ（ぞ）う（う）を（を）見（み）て（て）ください。", "example_reading": "えいぞうをみてください。", "example_meaning_cn": "请看影像。", "example_meaning_en": "Please see the video / image."},
        "N1_428": {"example_sentence": "（（英）えい）ち（ち）を（を）結集（けっしゅう）し（し）ましょ（しょ）う（う）。", "example_reading": "えいちをけっしゅうしましょう。", "example_meaning_cn": "集思广益（结集睿智）吧。", "example_meaning_en": "Let's combine our collective wisdom."},
        "N1_429": {"example_sentence": "（（英）えい）ど（ど）く（く）し（し）て（て）ください。", "example_reading": "えいどくしてください。", "example_meaning_cn": "请阅读英语。", "example_meaning_en": "Please read English."},
        "N1_430": {"example_sentence": "（（英）えい）ぶ（ぶ）ん（ん）で（て）書い（かい）て（て）ください。", "example_reading": "えいぶんでかいてください。", "example_meaning_cn": "请用英文写。", "example_meaning_en": "Please write in English."},
        "N1_431": {"example_sentence": "（（英）えい）め（め）い（い）な（な）判断（はんだん）です。", "example_reading": "えいめいなはんだんです。", "example_meaning_cn": "英明的判断。", "example_meaning_en": "It's a wise / sagacious judgment."},
        "N1_432": {"example_sentence": "（（繁）えい）ゆ（ゆ）う（う）に（に）なり（なり）たい（たい）です。", "example_reading": "えいゆうになりたいです。", "example_meaning_cn": "想成为英雄。", "example_meaning_en": "I want to be a hero."},
        "N1_433": {"example_sentence": "（（繁）えい）よ（よ）う（う）を（を）摂り（とり）ま（ま）しょ（しょ）う（う）。", "example_reading": "えいようをとりましょう。", "example_meaning_cn": "摄取营养吧。", "example_meaning_en": "Let's get some nutrition."},
        "N1_434": {"example_sentence": "（（繁）えい）ら（ら）ん（ん）し（し）ないで（で）ください。", "example_reading": "えいらんしないでください。", "example_meaning_cn": "请不要（广阅或圣览）。", "example_meaning_en": "Please don't (peruse / look over)."},
        "N1_435": {"example_sentence": "（（繁）えい）り（り）を（を）目的（もくてき）と（と）し（し）ないで（で）ください。", "example_reading": "えいりをもくてきとしないでください。", "example_meaning_cn": "不要以营利为目的。", "example_meaning_en": "Please don't make it for-profit."},
        "N1_436": {"example_sentence": "（（柄）え）が（が）あり（あり）ますね。", "example_reading": "えがありますね。", "example_meaning_cn": "真有风度（或手柄）呢。", "example_meaning_en": "It has character / it has a handle."},
        "N1_437": {"example_sentence": "（（描）えが）い（い）て（て）ください。", "example_reading": "えがいてください。", "example_meaning_cn": "请描绘。", "example_meaning_en": "Please draw / depict it."},
        "N1_438": {"example_sentence": "（（笑）えが）お（お）で（で）会い（あい）ましょう。", "example_reading": "えがおであいましょう。", "example_meaning_cn": "笑着见面吧。", "example_meaning_en": "Let's meet with a smile."},
        "N1_439": {"example_sentence": "（（餌）えさ）を（を）まき（まき）ましょ（しょ）う（う）。", "example_reading": "えさをまきましょう。", "example_meaning_cn": "撒饵吧。", "example_meaning_en": "Let's scatter the bait."},
        "N1_440": {"example_sentence": "（（会）え）し（し）ゃ（ゃ）く（く）し（し）て（て）ください。", "example_reading": "えしゃくしてください。", "example_meaning_cn": "请行个礼（寒暄）。", "example_meaning_en": "Please make a slight bow."},
        "N1_441": {"example_sentence": "（（縁）えん）が（が）あり（あり）ますね。", "example_reading": "えんがありますね。", "example_meaning_cn": "真是有缘（或边缘）呢。", "example_meaning_en": "There's a connection / tie between us."},
        "N1_442": {"example_sentence": "（（円）えん）か（か）つ（つ）に（に）進め（すすめ）て（て）ください。", "example_reading": "えんかつにすすめてください。", "example_meaning_cn": "请圆滑（顺利）地进行。", "example_meaning_en": "Please proceed smoothly."},
        "N1_443": {"example_sentence": "（（延）えん）き（き）し（し）て（て）ください。", "example_reading": "えんきしてください。", "example_meaning_cn": "请延期。", "example_meaning_en": "Please postpone it."},
        "N1_444": {"example_sentence": "（（演）えん）ぎ（ぎ）し（し）て（て）ください。", "example_reading": "えんぎしてください。", "example_meaning_cn": "请表演（演技）。", "example_meaning_en": "Please act / perform."},
        "N1_445": {"example_sentence": "（（遠）えん）き（き）ょ（ょ）り（り）恋愛（れんあい）です。", "example_reading": "えんきょりれんそうです。", "example_meaning_cn": "远距离公开。恋爱。", "example_meaning_en": "It's a long-distance relationship."},
        "N1_446": {"example_sentence": "（（遠）えん）げ（げ）ん（ん）に（に）し（し）て（て）ください。", "example_reading": "えんげんにしてください。", "example_meaning_cn": "请远离（或远因）。", "example_meaning_en": "Please keep away / remote cause."},
        "N1_447": {"example_sentence": "（（演）えん）げ（げ）き（き）を（を）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "えんげきをみましょう。", "example_meaning_cn": "看演戏吧。", "example_meaning_en": "Let's watch a play."},
        "N1_448": {"example_sentence": "（（演）えん）こ（こ）う（う）し（し）ないで（で）ください。", "example_reading": "えんこうしないでください。", "example_meaning_cn": "请不要（援交或火光）。", "example_meaning_en": "Please don't (engage in compensated dating / flame)."},
        "N1_449": {"example_sentence": "（（援）えん）ご（ご）し（し）て（て）ください。", "example_reading": "えんごしてください。", "example_meaning_cn": "请援护。", "example_meaning_en": "Please support / cover me."},
        "N1_450": {"example_sentence": "（（演）えん）さ（さ）い（い）し（し）て（て）ください。", "example_reading": "えんさいしてください。", "example_meaning_cn": "请演奏（或延期）。", "example_meaning_en": "Please perform / postpone."},
        "N1_451": {"example_sentence": "（（演）えん）さ（さ）く（く）し（し）ないで（で）ください。", "example_reading": "えんさくしないでください。", "example_meaning_cn": "请不要（掩饰或演算）。", "example_meaning_en": "Please don't (conceal / calculate)."},
        "N1_452": {"example_sentence": "（（円）えん）ざ（ざ）を（を）囲み（かこみ）ましょう。", "example_reading": "えんざをかこみましょう。", "example_meaning_cn": "坐成圆圈吧。", "example_meaning_en": "Let's sit in a circle."},
        "N1_453": {"example_sentence": "（（演）えん）し（し）ゅ（ゅ）つ（つ）し（し）て（て）ください。", "example_reading": "えんしゅつしてください。", "example_meaning_cn": "请导演（演出）。", "example_meaning_en": "Please direct / produce it."},
        "N1_454": {"example_sentence": "（（援）えん）じ（じ）ょ（ょ）し（し）て（て）ください。", "example_reading": "えんじょしてください。", "example_meaning_cn": "请援助。", "example_meaning_en": "Please assist / support."},
        "N1_455": {"example_sentence": "（（演）えん）ぜ（ぜ）つ（つ）し（し）て（て）ください。", "example_reading": "えんぜつしてください。", "example_meaning_cn": "请演说。", "example_meaning_en": "Please give a speech."},
        "N1_456": {"example_sentence": "（（遠）えん）そ（そ）く（く）に（に）行き（いき）ましょう。", "example_reading": "えんそくにいきましょう。", "example_meaning_cn": "去郊游吧。", "example_meaning_en": "Let's go on an excursion."},
        "N1_457": {"example_sentence": "（（園）えん）た（た）い（い）し（し）て（て）ください。", "example_reading": "えんたいしてください。", "example_meaning_cn": "请滞纳（或延滞）。", "example_meaning_en": "Please be in arrears / delay it."},
        "N1_458": {"example_sentence": "（（延）えん）ち（ち）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "えんちょうしてください。", "example_meaning_cn": "请延长。", "example_meaning_en": "Please extend it."},
        "N1_459": {"example_sentence": "（（円）えん）て（て）い（い）を（を）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "えんていをみましょう。", "example_meaning_cn": "看园丁（或亭阁）吧。", "example_meaning_en": "Let's see the gardener / pavilion."},
        "N1_460": {"example_sentence": "（（遠）えん）て（て）ん（ん）し（し）ないで（で）ください。", "example_reading": "えんてんしないでください。", "example_meaning_cn": "请不要（远转或大太阳下）。", "example_meaning_en": "Please don't (revolve / be under the blazing sun)."},
        "N1_461": {"example_sentence": "（（延）えん）ど（ど）お（お）くな（な）事（こと）を（を）し（し）ないで（で）ください。", "example_reading": "えんどおくなことをしないでください。", "example_meaning_cn": "请不要做疏远（延误）的事。", "example_meaning_en": "Please don't do anything that keeps us apart."},
        "N1_462": {"example_sentence": "（（遠）えん）に（に）し（し）て（て）ください。", "example_reading": "えんにしてください。", "example_meaning_cn": "请在远处（或延期）。", "example_meaning_en": "Please keep it distant / postpone it."},
        "N1_463": {"example_sentence": "（（延）えん）ね（ね）ん（ん）し（し）て（て）ください。", "example_reading": "えんねんしてください。", "example_meaning_cn": "请长寿（或延年）。", "example_meaning_en": "Please live long / prolong life."},
        "N1_464": {"example_sentence": "（（延）えん）ぱ（ぱ）ん（ん）し（し）て（て）ください。", "example_reading": "えんぱんしてください。", "example_meaning_cn": "请延期（或搬运）。", "example_meaning_en": "Please delay / transport it."},
        "N1_465": {"example_sentence": "（（遠）えん）ぽ（ぽ）う（う）から（から）来（き）ました。", "example_reading": "えんぽうからきました。", "example_meaning_cn": "从远方来。", "example_meaning_en": "I came from afar."},
        "N1_466": {"example_sentence": "（（円）えん）ま（ま）ん（ん）に（に）解決（かいけつ）し（し）ましょ（しょ）う（う）。", "example_reading": "えんまんにかいけつしましょう。", "example_meaning_cn": "圆满解决吧。", "example_meaning_en": "Let's resolve it amicably."},
        "N1_467": {"example_sentence": "（（遠）えん）り（り）ょ（ょ）し（し）ないで（で）ください。", "example_reading": "えんりょしないでください。", "example_meaning_cn": "请不要客气。", "example_meaning_en": "Please don't hesitate."},
        "N1_468": {"example_sentence": "（（延）えん）り（り）ゅう（ゅう）し（し）ないで（で）ください。", "example_reading": "えんりゅうしないでください。", "example_meaning_cn": "请不要（延迟或停留）。", "example_meaning_en": "Please don't (delay / stay)."},
        "N1_469": {"example_sentence": "（（遠）えん）ろ（ろ）を（を）いとわ（いとわ）ず（ず）来い（こい）！", "example_reading": "えんろをいとわずこい！", "example_meaning_cn": "不怕（不顾）远路过来吧！", "example_meaning_en": "Come regardless of the distance!"},
        "N1_470": {"example_sentence": "（（円）えん）わ（わ）ん（ん）を（を）描い（えがい）て（て）ください。", "example_reading": "えんわんをえがいてください。", "example_meaning_cn": "请划个圆圈（或海湾）。", "example_meaning_en": "Please draw a circle / arc."},
        "N1_471": {"example_sentence": "（（追）お）い（い）かけ（かけ）て（て）ください。", "example_reading": "おいかけてください。", "example_meaning_cn": "请追赶。", "example_meaning_en": "Please chase after them."},
        "N1_472": {"example_sentence": "（（追）お）い（い）こ（こ）し（し）て（て）ください。", "example_reading": "おいこしてください。", "example_meaning_cn": "请超过。", "example_meaning_en": "Please overtake it."},
        "N1_473": {"example_sentence": "（（追）お）い（い）さ（さ）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "おいさらわないでください。", "example_meaning_cn": "请不要衰老。", "example_meaning_en": "Please don't grow old and decrepit."},
        "N1_474": {"example_sentence": "（（追）お）い（い）だ（だ）し（し）て（て）ください。", "example_reading": "おいだしてください。", "example_meaning_cn": "请赶出去。", "example_meaning_en": "Please kick them out."},
        "N1_475": {"example_sentence": "（（追）お）い（い）つ（つ）い（い）て（て）ください。", "example_reading": "おいついてください。", "example_meaning_cn": "请赶上。", "example_meaning_en": "Please catch up."},
        "N1_476": {"example_sentence": "（（追）お）い（い）は（は）ら（ら）っ（っ）て（て）ください。", "example_reading": "おいはらってください。", "example_meaning_cn": "请驱逐出去。", "example_meaning_en": "Please drive them away."},
        "N1_477": {"example_sentence": "（（追）お）い（い）ま（ま）く（く）っ（っ）て（て）ください。", "example_reading": "おいまくってください。", "example_meaning_cn": "请穷追猛打。", "example_meaning_en": "Please press them hard / keep chasing."},
        "N1_478": {"example_sentence": "（（追）お）い（い）ま（ま）わ（わ）さ（さ）ないで（で）ください。", "example_reading": "おいまわさないでください。", "example_meaning_cn": "请不要乱赶（或追逐）。", "example_meaning_en": "Please don't chase them around."},
        "N1_479": {"example_sentence": "（（王）お）う（う）に（に）なり（なり）たい（たい）です。", "example_reading": "おうになりたいです。", "example_meaning_cn": "想当国王。", "example_meaning_en": "I want to be a king."},
        "N1_480": {"example_sentence": "（（往）お）う（う）い（い）し（し）ないで（で）ください。", "example_reading": "おういしないでください。", "example_meaning_cn": "请不要（归顺或去来）。", "example_meaning_en": "Please don't (submit / go and come)."},
        "N1_481": {"example_sentence": "（（謳）おう）か（か）し（し）ましょう。", "example_reading": "おうかしましょう。", "example_meaning_cn": "讴歌（尽情享受）吧。", "example_meaning_en": "Let's enjoy / celebrate to the full."},
        "N1_482": {"example_sentence": "（（黄）おう）か（か）に（に）し（し）ないで（で）ください。", "example_reading": "おうかにしないでください。", "example_meaning_cn": "请不要变黄（黄化）。", "example_meaning_en": "Please don't turn it yellow."},
        "N1_483": {"example_sentence": "（（応）おう）き（き）ゅ（ゅ）う（う）し（し）ょ（ょ）ち（ち）を（を）し（し）て（て）ください。", "example_reading": "おうきゅうしょちをしてください。", "example_meaning_cn": "请进行应急处置。", "example_meaning_en": "Please perform emergency first aid."},
        "N1_484": {"example_sentence": "（（往）おう）こ（こ）を（を）偲び（しのび）ましょう。", "example_reading": "おうこをしのびましょう。", "example_meaning_cn": "缅怀往昔（往古）吧。", "example_meaning_en": "Let's reflect on the ancient past."},
        "N1_485": {"example_sentence": "（（黄）おう）ご（ご）ん（ん）の（の）輝き（かがやき）です。", "example_reading": "おうごんのかがやきです。", "example_meaning_cn": "黄金的光辉。", "example_meaning_en": "It's the glitter of gold."},
        "N1_486": {"example_sentence": "（（応）おう）ざ（ざ）し（し）ないで（で）ください。", "example_reading": "おうざしないでください。", "example_meaning_cn": "请不要（坐在那或应对）。", "example_meaning_en": "Please don't (sit there / respond)."},
        "N1_487": {"example_sentence": "（（応）おう）じ（じ）て（て）ください。", "example_reading": "おうじてください。", "example_meaning_cn": "请响应（配合）。", "example_meaning_en": "Please respond / comply with it."},
        "N1_488": {"example_sentence": "（（欧）おう）し（し）ゅう（ゅう）を（を）旅（たび）し（し）ましょう。", "example_reading": "おうしゅうをたびしましょう。", "example_meaning_cn": "去欧洲旅行吧。", "example_meaning_en": "Let's travel around Europe."},
        "N1_489": {"example_sentence": "（（往）おう）し（し）ょ（ょ）し（し）ないで（で）ください。", "example_reading": "おうしょしないでください。", "example_meaning_cn": "请不要（去信或往事）。", "example_meaning_en": "Please don't (write a letter / dwell on the past)."},
        "N1_490": {"example_sentence": "（（応）おう）せ（せ）い（い）な（な）好奇心（こうきしん）です。", "example_reading": "おうせいなこうきしんです。", "example_meaning_cn": "旺盛的好奇心。", "example_meaning_en": "I have an exuberant curiosity."},
        "N1_491": {"example_sentence": "（（応）おう）せ（せ）ん（ん）し（し）て（て）ください。", "example_reading": "おうせんしてください。", "example_meaning_cn": "请应战（返击）。", "example_meaning_en": "Please fight back / respond to the challenge."},
        "N1_492": {"example_sentence": "（（応）おう）たい（たい）し（し）て（て）ください。", "example_reading": "おうたいしてください。", "example_meaning_cn": "请接待（应对）。", "example_meaning_en": "Please receive / deal with them."},
        "N1_493": {"example_sentence": "（（横）おう）だ（だ）ん（ん）し（し）て（て）ください。", "example_reading": "おうだんしてください。", "example_meaning_cn": "请横断（横穿）。", "example_meaning_en": "Please cross it."},
        "N1_494": {"example_sentence": "（（黄）おう）ど（ど）に（に）し（し）ないで（で）ください。", "example_reading": "おうどにしないでください。", "example_meaning_cn": "请不要弄成黄色（或王土）。", "example_meaning_en": "Please don't turn it yellow / king's territory."},
        "N1_495": {"example_sentence": "（（横）おう）ふ（ふ）う（う）な（な）態度（たいど）です。", "example_reading": "おうふうなたいどです。", "example_meaning_cn": "傲慢（横暴）的态度。", "example_meaning_en": "An overbearing / arrogant attitude."},
        "N1_496": {"example_sentence": "（（往）おう）ふ（ふ）く（く）し（し）て（て）ください。", "example_reading": "おうふくしてください。", "example_meaning_cn": "请往返。", "example_meaning_en": "Please go and return / round trip."},
        "N1_497": {"example_sentence": "（（欧）おう）べ（べ）い（い）を（を）見習い（みならい）ましょう。", "example_reading": "おうべいをみならいましょう。", "example_meaning_cn": "学习欧美吧。", "example_meaning_en": "Let's learn from the West / Europe and America."},
        "N1_498": {"example_sentence": "（（横）おう）ぼ（ぼ）う（う）し（し）ないで（で）ください。", "example_reading": "おうぼうしないでください。", "example_meaning_cn": "请不要横行霸道。", "example_meaning_en": "Please don't be tyrannical."},
        "N1_499": {"example_sentence": "（（応）おう）ぼ（ぼ）し（し）て（て）ください。", "example_reading": "おうぼしてください。", "example_meaning_cn": "请应聘（报名）。", "example_meaning_en": "Please apply / subscribe for it."},
        "N1_500": {"example_sentence": "（（王）おう）よ（よ）う（う）に（に）なり（なり）たい（たい）です。", "example_reading": "おうようになりたいです。", "example_meaning_cn": "想成就王业（或应用）。", "example_meaning_en": "I want to achieve a royal work / apply it."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_500.")

if __name__ == "__main__":
    main()
