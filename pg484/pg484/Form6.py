﻿
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form6(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(141, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(111, 51)
		self._label4.TabIndex = 27
		self._label4.Text = "Saturn Jovian"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 120)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(220, 32)
		self._label3.TabIndex = 26
		self._label3.Text = "Temperacher: -180C"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(11, 91)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(259, 29)
		self._label2.TabIndex = 25
		self._label2.Text = "Mass: 5.69  x 10^26"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(11, 63)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(259, 28)
		self._label1.TabIndex = 24
		self._label1.Text = "Distance: 9.5388 AU"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(123, 48)
		self._button1.TabIndex = 23
		self._button1.Text = "Back"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Form6
		# 
		self.ClientSize = System.Drawing.Size(247, 164)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "Form6"
		self.Text = "Form6"
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		self.myparent.Show()
		self.Close()