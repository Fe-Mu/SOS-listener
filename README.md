
# SOS-listener <img align="right" src="res/logo.png" height="150" width="150" alt="SOS Listener Logo"/>

A simple, easy-to-use, tool/App to request help during emergency situations.

## Disclaimer

1. This is not a professional App and it does not provide or promise to deliver any professional service.
2. This App is not guaranteed at any moment to function as intended. There are too many potential reasons, from hardware to software, why this App could fail to perform as intended, and therefore it can not be considered as a reliable source of help in an emergency situation. No end-user should rely solely on this App to provide or request aid, rescue or help in any given case or situation.
3. This App comes with no warranty of any kind. The use of this App is at the end-user's own risk.
4. This is not an App intended to be used as a phone contact book. This App was developed to be a potential source of help in case of an emergency. Use this App as intended, otherwise it could and might increase the probability of undesired results to happen.
5. SOS-listener will never require you to make any payment or ask you to enter your own private information, passwords, bank account or anything similar. In case of such events please report it to the Developer as soon as possible.

## Introduction

SOS-listener is a multiplatform capable tool writen in Python/Kivy language and developed by L.F.G. Muñoz ("the Author") that offers the potential for SOS request in emergency situations.

This App is not targeted at children, but it was designed on purpose with simplicity in mind so that it could easily be used by anyone during an emergency situation. 
This App has been given features that the Author consider essential, without overloading it with features that could end up overwhelming the user (e.g. children) in difficult scenarios. 
Quick access to essential features and a clean interface were prioritized instead of many features and complicated menus.

This App does not aim to be the most feature rich of its kind (since that would defeat the purpose of its simplicity). 
This App focuses on being **Simple, Intuitive, Easy to use, Essential and Private**. 

>IMPORTANT: For security reasons it is very important that your emergency-contacts have also you saved in their contacts so that, in case of an emergency, they will be able to clearly identify which person is calling them or sending them an SOS-message.

## Code of Conduct

To the End-User of this App, please:

- Do not facilitate (or help to facilitate) this App or any of its parts to any other person, entity, organization, association, partnership or anything equivalent for its use in any illegal or unethical activities and/or any activities that could harm or impact negatively anyone or anything.
- Do not use, directly or indirectly, this App to create a false identity to mislead another person, entity, organization, association, partnership or anything equivalent in any possible way, no matter the intention or the situation.
- Do not use, directly or indirectly, this App to steal, collect or process private information from another person, entity, organization, association, partnership or anything equivalent in any possible way, no matter the intention or the situation.
- Do not violate the privacy of other end-users and to please behave in a responsible manner and according to the law.
- Do not share the information of anyone else other that your own with other person, entity, organization, association, partnership or anything equivalent, no one else.

<ins>Always respect other people's privacy</ins>.

## Features

- _GPS coordinates display_<br/><br/>
- _Save Emergency-Contacts_<br/><br/>
- _Update Emergency-Contacts_<br/><br/>
- _Delete Emergency-Contacts_<br/><br/>
- _Call Emergency-Contacts_<br/><br/>
- _Send GPS position along with SOS-Messages_<br/><br/>
- _Send SOS-Messages_<br/>
    - To let an emergency-contact know your location and that they should call you back whenever they can and get help as soon as possible.<br/><br/>
- _Send Silent-SOS-Messages_<br/>
    - To let an emergency-contact know your location and let them know they should not attempt to call you back but get help as soon as possible.<br/><br/>
- _Ability to activate up to three Quick-Call Emergency-Buttons_<br/>
    - To contact without delay any of your local authorities/emergency-institutions<br/><br/>
- _Backup emergency-contacts_<br/><br/>
- _Restore emergency-contacts_<br/><br/>
- _Ability to change between light and dark themes_

## Save a new contact

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. Write a name for your new contact in the corresponding text field.
3. Write the country’s code number in the corresponding text field.
4. Write the new contact’s phone number in the corresponding text field.
5. Tap on the color wheel to choose the display color that will be assigned to your contact.
6. Press the "Save" button.

## Update an existing contact

<ins>To change the name of a contact you have to delete the existing contact and create a new one</ins>

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. Write the name of the existing contact in the corresponding text field. The name has to be written exactly as is displayed in the contact button.
3. Update the information in the desired fields:
    - Write the updated country’s code number in the corresponding text field.
    - Write the contact’s phone Number in the corresponding text field.
    - Tap on the color wheel to choose the display color that will be assigned to your contact.
4. Press the "Update" button.

## Delete an existing contact

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. Write the name of the existing contact in the corresponding text field. The name needs to be written exactly as displayed in the contact button.
3. Press the "Delete" button.

## Call Emergency-Contact

1. Tap on the emergency-contact button
2. Tap on the "Call" button in the new popup window
3. A call to the chosen emergency-contact will be made

## Send SOS-Message

1. Tap on the emergency-contact button
2. Tap on the "Send-SOS" button in the new popup window
3. An SOS with the following message will be sent:
> ++ Emergency-SOS ++<br/> 
> I need help! , please CALL BACK! , if I do not answer please send help to my location!

## Send Silent-SOS-Message

1. Tap on the emergency-contact button
2. Tap on the "Silent-SOS" button in the new popup window
3. A Silent-SOS with the following message will be sent:
> ++ Silent Emergency-SOS ++<br/>
> I need help! , please DO NOT CALL BACK! , please send help to my location!

## Location Messages

Sending a SOS-Message will also share the current Location of the person requesting the help in the form of a link that can be opened either on the Magic Earth App or on the Google Maps App. These apps need to be previously installed in order for the links to be able to be opened there.

