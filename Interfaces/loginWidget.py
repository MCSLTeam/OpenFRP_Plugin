from PyQt5.QtCore import QSize, QRect, QUrl
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QSizePolicy,
    QHBoxLayout,
)

from qfluentwidgets import (
    BodyLabel,
    HyperlinkLabel,
    LineEdit,
    PrimaryPushButton,
    PushButton,
    TitleLabel,
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
        self.setMinimumSize(QSize(485, 310))
        self.setMaximumSize(QSize(485, 310))
        self.loginWidget = QWidget(self)
        self.loginWidget.setGeometry(QRect(10, 20, 462, 271))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginWidget.sizePolicy().hasHeightForWidth())
        self.loginWidget.setSizePolicy(sizePolicy)
        self.loginWidget.setMinimumSize(QSize(350, 241))
        self.loginWidget.setMaximumSize(QSize(462, 271))
        self.loginWidget.setObjectName("loginWidget")

        self.gridLayout = QGridLayout(self.loginWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.ofAgreementBtnWidget = QWidget(self.loginWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ofAgreementBtnWidget.sizePolicy().hasHeightForWidth()
        )
        self.ofAgreementBtnWidget.setSizePolicy(sizePolicy)
        self.ofAgreementBtnWidget.setObjectName("ofAgreementBtnWidget")

        self.horizontalLayout_2 = QHBoxLayout(self.ofAgreementBtnWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.ofContentLabel = HyperlinkLabel(self.ofAgreementBtnWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ofContentLabel.sizePolicy().hasHeightForWidth()
        )
        self.ofContentLabel.setSizePolicy(sizePolicy)
        self.ofContentLabel.setUrl(QUrl("https://www.openfrp.net/content/"))
        self.ofContentLabel.setObjectName("ofContentLabel")

        self.horizontalLayout_2.addWidget(self.ofContentLabel)
        self.ofPrivacyLabel = HyperlinkLabel(self.ofAgreementBtnWidget)
        self.ofPrivacyLabel.setUrl(QUrl("https://www.openfrp.net/privacy/"))
        self.ofPrivacyLabel.setObjectName("ofPrivacyLabel")

        self.horizontalLayout_2.addWidget(self.ofPrivacyLabel)
        self.ofPolicyLabel = HyperlinkLabel(self.ofAgreementBtnWidget)
        self.ofPolicyLabel.setUrl(QUrl("https://www.openfrp.net/policy/"))
        self.ofPolicyLabel.setObjectName("ofPolicyLabel")

        self.horizontalLayout_2.addWidget(self.ofPolicyLabel)
        
        self.ofRegisterLabel = HyperlinkLabel(self.ofAgreementBtnWidget)
        self.ofRegisterLabel.setUrl(QUrl("https://console.openfrp.net/register"))
        self.ofRegisterLabel.setObjectName("ofRegisterLabel")

        self.horizontalLayout_2.addWidget(self.ofRegisterLabel)
        self.gridLayout.addWidget(self.ofAgreementBtnWidget, 4, 0, 1, 1)
        self.loginTitle = TitleLabel(self.loginWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginTitle.sizePolicy().hasHeightForWidth())
        self.loginTitle.setSizePolicy(sizePolicy)
        self.loginTitle.setObjectName("loginTitle")

        self.gridLayout.addWidget(self.loginTitle, 0, 0, 1, 1)
        self.userNameLineEdit = LineEdit(self.loginWidget)
        self.userNameLineEdit.setDragEnabled(False)
        self.userNameLineEdit.setProperty("transparent", True)
        self.userNameLineEdit.setObjectName("userNameLineEdit")

        self.gridLayout.addWidget(self.userNameLineEdit, 2, 0, 1, 1)
        self.tipLabel = BodyLabel(self.loginWidget)
        self.tipLabel.setObjectName("tipLabel")

        self.gridLayout.addWidget(self.tipLabel, 1, 0, 1, 1)
        self.passwordLineEdit = LineEdit(self.loginWidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")

        self.gridLayout.addWidget(self.passwordLineEdit, 3, 0, 1, 1)
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
        self.gridLayout.addWidget(self.loginBtnWidget, 5, 0, 1, 1)

        self.ofContentLabel.setText("OpenFrp 内容策略")
        self.ofPrivacyLabel.setText("OpenFrp 隐私策略")
        self.ofPolicyLabel.setText("OpenFrp 服务条款")
        self.loginTitle.setText("登录")
        self.userNameLineEdit.setPlaceholderText("用户名或邮箱")
        self.tipLabel.setText("登录 OpenFrp 账户即代表您遵守以下协议。")
        self.passwordLineEdit.setPlaceholderText("密码")
        self.loginBtn.setText("登录")
        self.cancelBtn.setText("取消")
