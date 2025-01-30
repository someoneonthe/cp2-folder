import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(148, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 37)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(148, 39)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 37)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(148, 66)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 37)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(148, 93)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 37)
		self._textBox4.TabIndex = 3
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 169)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(236, 39)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 214)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 36)
		self._button2.TabIndex = 5
		self._button2.Text = "Erase"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(148, 214)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 36)
		self._button3.TabIndex = 6
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 116)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(236, 50)
		self._label1.TabIndex = 7
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveBorder
		self.ClientSize = System.Drawing.Size(260, 280)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Font = System.Drawing.Font("Comic Sans MS", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		w = int(self._textBox1.Text)
		x = int(self._textBox2.Text)
		y = int(self._textBox3.Text)
		z = int(self._textBox4.Text)
		a = w + x + y + z
		self._label1.Text = str(a)

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()