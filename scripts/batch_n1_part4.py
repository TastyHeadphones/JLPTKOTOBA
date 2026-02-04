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
        "N1_301": {"example_sentence": "（（祝）いわ）い（い）を（を）し（し）ましょう。", "example_reading": "いわいをしましょう。", "example_meaning_cn": "庆祝吧。", "example_meaning_en": "Let's celebrate."},
        "N1_302": {"example_sentence": "（（言）い）わ（わ）せ（せ）て（て）ください。", "example_reading": "いわせててください。", "example_meaning_cn": "请让我说。", "example_meaning_en": "Please let me speak."},
        "N1_303": {"example_sentence": "（（言）い）わ（わ）ず（ず）も（も）が（が）な（な）の（の）事（こと）です。", "example_reading": "いわずもがなのことです。", "example_meaning_cn": "不说也罢（不言而喻）的事。", "example_meaning_en": "It's something better left unsaid."},
        "N1_304": {"example_sentence": "（（言）い）わ（わ）む（む）に（に）話し（はなし）て（て）ください。", "example_reading": "いわむにおなしてください。", "example_meaning_cn": "请详细（或全面）谈话。", "example_meaning_en": "Please speak in detail."},
        "N1_305": {"example_sentence": "（（言）い）わ（わ）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "いわらわないでください。", "example_meaning_cn": "请不要（开口或归咎）。", "example_meaning_en": "Please don't say anything / don't blame me."},
        "N1_306": {"example_sentence": "（（陰）いん）を（を）踏ん（ふん）で（て）ください。", "example_reading": "いんをふんでください。", "example_meaning_cn": "请押韵。", "example_meaning_en": "Please rhyme."},
        "N1_307": {"example_sentence": "（（意）い）ん（ん）が（が）お（お）う（う）ほ（ほ）う（う）です。", "example_reading": "いんがおうほうです。", "example_meaning_cn": "因果报应。", "example_meaning_en": "Karmic retribution / cause and effect."},
        "N1_308": {"example_sentence": "（（隠）いん）き（き）ょ（ょ）し（し）て（て）ください。", "example_reading": "いんきょしてください。", "example_meaning_cn": "请隐居（退休）。", "example_meaning_en": "Please retire from active life / go into seclusion."},
        "N1_309": {"example_sentence": "（（意）い）ん（ん）ぐ（ぐ）を（を）つけ（つけ）ないで（で）ください。", "example_reading": "いんぐをつけないでください。", "example_meaning_cn": "请不要（构陷或暗算的）。", "example_meaning_en": "Please don't trap me / calculate against me."},
        "N1_310": {"example_sentence": "（（陰）いん）け（け）な（な）場所（ばしょ）ですね。", "example_reading": "いんけなばしょですね。", "example_meaning_cn": "真是个阴森（阴沉）的地方呢。", "example_meaning_en": "It's a gloomy / dismal place."},
        "N1_311": {"example_sentence": "（（意）い）ん（ん）げ（げ）ん（ん）を（を）話し（はなし）て（て）ください。", "example_reading": "いんげんをおなしてください。", "example_meaning_cn": "请说明根源。", "example_meaning_en": "Please tell me the cause / origin."},
        "N1_312": {"example_sentence": "（（隠）いん）こ（こ）う（う）し（し）て（て）ください。", "example_reading": "いんこうしてください。", "example_meaning_cn": "请隐匿。", "example_meaning_en": "Please conceal it."},
        "N1_313": {"example_sentence": "（（陰）いん）さ（さ）つ（つ）し（し）ないで（で）ください。", "example_reading": "いんさつしないでください。", "example_meaning_cn": "请不要印（印刷）。", "example_meaning_en": "Please don't print it."},
        "N1_314": {"example_sentence": "（（隠）いん）し（し）ゃ（ゃ）た（た）い（い）を（を）見（み）て（て）ください。", "example_reading": "いんしゃたいをみてください。", "example_meaning_cn": "请看隐者（或影子）。", "example_meaning_en": "Please see the hermit / shadow."},
        "N1_315": {"example_sentence": "（（意）い）ん（ん）し（し）ゅ（ゅ）を（を）避け（さけ）ましょう。", "example_reading": "いんしゅをさけましょう。", "example_meaning_cn": "戒酒（避开饮酒）吧。", "example_meaning_en": "Let's avoid drinking."},
        "N1_316": {"example_sentence": "（（意）い）ん（ん）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "いんぜんとしています。", "example_meaning_cn": "隐然（潜伏）着。", "example_meaning_en": "It's latent / implicit."},
        "N1_317": {"example_sentence": "（（飲）いん）そ（そ）く（く）に（に）し（し）て（て）ください。", "example_reading": "いんそくにしてください。", "example_meaning_cn": "请快速饮用。", "example_meaning_en": "Please drink quickly."},
        "N1_318": {"example_sentence": "（（引）いん）た（た）い（い）し（し）て（て）ください。", "example_reading": "いんたいしてください。", "example_meaning_cn": "请引退（退休）。", "example_meaning_en": "Please retire."},
        "N1_319": {"example_sentence": "（（陰）いん）と（と）く（く）を（を）積ん（つん）で（て）ください。", "example_reading": "いんとくをつんでください。", "example_meaning_cn": "请积阴德。", "example_meaning_en": "Please accumulate secret acts of charity."},
        "N1_320": {"example_sentence": "（（隠）いん）ぷ（ぷ）し（し）ないで（で）ください。", "example_reading": "いんぷしないでください。", "example_meaning_cn": "请不要隐灭（或暗杀）。", "example_meaning_en": "Please don't conceal / suppress it."},
        "N1_321": {"example_sentence": "（（陰）いん）め（め）つ（つ）し（し）ないで（で）ください。", "example_reading": "いんめつしないでください。", "example_meaning_cn": "请不要灭迹。", "example_meaning_en": "Please don't destroy evidence."},
        "N1_322": {"example_sentence": "（（引）いん）よ（よ）う（う）し（し）て（て）ください。", "example_reading": "いんようしてください。", "example_meaning_cn": "请引用。", "example_meaning_en": "Please quote / cite it."},
        "N1_323": {"example_sentence": "（（引）いん）り（り）ょ（ょ）く（く）を（を）感じ（かんじ）ます。", "example_reading": "いんりょくをかんじます。", "example_meaning_cn": "感受到引力（吸引力）。", "example_meaning_en": "I feel the gravity / attraction."},
        "N1_324": {"example_sentence": "（（胃）い）ん（ん）り（り）ょ（ょ）う（う）を（を）控え（ひかえ）ましょう。", "example_reading": "いんりょうをひかえましょう。", "example_meaning_cn": "节制饮酒（或饮料）吧。", "example_meaning_en": "Let's cut back on drinks / beverages."},
        "N1_325": {"example_sentence": "（（植）う）え（え）き（き）を（を）育て（そだて）ましょう。", "example_reading": "うえきをそだてましょう。", "example_meaning_cn": "养植树（盆栽）吧。", "example_meaning_en": "Let's grow garden plants."},
        "N1_326": {"example_sentence": "（（飢）う）え（え）し（し）に（に）し（し）ないで（で）ください。", "example_reading": "うえしにしないでください。", "example_meaning_cn": "请不要饿死。", "example_meaning_en": "Please don't starve to death."},
        "N1_327": {"example_sentence": "（（植）う）え（え）つ（つ）け（け）て（て）ください。", "example_reading": "うえつけてください。", "example_meaning_cn": "请种植（或灌输）。", "example_meaning_en": "Please plant it / instill it."},
        "N1_328": {"example_sentence": "（（上）うえ）の（の）方（ほう）に（に）あり（あり）ます。", "example_reading": "うえのほうにあります。", "example_meaning_cn": "在上面一点的地方。", "example_meaning_en": "It's further up."},
        "N1_329": {"example_sentence": "（（飢）う）え（え）て（て）いますか。", "example_reading": "うえていますか。", "example_meaning_cn": "你在挨饿（或渴望）吗？", "example_meaning_en": "Are you starving / thirsting for something?"},
        "N1_330": {"example_sentence": "（（浮）う）か（か）れ（れ）ないで（で）ください。", "example_reading": "うかれないでください。", "example_meaning_cn": "请不要得意忘形（或漂浮）。", "example_meaning_en": "Please don't get carried away / don't be high-spirited."},
        "N1_331": {"example_sentence": "（（浮）う）か（か）わ（わ）せ（せ）て（て）ください。", "example_reading": "うかわせててください。", "example_meaning_cn": "请让其漂浮。", "example_meaning_en": "Please make it float."},
        "N1_332": {"example_sentence": "（（受）う）か（か）り（り）よ（よ）く（く）答え（こたえ）て（て）ください。", "example_reading": "うかりよくこたえてください。", "example_meaning_cn": "请爽快地（或漫不经心地）回答。", "example_meaning_en": "Please answer readily / carelessly."},
        "N1_333": {"example_sentence": "（（承）う）けたまわ（わ）り（り）ます。", "example_reading": "うけたまわります。", "example_meaning_cn": "我知道了（恭听/承领）。", "example_meaning_en": "I understand / I hear you (humble)."},
        "N1_334": {"example_sentence": "（（受）う）け（け）い（い）れ（れ）て（て）ください。", "example_reading": "うけいれてください。", "example_meaning_cn": "请接受（采纳）。", "example_meaning_en": "Please accept / admit it."},
        "N1_335": {"example_sentence": "（（受）う）け（け）お（お）っ（っ）て（て）ください。", "example_reading": "うけおってください。", "example_meaning_cn": "请承包。", "example_meaning_en": "Please contract for it."},
        "N1_336": {"example_sentence": "（（受）う）け（け）こ（こ）た（た）え（え）を（を）し（し）て（て）ください。", "example_reading": "うけこたえをしてください。", "example_meaning_cn": "请应答。", "example_meaning_en": "Please respond / give an answer."},
        "N1_337": {"example_sentence": "（（受）う）け（け）な（な）が（が）し（し）て（て）ください。", "example_reading": "うけながしてください。", "example_meaning_cn": "请搪塞（或避开）。", "example_meaning_en": "Please parry / ward off."},
        "N1_338": {"example_sentence": "（（受）う）け（け）な（な）い（い）で（で）ください。", "example_reading": "うけないでください。", "example_meaning_cn": "请不要接受（或受欢迎）。", "example_meaning_en": "Please don't receive it / don't be popular."},
        "N1_339": {"example_sentence": "（（受）う）け（け）ば（ば）こ（こ）に（に）入れ（いれ）て（て）ください。", "example_reading": "うけばこにいれてください。", "example_meaning_cn": "请放入收接盒（受箱）。", "example_meaning_en": "Please put it in the receiving box."},
        "N1_340": {"example_sentence": "（（受）う）け（け）も（も）っ（っ）て（て）ください。", "example_reading": "うけもってください。", "example_meaning_cn": "请担任（负责）。", "example_meaning_en": "Please take charge of / be responsible for."},
        "N1_341": {"example_sentence": "（（受）う）け（け）よ（よ）い（い）し（し）ないで（で）ください。", "example_reading": "うけよいしないでください。", "example_meaning_cn": "请不要承包（或做好人）。", "example_meaning_en": "Please don't contract / be too accommodating."},
        "N1_342": {"example_sentence": "（（動）うご）か（か）し（し）が（が）たい（たい）事実（じじつ）です。", "example_reading": "うごかしがたいじじつです。", "example_meaning_cn": "不可动摇的事实。", "example_meaning_en": "It's an unshakeable fact."},
        "N1_343": {"example_sentence": "（（動）うご）か（か）な（な）い（い）で（で）ください。", "example_reading": "うごかないでください。", "example_meaning_cn": "请不要动。", "example_meaning_en": "Please don't move."},
        "N1_344": {"example_sentence": "（（失）う）せ（せ）ろ（ろ）！", "example_reading": "うせろ！", "example_meaning_cn": "滚开（消失）！", "example_meaning_en": "Get lost! / Disappear!"},
        "N1_345": {"example_sentence": "（（右）う）せ（せ）つ（つ）し（し）て（て）ください。", "example_reading": "うせつしてください。", "example_meaning_cn": "请右转。", "example_meaning_en": "Please turn right."},
        "N1_346": {"example_sentence": "（（歌）うた）を（を）歌い（うたい）ましょう。", "example_reading": "うたをうたいましょう。", "example_meaning_cn": "唱歌吧。", "example_meaning_en": "Let's sing a song."},
        "N1_347": {"example_sentence": "（（疑）うたが）わ（わ）しい（しい）点（てん）があり（あり）ます。", "example_reading": "うたがわしいてんがあります。", "example_meaning_cn": "有可疑点。", "example_meaning_en": "There are some doubtful points."},
        "N1_348": {"example_sentence": "（（内）うち）に（に）秘め（ひめ）て（て）ください。", "example_reading": "うちにひめてください。", "example_meaning_cn": "请藏在心里（内在）。", "example_meaning_en": "Please keep it within yourself."},
        "N1_349": {"example_sentence": "（（打）う）ち（ち）あ（あ）け（け）て（て）ください。", "example_reading": "うちあけてください。", "example_meaning_cn": "请坦率说出来。", "example_meaning_en": "Please be frank / open up."},
        "N1_350": {"example_sentence": "（（打）う）ち（ち）あ（あ）げ（げ）ま（ま）しょ（しょ）う（う）。", "example_reading": "うちあげましょう。", "example_meaning_cn": "发射（或举行庆功宴）吧。", "example_meaning_en": "Let's launch / have a wrap party."},
        "N1_351": {"example_sentence": "（（打）う）ち（ち）き（き）っ（っ）て（て）ください。", "example_reading": "うちきってください。", "example_meaning_cn": "请停止（或敲碎）。", "example_meaning_en": "Please discontinue / chop off."},
        "N1_352": {"example_sentence": "（（打）う）ち（ち）け（け）し（し）て（て）ください。", "example_reading": "うちけしてください。", "example_meaning_cn": "请否定（或抵消）。", "example_meaning_en": "Please deny / cancel it out."},
        "N1_353": {"example_sentence": "（（打）う）ち（ち）こ（こ）ん（ん）で（て）ください。", "example_reading": "うちこんでください。", "example_meaning_cn": "请全身心投入（或打入）。", "example_meaning_en": "Please devote yourself / drive it in."},
        "N1_354": {"example_sentence": "（（内）うち）わ（わ）の（の）話（はなし）です。", "example_reading": "うちわのはなしです。", "example_meaning_cn": "内部的话（或圈子里的）。", "example_meaning_en": "It's an inside / private story."},
        "N1_355": {"example_sentence": "（（打）う）ち（ち）わ（わ）け（け）を（を）見（み）せ（せ）て（て）ください。", "example_reading": "うちわけをみせてください。", "example_meaning_cn": "请给我看明细。", "example_meaning_en": "Please show me the breakdown / details."},
        "N1_356": {"example_sentence": "（（空）うつ）お（お）な（な）気持ち（きもち）です。", "example_reading": "うつおなきもちです。", "example_meaning_cn": "空虚（虚幻）的心情。", "example_meaning_en": "I feel empty / hollow."},
        "N1_357": {"example_sentence": "（（討）う）ち（ち）と（と）っ（っ）て（て）ください。", "example_reading": "うちとってください。", "example_meaning_cn": "请击毙（或讨取）。", "example_meaning_en": "Please destroy / slay the enemy."},
        "N1_358": {"example_sentence": "（（討）う）ち（ち）は（は）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "うちはらわないでください。", "example_meaning_cn": "请不要（击退或驱散）。", "example_meaning_en": "Please don't (beat off / disperse)."},
        "N1_359": {"example_sentence": "（（討）う）ち（ち）ふ（ふ）せ（せ）て（て）ください。", "example_reading": "うちふせてください。", "example_meaning_cn": "请击倒（或俯卧）。", "example_meaning_en": "Please knock down / lie down face down."},
        "N1_360": {"example_sentence": "（（討）う）ち（ち）ほ（ほ）ろ（ろ）ぼ（ぼ）し（し）て（て）ください。", "example_reading": "うちほろぼしてください。", "example_meaning_cn": "请歼灭。", "example_meaning_en": "Please annihilate / destroy them."},
        "N1_361": {"example_sentence": "（（討）う）ち（ち）ま（ま）か（か）せ（せ）て（て）ください。", "example_reading": "うちまかせてください。", "example_meaning_cn": "请将其完全打败。", "example_meaning_en": "Please completely defeat / trounce them."},
        "N1_362": {"example_sentence": "（（討）う）ち（ち）も（も）ら（ら）さ（さ）ないで（で）ください。", "example_reading": "うちもらさないでください。", "example_meaning_cn": "请不要漏掉（或免于被杀）。", "example_meaning_en": "Please don't let anyone escape / omit anything."},
        "N1_363": {"example_sentence": "（（言）う）っ（っ）た（た）え（え）て（て）ください。", "example_reading": "うったえてください。", "example_meaning_cn": "请起诉（或诉苦）。", "example_meaning_en": "Please sue / complain about it."},
        "N1_364": {"example_sentence": "（（写）うつ）し（し）を（を）取っ（とっ）て（て）ください。", "example_reading": "うつしをとってください。", "example_meaning_cn": "请复印一份。", "example_meaning_en": "Please take a copy."},
        "N1_365": {"example_sentence": "（（写）うつ）し（し）だ（だ）し（し）て（て）ください。", "example_reading": "うつしだしてください。", "example_meaning_cn": "请放映出来（或勾勒出来）。", "example_meaning_en": "Please project / depict it."},
        "N1_366": {"example_sentence": "（（写）うつ）っ（っ）て（て）いますか。", "example_reading": "うつっていますか。", "example_meaning_cn": "拍下来了吗？（或移动/传染）。", "example_meaning_en": "Is it being filmed? / Has it moved?"},
        "N1_367": {"example_sentence": "（（虚）うつ）ろ（ろ）な（な）目（め）です。", "example_reading": "うつろなめです。", "example_meaning_cn": "空洞的眼神。", "example_meaning_en": "Languid / vacant eyes."},
        "N1_368": {"example_sentence": "（（器）うつわ）を（を）選ん（えらん）で（て）ください。", "example_reading": "うつわをえらんでください。", "example_meaning_cn": "请选择器皿（或人才）。", "example_meaning_en": "Please choose the vessel / person of talent."},
        "N1_369": {"example_sentence": "（（空）うつ）わ（わ）な（な）日々（ひび）を（を）避け（さけ）ましょう。", "example_reading": "うつわなひびわさけましょう。", "example_meaning_cn": "避开空虚的日子吧。", "example_meaning_en": "Let's avoid empty days."},
        "N1_370": {"example_sentence": "（（空）うつ）わ（わ）ら（ら）ないで（で）ください。", "example_reading": "うつわらないでください。", "example_meaning_cn": "请不要（虚晃或改变）。", "example_meaning_en": "Please don't (be hollow / change)."},
        "N1_371": {"example_sentence": "（（現）うつ）ん（ん）で（て）ください。", "example_reading": "うつんでください。", "example_meaning_cn": "请现身（或转变）。", "example_meaning_en": "Please reveal yourself / transform."},
        "N1_372": {"example_sentence": "（（腕）うで）を（を）磨い（みがい）て（て）ください。", "example_reading": "うでをみがいてください。", "example_meaning_cn": "请磨练技艺（手腕）。", "example_meaning_en": "Please polish your skills."},
        "N1_373": {"example_sentence": "（（腕）うで）き（き）き（き）の（の）大工（だいく）です。", "example_reading": "うでききのだいくです。", "example_meaning_cn": "技术高明的木匠。", "example_meaning_en": "He's a highly skilled carpenter."},
        "N1_374": {"example_sentence": "（（腕）うで）ど（ど）け（け）い（い）を（を）し（し）て（て）ください。", "example_reading": "うでどけいをしてください。", "example_meaning_cn": "请带上手表。", "example_meaning_en": "Please wear your wristwatch."},
        "N1_375": {"example_sentence": "（（腕）うで）ま（ま）え（え）を（を）見せ（みせ）て（て）ください。", "example_reading": "うでまえをみせてください。", "example_meaning_cn": "请大显身手。", "example_meaning_en": "Please show me your ability."},
        "N1_376": {"example_sentence": "（（腕）うで）わ（わ）を（を）はめ（はめ）て（て）ください。", "example_reading": "うでわをはめてください。", "example_meaning_cn": "请戴上手镯。", "example_meaning_en": "Please put on the bracelet."},
        "N1_377": {"example_sentence": "（（促）うなが）し（し）て（て）ください。", "example_reading": "うながしてください。", "example_meaning_cn": "请促使（催促）。", "example_meaning_en": "Please urge / stimulate it."},
        "N1_378": {"example_sentence": "（（唸）うな）ら（ら）ないで（で）ください。", "example_reading": "うならないでください。", "example_meaning_cn": "请不要呻吟（或吼叫）。", "example_meaning_en": "Please don't groan / roar."},
        "N1_379": {"example_sentence": "（（頷）うなず）い（い）て（て）ください。", "example_reading": "うなずいてください。", "example_meaning_cn": "请点头（同意）。", "example_meaning_en": "Please nod."},
        "N1_380": {"example_sentence": "（（唸）うな）り（り）声（ごえ）が（が）聞こえ（きこえ）ます。", "example_reading": "うなりごえがきこえます。", "example_meaning_cn": "能听到呻吟声（吼声）。", "example_meaning_en": "I can hear a groan / roar."},
        "N1_381": {"example_sentence": "（（自）うぬ）ぼ（ぼ）れ（れ）ないで（で）ください。", "example_reading": "うぬぼれないでください。", "example_meaning_cn": "请不要自满（骄傲）。", "example_meaning_en": "Please don't be conceited."},
        "N1_382": {"example_sentence": "（（奪）うば）わ（わ）ないで（で）ください。", "example_reading": "うばわないでください。", "example_meaning_cn": "请不要夺走。", "example_meaning_en": "Please don't take it away / rob it."},
        "N1_383": {"example_sentence": "（（生）う）ま（ま）れ（れ）た（た）ての（の）赤ん坊（あかんぼう）です。", "example_reading": "うまれたてのあかんぼうです。", "example_meaning_cn": "刚出生的婴孩。", "example_meaning_en": "It's a newborn baby."},
        "N1_384": {"example_sentence": "（（生）う）ま（ま）れ（れ）つ（つ）き（き）の（の）才能（さいのう）です。", "example_reading": "うまれつきのさいのうです。", "example_meaning_cn": "天生的才能。", "example_meaning_en": "It's an innate / natural talent."},
        "N1_385": {"example_sentence": "（（産）う）み（み）だ（だ）し（し）て（て）ください。", "example_reading": "うみだしてください。", "example_meaning_cn": "请生产出（或独创）。", "example_meaning_en": "Please bring forth / create it."},
        "N1_386": {"example_sentence": "（（海）うみ）べ（べ）を（を）散歩（さんぽ）し（し）ましょう。", "example_reading": "うみべをさんぽしましょう。", "example_meaning_cn": "在海边散步吧。", "example_meaning_en": "Let's take a walk by the sea."},
        "N1_387": {"example_sentence": "（（埋）う）め（め）あ（あ）お（お）ず（ず）し（し）ないで（で）ください。", "example_reading": "うめあおずしないでください。", "example_meaning_cn": "请不要（掩埋或纠缠）。", "example_meaning_en": "Please don't (bury / pester)."},
        "N1_388": {"example_sentence": "（（埋）う）め（め）た（た）て（て）を（を）し（し）て（て）ください。", "example_reading": "うめたてをしてください。", "example_meaning_cn": "请填拓（填海）。", "example_meaning_en": "Please reclaim the land / fill it in."},
        "N1_389": {"example_sentence": "（（裏）うら）が（が）え（え）し（し）て（て）ください。", "example_reading": "うらがえしてください。", "example_meaning_cn": "请里外翻过来。", "example_meaning_en": "Please turn it inside out."},
        "N1_390": {"example_sentence": "（（裏）うら）ぎ（ぎ）ら（ら）ないで（で）ください。", "example_reading": "うらぎらないでください。", "example_meaning_cn": "请不要背叛。", "example_meaning_en": "Please don't betray me."},
        "N1_391": {"example_sentence": "（（裏）うら）き（き）っ（っ）て（て）ください。", "example_reading": "うらきってください。", "example_meaning_cn": "请切断后路（或里切）。", "example_meaning_en": "Please cut off the rear / undercut it."},
        "N1_392": {"example_sentence": "（（裏）うら）こ（こ）さ（さ）ないで（で）ください。", "example_reading": "うらこさないでください。", "example_meaning_cn": "请不要（绕道或欺骗）。", "example_meaning_en": "Please don't (go around / deceive)."},
        "N1_393": {"example_sentence": "（（恨）うら）ま（ま）ないで（で）ください。", "example_reading": "うらまないでください。", "example_meaning_cn": "请不要怨恨。", "example_meaning_en": "Please don't resent / begrudge me."},
        "N1_394": {"example_sentence": "（（裏）うら）ま（ま）わ（わ）ら（ら）ないで（で）ください。", "example_reading": "うらまわらないでください。", "example_meaning_cn": "请不要绕到后面。", "example_meaning_en": "Please don't go around to the back."},
        "N1_395": {"example_sentence": "（（羨）うら）ま（ま）し（し）い（い）です。", "example_reading": "うらましいです。", "example_meaning_cn": "真羡慕。", "example_meaning_en": "I'm envious / jealous."},
        "N1_396": {"example_sentence": "（（恨）うら）み（み）を（を）晴らし（はらし）て（て）ください。", "example_reading": "うらみをはらしてください。", "example_meaning_cn": "请解恨。", "example_meaning_en": "Please avenge your grudge."},
        "N1_397": {"example_sentence": "（（裏）うら）め（め）し（し）い（い）目（め）で（で）見（み）ないで（で）ください。", "example_reading": "うらめしいめでみないでください。", "example_meaning_cn": "请不要用怨恨的眼神看我。", "example_meaning_en": "Please don't look at me with resentful eyes."},
        "N1_398": {"example_sentence": "（（彩）うら）ら（ら）か（か）な（な）日（ひ）ですね。", "example_reading": "うららかなひですね。", "example_meaning_cn": "真是明媚（晴朗）的一天呢。", "example_meaning_en": "It's a bright / sunny day."},
        "N1_399": {"example_sentence": "（（売）う）り（り）き（き）ら（ら）な（な）い（い）で（で）ください。", "example_reading": "うりきらないでください。", "example_meaning_cn": "请不要卖光（或坚持卖）。", "example_meaning_en": "Please don't sell out / don't insist on selling."},
        "N1_400": {"example_sentence": "（（売）う）り（り）さ（さ）ば（ば）い（い）て（て）ください。", "example_reading": "うりさばいてください。", "example_meaning_cn": "请销售（脱手）。", "example_meaning_en": "Please sell off / dispose of it."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_400.")

if __name__ == "__main__":
    main()
