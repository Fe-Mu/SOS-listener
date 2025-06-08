
"""

SoS-Listener is a multiplatform capable tool writen in Python/Kivy
language and developed by L.F.G. Muñoz ("the Author") that offers
the potential for SOS request in emergency situations.

Copyright  (C)  2025  L.F.G. Muñoz  lfgm.copyright@protonmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""


title = """

[u][b]Troubleshooting[/u][/b]
"""

txt_troubleshooting = """
[b]GPS coordinates not being displayed[/b]

    1. Make sure/check that the App was granted Location access during the Apps's first start. One possible way to check this is by pressing and keeping pressed the App icon until a small window with the text “App info” appears. Tap into this small window and choose the “Permissions” menu of the next window. You should be able to individually allow/disallow permissions for this App. This App requires the Location, Phone and SMS permissions in order for it to work properly.
    2. Check that your GPS is ON while using the App. This can be achieved by toggling ON the Location switch in the phone Settings or by tapping the Location icon on your phone.


[b]GPS coordinates are not accurate[/b]

    1. The accuracy of your position can vary depending on whether your device is using a precision or an approximate locating method. In some devices the end-user can choose one of these two methods but in other devices the end-user will not be able to choose between a precision or an approximate locating method.
    2. The accuracy between devices might also vary due to the fact that some GPS are more accurate than others.
    3. Turning on the wifi antenna might help, but not necessarily, with delivering a more accurate position. Keep in mind that turning ON the wifi antenna will also increase the energy consumption.


[b]SOS message not arriving[/b]

    1. There are many reasons why an SMS message cannot be delivered as desired. Sending an SOS message (since they are also SMS messages) at least twice could help to increase the chances that the message gets correctly delivered to the recipient.

"""
