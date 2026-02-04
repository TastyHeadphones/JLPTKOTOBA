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
        "N1_0": {"example_sentence": "（（相）あい）か（か）わ（わ）ら（ら）ず（ず）元気（げんき）ですね。", "example_reading": "あいかわらずげんきですね。", "example_meaning_cn": "还是老样子（依然）精神头十足呢。", "example_meaning_en": "You're as energetic as ever."},
        "N1_1": {"example_sentence": "（（愛）あい）き（き）ょ（ょ）う（う）を（を）振りまき（ふりまき）ましょう。", "example_reading": "あいきょうをふりまきましょう。", "example_meaning_cn": "撒（展示）娇（可爱）吧。", "example_meaning_en": "Let's spread some charm."},
        "N1_2": {"example_sentence": "（（哀）あい）こ（こ）を（を）禁じ（きんじ）得（え）ません。", "example_reading": "あいこをきんじえません。", "example_meaning_cn": "禁不住感到哀怜（悲哀）。", "example_meaning_en": "I can't help feeling sorrow."},
        "N1_3": {"example_sentence": "（（挨）あい）さ（さ）つ（つ）を（を）し（し）て（て）ください。", "example_reading": "あいさつをしてください。", "example_meaning_cn": "请打招呼。", "example_meaning_en": "Please greet (someone)."},
        "N1_4": {"example_sentence": "（（相）あい）じ（じ）ょ（ょ）う（う）を（を）注い（そそい）で（て）ください。", "example_reading": "あいじょうをそそいでください。", "example_meaning_cn": "请倾注爱情。", "example_meaning_en": "Please pour in your affection."},
        "N1_5": {"example_sentence": "（（合）あい）ず（ず）を（を）出し（だし）て（て）ください。", "example_reading": "あいずをだしてください。", "example_meaning_cn": "请发信号。", "example_meaning_en": "Please give a signal."},
        "N1_6": {"example_sentence": "（（愛）あい）せ（せ）い（い）し（し）て（て）ください。", "example_reading": "あいせいしてください。", "example_meaning_cn": "请爱静（喜爱）。", "example_meaning_en": "Please cherish it (or the quiet)."},
        "N1_7": {"example_sentence": "（（相）あい）そ（そ）が（が）いい（いい）ですね。", "example_reading": "あいそがいいですね。", "example_meaning_cn": "待人接物（和蔼）真好呢。", "example_meaning_en": "He/She is very sociable/affable."},
        "N1_8": {"example_sentence": "（（間）あいだ）を（を）空け（あけ）て（て）ください。", "example_reading": "あいだをあけてください。", "example_meaning_cn": "请留出间隔（时间）。", "example_meaning_en": "Please leave a space/interval."},
        "N1_9": {"example_sentence": "（（対）あい）た（た）い（い）し（し）て（て）ください。", "example_reading": "あいたいしてください。", "example_meaning_cn": "请面对面（对峙）。", "example_meaning_en": "Please face each other."},
        "N1_10": {"example_sentence": "（（対）あい）て（て）を（を）尊重（そんちょう）し（し）てください。", "example_reading": "あいてをそんちょうしてください。", "example_meaning_cn": "请尊重对方。", "example_meaning_en": "Please respect the other party."},
        "N1_11": {"example_sentence": "（（愛）あい）ど（ど）く（く）し（し）て（て）ください。", "example_reading": "あいどくしてください。", "example_meaning_cn": "请爱读（经常阅读）。", "example_meaning_en": "Please enjoy reading it regularly."},
        "N1_12": {"example_sentence": "（（生）あ）い（い）に（に）く（く）の（の）雨（あめ）ですね。", "example_reading": "あいにくのあめですね。", "example_meaning_cn": "很遗憾（不凑巧）下雨了呢。", "example_meaning_en": "Unfortunately, it's raining."},
        "N1_13": {"example_sentence": "（（曖）あい）ま（ま）い（い）な（な）態度（たいど）です。", "example_reading": "あいまいなたいどです。", "example_meaning_cn": "暧昧（含糊）的态度。", "example_meaning_en": "An ambiguous attitude."},
        "N1_14": {"example_sentence": "（（会）あ）い（い）ま（ま）み（み）え（え）て（て）ください。", "example_reading": "あいみみえてください。", "example_meaning_cn": "请相见（会面）。", "example_meaning_en": "Please meet with each other."},
        "N1_15": {"example_sentence": "（（愛）あい）よ（よ）う（う）し（し）て（て）ください。", "example_reading": "あいようしてください。", "example_meaning_cn": "请爱用（惯用）。", "example_meaning_en": "Please use it regularly."},
        "N1_16": {"example_sentence": "（（遭）あ）い（い）わ（わ）ず（ず）に（に）済み（すみ）まし（し）た。", "example_reading": "あいわずになみました。", "example_meaning_cn": "终于没遇上（不期而遇）。", "example_meaning_en": "I managed to avoid meeting (the misfortune)."},
        "N1_17": {"example_sentence": "（（遭）あ）う（う）のを（を）避け（さけ）られ（られ）ませ（ませ）ん。", "example_reading": "あうのわさけられません。", "example_meaning_cn": "无法避免遇见（遭遇）。", "example_meaning_en": "Encounters (misfortunes) are unavoidable."},
        "N1_18": {"example_sentence": "（（煽）あお）ら（ら）ないで（で）ください。", "example_reading": "あおらないでください。", "example_meaning_cn": "请不要扇动（挑衅）。", "example_meaning_en": "Please don't instigate/provoke."},
        "N1_19": {"example_sentence": "（（仰）あお）ぎ（ぎ）見（み）て（て）ください。", "example_reading": "あおぎみてください。", "example_meaning_cn": "请仰望（尊敬）。", "example_meaning_en": "Please look up (with respect)."},
        "N1_20": {"example_sentence": "（（赤）あか）ら（ら）め（め）て（て）ください。", "example_reading": "あからめてください。", "example_meaning_cn": "请脸红（变红）。", "example_meaning_en": "Please blush (turn red)."},
        "N1_21": {"example_sentence": "（（明）あか）る（る）い（い）方（ほう）へ（へ）行き（いき）ましょう。", "example_reading": "あかるいほうえいきましょう。", "example_meaning_cn": "向着明亮的地方走吧。", "example_meaning_en": "Let's go towards the light."},
        "N1_22": {"example_sentence": "（（明）あか）ら（ら）か（か）に（に）し（し）て（て）ください。", "example_reading": "あきらかにしてください。", "example_meaning_cn": "请弄清楚（明确）。", "example_meaning_en": "Please clarify it."},
        "N1_23": {"example_sentence": "（（諦）あきら）め（め）ない（ない）で（で）ください。", "example_reading": "あきらめないでください。", "example_meaning_cn": "请不要放弃。", "example_meaning_en": "Please don't give up."},
        "N1_24": {"example_sentence": "（（飽）あき）ら（ら）せ（せ）ないで（で）ください。", "example_reading": "あきらせないでください。", "example_meaning_cn": "请不要让我厌烦。", "example_meaning_en": "Please don't make me lose interest."},
        "N1_25": {"example_sentence": "（（呆）あき）れ（れ）て（て）しまい（しまい）まし（し）た。", "example_reading": "あきれてしまいました。", "example_meaning_cn": "真让人吃惊（愕然）。", "example_meaning_en": "I was amazed/appalled."},
        "N1_26": {"example_sentence": "（（悪）あく）意（い）は（は）あり（あり）ません。", "example_reading": "あくいわありません。", "example_meaning_cn": "没有恶意。", "example_meaning_en": "I have no ill will."},
        "N1_27": {"example_sentence": "（（握）あく）し（し）ゅ（ゅ）し（し）ましょう。", "example_reading": "あくしゅしましょう。", "example_meaning_cn": "握手吧。", "example_meaning_en": "Let's shake hands."},
        "N1_28": {"example_sentence": "（（悪）あく）じ（じ）ょ（ょ）う（う）け（け）ん（ん）です。", "example_reading": "あくじょうけんです。", "example_meaning_cn": "恶劣条件。", "example_meaning_en": "It's a bad condition."},
        "N1_29": {"example_sentence": "（（顎）あご）を（を）出し（だし）て（て）ください。", "example_reading": "あごをだしてください。", "example_meaning_cn": "请挺起下巴（或精疲力竭）。", "example_meaning_en": "Please lift your chin (or be exhausted)."},
        "N1_30": {"example_sentence": "（（憧）あこが）れ（れ）て（て）います。", "example_reading": "あこがれています。", "example_meaning_cn": "很憧憬。", "example_meaning_en": "I long for/admire it."},
        "N1_31": {"example_sentence": "（（朝）あさ）め（め）し（し）を（を）食べ（たべ）ましょう。", "example_reading": "あさめしをたべましょう。", "example_meaning_cn": "吃早饭吧。", "example_meaning_en": "Let's have breakfast."},
        "N1_32": {"example_sentence": "（（欺）あざ）む（む）か（か）ないで（で）ください。", "example_reading": "あざむかないでください。", "example_meaning_cn": "请不要欺骗。", "example_meaning_en": "Please don't deceive me."},
        "N1_33": {"example_sentence": "（（鮮）あざ）や（や）か（か）な（な）色（いろ）です。", "example_reading": "あざやかないろです。", "example_meaning_cn": "鲜艳的颜色。", "example_meaning_en": "It's a vivid color."},
        "N1_34": {"example_sentence": "（（嘲）あざ）わ（わ）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "あざわらわないでください。", "example_meaning_cn": "请不要嘲笑。", "example_meaning_en": "Please don't ridicule/sneer at me."},
        "N1_35": {"example_sentence": "（（味）あじ）が（が）あり（あり）ますね。", "example_reading": "あじがありますね。", "example_meaning_cn": "真有味道（韵味）呢。", "example_meaning_en": "It has a nice flavor/character."},
        "N1_36": {"example_sentence": "（（味）あじ）わ（わ）っ（っ）て（て）ください。", "example_reading": "あじわってください。", "example_meaning_cn": "请细细品味。", "example_meaning_en": "Please savor/appreciate it."},
        "N1_37": {"example_sentence": "（（預）あず）か（か）っ（っ）て（て）ください。", "example_reading": "あずかってください。", "example_meaning_cn": "请代为保管。", "example_meaning_en": "Please keep this for me."},
        "N1_38": {"example_sentence": "（（預）あず）け（け）て（て）ください。", "example_reading": "あずけてください。", "example_meaning_cn": "请寄存（或托付）。", "example_meaning_en": "Please deposit/entrust it."},
        "N1_39": {"example_sentence": "（（焦）あせ）ら（ら）ないで（で）ください。", "example_reading": "あせらないでください。", "example_meaning_cn": "请不要焦急。", "example_meaning_en": "Please don't rush/be impatient."},
        "N1_40": {"example_sentence": "（（焦）あせ）っ（っ）て（て）いますか。", "example_reading": "あせっていますか。", "example_meaning_cn": "你在着急吗？", "example_meaning_en": "Are you in a hurry/flustered?"},
        "N1_41": {"example_sentence": "（（値）あたい）し（し）ます。", "example_reading": "あたいします。", "example_meaning_cn": "值得。", "example_meaning_en": "It's worth/deserves it."},
        "N1_42": {"example_sentence": "（（当）あ）た（た）ら（ら）な（な）い（い）で（で）ください。", "example_reading": "あたらないでください。", "example_meaning_cn": "请不要被打中（或迁怒）。", "example_meaning_en": "Please don't be hit/vent your anger."},
        "N1_43": {"example_sentence": "（（当）あ）た（た）り（り）さ（さ）わ（わ）り（り）の（の）ない（ない）話（はなし）です。", "example_reading": "あたりさわりのないはなしです。", "example_meaning_cn": "四平八稳（不碍事）的话。", "example_meaning_en": "It's a harmless/inoffensive story."},
        "N1_44": {"example_sentence": "（（当）あ）た（た）る（る）のを（を）待っ（まっ）て（て）ください。", "example_reading": "あたるのわまってください。", "example_meaning_cn": "请等待中奖（或轮到）。", "example_meaning_en": "Please wait for it to hit/come true."},
        "N1_45": {"example_sentence": "（（扱）あつか）い（い）に（に）気（き）をつけ（つけ）て（て）ください。", "example_reading": "あつかいにきをつけてください。", "example_meaning_cn": "请小心对待（处理）。", "example_meaning_en": "Please handle with care."},
        "N1_46": {"example_sentence": "（（扱）あつか）っ（っ）て（て）ください。", "example_reading": "あつかってください。", "example_meaning_cn": "请处理（或经营）。", "example_meaning_en": "Please deal with/handle it."},
        "N1_47": {"example_sentence": "（（厚）あつ）か（か）ま（ま）し（し）い（い）ですね。", "example_reading": "あつかましいですね。", "example_meaning_cn": "真够厚颜无耻的呢。", "example_meaning_en": "How impudent/cheeky!"},
        "N1_48": {"example_sentence": "（（圧）あっ）く（く）し（し）て（て）ください。", "example_reading": "あっくしてください。", "example_meaning_cn": "请压平（或压缩）。", "example_meaning_en": "Please compress/flatten it."},
        "N1_49": {"example_sentence": "（（呆）あ）っ（っ）け（け）な（な）い（い）最後（さいご）でした。", "example_reading": "あっけないさいごでした。", "example_meaning_cn": "索然无味（太快）的结局。", "example_meaning_en": "It was an abruptly simple/disappointing end."},
        "N1_50": {"example_sentence": "（（圧）あっ）さ（さ）く（く）し（し）て（て）ください。", "example_reading": "あっさくしてください。", "example_meaning_cn": "请压窄（压榨）。", "example_meaning_en": "Please press/squeeze it."},
        "N1_51": {"example_sentence": "（（呆）あ）っ（っ）さ（さ）り（り）し（し）て（て）ください。", "example_reading": "あっさりしてください。", "example_meaning_cn": "请得更淡泊（或干脆）。", "example_meaning_en": "Please be simple/frank."},
        "N1_52": {"example_sentence": "（（圧）あっ）せ（せ）い（い）し（し）ないで（で）ください。", "example_reading": "あっせいしないでください。", "example_meaning_cn": "请不要高压统治。", "example_meaning_en": "Please don't tyrannize/oppress."},
        "N1_53": {"example_sentence": "（（斡）あっ）せ（せ）ん（ん）し（し）て（て）ください。", "example_reading": "あっせんしてください。", "example_meaning_cn": "请斡旋（中间介绍）。", "example_meaning_en": "Please mediate/recommend."},
        "N1_54": {"example_sentence": "（（圧）あっ）た（た）い（い）し（し）て（て）ください。", "example_reading": "あったいしてください。", "example_meaning_cn": "请压服（或压抑）。", "example_meaning_en": "Please suppress/subdue."},
        "N1_55": {"example_sentence": "（（圧）あっ）と（と）う（う）し（し）て（て）ください。", "example_reading": "あっとうしてください。", "example_meaning_cn": "请压倒。", "example_meaning_en": "Please overwhelm."},
        "N1_56": {"example_sentence": "（（圧）あっ）ぱ（ぱ）く（く）し（し）ないで（で）ください。", "example_reading": "あっぱくしないでください。", "example_meaning_cn": "请不要压迫。", "example_meaning_en": "Please don't pressure/oppress."},
        "N1_57": {"example_sentence": "（（当）あ）て（て）に（に）し（し）ないで（で）ください。", "example_reading": "あてにしないでください。", "example_meaning_cn": "请不要指望（指望不上）。", "example_meaning_en": "Please don't count on it."},
        "N1_58": {"example_sentence": "（（当）あ）て（て）字（じ）を（を）使い（つかい）ましょう。", "example_reading": "あてじをつかいましょう。", "example_meaning_cn": "用借字（借用字）吧。", "example_meaning_en": "Let's use a phonetic equivalent (ateji)."},
        "N1_59": {"example_sentence": "（（当）あ）て（て）は（は）め（め）て（て）ください。", "example_reading": "あてはめてください。", "example_meaning_cn": "请套用（应用）。", "example_meaning_en": "Please apply/fit it in."},
        "N1_60": {"example_sentence": "（（当）あ）て（て）は（は）ま（ま）り（り）ますか。", "example_reading": "あてはまりますか。", "example_meaning_cn": "适用吗？", "example_meaning_en": "Does it apply?"},
        "N1_61": {"example_sentence": "（（当）あ）て（て）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "あてるのわてつだってください。", "example_meaning_cn": "请帮我猜（或贴上）。", "example_meaning_en": "Please help me guess/hit it."},
        "N1_62": {"example_sentence": "（（後）あと）を（を）追っ（おっ）て（て）ください。", "example_reading": "あとをおってください。", "example_meaning_cn": "请追随（追踪）。", "example_meaning_en": "Please follow after them."},
        "N1_63": {"example_sentence": "（（跡）あと）を（を）継ぎ（つぎ）ます。", "example_reading": "あとをつぎます。", "example_meaning_cn": "继承家业（或踪迹）。", "example_meaning_en": "I'll succeed (inherited the business/track)."},
        "N1_64": {"example_sentence": "（（後）あと）が（が）き（き）を（を）書い（かい）て（て）ください。", "example_reading": "あとがきをかいてください。", "example_meaning_cn": "请写后记。", "example_meaning_en": "Please write the afterword."},
        "N1_65": {"example_sentence": "（（跡）あと）つぎ（つぎ）に（に）なり（なり）たい（たい）です。", "example_reading": "あとつぎになりたいです。", "example_meaning_cn": "想当继承人。", "example_meaning_en": "I want to be the successor."},
        "N1_66": {"example_sentence": "（（後）あと）ま（ま）わ（わ）し（し）に（に）し（し）て（て）ください。", "example_reading": "あとまわしにしてください。", "example_meaning_cn": "请往后挪。", "example_meaning_en": "Please put it off/defer it."},
        "N1_67": {"example_sentence": "（（貴）あな）た（た）を（を）信じ（しんじ）ます。", "example_reading": "あななをきんじます。", "example_meaning_cn": "相信你（贵方）。", "example_meaning_en": "I believe in you (polite)."},
        "N1_68": {"example_sentence": "（（暴）あば）か（か）ないで（ので）ください。", "example_reading": "あばかないでください。", "example_meaning_cn": "请不要揭露。", "example_meaning_en": "Please don't expose/reveal it."},
        "N1_69": {"example_sentence": "（（暴）あば）れ（れ）ないで（で）ください。", "example_reading": "あばれないでください。", "example_meaning_cn": "请不要胡闹（狂暴）。", "example_meaning_en": "Please don't act violently/riot."},
        "N1_70": {"example_sentence": "（（浴）あ）び（び）せ（せ）かけ（かけ）ないで（で）ください。", "example_reading": "あびせかけないでください。", "example_meaning_cn": "请不要泼洒（或纠缠）。", "example_meaning_en": "Please don't pour/shower me with it."},
        "N1_71": {"example_sentence": "（（浴）あ）び（び）て（て）ください。", "example_reading": "あびてください。", "example_meaning_cn": "请淋浴（或晒太阳）。", "example_meaning_en": "Please take a shower/bathe in it."},
        "N1_72": {"example_sentence": "（（危）あぶ）な（な）げ（げ）の（の）ない（ない）戦い（たたかい）でした。", "example_reading": "あぶなげのないたたかいでした。", "example_meaning_cn": "这是一场十拿九稳（不危险）的战斗。", "example_meaning_en": "It was a secure/steady battle."},
        "N1_73": {"example_sentence": "（（油）あぶら）を（を）引い（ひい）て（て）ください。", "example_reading": "あぶらをひいてください。", "example_meaning_cn": "请抹油（或涂油）。", "example_meaning_en": "Please apply oil."},
        "N1_74": {"example_sentence": "（（脂）あぶら）が（が）乗っ（のっ）て（て）いますね。", "example_reading": "あぶらがのっていますね。", "example_meaning_cn": "正当令（或起劲/多脂）呢。", "example_meaning_en": "He's at his peak/it's rich in fat."},
        "N1_75": {"example_sentence": "（（焙）あぶ）っ（っ）て（て）食べ（たべ）ましょう。", "example_reading": "あぶってたべましょう。", "example_meaning_cn": "烤一烤再吃吧。", "example_meaning_en": "Let's toast/grill it before eating."},
        "N1_76": {"example_sentence": "（（甘）あま）え（え）ないで（で）ください。", "example_reading": "あまえないでください。", "example_meaning_cn": "请不要撒娇。", "example_meaning_en": "Please don't depend on common kindness/be spoiled."},
        "N1_77": {"example_sentence": "（（甘）あま）え（え）か（か）し（し）すぎ（すぎ）です。", "example_reading": "あまえかしすぎです。", "example_meaning_cn": "太娇生惯养了。", "example_meaning_en": "You're spoiling them too much."},
        "N1_78": {"example_sentence": "（（雨）あま）ぐ（ぐ）を（を）持っ（もっ）て（て）き（き）ましたか。", "example_reading": "あまぐをもてきましたか。", "example_meaning_cn": "带雨具了吗？", "example_meaning_en": "Did you bring rain gear?"},
        "N1_79": {"example_sentence": "（（甘）あま）く（く）見（み）ないで（で）ください。", "example_reading": "あまくみないでください。", "example_meaning_cn": "请不要小看（太天真）。", "example_meaning_en": "Please don't underestimate/be naive."},
        "N1_80": {"example_sentence": "（（雨）あま）や（や）ど（ど）り（り）を（を）し（し）ましょう。", "example_reading": "あまやどりをしましょう。", "example_meaning_cn": "避雨吧。", "example_meaning_en": "Let's take shelter from the rain."},
        "N1_81": {"example_sentence": "（（余）あま）り（り）に（に）も（も）ひどい（ひどい）です。", "example_reading": "あまりにもひどいです。", "example_meaning_cn": "实在（太）过分了。", "example_meaning_en": "It's far too cruel/bad."},
        "N1_82": {"example_sentence": "（（余）あま）り（り）もの（もの）を（を）もらい（もらい）まし（し）た。", "example_reading": "あまりものをもらいました。", "example_meaning_cn": "领到了剩饭（余物）。", "example_meaning_en": "I received the leftovers."},
        "N1_83": {"example_sentence": "（（編）あ）ん（ん）で（で）ください。", "example_reading": "あんでください。", "example_meaning_cn": "请编织。", "example_meaning_en": "Please knit/weave it."},
        "N1_84": {"example_sentence": "（（怪）あや）し（し）い（い）人（ひと）がい（い）ます。", "example_reading": "あやしいひとがいます。", "example_meaning_cn": "有个可疑的人。", "example_meaning_en": "There's a suspicious person."},
        "N1_85": {"example_sentence": "（（操）あやつ）っ（っ）て（て）ください。", "example_reading": "あやつってください。", "example_meaning_cn": "请操纵。", "example_meaning_en": "Please manipulate/control it."},
        "N1_86": {"example_sentence": "（（危）あや）ぶ（ぶ）ま（ま）れ（れ）て（て）います。", "example_reading": "あやぶまれています。", "example_meaning_cn": "令人担忧（危险）。", "example_meaning_en": "It's being feared/doubted."},
        "N1_87": {"example_sentence": "（（危）あや）う（う）い（い）ところ（ところ）でした。", "example_reading": "あやういところでした。", "example_meaning_cn": "太险了（危险）。", "example_meaning_en": "That was close/was in danger."},
        "N1_88": {"example_sentence": "（（謝）あやま）っ（っ）て（て）ください。", "example_reading": "あやまってください。", "example_meaning_cn": "请道歉。", "example_meaning_en": "Please apologize."},
        "N1_89": {"example_sentence": "（（誤）あやま）ち（ち）を（を）認め（みとめ）てください。", "example_reading": "あやまちをみとめてください。", "example_meaning_cn": "请承认错误。", "example_meaning_en": "Please admit your mistake."},
        "N1_90": {"example_sentence": "（（歩）あゆ）み（み）を（を）止め（とめ）ないで（で）ください。", "example_reading": "あゆみをとめないでください。", "example_meaning_cn": "请不要停止脚步。", "example_meaning_en": "Please don't stop walking/progressing."},
        "N1_91": {"example_sentence": "（（歩）あゆ）ん（ん）で（て）ください。", "example_reading": "あゆんでください。", "example_meaning_cn": "请走下去（迈步）。", "example_meaning_en": "Please walk/proceed."},
        "N1_92": {"example_sentence": "（（洗）あら）い（い）ざ（ざ）ら（ら）い（い）話し（はなし）て（て）ください。", "example_reading": "あらいざらいおなしてください。", "example_meaning_cn": "请统统（全部）说出来。", "example_meaning_en": "Please tell me everything."},
        "N1_93": {"example_sentence": "（（新）あら）た（た）に（に）始め（はじめ）ましょう。", "example_reading": "あらたにはじめましょう。", "example_meaning_cn": "重新开始吧。", "example_meaning_en": "Let's start anew."},
        "N1_94": {"example_sentence": "（（改）あらた）まっ（まっ）た（た）態度（たいど）です。", "example_reading": "あらたまったたいどです。", "example_meaning_cn": "郑重（正式）的态度。", "example_meaning_en": "A formal/serious attitude."},
        "N1_95": {"example_sentence": "（（改）あらた）め（め）て（て）来（き）ます。", "example_reading": "あらためてきます。", "example_meaning_cn": "改天再来。", "example_meaning_en": "I'll come again another time."},
        "N1_96": {"example_sentence": "（（洗）あら）っ（っ）て（て）ください。", "example_reading": "あらってください。", "example_meaning_cn": "请洗洗。", "example_meaning_en": "Please wash it."},
        "N1_97": {"example_sentence": "（（荒）あ）ら（ら）さ（さ）ないで（で）ください。", "example_reading": "あらさないでください。", "example_meaning_cn": "请不要荒废（或捣乱）。", "example_meaning_en": "Please don't devastate/make a mess."},
        "N1_98": {"example_sentence": "（（荒）あ）ら（ら）し（し）に（に）なり（なり）そう（そう）です。", "example_reading": "あらしになりそうです。", "example_meaning_cn": "好像要起风暴了。", "example_meaning_en": "A storm seems to be brewing."},
        "N1_99": {"example_sentence": "（（争）あらそ）わ（わ）ないで（で）ください。", "example_reading": "あらそわないでください。", "example_meaning_cn": "请勿争斗。", "example_meaning_en": "Please don't fight/dispute."},
        "N1_100": {"example_sentence": "（（改）あらた）め（め）さ（さ）せ（せ）て（て）ください。", "example_reading": "あらためさせてください。", "example_meaning_cn": "请让我改过（或重新开始）。", "example_meaning_en": "Please let me reform/change it."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_100.")

if __name__ == "__main__":
    main()
