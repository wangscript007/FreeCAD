# -*- coding: utf-8 -*-

# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2017 sliptonic <shopinthewoods@gmail.com>               *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

import FreeCAD
import PathScripts.PathOpGui as PathOpGui
import PathScripts.PathProfileBaseGui as PathProfileBaseGui
import PathScripts.PathProfileEdges as PathProfileEdges

from PySide import QtCore

__title__ = "Path Profile based on edges Operation UI"
__author__ = "sliptonic (Brad Collette)"
__url__ = "http://www.freecadweb.org"
__doc__ = "Profile based on edges operation page controller and command implementation."

class TaskPanelOpPage(PathProfileBaseGui.TaskPanelOpPage):
    '''Page controller for profile based on edges operation.'''

    def profileFeatures(self):
        '''profileFeatures() ... return FeatureSide
        See PathProfileBaseGui.py for details.'''
        return PathProfileBaseGui.FeatureSide

Command = PathOpGui.SetupOperation('Profile Edges',
        PathProfileEdges.Create,
        TaskPanelOpPage,
        'Path-Profile-Edges',
        QtCore.QT_TRANSLATE_NOOP("PathProfile", "Edge Profile"),
        QtCore.QT_TRANSLATE_NOOP("PathProfile", "Profile based on edges"),
        PathProfileEdges.SetupProperties)

FreeCAD.Console.PrintLog("Loading PathProfileEdgesGui... done\n")
