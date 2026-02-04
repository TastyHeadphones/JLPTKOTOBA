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
        "N2_1101": {"example_sentence": "（（終）しゅう）し（し）て（て）ください。", "example_reading": "しゅうしてください。", "example_meaning_cn": "请终结（或练习）。", "example_meaning_en": "Please finish it/practice."},
        "N2_1102": {"example_sentence": "（（充）じゅう）じ（じ）つ（つ）し（し）て（て）いますね。", "example_reading": "じゅうじつしていますね。", "example_meaning_cn": "真充实呢。", "example_meaning_en": "It's very fulfilling, isn't it?"},
        "N2_1103": {"example_sentence": "（（修）しゅう）し（し）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "しゅうしょうしてください。", "example_meaning_cn": "请修饰（或褒奖）。", "example_meaning_en": "Please decorate/mend it."},
        "N2_1104": {"example_sentence": "（（執）しゅう）し（し）ょ（ょ）く（く）し（し）て（て）ください。", "example_reading": "しゅうしょくしてください。", "example_meaning_cn": "请就职。", "example_meaning_en": "Please find employment."},
        "N2_1105": {"example_sentence": "（（執）しゅう）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "しゅうしんしてください。", "example_meaning_cn": "请执着（或就寝）。", "example_meaning_en": "Please be persistent/go to bed."},
        "N2_1106": {"example_sentence": "（（充）じゅう）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "じゅうしんしてください。", "example_meaning_cn": "请充实（或重心）。", "example_meaning_en": "Please enrich/balance."},
        "N2_1107": {"example_sentence": "（（終）しゅう）せ（せ）つ（つ）し（し）て（て）ください。", "example_reading": "しゅうせつしてください。", "example_meaning_cn": "请终结（或收尾）。", "example_meaning_en": "Please conclude it."},
        "N2_1108": {"example_sentence": "（（修）しゅう）ぜ（ぜ）ん（ん）し（し）て（て）ください。", "example_reading": "しゅうぜんしてください。", "example_meaning_cn": "请修缮（修理）。", "example_meaning_en": "Please repair/mend it."},
        "N2_1109": {"example_sentence": "（（渋）じゅう）た（た）い（い）し（し）て（て）います。", "example_reading": "じゅうたいしています。", "example_meaning_cn": "正在受阻（滞留/严重病情）。", "example_meaning_en": "It's congested/in a serious condition."},
        "N2_1110": {"example_sentence": "（（充）じゅう）た（た）ん（ん）し（し）て（て）ください。", "example_reading": "じゅうたんしてください。", "example_meaning_cn": "请充填（或地毯）。", "example_meaning_en": "Please fill it up (or carpet)."},
        "N2_1111": {"example_sentence": "（（執）しゅう）ち（ち）ゃ（ゃ）く（く）し（し）ないで（で）ください。", "example_reading": "しゅうちゃくしないでください。", "example_meaning_cn": "请不要执着。", "example_meaning_en": "Please don't be obsessed."},
        "N2_1112": {"example_sentence": "（（終）しゅう）ち（ち）ゃ（ゃ）く（く）に（に）行き（いき）ましょう。", "example_reading": "しゅうちゃくにいきましょう。", "example_meaning_cn": "去终点（终着）吧。", "example_meaning_en": "Let's go to the final destination."},
        "N2_1113": {"example_sentence": "（（週）しゅう）ち（ち）ゅう（ゅう）し（し）て（て）ください。", "example_reading": "しゅうちゅうしてください。", "example_meaning_cn": "请集中（注意）。", "example_meaning_en": "Please concentrate."},
        "N2_1114": {"example_sentence": "（（終）しゅう）て（て）ん（ん）に（に）着き（つき）まし（し）た。", "example_reading": "しゅうてんに着きました。", "example_meaning_cn": "到达终点站了。", "example_meaning_en": "We've arrived at the end of the line."},
        "N2_1115": {"example_sentence": "（（収）しゅう）に（に）ゅう（ゅう）を（を）増やし（ふやし）たい（たい）です。", "example_reading": "しゅうにゅうをふやしたいです。", "example_meaning_cn": "想增加收入。", "example_meaning_en": "I want to increase my income."},
        "N2_1116": {"example_sentence": "（（祝）しゅう）は（は）い（い）を（を）あげ（あげ）ましょう。", "example_reading": "しゅうはいをあげましょう。", "example_meaning_cn": "祝酒吧。", "example_meaning_en": "Let's raise a celebratory glass."},
        "N2_1117": {"example_sentence": "（（週）しゅう）ふ（ふ）く（く）し（し）て（て）ください。", "example_reading": "しゅうふくしてください。", "example_meaning_cn": "请修复周期（或修复）。", "example_meaning_en": "Please restore/repair it."},
        "N2_1118": {"example_sentence": "（（終）しゅう）ほ（ほ）う（う）を（を）待っ（まっ）て（て）ください。", "example_reading": "しゅうほうをまってください。", "example_meaning_cn": "请等候终报（或周报）。", "example_meaning_en": "Please wait for the final report."},
        "N2_1119": {"example_sentence": "（（執）しゅう）み（み）ょ（ょ）う（う）な（な）態度（たいど）です。", "example_reading": "しゅうみょうなたいどです。", "example_meaning_cn": "执拗（顽强）的态度。", "example_meaning_en": "A persistent/stubborn attitude."},
        "N2_1120": {"example_sentence": "（（終）しゅう）り（り）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "しゅうりょうしてください。", "example_meaning_cn": "请结束。", "example_meaning_en": "Please finish/complete it."},
        "N2_1121": {"example_sentence": "（（修）しゅう）り（り）ょ（ょ）う（う）証（しょう）を（を）もらい（もらい）ます。", "example_reading": "しゅうりょうしょうをもらいます。", "example_meaning_cn": "领结业证书。", "example_meaning_en": "Receiving a certificate of completion."},
        "N2_1122": {"example_sentence": "（（収）しゅ）く（く）を（を）集め（あつめ）て（て）ください。", "example_reading": "しゅくをあつめてください。", "example_meaning_cn": "请收集句子（或住宿）。", "example_meaning_en": "Please gather the phrases/stay overnight."},
        "N2_1123": {"example_sentence": "（（主）しゅ）く（く）を（を）称え（たたえ）ましょう。", "example_reading": "しゅくをたたえましょう。", "example_meaning_cn": "赞美主（或功勋）吧。", "example_meaning_en": "Let's praise the Lord."},
        "N2_1124": {"example_sentence": "（（祝）しゅ）く（く）が（が）を（を）述べ（のべ）ましょう。", "example_reading": "しゅくがをのべましょう。", "example_meaning_cn": "表示祝贺吧。", "example_meaning_en": "Let's offer our congratulations."},
        "N2_1125": {"example_sentence": "（（宿）しゅ）く（く）ちゃ（ちゃ）く（く）し（し）て（て）ください。", "example_reading": "しゅくちゃくしてください。", "example_meaning_cn": "请值宿（值班）。", "example_meaning_en": "Please stay on night duty."},
        "N2_1126": {"example_sentence": "（（祝）しゅ）く（く）じ（じ）つ（つ）は（は）休み（やすみ）です。", "example_reading": "しゅくじつわやすみです。", "example_meaning_cn": "节日休息。", "example_meaning_en": "Public holidays are days off."},
        "N2_1127": {"example_sentence": "（（縮）しゅ）く（く）し（し）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "しゅくしょうしてください。", "example_meaning_cn": "请缩小。", "example_meaning_en": "Please reduce/downsize it."},
        "N2_1128": {"example_sentence": "（（主）しゅ）く（く）て（て）ん（ん）を（を）見（み）て（て）ください。", "example_reading": "しゅくてんをみてください。", "example_meaning_cn": "请看重点（或庆典）。", "example_meaning_en": "Please see the main point/celebration."},
        "N2_1129": {"example_sentence": "（（宿）しゅ）く（く）は（は）く（く）し（し）て（て）ください。", "example_reading": "しゅくはくしてください。", "example_meaning_cn": "请住宿。", "example_meaning_en": "Please stay overnight."},
        "N2_1130": {"example_sentence": "（（主）しゅ）し（し）を（を）話し（はなし）て（て）ください。", "example_reading": "しゅしをおなしてください。", "example_meaning_cn": "请说明主旨（宗旨）。", "example_meaning_en": "Please explain the purpose/intent."},
        "N2_1131": {"example_sentence": "（（守）しゅ）し（し）て（て）ください。", "example_reading": "しゅしてください。", "example_meaning_cn": "请遵守（守护）。", "example_meaning_en": "Please observe/protect it."},
        "N2_1132": {"example_sentence": "（（種）しゅ）じ（じ）ゅ（ゅ）な（な）品（しな）があり（あり）ます。", "example_reading": "しゅじゅなしながあります。", "example_meaning_cn": "有各种各样的物品。", "example_meaning_en": "There are various kinds of items."},
        "N2_1133": {"example_sentence": "（（手）しゅ）じ（じ）ゅ（ゅ）つ（つ）し（し）て（て）ください。", "example_reading": "しゅじゅつしてください。", "example_meaning_cn": "请做手术。", "example_meaning_en": "Please perform surgery."},
        "N2_1134": {"example_sentence": "（（主）しゅ）じ（じ）ょ（ょ）し（し）て（て）ください。", "example_reading": "しゅじょしてください。", "example_meaning_cn": "请主理（主持）。", "example_meaning_en": "Please preside over it."},
        "N2_1135": {"example_sentence": "（（首）しゅ）し（し）ょ（ょ）う（う）になり（なり）たい（たい）です。", "example_reading": "しゅしょうになりたいです。", "example_meaning_cn": "想当首相。", "example_meaning_en": "I want to become prime minister."},
        "N2_1136": {"example_sentence": "（（主）しゅ）す（す）い（い）し（し）て（て）ください。", "example_reading": "しゅすいしてください。", "example_meaning_cn": "请取水（主水）。", "example_meaning_en": "Please intake water."},
        "N2_1137": {"example_sentence": "（（手）しゅ）ぜ（ぜ）ん（ん）し（し）て（て）ください。", "example_reading": "しゅぜんしてください。", "example_meaning_cn": "请修理（修缮）。", "example_meaning_en": "Please repair it."},
        "N2_1138": {"example_sentence": "（（主）しゅ）た（た）い（い）てき（てき）に（に）動い（うごい）て（て）ください。", "example_reading": "しゅたいてきにうごいてください。", "example_meaning_cn": "请主动行动。", "example_meaning_en": "Please act proactively."},
        "N2_1139": {"example_sentence": "（（手）しゅ）だ（だ）ん（ん）を（を）選ば（えらば）ない（ない）で（で）ください。", "example_reading": "しゅだんをえらばないでください。", "example_meaning_cn": "请不择手段。", "example_meaning_en": "Please use any means necessary."},
        "N2_1140": {"example_sentence": "（（主）しゅ）ち（ち）ょ（ょ）く（く）し（し）て（て）ください。", "example_reading": "しゅちょくしてください。", "example_meaning_cn": "请值班（主直）。", "example_meaning_en": "Please be on duty."},
        "N2_1141": {"example_sentence": "（（主）しゅ）ち（ち）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "しゅちょうしてください。", "example_meaning_cn": "请主张。", "example_meaning_en": "Please assert/insist."},
         "N2_1142": {"example_sentence": "（（出）しゅ）っ（っ）か（か）し（し）て（て）ください。", "example_reading": "しゅっかしてください。", "example_meaning_cn": "请发货。", "example_meaning_en": "Please ship the goods."},
        "N2_1143": {"example_sentence": "（（出）しゅ）っ（っ）け（け）つ（つ）を（を）確認（かくにん）し（し）てください。", "example_reading": "しゅっけつをかくにんしてください。", "example_meaning_cn": "请确认出勤（出缺）。", "example_meaning_en": "Please check attendance."},
        "N2_1144": {"example_sentence": "（（出）しゅ）っ（っ）こ（こ）う（う）し（し）て（て）ください。", "example_reading": "しゅっこうしてください。", "example_meaning_cn": "请出港。", "example_meaning_en": "Please set sail."},
        "N2_1145": {"example_sentence": "（（出）しゅ）っ（っ）さ（さ）ん（ん）を（を）祝っ（いわっ）て（て）ください。", "example_reading": "しゅっさんをいわってください。", "example_meaning_cn": "请祝贺生产（出生）。", "example_meaning_en": "Please congratulate on the birth."},
        "N2_1146": {"example_sentence": "（（出）しゅ）っ（っ）し（し）し（し）て（て）ください。", "example_reading": "しゅっししてください。", "example_meaning_cn": "请出资。", "example_meaning_en": "Please invest/finance."},
        "N2_1147": {"example_sentence": "（（出）しゅ）っ（っ）し（し）ん（ん）は（は）どこ（どこ）ですか。", "example_reading": "しゅっしんわどこですか。", "example_meaning_cn": "出生地是哪里？", "example_meaning_en": "Where are you from?"},
        "N2_1148": {"example_sentence": "（（出）しゅ）っ（っ）せ（せ）い（い）を（を）祝っ（いわっ）て（て）ください。", "example_reading": "しゅっせいいをいわってください。", "example_meaning_cn": "请祝贺出世（出生）。", "example_meaning_en": "Please celebrate the birth."},
        "N2_1149": {"example_sentence": "（（出）しゅ）っ（っ）せ（せ）き（き）し（し）て（て）ください。", "example_reading": "しゅっせきしてください。", "example_meaning_cn": "请出席。", "example_meaning_en": "Please attend."},
        "N2_1150": {"example_sentence": "（（出）しゅ）っ（っ）ぱ（ぱ）つ（つ）し（し）ましょう。", "example_reading": "しゅっぱつしましょう。", "example_meaning_cn": "出发吧。", "example_meaning_en": "Let's depart."},
        "N2_1151": {"example_sentence": "（（出）しゅ）っ（っ）ぱ（ぱ）ん（ん）し（し）て（て）ください。", "example_reading": "しゅっぱんしてください。", "example_meaning_cn": "请出版。", "example_meaning_en": "Please publish it."},
        "N2_1152": {"example_sentence": "（（主）しゅ）に（に）ん（ん）を（を）任せ（まかせ）ます。", "example_reading": "しゅにんをまかせます。", "example_meaning_cn": "委任主任职务。", "example_meaning_en": "I'll appoint you as the person in charge."},
        "N2_1153": {"example_sentence": "（（手）しゅ）は（は）い（い）し（し）て（て）ください。", "example_reading": "しゅはいしてください。", "example_meaning_cn": "请指派（或调遣）。", "example_meaning_en": "Please arrange/dispatch."},
        "N2_1154": {"example_sentence": "（（首）しゅ）ふ（ふ）に（に）行き（いき）ましょう。", "example_reading": "しゅふにいきましょう。", "example_meaning_cn": "去首都吧。", "example_meaning_en": "Let's go to the capital city."},
        "N2_1155": {"example_sentence": "（（主）しゅ）ぼ（ぼ）う（う）し（し）て（て）ください。", "example_reading": "しゅぼうしてください。", "example_meaning_cn": "请主谋（谋划）。", "example_meaning_en": "Please mastermind/plan it."},
        "N2_1156": {"example_sentence": "（（手）しゅ）み（み）を（を）教えて（おしえて）ください。", "example_reading": "しゅみをおしえてください。", "example_meaning_cn": "请告诉我你的爱好。", "example_meaning_en": "Please tell me your hobby."},
        "N2_1157": {"example_sentence": "（（主）しゅ）め（め）い（い）を（を）受け（うけ）て（て）ください。", "example_reading": "しゅめいをうけてください。", "example_meaning_cn": "请接受指名（任命）。", "example_meaning_en": "Please accept the nomination/appointment."},
        "N2_1158": {"example_sentence": "（（種）しゅ）類（るい）を（を）分け（わけ）て（て）ください。", "example_reading": "しゅるいをわけてください。", "example_meaning_cn": "请分类。", "example_meaning_en": "Please sort them by kind."},
        "N2_1159": {"example_sentence": "（（主）しゅ）り（り）ょ（ょ）う（う）に（に）行き（いき）ましょう。", "example_reading": "しゅりょうにいきましょう。", "example_meaning_cn": "去打猎（狩猎）吧。", "example_meaning_en": "Let's go hunting."},
        "N2_1160": {"example_sentence": "（（旬）しゅん）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "しゅんをたのしみましょう。", "example_meaning_cn": "享受时令（应时）吧。", "example_meaning_en": "Let's enjoy the seasonal food."},
        "N2_1161": {"example_sentence": "（（巡）じゅん）し（し）に（に）行き（いき）ます。", "example_reading": "じゅんにいきます。", "example_meaning_cn": "去巡视（巡礼）。", "example_meaning_en": "I'm going on a tour/patrol."},
        "N2_1162": {"example_sentence": "（（順）じゅん）じ（じ）ょ（ょ）を（を）守り（まもり）ましょう。", "example_reading": "じゅんじょをまもりましょう。", "example_meaning_cn": "按顺序吧。", "example_meaning_en": "Let's follow the order."},
        "N2_1163": {"example_sentence": "（（順）じゅん）し（し）ん（ん）な（な）心（こころ）です。", "example_reading": "じゅんしんなこころです。", "example_meaning_cn": "纯真的心。", "example_meaning_en": "A pure/innocent heart."},
        "N2_1164": {"example_sentence": "（（順）じゅん）す（す）い（い）に（に）信じ（しんじ）て（て）ください。", "example_reading": "じゅんすいにしんじてください。", "example_meaning_cn": "请纯粹地相信。", "example_meaning_en": "Please believe it purely."},
        "N2_1165": {"example_sentence": "（（順）じゅん）ぜ（ぜ）ん（ん）と（と）し（し）た（た）態度（たいど）です。", "example_reading": "じゅんぜんとしたたいどです。", "example_meaning_cn": "纯然（纯正）的态度。", "example_meaning_en": "A pure/genuine attitude."},
        "N2_1166": {"example_sentence": "（（順）じゅん）な（な）ま（ま）を（を）話し（はなし）て（て）ください。", "example_reading": "じゅんなまをおなしてください。", "example_meaning_cn": "请说明顺便（或缘故）。", "example_meaning_en": "Please explain the circumstances."},
        "N2_1167": {"example_sentence": "（（準）じゅん）び（び）を（を）し（し）て（て）ください。", "example_reading": "じゅんびをしてください。", "example_meaning_cn": "请做准备。", "example_meaning_en": "Please make preparations."},
        "N2_1168": {"example_sentence": "（（巡）じゅん）り（り）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "じゅんりょうしてください。", "example_meaning_cn": "请去旅游（巡礼）。", "example_meaning_en": "Please go on a pilgrimage."},
        "N2_1169": {"example_sentence": "（（所）じょ）が（が）あり（あり）ますか。", "example_reading": "じょがありますか。", "example_meaning_cn": "有地方（处所）吗？", "example_meaning_en": "Is there a place/location?"},
        "N2_1170": {"example_sentence": "（（叙）じょ）し（し）て（て）ください。", "example_reading": "じょしてください。", "example_meaning_cn": "请叙述。", "example_meaning_en": "Please describe/narrate."},
        "N2_1171": {"example_sentence": "（（助）じょ）し（し）を（を）つけ（つけ）て（て）ください。", "example_reading": "じょしをつけてください。", "example_meaning_cn": "请加上助词。", "example_meaning_en": "Please add a particle."},
        "N2_1172": {"example_sentence": "（（徐）じょ）じょ（じょ）に（に）進み（すすみ）ましょう。", "example_reading": "じょじょにすすみましょう。", "example_meaning_cn": "徐徐（渐渐）前进吧。", "example_meaning_en": "Let's proceed gradually."},
        "N2_1173": {"example_sentence": "（（助）じょ）げ（げ）ん（ん）し（し）て（て）ください。", "example_reading": "じょげんしてください。", "example_meaning_cn": "请助言（提个建议）。", "example_meaning_en": "Please give some advice."},
        "N2_1174": {"example_sentence": "（（助）じょ）さ（さ）を（を）任せ（まかせ）ます。", "example_reading": "じょさをまかせます。", "example_meaning_cn": "交由助攻（辅助）。", "example_meaning_en": "I'll leave the assistance to you."},
        "N2_1175": {"example_sentence": "（（女）じょ）し（し）う（う）を（を）見（み）て（て）ください。", "example_reading": "じょしうをみてください。", "example_meaning_cn": "请看女优（女演员）。", "example_meaning_en": "Please watch the actress."},
        "N2_1176": {"example_sentence": "（（叙）じょ）し（し）ゅ（ゅ）つ（つ）し（し）て（て）ください。", "example_reading": "じょしゅつしてください。", "example_meaning_cn": "请叙述。", "example_meaning_en": "Please describe/narrate it."},
        "N2_1177": {"example_sentence": "（（助）じょ）し（し）ょ（ょ）う（う）を（を）読み（よみ）ましょう。", "example_reading": "じょしょうをよみましょう。", "example_meaning_cn": "读序章吧。", "example_meaning_en": "Let's read the prologue."},
        "N2_1178": {"example_sentence": "（（助）じょ）せ（せ）い（い）し（し）て（て）ください。", "example_reading": "じょせいしてください。", "example_meaning_cn": "请资助（助成）。", "example_meaning_en": "Please assist/subsidize."},
        "N2_1179": {"example_sentence": "（（助）じょ）そ（そ）う（う）し（し）て（て）ください。", "example_reading": "じょそうしてください。", "example_meaning_cn": "请助跑（助走）。", "example_meaning_en": "Please make a run-up."},
        "N2_1180": {"example_sentence": "（（所）じょ）た（た）い（い）を（を）持ち（もち）ます。", "example_reading": "じょたいをもちます。", "example_meaning_cn": "操持家务（或成家）。", "example_meaning_en": "I manage the household."},
        "N2_1181": {"example_sentence": "（（助）じょ）だ（だ）ん（ん）を（を）し（し）て（て）ください。", "example_reading": "じょだんをしてください。", "example_meaning_cn": "请进行助谈（或助言）。", "example_meaning_en": "Please assist in the talk."},
        "N2_1182": {"example_sentence": "（（所）じょ）ち（ち）を（を）話し（はなし）て（て）ください。", "example_reading": "じょちをおなしてください。", "example_meaning_cn": "请说出处（来源）。", "example_meaning_en": "Please state the source."},
        "N2_1183": {"example_sentence": "（（助）じょ）は（は）く（く）し（し）て（て）ください。", "example_reading": "じょはくしてください。", "example_meaning_cn": "请助拍（或助威）。", "example_meaning_en": "Please assist with clapping."},
        "N2_1184": {"example_sentence": "（（所）じょ）ひ（ひ）を（を）抑え（おさえ）ましょう。", "example_reading": "じょひをおさえましょう。", "example_meaning_cn": "节约开支（杂费）吧。", "example_meaning_en": "Let's cut down on miscellaneous expenses."},
        "N2_1185": {"example_sentence": "（（助）じょ）ほ（ほ）う（う）し（し）て（て）ください。", "example_reading": "じょほうしてください。", "example_meaning_cn": "请助攻（或辅助）。", "example_meaning_en": "Please assist in the defense/protection."},
        "N2_1186": {"example_sentence": "（（叙）じょ）ぶん（ぶん）を（を）書い（かい）て（て）ください。", "example_reading": "じょぶんをかいてください。", "example_meaning_cn": "请写序文。", "example_meaning_en": "Please write the preface."},
        "N2_1187": {"example_sentence": "（（初）しょ）を（を）忘れ（わすれ）ないで（で）ください。", "example_reading": "しょをわすれないでください。", "example_meaning_cn": "不要忘记初衷（初心）。", "example_meaning_en": "Please don't forget the beginning."},
        "N2_1188": {"example_sentence": "（（署）しょ）に（に）行き（いき）ましょう。", "example_reading": "しょにいきましょう。", "example_meaning_cn": "去警察局（署）吧。", "example_meaning_en": "Let's go to the station."},
        "N2_1189": {"example_sentence": "（（小）しょ）う（う）を（を）見（み）て（て）ください。", "example_reading": "しょうをみてください。", "example_meaning_cn": "请看那个章节（或小东西）。", "example_meaning_en": "Please see the chapter/small item."},
        "N2_1190": {"example_sentence": "（（消）しょう）を（を）し（し）て（て）ください。", "example_reading": "しょうをしてください。", "example_meaning_cn": "请消去（或消解）。", "example_meaning_en": "Please erase/delete it."},
        "N2_1191": {"example_sentence": "（（相）しょう）あ（あ）い（い）を（を）見（み）て（て）ください。", "example_reading": "しょうあいをみてください。", "example_meaning_cn": "请看情相（或缘分）。", "example_meaning_en": "Please see the compatibility."},
        "N2_1192": {"example_sentence": "（（消）しょう）か（か）し（し）て（て）ください。", "example_reading": "しょうかしてください。", "example_meaning_cn": "请消化。", "example_meaning_en": "Please digest it."},
        "N2_1193": {"example_sentence": "（（消）しょう）が（が）い（い）を（を）乗り越え（のりこえ）ましょう。", "example_reading": "しょうがいをのりこえましょう。", "example_meaning_cn": "克服障碍（或生涯）吧。", "example_meaning_en": "Let's overcome the obstacles."},
        "N2_1194": {"example_sentence": "（（小）しょう）か（か）ん（ん）を（を）読み（よみ）ましょう。", "example_reading": "しょうかんをよみましょう。", "example_meaning_cn": "读小简（或书信）吧。", "example_meaning_en": "Let's read the note/letter."},
        "N2_1195": {"example_sentence": "（（商）しょう）き（き）を（を）逃さ（のがさ）ないで（で）ください。", "example_reading": "しょうきをのがさないでください。", "example_meaning_cn": "请不要错失商机（或气）。", "example_meaning_en": "Please don't miss the business opportunity."},
        "N2_1196": {"example_sentence": "（（笑）しょう）き（き）を（を）誘い（さそい）ます。", "example_reading": "しょうきをさそいます。", "example_meaning_cn": "引人发笑。", "example_meaning_en": "It invites laughter."},
        "N2_1197": {"example_sentence": "（（消）しょう）き（き）ょ（ょ）く（く）てき（てき）な（な）態度（たいど）です。", "example_reading": "しょうきょくてきなたいどです。", "example_meaning_cn": "消极的态度。", "example_meaning_en": "A passive/negative attitude."},
        "N2_1198": {"example_sentence": "（（勝）しょう）き（き）を（を）つかみ（つかみ）ましょう。", "example_reading": "しょうきを掴みましょう。", "example_meaning_cn": "抓住胜机吧。", "example_meaning_en": "Let's seize the chance of victory."},
        "N2_1199": {"example_sentence": "（（賞）しょう）き（き）ん（ん）を（を）もらい（もらい）まし（し）た。", "example_reading": "しょうきんをもらいました。", "example_meaning_cn": "领到奖金了。", "example_meaning_en": "I received the prize money."},
        "N2_1200": {"example_sentence": "（（晶）しょう）け（け）い（い）を（を）見（み）て（て）ください。", "example_reading": "しょうけいをみてください。", "example_meaning_cn": "请看晶形（或捷径）。", "example_meaning_en": "Please see the crystal form/shortcut."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_1200.")

if __name__ == "__main__":
    main()
