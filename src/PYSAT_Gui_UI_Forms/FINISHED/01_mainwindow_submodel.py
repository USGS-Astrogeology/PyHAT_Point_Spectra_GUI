




        self.scrollAreaWidgetContents_2.setStyleSheet(_fromUtf8("QGroupBox {\n"
"  border: 2px solid gray;\n"
"  border-radius: 6px;\n"
"  margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"  padding-top: -14px;\n"
"  padding-left: 8px;\n"
"}\n"
        self.submodel = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.submodel.setFont(font)
        self.submodel.setObjectName(_fromUtf8("submodel"))
        self.verticalLayout = QtGui.QVBoxLayout(self.submodel)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.submodel_vlayout = QtGui.QVBoxLayout()
        self.submodel_vlayout.setMargin(11)
        self.submodel_vlayout.setSpacing(6)
        self.submodel_vlayout.setObjectName(_fromUtf8("submodel_vlayout"))
        self.submodel_choosedata_hlayout = QtGui.QHBoxLayout()
        self.submodel_choosedata_hlayout.setMargin(11)
        self.submodel_choosedata_hlayout.setSpacing(6)
        self.submodel_choosedata_hlayout.setObjectName(_fromUtf8("submodel_choosedata_hlayout"))
        self.submodel_choosedata = QtGui.QComboBox(self.submodel)
        self.submodel_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.submodel_choosedata.setObjectName(_fromUtf8("submodel_choosedata"))
        self.submodel_choosedata_hlayout.addWidget(self.submodel_choosedata)
        self.submodel_choosedata_hlayout.addItem(spacerItem)
        self.submodel_vlayout.addLayout(self.submodel_choosedata_hlayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.submodel)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.submodel)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.submodel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.submodel)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.submodel_vlayout.addLayout(self.horizontalLayout)
        self.submodel_choosealg_hlayout = QtGui.QHBoxLayout()
        self.submodel_choosealg_hlayout.setMargin(11)
        self.submodel_choosealg_hlayout.setSpacing(6)
        self.submodel_choosealg_hlayout.setObjectName(_fromUtf8("submodel_choosealg_hlayout"))
        self.submodel_choosealg = QtGui.QComboBox(self.submodel)
        self.submodel_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.submodel_choosealg.setObjectName(_fromUtf8("submodel_choosealg"))
        self.submodel_choosealg_hlayout.addWidget(self.submodel_choosealg)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_choosealg_hlayout.addItem(spacerItem2)
        self.submodel_vlayout.addLayout(self.submodel_choosealg_hlayout)
        self.regression_ransac_checkbox = QtGui.QCheckBox(self.submodel)
        self.regression_ransac_checkbox.setObjectName(_fromUtf8("regression_ransac_checkbox"))
        self.submodel_vlayout.addWidget(self.regression_ransac_checkbox)
        self.submodel_trainbutton_hlayout = QtGui.QHBoxLayout()
        self.submodel_trainbutton_hlayout.setMargin(11)
        self.submodel_trainbutton_hlayout.setSpacing(6)
        self.submodel_trainbutton_hlayout.setObjectName(_fromUtf8("submodel_trainbutton_hlayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_trainbutton_hlayout.addItem(spacerItem3)
        self.submodel_trainbutton = QtGui.QPushButton(self.submodel)
        self.submodel_trainbutton.setObjectName(_fromUtf8("submodel_trainbutton"))
        self.submodel_trainbutton_hlayout.addWidget(self.submodel_trainbutton)
        self.submodel_vlayout.addLayout(self.submodel_trainbutton_hlayout)
        self.verticalLayout.addLayout(self.submodel_vlayout)
        self.verticalLayout_8.addWidget(self.submodel)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem4)


        self.submodel.setTitle(_translate("MainWindow", "Files", None))
        self.submodel_choosedata.setItemText(0, _translate("MainWindow", "Choose Data", None))
        self.submodel_choosedata.setItemText(1, _translate("MainWindow", "Known Data", None))
        self.label.setText(_translate("MainWindow", "Min", None))
        self.label_2.setText(_translate("MainWindow", "Max", None))
        self.submodel_choosealg.setItemText(0, _translate("MainWindow", "Choose Algorithm", None))
        self.submodel_choosealg.setItemText(1, _translate("MainWindow", "PLS", None))
        self.submodel_choosealg.setItemText(2, _translate("MainWindow", "GP", None))
        self.submodel_choosealg.setItemText(3, _translate("MainWindow", "Others coming soon...", None))
        self.regression_ransac_checkbox.setText(_translate("MainWindow", "RANSAC", None))
        self.submodel_trainbutton.setText(_translate("MainWindow", "Train Submodels", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))

