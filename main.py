from functions import*

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Settings Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1078, 768))
        MainWindow.setFixedSize(1078, 768)
        MainWindow.setWindowIcon(QtGui.QIcon('img/mainIcon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Graph plot
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setGeometry(QtCore.QRect(450, 20, 541, 661))
        layout.addWidget(self.canvas,10, QtCore.Qt.AlignLeft | QtCore.Qt.AlignRight)

        # Window TabWidget - DON'T CHANGE ANYTHING
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 361, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        # CheckBox - Directed
        self.checkBox_YesDir = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_YesDir.setGeometry(QtCore.QRect(20, 340, 101, 20))
        self.checkBox_YesDir.setObjectName("checkBox_YesDir")

        # CheckBox - Not Directed
        self.checkBox_NotDir = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_NotDir.setGeometry(QtCore.QRect(130, 340, 121, 20))
        self.checkBox_NotDir.setObjectName("checkBox_NotDir")

        # Add one Widget
        self.Inser = QtWidgets.QWidget()
        self.Inser.setObjectName("Inser")

        # Set size of the font
        font = QtGui.QFont()
        font.setPointSize(10)

        # Start the constructors of QLabel's class, If you'll need to change, please go to class 'retranslateUi"
        self.label = QtWidgets.QLabel(self.tab)
        self.label_2 = QtWidgets.QLabel(self.Inser)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)

        # Set Geometry
        self.label.setGeometry(QtCore.QRect(10, 0, 231, 20))
        self.label_2.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label_3.setGeometry(QtCore.QRect(20, 380, 271, 16))
        self.label_4.setGeometry(QtCore.QRect(450, 14, 371, 16))
        self.label_5.setGeometry(QtCore.QRect(580, 14, 151, 16))
        self.label_6.setGeometry(QtCore.QRect(20, 430, 261, 16))
        self.label_7.setGeometry(QtCore.QRect(20, 450, 221, 16))
        self.label_8.setGeometry(QtCore.QRect(20, 470, 221, 16))
        self.label_9.setGeometry(QtCore.QRect(20, 510, 291, 16))
        self.label_10.setGeometry(QtCore.QRect(20, 560, 261, 16))
        self.label_11.setGeometry(QtCore.QRect(20, 580, 221, 16))
        self.label_12.setGeometry(QtCore.QRect(20, 600, 221, 16))
        self.label_13.setGeometry(QtCore.QRect(20, 630, 311, 16))
        self.label_14.setGeometry(QtCore.QRect(20, 690, 261, 16))

        #  Set Font
        self.label.setFont(font)
        self.label_2.setFont(font)

        # Set objects Name
        self.label.setObjectName("label")
        self.label_2.setObjectName("label_2")
        self.label_3.setObjectName("label_3")
        self.label_4.setObjectName("label_4")
        self.label_5.setObjectName("label_5")
        self.label_6.setObjectName("label_6")
        self.label_7.setObjectName("label_7")
        self.label_8.setObjectName("label_8")
        self.label_9.setObjectName("label_9")
        self.label_10.setObjectName("label_10")
        self.label_11.setObjectName("label_11")
        self.label_12.setObjectName("label_12")
        self.label_13.setObjectName("label_13")
        self.label_14.setObjectName("label_14")

        # Nodes and Edges Insertion
        self.inNodesEdges = QtWidgets.QPlainTextEdit(self.tab)
        self.inNodesEdges.setGeometry(QtCore.QRect(10, 30, 221, 241))
        self.inNodesEdges.setObjectName("inNodesEdges")

        # Adjacent Insertion - Get wich nodes are adjacents with one specific node
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 400, 131, 22))
        self.lineEdit.setObjectName("lineEdit")

        # Verteex Insertion - Get verteex of graph
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 530, 131, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # adjacent Nodes Insertion - Get if two nodes are adjacent
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 650, 131, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 650, 131, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")

        # Manual insertion Button
        self.SendManual = QtWidgets.QPushButton(self.tab)
        self.SendManual.setGeometry(QtCore.QRect(240, 240, 93, 28))
        self.SendManual.setObjectName("SendManual")
        self.tabWidget.addTab(self.tab, "")

        # Lote insertion Button
        self.SendLote = QtWidgets.QPushButton(self.Inser)
        self.SendLote.setGeometry(QtCore.QRect(30, 70, 93, 28))
        self.SendLote.setObjectName("SendLote")

        # Adjacent Insertion Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")

        # Verteex Insertion Button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 530, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        # Adjacent Nodes Insertion Button
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 650, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        
        #Qtool Button
        self.sendTxt = QtWidgets.QToolButton(self.Inser)
        self.sendTxt.setGeometry(QtCore.QRect(130, 20, 41, 31))
        self.sendTxt.setObjectName("sendTxt")

        self.tabWidget.addTab(self.Inser, "")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(450, 20, 541, 661))
        self.widget.setObjectName("widget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self.translate("MainWindow", "Grafos"))
        self.checkBox_YesDir.setText(self.translate("MainWindow", "Direcionado"))
        self.checkBox_NotDir.setText(self.translate("MainWindow", "Não-Direcionado"))
        self.label.setText(self.translate("MainWindow", "Digite os Vértices e Arestas:"))
        self.SendManual.setText(self.translate("MainWindow", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), self.translate("MainWindow", "Inserção Manual"))
        self.label_2.setText(self.translate("MainWindow", "Envio por Lote"))
        self.sendTxt.setText(self.translate("MainWindow", "..."))
        self.SendLote.setText(self.translate("MainWindow", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inser), self.translate("MainWindow", "Inserção Lote"))
        ## New Insertions
        self.label_3.setText(self.translate("MainWindow", "Digite o vértice para verificar a adjacência: "))
        self.label_4.setText(self.translate("MainWindow", "Ordem do Grafo: X"))
        self.label_5.setText(self.translate("MainWindow", "Tamanho do Grafo: X"))
        self.label_6.setText(self.translate("MainWindow", "A lista de vértices adjacentes é:"))
        self.label_7.setText(self.translate("MainWindow", "Vértices adjacentes de entrada:"))
        self.label_8.setText(self.translate("MainWindow", "Vértices adjacentes de saída:"))
        self.label_9.setText(self.translate("MainWindow", "Digite o vértice para verificar o grau do mesmo: "))
        self.pushButton.setText(self.translate("MainWindow", "Ok"))
        self.pushButton_2.setText(self.translate("MainWindow", "Ok"))
        self.label_10.setText(self.translate("MainWindow", "O grau do vértice é:"))
        self.label_11.setText(self.translate("MainWindow", "O grau do vértice de entrada é:"))
        self.label_12.setText(self.translate("MainWindow", "O grau do vértice de saída é:"))
        self.label_13.setText(self.translate("MainWindow", "Digite dois vértices para verificar se são adjacentes:"))
        self.pushButton_3.setText(self.translate("MainWindow", "Ok"))
        self.label_14.setText(self.translate("MainWindow", "Os vértices são:"))
        
        # Events Button
        self.SendManual.clicked.connect(self.mainGrapf)
        self.sendTxt.clicked.connect(self.forLote)
        self.SendLote.clicked.connect(self.mainGrapf)
        self.pushButton.clicked.connect(self.adjEdges)
        self.pushButton_2.clicked.connect(self.vertexDegree)
        self.pushButton_3.clicked.connect(self.adjNodes)

    ## Our Functions
    def send(self,edges):
        try:
            if(len(edges) > 0):
                if(self.checkBox_YesDir.text() == 'Direcionado' and self.checkBox_YesDir.isChecked() and not self.checkBox_NotDir.isChecked()):
                    self.dirOrNot = 1
                elif(self.checkBox_NotDir.text() == 'Não-Direcionado' and self.checkBox_NotDir.isChecked() and not self.checkBox_YesDir.isChecked()):
                    self.dirOrNot = 0
                else:
                    msg = QMessageBox.about(MainWindow, "Aviso!", "Você precisa escolher a opção direcionado ou não para o grafo funcionar")
                    msg.setWindowIcon(QtGui.QIcon('img/icon.png'))
                    self.dirOrNot = -1
            else:
                self.dirOrNot = 0
        except:
            print("Error send")
            self.dirOrNot = -1

    def forInsertion(self):
        f = open('txt\insertion.txt','w')
        f.close()
        f = open('txt\insertion.txt','a')
        in1 = self.inNodesEdges.toPlainText()
        f.writelines(in1)
        f.close()

    def forLote(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
    
    def way(self):
        
            self.LotOrNot = self.tabWidget.currentIndex()
            if(self.LotOrNot == 1):
                try:
                    with open(self.path) as f:
                        self.in1 = f.readlines()
                except:
                    QMessageBox.about(MainWindow, "Aviso!", "Insira um arquivo")
                    self.in1 = []
            elif(self.LotOrNot == 0):
                self.forInsertion()
                with open('txt\insertion.txt') as f:
                    self.in1 = f.readlines()
        
    def showGraph(self,G,res):
        if(self.strvalOrNot == 'Valorado'):
            pos = nx.spring_layout(G,k=50)
            nx.draw(G,pos,edge_color='black',node_size=500,node_color='pink',labels={node:node for node in G.nodes()})
            nx.draw_networkx_edge_labels(G,pos,edge_labels=res,font_color='red')
            plt.axis('off')
            self.canvas.draw_idle()
        else:
            pos = nx.spring_layout(G,k=50)
            nx.draw(G,pos,edge_color='black',node_size=500,node_color='pink',labels={node:node for node in G.nodes()})
            plt.axis('off')
            self.canvas.draw_idle()

    def adjEdges(self):
            try:
                self.in1 = []
                self.out = []

                value = self.lineEdit.text()

                if(self.dirOrNot == 1):
                    self.in1 = [n for n in self.G.predecessors(value)] 
                    self.out = [n for n in self.G.neighbors(value)] 
                    if(len(self.in1) > 0 and len(self.out) > 0):
                        self.label_6.setText(self.translate("MainWindow", " A lista de vértices adjacentes é: "+str(self.in1+self.out)))
                        self.label_7.setText(self.translate("MainWindow", "Vértices adjacentes de entrada: "+ str(self.in1)))
                        self.label_8.setText(self.translate("MainWindow", "Vértices adjacentes de saída: "+ str(self.out)))
                    elif(len(self.in1) > 0 and len(self.out) < 0):
                        self.label_6.setText(self.translate("MainWindow", " A lista de vértices adjacentes é: "+str(self.in1+self.out)))
                        self.label_7.setText(self.translate("MainWindow", "Vértices adjacentes de entrada: "+ str(self.in1)))
                        self.label_8.setText(self.translate("MainWindow", "Vértices adjacentes de saída: "+ str(self.out)))
                    
                    elif(len(self.in1) < 0 and len(self.out) > 0):
                        self.label_6.setText(self.translate("MainWindow", " A lista de vértices adjacentes é: "+str(self.in1+self.out)))
                        self.label_7.setText(self.translate("MainWindow", "Vértices adjacentes de entrada: "+ str(self.in1)))
                        self.label_8.setText(self.translate("MainWindow", "Vértices adjacentes de saída: "+ str(self.out)))

                    elif(len(self.in1) < 0 and len(self.out) < 0):
                        self.label_6.setText(self.translate("MainWindow", " A lista de vértices adjacentes é: "+str(self.in1+self.out)))
                        self.label_8.setText(self.translate("MainWindow", "Vértices adjacentes de saída: "+ str(self.out)))
                        self.label_7.setText(self.translate("MainWindow", "Vértices adjacentes de entrada: "+ str(self.in1)))
                    else:
                        self.label_6.setText(self.translate("MainWindow", " A lista de vértices adjacentes é: "+str(self.in1+self.out)))
                        self.label_8.setText(self.translate("MainWindow", "Vértices adjacentes de saída: "+ str(self.out)))
                        self.label_7.setText(self.translate("MainWindow", "Vértices adjacentes de entrada: "+ str(self.in1)))
                else:
                    in1 = [n for n in self.G.neighbors(value)] 
                    self.label_6.setText(self.translate("MainWindow", " A lista de vértices adjacentes é: "+ str(in1)))
                    self.label_7.setText(self.translate("MainWindow", "Vértices adjacentes de entrada: X"))
                    self.label_8.setText(self.translate("MainWindow", "Vértices adjacentes de saída: X "))
            except:
                QMessageBox.about(MainWindow, "Aviso!", "Não existe o vértice informado")
    
    def adjNodes(self):
        try:
            primary = self.lineEdit_3.text()
            secondary = self.lineEdit_4.text()


            if (self.dirOrNot == 1):
                adjacentes = [n for n in self.G.neighbors(primary)]
                adjacentes1 = adjacentes + [n for n in self.G.predecessors(primary)]
            else:
                adjacentes1 = [n for n in self.G.neighbors(primary)]

            if secondary in adjacentes1:
                self.label_14.setText(self.translate("MainWindow", "Os vértices são: Adjacentes"))
            else:
                self.label_14.setText(self.translate("MainWindow", "Os vértices são: Não-adjacentes"))
        except:
            QMessageBox.about(MainWindow, "Aviso!", "Não existe o vértice informado.")

    def vertexDegree(self):
        try:
            valueNode = self.lineEdit_2.text()
            self.label_10.setText(self.translate("MainWindow", "O grau do vértice é: "+ str (self.G.degree[valueNode])))

            if(self.dirOrNot == 1):
                in2 = [n for n in self.G.predecessors(valueNode)] #direcionado = adjacentes de entrada
                out2 = [n for n in self.G.neighbors(valueNode)] #direcionado = adjacentes de saída
                self.label_11.setText(self.translate("MainWindow", "O grau do vértice de entrada é:  "+ str(len(in2))))
                self.label_12.setText(self.translate("MainWindow", "O grau do vértice de saída é:  "+ str(len(out2))))
        except:
            QMessageBox.about(MainWindow, "Aviso!", "Não existe o vértice informado")

    def getOS(self,G):
        self.label_4.setText(self.translate("MainWindow", "Ordem do Grafo: "+str(G.number_of_nodes())))
        self.label_5.setText(self.translate("MainWindow", "Tamanho do Grafo: "+str( G.number_of_edges())))
        
    def mainGrapf(self):
        try:
            self.figure.clear()
            self.way()
            nodes,edges,self.strvalOrNot = insertion(self.in1,MainWindow)
            self.send(edges)
            self.G = direction(self.dirOrNot)
            self.G,res = valOrNot(self.strvalOrNot,self.G,edges,nodes)
            self.showGraph(self.G,res)
            self.getOS(self.G)
        except NameError:
            print("Error main Graph")

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        
        sys.exit(app.exec_())
    except NameError:
        print("Error main")
