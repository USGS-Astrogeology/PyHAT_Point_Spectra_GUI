# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.regrLabel = QtWidgets.QLabel(self.formGroupBox)
        self.regrLabel.setObjectName("regrLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.regrLabel)
        self.regrComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.regrComboBox.setObjectName("regrComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.regrComboBox)
        self.corrLabel = QtWidgets.QLabel(self.formGroupBox)
        self.corrLabel.setObjectName("corrLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.corrLabel)
        self.corrComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.corrComboBox.setObjectName("corrComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.corrComboBox)
        self.storageModeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.storageModeLabel.setObjectName("storageModeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.storageModeLabel)
        self.storageModeComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.storageModeComboBox.setObjectName("storageModeComboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.storageModeComboBox)
        self.verboseLabel = QtWidgets.QLabel(self.formGroupBox)
        self.verboseLabel.setObjectName("verboseLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.verboseLabel)
        self.verboseCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.verboseCheckBox)
        self.theta0Label = QtWidgets.QLabel(self.formGroupBox)
        self.theta0Label.setObjectName("theta0Label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.theta0Label)
        self.optimizerLabel = QtWidgets.QLabel(self.formGroupBox)
        self.optimizerLabel.setObjectName("optimizerLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.optimizerLabel)
        self.optimizerComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.optimizerComboBox.setObjectName("optimizerComboBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.optimizerComboBox)
        self.randomStartLabel = QtWidgets.QLabel(self.formGroupBox)
        self.randomStartLabel.setObjectName("randomStartLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.randomStartLabel)
        self.randomStartLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.randomStartLineEdit.setObjectName("randomStartLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.randomStartLineEdit)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.theta0LineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.theta0LineEdit.setObjectName("theta0LineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.theta0LineEdit)
        self.reductionMethodComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.reductionMethodComboBox.setObjectName("reductionMethodComboBox")
        self.reductionMethodComboBox.addItem("")
        self.reductionMethodComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reductionMethodComboBox)
        self.reductionMethodLabel = QtWidgets.QLabel(self.formGroupBox)
        self.reductionMethodLabel.setObjectName("reductionMethodLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.reductionMethodLabel)
        self.numOfComponenetsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.numOfComponenetsLabel.setObjectName("numOfComponenetsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfComponenetsLabel)
        self.numOfComponenetsLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.numOfComponenetsLineEdit.setObjectName("numOfComponenetsLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfComponenetsLineEdit)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setToolTip(("<html><head/><body><p><span style=\" font-weight:600;\">Gaussian Processes (GP)</span>�are a generic supervised learning method designed to solve�<span style=\" font-style:italic;\">regression</span>�and�<span style=\" font-style:italic;\">probabilistic classification</span>�problems.</p><p>The advantages of Gaussian processes are:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">The prediction interpolates the observations (at least for regular kernels).</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">The prediction is probabilistic (Gaussian) so that one can compute empirical confidence intervals and decide based on those if one should refit (online fitting, adaptive fitting) the prediction in some region of interest.</li><li style=\" margin-top:0px; margin-bottom:10px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">Versatile: different�<a href=\"http://scikit-learn.org/stable/modules/gaussian_process.html#gp-kernels\"><span style=\" color:#2878a2;\">kernels</span></a>�can be specified. Common kernels are provided, but it is also possible to specify custom kernels.</li></ul><p>The disadvantages of Gaussian processes include:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">They are not sparse, i.e., they use the whole samples/features information to perform the prediction.</li><li style=\" margin-top:0px; margin-bottom:10px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">They lose efficiency in high dimensional spaces � namely when the number of features exceeds a few dozens.</li></ul><p><a name=\"gaussian-process-regression-gpr\"/><br/></p></body></html>"))
        self.formGroupBox.setTitle(("Gaussian Process"))
        self.regrLabel.setText(("Regression Types"))
        self.corrLabel.setText(("Correlation Types"))
        self.storageModeLabel.setText(("Storage Mode"))
        self.verboseLabel.setText(("Verbose"))
        self.theta0Label.setText(("Theta 0"))
        self.optimizerLabel.setText(("Optimizer Types"))
        self.randomStartLabel.setText(("Random Start"))
        self.normalizeLabel.setText(("Normalize"))
        self.reductionMethodComboBox.setItemText(0, ("PCA"))
        self.reductionMethodComboBox.setItemText(1, ("ICA"))
        self.reductionMethodLabel.setText(("Choose dimensionality reduction method:"))
        self.numOfComponenetsLabel.setText(("Number of Components"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

