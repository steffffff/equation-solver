#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
#  equationADeuxInconuesV_01.py
#  
#  Copyright 2016 stef 
#  stefan@stefanthorpe.com
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.


class main:
	def __init__(self):		
		self.mainwindow = Tkinter.Tk()#creation of main display window, and setting of its atributes
		self.mainwindow.title("résoluteur d'équasion")	
		self.mainwindow.geometry('200x280')
		self.mainwindow.configure(background='#26596A')

		
		self.equationInput1 = Tkinter.Entry(self.mainwindow,background='#BACFC1')#first input box for first equation
		self.equationInput1.grid(row=0,column=0,padx=15,pady=15)
		
		self.equationInput2 = Tkinter.Entry(self.mainwindow,background='#BACFC1')#second input box for second equation 
		self.equationInput2.grid(row=1,column=0,padx=15,pady=15)
		
		self.submitButton = Tkinter.Button(self.mainwindow, text="résoudre",command=self.readEquation)#submit button
		self.submitButton.grid(row=2,column=0,padx=15,pady=15)
		
		self.xLabel = Tkinter.Entry(self.mainwindow,background='#BACFC1')#creating labels to display result
		
		self.yLabel = Tkinter.Entry(self.mainwindow,background='#BACFC1')
		
		self.mainwindow.mainloop()#initiating main display window
		
	def readEquation(self):
		self.equation1 = self.equationInput1.get()#fetches first equation from entry box
		matchObj1 = re.match(r'^((-*)[1-9]+x.[1-9]+y)=(-*)([0-9]+)$',self.equation1)#checking if equation is in valid format
		self.equation2 = self.equationInput2.get()#fetches second equation from entry box
		matchObj2 = re.match(r'^((-*)[1-9]+x.[1-9]+y)=(-*)([0-9]+)$',self.equation2)#checking if equation is in valid format
		if matchObj1 != None and matchObj2 != None:#checking that equasion is in valid format
			self.solveEquation()#calls solving function
		else: tkMessageBox.showerror("Erreur", "veillez enter deux équasion dans le format 1x+1y=1")#shows an error if equation is not in a valid format
		
	def solveEquation(self):
		try:
			#creating the A and B matrices 
			A = numpy.array([ [int(re.search(r'(-*)[0-9]+x',self.equation1).group().replace('x','')),int(re.search(r'(-*)[0-9]+y',self.equation1).group().replace('y',''))],[int(re.search(r'(-*)[0-9]+x',self.equation2).group().replace('x','')),int(re.search(r'(-*)[0-9]+y',self.equation2).group().replace('y',''))] ])
			B = numpy.array([int(re.search(r'(?<==)(.+)$',self.equation1).group()),int(re.search(r'(?<==)(.+)$',self.equation2).group())])
			self.result = str(numpy.linalg.solve(A,B))#
			print self.result
			self.xLabel.insert(0,'x='+str(float(re.search(r'(?<=\[)(.*?)(?= )',self.result).group())))
			self.xLabel.grid(row=3,column=0,padx=15,pady=15)
			self.yLabel.insert(0,'y='+str(float(re.search(r'(?<= )(.*?)(?=\])',self.result).group())))
			self.yLabel.grid(row=4,column=0,padx=15,pady=15)
		except ValueError: tkMessageBox.showerror("Erreur", "équasion sans solution")#shows an error if equation does not have a valid solution
	
if __name__ == '__main__':
	try: import Tkinter #trying to import needed module tkinter, will fail if package python-tkinter is not installed
	except ImportError: 
		print('veillez installer une vertion résante de python-tkinter')
		quit()
	try: import tkMessageBox #trying to import needed module tkMessageBox, will fail if package python-tkMessageBox is not installed
	except ImportError: 
		print('veillez installer une vertion résante de python-tkMessageBox')
		quit()
	try: import re #trying to import the regular expresions modual, will fail if package python-re is not installed
	except ImportError: 
		print('veillez installer une vertion résante de python-re')
		quit()
	try: import numpy #trying to import numpy, will fail if package python-numpy is not installed
	except ImportError: 
		print('veillez installer une vertion résante de python-numpy')
		quit()
		
	instance = main()
