# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw_test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.horizontalLayout_4.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_project_name = QtWidgets.QLabel(self.widget_6)
        self.label_project_name.setObjectName("label_project_name")
        self.verticalLayout_12.addWidget(self.label_project_name)
        self.label_analyst = QtWidgets.QLabel(self.widget_6)
        self.label_analyst.setObjectName("label_analyst")
        self.verticalLayout_12.addWidget(self.label_analyst)
        self.label_agency = QtWidgets.QLabel(self.widget_6)
        self.label_agency.setObjectName("label_agency")
        self.verticalLayout_12.addWidget(self.label_agency)
        self.horizontalLayout_4.addWidget(self.widget_6)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.toolBox = QtWidgets.QToolBox(self.widget_2)
        self.toolBox.setObjectName("toolBox")
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setGeometry(QtCore.QRect(0, 0, 178, 293))
        self.page_15.setObjectName("page_15")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_15)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.page_15)
        self.treeWidget_3.setObjectName("treeWidget_3")
        self.verticalLayout.addWidget(self.treeWidget_3)
        self.pushButton_first_chart = QtWidgets.QPushButton(self.page_15)
        self.pushButton_first_chart.setObjectName("pushButton_first_chart")
        self.verticalLayout.addWidget(self.pushButton_first_chart)
        self.toolBox.addItem(self.page_15, "")
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setGeometry(QtCore.QRect(0, 0, 178, 293))
        self.page_16.setObjectName("page_16")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_16)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.page_16)
        self.listWidget_4.setObjectName("listWidget_4")
        self.verticalLayout_3.addWidget(self.listWidget_4)
        self.pushButton_sec_chart = QtWidgets.QPushButton(self.page_16)
        self.pushButton_sec_chart.setObjectName("pushButton_sec_chart")
        self.verticalLayout_3.addWidget(self.pushButton_sec_chart)
        self.toolBox.addItem(self.page_16, "")
        self.page_18 = QtWidgets.QWidget()
        self.page_18.setGeometry(QtCore.QRect(0, 0, 217, 272))
        self.page_18.setObjectName("page_18")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_18)
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.page_18)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.dateEdit_start = QtWidgets.QDateEdit(self.page_18)
        self.dateEdit_start.setCalendarPopup(True)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.verticalLayout_5.addWidget(self.dateEdit_start)
        self.label_13 = QtWidgets.QLabel(self.page_18)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.dateEdit_end = QtWidgets.QDateEdit(self.page_18)
        self.dateEdit_end.setCalendarPopup(True)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.verticalLayout_5.addWidget(self.dateEdit_end)
        self.widget_3 = QtWidgets.QWidget(self.page_18)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_range_button = QtWidgets.QPushButton(self.widget_3)
        self.add_range_button.setObjectName("add_range_button")
        self.horizontalLayout_3.addWidget(self.add_range_button)
        self.del_range_button = QtWidgets.QPushButton(self.widget_3)
        self.del_range_button.setObjectName("del_range_button")
        self.horizontalLayout_3.addWidget(self.del_range_button)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.treeWidget = QtWidgets.QTreeWidget(self.page_18)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.toolBox.addItem(self.page_18, "")
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setGeometry(QtCore.QRect(0, 0, 178, 293))
        self.page_17.setObjectName("page_17")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_17)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_11 = QtWidgets.QCheckBox(self.page_17)
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout_4.addWidget(self.checkBox_11)
        self.checkBox_13 = QtWidgets.QCheckBox(self.page_17)
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_4.addWidget(self.checkBox_13)
        self.checkBox_14 = QtWidgets.QCheckBox(self.page_17)
        self.checkBox_14.setChecked(True)
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout_4.addWidget(self.checkBox_14)
        self.checkBox_15 = QtWidgets.QCheckBox(self.page_17)
        self.checkBox_15.setChecked(True)
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout_4.addWidget(self.checkBox_15)
        self.checkBox_12 = QtWidgets.QCheckBox(self.page_17)
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_4.addWidget(self.checkBox_12)
        self.checkBox = QtWidgets.QCheckBox(self.page_17)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.create_charts_button = QtWidgets.QPushButton(self.page_17)
        self.create_charts_button.setObjectName("create_charts_button")
        self.verticalLayout_4.addWidget(self.create_charts_button)
        self.toolBox.addItem(self.page_17, "")
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setGeometry(QtCore.QRect(0, 0, 193, 272))
        self.page_20.setObjectName("page_20")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_20)
        self.verticalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.page_20)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.verticalLayout_8.addWidget(self.treeWidget_2)
        self.widget_7 = QtWidgets.QWidget(self.page_20)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_7)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout_8.addWidget(self.widget_7)
        self.pushButton_tmc_subset = QtWidgets.QPushButton(self.page_20)
        self.pushButton_tmc_subset.setObjectName("pushButton_tmc_subset")
        self.verticalLayout_8.addWidget(self.pushButton_tmc_subset)
        self.toolBox.addItem(self.page_20, "")
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setGeometry(QtCore.QRect(0, 0, 178, 293))
        self.page_19.setObjectName("page_19")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_19)
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.page_19)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        self.filter1 = QtWidgets.QSlider(self.page_19)
        self.filter1.setOrientation(QtCore.Qt.Horizontal)
        self.filter1.setObjectName("filter1")
        self.verticalLayout_6.addWidget(self.filter1)
        self.label_15 = QtWidgets.QLabel(self.page_19)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        self.filter2 = QtWidgets.QSlider(self.page_19)
        self.filter2.setOrientation(QtCore.Qt.Horizontal)
        self.filter2.setInvertedAppearance(False)
        self.filter2.setObjectName("filter2")
        self.verticalLayout_6.addWidget(self.filter2)
        self.label_16 = QtWidgets.QLabel(self.page_19)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.filter3 = QtWidgets.QSlider(self.page_19)
        self.filter3.setOrientation(QtCore.Qt.Horizontal)
        self.filter3.setObjectName("filter3")
        self.verticalLayout_6.addWidget(self.filter3)
        self.toolBox.addItem(self.page_19, "")
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setGeometry(QtCore.QRect(0, 0, 178, 293))
        self.page_21.setObjectName("page_21")
        self.formLayout = QtWidgets.QFormLayout(self.page_21)
        self.formLayout.setContentsMargins(1, 1, 1, 1)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton_6)
        self.toolBox.addItem(self.page_21, "")
        self.verticalLayout_2.addWidget(self.toolBox)
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 250))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 176, 194))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        # self.webView_minimap = QtWebKitWidgets.QWebView(self.scrollAreaWidgetContents)
        self.webView_minimap = QtWebKitWidgets.QWebEngineView(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView_minimap.sizePolicy().hasHeightForWidth())
        self.webView_minimap.setSizePolicy(sizePolicy)
        self.webView_minimap.setUrl(QtCore.QUrl("about:blank"))
        self.webView_minimap.setObjectName("webView_minimap")
        self.verticalLayout_7.addWidget(self.webView_minimap)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.widget_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 250))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 250))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../NPMRDS_Data_Tool/FHWA-1080x353.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_11.addWidget(self.textEdit_2)
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_new_proj = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_new_proj.setFont(font)
        self.pushButton_new_proj.setObjectName("pushButton_new_proj")
        self.horizontalLayout_2.addWidget(self.pushButton_new_proj)
        self.pushButton_open_proj = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_open_proj.setFont(font)
        self.pushButton_open_proj.setObjectName("pushButton_open_proj")
        self.horizontalLayout_2.addWidget(self.pushButton_open_proj)
        self.pushButton_exit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_2.addWidget(self.pushButton_exit)
        self.verticalLayout_11.addWidget(self.widget)
        self.textEdit_2.raise_()
        self.widget.raise_()
        self.label_2.raise_()
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        # self.webView_map = QtWebKitWidgets.QWebView(self.tab_3)
        self.webView_map = QtWebKitWidgets.QWebEngineView(self.tab_3)
        self.webView_map.setUrl(QtCore.QUrl("about:blank"))
        self.webView_map.setObjectName("webView_map")
        self.verticalLayout_10.addWidget(self.webView_map)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        self.menuChartOptions = QtWidgets.QMenu(self.menubar)
        self.menuChartOptions.setObjectName("menuChartOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionView_Extra_Time = QtWidgets.QAction(MainWindow)
        self.actionView_Extra_Time.setObjectName("actionView_Extra_Time")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuChartOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FHWA Analytics Tool"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Project:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Analyst:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Agency:</span></p></body></html>"))
        self.label_project_name.setText(_translate("MainWindow", "Name"))
        self.label_analyst.setText(_translate("MainWindow", "JLT"))
        self.label_agency.setText(_translate("MainWindow", "KAI"))
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "Dataset"))
        self.pushButton_first_chart.setText(_translate("MainWindow", "Load Spatial Charts"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_15), _translate("MainWindow", "Dataset"))
        self.pushButton_sec_chart.setText(_translate("MainWindow", "Load Temporal Charts"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_16), _translate("MainWindow", "Data Type"))
        self.label_12.setText(_translate("MainWindow", "Start Date"))
        self.label_13.setText(_translate("MainWindow", "End Date"))
        self.add_range_button.setText(_translate("MainWindow", "Add Range"))
        self.del_range_button.setText(_translate("MainWindow", "Delete Range"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Date Range"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_18), _translate("MainWindow", "Date Ranges"))
        self.checkBox_11.setText(_translate("MainWindow", "Speed Band"))
        self.checkBox_13.setText(_translate("MainWindow", "Extra Time Comparison"))
        self.checkBox_14.setText(_translate("MainWindow", "Travel Time Distribution"))
        self.checkBox_15.setText(_translate("MainWindow", "Speed Frequency"))
        self.checkBox_12.setText(_translate("MainWindow", "Travel Time Trends"))
        self.checkBox.setText(_translate("MainWindow", "Congestion Stack"))
        self.create_charts_button.setText(_translate("MainWindow", "Analyze Before/After"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_17), _translate("MainWindow", "Analysis Type"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "ID"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "Name"))
        self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "Dir"))
        self.treeWidget_2.headerItem().setText(3, _translate("MainWindow", "TMC Mi"))
        self.treeWidget_2.headerItem().setText(4, _translate("MainWindow", "Total Mi"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Selected Length:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "0.0 miles"))
        self.pushButton_tmc_subset.setText(_translate("MainWindow", "Update"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_20), _translate("MainWindow", "TMCs"))
        self.label_14.setText(_translate("MainWindow", "Filter #1"))
        self.label_15.setText(_translate("MainWindow", "Filter #2"))
        self.label_16.setText(_translate("MainWindow", "Filter #3"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_19), _translate("MainWindow", "Data Filtering"))
        self.pushButton_5.setText(_translate("MainWindow", "Summary Report"))
        self.pushButton_6.setText(_translate("MainWindow", "Detailed Report"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_21), _translate("MainWindow", "Reports"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#00007f;\">Sketch Planning Analytics Tool</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:36pt; color:#00007f;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#00007f;\">Developed by Kittelson and Associates, Inc.</span></p></body></html>"))
        self.pushButton_new_proj.setText(_translate("MainWindow", "Create New"))
        self.pushButton_open_proj.setText(_translate("MainWindow", "Open Existing"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Welcome"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Facility Map"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.menuChartOptions.setTitle(_translate("MainWindow", "Chart Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoad_Data.setText(_translate("MainWindow", "Load Data"))
        self.actionView_Extra_Time.setText(_translate("MainWindow", "View Extra Time"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

from PyQt5 import QtWebEngineWidgets as QtWebKitWidgets
