
"""

SOS-listener is a multiplatform capable tool writen in Python/Kivy
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

import time
from time import sleep
from kivy.utils import platform
from kivy.clock import mainthread, Clock
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivymd.app import MDApp
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from plyer import sms
from plyer import call
from plyer import gps
from kivy import platform
from androidstorage4kivy import SharedStorage, Chooser

import AGPLv3
import about
import howto
import privacy
import contact
import licenses
import troubleshooting
import SoSListener_license
import json
import shutil
import os
import ast
import datetime

if platform == 'android':
    from jnius import autoclass

    Intent = autoclass("android.content.Intent")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    System = autoclass("java.lang.System")


class MainApp(MDApp):

    # Variables to manage the status of the emergency-call buttons
    status_switch_112 = BooleanProperty()
    status_switch_110 = BooleanProperty()
    status_switch_911 = BooleanProperty()
    status_light_theme = BooleanProperty()

    # app Build
    def build(self):

        self.cache = SharedStorage().get_cache_dir()  # file cache in the private storage (for cleaning purposes)

        # Screen manager and Screen creation
        self.sm = ScreenManager(transition=NoTransition())
        self.screen1 = Screen(name='s1')            # -->  "Main"                       screen
        self.screen2 = Screen(name='s2')            # -->  "More..."                    screen
        self.screen3 = Screen(name='s3')            # -->  "Restart"                    screen
        self.screen4 = Screen(name='s4')            # -->  "About"                      screen
        self.screen5 = Screen(name='s5')            # -->  "AGPLv3"                     screen
        self.screen6 = Screen(name='s6')            # -->  "How-To"                     screen
        self.screen7 = Screen(name='s7')            # -->  "Troubleshooting"            screen
        self.screen8 = Screen(name='s8')            # -->  "Privacy Policy @ Start"     screen
        self.screen9 = Screen(name='s9')            # -->  "Contact & Support"          screen
        self.screen10 = Screen(name='s10')          # -->  "Credits & Other Licenses"   screen
        self.screen11 = Screen(name='s11')          # -->  "Privacy policy"             screen

        # App theme declaration
        self.theme_cls.theme_style = 'Light'

        # Json files for storing the data the app needs for it to function
        self.store = JsonStore('data.json')
        self.store2 = JsonStore('data2.json')
        self.store3 = JsonStore('other_licenses.json')

        # Developer's donation and contact email
        donations_email = self.store2.get("donations_email")["email"]
        contact_email = self.store2.get("contact_email")["email"]


        ##############
        # PERMISSIONS
        ##############

        self.request_android_permissions()
        gps.configure(on_location=self.on_gps_location)
        gps.start(5000, 0)


        ###########
        # SWITCHES
        ###########

        # Check status of switch 112 @ Start
        if self.store2.get("disabled_112")["disable_112"] == 'no':
            self.status_switch_112 = True
        if self.store2.get("disabled_112")["disable_112"] == 'yes':
            self.status_switch_112 = False

        # Check status of switch 110 @ Start
        if self.store2.get("disabled_110")["disable_110"] == 'no':
            self.status_switch_110 = True
        if self.store2.get("disabled_110")["disable_110"] == 'yes':
            self.status_switch_110 = False

        # Check status of switch 911 @ Start
        if self.store2.get("disabled_911")["disable_911"] == 'no':
            self.status_switch_911 = True
        if self.store2.get("disabled_911")["disable_911"] == 'yes':
            self.status_switch_911 = False


        ##########
        # SCREEN 1 - Main screen
        ##########

        # Layout to place the emergency buttons
        self.layout_emergency = MDBoxLayout(size_hint=(1, .1), spacing='2dp')

        # Layout to scroll the emergency contacts
        self.layout_main_contacts = MDScrollView()

        # Layout to place the emergency contacts
        self.layout_contacts = MDBoxLayout(orientation='vertical'
                                           , size_hint=(1, 1)
                                           , adaptive_height=True
                                           )

        # Layout to contain the previous layouts of the main screen and their widgets
        self.layout_main_app = BoxLayout(orientation='vertical')

        #
        self.btn_112 = MDRaisedButton(on_press=self.call_112
                                      , text=self.store2.get("txt_nr_112")["num112"]
                                      , md_bg_color=(1, 0, .5, 1)
                                      , font_size='17dp'
                                      , size_hint=(1, 1)
                                      , disabled=not self.status_switch_112
                                      )

        self.btn_110 = MDRaisedButton(on_press=self.call_110
                                      , text=self.store2.get("txt_nr_110")["num110"]
                                      , font_size='17dp'
                                      , size_hint=(1, 1)
                                      , disabled=not self.status_switch_110
                                      )

        self.btn_911 = MDRaisedButton(on_press=self.call_911
                                      , text=self.store2.get("txt_nr_911")["num911"]
                                      , md_bg_color=(.95, .85, .1, 1)
                                      , font_size='17dp'
                                      , size_hint=(1, 1)
                                      , disabled=not self.status_switch_911
                                      )

        # Displays the current or last saved GPS position
        self.label_show_gps = MDRaisedButton(
            text='Your Latitude: ' + self.store2.get("lat")["latitude"] + '\n'
                                                                          'Your Longitude: ' + self.store2.get("lon")[
                     "longitude"]
            , font_size='17dp'
            , halign="center"
            , pos_hint={'center_x': .5, 'center_y': .5}
            , size_hint=(1, .1)
            , on_press=self.reset_gps
            , text_color='grey'
            , line_color='lightgrey'
            , md_bg_color='white'
        )

        # Button for the menu to create / modify / delete contacts
        self.btn_manager = MDRectangleFlatButton(text="Add / Manage Buttons"
                                                 , size_hint=(1, 0.1)
                                                 , font_size='17dp'
                                                 , line_color=(.85, .85, .85, 1)
                                                 , md_bg_color=(.85, .85, .85, 1)
                                                 , text_color=(.05, .75, .91, 1)
                                                 )

        # Opens popup when pressing button
        self.btn_manager.bind(on_press=self.show_popup)

        # Add widgets to the emergency layout
        self.layout_emergency.add_widget(self.btn_112)
        self.layout_emergency.add_widget(self.btn_110)
        self.layout_emergency.add_widget(self.btn_911)

        # Add widgets to the main layout
        self.layout_main_app.add_widget(self.layout_emergency)
        self.layout_main_app.add_widget(self.label_show_gps)
        self.layout_main_contacts.add_widget(self.layout_contacts)
        self.layout_main_app.add_widget(self.layout_main_contacts)
        self.layout_main_app.add_widget(self.btn_manager)

        self.info_btn = MDRectangleFlatButton(text='More...'
                                              , size_hint=(1, .1)
                                              , font_size='17dp'
                                              , on_press=self.go_to_screen2
                                              , line_color='lightgrey'
                                              , text_color=(.05, .75, .91, 1)
                                              )

        self.layout_main_app.add_widget(self.info_btn)

        # Create emergency-contact buttons for each contact's key/value in data.json
        for name in self.store:
            color = self.store.get(name)['color']

            btn_load_existing_contact = Button(text=name
                                               , font_size='20dp'
                                               , color=(0, 0, 0, 1)
                                               , background_color=color
                                               , background_normal=''
                                               , size_hint=(1, None)
                                               , height='150dp'
                                               )

            # Adds existing contacts to main layout @ app Start
            btn_load_existing_contact.bind(on_press=self.choose_popup)
            self.layout_contacts.add_widget(btn_load_existing_contact)

        # Adds main layout to screen 1
        self.screen1.add_widget(self.layout_main_app)

        # Adds screen 1 to screen manager
        self.sm.add_widget(self.screen1)


        ##########
        # SCREEN 2 - "More..." menu
        ##########

        # Layout to scroll the page
        s2_scroll = ScrollView()

        # Layout to place the widgets in this page
        s2_layout = MDGridLayout(cols=1
                                 , size_hint=(1, 1)
                                 , spacing='20dp'
                                 , padding='50dp'
                                 , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                 , md_bg_color=(.97, .97, .97, 1)
                                 )
        s4_lbl = MDRectangleFlatButton(text='About this App'
                                       , on_press=self.go_to_screen4
                                       , font_size='17dp'
                                       , size_hint=(1, 1)
                                       , text_color='grey'
                                       , line_color=(.90, .90, .90, 1)
                                       , md_bg_color='white'
                                       )
        s5_lbl = MDRectangleFlatButton(text='SOS-listener License'
                                       , on_press=self.go_to_screen5
                                       , font_size='17dp'
                                       , size_hint=(1, 1)
                                       , text_color='grey'
                                       , line_color=(.90, .90, .90, 1)
                                       , md_bg_color='white'
                                       )
        s6_lbl = MDRectangleFlatButton(text='How-To'
                                       , on_press=self.go_to_screen6
                                       , font_size='17dp'
                                       , size_hint=(1, 1)
                                       , text_color='grey'
                                       , line_color=(.90, .90, .90, 1)
                                       , md_bg_color='white'
                                       )
        s7_lbl = MDRectangleFlatButton(text='Troubleshooting'
                                       , on_press=self.go_to_screen7
                                       , font_size='17dp'
                                       , size_hint=(1, 1)
                                       , text_color='grey'
                                       , line_color=(.90, .90, .90, 1)
                                       , md_bg_color='white'
                                       )
        s9_lbl = MDRectangleFlatButton(text='Contact & Support'
                                       , on_press=self.go_to_screen9
                                       , font_size='17dp'
                                       , size_hint=(1, 1)
                                       , text_color='grey'
                                       , line_color=(.90, .90, .90, 1)
                                       , md_bg_color='white'
                                       )
        s10_lbl = MDRectangleFlatButton(text='Credits & Other Licenses'
                                       , on_press=self.go_to_screen10
                                       , font_size='17dp'
                                       , size_hint=(1, 1)
                                       , text_color='grey'
                                       , line_color=(.90, .90, .90, 1)
                                       , md_bg_color='white'
                                       )
        s11_lbl = MDRectangleFlatButton(text='Privacy Policy'
                                       , on_press=self.go_to_screen11
                                       , font_size='17dp'
                                       , size_hint=(1, 1)
                                       , text_color='grey'
                                       , line_color=(.90, .90, .90, 1)
                                       , md_bg_color='white'
                                       )
        back_to_1 = MDRectangleFlatButton(text='Back to Main'
                                          , on_press=self.go_to_screen1
                                          , font_size='17dp'
                                          , size_hint=(1, 1)
                                          , text_color='grey'
                                          , line_color=(.90, .90, .90, 1)
                                          , md_bg_color='white'
                                          )

        # Add widgets to main screen layout
        s2_layout.add_widget(s4_lbl)
        s2_layout.add_widget(s5_lbl)
        s2_layout.add_widget(s10_lbl)
        s2_layout.add_widget(s11_lbl)
        s2_layout.add_widget(s6_lbl)
        s2_layout.add_widget(s7_lbl)
        s2_layout.add_widget(s9_lbl)
        s2_layout.add_widget(back_to_1)

        # Adds main screen layout to screen 2
        s2_scroll.add_widget(s2_layout)
        self.screen2.add_widget(s2_scroll)

        # Adds screen 2 to screen manager
        self.sm.add_widget(self.screen2)


        ##########
        # SCREEN 3 - Restart
        ##########

        # Layout to scroll page
        s3_scroll = ScrollView()

        # Layout to place the widgets of this screen
        s3_layout = MDBoxLayout(orientation='vertical'
                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                , size_hint=(1, 1)
                                , adaptive_height=True
                                )
        s3_lbl = Label(text=about.txt_about + """You can now proceed to close and restart the app [b]manually[/b].

