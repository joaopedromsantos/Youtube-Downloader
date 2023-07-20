import requests as requests
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, \
    QSizePolicy, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont, QImage
from pytube import YouTube

"""

 EM TRANSIÇÃO

"""

# noinspection PyAttributeOutsideInit
class UiMainWindow(object):
    def __init__(self):
        super().__init__()

    def setup_ui(self, main_window):

        # Here organizes the components
        self.config_main_window(main_window)

        self.center(main_window)

        self.logo()

        self.url()

        self.video()

        self.file_type()

        self.file_location()

        self.button_download()

    @staticmethod
    def config_main_window(main_window):
        # Main_window configuration
        main_window.resize(800, 600)
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(QtCore.Qt.transparent)
        icon = QIcon(transparent_pixmap)
        MainWindow.setWindowIcon(icon)
        main_window.setWindowTitle(' ')

    def center(self, main_window):
        # Center widget
        self.Center_Widget = QWidget(main_window)
        main_window.setCentralWidget(self.Center_Widget)
        self.Center_Widget.setStyleSheet("""
                    background-color: #D9D9D9;

                """)
        self.Center_Widget_layout = QVBoxLayout(self.Center_Widget)
        self.Center_Widget_layout.setContentsMargins(70, 0, 70, 0)
        self.Center_Widget_layout.setSpacing(8)

    def logo(self):
        # Logo widget
        self.Logo_widget = QLabel(self.Center_Widget)
        self.Logo_widget.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("logo.png")
        self.Logo_widget.setPixmap(pixmap)
        self.Center_Widget_layout.addWidget(self.Logo_widget)

    def url(self):
        # Url Parent Widget
        self.Url_widget = QWidget()
        self.Url_layout = QVBoxLayout(self.Url_widget)
        self.Url_layout.setAlignment(Qt.AlignCenter)
        self.Url_layout.setContentsMargins(0, 8, 0, 0)
        self.Url_layout.setSpacing(8)

        # Url Label
        self.Label_url_widget = QLabel('Enter The Url:')
        font = QFont('Jockey One', 16, QFont.Bold)
        self.Label_url_widget.setFont(font)
        self.Label_url_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Url_layout.addWidget(self.Label_url_widget)

        # Url Link
        self.Url_link_widget = QTextEdit()
        self.Url_link_widget.setStyleSheet("""
            border-radius: 5px;
            background: #FFFFFF;
            padding-left: 10px;
            color: #747474;
            font-size: 16px;
            font-family: Fira Sans;
            font-style: normal;
            font-weight: 400;
            line-height: normal;
        """)
        self.Url_link_widget.setMaximumHeight(34)
        self.Url_layout.addWidget(self.Url_link_widget)

        # Url Button
        self.Button_search_widget = QPushButton("Search")
        self.Button_search_widget.setMinimumHeight(33)
        self.Button_search_widget.setMaximumHeight(50)
        self.Button_search_widget.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                background: #747474;
                width: 107px;
                height: 35px;
                color: #FFFFFF;
                font-size: 20px;
                font-family: Fira Sans;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
            }
            QPushButton:hover {
                background: #999999;
            }
            QPushButton:pressed {
                background: #555555;
            }
        """)
        self.Button_search_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Url_layout.addWidget(self.Button_search_widget, alignment=Qt.AlignRight)
        self.Button_search_widget.clicked.connect(self.search_video)  # Conecte o botão ao método search_video

        self.Center_Widget_layout.addWidget(self.Url_widget)

    def video(self):
        # Video Parent Widget
        self.Video_widget = QWidget()
        self.Video_layout = QHBoxLayout(self.Video_widget)
        self.Video_layout.setAlignment(Qt.AlignCenter)
        self.Video_layout.setContentsMargins(0, 0, 0, 0)
        self.Video_layout.setSpacing(8)

        # Video Thumbnail
        self.Thumbnail_widget = QLabel()
        self.Thumbnail_widget.setAlignment(Qt.AlignCenter)
        self.Thumbnail_widget.setStyleSheet("""
            background: white;
        """)
        self.Thumbnail_widget.setFixedSize(240, 135)
        # USAR RESIZE
        self.Video_layout.addWidget(self.Thumbnail_widget)

        # Video Widget Info
        self.Info_widget = QWidget()
        self.Info_layout = QVBoxLayout(self.Info_widget)
        self.Info_layout.setSpacing(8)
        self.Info_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Title Info
        self.Title_widget = QLabel()
        self.Title_widget.setMinimumHeight(21)
        self.Title_widget.setAlignment(Qt.AlignCenter)
        self.Title_widget.setStyleSheet('background: white')
        self.Title_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Info_layout.addWidget(self.Title_widget)

        # Duration Info
        self.Duration_widget = QLabel()
        self.Duration_widget.setMinimumHeight(21)
        self.Duration_widget.setAlignment(Qt.AlignCenter)
        self.Duration_widget.setStyleSheet('background: white')
        self.Duration_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Info_layout.addWidget(self.Duration_widget)

        self.Video_layout.addWidget(self.Info_widget)

        self.Center_Widget_layout.addWidget(self.Video_widget)

    def file_type(self):
        # Parent Widget File Type
        self.File_type_widget = QWidget()
        self.File_type_layout = QVBoxLayout(self.File_type_widget)
        self.File_type_layout.setAlignment(Qt.AlignCenter)
        self.File_type_layout.setContentsMargins(0, 0, 0, 0)
        self.File_type_layout.setSpacing(0)

        # Type Label
        self.Label_Type_widget = QWidget()
        self.Label_Type_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.File_type_layout.addWidget(self.Label_Type_widget)

        # Type Option
        self.Option_Type_widget = QWidget()
        self.Option_Type_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.File_type_layout.addWidget(self.Option_Type_widget)

        self.Center_Widget_layout.addWidget(self.File_type_widget)

    def file_location(self):
        # File Location Parent Widget
        self.File_location_widget = QWidget()
        self.File_location_layout = QVBoxLayout(self.File_location_widget)
        self.File_location_layout.setAlignment(Qt.AlignCenter)
        self.File_location_layout.setContentsMargins(0, 0, 0, 0)
        self.File_location_layout.setSpacing(0)

        # File Location Label
        self.Label_file_location = QWidget()
        self.Label_file_location.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.File_location_layout.addWidget(self.Label_file_location)

        # File Widget
        self.File_widget = QWidget()
        self.File_layout = QHBoxLayout(self.File_widget)
        self.File_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Widget Directory
        self.Directory_widget = QWidget()
        self.Directory_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.File_layout.addWidget(self.Directory_widget)

        # Widget Button
        self.Button_browse_widget = QWidget()
        self.Button_browse_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.File_layout.addWidget(self.Button_browse_widget)

        self.File_location_layout.addWidget(self.File_widget)

        self.Center_Widget_layout.addWidget(self.File_location_widget)

    def button_download(self):
        # Download Button
        self.Button_download = QPushButton()
        self.Button_download.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.Center_Widget_layout.addWidget(self.Button_download)

    def search_video(self):
        # Obtenha a URL inserida no QTextEdit
        url = self.Url_link_widget.toPlainText().strip()

        try:
            # Instancie a classe YouTube para obter informações do vídeo
            yt = YouTube(url)

            # Obtendo informações do vídeo
            video_thumbnail_url = yt.thumbnail_url
            video_title = yt.title
            video_duration = yt.length

            # Carregando a miniatura usando QPixmap
            thumbnail_data = QImage()
            thumbnail_data.loadFromData(requests.get(video_thumbnail_url).content)
            thumbnail_pixmap = QPixmap.fromImage(thumbnail_data)

            # Redimensionar a miniatura para o tamanho do QLabel (240x135)
            thumbnail_pixmap = thumbnail_pixmap.scaled(240, 135, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Exibir a miniatura na QLabel
            self.Thumbnail_widget.setPixmap(thumbnail_pixmap)

            # Atualizar os widgets com as informações do vídeo
            self.Title_widget.setText(f"Title: {video_title}")
            self.Duration_widget.setText(f"Duration: {video_duration} seconds")
            self.Thumbnail_widget.setStyleSheet('background: #D9D9D9')

        except Exception as e:
            # Caso ocorra algum erro ao buscar as informações do vídeo
            print("Erro ao buscar informações do vídeo:", str(e))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
