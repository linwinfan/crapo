# -*- coding: utf-8 -*-
# ©2018 Article 714
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class CrapoConfigSettings(models.TransientModel):
    """
    Crapo configuration
    """
    _name = 'crapo.config.settings'
    _inherit = 'res.config.settings'