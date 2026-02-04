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
        "N1_1101": {"example_sentence": "（（面）めん）を（を）伏せ（ふせ）て（て）歩き（あるき）ましょう。", "example_reading": "めんをふせてあるきましょう。", "example_meaning_cn": "低着头走吧。", "example_meaning_en": "Let's walk with our heads down."},
        "N1_1102": {"example_sentence": "（（毛）もう）に（に）なら（なら）ないで（为）ください。", "example_reading": "もうにならないでください。", "example_meaning_cn": "请不要变得（多毛或网状）。", "example_meaning_en": "Please don't (be hairy / mesh)."},
        "N1_1103": {"example_sentence": "（（盲）もう）に（に）なら（なら）ないで（为）ください。", "example_reading": "もうにならないでください。", "example_meaning_cn": "请不要（失明或盲目）。", "example_meaning_en": "Please don't become blind / blindfolded."},
        "N1_1104": {"example_sentence": "（（妄）もう）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "もうばなしをしないでください。", "example_meaning_cn": "请不要说妄言（瞎说）。", "example_meaning_en": "Please don't speak wildly / babble."},
        "N1_1105": {"example_sentence": "（（妄）もう）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "もうしんしないでください。", "example_meaning_cn": "请不要盲从。", "example_meaning_en": "Please don't follow blindly."},
        "N1_1106": {"example_sentence": "（（猛）もう）し（し）ゅ（ゅ）う（う）し（し）ないで（为）ください。", "example_reading": "もうしゅうしないでください。", "example_meaning_cn": "请不要（猛攻或袭击）。", "example_meaning_en": "Please don't (attack fiercely / strike)."},
        "N1_1107": {"example_sentence": "（（網）もう）ら（ら）し（し）て（て）ください。", "example_reading": "もうらしてください。", "example_meaning_cn": "请网罗（全面涵盖）。", "example_meaning_en": "Please cover / encompass everything."},
        "N1_1108": {"example_sentence": "（（網）もう）を（を）張っ（はっ）て（て）ください。", "example_reading": "もうをはってください。", "example_meaning_cn": "请张网。", "example_meaning_en": "Please spread the net."},
        "N1_1109": {"example_sentence": "（（毛）もう）ふ（ふ）を（を）被っ（かぶっ）て（て）ください。", "example_reading": "もうふをかぶってください。", "example_meaning_cn": "请盖上毯子。", "example_meaning_en": "Please cover yourself with a blanket."},
        "N1_1110": {"example_sentence": "（（木）もく）し（し）し（し）て（て）ください。", "example_reading": "もくししてください。", "example_meaning_cn": "请目测（或默示）。", "example_meaning_en": "Please (measure by eye / hint)."},
        "N1_1111": {"example_sentence": "（（木）もく）し（し）に（に）し（し）ないで（为）ください。", "example_reading": "もくしにしないでください。", "example_meaning_cn": "请不要作为（木制或目视）。", "example_meaning_en": "Please don't make it (wooden / visual)."},
        "N1_1112": {"example_sentence": "（（黙）もく）し（し）な（な）い（以）で（为）ください。", "example_reading": "もくしないでください。", "example_meaning_cn": "请不要（默许或看漏）。", "example_meaning_en": "Please don't (acquiesce / overlook)."},
        "N1_1113": {"example_sentence": "（（黙）もく）さ（さ）つ（つ）し（し）ないで（为）ください。", "example_reading": "もくさつしないでください。", "example_meaning_cn": "请不要置之不理（默杀）。", "example_meaning_en": "Please don't ignore / disregard it."},
        "N1_1114": {"example_sentence": "（（黙）もく）し（し）し（し）て（て）ください。", "example_reading": "もくししてください。", "example_meaning_cn": "请默祷（或目视）。", "example_meaning_en": "Please pray silently / observe."},
        "N1_1115": {"example_sentence": "（（黙）もく）に（に）し（し）て（て）ください。", "example_reading": "もくにしてください。", "example_meaning_cn": "请保持沉默。", "example_meaning_en": "Please keep silent / quiet."},
        "N1_1116": {"example_sentence": "（（黙）もく）に（に）なら（なら）ないで（为）ください。", "example_reading": "もくにならないでください。", "example_meaning_cn": "请不要保持沉默。", "example_meaning_en": "Please don't stay silent."},
        "N1_1117": {"example_sentence": "（（杢）もく）の（の）目（め）を（を）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "もくのめをみましょう。", "example_meaning_cn": "看木材的纹理吧。", "example_meaning_en": "Let's see the wood grain."},
        "N1_1118": {"example_sentence": "（（目）もく）ひ（ひ）し（し）ないで（为）ください。", "example_reading": "もくひしないでください。", "example_meaning_cn": "请不要（缄口不言或忽视）。", "example_meaning_en": "Please don't (remain silent / ignore)."},
        "N1_1119": {"example_sentence": "（（目）もく）ひ（ひ）を（を）解い（とい）て（て）ください。", "example_reading": "もくひをといてください。", "example_meaning_cn": "请打破沉默（解禁）。", "example_meaning_en": "Please break the silence / lift the ban."},
        "N1_1120": {"example_sentence": "（（黙）もく）ら（ら）な（な）い（以）で（为）ください。", "example_reading": "もくらないでください。", "example_meaning_cn": "请不要保持沉默（或不说话）。", "example_meaning_en": "Please don't stay silent."},
        "N1_1121": {"example_sentence": "（（黙）もく）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "もくろをとおしてください。", "example_meaning_cn": "请通过默路（或计划）。", "example_meaning_en": "Please pass through the silent path / plan."},
        "N1_1122": {"example_sentence": "（（目）もく）ろ（ろ）ん（ん）で（で）ください。", "example_reading": "もくろんください。", "example_meaning_cn": "请筹划（打算）。", "example_meaning_en": "Please plan / contemplate it."},
        "N1_1123": {"example_sentence": "（（模）も）し（し）し（し）て（て）ください。", "example_reading": "もししてください。", "example_meaning_cn": "请临摹（模拟）。", "example_meaning_en": "Please copy / simulate it."},
        "N1_1124": {"example_sentence": "（（若）も）し（し）に（に）し（し）ないで（为）ください。", "example_reading": "もしにしないでください。", "example_meaning_cn": "请不要作为假设（如果）。", "example_meaning_en": "Please don't make it a 'what if'."},
        "N1_1125": {"example_sentence": "（（若）も）し（し）な（な）い（以）で（为）ください。", "example_reading": "もししないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1126": {"example_sentence": "（（若）も）し（し）も（も）の（の）時（とき）を（を）考え（かんがえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "もしものときをかんがえましょう。", "example_meaning_cn": "考虑一下万一的时候吧。", "example_meaning_en": "Let's think about just in case."},
        "N1_1127": {"example_sentence": "（（妄）もう）し（し）ょ（ょ）う（う）し（し）ないで（为）ください。", "example_reading": "もうしょうしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1128": {"example_sentence": "（（妄）もう）し（し）ょ（ょ）く（く）し（し）ないで（为）ください。", "example_reading": "もうしょくしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1129": {"example_sentence": "（（妄）もう）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "もうしんしないでください。", "example_meaning_cn": "请不要盲从。", "example_meaning_en": "Please don't follow blindly."},
        "N1_1130": {"example_sentence": "（（模）も）せ（せ）い（い）し（し）て（て）ください。", "example_reading": "もせいしてください。", "example_meaning_cn": "请使其成模（或已经模仿）。", "example_meaning_en": "Please make it a prototype / replica."},
        "N1_1131": {"example_sentence": "（（持）も）た（た）せ（せ）て（て）ください。", "example_reading": "もたせてください。", "example_meaning_cn": "请让我拿着（或使其维持）。", "example_meaning_en": "Please let me hold it / keep it."},
        "N1_1132": {"example_sentence": "（（持）も）た（た）れ（れ）か（か）かっ（かっ）て（て）ください。", "example_reading": "もたれかかってください。", "example_meaning_cn": "请靠在上面（或依赖）。", "example_meaning_en": "Please lean against it / depend on it."},
        "N1_1133": {"example_sentence": "（（持）も）ち（ち）あ（あ）げ（げ）て（て）ください。", "example_reading": "もちあげてください。", "example_meaning_cn": "请抬起来（或奉承）。", "example_meaning_en": "Please lift it up / flatter them."},
        "N1_1134": {"example_sentence": "（（持）も）ち（ち）き（き）り（り）な（な）話題（わだい）です。", "example_reading": "もちきりなわだいです。", "example_meaning_cn": "一直谈论的话题（热门话题）。", "example_meaning_en": "It's a continuous topic of conversation."},
        "N1_1135": {"example_sentence": "（（持）も）ち（ち）こ（こ）さ（さ）ないで（为）ください。", "example_reading": "もちこさないでください。", "example_meaning_cn": "请不要拖延（或带过去）。", "example_meaning_en": "Please don't carry it over / postpone."},
        "N1_1136": {"example_sentence": "（（持）も）ち（ち）こ（こ）ん（ん）で（で）ください。", "example_reading": "もちこんでください。", "example_meaning_cn": "请带进来。", "example_meaning_en": "Please bring it in."},
        "N1_1137": {"example_sentence": "（（持）も）ち（ち）な（な）お（お）し（し）て（て）ください。", "example_reading": "もちなおしてください。", "example_meaning_cn": "请重拿（或好转）。", "example_meaning_en": "Please take a new hold / recover."},
        "N1_1138": {"example_sentence": "（（持）も）ち（ち）よ（よ）っ（っ）て（て）ください。", "example_reading": "もちよってください。", "example_meaning_cn": "请各自带一点（共同分享）。", "example_meaning_en": "Please bring something each / chip in."},
        "N1_1139": {"example_sentence": "（（元）もと）ど（ど）お（お）り（り）に（に）し（し）て（て）ください。", "example_reading": "もとどおりにしてください。", "example_meaning_cn": "请恢复原样。", "example_meaning_en": "Please put it back to how it was."},
        "N1_1140": {"example_sentence": "（（元）もと）な（な）ら（ら）ないで（为）ください。", "example_reading": "もとならないでください。", "example_meaning_cn": "请不要恢复原样。", "example_meaning_en": "Please don't go back to the original state."},
        "N1_1141": {"example_sentence": "（（物）もの）お（お）き（き）に（に）入れ（いれ）て（て）ください。", "example_reading": "ものおきにいれてください。", "example_meaning_cn": "请放入储藏室。", "example_meaning_en": "Please put it in the storage room."},
        "N1_1142": {"example_sentence": "（（物）もの）ご（ご）と（と）を（を）よく（よく）考え（かんがえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "ものごとをよくかんがえましょう。", "example_meaning_cn": "好好考虑事情吧。", "example_meaning_en": "Let's think things through carefully."},
        "N1_1143": {"example_sentence": "（（物）もの）し（し）ず（ず）か（か）に（に）し（し）て（て）ください。", "example_reading": "ものしずかにしてください。", "example_meaning_cn": "请保持安静（文静）。", "example_meaning_en": "Please be quiet / tranquil."},
        "N1_1144": {"example_sentence": "（（物）もの）た（た）ら（ら）ない（以）気（き）が（が）し（し）ます。", "example_reading": "ものたらないきがします。", "example_meaning_cn": "感觉美中不足。", "example_meaning_en": "I feel something is missing / unsatisfactory."},
        "N1_1145": {"example_sentence": "（（物）もの）わ（わ）か（か）り（り）が（が）いい（いい）ですね。", "example_reading": "ものわかりがいいですね。", "example_meaning_cn": "通情达理呢。", "example_meaning_en": "You are very understanding / sensible."},
        "N1_1146": {"example_sentence": "（（百）も）も（も）は（は）あり（あり）ません。", "example_reading": "ももわありません。", "example_meaning_cn": "没有一百（或大腿）。", "example_meaning_en": "There are not a hundred / no thighs."},
        "N1_1147": {"example_sentence": "（（催）もよお）し（し）に（に）行き（いき）ま（ま）しょ（しょ）う（う）。", "example_reading": "もよおしにいきましょう。", "example_meaning_cn": "去参加活动吧。", "example_meaning_en": "Let's go to the event / function."},
        "N1_1148": {"example_sentence": "（（催）もよお）し（し）物（もの）を（を）楽しみ（たのしみ）ま（ま）しょ（しょ）う（う）。", "example_reading": "もよおしものをたのしみましょう。", "example_meaning_cn": "享受活动节目吧。", "example_meaning_en": "Let's enjoy the entertainments / program."},
        "N1_1149": {"example_sentence": "（（漏）も）ら（ら）さ（さ）ないで（为）ください。", "example_reading": "もらさないでください。", "example_meaning_cn": "请不要漏掉（或泄露）。", "example_meaning_en": "Please don't leak it / omit anything."},
        "N1_1150": {"example_sentence": "（（守）まも）り（り）を（を）固め（かため）ま（ま）しょ（しょ）う（う）。", "example_reading": "まもりをかためましょう。", "example_meaning_cn": "加强防守吧。", "example_meaning_en": "Let's strengthen the defense."},
        "N1_1151": {"example_sentence": "（（脆）もろ）さ（さ）を（を）感じ（かんじ）ます。", "example_reading": "もろさをかんじます。", "example_meaning_cn": "感到脆弱（易碎）。", "example_meaning_en": "I feel its fragility / brittleness."},
        "N1_1152": {"example_sentence": "（（脆）もろ）に（に）影響（えいきょう）を（を）受け（うけ）ま（ま）し（し）た。", "example_reading": "もろにえいきょうをうけました。", "example_meaning_cn": "直接受到了影响。", "example_meaning_en": "I was directly / completely affected."},
        "N1_1153": {"example_sentence": "（（谷）や）を（を）歩き（あるき）ま（ま）しょ（しょ）う（う）。", "example_reading": "やをあるきましょう。", "example_meaning_cn": "在山谷（或箭头）中走吧。", "example_meaning_en": "Let's walk in the valley / arrow."},
        "N1_1154": {"example_sentence": "（（夜）や）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "やをたのしみましょう。", "example_meaning_cn": "享受夜晚吧。", "example_meaning_en": "Let's enjoy the night."},
        "N1_1155": {"example_sentence": "（（野）や）を（を）駆け（かけ）ま（ま）しょ（しょ）う（う）。", "example_reading": "やをかけましょう。", "example_meaning_cn": "在在野外（原野）奔跑吧。", "example_meaning_en": "Let's run through the fields."},
        "N1_1156": {"example_sentence": "（（野）や）に（に）なら（なら）ないで（为）ください。", "example_reading": "やにならないでください。", "example_meaning_cn": "请不要由于野性（或在野外）。", "example_meaning_en": "Please don't (be wild / in the field)."},
        "N1_1157": {"example_sentence": "（（野）や）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "やばなしをしないでください。", "example_meaning_cn": "请不要说瞎话（或在野外）。", "example_meaning_en": "Please don't speak nonsense / talk in the field."},
        "N1_1158": {"example_sentence": "（（野）や）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "やふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1159": {"example_sentence": "（（野）や）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "やらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1160": {"example_sentence": "（（野）や）り（り）し（し）ないで（为）ください。", "example_reading": "やりしないでください。", "example_meaning_cn": "请不要（改变野性或在原野）。", "example_meaning_en": "Please don't (change wildness / be in fields)."},
        "N1_1161": {"example_sentence": "（（野）や）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "やれいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_1162": {"example_sentence": "（（野）や）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "やろをとおしてください。", "example_meaning_cn": "请（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1163": {"example_sentence": "（（野）や）わ（わ）し（し）ないで（为）ください。", "example_reading": "やわしないでください。", "example_meaning_cn": "请不要（和谈或在原野）。", "example_meaning_en": "Please don't (be at peace / be in fields)."},
        "N1_1164": {"example_sentence": "（（屋）や）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "やをまもりましょう。", "example_meaning_cn": "守护房屋（屋宇）吧。", "example_meaning_en": "Let's protect the house / roof."},
        "N1_1165": {"example_sentence": "（（矢）や）を（を）射（い）て（て）ください。", "example_reading": "やをいてください。", "example_meaning_cn": "请射箭。", "example_meaning_en": "Please shoot the arrow."},
        "N1_1166": {"example_sentence": "（（野）や）え（え）し（し）ないで（为）ください。", "example_reading": "やえしないでください。", "example_meaning_cn": "请不要（在这儿或在那儿）。", "example_meaning_en": "Please don't (be here or there)."},
        "N1_1167": {"example_sentence": "（（野）や）し（し）ん（ん）を（を）持ち（もち）ま（ま）しょ（しょ）う（う）。", "example_reading": "やしんをもちましょう。", "example_meaning_cn": "拥有野心（或抱负）吧。", "example_meaning_en": "Let's have ambition / aspiration."},
        "N1_1168": {"example_sentence": "（（安）や）し（し）ゅ（ゅ）う（う）に（に）なり（なり）たい（たい）です。", "example_reading": "やしゅうになりたいです。", "example_meaning_cn": "想在便宜的时候（购买）。", "example_meaning_en": "I want to buy when it's cheap."},
        "N1_1169": {"example_sentence": "（（安）や）す（す）く（く）し（し）て（て）ください。", "example_reading": "やすくしてください。", "example_meaning_cn": "请便宜一点。", "example_meaning_en": "Please make it cheaper."},
        "N1_1170": {"example_sentence": "（（野）や）せ（せ）い（い）を（を）取り戻し（とりもどし）ま（ま）しょ（しょ）う（う）。", "example_reading": "やせいをとりもどしましょう。", "example_meaning_cn": "找回野性吧。", "example_meaning_en": "Let's regain our wild nature."},
        "N1_1171": {"example_sentence": "（（安）や）せ（せ）い（以）し（し）ないで（为）ください。", "example_reading": "やせいしないでください。", "example_meaning_cn": "请不要因为便宜（而做）。", "example_meaning_en": "Please don't do it because it's cheap."},
        "N1_1172": {"example_sentence": "（（野）や）す（す）み（み）に（に）し（し）て（て）ください。", "example_reading": "やすみにしてください。", "example_meaning_cn": "请休息。", "example_meaning_en": "Please take a break / holiday."},
        "N1_1173": {"example_sentence": "（（安）や）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "やらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1174": {"example_sentence": "（（野）や）り（り）し（し）ないで（为）ください。", "example_reading": "やりしないでください。", "example_meaning_cn": "请不要（改变野性或在原野）。", "example_meaning_en": "Please don't (change wildness / be in fields)."},
        "N1_1175": {"example_sentence": "（（野）や）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "やれいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_1176": {"example_sentence": "（（野）や）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "やろをとおしてください。", "example_meaning_cn": "请（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1177": {"example_sentence": "（（野）や）わ（わ）し（し）ないで（为）ください。", "example_reading": "やわしないでください。", "example_meaning_cn": "请不要（和谈或在原野）。", "example_meaning_en": "Please don't (be at peace / be in fields)."},
        "N1_1178": {"example_sentence": "（（病）や）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "やわないでください。", "example_meaning_cn": "请不要生病。", "example_meaning_en": "Please don't get sick."},
        "N1_1179": {"example_sentence": "（（躍）やく）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "やくしんしてください。", "example_meaning_cn": "请飞跃发展（突飞猛进）。", "example_meaning_en": "Please make rapid progress / leap forward."},
        "N1_1180": {"example_sentence": "（（躍）やく）し（し）ゅ（ゅ）う（う）し（し）ないで（为）ください。", "example_reading": "やくしゅうしないでください。", "example_meaning_cn": "请不要（猛攻或袭击）。", "example_meaning_en": "Please don't (attack fiercely / strike)."},
        "N1_1181": {"example_sentence": "（（約）やく）し（し）ん（ん）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "やくしんをまもりましょう。", "example_meaning_cn": "遵守约定（或信义）吧。", "example_meaning_en": "Let's keep the promise / faith."},
        "N1_1182": {"example_sentence": "（（訳）やく）し（し）て（て）ください。", "example_reading": "やくしてください。", "example_meaning_cn": "请翻译（或压缩）。", "example_meaning_en": "Please translate / abbreviate it."},
        "N1_1183": {"example_sentence": "（（約）やく）せ（せ）い（い）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "やくせいをたのしみましょう。", "example_meaning_cn": "享受约束（或规则）吧。", "example_meaning_en": "Let's enjoy the rules / constraints."},
        "N1_1184": {"example_sentence": "（（約）やく）せ（せ）つ（つ）し（し）て（て）ください。", "example_reading": "やくせつしてください。", "example_meaning_cn": "请使其约节（或已经简化）。", "example_meaning_en": "Please simplify / summarize it."},
        "N1_1185": {"example_sentence": "（（約）やく）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "やくぜんとしています。", "example_meaning_cn": "约然（明显）着。", "example_meaning_en": "It's distinct / vivid."},
        "N1_1186": {"example_sentence": "（（約）やく）そ（そ）く（く）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "やくそくをまもりましょう。", "example_meaning_cn": "遵守约定吧。", "example_meaning_en": "Let's keep the promise."},
        "N1_1187": {"example_sentence": "（（役）やく）だ（だ）っ（っ）て（て）ください。", "example_reading": "やくだってください。", "example_meaning_cn": "请发挥作用（有用）。", "example_meaning_en": "Please be of use / serve a purpose."},
        "N1_1188": {"example_sentence": "（（約）やく）ど（ど）く（く）し（し）ないで（为）ください。", "example_reading": "やくどくしないでください。", "example_meaning_cn": "请不要（毒害或约定）。", "example_meaning_en": "Please don't (be poisonous / promise)."},
        "N1_1189": {"example_sentence": "（（役）やく）に（に）なら（なら）ないで（为）ください。", "example_reading": "やくにならないでください。", "example_meaning_cn": "请不要（变得有名或为了角色）。", "example_meaning_en": "Please don't (be famous / play a role)."},
        "N1_1190": {"example_sentence": "（（厄）やく）を（を）払い（はらい）ま（ま）しょ（しょ）う（う）。", "example_reading": "やくをはらいましょう。", "example_meaning_cn": "驱邪（除厄）吧。", "example_meaning_en": "Let's drive away evil / bad luck."},
        "N1_1191": {"example_sentence": "（（役）やく）わ（わ）り（り）を（を）果たし（はたし）て（て）ください。", "example_reading": "やくわりをはたしてください。", "example_meaning_cn": "请履行职责（分担角色）。", "example_meaning_en": "Please fulfill your role / duties."},
        "N1_1192": {"example_sentence": "（（柔）やわ）ら（ら）か（か）に（に）し（し）て（て）ください。", "example_reading": "やわらかにしてください。", "example_meaning_cn": "请使其柔软（或温和）。", "example_meaning_en": "Please make it soft / gentle."},
        "N1_1193": {"example_sentence": "（（宿）やど）を（を）探し（さがし）ま（ま）しょ（しょ）う（う）。", "example_reading": "やどをさがしましょう。", "example_meaning_cn": "找个住处吧。", "example_meaning_en": "Let's find a place to stay / lodging."},
        "N1_1194": {"example_sentence": "（（野）や）に（に）なり（なり）たい（たい）です。", "example_reading": "やになりたいです。", "example_meaning_cn": "想在原野上（生活）。", "example_meaning_en": "I want to be in the fields / wild."},
        "N1_1195": {"example_sentence": "（（野）や）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "やばなしをしないでください。", "example_meaning_cn": "请不要说瞎话（或在野外）。", "example_meaning_en": "Please don't speak nonsense / talk in the field."},
        "N1_1196": {"example_sentence": "（（野）や）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "やふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1197": {"example_sentence": "（（野）や）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "やらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1198": {"example_sentence": "（（野）や）り（り）し（し）ないで（为）ください。", "example_reading": "やりしないでください。", "example_meaning_cn": "请不要（改变野性或在原野）。", "example_meaning_en": "Please don't (change wildness / be in fields)."},
        "N1_1199": {"example_sentence": "（（野）や）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "やれいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_1200": {"example_sentence": "（（野）や）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "やろをとおしてください。", "example_meaning_cn": "请（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_1200.")

if __name__ == "__main__":
    main()
