from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model, view):
        super().__init__()

        self._model = model
        self._view = view

        # connect widgets to controller
        self._view.ui.spinBox_amount.valueChanged.connect(self.change_amount)
        self._view.ui.pushButton_reset.clicked.connect(lambda: self.change_amount(0))

        # listen for model event signals
        self._model.amount_changed.connect(self.on_amount_changed)
        self._model.even_odd_changed.connect(self.on_even_odd_changed)
        self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

    @pyqtSlot(int)
    def change_amount(self, value):
        self._model.amount = value

        # calculate even or odd
        self._model.even_odd = 'odd' if value % 2 else 'even'

        # calculate button enabled state
        self._model.enable_reset = True if value else False

    @pyqtSlot(int)
    def on_amount_changed(self, value):
        self._view.ui.spinBox_amount.setValue(value)

    @pyqtSlot(str)
    def on_even_odd_changed(self, value):
        self._view.ui.label_even_odd.setText(value)

    @pyqtSlot(bool)
    def on_enable_reset_changed(self, value):
        self._view.ui.pushButton_reset.setEnabled(value)
