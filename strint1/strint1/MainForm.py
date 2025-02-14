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
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Text"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 105)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(92, 32)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(118, 6)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(190, 31)
		self._textBox1.TabIndex = 6
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(118, 105)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(92, 32)
		self._button2.TabIndex = 7
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(216, 105)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(92, 32)
		self._button3.TabIndex = 8
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 61)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 9
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(118, 61)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 10
		self._label3.Text = "label3"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(320, 149)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "strint1"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		mystr = self._textBox1.Text.lower()
		for lcv in range(len(mystr)):
			for lcv2 in range(lcv + 1, len(mystr)):
				let = mystr[lcv]
				let2 = mystr[lcv2]
				if let == let2:
					self._label3.Text += ltr2 + ""
		

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""