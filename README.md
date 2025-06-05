
# SoS-Listener <img align="right" src="src/logo.png" height="150" width="150" alt="SOS Listener Logo"/>

A simple, easy-to-use, tool/App to request help during emergency situations.

## Disclaimer

1. This is not a professional App and it does not provide or promise to deliver any professional service.
2This App is not guaranteed at any moment to function as intended. There are too many potential reasons, from hardware to software, why this App could fail to perform as intended, and therefore it can not be considered as a reliable source of help in an emergency situation. No end-user should rely solely on this App to provide or request aid, rescue or help in any given case or situation.
3This App comes with no warranty of any kind. The use of this App is at the end-user's own risk.
4This is not an App intended to be used as a phone contact book. This App was developed to be a potential source of help in case of an emergency. Use this App as intended, otherwise it could and might increase the probability of undesired results to happen.

## Introduction

SoS-Listener is a multiplatform capable tool writen in Python/Kivy language and developed by L. F. G. Muñoz ("the Author") that offers the potential for SOS request in emergency situations.

This App is not targeted at children, but it was designed on purpose with simplicity in mind so that it could easily be used by anyone during an emergency situation. 
This App has been given features that the Author consider essential, without overloading it with features that could end up overwhelming the user (e.g. children) in difficult scenarios. 
Quick access to essential features and a clean interface were prioritized instead of many features and complicated menus.

This App does not aim to be the most feature rich of its kind (since that would defeat the purpose of its simplicity). 
This App focuses on being **Simple, Intuitive, Easy to use, Essential and Private**. 

## Code of Conduct

To the End-User of this App, please:

- Not to facilitate (or help to facilitate) this App or any of its parts to any other person, entity, organization, association, partnership or anything equivalent for its use in any illegal or unethical activities and/or any activities that could harm or impact negatively anyone or anything.
- Not to use, directly or indirectly, this App to create a false identity to mislead another person, entity, organization, association, partnership or anything equivalent in any possible way, no matter the intention or the situation.
- Not to use, directly or indirectly, this App to steal, collect or process private information from another person, entity, organization, association, partnership or anything equivalent in any possible way, no matter the intention or the situation.
- Not to violate the privacy of other end-users and to please behave in a responsible manner and according to the law.
- Not to share the information of anyone else other that your own with other person, entity, organization, association, partnership or anything equivalent, no one else.

Always respect other people's privacy.

## Features

- **GPS coordinates display**: To allow the user to know its current location at all times whenever the location services and permissions are activated/granted.
- **Add Emergency Contacts**
- **Update Emergency-Contacts**
- **Delete Emergency-Contacts**
- **Call Emergency-Contacts**
- **Send GPS position along with SOS-Messages**: To let your emergency-contact know your current position.
- **Send SOS-Messages**: To let your emergency-contact know your location and that they should call you back whenever they can and get help as soon as possible.
- **Send Silent-SOS Messages**: To let your emergency-contact know your location and let them know they should not attempt to call you back but get help as soon as possible.
- **Ability to activate up to three Quick-Call Emergency-Buttons**: To contact without delay any of your local authorities/emergency-institutions
- **Ability to change between light and dark themes**

## Save a new contact

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. Write a name for your new contact in the corresponding text field.
3. Write the country’s code number in the corresponding text field.
4. Write the new contact’s phone number in the corresponding text field.
5. Tap on the color wheel to choose the display color that will be assigned to your contact.
6. Press the "Save" button.

## Update an existing contact

To change the name of a contact you have to create a new contact

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
2. Tap on the "Send-SOS" or "Silent-SOS" button in the new popup window
3. An SOS with the following message will be sent:
> --Emergency-SOS--<br/> 
> I need help! , PLEASE CALL BACK! , if I dont answer please send help to my location!

## Send Silent-SOS-Message

1. Tap on the emergency-contact button
2. Tap on the "Send-SOS" or "Silent-SOS" button in the new popup window
3. A Silent-SOS with the following message will be sent:
> --Silent Emergency-SOS--<br/>
> I need help! , DO NOT CALL BACK! , please send help to my location!

## Activate the Quick-Call Emergency-Buttons

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police, Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To activate one or more of these buttons do the following:

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. When the new popup window opens, write a new emergency number in one of the text fields next to the label -- Emergency Nr. 1, 2 or 3-- and toggle the switch next to it to the ON state.
3. The color of the -- Emergency Nr. -- label will match, as a result, the color of the button that later will be displayed in the main screen.
4. Click on the "Update" button at the bottom of the screen.
5. The activated button will be available for its use at the top of the main screen in the chosen color.

## Change the Quick-Call Emergency-Number

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police, Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To change/delete one or more of these emergency numbers do the following:

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. When the new popup window opens, write a new emergency number (or a non-callable number e.g. "---") in one of the text fields next to the label -- Emergency Nr. 1, 2 or 3--.
3. Click on the "Update" button at the bottom of the screen.
4. The changed emergency number button will be displayed in the button at the top of the main screen.

## Deactivate the Quick-Call Emergency-Buttons

This App comes with three (deactivated by default) buttons at the top of the main screen. Each button can be associated with an emergency number e.g.: Fire Department, Police or Medical Services, and can, once activated, be used directly from the main screen to call instantly the number they were associated with. To deactivate one or more of these buttons do the following:

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. When the new popup window opens, toggle the switch next to it to the OFF state.
3. Click on the "Update" button at the bottom of the screen.
4. The deactivated button will be displayed at the top of the main screen in grey color.

## Manually Update App

At the end of the following steps you should end up with a single and updated App installation. The update should NEVER create a duplicate of the App. If you notice a duplicate was created after the update it could mean it is not the original APK published by the developer. Uninstall the App duplicate, delete the recently downloaded APK and please inform the developer about this.

To update the App:

1. Go to https://github.com/Fe-Mu/SoS-Listener/releases and search for the "Releases" section in the column on the right side of the page and download the newest/latest App release in the official GitHub Website/Repository.
2. Go to the location where the APK was downloaded (usually the Downloads folder).
3. Tap on the downloaded APK and click on install and proceed with the installation steps that will follow. If during the installation you receive a message that there is a problem with the Signature it could mean that the App was tampered by someone else and therefore the Signatures of the original APK and the new APK do not match. In such case Android should prevent the installation since this is a security issue. In such case do not install the new APK and please inform the Developer about this.
4. After the installation your App will be updated.

## Activate/Deactivate the light-theme

1. Tap on the "Add/Manage Buttons" button in the main screen.
2. When the new popup screen opens, toggle the light-theme switch at the top of the window to the desired ON/OFF state.
3. The new theme will be automatically applied and displayed on the main screen.

## License

SoS-Listener is a multiplatform capable tool writen in Python/Kivy<br/>
language and developed by L. F. G. Muñoz ("the Author") that offers<br/>
the potential for SOS request in emergency situations.

Copyright  (C)  2025  L. F. G. Muñoz  lfgm.copyright@protonmail.com

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