"""
                       , color='grey'
                       , size_hint_y=None
                       , valign='top'
                       , halign='left'
                       , markup=True
                       )

        # Setting the label's height with adaptive width
        s3_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s3_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s3_restart_btn = MDRaisedButton(text='Close App &\n'
                                             'Restart App'
                                        , size_hint=(.5, None)
                                        , on_press=self.restart_app
                                        , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                        )

        # Adds widgets to main screen layout
        s3_layout.add_widget(s3_lbl)
        s3_layout.add_widget(s3_restart_btn)

        # Adds main screen layout to screen 3
        s3_scroll.add_widget(s3_layout)
        self.screen3.add_widget(s3_scroll)

        # Adds screen 3 to screen manager
        self.sm.add_widget(self.screen3)


        ##########
        # SCREEN 4 - About
        ##########

        # Layout to scroll page
        s4_scroll = ScrollView()

        # Layout to place the widgets of this screen
        s4_layout = MDBoxLayout(orientation='vertical'
                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                , size_hint=(1, 1)
                                , adaptive_height=True
                                )
        s4_title_about = Label(text=about.title
                            , font_size='20dp'
                            , color='grey'
                            , size_hint_y=None
                            , valign='top'
                            , halign='center'
                            , markup=True
                            )
        s4_lbl = Label(text=about.txt_about
                       , color='grey'
                       , size_hint_y=None
                       , valign='top'
                       , halign='left'
                       , markup=True
                       )

        # Setting the label's height with adaptive width
        s4_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s4_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s4_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        s4_to_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        # Adds widgets to main screen layout
        s4_layout.add_widget(s4_to_2)
        s4_layout.add_widget(s4_title_about)
        s4_layout.add_widget(s4_lbl)
        s4_layout.add_widget(s4_to_to_2)

        # Adds main screen layout to screen 4
        s4_scroll.add_widget(s4_layout)
        self.screen4.add_widget(s4_scroll)

        # Adds screen 4 to screen manager
        self.sm.add_widget(self.screen4)


        ##########
        # SCREEN 5 - SOS-listener License
        ##########


        # Layout to scroll page
        s5_scroll = ScrollView()

        # Layout to place the widgets of this screen
        s5_layout = MDBoxLayout(orientation='vertical'
                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                , size_hint=(1, 1)
                                , adaptive_height=True
                                )
        s5_sosListener_title = Label(text=SoSListener_license.sosListener_title
                           , font_size='20dp'
                           , color='grey'
                           , size_hint_y=None
                           , valign='top'
                           , halign='center'
                           , markup=True
                           )
        s5_sosListener_license = Label(text=SoSListener_license.sosListener_license
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_title_lbl = Label(text=AGPLv3.title
                           , font_size='20dp'
                           , color='grey'
                           , size_hint_y=None
                           , valign='top'
                           , halign='center'
                           , markup=True
                           )
        s5_pre_lbl = Label(text=AGPLv3.txt_preamble
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text0_lbl = Label(text=AGPLv3.txt_0
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text1_lbl = Label(text=AGPLv3.txt_1
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text2_lbl = Label(text=AGPLv3.txt_2
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text3_lbl = Label(text=AGPLv3.txt_3
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text4_lbl = Label(text=AGPLv3.txt_4
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text5_lbl = Label(text=AGPLv3.txt_5
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text6_lbl = Label(text=AGPLv3.txt_6
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text7_lbl = Label(text=AGPLv3.txt_7
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text8_lbl = Label(text=AGPLv3.txt_8
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text9_lbl = Label(text=AGPLv3.txt_9
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text10_lbl = Label(text=AGPLv3.txt_10
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text11_lbl = Label(text=AGPLv3.txt_11
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text12_lbl = Label(text=AGPLv3.txt_12
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text13_lbl = Label(text=AGPLv3.txt_13
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text14_lbl = Label(text=AGPLv3.txt_14
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text15_lbl = Label(text=AGPLv3.txt_15
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text16_lbl = Label(text=AGPLv3.txt_16
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text17_lbl = Label(text=AGPLv3.txt_17
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )
        s5_text18_lbl = Label(text=AGPLv3.txt_18
                                  , color='grey'
                                  , size_hint_y=None
                                  , valign='top'
                                  , halign='left'
                                  , markup=True
                                  )

        # Setting the label's height with adaptive width for all labels

        s5_sosListener_title.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_sosListener_title.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_sosListener_license.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_sosListener_license.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_pre_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_pre_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text0_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text0_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text1_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text1_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text2_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text2_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text3_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text3_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text4_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text4_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text5_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text5_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text6_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text6_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text7_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text7_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text8_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text8_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text9_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text9_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text10_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text10_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text11_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text11_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text12_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text12_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text13_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text13_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text14_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text14_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text15_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text15_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text16_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text16_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text17_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text17_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s5_text18_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s5_text18_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))


        s5_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        s5_to_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        # Adds widgets to main screen layout
        s5_layout.add_widget(s5_to_to_2)
        s5_layout.add_widget(s5_sosListener_title)
        s5_layout.add_widget(s5_sosListener_license)
        s5_layout.add_widget(s5_title_lbl)
        s5_layout.add_widget(s5_pre_lbl)
        s5_layout.add_widget(s5_text0_lbl)
        s5_layout.add_widget(s5_text1_lbl)
        s5_layout.add_widget(s5_text2_lbl)
        s5_layout.add_widget(s5_text3_lbl)
        s5_layout.add_widget(s5_text4_lbl)
        s5_layout.add_widget(s5_text5_lbl)
        s5_layout.add_widget(s5_text6_lbl)
        s5_layout.add_widget(s5_text7_lbl)
        s5_layout.add_widget(s5_text8_lbl)
        s5_layout.add_widget(s5_text9_lbl)
        s5_layout.add_widget(s5_text10_lbl)
        s5_layout.add_widget(s5_text11_lbl)
        s5_layout.add_widget(s5_text12_lbl)
        s5_layout.add_widget(s5_text13_lbl)
        s5_layout.add_widget(s5_text14_lbl)
        s5_layout.add_widget(s5_text15_lbl)
        s5_layout.add_widget(s5_text16_lbl)
        s5_layout.add_widget(s5_text17_lbl)
        s5_layout.add_widget(s5_text18_lbl)
        s5_layout.add_widget(s5_to_2)

        # Adds main screen layout to screen 5
        s5_scroll.add_widget(s5_layout)
        self.screen5.add_widget(s5_scroll)

        # Adds screen 5 to screen manager
        self.sm.add_widget(self.screen5)

        ##########
        # SCREEN 6 - How-to
        ##########

        # Layout to scroll page
        s6_scroll = ScrollView()

        # Layout to place the widgets of this screen
        s6_layout = MDBoxLayout(orientation='vertical'
                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                , size_hint=(1, 1)
                                , adaptive_height=True
                                )
        s6_title_lbl = Label(text=howto.title
                           , font_size='20dp'
                           , color='grey'
                           , size_hint_y=None
                           , valign='top'
                           , halign='center'
                           , markup=True
                           )
        s6_how_to_lbl_1 = Label(text=howto.txt_how_to_1
                              , color='grey'
                              , size_hint_y=None
                              , valign='top'
                              , halign='left'
                              , markup=True
                              )
        s6_how_to_lbl_2 = Label(text=howto.txt_how_to_2
                              , color='grey'
                              , size_hint_y=None
                              , valign='top'
                              , halign='left'
                              , markup=True
                              )

        # Setting the label's height with adaptive width for all labels
        s6_title_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s6_title_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s6_how_to_lbl_1.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s6_how_to_lbl_1.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s6_how_to_lbl_2.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s6_how_to_lbl_2.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s6_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        s6_to_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        # Adds widgets to main screen layout
        s6_layout.add_widget(s6_to_to_2)
        s6_layout.add_widget(s6_title_lbl)
        s6_layout.add_widget(s6_how_to_lbl_1)
        s6_layout.add_widget(s6_how_to_lbl_2)
        s6_layout.add_widget(s6_to_2)

        # Adds main screen layout to screen 6
        s6_scroll.add_widget(s6_layout)
        self.screen6.add_widget(s6_scroll)

        # Adds screen 6 to screen manager
        self.sm.add_widget(self.screen6)


        ##########
        # SCREEN 7 - Troubleshooting
        ##########

        # Layout to scroll page
        s7_scroll = ScrollView()

        # Layout to place the widgets of this screen
        s7_layout = MDBoxLayout(orientation='vertical'
                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                , size_hint=(1, 1)
                                , adaptive_height=True
                                )
        s7_title_lbl = Label(text=troubleshooting.title
                           , font_size='20dp'
                           , color='grey'
                           , size_hint_y=None
                           , valign='top'
                           , halign='center'
                           , markup=True
                           )
        s7_troubleshooting_lbl = Label(text=troubleshooting.txt_troubleshooting
                                       , color='grey'
                                       , size_hint_y=None
                                       , valign='top'
                                       , halign='left'
                                       , markup=True
                                       )

        # Setting the label's height with adaptive width for all labels
        s7_title_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s7_title_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s7_troubleshooting_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s7_troubleshooting_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s7_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        s7_to_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        # Adds widgets to main screen layout
        s7_layout.add_widget(s7_to_to_2)
        s7_layout.add_widget(s7_title_lbl)
        s7_layout.add_widget(s7_troubleshooting_lbl)
        s7_layout.add_widget(s7_to_2)

        # Adds main screen layout to screen 7
        s7_scroll.add_widget(s7_layout)
        self.screen7.add_widget(s7_scroll)

        # Adds screen 7 to screen manager
        self.sm.add_widget(self.screen7)


        ##########
        # SCREEN 8 - SHOW PRIVACY @ Start
        ##########

        # Layout to scroll page
        self.s8_scroll = ScrollView()

        # Layout to place the widgets of this screen
        self.s8_layout = MDBoxLayout(orientation='vertical'
                                      , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                      , size_hint=(1, 1)
                                      , adaptive_height=True
                                      )
        s8_title_lbl = Label(text=privacy.title
                            , font_size='20dp'
                            , color='grey'
                            , size_hint_y=None
                            , valign='top'
                            , halign='center'
                            , markup=True
                            )
        s8_policy_lbl = Label(
            text=privacy.txt_privacy + '\n' + privacy.txt_permissions + '\n' + privacy.txt_collection + '\n' + privacy.txt_usage + '\n' + privacy.txt_deletion
            , color='grey'
            , size_hint_y=None
            , valign='top'
            , halign='left'
            , markup=True
            )

        # Setting the label's height with adaptive width for all labels
        s8_policy_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s8_policy_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s8_to_2 = MDRaisedButton(text='Continue'
                               , width='50dp'
                               , size_hint=(.5, None)
                               , on_press=self.continue_bnt
                               , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                               )

        # Adds widgets to main screen layout
        self.s8_layout.add_widget(s8_title_lbl)
        self.s8_layout.add_widget(s8_policy_lbl)
        self.s8_layout.add_widget(s8_to_2)

        # Adds main screen layout to screen 11
        self.s8_scroll.add_widget(self.s8_layout)
        self.screen8.add_widget(self.s8_scroll)

        # Adds screen 11 to screen manager
        self.sm.add_widget(self.screen8)


        ##########
        # SCREEN 9 - Contact & Support
        ##########

        #  Layout to scroll the page
        s9_scroll = ScrollView()

        # Layout to place the widgets of this screen
        s9_layout = MDBoxLayout(orientation='vertical'
                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                , size_hint=(1, 1)
                                , adaptive_height=True
                                , spacing='20dp'
                                )

        s9_title_lbl = Label(text=contact.title
                           , font_size='20dp'
                           , color='grey'
                           , size_hint_y=None
                           , valign='top'
                           , halign='center'
                           , markup=True
                           )
        s9_contact_lbl = Label(text=contact.txt_support + """