1. Magic Earth is the recommended App to open shared Location coordinates due to its privacy-oriented nature which aligns with SOS-listener's commitment to respect the End-User's privacy. Additionally Magic Earth offers the possibility to download (at no cost) offline maps for entire and multiple countries across the world if desired. This allows the sender and the receiver to share and pinpoint any Location coordinates in an offline map when no internet connectivity is available (as long as the region was previously downloaded in Magic Earth).
2. Google Maps was chosen as the second App to open shared Location coordinates due to its popularity and wide adoption across multiple devices and countries. 

>Disclaimer: The developer or this App has no affiliation or relationship with Magic Earth or Google in any way.

## Activate the Quick-Call Emergency-Buttons

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police, Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To activate one or more of these buttons do the following:

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. When the new popup window opens, write a new emergency number in one of the text fields next to the label "-- Emergency Nr. --" and toggle the switch next to it to the ON state.
3. The color of the "-- Emergency Nr. --" label will match, as a result, the color of the button that later will be displayed in the main screen.
4. Click on the "Update" button at the bottom of the screen.
5. The activated button will be available for its use at the top of the main screen in the chosen color.

## Change the Quick-Call Emergency-Number

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police, Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To change/delete one or more of these emergency numbers do the following:

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. When the new popup window opens, write a new emergency number in one of the text fields next to the label "-- Emergency Nr. --".
3. Click on the "Update" button at the bottom of the screen.
4. The changed emergency number button will be displayed in the button at the top of the main screen.

## Deactivate the Quick-Call Emergency-Buttons

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police or Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To deactivate one or more of these buttons do the following:

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. When the new popup window opens, toggle the switch next to it to the OFF state.
3. Click on the "Update" button at the bottom of the screen.
4. The deactivated button will be displayed at the top of the main screen in grey color.

## Backup emergency-contacts

To perform a backup of your emergence-contacts:

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. Tap on the "Backup" button.
3. A backup of your emergency-contacts will be automatically generated inside the system's /Documents/SOS-listener directory.
4. A small confirmation popup window will appear.
5. Tap anywhere outside the popup window to close it.

## Restore emergency-contacts

To restore your emergence-contacts:

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. Tap on the "Restore" button of the popup window.
3. Search for the backup file inside the system's /Documents/SOS-listener directory.
4. Select and confirm the file selection.
5. A small confirmation popup window will appear.
6. Tap anywhere outside the popup window to close it.
7. Close and Restart the App and the App will automatically load the imported emergency-contacts.

>IMPORTANT: For security reasons it is recommended that you delete the backup or that you save it in a secure place (not in your phone) after restoring the emergency-contacts.

## Check which version of the App is installed

Option 1:
    
1. Go to Settings
2. Go to Apps
3. Depending on your phone interface tap on "App manager" or "See all apps".
4. Tap on your App's name
5. You will be taken to the App's information window where you should be able to find the version that is currently installed on your device.
6. Check that the App version that is installed on your device is the same version found on https://github.com/Fe-Mu/SOS-listener/releases
7. Update the App if versions are not the same
    
Option 2:
    
1. Touch and hold down the App icon in your phone for a short moment.
2. A small menu will appear will a few options.
3. Tap on "App info" or on the circle with a letter "i".
4. You will be taken to the App's information window where you should be able to find the version that is currently installed on your device.
5. Check that the App version that is installed on your device is the same version found on https://github.com/Fe-Mu/SOS-listener/releases
6. Update the App if versions are not the same
   
>It is highly recommended to always update and run the latest version of the App.

## Manually Update App

<ins>Before an App update make sure you make first a backup of your emergency-contacts (see above), since the manually updating the App will delete the existing emergency-contacts.</ins>

At the end of the following steps you should end up with a single and updated App installation. The update should NEVER create a duplicate of the App. If you notice a duplicate was created after the update it could mean it is not the original APK published by the developer. Uninstall the App duplicate, delete the recently downloaded APK and please inform the developer about this.

To update the App:

1. Close the App if the App is running
2. Go to https://github.com/Fe-Mu/SOS-listener/releases and download the newest/latest App release from the official GitHub Repository.
3. Go to the location where the APK was downloaded (usually the Downloads folder).
4. Tap on the downloaded APK and click on install and proceed with the installation steps that will follow. If during the installation you receive a message that there is a problem with the Signature it could mean that the App was tampered by someone else and therefore the Signatures of the original APK and the new APK do not match. In such case Android should prevent the installation since this is a security issue. In such case do not install the new APK and please inform the Developer about this.
5. If everything went well the App should now have the latest updates.

## Activate/Deactivate the light-theme

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. When the new popup screen opens, toggle the light-theme switch at the top of the window to the desired ON/OFF state.
3. The new theme will be automatically applied and displayed on the main screen.

## License

SOS-listener is a multiplatform capable tool writen in Python/Kivy<br/>
language and developed by L.F.G. Muñoz ("the Author") that offers<br/>
the potential for SOS request in emergency situations.

Copyright  (C)  2025  L.F.G. Muñoz  lfgm.copyright@protonmail.com

This program is free software: you can redistribute it and/or modify<br/>
it under the terms of the GNU Affero General Public License as published<br/>
by the Free Software Foundation, either version 3 of the License, or<br/>
(at your option) any later version.

This program is distributed in the hope that it will be useful,<br/>
but WITHOUT ANY WARRANTY; without even the implied warranty of<br/>
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the<br/>
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License<br/>
along with this program.  If not, see <https://www.gnu.org/licenses/>.
