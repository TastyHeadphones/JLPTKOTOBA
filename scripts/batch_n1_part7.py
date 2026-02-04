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
        "N1_601": {"example_sentence": "（（思）おも）い（い）な（な）さ（さ）ないで（で）ください。", "example_reading": "おもいなさないでください。", "example_meaning_cn": "请不要（误认为或不在）。", "example_meaning_en": "Please don't (misunderstand / ignore)."},
        "N1_602": {"example_sentence": "（（思）おも）い（い）な（な）や（や）ま（ま）ないで（で）ください。", "example_reading": "おもいなやまないでください。", "example_meaning_cn": "请不要烦恼（深思熟虑）。", "example_meaning_en": "Please don't worry / agonize over it."},
        "N1_603": {"example_sentence": "（（思）おも）い（い）の（の）か（か）ら（ら）だ（だ）が（が）不（ふ）自（じ）然（ぜん）です。", "example_reading": "おもいのからだがふしぜんです。", "example_meaning_cn": "想法本身很自然，但身体不自然。", "example_meaning_en": "The thought is natural, but the physical part is not."},
        "N1_604": {"example_sentence": "（（思）おも）い（い）の（の）ほ（ほ）か（か）高い（たかい）ですね。", "example_reading": "おもいのほかたかいですね。", "example_meaning_cn": "出乎意料（意外）地贵呢。", "example_meaning_en": "It's unexpectedly expensive."},
        "N1_605": {"example_sentence": "（（思）おも）い（い）み（み）だ（だ）さ（さ）ないで（で）ください。", "example_reading": "おもいみださないでください。", "example_meaning_cn": "请不要（心乱或打扰）。", "example_meaning_en": "Please don't (disturb / be distracted)."},
        "N1_606": {"example_sentence": "（（思）おも）い（い）め（め）ぐ（ぐ）ら（ら）し（し）て（て）ください。", "example_reading": "おもいめぐらしてください。", "example_meaning_cn": "请反复思考（深谋远虑）。", "example_meaning_en": "Please ponder / reflect carefully."},
        "N1_607": {"example_sentence": "（（思）おも）い（い）も（も）よ（よ）ら（ら）な（な）い（い）出来事（できごと）です。", "example_reading": "おもいもよらないできごとです。", "example_meaning_cn": "万万没想到（意外）的事情。", "example_meaning_en": "It's an unthinkable / unexpected event."},
        "N1_608": {"example_sentence": "（（思）おも）い（い）や（や）り（り）の（の）ある（ある）人（ひと）です。", "example_reading": "おもいやりのあるひとです。", "example_meaning_cn": "是个体贴（有同情心）的人。", "example_meaning_en": "They are a considerate person."},
        "N1_609": {"example_sentence": "（（思）おも）い（い）わ（わ）ず（ず）わ（わ）し（し）ないで（で）ください。", "example_reading": "おもいわずわしないでください。", "example_meaning_cn": "请不要（深思或烦恼）。", "example_meaning_en": "Please don't (brood / worry)."},
        "N1_610": {"example_sentence": "（（思）おも）う（う）存（ぞん）分（ぶん）食べて（たべて）ください。", "example_reading": "おもうぞんぶんたべてください。", "example_meaning_cn": "请尽情（随心所欲）享用吧。", "example_meaning_en": "Please eat to your heart's content."},
        "N1_611": {"example_sentence": "（（面）おも）しろ（ろ）おか（か）し（し）く（く）話し（はなし）ま（ま）しょ（しょ）う（う）。", "example_reading": "おもしろおかしくおなしましょう。", "example_meaning_cn": "风趣幽默地谈话吧。", "example_meaning_en": "Let's speak in a fun and amusing way."},
        "N1_612": {"example_sentence": "（（表）おも）て（て）む（む）き（き）の（の）理由（りゆう）です。", "example_reading": "おもてむきのりゆうです。", "example_meaning_cn": "表面的（公开的）理由。", "example_meaning_en": "It's an ostensible / official reason."},
        "N1_613": {"example_sentence": "（（主）おも）な（な）原因（げんいん）を（を）調べ（しらべ）ましょう。", "example_reading": "おもなげんいんをしらべましょう。", "example_meaning_cn": "调查主要原因吧。", "example_meaning_en": "Let's investigate the main cause."},
        "N1_614": {"example_sentence": "（（思）おも）わ（わ）せ（せ）ぶり（ぶり）な（な）態度（たいど）です。", "example_reading": "おもわせぶりなたいどです。", "example_meaning_cn": "故作姿态（暗示）的态度。", "example_meaning_en": "It's a suggestive / flirtatious attitude."},
        "N1_615": {"example_sentence": "（（思）おも）わ（わ）ず（ず）笑っ（わらっ）て（て）しまい（しまい）まし（し）た。", "example_reading": "おもわずわらってしまいました。", "example_meaning_cn": "禁不住（不由得）笑了出来。", "example_meaning_en": "I couldn't help laughing."},
        "N1_616": {"example_sentence": "（（思）おも）わ（わ）く（く）が（が）はずれ（はずれ）まし（し）た。", "example_reading": "おもわくがはずれました。", "example_meaning_cn": "意图（打算）落空了。", "example_meaning_en": "My expectations / speculations were frustrated."},
        "N1_617": {"example_sentence": "（（親）おや）こう（こう）こう（こう）し（し）ましょう。", "example_reading": "おやこうこうしましょう。", "example_meaning_cn": "孝顺父母吧。", "example_meaning_en": "Let's be filial to our parents."},
        "N1_618": {"example_sentence": "（（親）おや）し（し）お（お）ず（ず）し（し）ないで（で）ください。", "example_reading": "おやしおずしないでください。", "example_meaning_cn": "请不要（亲身或亲近）。", "example_meaning_en": "Please don't (be intimate / close)."},
        "N1_619": {"example_sentence": "（（親）おや）ゆ（ゆ）ず（ず）り（り）の（の）才能（さいのう）です。", "example_reading": "おやゆずりのさいのうです。", "example_meaning_cn": "继承自父母的才能。", "example_meaning_en": "It's a talent inherited from my parents."},
        "N1_620": {"example_sentence": "（（及）およ）ば（ば）な（な）い（い）で（で）ください。", "example_reading": "およばないでください。", "example_meaning_cn": "请不要够不着（或比不上）。", "example_meaning_en": "Please don't be inferior / can't reach it."},
        "N1_621": {"example_sentence": "（（泳）およ）ぎ（ぎ）き（き）っ（っ）て（て）ください。", "example_reading": "およぎきってください。", "example_meaning_cn": "请游到底。", "example_meaning_en": "Please swim all the way."},
        "N1_622": {"example_sentence": "（（及）およ）ぼ（ぼ）さ（さ）ないで（で）ください。", "example_reading": "およぼさないでください。", "example_meaning_cn": "请不要波及（使产生影响）。", "example_meaning_en": "Please don't exert influence / cause effect."},
        "N1_623": {"example_sentence": "（（織）お）り（り）な（な）さ（さ）ないで（で）ください。", "example_reading": "おりなさないでください。", "example_meaning_cn": "请不要编织（或交织）。", "example_meaning_en": "Please don't weave (together)."},
        "N1_624": {"example_sentence": "（（織）お）り（り）ま（ま）ぜ（ぜ）て（て）ください。", "example_reading": "おりまぜてください。", "example_meaning_cn": "请交织（混织）。", "example_meaning_en": "Please interweave / mix together."},
        "N1_625": {"example_sentence": "（（折）お）り（り）重な（かさな）っ（っ）て（て）います。", "example_reading": "おりかさなっています。", "example_meaning_cn": "重叠（折叠）在一起。", "example_meaning_en": "It's folded / piled up."},
        "N1_626": {"example_sentence": "（（檻）おり）に（に）入れ（いれ）て（て）ください。", "example_reading": "おりにいれてください。", "example_meaning_cn": "请放入笼子里。", "example_meaning_en": "Please put it in the cage."},
        "N1_627": {"example_sentence": "（（折）お）り（り）こ（こ）ま（ま）ないで（で）ください。", "example_reading": "おりこまないでください。", "example_meaning_cn": "请不要折叠进去（或纳入）。", "example_meaning_en": "Please don't fold it in / incorporate it."},
        "N1_628": {"example_sentence": "（（折）お）り（り）た（た）た（た）ん（ん）で（て）ください。", "example_reading": "おりたたんでください。", "example_meaning_cn": "请叠起来。", "example_meaning_en": "Please fold it up."},
        "N1_629": {"example_sentence": "（（折）お）り（り）ふ（ふ）し（し）の（の）出来事（できごと）です。", "example_reading": "おりふしのできごとです。", "example_meaning_cn": "时有的（偶然的）事情。", "example_meaning_en": "It's an occasional / seasonal event."},
        "N1_630": {"example_sentence": "（（折）お）り（り）も（も）の（の）を（を）し（し）て（て）ください。", "example_reading": "おりものをしてください。", "example_meaning_cn": "请做折纸（或分泌物）。", "example_meaning_en": "Please do origami / weave textile."},
        "N1_631": {"example_sentence": "（（愚）おろ）か（か）な（な）真似（まね）は（は）やめ（やめ）ましょ（しょ）う（う）。", "example_reading": "おろかなまねわやめましょう。", "example_meaning_cn": "停止愚蠢的行为吧。", "example_meaning_en": "Let's stop acting foolishly."},
        "N1_632": {"example_sentence": "（（疎）おろそ）か（か）に（に）し（し）ないで（で）ください。", "example_reading": "おろそかにしないでください。", "example_meaning_cn": "请不要疏忽（怠慢）。", "example_meaning_en": "Please don't neglect it / be careless."},
        "N1_633": {"example_sentence": "（（疎）おろ）し（し）う（う）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "おろしうらわないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_634": {"example_sentence": "（（恩）おん）を（を）仇（あだ）で（で）返さ（かえさ）ないで（で）ください。", "example_reading": "おんをあだでかえさないでください。", "example_meaning_cn": "不要恩将仇报。", "example_meaning_en": "Please don't return good with evil."},
        "N1_635": {"example_sentence": "（（音）おん）が（が）く（く）を（を）聴き（きき）ま（ま）しょ（しょ）う（う）。", "example_reading": "おんがくをききましょう。", "example_meaning_cn": "听音乐吧。", "example_meaning_en": "Let's listen to music."},
        "N1_636": {"example_sentence": "（（温）おん）け（け）い（い）を（を）受け（うけ）て（て）い（い）ます。", "example_reading": "おんけいをうけています。", "example_meaning_cn": "蒙受恩惠。", "example_meaning_en": "I'm receiving favors / benefits."},
        "N1_637": {"example_sentence": "（（音）おん）し（し）ん（ん）が（が）不（ふ）通（つう）です。", "example_reading": "おんしんがふつうです。", "example_meaning_cn": "音讯中断（失去联系）。", "example_meaning_en": "There is no news / communication is cut off."},
        "N1_638": {"example_sentence": "（（音）おん）せ（せ）い（い）で（で）入力（にゅうりょく）し（し）て（て）ください。", "example_reading": "おんせいでにゅうりょくしてください。", "example_meaning_cn": "请用语音输入。", "example_meaning_en": "Please input via voice."},
        "N1_639": {"example_sentence": "（（温）おん）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "おんぜんとしています。", "example_meaning_cn": "温然（温和）着。", "example_meaning_en": "It's gentle / mild."},
        "N1_640": {"example_sentence": "（（温）おん）たい（たい）の（の）気候（きこう）です。", "example_reading": "おんたいのきこうです。", "example_meaning_cn": "温带的气候。", "example_meaning_en": "It's a temperate climate."},
        "N1_641": {"example_sentence": "（（温）おん）だ（だ）んな（な）気候（きこう）を（を）好み（このみ）ます。", "example_reading": "おんだんなきこうをこのみます。", "example_meaning_cn": "喜欢温暖的气候。", "example_meaning_en": "I prefer a mild / warm climate."},
        "N1_642": {"example_sentence": "（（音）おん）ち（ち）を（を）治し（なおし）たい（たい）です。", "example_reading": "おんちをなおしたいです。", "example_meaning_cn": "想治好五音不全。", "example_meaning_en": "I want to fix my tone deafness."},
        "N1_643": {"example_sentence": "（（温）おん）ど（ど）を（を）測り（はかり）ましょう。", "example_reading": "おんどをはかりましょう。", "example_meaning_cn": "测量温度吧。", "example_meaning_en": "Let's measure the temperature."},
        "N1_644": {"example_sentence": "（（音）おん）ぱ（ぱ）を（を）利用（りよう）し（し）て（て）ください。", "example_reading": "おんぱをりようしてください。", "example_meaning_cn": "请利用声波。", "example_meaning_en": "Please use sound waves."},
        "N1_645": {"example_sentence": "（（温）おん）ぽ（ぽ）し（し）ないで（で）ください。", "example_reading": "おんぽしないでください。", "example_meaning_cn": "请不要（热敷或保护）。", "example_meaning_en": "Please don't (apply hot compress / protect)."},
        "N1_646": {"example_sentence": "（（陰）おん）み（み）ょ（ょ）う（う）じ（じ）に（に）なり（なり）たい（たい）です。", "example_reading": "おんみょうじになりたいです。", "example_meaning_cn": "想成为阴阳师。", "example_meaning_en": "I want to be an Onmyoji (diviner)."},
        "N1_647": {"example_sentence": "（（恩）おん）め（め）い（い）を（を）受け（うけ）て（て）ください。", "example_reading": "おんめいをうけてください。", "example_meaning_cn": "请受恩（恩赐）。", "example_meaning_en": "Please receive the favor / decree."},
        "N1_648": {"example_sentence": "（（恩）おん）も（も）の（の）に（に）なり（なり）たい（たい）です。", "example_reading": "おんものになりたいです。", "example_meaning_cn": "想成为（被恩惠的）人。", "example_meaning_en": "I want to be a person of grace."},
        "N1_649": {"example_sentence": "（（恩）おん）ら（ら）ん（ん）し（し）ないで（で）ください。", "example_reading": "おんらんしないでください。", "example_meaning_cn": "请不要（恩乱或搅扰）。", "example_meaning_en": "Please don't (be ungrateful / disturb)."},
        "N1_650": {"example_sentence": "（（恩）おん）り（り）を（を）感じ（かんじ）て（て）ください。", "example_reading": "おんりをかんじてください。", "example_meaning_cn": "请感受到恩利（或感激）。", "example_meaning_en": "Please feel the gratitude / benefit."},
        "N1_651": {"example_sentence": "（（河）か）に（に）落ち（おち）ないで（で）ください。", "example_reading": "かにおちないでください。", "example_meaning_cn": "请不要掉进河里。", "example_meaning_en": "Please don't fall into the river."},
        "N1_652": {"example_sentence": "（（蚊）か）に（に）刺さ（ささ）れ（れ）まし（し）た。", "example_reading": "かにさされました。", "example_meaning_cn": "被蚊子叮了。", "example_meaning_en": "I was bitten by a mosquito."},
        "N1_653": {"example_sentence": "（（課）か）を（を）まとめ（まとめ）て（て）ください。", "example_reading": "かをまとめてください。", "example_meaning_cn": "请统一（或管理）科室。", "example_meaning_en": "Please manage the section / lesson."},
        "N1_654": {"example_sentence": "（（科）か）に（に）分け（わけ）て（て）ください。", "example_reading": "かにわけてください。", "example_meaning_cn": "请分成科目（或种类）。", "example_meaning_en": "Please divide it into departments / subjects."},
        "N1_655": {"example_sentence": "（（果）か）を（を）得（え）て（て）ください。", "example_reading": "かをえてください。", "example_meaning_cn": "请取得果实（或结果）。", "example_meaning_en": "Please get the fruit / result."},
        "N1_656": {"example_sentence": "（（可）か）と（と）し（し）て（て）ください。", "example_reading": "かとしてください。", "example_meaning_cn": "请定为许可（或合格）。", "example_meaning_en": "Please mark it as passed / acceptable."},
        "N1_657": {"example_sentence": "（（火）か）を（を）つけ（つけ）ないで（で）ください。", "example_reading": "かをつけないでください。", "example_meaning_cn": "请不要点火。", "example_meaning_en": "Please don't light the fire."},
        "N1_658": {"example_sentence": "（（架）か）を（を）組ん（くん）で（て）ください。", "example_reading": "かをくんでください。", "example_meaning_cn": "请搭架子。", "example_meaning_en": "Please set up the frame / shelf."},
        "N1_659": {"example_sentence": "（（荷）か）を（を）運び（はこび）ま（ま）しょ（しょ）う（う）。", "example_reading": "かをはこびましょう。", "example_meaning_cn": "运货吧。", "example_meaning_en": "Let's carry the luggage / load."},
        "N1_660": {"example_sentence": "（（華）か）を（を）添え（そえ）て（て）ください。", "example_reading": "かをそえてください。", "example_meaning_cn": "请增光添彩（添华）。", "example_meaning_en": "Please add some glamour / brilliance."},
        "N1_661": {"example_sentence": "（（暇）か）を（を）出し（だし）て（て）ください。", "example_reading": "かをだしてください。", "example_meaning_cn": "请休假（或解雇）。", "example_meaning_en": "Please take a leave / dismiss me."},
        "N1_662": {"example_sentence": "（（過）か）を（を）認め（みとめ）て（て）ください。", "example_reading": "かをみとめてください。", "example_meaning_cn": "请承认过失（或经过）。", "example_meaning_en": "Please acknowledge the fault / excess."},
        "N1_663": {"example_sentence": "（（歌）か）を（を）詠み（よみ）ましょう。", "example_reading": "かをよみましょう。", "example_meaning_cn": "咏歌（作诗）吧。", "example_meaning_en": "Let's compose a poem / song."},
        "N1_664": {"example_sentence": "（（下）か）に（に）降り（ふり）て（て）ください。", "example_reading": "かにふりてください。", "example_meaning_cn": "请走下去。", "example_meaning_en": "Please go down / go below."},
        "N1_665": {"example_sentence": "（（箇）か）に（に）入れ（いれ）て（て）ください。", "example_reading": "かにいれてください。", "example_meaning_cn": "请放入计数中（或箇）。", "example_meaning_en": "Please put it into the category / items."},
        "N1_666": {"example_sentence": "（（介）か）い（い）し（し）ないで（で）ください。", "example_reading": "かいしないでください。", "example_meaning_cn": "请不要引以为意（或在乎）。", "example_meaning_en": "Please don't worry / mind it."},
        "N1_667": {"example_sentence": "（（外）がい）を（を）避け（さけ）て（て）ください。", "example_reading": "がいをさけてください。", "example_meaning_cn": "请避开外面（或害处）。", "example_meaning_en": "Please avoid the outside / harm."},
        "N1_668": {"example_sentence": "（（害）がい）を（を）及ぼさ（およぼさ）ないで（で）ください。", "example_reading": "がいをおよぼさないでください。", "example_meaning_cn": "不要带来危害。", "example_meaning_en": "Please don't cause harm."},
        "N1_669": {"example_sentence": "（（悔）かい）を（を）残さ（のこさ）ないで（で）ください。", "example_reading": "かいをのこさないでください。", "example_meaning_cn": "不要留下遗憾。", "example_meaning_en": "Please leave no regrets."},
        "N1_670": {"example_sentence": "（（貝）かい）を（を）拾い（ひろい）ましょう。", "example_reading": "かいをひろいましょう。", "example_meaning_cn": "拾贝壳吧。", "example_meaning_en": "Let's pick up shells."},
        "N1_671": {"example_sentence": "（（甲斐）かい）が（が）あり（あり）ますね。", "example_reading": "かいがありますね。", "example_meaning_cn": "真有价值（或效果）呢。", "example_meaning_en": "It's worthwhile / fruitful."},
        "N1_672": {"example_sentence": "（（階）かい）を（を）上がっ（あがっ）て（て）ください。", "example_reading": "かいをあがってください。", "example_meaning_cn": "请上楼（或等级）。", "example_meaning_en": "Please go upstairs / up a level."},
        "N1_673": {"example_sentence": "（（会）かい）を（を）開き（ひらき）ましょう。", "example_reading": "かいをひらきましょう。", "example_meaning_cn": "开会办会吧。", "example_meaning_en": "Let's hold a meeting / association."},
        "N1_674": {"example_sentence": "（（改）かい）を（を）加え（くわえ）て（て）ください。", "example_reading": "かいをくわえてください。", "example_meaning_cn": "请进行修改（改良）。", "example_meaning_en": "Please make revisions / alterations."},
        "N1_675": {"example_sentence": "（（解）かい）を（を）見つけ（みつけ）て（て）ください。", "example_reading": "かいをみつけてください。", "example_meaning_cn": "请找到解答（理解）。", "example_meaning_en": "Please find the solution / answer."},
        "N1_676": {"example_sentence": "（（開）かい）し（し）て（て）ください。", "example_reading": "かいしてください。", "example_meaning_cn": "请开启（开始）。", "example_meaning_en": "Please open / start."},
        "N1_677": {"example_sentence": "（（塊）かい）を（を）砕い（くだい）て（て）ください。", "example_reading": "かいをくだいてください。", "example_meaning_cn": "请打碎土块（或硬块）。", "example_meaning_en": "Please break the lump / clod."},
        "N1_678": {"example_sentence": "（（改）かい）あ（あ）く（く）し（し）ないで（で）ください。", "example_reading": "かいあくしないでください。", "example_meaning_cn": "请不要改恶（越改越坏）。", "example_meaning_en": "Please don't make it worse / deteriorate it."},
        "N1_679": {"example_sentence": "（（改）かい）い（い）あ（あ）お（お）ず（ず）し（し）ないで（で）ください。", "example_reading": "かいいあおずしないでください。", "example_meaning_cn": "请不要（改选或改变）。", "example_meaning_en": "Please don't (alter / change)."},
        "N1_680": {"example_sentence": "（（改）かい）い（い）を（を）し（し）て（て）ください。", "example_reading": "かいいをしてください。", "example_meaning_cn": "请进行改一（或统一）。", "example_meaning_en": "Please perform reform / unification."},
        "N1_681": {"example_sentence": "（（改）かい）え（え）し（し）ないで（で）ください。", "example_reading": "かいえしないでください。", "example_meaning_cn": "请不要改绘（或改变）。", "example_meaning_en": "Please don't redraw / alter."},
        "N1_682": {"example_sentence": "（（開）かい）え（え）ん（ん）し（し）て（て）ください。", "example_reading": "かいえんしてください。", "example_meaning_cn": "请开始演戏。", "example_meaning_en": "Please start the performance."},
        "N1_683": {"example_sentence": "（（改）かい）お（お）し（し）ないで（で）ください。", "example_reading": "かいおしないでください。", "example_meaning_cn": "请不要（改变或改正）。", "example_meaning_en": "Please don't (alter / correct)."},
        "N1_684": {"example_sentence": "（（外）がい）か（か）を（を）得（え）て（て）ください。", "example_reading": "がいかをえてください。", "example_meaning_cn": "请获取外币（或凯歌）。", "example_meaning_en": "Please earn foreign currency / victory song."},
        "N1_685": {"example_sentence": "（（改）かい）か（か）く（く）し（し）て（て）ください。", "example_reading": "かいかくしてください。", "example_meaning_cn": "请改革。", "example_meaning_en": "Please reform it."},
        "N1_686": {"example_sentence": "（（海）かい）き（き）ょ（ょ）う（う）を（を）渡り（わたり）ましょう。", "example_reading": "かいきょうをわたりましょう。", "example_meaning_cn": "渡过海峡吧。", "example_meaning_en": "Let's cross the strait."},
        "N1_687": {"example_sentence": "（（快）かい）き（き）ょ（ょ）し（し）て（て）ください。", "example_reading": "かいきょしてください。", "example_meaning_cn": "请采取快举（壮举）。", "example_meaning_en": "Please perform a brilliant feat."},
        "N1_688": {"example_sentence": "（（快）かい）き（き）を（を）祈り（いのり）ましょう。", "example_reading": "かいきをいのりましょう。", "example_meaning_cn": "祈祷康复吧。", "example_meaning_en": "Let's pray for a full recovery."},
        "N1_689": {"example_sentence": "（（海）かい）く（く）に（に）なり（なり）たい（たい）です。", "example_reading": "かいくにになりたいです。", "example_meaning_cn": "想成为海国（或开放）。", "example_meaning_en": "I want to be a maritime nation / open up."},
        "N1_690": {"example_sentence": "（（改）かい）け（け）つ（つ）し（し）て（て）ください。", "example_reading": "かいけつしてください。", "example_meaning_cn": "请解决。", "example_meaning_en": "Please resolve it."},
        "N1_691": {"example_sentence": "（（会）かい）け（け）い（い）を（を）任せ（まかせ）て（て）ください。", "example_reading": "かいけいをまかせてください。", "example_meaning_cn": "会计（结账）请交给我。", "example_meaning_en": "Please leave the accounting / bill to me."},
        "N1_692": {"example_sentence": "（（解）かい）け（け）つ（つ）し（し）て（て）ください。", "example_reading": "かいけつしてください。", "example_meaning_cn": "请解决（解开）。", "example_meaning_en": "Please solve / settle it."},
        "N1_693": {"example_sentence": "（（快）かい）け（け）つ（つ）し（し）ないで（で）ください。", "example_reading": "かいけつしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_694": {"example_sentence": "（（改）かい）げ（げ）ん（ん）し（し）て（て）ください。", "example_reading": "かいげんしてください。", "example_meaning_cn": "请改元（或戒严）。", "example_meaning_en": "Please change the era name / place under martial law."},
        "N1_695": {"example_sentence": "（（外）がい）こ（こ）う（う）を（を）重視（じゅうし）し（し）ましょう。", "example_reading": "がいこうをじゅうししましょう。", "example_meaning_cn": "重视外交吧。", "example_meaning_en": "Let's prioritize diplomacy."},
        "N1_696": {"example_sentence": "（（快）かい）こ（こ）く（く）し（し）て（て）ください。", "example_reading": "かいこくしてください。", "example_meaning_cn": "请开国（或告诫）。", "example_meaning_en": "Please open the country / warn it."},
        "N1_697": {"example_sentence": "（（海）かい）ご（ご）し（し）ないで（で）ください。", "example_reading": "かいごしないでください。", "example_meaning_cn": "请不要（巡游或照顾）。", "example_meaning_en": "Please don't (cruise / care for)."},
        "N1_698": {"example_sentence": "（（介）かい）ご（ご）し（し）て（て）ください。", "example_reading": "かいごしてください。", "example_meaning_cn": "请进行护理。", "example_meaning_en": "Please provide nursing care."},
        "N1_699": {"example_sentence": "（（解）かい）ご（ご）し（し）ないで（で）ください。", "example_reading": "かいごしないでください。", "example_meaning_cn": "请不要（误解或开悟）。", "example_meaning_en": "Please don't (misunderstand / realize)."},
        "N1_700": {"example_sentence": "（（改）かい）さ（さ）つ（つ）を（を）通り（とおり）ましょう。", "example_reading": "かいさつを通りましょう。", "example_meaning_cn": "过检票口。吧。", "example_meaning_en": "Let's go through the ticket gate."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_700.")

if __name__ == "__main__":
    main()
