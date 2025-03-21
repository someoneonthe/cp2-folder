import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._button10 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 34)
		self._button1.TabIndex = 0
		self._button1.Text = "Mercury"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(123, 13)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 36)
		self._button2.TabIndex = 1
		self._button2.Text = "Venus"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(13, 53)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 45)
		self._button3.TabIndex = 2
		self._button3.Text = "Earth"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(123, 52)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(104, 46)
		self._button4.TabIndex = 3
		self._button4.Text = "Mars"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(13, 104)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(104, 45)
		self._button5.TabIndex = 4
		self._button5.Text = "Jupiter"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(123, 104)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(104, 45)
		self._button6.TabIndex = 5
		self._button6.Text = "Saturn"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(13, 155)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(104, 39)
		self._button7.TabIndex = 6
		self._button7.Text = "Uranus"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(127, 155)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(100, 39)
		self._button8.TabIndex = 7
		self._button8.Text = "Neptune"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Location = System.Drawing.Point(13, 200)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(104, 33)
		self._button9.TabIndex = 8
		self._button9.Text = "Pluto"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# button10
		# 
		self._button10.Location = System.Drawing.Point(127, 200)
		self._button10.Name = "button10"
		self._button10.Size = System.Drawing.Size(100, 33)
		self._button10.TabIndex = 9
		self._button10.Text = "Quit"
		self._button10.UseVisualStyleBackColor = True
		self._button10.Click += self.Button10Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(245, 261)
		self.Controls.Add(self._button10)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "pg484"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self)
		form1.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from Form2 import *
		form2 = Form2(self)
		form2.Show()
		self.Hide()

	def Button3Click(self, sender, e):
		from Form3 import *
		form3 = Form3(self)
		form3.Show()
		self.Hide()

	def Button4Click(self, sender, e):
		from Form4 import *
		form4 = Form4(self)
		form4.Show()
		self.Hide()

	def Button5Click(self, sender, e):
		from Form5 import *
		form5 = Form5(self)
		form5.Show()
		self.Hide()

	def Button6Click(self, sender, e):
		from Form6 import *
		form6 = Form6(self)
		form6.Show()
		self.Hide()

	def Button7Click(self, sender, e):
		from Form7 import *
		form7 = Form7(self)
		form7.Show()
		self.Hide()

	def Button8Click(self, sender, e):
		from Form8 import *
		form8 = Form8(self)
		form8.Show()
		self.Hide()

	def Button9Click(self, sender, e):
		from Form9 import *
		form9 = Form9(self)
		form9.Show()
		self.Hide()

	def Button10Click(self, sender, e):
		Application.Exit()