You can support the developer by sending a donation to the following Paypal address: 

    """ + donations_email + """

For any questions or feedback, please send an email to: 

    """ + contact_email + """

"""
                                       , color='grey'
                                       , size_hint_y=None
                                       , valign='top'
                                       , halign='left'
                                       , markup=True
                                       )

        # Setting the label's height with adaptive width for all labels
        s9_title_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s9_title_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s9_contact_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s9_contact_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s9_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        # Adds widgets to main screen layout
        s9_layout.add_widget(s9_title_lbl)
        s9_layout.add_widget(s9_contact_lbl)
        s9_layout.add_widget(s9_to_2)

        # Adds main screen layout to screen 9
        s9_scroll.add_widget(s9_layout)
        self.screen9.add_widget(s9_scroll)

        # Adds screen 9 to screen manager
        self.sm.add_widget(self.screen9)


        ###########
        # SCREEN 10 - Licenses
        ###########

        # Layout to scroll page
        self.s10_scroll = ScrollView()

        # Layout to place the widgets of this screen
        self.s10_layout = MDBoxLayout(orientation='vertical'
                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                , size_hint=(1, 1)
                                , adaptive_height=True
                                )
        s10_title_lbl = Label(text=licenses.title
                            , font_size='20dp'
                            , color='grey'
                            , size_hint_y=None
                            , valign='top'
                            , halign='center'
                            , markup=True
                            )
        s10_intro_lbl = Label(text="""
