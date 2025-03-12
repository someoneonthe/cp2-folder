import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(122, 94)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 17
		self._label3.Text = "label3"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(17, 94)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 16
		self._label2.Text = "label2"
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(220, 138)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(92, 32)
		self._button3.TabIndex = 15
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(122, 138)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(92, 32)
		self._button2.TabIndex = 14
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(123, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(190, 31)
		self._textBox1.TabIndex = 13
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(16, 138)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(92, 32)
		self._button1.TabIndex = 12
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(17, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 11
		self._label1.Text = "Text"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(17, 53)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 18
		self._label4.Text = "label4"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(122, 50)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(190, 31)
		self._textBox2.TabIndex = 19
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(332, 184)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "strint2"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word1 = self._textBox1.Text.lower()
		word2 = self._textBox2.Text.lower()
		if len(word1) != len(word2):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word1)):
				c = word1[lcv]
				index = word2.index(c)
				if index == -1:
					self._label3.Text = "False"
				else:
					word2= word2[0:index] + word2[index +1:]
		self._label3.Text == str(len(word2) == 0)