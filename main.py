import sys
from pathlib import Path
import difflib
import time
import datetime
import random

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap, QImage, QColor, QStandardItemModel, QStandardItem, QPainter, QPen
from PyQt5.QtCore import Qt, QUrl, QFileInfo, QStringListModel, QCoreApplication, QTimer, QTime
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import shutil

from get import *

class MainWindow(QWidget):
    

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_zhishixuexi()
        self.init_sousuo()
        self.init_login()
        self.init_time()
        self.init_ques()
        self.init_video()
        self.init_score()
        self.init_score_record()
        self.init_exam_num()
        self.init_add()
    
    def init_ui(self):
        self.ui = uic.loadUi("./main_window.ui")
        self.stacked_widget = self.ui.stackedWidget
        self.ui.actionHome.triggered.connect(self.go_Home)
        self.ui.zhishixuexi.triggered.connect(self.go_zhishixuexi)
        #self.ui.ac_yaoxing.triggered.connect(self.go_yaoxing)
        #self.ui.ac_paozhi.triggered.connect(self.go_paozhi)
        self.ui.mohuchaxun.triggered.connect(self.go_mohuchaxun)
        self.ui.xuexishijian.triggered.connect(self.go_time)
        self.ui.ac_20.triggered.connect(self.go_q20)
        self.ui.ac_50.triggered.connect(self.go_q50)
        self.ui.ac_100.triggered.connect(self.go_q100)
        self.ui.ac_v.triggered.connect(self.go_video)
        self.ui.kaoshichengji.triggered.connect(self.go_kaoshichengji)
        self.ui.ac_about.triggered.connect(self.go_about)
        self.ui.add.triggered.connect(self.go_add)
        self.stacked_widget.setCurrentIndex(5)

    def init_zhishixuexi(self):
        self.name = self.ui.name
        self.zhizhu = self.ui.zhizhu
        self.chengyao = self.ui.chengyao
        self.zhongzhi_label = self.ui.zhongzhi
        self.paozhi_label = self.ui.paozhi
        self.yaoxing_label = self.ui.yaoxing
        self.zhuzhi_lable = self.ui.zhuzhi
        self.zhongzhi_textBrowser = self.ui.tb_zhongzhi
        self.paozhi_textBrowser = self.ui.tb_paozhi
        self.yaoxing_textBrowser = self.ui.tb_yaoxing
        self.zhuzhi_textBrowser = self.ui.tb_zhuzhi
        self.prev_page = self.ui.prev_page
        self.next_page = self.ui.next_page
        self.img = QImage(334, 289, QImage.Format_RGB32)
        self.img.fill(QColor(240, 240, 240))
        self.next_page.clicked.connect(self.next)
        self.page = -1
        self.next()
        self.prev_page.clicked.connect(self.prev)
        self.tingzhixuexi = self.ui.tingzhixuexi
        self.tingzhixuexi.clicked.connect(self.tingzhixuexi_f)
        self.jixvxuexi = self.ui.jixvxuexi
        self.jixvxuexi.clicked.connect(self.jixvxuexi_f)

    def init_sousuo(self):
        self.sousuokuang = self.ui.lineEdit
        self.sousuo = self.ui.sousuo
        self.jieguo = self.ui.listView
        self.sousuokuang.setPlaceholderText("请输入关键词")
        self.sousuo.clicked.connect(self.search)
        self.jieguo.clicked.connect(self.search_results)
        self.name_2 = self.ui.name_2
        self.zhizhu_2 = self.ui.zhizhu_2
        self.chengyao_2 = self.ui.chengyao_2
        self.zhongzhi_label_2 = self.ui.zhongzhi_2
        self.paozhi_label_2 = self.ui.paozhi_2
        self.yaoxing_label_2 = self.ui.yaoxing_2
        self.zhuzhi_lable_2 = self.ui.zhuzhi_2
        self.zhongzhi_textBrowser_2 = self.ui.tb_zhongzhi_2
        self.paozhi_textBrowser_2 = self.ui.tb_paozhi_2
        self.yaoxing_textBrowser_2 = self.ui.tb_yaoxing_2
        self.zhuzhi_textBrowser_2 = self.ui.tb_zhuzhi_2

    def init_login(self):
        self.ui.menu.setEnabled(False)
        self.ui.menu_2.setEnabled(False)
        self.ui.menu_3.setEnabled(False)
        self.ui.menu_4.setEnabled(False)
        #self.ui.menu_5.setEnabled(False)
        self.id = self.ui.id
        self.name_id = self.ui.name_3
        self.login_btn = self.ui.login
        self.login_msg = self.ui.msg
        self.login_btn.clicked.connect(self.login)

    def init_time(self):
        self.tableView = self.ui.tableView

    def init_ques(self):
        self.next_q = self.ui.next_q
        self.prev_q = self.ui.prev_q
        self.tijiaoshijuan = self.ui.tijiaoshijuan
        self.A = self.ui.A
        self.B = self.ui.B
        self.C = self.ui.C
        self.D = self.ui.D
        self.E = self.ui.E
        self.tb_A = self.ui.tb_A
        self.tb_B = self.ui.tb_B
        self.tb_C = self.ui.tb_C
        self.tb_D = self.ui.tb_D
        self.tb_E = self.ui.tb_E
        self.title = self.ui.title
        self.zhizhu_3 = self.ui.zhizhu_3
        self.chengyao_3 = self.ui.chengyao_3
        self.answer_t = self.ui.answer
        #self.next_q.clicked.connect(self.next_ques)
        #self.prev_q.clicked.connect(self.prev_ques)
        self.tijiaoshijuan.clicked.connect(self.tijiao)
        self.time_label = self.ui.time_label
        self.current_page = self.ui.current_page
        self.buttonGroup = self.ui.buttonGroup

    def init_video(self):
        self.QVideoWidge = self.ui.widget
        self.video_exit = self.ui.video_exit
        self.video_title = self.ui.video_title
        self.A1 = self.ui.A1
        self.B1 = self.ui.B1
        self.C1 = self.ui.C1
        self.tb_A1 = self.ui.tb_A1
        self.tb_B1 = self.ui.tb_B1
        self.tb_C1 = self.ui.tb_C1
        self.confirm = self.ui.confirm
        self.next_vq = self.ui.next_vq
        self.answer_2 = self.ui.answer_2
        self.video_exit.clicked.connect(self.v_exit)
        self.confirm.clicked.connect(self.confirm_f)
        self.next_vq.clicked.connect(self.next_video_ques)
        self.mplayer = QMediaPlayer()
        #self.media_content = QMediaContent(QUrl.fromLocalFile('./嵌套序列 01.avi'))  # 2
        # self.player.setMedia(QMediaContent(QUrl('http://example.com/music.mp3')))
        self.mplayer.setVideoOutput(self.ui.widget)
        #self.mplayer.setMedia(self.media_content)    # 3
        self.mplayer.setVolume(80)                   # 4

    def init_score(self):
        self.score_t = self.ui.score
        self.chakandaan = self.ui.chakandaan
        self.chakandaan.clicked.connect(self.daanye)
        self.QChartView = self.ui.QChartView

    def init_score_record(self):
        self.tableView_2 = self.ui.tableView_2

    def init_exam_num(self):
        self.exam_num = self.ui.exam_num
        self.exam_num_button = self.ui.exam_num_button
        self.exam_num_button.clicked.connect(self.set_seed)

    def init_add(self):
        self.add_btn = self.ui.add_btn
        self.chengyao_up_btn = self.ui.chengyao_up_btn
        self.zhizhu_up_btn = self.ui.zhizhu_up_btn
        self.chengyao_up = self.ui.chengyao_up
        self.zhizhu_up = self.ui.zhizhu_up
        self.pte_name = self.ui.pte_name
        self.pte_zhongzhi = self.ui.pte_zhongzhi        
        self.pte_paozhi = self.ui.pte_paozhi        
        self.pte_yaoxing = self.ui.pte_yaoxing
        self.pte_zhuzhi = self.ui.pte_zhuzhi
        self.status = self.ui.status
        self.chengyao_up_btn.clicked.connect(self.chengyao_up_f) 
        self.zhizhu_up_btn.clicked.connect(self.zhizhu_up_f)   
        self.add_btn.clicked.connect(self.add_f)
        self.chengyao_img_name = None
        self.zhizhu_img_name = None

    def next(self):
        self.page = (self.page + 1) % get_len()
        name, zhongzhi, paozhi, yaoxing, zhuzhi = get_page(self.page)
        self.zhongzhi_textBrowser.setText(zhongzhi)
        self.paozhi_textBrowser.setText(paozhi)
        self.yaoxing_textBrowser.setText(yaoxing)
        self.zhuzhi_textBrowser.setText(zhuzhi)
        self.name.setText(name)
        self.name.update()
        self.showpic(name, self.zhizhu, self.chengyao)
        pass

    def prev(self):
        self.page = (self.page - 1) % get_len()
        name, zhongzhi, paozhi, yaoxing, zhuzhi = get_page(self.page)
        self.zhongzhi_textBrowser.setText(zhongzhi)
        self.paozhi_textBrowser.setText(paozhi)
        self.yaoxing_textBrowser.setText(yaoxing)
        self.zhuzhi_textBrowser.setText(zhuzhi)
        self.name.setText(name)
        self.name.update()
        self.showpic(name, self.zhizhu, self.chengyao)
        pass

    def showpic(self, name, zhizhu, chengyao):
        if Path(f"./120image/zhizhu/{name}.jpg").exists():
            zhizhu_img = QImage(f"./120image/zhizhu/{name}.jpg")
            zhizhu_img = self.m_resize(zhizhu_img)
            pixmap = QPixmap.fromImage(zhizhu_img)
            zhizhu.setPixmap(pixmap)
        else: zhizhu.setPixmap(QPixmap.fromImage(self.img))
        if Path(f"./120image/chengyao/{name}.jpg").exists():
            chengyao_img = QImage(f"./120image/chengyao/{name}.jpg")
            chengyao_img = self.m_resize(chengyao_img)
            pixmap = QPixmap.fromImage(chengyao_img)
            chengyao.setPixmap(pixmap)
        else: chengyao.setPixmap(QPixmap.fromImage(self.img))
    
    def m_resize(self, pil_image, w_box=334, h_box=289):  # 参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])

        width = int(w * factor)
        height = int(h * factor)
        return pil_image.scaled(width, height)

    def search(self):
        key_word = self.sousuokuang.text()
        n_list = get_name_list()
        self.result = difflib.get_close_matches(key_word, n_list, 16, cutoff=0.1)
        listModel = QStringListModel()
        listModel.setStringList(self.result)
        self.jieguo.setModel(listModel)

    def search_results(self, qModelIndex):
        name = self.result[qModelIndex.row()]
        value = get_value(name)
        self.zhongzhi_textBrowser_2.setText(value["种植"])
        self.paozhi_textBrowser_2.setText(value["炮制"])
        self.yaoxing_textBrowser_2.setText(value["药性"])
        self.zhuzhi_textBrowser_2.setText(value["主治"])
        self.name_2.setText(name)
        self.name_2.update()
        self.showpic(name, self.zhizhu_2, self.chengyao_2)

    def tingzhixuexi_f(self):
        self.ui.menu.setEnabled(True)
        self.ui.menu_2.setEnabled(True)
        self.ui.menu_3.setEnabled(True)
        self.ui.menu_4.setEnabled(True)
        self.ui.menu_5.setEnabled(True)
        self.ui.menu_6.setEnabled(True)
        self.ui.menu_7.setEnabled(True)
        self.next_page.setEnabled(False)
        self.prev_page.setEnabled(False)
        self.tingzhixuexi.setEnabled(False)
        self.jixvxuexi.setEnabled(True)
        self.end = time.perf_counter()
        timer = get_time(self.idx)
        timer += round(self.end - self.start)
        save_time(self.idx, timer)

    def jixvxuexi_f(self):
        self.ui.menu.setEnabled(False)
        self.ui.menu_2.setEnabled(False)
        self.ui.menu_3.setEnabled(False)
        self.ui.menu_4.setEnabled(False)
        self.ui.menu_5.setEnabled(False)
        self.next_page.setEnabled(True)
        self.prev_page.setEnabled(True)
        self.tingzhixuexi.setEnabled(True)
        self.jixvxuexi.setEnabled(False)
        self.start = time.perf_counter()

    def login(self):
        self.idx = self.id.text()
        name = self.name_id.text()
        if self.idx == "" or name == "": return
        if checkin(self.idx, name): self.go_Home()
        elif conflict_check(self.idx, name): self.go_Home()
        else: 
            self.login_msg.setText("已有同一学号不同姓名的用户！")
            self.login_msg.setStyleSheet("color:red")


    def next_ques(self):
        #self.A.setChecked(False)
        #self.B.setChecked(False)
        #self.C.setChecked(False)
        #self.D.setChecked(False)
        #self.E.setChecked(False)
        if self.q_page == 0:self.prev_q.setEnabled(True)
        if self.q_page == self.q_num - 2:
            self.next_q.setEnabled(False)
            #self.tijiaoshijuan.setEnabled(True)
            #return
        self.q_page = self.q_page + 1
        self.current_page.setText(f"{self.q_page + 1}/{self.q_num}")
        #title, pic0, pic1, a, b, c, d, e, ans = get_ques(f"\"{self.q_list[self.q_page]}\"")
        title, pic0, pic1, choices, self.ans = get_ques(str(self.q_list[self.q_page])).values()
        #print(self.q_page)
        #self.answers[self.q_page - 1] = self.ans
        a, b, c, d, e = choices.values()
        self.tb_A.setText(a)
        self.tb_B.setText(b)
        self.tb_C.setText(c)
        self.tb_D.setText(d)
        self.tb_E.setText(e)
        self.title.setText(title)
        self.title.update()
        if pic0 != None:
            zhizhu_img = QImage(f"./120image/zhizhu/{pic0}.jpg")
            zhizhu_img = self.m_resize(zhizhu_img)
            pixmap = QPixmap.fromImage(zhizhu_img)
            self.zhizhu_3.setPixmap(pixmap)
        else: self.zhizhu_3.setPixmap(QPixmap.fromImage(self.img))
        if pic1 != None:
            chengyao_img = QImage(f"./120image/chengyao/{pic1}.jpg")
            chengyao_img = self.m_resize(chengyao_img)
            pixmap = QPixmap.fromImage(chengyao_img)
            self.chengyao_3.setPixmap(pixmap)
        else: self.chengyao_3.setPixmap(QPixmap.fromImage(self.img))
        #self.check_answer(self.ans)
        chosen = -1
        if self.A.isChecked(): chosen = 0
        elif self.B.isChecked(): chosen = 1
        elif self.C.isChecked(): chosen = 2
        elif self.D.isChecked(): chosen = 3
        elif self.E.isChecked(): chosen = 4
        self.chosens[self.q_page - 1] = chosen
        if self.chosens[self.q_page] == -1:
            self.buttonGroup.setExclusive(False)
            self.A.setChecked(False)
            self.B.setChecked(False) 
            self.C.setChecked(False) 
            self.D.setChecked(False) 
            self.E.setChecked(False)
            self.buttonGroup.setExclusive(True)
        if self.chosens[self.q_page] == 0: self.A.setChecked(True)
        elif self.chosens[self.q_page] == 1: self.B.setChecked(True)
        elif self.chosens[self.q_page] == 2: self.C.setChecked(True)
        elif self.chosens[self.q_page] == 3: self.D.setChecked(True)
        elif self.chosens[self.q_page] == 4: self.E.setChecked(True)

    def prev_ques(self):
        #self.A.setChecked(False)
        #self.B.setChecked(False)
        #self.C.setChecked(False)
        #self.D.setChecked(False)
        #self.E.setChecked(False)
        if self.q_page == self.q_num - 1:self.next_q.setEnabled(True)
        if self.q_page == 1:
            self.prev_q.setEnabled(False)
            #self.tijiaoshijuan.setEnabled(True)
            #return
        self.q_page = self.q_page - 1
        self.current_page.setText(f"{self.q_page + 1}/{self.q_num}")
        #title, pic0, pic1, a, b, c, d, e, ans = get_ques(f"\"{self.q_list[self.q_page]}\"")
        title, pic0, pic1, choices, self.ans = get_ques(str(self.q_list[self.q_page])).values()
        #self.answers[self.q_page + 1] = self.ans
        a, b, c, d, e = choices.values()
        self.tb_A.setText(a)
        self.tb_B.setText(b)
        self.tb_C.setText(c)
        self.tb_D.setText(d)
        self.tb_E.setText(e)
        self.title.setText(title)
        self.title.update()
        if pic0 != None:
            zhizhu_img = QImage(f"./120image/zhizhu/{pic0}.jpg")
            zhizhu_img = self.m_resize(zhizhu_img)
            pixmap = QPixmap.fromImage(zhizhu_img)
            self.zhizhu_3.setPixmap(pixmap)
        else: self.zhizhu_3.setPixmap(QPixmap.fromImage(self.img))
        if pic1 != None:
            chengyao_img = QImage(f"./120image/chengyao/{pic1}.jpg")
            chengyao_img = self.m_resize(chengyao_img)
            pixmap = QPixmap.fromImage(chengyao_img)
            self.chengyao_3.setPixmap(pixmap)
        else: self.chengyao_3.setPixmap(QPixmap.fromImage(self.img))
        chosen = -1
        if self.A.isChecked(): chosen = 0
        elif self.B.isChecked(): chosen = 1
        elif self.C.isChecked(): chosen = 2
        elif self.D.isChecked(): chosen = 3
        elif self.E.isChecked(): chosen = 4
        self.chosens[self.q_page + 1] = chosen
        if self.chosens[self.q_page] == -1:
            self.buttonGroup.setExclusive(False)
            self.A.setChecked(False)
            self.B.setChecked(False) 
            self.C.setChecked(False) 
            self.D.setChecked(False) 
            self.E.setChecked(False)
            self.buttonGroup.setExclusive(True)               
        if self.chosens[self.q_page] == 0: self.A.setChecked(True)
        elif self.chosens[self.q_page] == 1: self.B.setChecked(True)
        elif self.chosens[self.q_page] == 2: self.C.setChecked(True)
        elif self.chosens[self.q_page] == 3: self.D.setChecked(True)
        elif self.chosens[self.q_page] == 4: self.E.setChecked(True)

    '''def check_answer(self, answer):
        chosen = -1
        if self.A.isChecked(): chosen = 0
        elif self.B.isChecked(): chosen = 1
        elif self.C.isChecked(): chosen = 2
        elif self.D.isChecked(): chosen = 3
        elif self.E.isChecked(): chosen = 4
        if chosen == answer: self.right += 1
        self.chosens.append(chosen)'''

    def tijiao(self):
        chosen = -1
        if self.A.isChecked(): chosen = 0
        elif self.B.isChecked(): chosen = 1
        elif self.C.isChecked(): chosen = 2
        elif self.D.isChecked(): chosen = 3
        elif self.E.isChecked(): chosen = 4
        self.chosens[self.q_page] = chosen
        self.timer.stop()
        self.timer.timeout.disconnect(self.showTime)
        #self.tijiaoshijuan.setEnabled(False)
        '''self.check_answer(self.ans)
        #去除第一个-1（首次调用）
        self.chosens = self.chosens[1:]'''
        for i, j in enumerate(self.answers):
            if self.chosens[i] == j: self.right += 1
        self.score = round(self.right / self.q_num * 100)
        save_score(self.idx, self.score, self.exam_time.toString('hh:mm:ss'), self.seed)
        self.stacked_widget.setCurrentIndex(8)
        self.score_t.setText(f"您的正确率为{str(self.score)}%，选择的题目数量为{self.q_num}，试卷号为{self.exam_num.text()}")
        series = QPieSeries()
        series.append("正确", self.right)
        series.append("错误", self.q_num - self.right)
        slice = QPieSlice()
        slice = series.slices()[0]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.green, 2))
        slice.setBrush(Qt.green)
        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().setAlignment(Qt.AlignBottom)
        #chartview = QChartView(chart)
        #chartview.setRenderHint(QPainter.Antialiasing)
        self.QChartView.setChart(chart)
        self.QChartView.setRenderHint(QPainter.Antialiasing)
        
    def daanye(self):
        self.q_page = 0
        self.next_q.setEnabled(True)
        self.stacked_widget.setCurrentIndex(7)
        self.next_q.clicked.disconnect(self.next_ques)
        self.next_q.clicked.connect(self.next_ques_2)
        self.prev_q.clicked.disconnect(self.prev_ques)
        self.prev_q.clicked.connect(self.prev_ques_2)
        self.tijiaoshijuan.clicked.disconnect(self.tijiao)
        self.tijiaoshijuan.setText("结束查看")
        self.tijiaoshijuan.clicked.connect(self.jiesuchakan)
        self.current_page.setText(f"{self.q_page + 1}/{self.q_num}")
        title, pic0, pic1, choices, ans = get_ques(str(self.q_list[self.q_page])).values()
        a, b, c, d, e = choices.values()
        self.tb_A.setText(a)
        self.tb_B.setText(b)
        self.tb_C.setText(c)
        self.tb_D.setText(d)
        self.tb_E.setText(e)
        self.title.setText(title)
        self.title.update()
        if pic0 != None:
            zhizhu_img = QImage(f"./120image/zhizhu/{pic0}.jpg")
            zhizhu_img = self.m_resize(zhizhu_img)
            pixmap = QPixmap.fromImage(zhizhu_img)
            self.zhizhu_3.setPixmap(pixmap)
        else: self.zhizhu_3.setPixmap(QPixmap.fromImage(self.img))
        if pic1 != None:
            chengyao_img = QImage(f"./120image/chengyao/{pic1}.jpg")
            chengyao_img = self.m_resize(chengyao_img)
            pixmap = QPixmap.fromImage(chengyao_img)
            self.chengyao_3.setPixmap(pixmap)
        else: self.chengyao_3.setPixmap(QPixmap.fromImage(self.img))
        #self.check_answer(ans)
        al = ["A", "B", "C", "D", "E", "无"]
        self.answer_t.setText(f"正确答案：{al[ans]}, 你的答案：{al[self.chosens[self.q_page]]}")
        if ans == self.chosens[self.q_page]:
            self.answer_t.setStyleSheet("color:green")
        else: self.answer_t.setStyleSheet("color:red")
        
    def jiesuchakan(self):
        self.ui.menu.setEnabled(True)
        self.ui.menu_2.setEnabled(True)
        self.ui.menu_3.setEnabled(True)
        self.ui.menu_4.setEnabled(True)
        self.ui.menu_5.setEnabled(True)
        self.ui.menu_6.setEnabled(True)
        self.ui.menu_7.setEnabled(True)
        self.next_q.clicked.disconnect(self.next_ques_2)
        self.prev_q.clicked.disconnect(self.prev_ques_2)

        self.tijiaoshijuan.clicked.disconnect(self.jiesuchakan)
        self.tijiaoshijuan.clicked.connect(self.tijiao)
        self.tijiaoshijuan.setText("提交试卷")
        self.go_Home()
    
    def next_ques_2(self):
        '''self.A.setCheckable(False)
        self.B.setCheckable(False)
        self.C.setCheckable(False)
        self.D.setCheckable(False)
        self.E.setCheckable(False)'''
        if self.q_page == 0:self.prev_q.setEnabled(True)
        if self.q_page == self.q_num - 2:
            self.next_q.setEnabled(False)
            #self.tijiaoshijuan.setEnabled(True)
            #return
        self.q_page = self.q_page + 1
        self.current_page.setText(f"{self.q_page + 1}/{self.q_num}")
        #title, pic0, pic1, a, b, c, d, e, ans = get_ques(f"\"{self.q_list[self.q_page]}\"")
        title, pic0, pic1, choices, ans = get_ques(str(self.q_list[self.q_page])).values()
        a, b, c, d, e = choices.values()
        self.tb_A.setText(a)
        self.tb_B.setText(b)
        self.tb_C.setText(c)
        self.tb_D.setText(d)
        self.tb_E.setText(e)
        self.title.setText(title)
        self.title.update()
        if pic0 != None:
            zhizhu_img = QImage(f"./120image/zhizhu/{pic0}.jpg")
            zhizhu_img = self.m_resize(zhizhu_img)
            pixmap = QPixmap.fromImage(zhizhu_img)
            self.zhizhu_3.setPixmap(pixmap)
        else: self.zhizhu_3.setPixmap(QPixmap.fromImage(self.img))
        if pic1 != None:
            chengyao_img = QImage(f"./120image/chengyao/{pic1}.jpg")
            chengyao_img = self.m_resize(chengyao_img)
            pixmap = QPixmap.fromImage(chengyao_img)
            self.chengyao_3.setPixmap(pixmap)
        else: self.chengyao_3.setPixmap(QPixmap.fromImage(self.img))
        #self.check_answer(ans)
        al = ["A", "B", "C", "D", "E", "无"]
        self.answer_t.setText(f"正确答案：{al[ans]}, 你的答案：{al[self.chosens[self.q_page]]}")
        if ans == self.chosens[self.q_page]:
            self.answer_t.setStyleSheet("color:green")
        else: self.answer_t.setStyleSheet("color:red")

    def prev_ques_2(self):
        '''self.A.setCheckable(False)
        self.B.setCheckable(False)
        self.C.setCheckable(False)
        self.D.setCheckable(False)
        self.E.setCheckable(False)'''
        if self.q_page == self.q_num - 1:self.next_q.setEnabled(True)
        if self.q_page == 1:
            self.prev_q.setEnabled(False)
            #self.tijiaoshijuan.setEnabled(True)
            #return
        self.q_page = self.q_page - 1
        self.current_page.setText(f"{self.q_page + 1}/{self.q_num}")
        #title, pic0, pic1, a, b, c, d, e, ans = get_ques(f"\"{self.q_list[self.q_page]}\"")
        title, pic0, pic1, choices, ans = get_ques(str(self.q_list[self.q_page])).values()
        a, b, c, d, e = choices.values()
        self.tb_A.setText(a)
        self.tb_B.setText(b)
        self.tb_C.setText(c)
        self.tb_D.setText(d)
        self.tb_E.setText(e)
        self.title.setText(title)
        self.title.update()
        if pic0 != None:
            zhizhu_img = QImage(f"./120image/zhizhu/{pic0}.jpg")
            zhizhu_img = self.m_resize(zhizhu_img)
            pixmap = QPixmap.fromImage(zhizhu_img)
            self.zhizhu_3.setPixmap(pixmap)
        else: self.zhizhu_3.setPixmap(QPixmap.fromImage(self.img))
        if pic1 != None:
            chengyao_img = QImage(f"./120image/chengyao/{pic1}.jpg")
            chengyao_img = self.m_resize(chengyao_img)
            pixmap = QPixmap.fromImage(chengyao_img)
            self.chengyao_3.setPixmap(pixmap)
        else: self.chengyao_3.setPixmap(QPixmap.fromImage(self.img))
        #self.check_answer(ans)
        al = ["A", "B", "C", "D", "E", "无"]
        self.answer_t.setText(f"正确答案：{al[ans]}, 你的答案：{al[self.chosens[self.q_page]]}")
        if ans == self.chosens[self.q_page]:
            self.answer_t.setStyleSheet("color:green")
        else: self.answer_t.setStyleSheet("color:red")

    def set_seed(self):
        self.seed = int(self.exam_num.text())
        self.go_q(self.q_num)

    def v_exit(self):
        self.mplayer.stop()
        self.mplayer.setPosition(0)
        self.ui.menu.setEnabled(True)
        self.ui.menu_2.setEnabled(True)
        self.ui.menu_3.setEnabled(True)
        self.ui.menu_4.setEnabled(True)
        self.ui.menu_5.setEnabled(True)
        self.ui.menu_6.setEnabled(True)
        self.ui.menu_7.setEnabled(True)
        self.go_Home()

    def confirm_f(self):
        chosen = -1
        if self.A1.isChecked(): chosen = 0
        elif self.B1.isChecked(): chosen = 1
        elif self.C1.isChecked(): chosen = 2
        al = ["A", "B", "C", "无"]
        if chosen == self.ans:
            self.answer_2.setText(f"正确答案：{al[self.ans]}, 你的答案：{al[chosen]}")
            self.answer_2.setStyleSheet("color:green")
        else:
            self.answer_2.setText(f"正确答案：{al[self.ans]}, 你的答案：{al[chosen]}")
            self.answer_2.setStyleSheet("color:red")
        self.next_vq.setEnabled(True)
        self.confirm.setEnabled(False)

    def next_video_ques(self):
        self.answer_2.setText('')
        self.mplayer.stop()
        self.v_page += 1
        if self.v_page >= get_v_len():
            self.video_title.setText("视频观看结束，请选择菜单进入其他功能")
            self.ui.menu.setEnabled(True)
            self.ui.menu_2.setEnabled(True)
            self.ui.menu_3.setEnabled(True)
            self.ui.menu_4.setEnabled(True)
            self.ui.menu_5.setEnabled(True)
            self.ui.menu_6.setEnabled(True)
            self.next_vq.setEnabled(False)
            return
        title, video, choices, self.ans = get_v_ques(str(self.v_page)).values()
        a, b, c = choices.values()
        self.media_content = QMediaContent(QUrl.fromLocalFile(video))
        self.mplayer.setMedia(self.media_content)
        self.mplayer.play()
        self.tb_A1.setText(a)
        self.tb_B1.setText(b)
        self.tb_C1.setText(c)
        self.video_title.setText(title)
        self.video_title.update()
        self.next_vq.setEnabled(False)
        self.confirm.setEnabled(True)

    def chengyao_up_f(self):
        self.chengyao_img_name, img_type = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg")
        img = QImage(self.chengyao_img_name)
        img = self.m_resize(img)
        pixmap = QPixmap.fromImage(img)
        self.chengyao_up.setPixmap(pixmap)


    def zhizhu_up_f(self):
        self.zhizhu_img_name, img_type = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg")
        img = QImage(self.zhizhu_img_name)
        img = self.m_resize(img)
        pixmap = QPixmap.fromImage(img)
        self.zhizhu_up.setPixmap(pixmap)
        

    def add_f(self):
        self.status.setText(f"正在添加条目")
        self.status.setStyleSheet("color:black")
        name = self.pte_name.toPlainText()
        zhongzhi = self.pte_zhongzhi.toPlainText()
        paozhi = self.pte_paozhi.toPlainText()
        yaoxing = self.pte_yaoxing.toPlainText()
        zhuzhi = self.pte_zhuzhi.toPlainText()
        with open("./data.json", "r", encoding='utf-8') as f:
            dic = json.load(f)
        dic[name] = {"种植" : zhongzhi,
                    "炮制" : paozhi,
                    "药性" : yaoxing,
                    "主治" : zhuzhi }
        with open("./data.json", "w", encoding='utf-8') as f:  
            json.dump(dic, f, ensure_ascii=False)
        name = self.pte_name.toPlainText()
        if self.chengyao_img_name != None:
            shutil.copy(self.chengyao_img_name, f"./120image/chengyao/{name}.jpg")
        if self.zhizhu_img_name != None:
            shutil.copy(self.zhizhu_img_name, f"./120image/zhizhu/{name}.jpg")
        self.status.setText(f"添加条目“{name}”成功，请重启软件以查看")
        self.status.setStyleSheet("font-size: 16px; color:green")
        self.pte_name.setPlainText("")
        self.pte_zhongzhi.setPlainText("")
        self.pte_paozhi.setPlainText("")
        self.pte_yaoxing.setPlainText("")
        self.pte_zhuzhi.setPlainText("")
        self.zhizhu_up.setPixmap(QPixmap.fromImage(self.img))
        self.chengyao_up.setPixmap(QPixmap.fromImage(self.img))

    def go_Home(self):
        self.ui.menu.setEnabled(True)
        self.ui.menu_2.setEnabled(True)
        self.ui.menu_3.setEnabled(True)
        self.ui.menu_4.setEnabled(True)
        self.ui.menu_5.setEnabled(True)
        self.ui.menu_6.setEnabled(True)
        self.ui.menu_7.setEnabled(True)
        self.stacked_widget.setCurrentIndex(0)

    def go_zhishixuexi(self):
        self.stacked_widget.setCurrentIndex(1)
        self.ui.menu.setEnabled(False)
        self.ui.menu_2.setEnabled(False)
        self.ui.menu_3.setEnabled(False)
        self.ui.menu_4.setEnabled(False)
        self.ui.menu_5.setEnabled(False)
        self.ui.menu_6.setEnabled(False)
        self.ui.menu_7.setEnabled(False)
        self.tingzhixuexi.setEnabled(True)
        self.jixvxuexi.setEnabled(False)
        self.next_page.setEnabled(True)
        self.prev_page.setEnabled(True)
        self.start = time.perf_counter()

    def go_add(self):
        self.stacked_widget.setCurrentIndex(2)

    def go_paozhi(self):
        self.stacked_widget.setCurrentIndex(3)
        #self.init_paozhi()

    def go_mohuchaxun(self):
        self.stacked_widget.setCurrentIndex(4)

    def go_time(self):
        self.stacked_widget.setCurrentIndex(6)
        dic = get_idx_time()
        self.model = QStandardItemModel(len(dic),3)
        self.model.setHorizontalHeaderLabels(["学号", "姓名", "学习时长"])
        for i, k in enumerate(dic):
            item = QStandardItem(k)
            #设置每个位置的文本值
            self.model.setItem(i, 0, item)
            item = QStandardItem(dic[k]["name"])
            self.model.setItem(i, 1, item)
            item = QStandardItem(str(datetime.timedelta(seconds=dic[k]["time"])))
            self.model.setItem(i, 2, item)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def go_q(self, q_num):
        # 创建并初始化一个QTime对象，开始计时
        self.exam_time = QTime(0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.A.setCheckable(True)
        self.B.setCheckable(True)
        self.C.setCheckable(True)
        self.D.setCheckable(True)
        self.E.setCheckable(True)
        self.ui.menu.setEnabled(False)
        self.ui.menu_2.setEnabled(False)
        self.ui.menu_3.setEnabled(False)
        self.ui.menu_4.setEnabled(False)
        self.ui.menu_5.setEnabled(False)
        self.ui.menu_6.setEnabled(False)
        self.ui.menu_7.setEnabled(False)
        self.answer_t.setText("")
        self.prev_q.clicked.connect(self.prev_ques)
        self.next_q.clicked.connect(self.next_ques)
        self.stacked_widget.setCurrentIndex(7)
        self.prev_q.setEnabled(False)
        self.next_q.setEnabled(True)
        #self.tijiaoshijuan.setEnabled(False)
        self.q_set = set()
        #self.seed = seed
        random.seed(self.seed)
        while len(self.q_set) < q_num:
            self.q_set.add(random.randint(0, get_ques_len() - 1))
        self.q_list = list(self.q_set)
        self.q_page = 0
        self.current_page.setText(f"{self.q_page + 1}/{self.q_num}")
        #self.q_num = 20
        self.right = 0
        self.chosens = []
        self.answers = []
        for i in range(q_num):
            self.chosens.append(-1)
            _, _, _, _, ans = get_ques(str(self.q_list[i])).values()
            self.answers.append(ans)
        #self.answers = []
        title, pic0, pic1, choices, self.ans = get_ques(str(self.q_list[self.q_page])).values()
        a, b, c, d, e = choices.values()
        self.tb_A.setText(a)
        self.tb_B.setText(b)
        self.tb_C.setText(c)
        self.tb_D.setText(d)
        self.tb_E.setText(e)
        self.title.setText(title)
        self.title.update()
        if pic0 != None:
            zhizhu_img = QImage(f"./120image/zhizhu/{pic0}.jpg")
            zhizhu_img = self.m_resize(zhizhu_img)
            pixmap = QPixmap.fromImage(zhizhu_img)
            self.zhizhu_3.setPixmap(pixmap)
        else: self.zhizhu_3.setPixmap(QPixmap.fromImage(self.img))
        if pic1 != None:
            chengyao_img = QImage(f"./120image/chengyao/{pic1}.jpg")
            chengyao_img = self.m_resize(chengyao_img)
            pixmap = QPixmap.fromImage(chengyao_img)
            self.chengyao_3.setPixmap(pixmap)
        else: self.chengyao_3.setPixmap(QPixmap.fromImage(self.img))

    def showTime(self):
        # 计算已用时长，并将其显示在标签中
        self.exam_time = self.exam_time.addSecs(1)
        self.time_label.setText(self.exam_time.toString('hh:mm:ss'))

    def go_q20(self):
        self.q_num = 20
        self.exam_num.setText(f"{random.randint(0, 65535)}")
        self.stacked_widget.setCurrentIndex(11)
        #self.go_q(self.q_num)

    def go_q50(self):
        self.q_num = 50
        self.exam_num.setText(f"{random.randint(0, 65535)}")
        self.stacked_widget.setCurrentIndex(11)
        #self.go_q(self.q_num)

    def go_q100(self):
        self.q_num = 100
        self.exam_num.setText(f"{random.randint(0, 65535)}")
        self.stacked_widget.setCurrentIndex(11)
        #self.go_q(self.q_num)

    def go_kaoshichengji(self):
        self.stacked_widget.setCurrentIndex(9)
        dic = get_exam()
        iddic = get_idx_time()
        self.model = QStandardItemModel(len(dic),6)
        self.model.setHorizontalHeaderLabels(["学号", "姓名", "试卷号", "提交时间", "考试用时", "考试成绩"])
        for i, k in enumerate(dic.items()):
            #print(k)
            #('Thu Jan 12 11:38:06 2023', {'id': '001', 'score': 15})
            item = QStandardItem(k[0])
            #设置每个位置的文本值
            self.model.setItem(i, 3, item)
            item = QStandardItem(iddic[k[1]["id"]]["name"])
            self.model.setItem(i, 1, item)
            item = QStandardItem(k[1]["id"])
            self.model.setItem(i, 0, item)
            item = QStandardItem(str(k[1]["score"]))
            self.model.setItem(i, 5, item)
            item = QStandardItem(str(k[1]["exam_time"]))
            self.model.setItem(i, 4, item)
            item = QStandardItem(str(k[1]["seed"]))
            self.model.setItem(i, 2, item)
        self.tableView_2.setModel(self.model)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableView_2.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        '''for i in range(6):
            self.tableView_2.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)'''
        
    def go_video(self):
        self.stacked_widget.setCurrentIndex(12)
        self.ui.menu.setEnabled(False)
        self.ui.menu_2.setEnabled(False)
        self.ui.menu_3.setEnabled(False)
        self.ui.menu_4.setEnabled(False)
        self.ui.menu_5.setEnabled(False)
        self.ui.menu_6.setEnabled(False)
        self.ui.menu_7.setEnabled(False)
        self.next_vq.setEnabled(False)
        self.confirm.setEnabled(True)
        self.v_page = 0
        title, video, choices, self.ans = get_v_ques(str(self.v_page)).values()
        a, b, c = choices.values()
        self.media_content = QMediaContent(QUrl.fromLocalFile(video))
        self.mplayer.setMedia(self.media_content)
        self.mplayer.play()
        self.tb_A1.setText(a)
        self.tb_B1.setText(b)
        self.tb_C1.setText(c)
        self.video_title.setText(title)
        self.video_title.update()


    def go_about(self):
        self.stacked_widget.setCurrentIndex(10)


if __name__ == '__main__':
    #QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    w = MainWindow()
    # 展示窗口
    w.ui.show()

    app.exec()  