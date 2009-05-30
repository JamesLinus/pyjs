# Copyright (C) 2006-2009 Google, Inc.
# Copyright (C) 2009 Laszlo Krekacs
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from pyjamas.ui.CustomButton import CustomButton

class PushButton (CustomButton):
    """
    A normal push button with custom styling.

    CSS: .gwt-PushButton-
    up/down/up-hovering/down-hovering/up-disabled/down-disabled {.html-face}
    """    
    STYLENAME_DEFAULT = "gwt-PushButton"
    
    def __init__(self, upImageText = None, downImageText=None, handler = None):
        """
        Constructor for PushButton.
        """
        CustomButton.__init__(self, upImageText, downImageText, handler)
        self.setStyleName(self.STYLENAME_DEFAULT)
    
    
    def onClick(self, sender=None):
        self.setDown(False)
        CustomButton.onClick(self)
    

    def onClickCancel(self):
        self.setDown(False)

    
    def onClickStart(self):
        self.setDown(True)
    

