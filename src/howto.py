"""

SOS-listener is a multiplatform capable tool writen in Python/Kivy
language and developed by L.F.G. Muñoz ("the Author") that offers
the potential for SOS request in emergency situations.

Copyright  (C)  2025  L.F.G. Muñoz  sos.contact@protonmail.com

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

[u][b]How-To[/u][/b]
"""

txt_how_to_1 = """
[b]Activate/Deactivate the light-theme[/b]

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. When the new popup screen opens, toggle the light-theme switch at the top of the window to the desired ON/OFF state.
    3. The new theme will be automatically applied and displayed on the main screen.


[b]Save a new contact[/b]

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. Write a name for your new contact in the corresponding text field.
    3. Write the country’s code number in the corresponding text field.
    4. Write the new contact’s phone number in the corresponding text field.
    5. Tap on the color wheel to choose the display color that will be assigned to your contact.
    6. Press the "Save" button.


[b]Update an existing contact[/b]

[u]To change the name of a contact you have to delete the existing contact and create a new one[/u]

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. Write the name of the existing contact in the corresponding text field. The name has to be written exactly as is displayed in the contact button.
    3. Update the information in the desired fields:
        - Write the updated country’s code number in the corresponding text field.
        - Write the contact’s phone Number in the corresponding text field.
        - Tap on the color wheel to choose the display color that will be assigned to your contact.
    4. Press the "Update" button.


[b]Delete an existing contact[/b]

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. Write the name of the existing contact in the corresponding text field. The name needs to be written exactly as displayed in the contact button.
    3. Press the "Delete" button.


[b]Call Emergency-Contact[/b]

    1. Tap on the emergency-contact button
    2. Tap on the "Call" button in the new popup window
    3. A call to the chosen emergency-contact will be made


[b]Send SOS-Message[/b]

    1. Tap on the emergency-contact button
    2. Tap on the "Send-SOS" button in the new popup window
    3. An SOS with the following message will be sent:
    
    ++ Emergency-SOS ++
    I need help! , please CALL BACK! , if I dont answer please send help to my location!


[b]Send Silent-SOS-Message[/b]

    1. Tap on the emergency-contact button
    2. Tap on the "Silent-SOS" button in the new popup window
    3. A Silent-SOS with the following message will be sent:
    
    ++ Silent Emergency-SOS ++
    I need help! , please DO NOT CALL BACK! , please send help to my location!
"""

