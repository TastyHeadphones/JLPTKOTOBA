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
        "N1_1201": {"example_sentence": "（（野）や）わ（わ）ら（ら）な（な）い（い）で（为）ください。", "example_reading": "やわないでください。", "example_meaning_cn": "请不要变得软弱（或生病）。", "example_meaning_en": "Please don't (be soft / get sick)."},
        "N1_1202": {"example_sentence": "（（唯）ゆい）い（い）つ（つ）の（の）宝物（たからもの）です。", "example_reading": "ゆいいつのたからものです。", "example_meaning_cn": "唯一的宝物。", "example_meaning_en": "It's my only treasure."},
        "N1_1203": {"example_sentence": "（（唯）ゆい）い（い）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "ゆいいんしないでください。", "example_meaning_cn": "请不要唯心（或遗言）。", "example_meaning_en": "Please don't be idealistic / leave a will."},
        "N1_1204": {"example_sentence": "（（遺）ゆい）ご（ご）ん（ん）を（を）書き（かき）ま（ま）しょ（しょ）う（う）。", "example_reading": "ゆいごんをかきましょう。", "example_meaning_cn": "写遗嘱吧。", "example_meaning_en": "Let's write a will."},
        "N1_1205": {"example_sentence": "（（結）ゆい）い（い）に（に）し（し）ないで（为）ください。", "example_reading": "ゆいにしないでください。", "example_meaning_cn": "请不要作为结（或已经系好）。", "example_meaning_en": "Please don't make it a knot / tied."},
        "N1_1206": {"example_sentence": "（（唯）ゆい）に（に）なら（なら）ないで（为）ください。", "example_reading": "ゆいにならないでください。", "example_meaning_cn": "请不要唯独（或唯一）。", "example_meaning_en": "Please don't be unique / alone."},
        "N1_1207": {"example_sentence": "（（幽）ゆう）に（に）し（し）て（て）ください。", "example_reading": "ゆうにしてください。", "example_meaning_cn": "请使其变得幽静（或优裕）。", "example_meaning_en": "Please make it quiet / surplus."},
        "N1_1208": {"example_sentence": "（（優）ゆう）え（え）つ（つ）か（か）ん（ん）に（に）浸ら（ひたら）ないで（为）ください。", "example_reading": "ゆうえつかんをひたらないでください。", "example_meaning_cn": "不要沉浸在优越感中。", "example_meaning_en": "Don't indulge in a sense of superiority."},
        "N1_1209": {"example_sentence": "（（有）ゆう）え（え）き（き）な（な）時間（じかん）を（を）過ごし（すごし）ま（ま）しょ（しょ）う（う）。", "example_reading": "ゆうえきなじかんをすごしましょう。", "example_meaning_cn": "度过有益的时间吧。", "example_meaning_en": "Let's spend a meaningful / beneficial time."},
        "N1_1210": {"example_sentence": "（（優）ゆう）え（え）ん（ん）し（し）ないで（为）ください。", "example_reading": "ゆうえんしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1211": {"example_sentence": "（（融）ゆう）が（が）し（し）ないで（为）ください。", "example_reading": "ゆうがしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1212": {"example_sentence": "（（優）ゆう）が（が）な（な）振る舞い（ふるまい）を（を）し（し）て（て）ください。", "example_reading": "ゆうがなふるまいをしてください。", "example_meaning_cn": "请表现得优雅。", "example_meaning_en": "Please behave elegantly / gracefully."},
        "N1_1213": {"example_sentence": "（（融）ゆう）き（き）を（を）出し（だし）て（て）ください。", "example_reading": "ゆうきをだしてください。", "example_meaning_cn": "请拿出勇气（或融化）。", "example_meaning_en": "Please have courage / melt."},
        "N1_1214": {"example_sentence": "（（有）ゆう）き（き）ぶ（ぶ）つ（つ）を（を）調べ（しらべ）ま（ま）しょ（しょ）う（う）。", "example_reading": "ゆうきぶつをしらべましょう。", "example_meaning_cn": "调查有机物吧。", "example_meaning_en": "Let's investigate organic matter."},
        "N1_1215": {"example_sentence": "（（悠）ゆう）き（き）ゅ（ゅ）う（う）の（の）時（とき）を（を）刻み（きざみ）ま（ま）しょ（しょ）う（う）。", "example_reading": "ゆうきゅうのときをきざみましょう。", "example_meaning_cn": "刻下悠久的时间吧。", "example_meaning_en": "Let's mark the eternal / leisurely time."},
        "N1_1216": {"example_sentence": "（（有）ゆう）く（く）を（を）感じ（かんじ）ます。", "example_reading": "ゆうくをかんじます。", "example_meaning_cn": "感到忧郁（或有空）。", "example_meaning_en": "I feel gloomy / free time."},
        "N1_1217": {"example_sentence": "（（有）ゆう）け（け）つ（つ）し（し）て（て）ください。", "example_reading": "ゆうけつしてください。", "example_meaning_cn": "请使其成结（或已经输血）。", "example_meaning_en": "Please make it tie / give a blood transfusion."},
        "N1_1218": {"example_sentence": "（（有）ゆう）げ（げ）ん（ん）し（し）て（て）ください。", "example_reading": "ゆうげんしてください。", "example_meaning_cn": "请使其有限（或已经言明）。", "example_meaning_en": "Please make it finite / state it."},
        "N1_1219": {"example_sentence": "（（有）ゆう）ご（ご）し（し）ないで（为）ください。", "example_reading": "ゆうごしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1220": {"example_sentence": "（（融）ゆう）ご（ご）う（う）し（し）て（て）ください。", "example_reading": "ゆうごうしてください。", "example_meaning_cn": "请融合。", "example_meaning_en": "Please fuse / merge it."},
        "N1_1221": {"example_sentence": "（（有）ゆう）さ（さ）を（を）保っ（たもっ）て（て）ください。", "example_reading": "ゆうさをたもってください。", "example_meaning_cn": "请保持优势（或悠然）。", "example_meaning_en": "Please maintain the superiority / leisure."},
        "N1_1222": {"example_sentence": "（（有）ゆう）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "ゆうしんしないでください。", "example_meaning_cn": "请不要（有心或唯心）。", "example_meaning_en": "Please don't (have a mind / be idealistic)."},
        "N1_1223": {"example_sentence": "（（有）ゆう）し（し）ゅ（ゅ）う（う）な（な）成績（せいせき）です。", "example_reading": "ゆうしゅうなせいせきです。", "example_meaning_cn": "优秀的成绩。", "example_meaning_en": "It's an excellent result."},
        "N1_1224": {"example_sentence": "（（有）ゆう）し（し）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "ゆうしょうしてください。", "example_meaning_cn": "请使其有证（或已经获胜）。", "example_meaning_en": "Please prove it / win the victory."},
        "N1_1225": {"example_sentence": "（（優）ゆう）す（す）う（う）な（な）存在（そんざい）です。", "example_reading": "ゆうすうなそんざいです。", "example_meaning_cn": "屈指可数的（卓越的）存在。", "example_meaning_en": "It's a prominent / outstanding presence."},
        "N1_1226": {"example_sentence": "（（宥）ゆう）せ（せ）い（い）し（し）て（て）ください。", "example_reading": "ゆうせいしてください。", "example_meaning_cn": "请使其宽恕（或已经优势）。", "example_meaning_en": "Please forgive / make it superior."},
        "N1_1227": {"example_sentence": "（（優）ゆう）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "ゆうぜんとしています。", "example_meaning_cn": "悠然（自若）着。", "example_meaning_en": "It's leisure / calm / composed."},
        "N1_1228": {"example_sentence": "（（有）ゆう）そ（そ）う（う）し（し）て（て）ください。", "example_reading": "ゆうそうしてください。", "example_meaning_cn": "请使其邮送（或已经运送）。", "example_meaning_en": "Please send it by mail."},
        "N1_1229": {"example_sentence": "（（有）ゆう）そ（そ）く（く）し（し）ないで（为）ください。", "example_reading": "ゆうそくしないでください。", "example_meaning_cn": "请不要（有息或快速）。", "example_meaning_en": "Please don't (have interest / be high-speed)."},
        "N1_1230": {"example_sentence": "（（有）ゆう）だ（だ）い（い）な（な）景色（けしき）です。", "example_reading": "ゆうだいなけしきです。", "example_meaning_cn": "雄大的景色。", "example_meaning_en": "It's a magnificent / grand view."},
        "N1_1231": {"example_sentence": "（（誘）ゆう）だ（だ）く（く）し（し）ないで（为）ください。", "example_reading": "ゆうだくしないでください。", "example_meaning_cn": "请不要（诱诺或答应）。", "example_meaning_en": "Please don't (consent / accept)."},
        "N1_1232": {"example_sentence": "（（有）ゆう）ち（ち）く（く）し（し）て（て）ください。", "example_reading": "ゆうちくしてください。", "example_meaning_cn": "请使其有畜（或已经筑好）。", "example_meaning_en": "Please stock / build it."},
        "N1_1233": {"example_sentence": "（（誘）ゆう）ち（ち）し（し）て（て）ください。", "example_reading": "ゆうちしてください。", "example_meaning_cn": "请引致（召集）。", "example_meaning_en": "Please invite / attract / solicit."},
        "N1_1234": {"example_sentence": "（（有）ゆう）ち（ち）ょ（ょ）う（う）に（に）し（し）ないで（为）ください。", "example_reading": "ゆうちょうにしないでください。", "example_meaning_cn": "请不要慢条斯理（不紧不慢）。", "example_meaning_en": "Please don't be so leisurely / slow."},
        "N1_1235": {"example_sentence": "（（誘）ゆう）ど（ど）う（う）し（し）て（て）ください。", "example_reading": "ゆうどうしてください。", "example_meaning_cn": "请引导（诱导）。", "example_meaning_en": "Please guide / lead / induce."},
        "N1_1236": {"example_sentence": "（（有）ゆう）に（に）し（し）て（て）ください。", "example_reading": "ゆうにしてください。", "example_meaning_cn": "请定为有效（或优裕）。", "example_meaning_en": "Please make it valid / surplus."},
        "N1_1237": {"example_sentence": "（（有）ゆう）に（に）ん（ん）し（し）て（て）ください。", "example_reading": "ゆうにんしてください。", "example_meaning_cn": "请使其留任（或已经委任）。", "example_meaning_en": "Please reappoint / commission him."},
        "N1_1238": {"example_sentence": "（（有）ゆう）は（は）あり（あり）ません。", "example_reading": "ゆうわありません。", "example_meaning_cn": "没有有效（或有名）。", "example_meaning_en": "There is no validity / fame."},
        "N1_1239": {"example_sentence": "（（有）ゆう）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "ゆうばなしをしないでください。", "example_meaning_cn": "请不要（说明或谈话）。", "example_meaning_en": "Please don't (explain / talk)."},
        "N1_1240": {"example_sentence": "（（有）ゆう）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "ゆうふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1241": {"example_sentence": "（（有）ゆう）ぽ（ぽ）し（し）てください。", "example_reading": "ゆうぽしてください。", "example_meaning_cn": "请使其有步（或已经进步）。", "example_meaning_en": "Please make progress / advance."},
        "N1_1242": {"example_sentence": "（（融）ゆう）ほ（ほ）う（う）し（し）て（て）ください。", "example_reading": "ゆうほうしてください。", "example_meaning_cn": "请使其有法（或已经播放）。", "example_meaning_en": "Please follow the law / broadcast."},
        "N1_1243": {"example_sentence": "（（有）ゆう）ま（ま）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "ゆうまわらないでください。", "example_meaning_cn": "请不要（绕道或改变）。", "example_meaning_en": "Please don't (go around / change)."},
        "N1_1244": {"example_sentence": "（（有）ゆう）め（め）い（い）に（に）なり（なり）たい（たい）です。", "example_reading": "ゆうめいになりたいです。", "example_meaning_cn": "想变得有名。", "example_meaning_en": "I want to become famous."},
        "N1_1245": {"example_sentence": "（（有）ゆう）も（も）う（う）な（な）振る舞い（ふるまい）です。", "example_reading": "ゆうもうなふるまいです。", "example_meaning_cn": "勇猛的行为。", "example_meaning_en": "It's a brave / daring behavior."},
        "N1_1246": {"example_sentence": "（（有）ゆう）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "ゆうらんしないでください。", "example_meaning_cn": "请不要（游玩或紊乱）。", "example_meaning_en": "Please don't (sightsee / be disturbed)."},
        "N1_1247": {"example_sentence": "（（有）ゆう）り（り）し（し）ないで（为）ください。", "example_reading": "ゆうりしないでください。", "example_meaning_cn": "请不要（分离或改变）。", "example_meaning_en": "Please don't (be separated / change)."},
        "N1_1248": {"example_sentence": "（（有）ゆう）り（り）ょ（ょ）く（く）な（な）候補（こうほ）です。", "example_reading": "ゆうりょくなこうほです。", "example_meaning_cn": "有力的（有影响力的）候选人。", "example_meaning_en": "It's a powerful / influential candidate."},
        "N1_1249": {"example_sentence": "（（悠）ゆう）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "ゆぅるのをてつだってください。", "example_meaning_cn": "请帮我旋转（或休闲）。", "example_meaning_en": "Please help me rotate / leisure."},
        "N1_1250": {"example_sentence": "（（有）ゆう）れ（れ）い（い）は（は）心（こころ）の（の）迷い（まよい）です。", "example_reading": "ゆうれいわこころのまよいです。", "example_meaning_cn": "幽灵是心里的迷惘（幻觉）。", "example_meaning_en": "Ghosts are just illusions of the mind."},
        "N1_1251": {"example_sentence": "（（誘）ゆう）惑（わく）に（に）負け（まけ）ないで（为）ください。", "example_reading": "ゆうわくにまけないでください。", "example_meaning_cn": "不要输给诱惑。", "example_meaning_en": "Don't give in to temptation."},
        "N1_1252": {"example_sentence": "（（有）ゆう）わ（わ）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "ゆうわをたのしみましょう。", "example_meaning_cn": "享受和谈（或融合）吧。", "example_meaning_en": "Let's enjoy the reconciliation / fusion."},
        "N1_1253": {"example_sentence": "（（有）ゆう）を（を）尽くし（つくし）て（て）ください。", "example_reading": "ゆうをつくしてください。", "example_meaning_cn": "请极尽所有（或优势）。", "example_meaning_en": "Please do your utmost with everything you have."},
        "N1_1254": {"example_sentence": "（（指）ゆび）き（き）り（り）を（を）し（し）ま（ま）しょ（しょ）う（う）。", "example_reading": "ゆびきりをしましょう。", "example_meaning_cn": "拉钩（许诺）吧。", "example_meaning_en": "Let's make a pinky swear."},
        "N1_1255": {"example_sentence": "（（指）ゆび）さ（さ）し（し）て（て）ください。", "example_reading": "ゆびさしてください。", "example_meaning_cn": "请指出来。", "example_meaning_en": "Please point it out."},
        "N1_1256": {"example_sentence": "（（弓）ゆ）み（み）を（を）引い（ひい）て（て）ください。", "example_reading": "ゆみをひいてください。", "example_meaning_cn": "请拉弓。", "example_meaning_en": "Please draw the bow."},
        "N1_1257": {"example_sentence": "（（緩）ゆる）み（み）を（を）直し（なおし）て（て）ください。", "example_reading": "ゆるみをなおしてください。", "example_meaning_cn": "请勒紧（修正松动处）。", "example_meaning_en": "Please tighten the looseness / slack."},
        "N1_1258": {"example_sentence": "（（揺）ゆ）る（る）ぎ（ぎ）ない（ない）自信（じしん）です。", "example_reading": "ゆるぎないじしんです。", "example_meaning_cn": "坚定不移的自信。", "example_meaning_en": "It's an unwavering confidence."},
        "N1_1259": {"example_sentence": "（（揺）ゆ）る（る）ぐ（ぐ）のを（を）やめ（やめ）ましょう。", "example_reading": "ゆるぐのをやめましょう。", "example_meaning_cn": "别再动摇了吧。", "example_meaning_en": "Let's stop shaking / wavering."},
        "N1_1260": {"example_sentence": "（（予）よ）に（に）し（し）て（て）ください。", "example_reading": "よにしてください。", "example_meaning_cn": "请定为预备（或世界）。", "example_meaning_en": "Please make it preparation / world."},
        "N1_1261": {"example_sentence": "（（世）よ）の（の）中（なか）の（の）仕組み（しくみ）を（を）知り（しり）ま（ま）しょ（しょ）う（う）。", "example_reading": "よのなかのしくみをしりましょう。", "example_meaning_cn": "了解世间的机制吧。", "example_meaning_en": "Let's learn how the world works."},
        "N1_1262": {"example_sentence": "（（予）よ）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "よばなしをしないでください。", "example_meaning_cn": "请不要说预言（或闲聊）。", "example_meaning_en": "Please don't speak prophecies / talk."},
        "N1_1263": {"example_sentence": "（（予）よ）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "よふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1264": {"example_sentence": "（（予）よ）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "よらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1265": {"example_sentence": "（（予）よ）り（り）し（し）ないで（为）ください。", "example_reading": "よりしないでください。", "example_meaning_cn": "请不要（借用或假定）。", "example_meaning_en": "Please don't (borrow / assume)."},
        "N1_1266": {"example_sentence": "（（予）よ）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "よれいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_1267": {"example_sentence": "（（予）よ）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "よろをとおしてください。", "example_meaning_cn": "请（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1268": {"example_sentence": "（（予）よ）わ（わ）し（し）ないで（为）ください。", "example_reading": "よわしないでください。", "example_meaning_cn": "请不要（和谈或预备）。", "example_meaning_en": "Please don't (be at peace / prepare)."},
        "N1_1269": {"example_sentence": "（（良）よ）い（い）事（こと）を（を）し（し）ましょう。", "example_reading": "よいことをしましょう。", "example_meaning_cn": "做点好事吧。", "example_meaning_en": "Let's do something good."},
        "N1_1270": {"example_sentence": "（（酔）よ）い（い）を（を）覚まし（さまし）ま（ま）しょ（しょ）う（う）。", "example_reading": "よいをさましましょう。", "example_meaning_cn": "醒醒酒吧。", "example_meaning_en": "Let's sober up."},
        "N1_1271": {"example_sentence": "（（養）よう）い（い）し（し）ないで（为）ください。", "example_reading": "よういしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1272": {"example_sentence": "（（用）よう）い（い）し（し）て（て）ください。", "example_reading": "よういしてください。", "example_meaning_cn": "请准备。", "example_meaning_en": "Please prepare it / get ready."},
        "N1_1273": {"example_sentence": "（（様）よう）い（い）ん（ん）を（を）調べ（しらべ）ま（ま）しょ（しょ）う（う）。", "example_reading": "よういんをしらべましょう。", "example_meaning_cn": "调查主要原因（要因）吧。", "example_meaning_en": "Let's investigate the main cause / factor."},
        "N1_1274": {"example_sentence": "（（要）よう）え（え）き（き）を（を）使い（つかい）ま（ま）しょ（しょ）う（う）。", "example_reading": "ようえきをつかいましょう。", "example_meaning_cn": "使用溶液（或要职）吧。", "example_meaning_en": "Let's use the solution / take an important post."},
        "N1_1275": {"example_sentence": "（（要）よう）え（え）ん（ん）な（な）美（うつく）しさ（さ）です。", "example_reading": "ようえんなうつくしさです。", "example_meaning_cn": "妖艳的美丽。", "example_meaning_en": "It's an alluring / bewitching beauty."},
        "N1_1276": {"example_sentence": "（（様）よう）き（き）に（に）過ごし（すごし）ま（ま）しょ（しょ）う（う）。", "example_reading": "ようきにすごしましょう。", "example_meaning_cn": "开朗地生活吧。", "example_meaning_en": "Let's live cheerfully / merrily."},
        "N1_1277": {"example_sentence": "（（養）よう）き（き）ゅ（ゅ）う（う）し（し）て（て）ください。", "example_reading": "ようきゅうしてください。", "example_meaning_cn": "请要求。", "example_meaning_en": "Please request / demand it."},
        "N1_1278": {"example_sentence": "（（要）よう）き（き）ょ（ょ）く（く）を（を）聞き（きき）たい（たい）です。", "example_reading": "ようきょくをききたいです。", "example_meaning_cn": "想听听（能乐的）曲辞（或要请）。", "example_meaning_en": "I want to hear the Noh song lyrics / request."},
        "N1_1279": {"example_sentence": "（（要）よう）け（け）つ（つ）し（し）て（て）ください。", "example_reading": "ようけつしてください。", "example_meaning_cn": "请总结要点（或已经解决）。", "example_meaning_en": "Please summarize the main points."},
        "N1_1280": {"example_sentence": "（（要）よう）げ（げ）ん（ん）を（を）使い（つかい）ま（ま）しょ（しょ）う（う）。", "example_reading": "ようげんをつかいましょう。", "example_meaning_cn": "使用用言（动词、形容词等）吧。", "example_meaning_en": "Let's use the predicate words."},
        "N1_1281": {"example_sentence": "（（要）よう）ご（ご）し（し）ないで（为）ください。", "example_reading": "ようごしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1282": {"example_sentence": "（（擁）よう）ご（ご）し（し）て（て）ください。", "example_reading": "ようごしてください。", "example_meaning_cn": "请拥护（保护）。", "example_meaning_en": "Please protect / advocate for them."},
        "N1_1283": {"example_sentence": "（（要）よう）さ（さ）を（を）保っ（たもっ）て（て）ください。", "example_reading": "ようさをたもってください。", "example_meaning_cn": "请保持要领（或妖气）。", "example_meaning_en": "Please maintain the main point / charm."},
        "N1_1284": {"example_sentence": "（（要）よう）さ（さ）い（い）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "ようさいをまもりましょう。", "example_meaning_cn": "守卫要塞（堡垒）吧。", "example_meaning_en": "Let's defend the fortress / stronghold."},
        "N1_1285": {"example_sentence": "（（要）よう）し（し）に（に）なり（なり）たい（たい）です。", "example_reading": "ようしになりたいです。", "example_meaning_cn": "想成为养子（或拥有容貌）。", "example_meaning_en": "I want to be an adopted child / have a good appearance."},
        "N1_1286": {"example_sentence": "（（容）よう）し（し）ゅ（ゅ）う（う）し（し）て（て）ください。", "example_reading": "ようしゅうしてください。", "example_meaning_cn": "请使其成形（或已经收集）。", "example_meaning_en": "Please shape it / collect it."},
        "N1_1287": {"example_sentence": "（（要）よう）し（し）ょ（ょ）を（を）押さえ（おさえ）て（て）ください。", "example_reading": "ようしょをおさえてください。", "example_meaning_cn": "请守住要其（重点）。", "example_meaning_en": "Please secure the strategic point / focus on the main parts."},
        "N1_1288": {"example_sentence": "（（要）よう）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "ようしんしないでください。", "example_meaning_cn": "请不要（有心或唯心）。", "example_meaning_en": "Please don't (have a mind / be idealistic)."},
        "N1_1289": {"example_sentence": "（（要）よう）す（す）う（う）を（を）数え（かぞえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "ようすうをかぞえましょう。", "example_meaning_cn": "数数要素（或数量）吧。", "example_meaning_en": "Let's count the number of factors / elements."},
        "N1_1290": {"example_sentence": "（（要）よう）せ（せ）い（い）し（し）て（て）ください。", "example_reading": "ようせいしてください。", "example_meaning_cn": "请请求（要请）。", "example_meaning_en": "Please request / call for it."},
        "N1_1291": {"example_sentence": "（（養）よう）せ（せ）い（い）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "ようせいをたのしみましょう。", "example_meaning_cn": "享受晚年（或保养）吧。", "example_meaning_en": "Let's enjoy our later years / recreation."},
        "N1_1292": {"example_sentence": "（（妖）よう）せ（せ）い（い）を（を）信じ（しんじ）ま（ま）す（す）か。", "example_reading": "ようせいをしんじますか。", "example_meaning_cn": "你相信妖精吗？", "example_meaning_en": "Do you believe in fairies?"},
        "N1_1293": {"example_sentence": "（（要）よう）せ（せ）つ（つ）し（し）て（て）ください。", "example_reading": "ようせつしてください。", "example_meaning_cn": "请总结要点（或已经简化）。", "example_meaning_en": "Please summarize the main points."},
        "N1_1294": {"example_sentence": "（（様）よう）ぞ（ぞ）う（う）し（し）て（て）ください。", "example_reading": "ようぞうしてください。", "example_meaning_cn": "请使其成形（或已经制作）。", "example_meaning_en": "Please shape / make it."},
        "N1_1295": {"example_sentence": "（（容）よう）た（た）い（い）を（を）見守り（みまもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "ようたいをみまもりましょう。", "example_meaning_cn": "监视病情（或事态）吧。", "example_meaning_en": "Let's watch the patient's condition / state of affairs."},
        "N1_1296": {"example_sentence": "（（要）よう）だ（だ）ん（ん）し（し）ないで（为）ください。", "example_reading": "ようだんしないでください。", "example_meaning_cn": "请不要（说预言或闲聊）。", "example_meaning_en": "Please don't speak prophecies / talk."},
        "N1_1297": {"example_sentence": "（（要）よう）ち（ち）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "ようちをまもりましょう。", "example_meaning_cn": "守卫要地吧。", "example_meaning_en": "Let's defend the important ground."},
        "N1_1298": {"example_sentence": "（（幼）よう）ち（ち）な（な）考え（かんがえ）を（を）捨て（すて）ま（ま）しょ（しょ）う（う）。", "example_reading": "ようちなかんがえをすてましょう。", "example_meaning_cn": "抛弃幼稚的想法吧。", "example_meaning_en": "Let's discard such childish ideas."},
        "N1_1299": {"example_sentence": "（（要）よう）て（て）ん（ん）を（を）まとめ（まとめ）て（て）ください。", "example_reading": "ようてんをまとめてください。", "example_meaning_cn": "请总结要点。", "example_meaning_en": "Please summarize the main points."},
        "N1_1300": {"example_sentence": "（（用）よう）に（に）し（し）て（て）ください。", "example_reading": "ようにしてください。", "example_meaning_cn": "请使其有用（或已经准备）。", "example_meaning_en": "Please make it useful / ready."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_1300.")

if __name__ == "__main__":
    main()
