import json


with open("./video_questions.json", "w", encoding='utf-8') as f:
    json.dump({},f, ensure_ascii=False)


dic = {"0" : {"title" : "中药炮制是中药的制药技术，炮制方法和炮制技能错误的一组是：",
                "video" : "./video/嵌套序列 01.avi",
                "choices" : {
                    "A" : "竞选加工、切制饮片、清炒法、加辅料、炒法",
                    "B" : "制法、断法、蒸法、煮法、单法、复制法、粘贴法", #粘贴法
                    "C" : "发酵法、发芽法、味法、制疮法、提性法、水飞法"
                },
                "answer" : 1}}
with open("./video_questions.json", "r", encoding='utf-8') as f:
    rdic = json.load(f)
#rdic = {}
rdic.update(dic)
with open("./video_questions.json", "w") as f:
    json.dump(rdic,f, ensure_ascii=False)


dic = {"1" : {"title" : "竞选加工是选取药材的有效部位，去除非药用的异物、杂质或将药材进行分档，使其达到规定的药用进度标准的一类操作。竞选加工多种方式，其中错误的一组是：",
                "video" : "./video/嵌套序列 02.avi",
                "choices" : {
                    "A" : "挑选、钉法、筛选、风选、水选", #水选
                    "B" : "洗漂、去皮壳、去毛、去颅", 
                    "C" : "去腥、去核、去头尾足赤、碾捣、制绒"
                },
                "answer" : 0}}
with open("./video_questions.json", "r", encoding='utf-8') as f:
    rdic = json.load(f)
#rdic = {}
rdic.update(dic)
with open("./video_questions.json", "w") as f:
    json.dump(rdic,f, ensure_ascii=False)


dic = {"2" : {"title" : "挑选是用手挑选去混在药物中的杂质、霉败品，或区分不同药用部位，或按药材大小粗细归类的操作。以下关于挑选的说法错误的是：",
                "video" : "./video/嵌套序列 03.avi",
                "choices" : {
                    "A" : "枸杞子最易生霉变色，要用时要把霉变的果实及残留的果梗挑拣出来，以保证药品质量。枸杞子的杂质含量不得过5%。", #1%
                    "B" : "麻黄要将茎与根严格分离，茎含麻黄型生物碱，根含大环金胺生物碱，成分不同分别入药。", 
                    "C" : "白柱的根茎大小不等，历史浸泡和温润的时间一致，要进行分档，以保证影片质量。"
                },
                "answer" : 0}}
with open("./video_questions.json", "r", encoding='utf-8') as f:
    rdic = json.load(f)
#rdic = {}
rdic.update(dic)
with open("./video_questions.json", "w") as f:
    json.dump(rdic,f, ensure_ascii=False)