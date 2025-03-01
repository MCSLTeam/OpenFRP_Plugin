from PyQt5.QtCore import QSize, QRect
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QSizePolicy,
    QHBoxLayout,
)

from qfluentwidgets import (
    BodyLabel,
    PrimaryPushButton,
    PushButton,
    SubtitleLabel,
)


class LoginContainer(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("loginContainer")

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(QSize(485, 250))
        self.loginWidget = QWidget(self)
        self.loginWidget.setGeometry(QRect(10, 20, 462, 250))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginWidget.sizePolicy().hasHeightForWidth())
        self.loginWidget.setSizePolicy(sizePolicy)
        self.loginWidget.setMinimumSize(QSize(350, 241))
        self.loginWidget.setMaximumSize(QSize(462, 250))
        self.loginWidget.setObjectName("loginWidget")

        self.gridLayout = QGridLayout(self.loginWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.loginTitle = SubtitleLabel(self.loginWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginTitle.sizePolicy().hasHeightForWidth())
        self.loginTitle.setSizePolicy(sizePolicy)
        self.loginTitle.setObjectName("loginTitle")

        self.gridLayout.addWidget(self.loginTitle, 0, 0, 1, 1)
        self.tipLabel = BodyLabel(self.loginWidget)
        self.tipLabel.setObjectName("tipLabel")

        self.gridLayout.addWidget(self.tipLabel, 1, 0, 1, 1)
        self.loginBtnWidget = QWidget(self.loginWidget)
        self.loginBtnWidget.setObjectName("loginBtnWidget")

        self.horizontalLayout = QHBoxLayout(self.loginBtnWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.loginBtn = PrimaryPushButton(self.loginBtnWidget)
        self.loginBtn.setObjectName("loginBtn")

        self.horizontalLayout.addWidget(self.loginBtn)
        self.cancelBtn = PushButton(self.loginBtnWidget)
        self.cancelBtn.setObjectName("cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)
        self.gridLayout.addWidget(self.loginBtnWidget, 2, 0, 1, 1)

        self.loginTitle.setText("登录 OpenFrp")
        self.tipLabel.setText("在点击按钮后，我们将打开浏览器进行授权，请您知晓。")
        self.loginBtn.setText("登录")
        self.cancelBtn.setText("取消")