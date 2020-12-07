#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Synth
# Author: Robert Warner
# Description: Synth Project for Music Technology
# Generated: Mon Dec  7 11:17:33 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class synth(gr.top_block, Qt.QWidget):
    def __init__(self):
        gr.top_block.__init__(self, "Synth")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Synth")
        qtgui.util.check_set_qss()

        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "synth")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(
                self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.waveform_radio_buttons = waveform_radio_buttons = 0
        self.samp_rate = samp_rate = 32000
        self.g_button = g_button = 0
        self.f_button = f_button = 0
        self.e_button = e_button = 0
        self.d_button = d_button = 0
        self.c_button = c_button = 0
        self.c1_button = c1_button = 0
        self.b_button = b_button = 0
        self.a_button = a_button = 0

        ##################################################
        # Blocks
        ##################################################
        self.signal_src = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE,
                                              0.0, 1, 0)

        self._waveform_radio_buttons_options = (
            0,
            1,
            2,
        )
        self._waveform_radio_buttons_labels = (
            'Sine Wave',
            'Triangle Wave',
            'Square Wave',
        )
        self._waveform_radio_buttons_group_box = Qt.QGroupBox(
            "Waveform Radio Buttons")
        self._waveform_radio_buttons_box = Qt.QVBoxLayout()

        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)

            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)

        self._waveform_radio_buttons_button_group = variable_chooser_button_group(
        )
        self._waveform_radio_buttons_group_box.setLayout(
            self._waveform_radio_buttons_box)
        for i, label in enumerate(self._waveform_radio_buttons_labels):
            radio_button = Qt.QRadioButton(label)
            self._waveform_radio_buttons_box.addWidget(radio_button)
            self._waveform_radio_buttons_button_group.addButton(
                radio_button, i)
        self._waveform_radio_buttons_callback = lambda i: Qt.QMetaObject.invokeMethod(
            self._waveform_radio_buttons_button_group, "updateButtonChecked",
            Qt.Q_ARG("int", self._waveform_radio_buttons_options.index(i)))
        self._waveform_radio_buttons_callback(self.waveform_radio_buttons)
        self._waveform_radio_buttons_button_group.buttonClicked[int].connect(
            lambda i: self.set_waveform_radio_buttons(
                self._waveform_radio_buttons_options[i]))
        self.top_layout.addWidget(self._waveform_radio_buttons_group_box)
        self.time_sink = qtgui.time_sink_f(
            1024,  #size
            samp_rate,  #samp_rate
            "",  #name
            1  #number of inputs
        )
        self.time_sink.set_update_time(0.05)
        self.time_sink.set_y_axis(-1, 1)

        self.time_sink.set_y_label('Amplitude', "")

        self.time_sink.enable_tags(-1, True)
        self.time_sink.set_trigger_mode(qtgui.TRIG_MODE_FREE,
                                        qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.time_sink.enable_autoscale(False)
        self.time_sink.enable_grid(False)
        self.time_sink.enable_axis_labels(True)
        self.time_sink.enable_control_panel(False)
        self.time_sink.enable_stem_plot(False)

        if not True:
            self.time_sink.disable_legend()

        labels = ['', '', '', '', '', '', '', '', '', '']
        widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        colors = [
            "blue", "red", "green", "black", "cyan", "magenta", "yellow",
            "dark red", "dark green", "blue"
        ]
        styles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.time_sink.set_line_label(i, "Data {0}".format(i))
            else:
                self.time_sink.set_line_label(i, labels[i])
            self.time_sink.set_line_width(i, widths[i])
            self.time_sink.set_line_color(i, colors[i])
            self.time_sink.set_line_style(i, styles[i])
            self.time_sink.set_line_marker(i, markers[i])
            self.time_sink.set_line_alpha(i, alphas[i])

        self._time_sink_win = sip.wrapinstance(self.time_sink.pyqwidget(),
                                               Qt.QWidget)
        self.top_layout.addWidget(self._time_sink_win)

        self.audio_sink = audio.sink(samp_rate, '', True)

        # add high c
        _c1_button_push_button = Qt.QPushButton("C'")
        self._c1_button_choices = {'Pressed': 523.2511, 'Released': 0}
        _c1_button_push_button.pressed.connect(
            lambda: self.set_c1_button(self._c1_button_choices['Pressed']))
        _c1_button_push_button.released.connect(
            lambda: self.set_c1_button(self._c1_button_choices['Released']))
        self.top_layout.addWidget(_c1_button_push_button)

        # add b button
        _b_button_push_button = Qt.QPushButton('B')
        self._b_button_choices = {'Pressed': 493.8833, 'Released': 0}
        _b_button_push_button.pressed.connect(
            lambda: self.set_b_button(self._b_button_choices['Pressed']))
        _b_button_push_button.released.connect(
            lambda: self.set_b_button(self._b_button_choices['Released']))
        self.top_layout.addWidget(_b_button_push_button)

        # add a button
        _a_button_push_button = Qt.QPushButton('A')
        self._a_button_choices = {'Pressed': 440.0000, 'Released': 0}
        _a_button_push_button.pressed.connect(
            lambda: self.set_a_button(self._a_button_choices['Pressed']))
        _a_button_push_button.released.connect(
            lambda: self.set_a_button(self._a_button_choices['Released']))
        self.top_layout.addWidget(_a_button_push_button)

        # add g button
        _g_button_push_button = Qt.QPushButton('G')
        self._g_button_choices = {'Pressed': 391.9954, 'Released': 0}
        _g_button_push_button.pressed.connect(
            lambda: self.set_g_button(self._g_button_choices['Pressed']))
        _g_button_push_button.released.connect(
            lambda: self.set_g_button(self._g_button_choices['Released']))
        self.top_layout.addWidget(_g_button_push_button)

        # add f button
        _f_button_push_button = Qt.QPushButton('F')
        self._f_button_choices = {'Pressed': 349.2282, 'Released': 0}
        _f_button_push_button.pressed.connect(
            lambda: self.set_f_button(self._f_button_choices['Pressed']))
        _f_button_push_button.released.connect(
            lambda: self.set_f_button(self._f_button_choices['Released']))
        self.top_layout.addWidget(_f_button_push_button)

        #add e button
        _e_button_push_button = Qt.QPushButton('E')
        self._e_button_choices = {'Pressed': 329.6276, 'Released': 0}
        _e_button_push_button.pressed.connect(
            lambda: self.set_e_button(self._e_button_choices['Pressed']))
        _e_button_push_button.released.connect(
            lambda: self.set_e_button(self._e_button_choices['Released']))
        self.top_layout.addWidget(_e_button_push_button)

        # add d button
        _d_button_push_button = Qt.QPushButton('D')
        self._d_button_choices = {'Pressed': 293.6648, 'Released': 0}
        _d_button_push_button.pressed.connect(
            lambda: self.set_d_button(self._d_button_choices['Pressed']))
        _d_button_push_button.released.connect(
            lambda: self.set_d_button(self._d_button_choices['Released']))
        self.top_layout.addWidget(_d_button_push_button)

        # add c1
        _c_button_push_button = Qt.QPushButton('C')
        self._c_button_choices = {'Pressed': 261.6256, 'Released': 0}
        _c_button_push_button.pressed.connect(
            lambda: self.set_c_button(self._c_button_choices['Pressed']))
        _c_button_push_button.released.connect(
            lambda: self.set_c_button(self._c_button_choices['Released']))
        self.top_layout.addWidget(_c_button_push_button)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.signal_src, 0), (self.audio_sink, 0))
        self.connect((self.signal_src, 0), (self.time_sink, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "synth")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_waveform_radio_buttons(self):
        return self.waveform_radio_buttons

    def set_waveform_radio_buttons(self, waveform_radio_buttons):
        self.waveform_radio_buttons = waveform_radio_buttons
        self._waveform_radio_buttons_callback(self.waveform_radio_buttons)
        if waveform_radio_buttons == 0:
            self.signal_src.set_waveform(analog.GR_COS_WAVE)
        elif waveform_radio_buttons == 1:
            self.signal_src.set_waveform(analog.GR_TRI_WAVE)
        elif waveform_radio_buttons == 2:
            self.signal_src.set_waveform(analog.GR_SQR_WAVE)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.time_sink.set_samp_rate(self.samp_rate)
        self.signal_src.set_sampling_freq(self.samp_rate)

    def get_g_button(self):
        return self.g_button

    def set_g_button(self, g_button):
        self.signal_src.set_frequency(g_button)
        self.g_button = g_button

    def get_f_button(self):
        return self.f_button

    def set_f_button(self, f_button):
        self.signal_src.set_frequency(f_button)
        self.f_button = f_button

    def get_e_button(self):
        return self.e_button

    def set_e_button(self, e_button):
        self.signal_src.set_frequency(e_button)
        self.e_button = e_button

    def get_d_button(self):
        return self.d_button

    def set_d_button(self, d_button):
        self.signal_src.set_frequency(d_button)
        self.d_button = d_button

    def get_c_button(self):
        return self.c_button

    def set_c_button(self, c_button):
        self.signal_src.set_frequency(c_button)
        self.c_button = c_button

    def get_c1_button(self):
        return self.c1_button

    def set_c1_button(self, c1_button):
        self.signal_src.set_frequency(c1_button)
        self.c1_button = c1_button

    def get_b_button(self):
        return self.b_button

    def set_b_button(self, b_button):
        self.signal_src.set_frequency(b_button)
        self.b_button = b_button

    def get_a_button(self):
        return self.a_button

    def set_a_button(self, a_button):
        self.signal_src.set_frequency(a_button)
        self.a_button = a_button


def main(top_block_cls=synth, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(
            Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
