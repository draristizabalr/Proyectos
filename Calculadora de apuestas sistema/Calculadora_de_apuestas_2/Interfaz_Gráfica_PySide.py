import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QLineEdit, QSpinBox, QHBoxLayout, \
    QStackedLayout, QPushButton


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        # Título de la ventana
        self.setWindowTitle('Calculadora Apuestas Sistema')
        self.setFixedSize(600, 400)

        # Método de creación de componentes
        self._crear_componentes_iniciales()

    def _crear_componentes_iniciales(self):
        # Creamos la barra de menú superior
        menu = self.menuBar()
        # Creamos la primera opción de la barra de menú
        menu_archivo = menu.addMenu('Archivo')
        # Creamos las acciones del menú "Archivo"
        accion_abrir = QAction('Abrir', self)
        accion_guardar = QAction('Guardar', self)
        accion_guardar_como = QAction('Guardar como ...', self)
        accion_salir = QAction('Salir', self)
        # Agregamos los slots a las acciones del menú "Archivo"
        accion_abrir.triggered.connect(self._abrir)
        accion_guardar.triggered.connect(self._guardar)
        accion_guardar_como.triggered.connect(self._guardar_como)
        accion_salir.triggered.connect(self._salir)
        # Agregamos las acciones del menu "Archivo"
        menu_archivo.addActions([accion_abrir, accion_guardar, accion_guardar_como])
        menu_archivo.addSeparator()
        menu_archivo.addAction(accion_salir)
        # Agregamos un mensaje a la barra de estado de la ventana
        accion_abrir.setStatusTip('Se abrirá un proceso que esté en construcción ...')
        accion_guardar.setStatusTip('Guardar la información para terminar en un futuro ...')
        accion_guardar_como.setStatusTip('Guardar la información para terminar en un futuro ...')
        accion_salir.setStatusTip('Salir del programa')
        # Agregamos un mensaje a la barra de estado de la ventana
        self.statusBar().showMessage('Detalles ...')

        # Creamos el layout vertical, que en este caso es el principal
        layout_principal = QVBoxLayout()
        # Después creamos los layouts hijos
        layout_numero_cuotas = QHBoxLayout()
        layout_detalle_apuestas = QVBoxLayout()

        # Agregamos los layouts al layout principal
        layout_principal.addLayout(layout_numero_cuotas)
        layout_principal.addLayout(layout_detalle_apuestas)

        # Etiqueta "Número de Cuotas"
        etiqueta_numero_cuotas = QLabel('Numero de cuotas:')
        # SpinBox "Número de cuotas"
        self.numero_cuotas = QSpinBox()
        self.numero_cuotas.setRange(1, 12)
        # Botón para crear los componentes del próximo layout
        boton_numero_cuotas = QPushButton('Continuar')
        boton_numero_cuotas.setFixedSize(100, 30)
        boton_numero_cuotas.pos()
        boton_numero_cuotas.pressed.connect(lambda: self._crear_layout_detalle_cuotas(self.numero_cuotas.text()))
        # Agregamos los componentes de número de cuotas al layout respectivo
        layout_numero_cuotas.addWidget(etiqueta_numero_cuotas)
        layout_numero_cuotas.addWidget(self.numero_cuotas)
        layout_principal.addWidget(boton_numero_cuotas)

        # Contenedor para publicar el layout
        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        # Publicamos el contenedor
        self.setCentralWidget(contenedor)

    def _abrir(self):
        print('Signal "Abrir"')

    def _guardar(self):
        print('Signal "Guardar"')

    def _guardar_como(self):
        print('Signal "Guardar como ..."')

    def _salir(self):
        print('Signal "Salir"')
        self.close()
        sys.exit()

    def _crear_layout_detalle_cuotas(self, numero_cuotas):
        # Creamos una función generadora de componentes
        for indice in range(int(numero_cuotas)):
            etiqueta_apuesta = QLabel(f'Apuesta {indice}')
            nombre_apuesta = QLineEdit()
            cuota_apuesta = QLineEdit()


        # Publicamos el contenedor
        self.setCentralWidget(etiqueta_numero_apuestas)











if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()
