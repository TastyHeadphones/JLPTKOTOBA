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
        "N3_1051": {"example_sentence": "（艶）がありますね。 ", "example_reading": "つやがありますね。", "example_meaning_cn": "有光泽（或很艳丽）呢。", "example_meaning_en": "It has a gloss/lustre, doesn't it?"},
        "N3_1052": {"example_sentence": "（強）いですね！", "example_reading": "つよいですね！", "example_meaning_cn": "真强（或有力）呢！", "example_meaning_en": "How strong!"},
        "N3_1053": {"example_sentence": "つ（（連）つ）れていってください。", "example_reading": "つれていってください。", "example_meaning_cn": "请带我一起去。", "example_meaning_en": "Please take me with you."},
        "N3_1054": {"example_sentence": "つ（（連）つ）れてきてください。", "example_reading": "つれてきてください。", "example_meaning_cn": "请带来。", "example_meaning_en": "Please bring them here."},
        "N3_1055": {"example_sentence": "（（露）つゆ）が降りています。", "example_reading": "つゆがおりています。", "example_meaning_cn": "下露水了。", "example_meaning_en": "Dew is falling."},
        "N3_1056": {"example_sentence": "（（梅雨）つゆ）が明けました。", "example_reading": "つゆがあけました。", "example_meaning_cn": "出梅（梅雨结束）了。", "example_meaning_en": "The rainy season is over."},
        "N3_1057": {"example_sentence": "（（辛）つら）いですね。", "example_reading": "つらいですね。", "example_meaning_cn": "真艰辛（或难受）呢。", "example_meaning_en": "It's tough/painful, isn't it?"},
        "N3_1058": {"example_sentence": "（（貫）つらぬ）いてください。", "example_reading": "つらぬいてください。", "example_meaning_cn": "请贯彻（或贯穿）。", "example_meaning_en": "Please go through/stick to it."},
        "N3_1059": {"example_sentence": "（（吊）つ）ってください。", "example_reading": "つってください。", "example_meaning_cn": "请吊起来（或垂落）。", "example_meaning_en": "Please hang/dangle it."},
        "N3_1060": {"example_sentence": "て（（手）て）を洗ってください。", "example_reading": "てをあらってください。", "example_meaning_cn": "请洗手。", "example_meaning_en": "Please wash your hands."},
        "N3_1061": {"example_sentence": "てあ（（手上）てあ）げです。", "example_reading": "てあげです。", "example_meaning_cn": "束手无策（举手投降）了。", "example_meaning_en": "I'm giving up/at my wit's end."},
        "N3_1062": {"example_sentence": "て（（手）て）あ（（足）あし）を動かしてください。", "example_reading": "てあしをうごかしてください。", "example_meaning_cn": "请动动手脚。", "example_meaning_en": "Please move your hands and feet."},
        "N3_1063": {"example_sentence": "で（（出）で）かけて（て）きます。", "example_reading": "でかけてきます。", "example_meaning_cn": "我出门了。", "example_meaning_en": "I'm going out."},
        "N3_1064": {"example_sentence": "て（（適）てき）して（て）います。", "example_reading": "てきしています。", "example_meaning_cn": "适合。", "example_meaning_en": "It's suitable."},
        "N3_1065": {"example_sentence": "て（（的）てき）が外れました。", "example_reading": "まとがはずれました。", "example_meaning_cn": "脱靶了（或没中要害）。", "example_meaning_en": "Missed the target."},
        "N3_1066": {"example_sentence": "てき（（敵）てき）ではありません。", "example_reading": "てきではありません。", "example_meaning_cn": "不是敌人（或对手）。", "example_meaning_en": "They're not the enemy/a match."},
        "N3_1067": {"example_sentence": "てき（適宜）宜（ぎ）に対応してください。", "example_reading": "てきぎにたいおうしてください。", "example_meaning_cn": "请酌情应对。", "example_meaning_en": "Please respond appropriately/as you see fit."},
        "N3_1068": {"example_sentence": "てき（（適切）せつ）な判断です。", "example_reading": "てきせつなはんだんです。", "example_meaning_cn": "适切（妥当）的判断。", "example_meaning_en": "It's an appropriate judgment."},
        "N3_1069": {"example_sentence": "てき（適（（度）ど）に運動してください。", "example_reading": "てきどにうんどうしてください。", "example_meaning_cn": "请适度运动。", "example_meaning_en": "Please exercise moderately."},
        "N3_1070": {"example_sentence": "てき（（適用）よう）されます。", "example_reading": "てきようされます。", "example_meaning_cn": "被适用（或应用）。", "example_meaning_en": "It is applied."},
        "N3_1071": {"example_sentence": "でき（（出来）でき）ました！ ", "example_reading": "できました！", "example_meaning_cn": "做好了（或完成了）！", "example_meaning_en": "I'm done/It's finished!"},
        "N3_1072": {"example_sentence": "で（でお（（覆）お）われて）います。", "example_reading": "おおわれています。", "example_meaning_cn": "被覆盖着。", "example_meaning_en": "It is covered."},
        "N3_1073": {"example_sentence": "て（手）が（（掛）か）かります。", "example_reading": "てがかかります。", "example_meaning_cn": "费事（或棘手）。", "example_meaning_en": "It takes effort/is a handful."},
        "N3_1074": {"example_sentence": "て（手）が（（空）あ）きました。", "example_reading": "てがあきました。", "example_meaning_cn": "腾出手（有空）了。", "example_meaning_en": "I'm free now/my hands are free."},
        "N3_1075": {"example_sentence": "て（手）ざ（座）わり（（触）さ）が良いです。", "example_reading": "てざわりがいいです。", "example_meaning_cn": "手感好。", "example_meaning_en": "It feels good to the touch."},
        "N3_1076": {"example_sentence": "でし（弟子）になりたいです。", "example_reading": "でしになりたいです。", "example_meaning_cn": "想成为弟子（学生）。", "example_meaning_en": "I want to become a disciple."},
        "N3_1077": {"example_sentence": "て（（出）で）してください。", "example_reading": "だしてください。", "example_meaning_cn": "请交出来（或递出）。", "example_meaning_en": "Please submit/hand it in."},
         "N3_1078": {"example_sentence": "て（手）をつないでください。", "example_reading": "てをつないでください。", "example_meaning_cn": "请牵手。", "example_meaning_en": "Please hold hands."},
        "N3_1079": {"example_sentence": "てつ（（鉄）てつ）は固いです。", "example_reading": "てつわかたいです。", "example_meaning_cn": "铁很硬。", "example_meaning_en": "Iron is hard."},
        "N3_1080": {"example_sentence": "てつ（（哲）てつ）学（がく）を学びます。", "example_reading": "てつがくをまなびます。", "example_meaning_cn": "学习哲学。", "example_meaning_en": "I study philosophy."},
        "N3_1081": {"example_sentence": "てつ（（徹）てつ）夜（や）しました。", "example_reading": "てつやしました。", "example_meaning_cn": "熬通宵（彻夜）了。", "example_meaning_en": "I stayed up all night."},
        "N3_1082": {"example_sentence": "てつ（手伝）伝（つだ）ってください。", "example_reading": "てつだってください。", "example_meaning_cn": "请帮忙。", "example_meaning_en": "Please help me."},
        "N3_1083": {"example_sentence": "て（（手）て）つ（づ（（続）づ））きをしてください。", "example_reading": "てつづきをしてください。", "example_meaning_cn": "请办手续。", "example_meaning_en": "Please follow the procedures."},
        "N3_1084": {"example_sentence": "てつ（（鉄）てっ）ぽう（ぽう）を撃ちます。", "example_reading": "てっぽうをうちます。", "example_meaning_cn": "开枪（铁炮）。", "example_meaning_en": "Firing a gun."},
        "N3_1085": {"example_sentence": "てま（手）間（ま）をかけてください。", "example_reading": "てまをかけてください。", "example_meaning_cn": "请花点工夫（费心）。", "example_meaning_en": "Please take the trouble/time."},
        "N3_1086": {"example_sentence": "でも（でも）いいですよ。", "example_reading": "でもいいですよ。", "example_meaning_cn": "但是也可以哦。", "example_meaning_en": "But that's fine too."},
        "N3_1087": {"example_sentence": "てる（（照）てる）っていますね。 ", "example_reading": "てっていますね。", "example_meaning_cn": "正在照射（或害羞）着呢。", "example_meaning_en": "It's shining/they're shy, aren't they?"},
        "N3_1088": {"example_sentence": "テレ（てれ）ているんですか。", "example_reading": "てれているんですか。", "example_meaning_cn": "是在害羞（腼腆）吗？", "example_meaning_en": "Are you feeling shy?"},
        "N3_1089": {"example_sentence": "てん（（天）てん）気（き）がいいですね。", "example_reading": "てんきがいいですね。", "example_meaning_cn": "天气真好呢。", "example_meaning_en": "The weather is nice, isn't it?"},
        "N3_1090": {"example_sentence": "てん（（点）てん）を（（打）う）ってください。", "example_reading": "てんをうってください。", "example_meaning_cn": "请打点（画圆点）。", "example_meaning_en": "Please put a point/dot."},
        "N3_1091": {"example_sentence": "てん（（天）てん）の（（声）こえ）を聞きます。", "example_reading": "てんのこえをききます。", "example_meaning_cn": "听天之声（启示）。", "example_meaning_en": "I'll listen to the voice from heaven."},
        "N3_1092": {"example_sentence": "てん（（天）てん）候（こう）を調べてください。", "example_reading": "てんこうをしらべてください。", "example_meaning_cn": "请查询气候（天气状况）。", "example_meaning_en": "Please check the weather conditions."},
        "N3_1093": {"example_sentence": "てん（（転）てん）勤（きん）しました。", "example_reading": "てんきんしました。", "example_meaning_cn": "调职（转任）了。", "example_meaning_en": "I was transferred (within the company)."},
        "N3_1094": {"example_sentence": "てん（（点）てん）検（けん）してください。", "example_reading": "てんけんしてください。", "example_meaning_cn": "请点检（检查）。", "example_meaning_en": "Please inspect/check it."},
        "N3_1095": {"example_sentence": "てん（（展）てん）示（じ）してください。", "example_reading": "てんじしてください。", "example_meaning_cn": "请展示。", "example_meaning_en": "Please display/exhibit it."},
        "N3_1096": {"example_sentence": "てん（（天）てん）井（じょう）を見てください。", "example_reading": "てんじょうをみてください。", "example_meaning_cn": "请看天花板。", "example_meaning_en": "Please look at the ceiling."},
        "N3_1097": {"example_sentence": "てん（（天）てん）才（さい）ですね！", "example_reading": "てんさいですね！", "example_meaning_cn": "真是天才呢！", "example_meaning_en": "You're a genius!"},
        "N3_1098": {"example_sentence": "てん（（伝）てん）染（せん）しないでください。", "example_reading": "でんせんしないでください。", "example_meaning_cn": "请不要传染。", "example_meaning_en": "Please don't infect others."},
        "N3_1099": {"example_sentence": "でん（（伝）でん）統（とう）を守りましょう。", "example_reading": "でんとうをまもりましょう。", "example_meaning_cn": "守护传统吧。", "example_meaning_en": "Let's preserve tradition."},
        "N3_1100": {"example_sentence": "てん（（天）てん）に（（召）め）されました。", "example_reading": "てんにめされました。", "example_meaning_cn": "被天堂召回（去世）了。", "example_meaning_en": "They've been called to heaven/passed away."},
        "N3_1101": {"example_sentence": "てん（（展）てん）望（ぼう）が良いです。", "example_reading": "てんぼうがいいです。", "example_meaning_cn": "展望（视野）很好。", "example_meaning_en": "The view/prospect is good."},
        "N3_1102": {"example_sentence": "と（（都）と）へ行きます。", "example_reading": "とへいきます。", "example_meaning_cn": "进城（或去都市）。", "example_meaning_en": "Going to the capital/city."},
        "N3_1103": {"example_sentence": "と（（戸）と）を閉めてください。", "example_reading": "とをしめてください。", "example_meaning_cn": "请关门（户）。", "example_meaning_en": "Please close the door."},
        "N3_1104": {"example_sentence": "（（溶）と）かしてください。", "example_reading": "とかしてください。", "example_meaning_cn": "请溶解（或熔化）。", "example_meaning_en": "Please dissolve/melt it."},
        "N3_1105": {"example_sentence": "（（解）と）いてください。", "example_reading": "といてください。", "example_meaning_cn": "请解答（或解开）。", "example_meaning_en": "Please solve/untie it."},
        "N3_1106": {"example_sentence": "（（説）と）いてください。", "example_reading": "といでください。", "example_meaning_cn": "请说服（或讲解）。", "example_meaning_en": "Please explain/preach."},
        "N3_1107": {"example_sentence": "（（研）と）いでください。", "example_reading": "といでください。", "example_meaning_cn": "请磨（或淘米）。", "example_meaning_en": "Please sharpen/wash (rice)."},
        "N3_1108": {"example_sentence": "とう（（塔）とう）があります。", "example_reading": "とうがあります。", "example_meaning_cn": "有一座塔。", "example_meaning_en": "There is a tower."},
        "N3_1109": {"example_sentence": "とう（（答）とう）を書いてください。", "example_reading": "とうをかいてください。", "example_meaning_cn": "请写答案。", "example_meaning_en": "Please write the answer."},
        "N3_1110": {"example_sentence": "どう（（同）どう）意（い）します。", "example_reading": "どういします。", "example_meaning_cn": "我同意。", "example_meaning_en": "I agree."},
        "N3_1111": {"example_sentence": "とう（（島）とう）へ渡ります。", "example_reading": "とうわわたります。", "example_meaning_cn": "渡到岛上去。", "example_meaning_en": "I'll cross to the island."},
        "N3_1112": {"example_sentence": "とう（（東）とう）洋（よう）の文化です。", "example_reading": "とうようのぶんかです。", "example_meaning_cn": "东方的文化。", "example_meaning_en": "It's Eastern culture."},
        "N3_1113": {"example_sentence": "とう（（当）とう）局（きょく）に聞いてください。", "example_reading": "とうきょくにきいてください。", "example_meaning_cn": "请向当局（有关部门）询问。", "example_meaning_en": "Please ask the authorities."},
        "N3_1114": {"example_sentence": "どう（（動）どう）機（き）は何ですか。", "example_reading": "どうきわなんですか。", "example_meaning_cn": "动机是什么？", "example_meaning_en": "What is the motive?"},
        "N3_1115": {"example_sentence": "とう（（登）とう）記（き）してください。", "example_reading": "とうきしてください。", "example_meaning_cn": "请登记（备案）。", "example_meaning_en": "Please register/file it."},
        "N3_1116": {"example_sentence": "どう（（道）どう）具（ぐ）を揃えてください。", "example_reading": "どうぐをそろえてください。", "example_meaning_cn": "请准备齐工具。", "example_meaning_en": "Please gather the tools."},
        "N3_1117": {"example_sentence": "とう（（統計）けい）を見てください。", "example_reading": "とうけいをみてください。", "example_meaning_cn": "请看统计。", "example_meaning_en": "Please look at the statistics."},
        "N3_1118": {"example_sentence": "ど（（道）どう）徳（とく）を守りましょう。", "example_reading": "どうとくをまもりましょう。", "example_meaning_cn": "遵守道德吧。", "example_meaning_en": "Let's uphold morality."},
        "N3_1119": {"example_sentence": "とう（（当）とう）日（じつ）に会いましょう。", "example_reading": "とうじつにあいましょう。", "example_meaning_cn": "当日再见吧。", "example_meaning_en": "Let's meet on the day."},
        "N3_1120": {"example_sentence": "とう（（当）とう）然（ぜん）ですね！", "example_reading": "とうぜんですね！", "example_meaning_cn": "理所当然呢！", "example_meaning_en": "Of course/It's natural!"}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N3_1120 (N3 complete).")

if __name__ == "__main__":
    main()
