
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent, num):
		self.InitializeComponent()
		self.myparent = parent
		self.num = num
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Intro to E- commerce",
			"The Future of the web",
			"Advanced visual basic",
			"Network Security"]))
		self._comboBox1.Location = System.Drawing.Point(13, 13)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(30, 62)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._comboBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.myparent.Show()
		self.Close()
		self.num = 0
		if self.comboBox1.Text == "Intro to E- commerce":
			self.num = 295
		if self.comboBox1.Text == "The Future of the web":
			self.num = 295
		if self.comboBox1.Text == "Advanced visual basic":
			self.num = 395
		if self.comboBox1.Text == "Network Security":
			self.num = 395
			
	def Form1FormClosing(self, sender, e):
		self.myparent.Show()