txt_how_to_2 = """
[b]Location Messages[/b]

Sending a SOS-Message will also share the current Location of the person requesting the help in the form of a link that can be opened either on the Magic Earth App or on the Google Maps App. These apps need to be previously installed in order for the links to be able to be opened there.

    1. Magic Earth is the recommended App to open shared Location coordinates due to its privacy-oriented nature which aligns with SOS-listener's commitment to respect the end-user's privacy. Additionally Magic Earth offers the possibility to download (at no cost) offline maps for entire and multiple countries across the world if desired. This allows the sender and the receiver to share and pinpoint any Location coordinates in an offline map when no internet connectivity is available (as long as the region was previously downloaded in Magic Earth).
    2. Google Maps was chosen as the second App to open shared Location coordinates due to its popularity and wide adoption across multiple devices and countries. 

Disclaimer: The developer of this App has no affiliation or relationship with Magic Earth or Google.


[b]Activate the Quick-Call Emergency-Buttons[/b]

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police, Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To activate one or more of these buttons do the following:

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. When the new popup window opens, write a new emergency number in one of the text fields next to the label -- Emergency Nr. 1, 2 or 3-- and toggle the switch next to it to the ON state.
    3. The color of the -- Emergency Nr. -- label will match, as a result, the color of the button that later will be displayed in the main screen.
    4. Click on the "Update" button at the bottom of the screen.
    5. The activated button will be available for its use at the top of the main screen in the chosen color.


[b]Change the Quick-Call Emergency-Number[/b]

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police, Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To change/delete one or more of these emergency numbers do the following:

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. When the new popup window opens, write a new emergency number (or a non-callable number e.g. "---") in one of the text fields next to the label -- Emergency Nr. 1, 2 or 3--.
    3. Click on the "Update" button at the bottom of the screen.
    4. The changed emergency number button will be displayed in the button at the top of the main screen.


[b]Deactivate the Quick-Call Emergency-Buttons[/b]

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police or Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To deactivate one or more of these buttons do the following:

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. When the new popup window opens, toggle the switch next to it to the OFF state.
    3. Click on the "Update" button at the bottom of the screen.
    4. The deactivated button will be displayed at the top of the main screen in grey color.


[b]Backup emergency-contacts[/b]

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. Tap on the "Backup" button.
    3. A backup of your emergency-contacts will be automatically generated in the system's /Documents/SOS-listener directory.
    4. A small confirmation popup window will appear.
    5. Tap anywhere outside the popup window to close it.


[b]Restore emergency-contacts[/b]

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. Tap on the "Restore" button of the popup window.
    3. Search for the backup file inside the system's /Documents/SOS-listener directory.
    4. Select and confirm the file selection.
    5. A small confirmation popup window will appear.
    6. Tap anywhere outside the popup window to close it.
    7. Close and restart the App to automatically load the imported emergency-contacts.

IMPORTANT: For security reasons it is recommended that you delete the backup or that you save it in a secure place (not in your phone) after restoring the emergency-contacts.


[b]Check which version of the App is installed[/b]

Option 1:
    
    1. Check the app version displayed on the top on the main screen
    
Option 2:
    
    1. Go to Settings
    2. Go to Apps
    3. Depending on your phone interface tap on "App manager" or "See all apps".
    4. Tap on your App's name
    5. You will be taken to the App's information window where you should be able to find the version that is currently installed on your device.
    6. Check if the App version that is installed on your device is the same version found on [u]https://github.com/Fe-Mu/SOS-listener/releases[/u]
    7. Manually update the App on your device if the two App versions are not the same
    
Option 3:
        
    1. Touch and hold down the App icon in your phone for a short moment.
    2. A small menu will appear will a few options.
    3. Tap on "App info" or on the circle with a letter "i".
    4. You will be taken to the App's information window where you should be able to find the version that is currently installed on your device.
    5. Check if the App version that is installed on your device is the same version found on [u]https://github.com/Fe-Mu/SOS-listener/releases[/u]
    6. Manually update the App on your device if the two App versions are not the same
   
IMPORTANT: It is highly recommended to always update and run the latest version of the App.


[b]Manually Update App[/b]

[u]Before a manual App update make sure you make first a backup of your emergency-contacts (see above), since manually updating the App will delete the existing emergency-contacts.[/u]

At the end of the following steps you should end up with a single and updated App installation. The update should NEVER create a duplicate of the App. If you notice a duplicate was created after the update it could mean it is not the original APK published by the developer. Uninstall the App duplicate, delete the recently downloaded APK and please inform the developer about this.

To update the App:

    1. Close the App if the App is running
    2. Go to [u]https://github.com/Fe-Mu/SOS-listener/releases[/u] and download the newest/latest App release from the official GitHub Repository.
    3. Go to the location where the APK was downloaded (usually the Downloads folder).
    4. Tap on the downloaded APK and click on install and proceed with the installation steps that will follow. If during the installation you receive a message that there is a problem with the Signature it could mean that the App was tampered by someone else and therefore the Signatures of the original APK and the new APK do not match. In such case Android should prevent the installation since this is a security issue. In such case do not install the new APK and please inform the developer about this.
    5. If everything went well the App should now have the latest updates.


[b]Activate/Deactivate the light-theme[/b]

    1. Tap on the "Add/Manage Buttons" button in the main screen.
    2. When the new popup screen opens, toggle the light-theme switch at the top of the window to the desired ON/OFF state.
    3. The new theme will be automatically applied and displayed on the main screen.

"""