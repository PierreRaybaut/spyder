# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""Variable Explorer Plugin Configuration Page."""

# Third party imports
from qtpy.QtWidgets import QGroupBox, QVBoxLayout
from spyder_kernels.utils.misc import is_module_installed

# Local imports
from spyder.config.base import _
from spyder.api.preferences import PluginConfigPage

class VariableExplorerConfigPage(PluginConfigPage):

    def setup_page(self):
        # Filter Group
        filter_group = QGroupBox(_("Filter"))
        filter_data = [
            ('exclude_private', _("Exclude private references")),
            ('exclude_capitalized', _("Exclude capitalized references")),
            ('exclude_uppercase', _("Exclude all-uppercase references")),
            ('exclude_unsupported', _("Exclude unsupported data types")),
            ('exclude_callables_and_modules',
             _("Exclude callables and modules"))
        ]
        filter_boxes = [self.create_checkbox(text, option)
                        for option, text in filter_data]
        filter_layout = QVBoxLayout()
        for box in filter_boxes:
            filter_layout.addWidget(box)
        filter_group.setLayout(filter_layout)

        # Display Group
        display_group = QGroupBox(_("Display"))
        display_data = [("minmax", _("Show arrays min/max"), "")]
        display_boxes = [
            self.create_checkbox(text, option, tip=tip)
            for option, text, tip in display_data
        ]
        display_layout = QVBoxLayout()
        for box in display_boxes:
            display_layout.addWidget(box)
        plotlibs = [
            (libname, libname)
            for libname in ("matplotlib", "guiqwt")
            if is_module_installed(libname)
        ]
        if plotlibs:
            plotlib_box = self.create_combobox(
                _("Plotting library:") + "   ",
                plotlibs,
                "plotlib",
                default="matplotlib",
                tip=_(
                    "Default library used to plot data from NumPy arrays (curve, histogram, image)"
                ),
            )
            display_layout.addWidget(plotlib_box)
        display_group.setLayout(display_layout)

        vlayout = QVBoxLayout()
        vlayout.addWidget(filter_group)
        vlayout.addWidget(display_group)
        vlayout.addStretch(1)
        self.setLayout(vlayout)
