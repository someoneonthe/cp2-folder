import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Location = System.Drawing.Point(12, 49)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(218, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 98)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 31)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(100, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(130, 31)
		self._textBox1.TabIndex = 2
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label2.Location = System.Drawing.Point(12, 72)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(218, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 12)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(81, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Radius"
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(94, 98)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(71, 31)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(171, 98)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(59, 31)
		self._button3.TabIndex = 6
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveBorder
		self.ClientSize = System.Drawing.Size(243, 140)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = 3.141592654
		num = int(self._textBox1.Text)
		cir = 2 * pi * num
		area = pi * num ** 2
		self._label1.Text = "Circumference: " + str(cir)
		self._label2.Text = "Area: " + str(area)
		

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()