The packages 1 to 9 were directly installed by the Developer during the creation of this App. The packages 10 to 33 were installed automatically during the installation of packages 1 to 9.


[b][u]Licenses[/u][/b]

"""
                      , color='grey'
                      , size_hint_y=None
                      , valign='top'
                      , halign='left'
                      , markup=True
                      )

        s10_logo_lbl = Label(text="""\n\n\n
The spiral icon used for the creation of the Logo of this App was obtained from www.freepik.com from Icon Desai and can be found in the following link: https://www.freepik.com/icon/spirals_17826599#fromView=search&page=1&position=5&uuid=ee281425-2c93-4aa7-8b68-880117868be6
"""
                      , color='grey'
                      , size_hint_y=None
                      , valign='top'
                      , halign='left'
                      , markup=True
                      )

        # Setting the label's height with adaptive width for all labels
        s10_intro_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s10_intro_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s10_logo_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s10_logo_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s10_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        s10_to_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        # Adds widgets to main screen layout
        self.s10_layout.add_widget(s10_to_to_2)
        self.s10_layout.add_widget(s10_title_lbl)
        self.s10_layout.add_widget(s10_logo_lbl)
        self.s10_layout.add_widget(s10_intro_lbl)
        self.generate_licenses_page()
        self.s10_layout.add_widget(s10_to_2)

        # Adds main screen layout to Screen 10
        self.s10_scroll.add_widget(self.s10_layout)
        self.screen10.add_widget(self.s10_scroll)

        # Adds screen 10 to screen manager
        self.sm.add_widget(self.screen10)


        ###########
        # SCREEN 11 - Privacy Policy
        ###########

        # Layout to scroll page
        self.s11_scroll = ScrollView()

        # Layout to place the widgets of this screen
        self.s11_layout = MDBoxLayout(orientation='vertical'
                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                , size_hint=(1, 1)
                                , adaptive_height=True
                                )
        s11_title_lbl = Label(text=privacy.title
                            , font_size='20dp'
                            , color='grey'
                            , size_hint_y=None
                            , valign='top'
                            , halign='center'
                            , markup=True
                            )
        s11_policy_lbl = Label(text=privacy.txt_privacy+'\n'+privacy.txt_permissions+'\n'+privacy.txt_collection+'\n'+privacy.txt_usage+'\n'+privacy.txt_deletion
                      , color='grey'
                      , size_hint_y=None
                      , valign='top'
                      , halign='left'
                      , markup=True
                      )

        # Setting the label's height with adaptive width for all labels
        s11_policy_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        s11_policy_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        s11_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        s11_to_to_2 = MDRaisedButton(text='Return'
                                 , size_hint_x=None
                                 , width='50dp'
                                 , on_press=self.go_to_screen2
                                 )

        # Adds widgets to main screen layout
        self.s11_layout.add_widget(s11_to_to_2)
        self.s11_layout.add_widget(s11_title_lbl)
        self.s11_layout.add_widget(s11_policy_lbl)
        self.s11_layout.add_widget(s11_to_2)

        # Adds main screen layout to screen 11
        self.s11_scroll.add_widget(self.s11_layout)
        self.screen11.add_widget(self.s11_scroll)

        # Adds screen 11 to screen manager
        self.sm.add_widget(self.screen11)


        ###########
        # SWITCHES - Light/Dark themes
        ###########

        # Settings for the dark-theme configuration
        if self.store2.get("light_theme")["selected"] == 'no':
            self.status_light_mode = False
            self.store2.put("light_theme", selected='no')
            self.label_show_gps.md_bg_color = (.12, .12, .12, 1)
            self.label_show_gps.text_color = (.02, .91, 1, 1)
            self.label_show_gps.line_color = "grey"
            self.btn_manager.line_color = 'grey'
            self.btn_manager.md_bg_color = (.12, .12, .12, 1)
            self.btn_manager.text_color = (.02, .91, 1, 1)
            self.info_btn.line_color = 'lightgrey'
            self.info_btn.text_color = 'white'
            self.info_btn.md_bg_color = (.04, .71, 1, 1)

        # Settings for the light-theme configuration
        if self.store2.get("light_theme")["selected"] == 'yes':
            self.status_light_mode = True
            self.store2.put("light_theme", selected='yes')
            self.label_show_gps.md_bg_color = "white"
            self.label_show_gps.text_color = "grey"
            self.label_show_gps.line_color = "lightgrey"
            self.btn_manager.line_color = (.85, .85, .85, 1)
            self.btn_manager.md_bg_color = (.85, .85, .85, 1)
            self.btn_manager.text_color = (.05, .75, .91, 1)
            self.info_btn.line_color = 'lightgrey'
            self.info_btn.text_color = (.05, .75, .91, 1)
            self.info_btn.md_bg_color = 'white'

        return self.sm


        ###########
        # FUNCTIONS
        ###########

    # GPS location
    def on_gps_location(self, **kwargs):
        # kwargs["lat"] = 4.5
        # kwargs["lon"] = 9.0

        # self.gps_location = '\n'.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
        # self.gps_btn1.text = '\n'.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
        # self.gps_btn2.text = f"{kwargs['lat']}, {kwargs['lon']}"
        # self.gps_btn3.text = f" https://www.google.com/maps/search/?api=1&query={kwargs['lat']},{kwargs['lon']}"

        # self.show_gps.text = f"{kwargs['lat']}, {kwargs['lon']}"

        # Displays directly on a button the latitude and longitude coordinates from the "on_gps_location" function
        self.label_show_gps.text = 'Your Latitude:   ' + f"{kwargs['lat']}" + '\n' 'Your Longitude:  ' + f"{kwargs['lon']}"

        # Stores the latitude and longitude coordinates from the "on_gps_location" function in a json file
        self.store2.put("lat", latitude=f"{kwargs['lat']}")
        self.store2.put("lon", longitude=f"{kwargs['lon']}")

    # GPS start
    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    # GPS stop
    def stop(self):
        gps.stop()

    # Popup
    def show_popup(self, instance):

        # Layouts to contain the other layouts of show_popup and their widgets
        layout_show_popup_main = MDGridLayout(cols=1)

        # Layout for the emergency-buttons and the light/dark theme settings
        layout_top1 = MDBoxLayout(orientation='horizontal')
        layout_top2 = MDBoxLayout(orientation='horizontal')
        layout_top3 = MDBoxLayout(orientation='horizontal')
        layout_top4 = MDBoxLayout(orientation='horizontal')

        # Layout for the contact information
        layout_middle1 = MDBoxLayout(orientation='horizontal')
        layout_middle2 = MDBoxLayout(orientation='horizontal')
        layout_middle3 = MDBoxLayout( orientation='horizontal')

        # Layouts colorwheel
        layout_colorpicker = MDBoxLayout(orientation='horizontal'
                                        ,size_hint=(5,5)
                                        , padding='10dp')

        # Layout for the save, update & delete buttons to manage the new or existing emergency-contacts
        layout_bottom_popup = MDBoxLayout(size_hint=(1, None)
                                          , height='50dp'
                                          , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                          )

        # Layout for the exit popup button
        layout_exit_popup = MDBoxLayout(size_hint=(1, None)
                                        , height='50dp'
                                        , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                        )

        # Toggle button light/dark
        self.light_lbl = Label(text='Light Theme'
                               , color='lightgrey'
                               , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                               , size_hint=(1, 1)
                               )
        self.light_empty_lbl = Label(text=''
                                     , color='lightgrey'
                                     , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                     , size_hint=(0.5, None)
                                     , height='40dp'
                                     )
        self.light_switch = Switch(active=self.status_light_mode
                                   , size_hint=(0.5, 1)
                                   )
        self.light_switch.bind(active=self.light_on)

        # Fire & Medical widgets 112
        self.label_112 = Label(text='-- Emergency Nr. 1 --'
                               , color=(1, 0, .5, 1)
                               , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                               , size_hint=(1, 1)
                               )
        self.txt_input_112 = TextInput(text=""
                                       , font_size='15dp'
                                       , halign='center'
                                       , border=(4, 4, 4, 4)
                                       , multiline=False
                                       , input_filter='int'
                                       , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                       , hint_text='Enter Nr.'
                                       , background_color='lightgrey'
                                       , size_hint=(0.5, None)
                                       , height='40dp'
                                       )
        self.switch_112 = Switch(active=self.status_switch_112, size_hint=(0.5, 1))
        self.switch_112.bind(active=self.switched_112)

        # Police Widgets 110
        self.label_110 = Label(text='-- Emergency Nr. 2 --'
                               , color=(.35, .75, 1, 1)
                               , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                               , size_hint=(1, 1)
                               )
        self.txt_input_110 = TextInput(text=''
                                       , font_size='15dp'
                                       , halign='center'
                                       , border=(4, 4, 4, 4)
                                       , multiline=False
                                       , input_filter='int'
                                       , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                       , hint_text='Enter Nr.'
                                       , background_color='lightgrey'
                                       , size_hint=(0.5, None)
                                       , height='40dp'
                                       )

        self.switch_110 = Switch(active=self.status_switch_110, size_hint=(0.5, 1))
        self.switch_110.bind(active=self.switched_110)

        # Emergency widgets 911
        self.label_911 = Label(text='-- Emergency Nr. 3 --'
                               , color=(.95, .85, .1, 1)
                               , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                               , size_hint=(1, 1)
                               )
        self.txt_input_911 = TextInput(text=''
                                       , font_size='15dp'
                                       , halign='center'
                                       , border=(4, 4, 4, 4)
                                       , multiline=False
                                       , input_filter='int'
                                       , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                       , hint_text='Enter Nr.'
                                       , background_color='lightgrey'
                                       , size_hint=(0.5, None)
                                       , height='40dp'
                                       )

        self.switch_911 = Switch(active=self.status_switch_911, size_hint=(0.5, 1))
        self.switch_911.bind(active=self.switched_911)

        # Text inputs for saving, updating and deleting contacts
        self.txt_input_name = TextInput(hint_text='Enter contact name'
                                        , font_size='15dp'
                                        , border=(4, 4, 4, 4)
                                        , multiline=False
                                        , background_color='lightgrey'
                                        , size_hint=(0.5, None)
                                        , height='40dp'
                                        )
        self.txt_input_country = TextInput(hint_text='Enter a country code: e.g. 55'
                                           , font_size='15dp'
                                           , border=(4, 4, 4, 4)
                                           , multiline=False
                                           , input_filter='int'
                                           , background_color='lightgrey'
                                           , size_hint=(0.5, None)
                                           , height='40dp'
                                           )
        self.txt_input_telephone = TextInput(hint_text='Enter phone Nr.: e.g. 123456789'
                                             , font_size='15dp'
                                             , border=(4, 4, 4, 4)
                                             , multiline=False
                                             , input_filter='int'
                                             , background_color='lightgrey'
                                             , size_hint=(0.5, None)
                                             , height='40dp'
                                             )

        # Save, update, delete and cancel buttons
        self.btn_save = MDRectangleFlatButton(on_press=self.save_data
                                              , text='Save'
                                              , font_size='17dp'
                                              , size_hint=(1, 1)
                                              , line_color='lightgrey'
                                              , text_color='lightgrey'
                                              , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                              )
        self.btn_update = MDRectangleFlatButton(on_press=self.update_data
                                                , text='Update'
                                                , font_size='17dp'
                                                , size_hint=(1, 1)
                                                , line_color='lightgrey'
                                                , text_color='lightgrey'
                                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                                )
        self.btn_delete = MDRectangleFlatButton(on_press=self.delete_data
                                                , text='Delete'
                                                , font_size='17dp'
                                                , size_hint=(1, 1)
                                                , line_color='lightgrey'
                                                , text_color='lightgrey'
                                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                                )
        self.btn_backup = MDRectangleFlatButton(on_press=self.backup_contacts
                                                , text='Backup'
                                                , font_size='17dp'
                                                , size_hint=(1, 1)
                                                , line_color='lightgrey'
                                                , text_color='lightgrey'
                                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                                )
        self.btn_restore = MDRectangleFlatButton(text='Restore'
                                                , font_size='17dp'
                                                , size_hint=(1, 1)
                                                , line_color='lightgrey'
                                                , text_color='lightgrey'
                                                , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                                #, on_press=self.restore_contacts
                                                )
        self.btn_restore.bind(on_release=lambda x: Chooser(self.chooser_callback).choose_content("text/*"))

        self.btn_exit = MDRectangleFlatButton(on_press=self.close_popup
                                              , text="Exit"
                                              , halign='center'
                                              , font_size='17dp'
                                              , size_hint=(1, 1)
                                              , line_color='lightgrey'
                                              , text_color='lightgrey'
                                              , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                              , padding='0dp'
                                              )

        # Create colorpicker object
        self.colorpicker = ColorPicker(size_hint=(1, 1),
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Adds widgets to all show_popup secondary layouts
        layout_top1.add_widget(self.light_switch)
        layout_top1.add_widget(self.light_lbl)
        layout_top1.add_widget(self.light_empty_lbl)

        layout_top2.add_widget(self.switch_112)
        layout_top2.add_widget(self.label_112)
        layout_top2.add_widget(self.txt_input_112)

        layout_top3.add_widget(self.switch_110)
        layout_top3.add_widget(self.label_110)
        layout_top3.add_widget(self.txt_input_110)

        layout_top4.add_widget(self.switch_911)
        layout_top4.add_widget(self.label_911)
        layout_top4.add_widget(self.txt_input_911)

        layout_middle1.add_widget(self.txt_input_name)
        layout_middle2.add_widget(self.txt_input_country)
        layout_middle3.add_widget(self.txt_input_telephone)

        layout_bottom_popup.add_widget(self.btn_save)
        layout_bottom_popup.add_widget(self.btn_update)
        layout_bottom_popup.add_widget(self.btn_delete)
        layout_exit_popup.add_widget(self.btn_backup)
        layout_exit_popup.add_widget(self.btn_restore)
        layout_exit_popup.add_widget(self.btn_exit)

        layout_colorpicker.add_widget(self.colorpicker)

        # Adds secondary layouts to main show_popup layout
        layout_show_popup_main.add_widget(layout_top1)
        layout_show_popup_main.add_widget(layout_top2)
        layout_show_popup_main.add_widget(layout_top3)
        layout_show_popup_main.add_widget(layout_top4)
        layout_show_popup_main.add_widget(layout_middle1)
        layout_show_popup_main.add_widget(layout_middle2)
        layout_show_popup_main.add_widget(layout_middle3)
        layout_show_popup_main.add_widget(layout_colorpicker)
        layout_show_popup_main.add_widget(layout_bottom_popup)
        layout_show_popup_main.add_widget(layout_exit_popup)

        # Declares the main layout as the content of the popup
        self.popup = Popup(title='Button Manager'
                           , title_align='center'
                           , title_size='20dp'
                           , content=layout_show_popup_main
                           , size_hint=(1,1)
                           )

        # Opens the popup
        self.popup.open()

    # Choose popup
    def choose_popup(self, instance):

        # Used to get the text of the button (instance) that was pressed before
        self.called = instance.text

        layout_choose_popup = BoxLayout(orientation='vertical'
                                        , spacing="20dp"
                                        , padding="10dp"
                                        )

        # Widgets to call or send S.O.S. to a contact
        btn_call = MDRectangleFlatButton(on_press=self.call_number
                                         , text='Call'
                                         , halign='center'
                                         , font_size='17dp'
                                         , size_hint=(0.6, 0.2)
                                         , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                         , line_color=(.20, 80, .60, 1)
                                         , text_color='lightgrey'
                                         )

        btn_cancel = MDRectangleFlatButton(on_press=self.close_popup
                                           , text="Cancel"
                                           , halign='center'
                                           , font_size='17dp'
                                           , size_hint=(0.6, 0.2)
                                           , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                           , line_color='grey'
                                           , text_color='lightgrey'
                                           )

        btn_sos = MDRectangleFlatButton(on_press=self.send_sos
                                        , text="Send \nSOS"
                                        , halign='center'
                                        , font_size='17dp'
                                        , size_hint=(0.6, 0.2)
                                        , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                        , line_color='yellow'
                                        , text_color='lightgrey'
                                        )

        btn_silent_sos = MDRectangleFlatButton(on_press=self.silent_sos
                                               , text="Silent \nSOS"
                                               , halign='center'
                                               , font_size='17dp'
                                               , size_hint=(0.6, 0.2)
                                               , pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                               # ,line_color=(.67,.51,1,1)
                                               , line_color=(.80, .2, .47, 1)
                                               , text_color='lightgrey'
                                               )

        # Add widgets to popup
        layout_choose_popup.add_widget(btn_call)
        layout_choose_popup.add_widget(btn_cancel)
        layout_choose_popup.add_widget(btn_sos)
        layout_choose_popup.add_widget(btn_silent_sos)

        # Declares the main layout as the content of the popup
        self.popup = Popup(title='Touch an option'
                           , title_align='center'
                           , title_size='20dp'
                           , content=layout_choose_popup
                           , size_hint=(0.6, 0.7)
                           )

        # Opens popup
        self.popup.open()

    # Save Contact
    def save_data(self, instance):

        # Saves input information in local variables
        save_name = self.txt_input_name.text
        country = self.txt_input_country.text
        telephone = self.txt_input_telephone.text
        color = self.colorpicker.color

        # If the input name does not exist in the json file and the text field is not blank
        if save_name not in self.store and save_name is not "":

            # Save new emergency-contact in the json file
            self.store.put(save_name, country=country, telephone=telephone, color=color)

            # Creates a new button for the emergence-contact screen
            btn_add_nex_contact = Button(text=save_name
                                         , font_size='20dp'
                                         , color=(0, 0, 0, 1)
                                         , background_color=color
                                         , background_normal=''
                                         , size_hint=(1, None)
                                         , height='150dp'
                                         )

            # Applies the color that the colorpicker is showing to the button's background (default is white)
            btn_add_nex_contact.background_color = color

            # Assigns a trigger function (choose_popup) when the button is pressed
            btn_add_nex_contact.bind(on_press=self.choose_popup)

            # Adds the newly created button to the emergency-contact screen
            self.layout_contacts.add_widget(btn_add_nex_contact)

        # Closes popup
        self.popup.dismiss()

    # Update contact
    def update_data(self, instance):

        # Saves input information in local variable
        update_name = self.txt_input_name.text

        # If input name textfield is empty saves existing number in a local
        # variable otherwise it saves the input name text in a local variable
        if self.txt_input_112.text == "":
            update_112 = self.store2.get('txt_nr_112')['num112']
        else:
            update_112 = self.txt_input_112.text

        if self.txt_input_110.text == "":
            update_110 = self.store2.get('txt_nr_110')['num110']
        else:
            update_110 = self.txt_input_110.text

        if self.txt_input_911.text == "":
            update_911 = self.store2.get('txt_nr_911')['num911']
        else:
            update_911 = self.txt_input_911.text

        # Updates the emergency-numbers in json file and the labels of
        # the emergency buttons in the main screen
        self.store2.put("txt_nr_112", num112=update_112)
        self.btn_112.text = self.store2.get('txt_nr_112')['num112']

        self.store2.put("txt_nr_110", num110=update_110)
        self.btn_110.text = self.store2.get('txt_nr_110')['num110']

        self.store2.put("txt_nr_911", num911=update_911)
        self.btn_911.text = self.store2.get('txt_nr_911')['num911']

        # Checks if the input name already exists in the json file
        if self.store.exists(update_name):

            # If country textfield is empty saves existing number in a local
            # variable otherwise it saves the country text in a local variable
            if self.txt_input_country.text == "":
                country = self.store.get(update_name)['country']
            else:
                country = self.txt_input_country.text

            # If telephone textfield is empty saves existing number in a local
            # variable otherwise it saves the telephone text in a local variable
            if self.txt_input_telephone.text == "":
                telephone = self.store.get(update_name)['telephone']
            else:
                telephone = self.txt_input_telephone.text

            # If the colorpicker is white (default) it gets the existing saved color from the json file
            # variable otherwise it saves the new selected color in a local variable
            if self.colorpicker.color == [1, 1, 1, 1]:
                color = self.store.get(update_name)["color"]
            else:
                color = self.colorpicker.color

            # Updates existing contact with new information
            self.store.put(update_name, country=country, telephone=telephone, color=color)

            # Updates the existing emergency-contact button in the main screen layout
            for existing_btn in self.layout_contacts.children:
                if existing_btn.text == update_name:
                    existing_btn.text = update_name
                    existing_btn.background_color = color
                    break

        # Closes popup
        self.popup.dismiss()

    # Delete contact
    def delete_data(self, instance):

        # Saves input name text in a local variable
        delete_name = self.txt_input_name.text

        # If the input name exists in the json file it deletes it.
        # It also deletes the existing emergency-contact button in the
        # main screen layout and closes the popup at the end.
        if self.store.exists(delete_name):
            self.store.delete(delete_name)
            for existing_btn in self.layout_contacts.children:
                if existing_btn.text == delete_name:
                    self.layout_contacts.remove_widget(existing_btn)
                    break

        # Closes popup
        self.popup.dismiss()

    # Call number
    def call_number(self, instance):

        # Gets contact name from the emergency-contact button that was pressed and saves it in a local variable
        name = self.called
        if self.store.exists(name):

            # Calls the number of the selected emergency-contact
            call.makecall(tel="+" + self.store[name]['country'] + self.store[name]['telephone'])

        # Closes popup
        self.popup.dismiss()

    # SOS message
    def send_sos(self, instance):

        # Gets contact name from the emergency-contact button that was pressed and saves it in a local variable
        name = self.called
        if self.store.exists(name):

            # Sends an SOS SMS message to the selected emergency-contact
            sms.send(recipient="+" + self.store[name]['country'] + self.store[name]['telephone']
                     ,
                     message='++ Emergency-SOS ++\nI need help! , PLEASE CALL BACK! , if I do not answer please send help to my location!'
                     )

            time.sleep(1)
            sms.send(recipient="+" + self.store[name]['country'] + self.store[name]['telephone']
                     ,
                     message=f"Location:\nhttps://www.google.com/maps/search/?api=1&query={self.store2.get('lat')['latitude']},{self.store2.get('lon')['longitude']}"
                     )

            time.sleep(1)
            sms.send(recipient="+" + self.store[name]['country'] + self.store[name]['telephone']
                     ,
                     message=f"Location:\nhttps://magicearth.com/?show_on_map&lat={self.store2.get('lat')['latitude']}&lon={self.store2.get('lon')['longitude']}"
                     )

        # Closes popup
        self.popup.dismiss()

    # Silent SOS message
    def silent_sos(self, instance):

        # Gets contact name from the emergency-contact button that was pressed and saves it in a local variable
        name = self.called
        if self.store.exists(name):

            # Sends a silent SOS SMS to the selected emergency-contact
            sms.send(recipient="+" + self.store[name]['country'] + self.store[name]['telephone']
                     ,
                     message='++ Silent Emergency-SOS ++\nI need help! , DO NOT CALL BACK! , please send help to my location!'
                     )

            time.sleep(1)
            sms.send(recipient="+" + self.store[name]['country'] + self.store[name]['telephone']
                     ,
                     message=f"Location:\nhttps://www.google.com/maps/search/?api=1&query={self.store2.get('lat')['latitude']},{self.store2.get('lon')['longitude']}"
                     )

            time.sleep(1)
            sms.send(recipient="+" + self.store[name]['country'] + self.store[name]['telephone']
                     ,
                     message=f"Location:\nhttps://magicearth.com/?show_on_map&lat={self.store2.get('lat')['latitude']}&lon={self.store2.get('lon')['longitude']}"
                     )

        # Closes popup
        self.popup.dismiss()

    # Send gps
    def send_gps(self, instance):

        # Gets contact name from the emergency-contact button that was pressed and saves it in a local variable
        name = self.called
        if self.store.exists(name):

            # Sends saved gps coordinates to the selected emergency-contact
            telephone = self.store[name]['telephone']
            sms.send(recipient="+" + self.store[name]['country'] + self.store[name]['telephone']
                     ,
                     message=f" https://www.google.com/maps/search/?api=1&query={self.store2.get('lat')['latitude']},{self.store2.get('lon')['longitude']}")

    # Closes popup
    def close_popup(self, *args):
        self.popup.dismiss()

    # Android permission requests
    def request_android_permissions(self):

        from android.permissions import request_permissions, Permission, check_permission

        # Permissions that will be requested
        request_permissions([Permission.ACCESS_COARSE_LOCATION
                             ,Permission.ACCESS_FINE_LOCATION
                             ,Permission.CALL_PHONE
                             ,Permission.SEND_SMS
                             ])

    # Call 112
    def call_112(self, instance):

        # Calls the emergency-number saved in the first emergency-button
        call.makecall(tel=self.store2.get('txt_nr_112')['num112'])

    # Call 110
    def call_110(self, instance):

        # Calls the emergency-number saved in the second emergency-button
        call.makecall(tel=self.store2.get('txt_nr_110')['num110'])

    # Call 911
    def call_911(self, instance):

        # Calls the emergency-number saved in the third emergency-button
        call.makecall(tel=self.store2.get('txt_nr_911')['num911'])

    # Manages the change of state from E-button 112
    def switched_112(self, instance, value):
        if value == True:
            self.store2.put("disabled_112", disable_112="no")
            self.btn_112.disabled = False
            self.status_switch_112 = True
            return False
        else:
            self.store2.put("disabled_112", disable_112="yes")
            self.btn_112.disabled = True
            self.status_switch_112 = False
            return True

    # Manages the change of state from E-button 110
    def switched_110(self, instance, value):
        if value == True:
            self.store2.put("disabled_110", disable_110="no")
            self.btn_110.disabled = False
            self.status_switch_110 = True
            return False
        else:
            self.store2.put("disabled_110", disable_110="yes")
            self.btn_110.disabled = True
            self.status_switch_110 = False
            return True

    # Manages the change of state from E-button 911
    def switched_911(self, instance, value):
        if value == True:
            self.store2.put("disabled_911", disable_911="no")
            self.btn_911.disabled = False
            self.status_switch_911 = True
            return False
        else:
            self.store2.put("disabled_911", disable_911="yes")
            self.btn_911.disabled = True
            self.status_switch_911 = False
            return True

    # Intentional "delete" of GPS coordinates in App
    def reset_gps(self, instance):

        # Empty the saved latitude and longitude in the json file
        self.store2.put('lat', latitude="")
        self.store2.put('lon', longitude="")

        # Empty the text displayed in the button on the main app screen
        self.label_show_gps.text = ('Your Latitude: ' + self.store2.get("lat")["latitude"] + '\n'
                                                                                             'Your Longitude: ' +
                                    self.store2.get("lon")["longitude"])

    # Switch to screen1
    def go_to_screen1(self, *args):
        self.sm.current = 's1'

    # Switch to screen2
    def go_to_screen2(self, *args):
        self.sm.current = 's2'

    # Switch to screen3
    def go_to_screen3(self, *args):
        self.sm.current = 's3'

    # Switch to screen4
    def go_to_screen4(self, *args):
        self.sm.current = 's4'

    # Switch to screen5
    def go_to_screen5(self, *args):
        self.sm.current = 's5'

    # Switch to screen6
    def go_to_screen6(self, *args):
        self.sm.current = 's6'

    # Switch to screen7
    def go_to_screen7(self, *args):
        self.sm.current = 's7'

    # Switch to screen8
    def go_to_screen8(self, *args):
        self.sm.current = 's8'

    # Switch to screen9
    def go_to_screen9(self, *args):
        self.sm.current = 's9'

    # Switch to screen10
    def go_to_screen10(self, *args):
        self.sm.current = 's10'

    # Switch to screen11
    def go_to_screen11(self, *args):
        self.sm.current = 's11'

    # Continue to main screen after initial privacy policy
    def continue_bnt(self, *args):
        self.store2.put("eula", granted="yes")
        self.store2.put("permissions", granted="yes")
        self.sm.current = ('s1')

    # Checks on app start
    def on_start(self):

        if (self.store2.get("permissions")['granted'] == "no" and self.store2.get('app_restart')['restarted'] == "no"
                and self.store2.get('eula')['granted'] == "no"):
            self.sm.current = 's3'

        if (self.store2.get("permissions")['granted'] == "yes" and self.store2.get('app_restart')['restarted'] == "yes"
                and self.store2.get('eula')['granted'] == "no"):
            self.sm.current = 's8'

        if (self.store2.get("permissions")['granted'] == "yes" and self.store2.get('app_restart')['restarted'] == "yes"
                and self.store2.get('eula')['granted'] == "yes"):
            self.sm.current = 's1'

    # Restart App (for after manual closing App)
    def restart_app(self, *args):
        self.store2.put("eula", granted="no")
        self.store2.put("permissions", granted="yes")
        self.store2.put("app_restart", restarted="yes")
        if platform == 'android':
            System.exit(0)
        else:
            self.sm.clear_widgets()
            self.stop()

    # Light theme switch
    def light_on(self, instance, value):

        # Settings for the light/dark themes configuration
        if value == True:
            self.status_light_mode = True
            self.store2.put("light_theme", selected='yes')
            self.label_show_gps.md_bg_color = "white"
            self.label_show_gps.text_color = "grey"
            self.label_show_gps.line_color = "lightgrey"
            self.btn_manager.line_color = (.85, .85, .85, 1)
            self.btn_manager.md_bg_color = (.85, .85, .85, 1)
            self.btn_manager.text_color = (.05, .75, .91, 1)
            self.info_btn.line_color = 'lightgrey'
            self.info_btn.text_color = (.05, .75, .91, 1)
            self.info_btn.md_bg_color = 'white'
        else:
            self.status_light_mode = False
            self.store2.put("light_theme", selected='no')
            self.label_show_gps.md_bg_color = (.12, .12, .12, 1)
            self.label_show_gps.text_color = (.02, .91, 1, 1)
            self.label_show_gps.line_color = "grey"
            self.btn_manager.line_color = 'grey'
            self.btn_manager.md_bg_color = (.12, .12, .12, 1)
            self.btn_manager.text_color = (.02, .91, 1, 1)
            self.info_btn.line_color = 'lightgrey'
            self.info_btn.text_color = 'white'
            self.info_btn.md_bg_color = (.04, .71, 1, 1)

    # License screen generator
    def generate_licenses_page(self):

        # For each item in json file, it checks for the 'Name', 'Version',
        # 'License' and 'url' keys and saves their values in local variables
        for i in self.store3:
            text1 = self.store3.get(i)['Name']
            text2 = self.store3.get(i)['Version']
            text3 = self.store3.get(i)['License']
            text4 = self.store3.get(i)['url']

            # Assigns all values to a single all_text local variable
            all_text = i+'.\n'+text1+'\n'+text2+'\n'+text3+'\n'+text4+"\n\n"

            # Assigns the value in the all_text variable to a label
            i_lbl = Label(text= all_text
                          , color='grey'
                          , size_hint_y = None
                          , valign='top'
                          , halign='left'
                          , markup=True
                          )

            # Setting the label's height with adaptive width
            i_lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
            i_lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

            # Adds each created label to the main layout of screen 10
            self.s10_layout.add_widget(i_lbl)

    """From the antorix/KivyLoadSave GitHub repository found in: https://github.com/antorix/KivyLoadSave/tree/main"""
    def chooser_callback(self, uri_list):

        """ Callback handling the chooser """

        try:
            for uri in uri_list:
                # We obtain the file from the Android's "Shared storage", but we can't work with it directly.
                # We need to first copy it to our app's "Private storage." The callback receives the
                # 'android.net.Uri' rather than a usual POSIX-style file path. Calling the 'copy_from_shared'
                # method copies this file to our private storage and returns a normal file path of the
                # copied file in the private storage:
                self.opened_file = SharedStorage().copy_from_shared(uri)

                self.uri = uri  # just to keep the uri for future reference

        except Exception as e:
            pass

    """From the antorix/KivyLoadSave GitHub repository found in: https://github.com/antorix/KivyLoadSave/tree/main"""
    def on_resume(self):

        """ We load our file when the chooser closes and our app resumes from the paused mode """

        # Added by L.F.G Muñoz
        restore_pass = Label(text="\nNew emergency-contacts have been imported. Close and restart the App to automatically load the imported emergency-contacts."
                            , size_hint_y=None
                            , valign='top'
                            , halign='left'
                            , markup=True
                            )
        restore_problem = Label(text="Something went wrong. The emergency-contacts could not be restored."
                            , size_hint_y=None
                            , valign='top'
                            , halign='left'
                            , markup=True
                            )

        # Added by L.F.G Muñoz
        # Setting the label's height with adaptive width
        restore_pass.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        restore_pass.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        restore_problem.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        restore_problem.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        if self.opened_file is not None:

            try:

                with open(self.opened_file, "r") as file:  # we can work with this file in a normal Python way

                    # Added by L.F.G Muñoz to suit App's functionality
                    self.read_string = str(file.read()).strip()         # Read file and extract string
                    self.result = ast.literal_eval(self.read_string)    # Convert String to dictionary

                with open('data.json', 'w') as d:
                    json.dump(self.result, d)                           # Write dictionary to .json file

            except:

                # Name and content of popup changed by L.F.G Muñoz
                self.backup_popup = Popup(title='Information'
                                          , title_align='center'
                                          , title_size='20dp'
                                          , content=restore_problem
                                          , size_hint=(0.6, 0.3)
                                          )
                self.backup_popup.open()

            else:
                # Name and content of Popup changed by L.F.G Muñoz
                self.restore_popup = Popup(title='Information'
                                        , title_align='center'
                                        , title_size='20dp'
                                        , content=restore_pass
                                        , size_hint=(0.6, 0.27)
                                        )
                self.restore_popup.open()

                # Added by L.F.G Muñoz
                for name in self.store:
                    color = self.store.get(name)['color']

                    btn_load_existing_contact = Button(text=name
                                                       , font_size='20dp'
                                                       , color=(0, 0, 0, 1)
                                                       , background_color=color
                                                       , background_normal=''
                                                       , size_hint=(1, None)
                                                       , height='150dp'
                                                       )

                    # Adds existing contacts to main layout @ app Start
                    btn_load_existing_contact.bind(on_press=self.choose_popup)
                    self.layout_contacts.add_widget(btn_load_existing_contact)

                self.opened_file = None  # reverting file path back to None

                if self.cache and os.path.exists(self.cache): shutil.rmtree(self.cache)  # cleaning cache"""

    """From the antorix/KivyLoadSave GitHub repository found in: https://github.com/antorix/KivyLoadSave/tree/main"""
    # Method name change from 'save_file' to 'backup_contacts' by L.F.G. Muñoz
    def backup_contacts(self,*args):

        """ Save the contacts to device's Documents folder """

        # Added by L.F.G Muñoz
        backup_pass = Label(text="A backup of all emergency-contacts has been saved in the /Documents/SOS-listener directory."
                            , size_hint_y=None
                            , valign='top'
                            , halign='left'
                            , markup=True
                            )
        backup_problem = Label(text="Something went wrong. The backup could not be created."
                            , size_hint_y=None
                            , valign='top'
                            , halign='left'
                            , markup=True
                            )

        # Added by L.F.G Muñoz
        # Setting the label's height with adaptive width

        backup_pass.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        backup_pass.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        backup_problem.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        backup_problem.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        # Added by L.F.G Muñoz
        today = datetime.datetime.now()

        try:

            # Modified by L.F.G Muñoz to suit App's functionality
            filename = os.path.join(SharedStorage().get_cache_dir(),
                                    str(today.strftime("%Y.%m.%d"))+"_sosListener_backup.txt")  # forming the path of our new file

            with open(filename, "w") as file:  # creating the file in a normal way, but again in the private storage

            # Modified by L.F.G Muñoz to suit App's functionality
            # Save backup in the system's /Documents folder
                file.write(self.json_contacts_to_string())

            SharedStorage().copy_to_shared(private_file=filename)  # but now we can copy it to the shared storage

        except:

            # Name and content of popup changed by L.F.G Muñoz
            self.backup_popup = Popup(title='Information'
                                       , title_align='center'
                                       , title_size='20dp'
                                       , content=backup_problem
                                       , size_hint=(0.6, 0.3)
                                       )
            self.backup_popup.open()

        else:
            # Name and content of popup changed by L.F.G Muñoz
            self.backup_popup = Popup(title='Information'
                                       , title_align='center'
                                       , title_size='20dp'
                                       , content=backup_pass
                                       , size_hint=(0.6, 0.3)
                                       )
            self.backup_popup.open()

            if self.cache and os.path.exists(self.cache): shutil.rmtree(self.cache)  # cleaning cache

    # Read .json file and converts to string
    def json_contacts_to_string(self):
        with open('data.json') as f:
            d = json.load(f)
        return str(d)


if __name__ == '__main__':
    MainApp().run()
