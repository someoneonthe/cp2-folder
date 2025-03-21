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
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 112)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(149, 39)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(147, 188)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(64, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "lp3-2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		diamiter = int(self._textBox1.Text)
		price = 1.75 + (0.05 * diamiter * diamiter)
		self._label1.Text = "$" + str(price)