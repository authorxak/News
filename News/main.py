from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemeManager
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import  RoundedRectangularElevationBehavior

from kivy.uix.screenmanager import Screen , ScreenManager
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

import webbrowser
import requests
from  bs4 import  BeautifulSoup


kv= """
<ShowScreen>:
	MDFloatLayout:
		id:bg
		md_bg_color: 255/255,36/255,0/255,1
		Label:
		    id:lbl
	    	text:"Zero"
			font_name:"font/3.ttf"
			font_size:"100sp"
			opacity:0
			
<LogScreen>:
	on_enter:
		app.anim(mbg)
		app.anim1(mbg1)
		
	MDFloatLayout:
		
		MDFloatLayout:
			id:mbg
			pos_hint: {"center_y":1.8}
			radius: [0,0,0,40]
			canvas:
				Color:
					rgb: (1,.14,0,1)
				Rectangle:
					pos:self.pos
					size:(self.width,self.height/4.8)
					
		MDFloatLayout:
			id:mbg1
			pos_hint: {"center_y":1.8}
			radius: [0,0,0,40]
			canvas:
				Color:
					rgb: (1,.14,0,.5)
				Ellipse:
					pos: self.pos
					size:(self.width,self.height/1.5)
					
		MDIconButton:
			icon:"account-circle"
			pos_hint:{"center_x":.5,"center_y":.8}
			user_font_size:"100sp"
			theme_text_color:"Custom"
			text_color:1,1,1,1
			
		MDLabel:
			text: "Login Page"
			font_name:"font/2.ttf"
			markup: True
			pos_hint:{"center_y":.7}
			halign: "center"
			font_style: "H5"
			color:1,1,1,1
			
		MDTextField:
			id:txt
			hint_text:"Login"
			pos_hint:{"center_x":.55 , "center_y":.4}
			size_hint_x:.7
			
		MDTextField:
			id:txt1
			hint_text:"Password"
			pos_hint:{"center_x":.55 , "center_y":.3}
			size_hint_x:.7
			password: True
			
		MDIconButton:
			id:eye
			icon:"key"
			pos_hint:{"center_x":.15 , "center_y":.3}
		
		MDIconButton:
			id:circle
			icon:"account"
			pos_hint:{"center_x":.15 , "center_y":.4}
			
			
		MDFillRoundFlatButton:
			text: "sign in"
			pos_hint:{"center_x":.5 , "center_y":.2}
			size_hint_x:.8
			on_press: root.next()
		
<MenuScreen>:			
	BoxLayout:
		id:grid_banner
		orientation: "vertical"
		MDToolbar:
			id:toolbar
			title:"News - ZeroNeT"
			font_name: "font/2.ttf"
			right_action_items: [["brightness-6",lambda x: app.dots()]]
			left_action_items:[["menu", lambda x: root.nav()]]
		Button:
			text: root.texting(0)
			on_press: root.weblink(1)
			
		Button:
			text: root.texting(2)
			on_press: root.weblink(3)
		
		Button:
			text: root.texting(4)
			on_press: root.weblink(5)
			
		Button:
			text: root.texting(6)
			on_press: root.weblink(7)
			
		Button:
			text: root.texting(8)
			on_press: root.weblink(9)
			
		Button:
			text: root.texting(10)
			on_press: root.weblink(11)
			
		Button:
			text: root.texting(12)
			on_press: root.weblink(13)
			
		Button:
			text: root.texting(14)
			on_press: root.weblink(15)
			
		Button:
			text: root.texting(16)
			on_press: root.weblink(17)
		
			
<InfoScreen>:
	BoxLayout:
		orientation: "vertical"
		
		MDToolbar:
			id:toolbar
			title:"News - ZeroNeT"
			font_name: "font/2.ttf"
			right_action_items: [["brightness-6",lambda x: app.dots()]]
			left_action_items:[["home", lambda x: root.nav1()]]
			
		Image:
			source:"img/nav.jpg"
			pos_hint_y:None
				
		MDLabel:
			size_hint_y:None
			text:f"Author: [b]Zero[/b]"
			markup: True
			color:0,0,0,1
					
		MDLabel:
			size_hint_y:None
			text:f"Library: [b]Kivy/Kivymd[/b]"
			markup: True
			color:0,0,0,1
					
				
		MDRectangleFlatIconButton:
			size_hint_x:1
			text:"GitHub"
			icon:"github"
			on_press: root.link(1)
						
		MDRectangleFlatIconButton:
			size_hint_x:1
			text:"Telegram"
			icon:"telegram"
			on_press: root.link(2)
								
		MDRectangleFlatIconButton:
			size_hint_x:1
			text:"Email"
			icon:"email"
			on_press: root.link(3)
					
		Widget:

		
"""
Builder.load_string(kv)

#---------------------------------------------
	
class ShowScreen(Screen):
	
	def on_enter(self):
		anim=Animation(opacity=1,duration=3)
		anim+=Animation(opacity=0,duration=1)
		anim.start(self.ids["lbl"])
		Clock.schedule_once(self.start,6)
		
	def start(self,*args):
		self.manager.current="login"
		self.manager.transition.direction="left"
	
class LogScreen(Screen):
	def next(self):
		#if self.ids["txt"].text=="" and self.ids["txt1"].text=="":
#			self.manager.transition.direction="up"
#			self.manager.current="menu"
		self.manager.transition.direction="up"
		self.manager.current="menu"
			
			
			
			
class MenuScreen(Screen):
	try:
		resp=requests.get("https://www.bbc.com/news/world")
		soup=BeautifulSoup(resp.text,"html.parser")
		soupGo=soup.find_all("a",class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")
		list=[]
		index=0
		for i in soupGo:
			index+=1
			if index<=9:
				soup2=i.find("h3",class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")
				soup1=i.get("href")
				list.append(soup2.get_text())
				list.append("https://www.bbc.com"+soup1)
				
		news_list=list
	except:
		news_list="error"
		
	def nav(self):
		self.manager.current="info"
		self.manager.transition.direction="left"
			
	def texting(self,x):
		if self.news_list!="error":
			return str(self.news_list[x])
		else:
			return "error"
		
	def weblink(self,x):
		if self.news_list!="error":
			webbrowser.open(f"{self.news_list[x]}")
			

class InfoScreen(Screen):
	def nav1(self):
		self.manager.current="menu"
		self.manager.transition.direction="right"
		
	def link(self,x):
		if x==1:
			webbrowser.open("https://github.com/authorxak")
		elif x==2:
			webbrowser.open("https://t.me/AuthorXAK")
		elif x==3:
			webbrowser.open("mailto:boksov657@gmail.com?")


#---------------------------------------------


class BannerApp(MDApp):
	def build(self):
		self.sm=ScreenManager()
		self.sm.add_widget(ShowScreen(name="show"))
		self.sm.add_widget(LogScreen(name="login"))
		self.sm.add_widget(MenuScreen(name="menu"))
		self.sm.add_widget(InfoScreen(name="info"))
		self.theme_cls.primary_palette="Red"
		return self.sm
		
	def anim(self,box):
		anim=Animation(pos_hint={"center_y":1.4},duration=.7)
		anim.start(box)
		
	def anim1(self,box):
		anim=Animation(pos_hint={"center_y":1.1},duration=.7)
		anim.start(box)
		
	def dots(self):
		if self.theme_cls.theme_style=="Light":
			self.theme_cls.theme_style="Dark"
		else:
			self.theme_cls.theme_style="Light"
		
		
BannerApp().run()